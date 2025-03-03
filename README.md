# Collaboration Network Analysis Documentation

This repository contains code and data to analyze academic collaborations, focusing on building networks of co-authorships from publication data. Below is a detailed overview of the data, network structure, and script functionality.

---

## 📁 Data Description

### `br_publications.csv`  
This CSV file contains metadata for academic publications. Below are its columns and their descriptions:

| Column Name           | Description                                                                                                      | Format/Example                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `id`                  | Unique identifier for the publication.                                                                           | `W2928842276`                                                                                  |
| `doi`                 | Digital Object Identifier (DOI) of the publication.                                                             | `10.1016/j.patrec.2019.03.022`                                                                 |
| `title`               | Title of the publication.                                                                                        | `"A novel deep learning based framework for the detection and classification of breast cancer"` |
| `publication_year`    | Year the publication was released.                                                                               | `2019`                                                                                         |
| `authorships`         | List of authors in JSON format, including their IDs, names, institutions, and countries.                        | JSON string with nested fields (see example below).                                            |
| `subfield`            | Subfield of the publication in JSON format (e.g., `Artificial Intelligence`).                                   | `{"id": "subfields/1702", "display_name": "Artificial Intelligence"}`                          |
| `cited_by_count`      | Total number of citations the publication has received.                                                         | `685`                                                                                          |
| `counts_by_year`      | JSON object listing yearly citation counts for the past 7 years.                                                 | `{"6_year": 8, "5_year": 96, ..., "0_year": 26}`                                               |
| `primary_topic`       | Primary research topic of the publication (if available).                                                       | `{'id': 'T10862', 'display_name': 'AI in cancer detection'}`                                   |

#### Example `authorships` Entry:
```json
[
  {
    "id": "A5112426596",
    "name": "SanaUllah Khan",
    "institutions": [{"id": "I206573129", "display_name": "Islamia College University"}],
    "countries": ["PK"]
  }
]
```

## 🌐 Collaboration Network Structure

The script generates a **collaboration network** in GEXF format, where:  
- **Nodes** represent authors.  
- **Edges** represent collaborations between authors (co-authorship in a publication).  

### Node Attributes
| Attribute | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| `label1`  | Country code of the author's primary institution (e.g., `PK`, `BR`, `US`). |
| `label2`  | Author's primary subfield (e.g., `Artificial Intelligence`).               |

### Edge Attributes
| Attribute | Description                                      |
|-----------|--------------------------------------------------|
| `weight`  | Number of times two authors collaborated.        |

### Example GEXF Snippet
```xml
<node id="A5076776322" label="A5076776322">
  <attvalues>
    <attvalue for="0" value="BR" />                 <!-- Country -->
    <attvalue for="1" value="Artificial Intelligence" />  <!-- Subfield -->
  </attvalues>
</node>
<edge source="A5076776322" target="A5112426596" weight="1" />
```

## 📜 Script Functionality

The script processes the CSV data to build a collaboration network and supports filtering publications by subfield, citations, or year.

### Key Steps:
1. **Parse Data**:  
   - Extract author details (IDs, countries) and subfields from JSON-formatted columns.
   - Track each author's subfield activity (e.g., how many times they published in `Artificial Intelligence`).

2. **Build Network**:  
   - Create nodes for authors with attributes:  
     - `label1`: First country listed in their institution data.  
     - `label2`: Subfield they publish in most frequently.  
   - Add edges between co-authors, weighted by the number of shared publications.

3. **Filter Data (Optional)**:  
   - Use helper functions to filter publications by:  
     - Subfield (e.g., `Artificial Intelligence`).  
     - Minimum citation count.  
     - Publication year.

### Example Workflow:
```python
# Load data
df = pd.read_csv("../data/csv/openalex/br_publications.csv")

# Optional: Filter publications
df_filtered = filter_subfielf_publications(df, "Artificial Intelligence")
df_filtered = filter_publications_by_citation_count(df_filtered, 100)

# Build the collaboration network
G = build_collaboration_network(df_filtered)

# Save to GEXF
nx.write_gexf(G, "collaboration_network.gexf")