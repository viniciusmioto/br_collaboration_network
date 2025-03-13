# Fundalmentals of Collaboration Networks 

## newman_2001_scientific_collaboration_networks_i.pdf

- **Research questions or problems:** Analyzes **scientific collaboration networks** in physics, biomedical research, and computer science, focusing on statistical properties like authorship trends and clustering.
- **Approach or methodology:** Constructs **co-authorship networks** from bibliographic databases (1995–1999), analyzing **degree distribution, clustering, and connected components**.
- **Data sources:** **Medline, Los Alamos e-Print Archive, SPIRES, NCSTRL** (1995–1999).
- **Results and conclusions:** Collaboration patterns vary by field, with **power-law distributions in authorship**, strong clustering, and the presence of a **giant connected component**.

## newman_2001_scientific_collaboration_networks_ii.pdf

- **Research questions or problems:** Extends prior work to analyze **nonlocal properties** like typical distances, centrality, and collaboration strength.
- **Approach or methodology:** Computes **shortest paths, betweenness centrality**, and introduces a **weighted collaboration network** based on shared papers.
- **Data sources:** Same as **Newman (2001) Part I**.
- **Results and conclusions:** Scientific networks exhibit a **small-world effect**, **funneling phenomenon**, and **central figures with high betweenness**. Weighted networks offer a better representation of collaboration strength.

## newman_2004_coauthorship_networks.pdf

- **Research questions or problems:** Provides an overview of **co-authorship networks across biology, physics, and mathematics**, examining collaboration trends, Erdős numbers, and preferential attachment.
- **Approach or methodology:** Constructs **co-authorship networks** and compares statistical properties across fields, analyzing clustering, network distances, and collaboration strength.
- **Data sources:** **Medline (biology), Physics E-print Archive, Mathematical Reviews** (1940–1999).
- **Results and conclusions:** Collaboration patterns vary significantly by field, with biology showing the highest co-authorship rates. Preferential attachment is evident, and the largest connected component spans most of each network.

## barabasi_2002_evolution_social_network.pdf

- **Research questions or problems:** Examines the **evolution and topology of complex evolving networks**, using the co-authorship network of scientists in mathematics and neuroscience as a prototype. Investigates scale-free properties, preferential attachment, and network evolution.
- **Approach or methodology:** Combines **empirical measurements, modeling, and numerical simulations** to study degree distribution, clustering coefficient, and network evolution over time.
- **Data sources:** **Mathematics (M) and neuroscience (NS)** journal databases from **1991–98**, covering **70,975 mathematics authors** and **209,293 neuroscience authors**.
- **Results and conclusions:** Co-authorship networks are **scale-free**, governed by **preferential attachment**, with **increasing average degree** and **decreasing node separation**. Internal links significantly influence network structure.

## elmacioglu_2005_six_degrees_of_separation.pdf

- **Research questions or problems:** Studies **collaboration networks of database researchers** from DBLP to analyze publication behavior, average distance, and clustering patterns. Tests the "six degrees of separation" hypothesis.
- **Approach or methodology:** Uses **social network analysis** on a **co-authorship network**, tracking average path length, collaboration frequency, clustering coefficient, and Lotka's Law.
- **Data sources:** **DBLP database (1968–2003)**, including **32,689 authors and 38,773 papers**.
- **Results and conclusions:** The network exhibits a **stable average distance of ~6**, follows **Lotka’s Law (power-law distribution ~-2.15)**, and shows increasing collaboration frequency and clustering.


## madaan_evolution_collaboration_2014.pdf

- **Research questions or problems:** Examines the **long-term evolution of the DBLP collaboration network**, analyzing changes in authorship, degree distribution, and clustering.
- **Approach or methodology:** Uses **social network analysis with NetworkX** to analyze annual trends (1936–2013) in co-authorship networks, applying **Lotka’s Law, Lorenz curve, and Gini coefficient**.
- **Data sources:** **DBLP Computer Science dataset (1936–2013)**, covering **2.4 million papers and 1.3 million authors**.
- **Results and conclusions:** **Collaboration is increasing**, with a decrease in single-author papers, increasing average authors per paper, and a growing giant connected component. Inequality in collaboration is rising.

# International Collaborations

## cheng_2016_exploring_university.pdf

