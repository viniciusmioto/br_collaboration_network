import pandas as pd
import logging

# Configure logging to write messages to a file
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# List of sub-areas to process
sub_areas = [
    "ai",
    "arch",
    "bio",
    "chi",
    "cse",
    "data",
    "dbis",
    "ds",
    "formal",
    "graphics",
    "hardware",
    "ir",
    "net",
    "or",
    "pl",
    "robotics",
    "se",
    "security",
    "theory",
    "vision",
]


def main():
    logging.info("Script execution started.")

    # Load the main researchers dataset
    main_url = "https://raw.githubusercontent.com/aserg-ufmg/CSIndex/refs/heads/master/data/all-researchers.csv"
    logging.info(f"Loading main dataset from {main_url}")
    try:
        df = pd.read_csv(main_url, names=["researcher", "institution", "pid"])
        # Initialize sub_areas as lists
        df["sub_areas"] = [[] for _ in range(len(df))]
        initial_count = len(df)
        logging.info(f"Initial dataset contains {initial_count} researchers")
    except Exception as e:
        logging.error(f"Failed to load main dataset: {e}")
        return

    # Base URL for sub-area CSV files at a specific commit
    base_url = "https://raw.githubusercontent.com/aserg-ufmg/CSIndex/1082747ff0dbf524e2fe81bc343041bd95fcf1b4/data/"

    # Process each sub-area to find matching researchers
    for sub_area in sub_areas:
        csv_url = f"{base_url}{sub_area}-out-profs-list.csv"
        logging.info(f"Processing sub-area '{sub_area}': {csv_url}")

        try:
            # Read sub-area CSV
            sub_df = pd.read_csv(csv_url, names=["researcher", "institution"])
            sub_set = set(zip(sub_df["researcher"], sub_df["institution"]))
            logging.info(f"Sub-area '{sub_area}' has {len(sub_df)} entries.")

            # Check each researcher in the main DataFrame for a match
            matches = 0
            for idx, row in df.iterrows():
                key = (row["researcher"], row["institution"])
                if key in sub_set:
                    df.at[idx, "sub_areas"].append(sub_area)
                    matches += 1

            logging.info(f"Found {matches} matches for sub-area '{sub_area}'.")

        except Exception as e:
            logging.error(f"Error processing sub-area '{sub_area}': {e}")
            continue

    # Filter out researchers with no sub-area matches
    logging.info(f"Total researchers before filtering: {len(df)}")
    df = df[df["sub_areas"].apply(len) > 0]
    logging.info(f"Total researchers after filtering: {len(df)}")

    # Save the enriched dataset
    output_file = "br_cs_researchers.csv"
    try:
        df.to_csv(output_file, index=False)
        logging.info(f"Dataset saved to {output_file}")
    except Exception as e:
        logging.error(f"Failed to save dataset: {e}")

    logging.info("Script execution completed.")


if __name__ == "__main__":
    main()
