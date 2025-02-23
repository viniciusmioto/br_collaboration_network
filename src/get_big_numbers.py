import requests
import csv
from time import sleep

COUNTRY_CODES = [
    "CN",
    "US",
    "ID",
    "IN",
    "GB",
    "DE",
    "JP",
    "RU",
    "CA",
    "FR",
    "KR",
    "BR",
    "IT",
    "ES",
    "AU",
]


def get_count(url):
    """Makes a GET request to the given URL and returns the count from the response metadata."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        total_publications = data.get("meta", {}).get("count", 0)
        citations_count = data.get("meta", {}).get("cited_by_count_sum", 0)

        return total_publications, citations_count
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return 0


def main():
    results = []
    rank = 1

    for country in COUNTRY_CODES:
        # Build the API endpoint using the country code
        works_url = (
            f"https://api.openalex.org/works?page=1&"
            f"filter=primary_topic.field.id:fields/17,publication_year:2019+-+2024,type:types/article|types/book-chapter,"
            f"authorships.countries:{country}&cited_by_count_sum=true&per_page=1"
        )

        total_publications, citations_count = get_count(works_url)

        results.append(
            {
                "rank": rank,
                "country": country,
                "total_publications": total_publications,
                "citation_count": citations_count,
                # ration two decimal places
                "ratio": round(citations_count / total_publications, 2) if total_publications > 0 else 0,
            }
        )

        rank += 1
        sleep(1)

    # Sort the results by total publications (descending order)
    results.sort(key=lambda x: x["total_publications"], reverse=True)

    # Write results to CSV
    output_file = "../data/csv/big_numbers.csv"
    try:
        with open(output_file, "w", newline="") as csvfile:
            fieldnames = ["rank", "country", "total_publications", "citation_count", "ratio"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in results:
                writer.writerow(row)
        print(f"Data successfully written to {output_file}")
    except Exception as e:
        print(f"Error writing CSV file: {e}")


if __name__ == "__main__":
    main()
