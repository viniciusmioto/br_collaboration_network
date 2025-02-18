import pandas as pd
import networkx as nx
import json
import logging
import os
import itertools

# Configure logging to file and console
logging.basicConfig(
    filename="full_network.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(message)s"))
logging.getLogger("").addHandler(console)

# Input CSV file and output file for the full network
INPUT_CSV = "../data/csv/open_alex_publications.csv"
OUTPUT_FILE = "../data/graphs/open_alex/full_network.gexf"

def build_full_network(df: pd.DataFrame) -> nx.Graph:
    """
    Builds a full weighted collaboration network from the CSV data.
    Nodes represent authors and edges indicate coauthorship (with weight as frequency).
    For each author, the subfield attribute is set to the most common subfield 
    (display_name) encountered across their publications.
    """
    G = nx.Graph()
    # Dictionary to store subfield frequency per author: {author_id: {subfield: count}}
    author_subfields = {}

    for idx, row in df.iterrows():
        pub_id = row["id"]

        try:
            authors = json.loads(row["authorships"])
        except Exception as e:
            logging.error(f"Error parsing authorships for publication {pub_id}: {e}")
            continue

        try:
            subfield_data = json.loads(row["subfield"])
            subfield_display = subfield_data.get("display_name", "unknown")
        except Exception as e:
            logging.error(f"Error parsing subfield for publication {pub_id}: {e}")
            subfield_display = "unknown"

        author_ids = []
        for author in authors:
            a_id = author.get("id")
            a_name = author.get("name", "")
            if not a_id:
                continue

            # Add node if it doesn't exist
            if not G.has_node(a_id):
                G.add_node(a_id, label=a_name, name=a_name)
                author_subfields[a_id] = {}
            # Update the subfield frequency count for the author
            author_subfields[a_id][subfield_display] = author_subfields[a_id].get(subfield_display, 0) + 1

            author_ids.append(a_id)

        # Add/update edges between each pair of co-authors
        for a, b in itertools.combinations(author_ids, 2):
            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)

    # For each node, assign the most common subfield from its publications
    for a_id in G.nodes():
        counts = author_subfields.get(a_id, {})
        if counts:
            # Pick the subfield with the highest frequency
            most_common_subfield = max(counts.items(), key=lambda item: item[1])[0]
        else:
            most_common_subfield = "unknown"
        G.nodes[a_id]["sub_field"] = most_common_subfield

    return G

def main():
    logging.info("Reading CSV data...")
    try:
        df = pd.read_csv(INPUT_CSV)
    except Exception as e:
        logging.error(f"Error reading CSV file {INPUT_CSV}: {e}")
        return
    logging.info(f"Loaded {len(df)} publications.")

    logging.info("Building the full collaboration network...")
    full_network = build_full_network(df)
    logging.info(f"Network constructed with {full_network.number_of_nodes()} nodes "
                 f"and {full_network.number_of_edges()} edges.")

    logging.info("Saving the network to GEXF file...")
    try:
        nx.write_gexf(full_network, OUTPUT_FILE)
        logging.info(f"Full network saved successfully to {OUTPUT_FILE}.")
    except Exception as e:
        logging.error(f"Error saving network to file: {e}")

if __name__ == "__main__":
    main()