import pandas as pd
import requests
import xml.etree.ElementTree as ET
import networkx as nx
import time
import logging
import os
import itertools
from typing import List, Tuple, Dict, Set

# Configure logging
logging.basicConfig(
    filename="network_construction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Constants
SUB_AREAS = [
    # "ai",
    # "arch",
    "bio",
    # "chi",
    "cse",
    # "data",
    # "dbis",
    # "ds",
    # "formal",
    # "graphics",
    # "hardware",
    # "ir",
    # "net",
    # "or",
    "pl",
    # "robotics",
    # "se",
    # "security",
    # "theory",
    # "vision",
]

INPUT_CSV = "../data/csv/br_cs_researchers.csv"
BASE_DBLP_URL = "https://dblp.org/pid/"
REQUEST_DELAY = 1
OUTPUT_DIR = "../data/graphs"


def parse_dblp_xml(xml_content: str) -> List[Tuple[str, List[Tuple[str, str]]]]:
    """Parse DBLP XML and extract publication groups with authors"""
    publications = []
    root = ET.fromstring(xml_content)

    for pub in root.findall(".//r/*"):
        pub_key = pub.attrib.get("key", "")
        authors = []
        for author in pub.findall(".//author[@pid]"):
            pid = author.attrib["pid"]
            name = author.text.strip() if author.text else ""
            if pid and name:
                authors.append((pid, name))
        if len(authors) >= 2 and pub_key:
            publications.append((pub_key, authors))
    return publications


def fetch_dblp_data(pid: str) -> List[Tuple[str, List[Tuple[str, str]]]]:
    """Fetch and parse DBLP data for a given PID"""
    try:
        response = requests.get(f"{BASE_DBLP_URL}{pid}.xml", timeout=10)
        response.raise_for_status()
        return parse_dblp_xml(response.content)
    except Exception as e:
        logging.error(f"Failed to fetch data for PID {pid}: {e}")
        return []


def determine_sub_area(co_pid: str, all_researchers: dict, current_sub: str) -> str:
    """Determine sub-area classification for co-authors"""
    if co_pid in all_researchers:
        sub_areas = all_researchers[co_pid]
        if current_sub in sub_areas:
            return current_sub
        if len(sub_areas) == 1:
            return sub_areas[0]
        return "multi"
    return "external"


def process_publication(
    G: nx.Graph,
    pub_key: str,
    authors: List[Tuple[str, str]],
    all_researchers: dict,
    current_sub: str,
    researcher_map: dict,
    processed_pubs: Set[str],
):
    """Process a single publication and update the network"""
    if pub_key in processed_pubs:
        return

    processed_pubs.add(pub_key)

    # First pass: ensure all authors are in the graph
    nodes = []
    for co_pid, co_name in authors:
        # Determine node attributes
        node_attrs = {
            "label": co_name,
            "name": co_name,
            "sub_area": determine_sub_area(co_pid, all_researchers, current_sub),
            "original": co_pid in researcher_map,
        }

        # Add/update node
        if not G.has_node(co_pid):
            G.add_node(co_pid, **node_attrs)
        else:
            # Update sub_area if needed
            current = G.nodes[co_pid]["sub_area"]
            new = node_attrs["sub_area"]
            if current in ["external", "multi"] and new not in [
                current_sub,
                "external",
                "multi",
            ]:
                G.nodes[co_pid]["sub_area"] = new

        nodes.append(co_pid)

    # Create/update edges with weights
    for u, v in itertools.combinations(nodes, 2):
        if u != v:
            if G.has_edge(u, v):
                G[u][v]["weight"] += 1
            else:
                G.add_edge(u, v, weight=1)


def build_subarea_network(
    sub_area: str, all_researchers: dict, df: pd.DataFrame
) -> nx.Graph:
    """Build weighted collaboration network for a specific sub-area"""
    logging.info(f"\n{'='*50}\nStarting network construction for {sub_area}\n{'='*50}")

    # Filter target sub-area researchers
    target_df = df[df["sub_areas"].apply(lambda x: sub_area in x)]
    logging.info(f"Found {len(target_df)} researchers in {sub_area} sub-area")

    # Initialize graph and tracking set
    G = nx.Graph()
    researcher_map = target_df.set_index("pid").to_dict("index")
    processed_pubs = set()

    # Add target researchers with institution info
    for pid, data in researcher_map.items():
        G.add_node(
            pid,
            label=data["researcher"],
            name=data["researcher"],
            institution=data["institution"],
            sub_area=sub_area,
            original=True,
        )

    # Process each target researcher's publications
    for idx, pid in enumerate(researcher_map.keys(), 1):
        logging.info(
            f"Processing {sub_area} researcher {idx}/{len(researcher_map)}: {pid}"
        )
        time.sleep(REQUEST_DELAY)

        # Get publications from DBLP
        publications = fetch_dblp_data(pid)

        # Process each publication
        for pub_key, authors in publications:
            process_publication(
                G,
                pub_key,
                authors,
                all_researchers,
                sub_area,
                researcher_map,
                processed_pubs,
            )

    return G


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load researcher data
    logging.info("Loading researcher dataset")
    df = pd.read_csv(INPUT_CSV)
    df["sub_areas"] = df["sub_areas"].apply(eval)
    all_researchers = df.set_index("pid")["sub_areas"].to_dict()

    # Process all sub-areas
    for sub_area in SUB_AREAS:
        try:
            start_time = time.time()
            network = build_subarea_network(sub_area, all_researchers, df)

            # Save network
            output_file = os.path.join(OUTPUT_DIR, f"{sub_area}_network.gexf")
            nx.write_gexf(network, output_file)

            duration = time.time() - start_time
            logging.info(
                f"Completed {sub_area} in {duration:.1f}s: "
                f"{network.number_of_nodes()} nodes, "
                f"{network.number_of_edges()} edges"
            )

        except Exception as e:
            logging.error(f"Failed to process {sub_area}: {str(e)}")
            continue


if __name__ == "__main__":
    main()