- **Research questions or problems:**
  - Examine research collaboration between universities and industry (UI) in computer science.
  - Understand the impact of individual countries on international UI collaboration.
  - Investigate UI collaborative papers at global and country levels.

- **Approach or methodology:**
  - Used bibliometric methods to analyze computer science journal papers indexed in the Science Citation Index (SCI).
  - Calculated centrality measures (density, degree, betweenness, closeness) of UI collaborative networks.
  - Applied an independent sample t-test to compare UI papers with other computer science papers.

- **Databases or data sources:**
  - Data from computer science journal articles published between 2002 and 2011.
  - Indexed in the SCI and collected from Journal Citation Reports (JCR) and Web of Science (WOS) databases.
  - 12,713 papers from 18 top journals in "hardware and architecture" and "software engineering."

- **Results and conclusions:**
  - Global increase in UI papers with a stable collaboration ratio.
  - UI papers had a higher average number of authors than other papers.
  - International UI collaboration intensified, particularly with the USA as the dominant partner.
  - Country-specific preferences for international or domestic collaborations were observed.

## garcia_2014_analysing_the_coauthorship.pdf

- **Research questions or problems:**
  - Analyze coauthorship networks of Latin American Computer Science research groups.
  - Understand the topological structure of the networks and their evolution over time.
  - Identify influential authors based on complex network metrics.

- **Approach or methodology:**
  - Bibliometric analysis of coauthorship networks using complex network metrics (degree, closeness, betweenness centrality).
  - Defined research networks as groups of authors who published together at least five papers over a decade.

- **Databases or data sources:**
  - Data collected from DBLP (Digital Bibliography & Library Project) for 1994-2013.
  - 35 institutions from Latin America, forming a coauthorship network of 15,601 vertices and 24,722 edges.

- **Results and conclusions:**
  - Significant increase in publications and collaborations in Latin America from 2004-2013.
  - Identified influential authors through centrality metrics.
  - International collaborations were primarily between Brazil-Chile and Argentina-Brazil, though diversity in collaborations grew.

## guan_2004_comparative_study_research.pdf

- **Research questions or problems:**
  - Compare the research performance in computer science across the USA, Germany, UK, Japan, India, and China.
  - Analyze quantitative distribution and growth of publications, collaboration patterns, and research impact.

- **Approach or methodology:**
  - Employed scientometric indicators to compare research output (number of publications, Activity Index, Co-authorship Index, Normalized Impact Factor).

- **Databases or data sources:**
  - INSPEC database (1993-2002) with 9,632 computer science papers.
  - Journal Impact Factor data from Journal Citation Report (JCR).

- **Results and conclusions:**
  - USA had a dominant position in computer science publications.
  - China's rapid increase in publications was largely in domestic journals, resulting in lower international visibility.
  - Co-authorship patterns revealed differences in author collaboration preferences between Western countries and China.

## haunschild_use_openalex_bibliometric_2024.pdf

- **Research questions or problems:**
  - Explore the use of OpenAlex to create bibliometric global overlay maps.
  - Visualize research output of entities (authors, institutions) in the broader science system and normalize overlay data for comparisons.

- **Approach or methodology:**
  - Used bibliometric analysis and information visualization with VOSviewer for clustering.
  - SQL queries were used to extract citation data from OpenAlex and generate overlay maps.

- **Databases or data sources:**
  - OpenAlex snapshot from August 2023, covering publications from 1800 to 2022.

- **Results and conclusions:**
  - Demonstrated six global base maps with overlay maps for individual authors and research institutions.
  - Raw overlay maps emphasized high-level concepts, while normalized maps highlighted specific research areas.
  - OpenAlex proves useful for creating meaningful bibliometric maps, though data accuracy affects map quality.

## luukkonen_1993_measurement_of_international.pdf

- **Research questions or problems:**
  - Discuss methodology for measuring international scientific collaboration (ISC) between countries.
  - Explore different methods of analyzing ISC through bibliometric data and highlight the importance of both absolute and relative measures.

- **Approach or methodology:**
  - Discussed various approaches for measuring ISC, including integer vs. fractional counting and measures of relatedness like Salton's and Jaccard’s measures.
  - Emphasized the use of observed vs. expected numbers of collaborative papers.

- **Databases or data sources:**
  - Data from the 30 largest countries in terms of scientific papers (1981-1986) across all scientific fields, using bibliometric databases.

