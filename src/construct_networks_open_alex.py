import pandas as pd
import networkx as nx
import json
import logging
import os
import itertools

# Configure logging to both file and console
logging.basicConfig(
    filename="network_graphs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(message)s"))
logging.getLogger("").addHandler(console)

# Input CSV file and output directory for graphs
INPUT_CSV = "../data/csv/open_alex_publications.csv"
OUTPUT_DIR = "../data/graphs/open_alex/"

def build_network_for_subfield(publications):
    """
    Build a weighted collaboration network for a list of publications.
    
    Each publication contributes edges among co-authors. The weight of an edge
    indicates the number of publications in which the two authors collaborated.
    """
    G = nx.Graph()

    for _, pub in publications.iterrows():
        pub_id = pub["id"]
        try:
            # Parse the JSON string from the 'authorships' column
            authors = json.loads(pub["authorships"])
        except Exception as e:
            logging.error(f"Error parsing authorships for publication {pub_id}: {e}")
            continue

        # Only process publications with at least 2 authors
        if len(authors) < 2:
            continue

        # Add nodes for each author and collect their IDs
        author_ids = []
        for author in authors:
            a_id = author.get("id")
            a_name = author.get("name", "")
            if not a_id:
                continue
            if not G.has_node(a_id):
                # Node attribute can include the author's name
                G.add_node(a_id, label=a_name, name=a_name)
            author_ids.append(a_id)

        # For each unique pair of co-authors, add or update an edge
        for a, b in itertools.combinations(author_ids, 2):
            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)

    return G

def main():
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    logging.info("Reading CSV data...")
    try:
        df = pd.read_csv(INPUT_CSV)
    except Exception as e:
        logging.error(f"Failed to read {INPUT_CSV}: {e}")
        return

    # Group publications by subfield.
    # The 'subfield' column is stored as a JSON string.
    subfield_groups = {}
    for idx, row in df.iterrows():
        try:
            subfield_data = json.loads(row["subfield"])
            subfield_id = subfield_data.get("id", "unknown")
            # Using subfield id as key; display_name is available for logging/output.
            display_name = subfield_data.get("display_name", "unknown")
        except Exception as e:
            logging.error(f"Error parsing subfield for row {idx}: {e}")
            continue

        if subfield_id not in subfield_groups:
            subfield_groups[subfield_id] = {"display_name": display_name, "data": []}
        subfield_groups[subfield_id]["data"].append(row)

    logging.info(f"Found {len(subfield_groups)} unique subfields.")
    
    # Process each subfield group and build/save the corresponding network graph.
    for subfield_id, info in subfield_groups.items():
        display_name = info["display_name"]
        logging.info(f"Building network for subfield: {display_name} ({subfield_id}) "
                     f"with {len(info['data'])} publications")
        
        # Convert list of rows to a DataFrame for easier processing
        subfield_df = pd.DataFrame(info["data"])
        G = build_network_for_subfield(subfield_df)
        output_file = os.path.join(OUTPUT_DIR, f"{subfield_id.replace('/', '_')}_network.gexf")
        try:
            nx.write_gexf(G, output_file)
            logging.info(f"Saved network for {display_name} to {output_file} "
                         f"({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")
        except Exception as e:
            logging.error(f"Error saving network for {display_name}: {e}")

if __name__ == "__main__":
    main()