- **Results and conclusions:**
  - Concluded that both absolute and relative measures are essential for ISC analysis.
  - Absolute measures identify major collaborative countries, while relative measures normalize data for size differences.
  - Suggested using mapping techniques to visualize ISC networks based on collaboration numbers.

## niu_2014_network_structure_distribution.pdf

- **Research questions or problems:**
  - Investigate the scale of Chinese international research collaboration (IRC).
  - Identify collaborating countries, research fields, and key journals for Chinese IRC articles.

- **Approach or methodology:**
  - Applied bibliometric and social network methods to analyze international co-authored articles involving China.
  - Used statistical grouping to analyze journal distribution and identified core journals for each research field.

- **Databases or data sources:**
  - Data from Web of Science (WoS) covering 211,946 articles (2002-2011) with at least one author from China.

- **Results and conclusions:**
  - Significant increase in the number of Chinese IRC articles, particularly in physical sciences.
  - China collaborated primarily with scientifically advanced countries, accounting for over 80% of IRC articles.
  - Identified core journals in 22 ESI fields and analyzed the distribution of journals and articles.


## pessoa_jr_2022_a_geographic_analysis.pdf

- **Research questions or problems:**
  - Conduct a geographic analysis of interdisciplinary collaborations within the Brazilian scientific community.
  - Examine collaboration patterns across eight knowledge areas and five geographic regions of Brazil.

- **Approach or methodology:**
  - Analyzed coauthorship networks with a focus on interdisciplinary collaborations.
  - Generated collaboration identifiers based on publication titles to map interdisciplinary patterns.

- **Databases or data sources:**
  - Data from the CNPq’s Lattes Platform covering 263,264 Brazilian researchers and over 10 million publications.
  - Demographic data from IBGE and graduate program information from CAPES.

- **Results and conclusions:**
  - Detailed analysis of interdisciplinary collaboration across Brazil's geographic regions and knowledge areas.
  - Found patterns linked to economic disparities and the concentration of research excellence.

## wainer_2009_scientific_production.pdf

- **Research questions or problems:**
  - Compare scientific production in computer science across Brazil, Latin America, BRIC nations, and other relevant countries.
  - Compare publication ratios between journals and conferences and analyze sub-area distributions.

- **Approach or methodology:**
  - Quantitative analysis using publication data from ISI Web of Science and Scopus.
  - Compared countries based on publication numbers, distribution across sub-areas, and journal impact factors.

- **Databases or data sources:**
  - Data from ISI Web of Science (2001-2005) and Scopus.
  - 352 ISI computer science journals and 454 Scopus journals included in the study.

- **Results and conclusions:**
  - Brazil had the largest computer science production in Latin America but lagged behind major countries like the USA and China.
  - Brazil's publication distribution was similar to India and Russia, but with significant differences in conference and journal publication ratios.

## okamura_century_global_collaboration_2023.pdf

- **Research questions or problems:**  
This paper examines the **evolution of international scientific collaboration over the past half-century**, using large-scale bibliometric data. It explores:
  - How **international collaboration clusters have formed and changed** over time.
  - The shifting role of **top-tier countries**, particularly the **United States and China**, in global research collaboration.
  - The phenomenon of a **“Shrinking World”**, where research collaboration has increased globally, leading to tighter integration between countries.

- **Approach or methodology:**  
  - The study employs **bibliometric analysis using OpenAlex**, an open bibliometric database.
  - It applies **hierarchical clustering analysis (HCA)** to identify and visualize **collaboration clusters** for different scientific disciplines.
  - **Jaccard distance-based metrics** are used to quantify the proximity between countries in terms of their co-authored research outputs.
  - It introduces the **International Coupling Distance (ICD)** as a measure of collaboration intensity over time.

**Databases or data sources:**  
  - **OpenAlex API**, a fully open bibliographic database launched in 2022, replacing Microsoft Academic Graph (MAG).
  - OpenAlex compiles metadata from **CrossRef, ORCID, ROR, PubMed, arXiv, and Zenodo**.
  - The study uses data on **239 million works**, including journal articles, conference papers, preprints, and book chapters.

**Results and conclusions:**  
  - **China's dramatic rise in research output** is evident across multiple disciplines, surpassing the United States in areas like **Artificial Intelligence, Quantum Science, and Biotechnology**.
  - The **United States and China moved closer together in research collaboration for decades but began moving apart after 2019**, likely due to geopolitical tensions.
  - **Collaboration rates have increased globally**, with Europe maintaining high levels of international cooperation.
  - A **hierarchical clustering analysis** reveals **distinct international collaboration clusters**, showing a gradual reorganization of research alliances.
  - The **“Shrinking World” phenomenon** is supported by a decline in the **International Coupling Distance (ICD)**, indicating increased international collaboration over time.
  - The study emphasizes that **open bibliometrics platforms like OpenAlex provide a viable alternative** to commercial databases and enhance transparency in scientometric research.


---

# Interdisciplinary Computer Science

## bird_2009_structure_and_dynamics.pdf

- **Research questions or problems:**
  - Study the **complex network of collaboration relationships** in computer science.
  - Quantify informal differences between research areas and investigate collaboration patterns at various levels.
  - Examine the **interdisciplinary nature** of research areas and explore whether there are **well-defined sub-areas**.

- **Approach or methodology:**
  - **Collaboration graph extracted from the DBLP bibliographic database** with additional **extrinsic data** for defining research areas.
  - Applied **network analysis methods** including **topological measures**, **community structure analysis**, **betweenness centralization**, and **longitudinal assortativity**.
  - Performed **principal component analysis** and studied **author overlap and migration patterns** across areas.

- **Databases or data sources:**
  - Primary data from the **DBLP bibliographic database** (XML dump, February 4th, 2008).
  - **Extrinsic data** manually validated for research area definitions.

- **Results and conclusions:**
  - Found **significant differences in collaboration patterns** among research areas.
  - Identified that **PL and SE are interdisciplinary**, while **AI and ARCH are not**.
  - **Databases (DB) is well-integrated**, while **SE is fragmented**.
  - Presented empirical evidence supporting some computer science folklore.
  - Network analysis highlighted subtle properties of collaboration beyond basic distributions.


## franceschet_2011_collaboration_computer.pdf

- **Research questions or problems:**
  - Study **collaboration in computer science** from a **network science perspective**, focusing on bibliometric properties like **discipline size**, **scholar productivity**, and **collaboration levels**.
  - Examine **global network properties** like **reachability**, **separation distance**, **resilience**, **clustering**, and **assortativity** over time since 1960.

- **Approach or methodology:**
  - Built **networks of collaboration** based on co-authorship, including **affiliation networks** and **author-author collaboration networks**.
  - Used **network science metrics** like **degree distribution**, **transitivity coefficient**, and **clustering coefficient**.
  - Conducted **longitudinal analysis** of networks from 1960 to 2008.

- **Databases or data sources:**
  - Data from **DBLP bibliographic database** (XML version downloaded in early 2010).
  - Analyzed publications from **1936 to 2008**, focusing on **1960 to 2008** for temporal analysis.

- **Results and conclusions:**
  - Found **highly asymmetric productivity** in computer science, consistent with **Lotka's law**.
  - The **collaboration level** is moderate, with two or three authors per paper being typical.
  - **Conference papers** are more collaborative than journal papers.
  - The computer science collaboration network shows **small-world properties** and evidence of **assortative mixing**.
  - Temporal analysis revealed a **steady expansion** of the field, with **conferences becoming the dominant publication venue** after 1983.
  - Highlighted the differences in collaboration patterns between **conference and journal collaborations**.

## druszcz_citation_disparity_2024.pdf

- **Research questions or problems:**
  - Investigate the **citation disparity** across different sub-areas of Brazilian Computer Science.
  - Explore how using **citations as a metric** can lead to unfair comparisons, and suggest methods to mitigate this disparity, particularly with the **universal fit citation**.

- **Approach or methodology:**
  - Analyzed **citation data** and used the **power-law distribution** for scientific citations.
  - Introduced the **complementary cumulative distribution function** to quantify disparity.
  - Used the **universal fit citation** to normalize citations based on average citations in each research area and year.

- **Databases or data sources:**
  - Data from **CSIndexBr**, **DBLP**, and **OpenCitations** (collected between November 2022 and January 2023).

- **Results and conclusions:**
  - Found **significant citation disparity** across sub-areas, with certain areas like **Computer Vision** and **Security** being more highly cited than others like **Algorithms** and **Formal Methods**.
  - The **universal fit citation** helped reduce the disparity, suggesting that it could provide fairer comparisons of scientific impact across areas.

---

# OpenAlex

## "culbert_reference_coverage_analysis_openalex_2024.pdf"

- **Research questions or problems:**  
The main research problem is to assess the **trustworthiness of OpenAlex's scholarly metadata** as an open-source alternative to proprietary databases like Web of Science and Scopus. Specific questions include whether **reference coverage differs** between the three databases and how coverage of **abstracts, ORCIDs, and Open Access status** varies. The study aims to determine if OpenAlex can serve as an adequate or superior **free alternative** for bibliometric research.

- **Approach or methodology:**  
The study performs a **large-scale comparative analysis** of OpenAlex, Web of Science (WoS), and Scopus using a **'Shared Corpus'** of 16.8 million recent publications (2015-2022). It compares **reference coverage** and the coverage of **abstracts, funding information, ORCIDs, and Open Access status** using DOI matching. Statistical measures (mean, median, etc.) were employed for reference counts, and journal-level metadata coverage was assessed.

- **Databases or data sources:**  
The primary data sources are **OpenAlex, Web of Science, and Scopus**. A **'Shared Corpus'** derived from these three databases forms the basis of the analysis. The study also notes that all three databases use the **Unpaywall** service for Open Access status.

- **Results and conclusions:**  
OpenAlex shows comparable **average source reference numbers** and internal coverage rates to WoS and Scopus, but it has slight overcounting and undercounting in some journals. It has **higher ORCID coverage**, lower **abstract coverage**, and similar **Open Access status coverage** compared to the proprietary databases. The study concludes with a **recommendation for caution** when using OpenAlex for scientometric studies due to data quality issues and potential volatility.

## "estevez_new_trends_bibliometric_2023.pdf"

- **Research questions or problems:**  
This paper provides a **comparative analysis of 44 bibliometric and bibliographical APIs**. It establishes a **taxonomy** for these APIs, evaluates their metadata and capabilities, assesses their **interoperability**, and highlights the **lack of a single API** that meets all bibliometric needs.

- **Approach or methodology:**  
The study employs a **descriptive comparative analysis** of 44 bibliographic APIs, collecting data on their features in **March 2022**. The APIs were categorized into four groups: **general, content, search, and query modes**. The paper analyzes their support for various **bibliometric analyses** and their **interoperability** with shared identifiers like DOI and PubMedID.

- **Databases or data sources:**  
The study examines **44 bibliometric APIs**, including those from providers like **Semantic Scholar, Lens, InCites, Web of Science, Scopus, Dimensions, OpenAlex, CrossRef, Unpaywall, ORCID**, and more.

- **Results and conclusions:**  
The study finds that **Clarivate Analytics and Elsevier offer highly versatile APIs**, while **non-profit organizations** often promote open science via their APIs. Most APIs provide **free access** for academic use, though metadata retrieval may have limitations. The study concludes that **no single API** meets all bibliometric needs, recommending the **combination of multiple APIs** for comprehensive data coverage.

## "ortega_indexation_2024.pdf"

- **Research questions or problems:**  
This study investigates the **coverage and overlap of retracted publications, retraction notices, and withdrawals** across seven major scholarly databases: Dimensions, OpenAlex, PubMed, Scilit, Scopus, The Lens, and Web of Science (WoS). It aims to identify **discrepancies** in coverage, understand the **reasons** for these differences, and determine the best database or combination for representing retracted literature.

- **Approach or methodology:**  
The study employs a **quantitative approach** to compare coverage of retracted documents from the seven databases for publications from 2000 onwards. Data were collected via **web search interfaces** and **REST APIs** for OpenAlex and Scilit. **Multidimensional Scaling (MDS)** and **k-means clustering** were used to analyze coverage differences, and **Venn diagrams** illustrated database overlap.

- **Databases or data sources:**  
The study compares the coverage in **Dimensions, OpenAlex, PubMed, Scilit, Scopus, The Lens, and Web of Science (WoS)**.

- **Results and conclusions:**  
Non-selective databases like **Dimensions, OpenAlex, Scilit, and The Lens** index more retracted publications than selective databases like PubMed, Scopus, and WoS. **OpenAlex and Scilit** demonstrated the widest coverage. A combination of **OpenAlex, Scilit, and WoS** covered 99.9% of retracted literature. The study highlights **issues with accurate labelling** of retracted publications in some databases, recommending that researchers query multiple non-selective databases for comprehensive results.
