# Collaboration Networks

## "Evolution of the social network of scientific collaborations" (Barabasi et al., 2002)
- \cite{barabasi_2002_evolution_social_network}

### Problems/Questions
This paper addresses the topological and dynamic mechanisms governing the evolution of complex networks, using the co-authorship network of scientists as a prototype. It explores how the network evolves over time, which parameters are crucial to understanding network topology, and aims to construct a model that captures the network's evolution and scaling.

### Approach
The study uses three complementary approaches:
- Empirical measurements to uncover topological measures and their time evolution. The electronic databases containing all relevant journals in mathematics and neuroscience for an 8-year period (1991–98) were mapped.
- A simple model is proposed to capture the network’s time evolution. In some limits, the model can be solved analytically, predicting a two-regime scaling in agreement with the measurements.
- Numerical simulations are used to uncover the behavior of quantities that could not be predicted analytically.

### Results
The co-authorship network is scale-free, and its evolution is governed by preferential attachment, affecting both internal and external links. The average degree increases in time, and node separation decreases. Internal links play an important role in determining the observed scaling behavior and network topology. The study also highlights the importance of distinguishing between asymptotic and intermediate behavior, as many quantities used to characterize the network are time-dependent.

---

## "On Six Degrees of Separation in DBLP-DB and More" (Elmacioglu & Lee, 2005)
- \cite{elmacioglu_2005_six_degrees_of_separation}

### Problems/Questions
This paper investigates the collaboration network of database researchers using the DBLP database to find patterns underlying the database community and their publication behavior.

### Approach
The study analyzes a collaboration network constructed from the DBLP database, examining citation data from 1968 to 2003. It hand-picked publication venues closely related to the database community, intentionally excluding venues related to Information Retrieval or Digital Library. The collaboration network consists of nodes of authors and edges connecting any two authors if they co-authored one or more papers.

### Results
The average distance of all database scholars in the network has stabilized to about 6, indicating the "six degrees of separation" phenomenon. The community shows a power-law distribution in the frequency of publications, with a few scholars publishing many papers and the majority publishing a small number. Scholars collaborate more often than before, with steadily increasing clustering coefficients. The study also identifies the most "central" scholars in the network.

---

## "Scientific collaboration networks. I. Network construction and fundamental results" (Newman, 2001)
- \cite{newman_2001_scientific_collaboration_networks_i}

### Problems/Questions
This study aims to construct and analyze networks of collaboration between scientists in different disciplines (physics, biomedical research, and computer science). It investigates statistical properties such as the number of papers written by authors, the number of authors per paper, and the number of collaborators scientists have.

### Approach
Collaboration networks were constructed using data from four publicly available databases of papers over a five-year period (1995-1999). The files were parsed to extract author names, and edges were added between each pair of authors on each paper.

### Results
The study found that the average number of papers per author varied across disciplines, with high-energy physics having a significantly higher number. The distributions of the number of papers per author followed a power law. The average number of collaborators was markedly lower in theoretical disciplines than in experimental ones. The study also identified a giant component in all networks, with the majority of scientists connected through intermediate collaborators.

---

## "Scientific collaboration networks. II. Shortest paths, weighted networks, and centrality" (Newman, 2001)
- \cite{newman_2001_scientific_collaboration_networks_ii}

### Problems/Questions
This paper expands on the previous study by examining non-local statistics, such as typical distances between scientists and measures of centrality. It addresses the limitations of simple networks and proposes a measure of collaboration strength based on the number of co-authored papers.

### Approach
The study used the same collaboration networks from the previous paper. It calculated shortest paths between vertices, average distances, and betweenness centrality. A weighted collaboration network was introduced to account for the strength of collaborative ties, considering the number of co-authors and papers.

### Results
The study found small average distances between scientists, indicating a "small world" effect. It also revealed a "funneling" effect, where most paths between scientists pass through only a few of their collaborators. The weighted collaboration network showed that the sheer number of collaborators was no longer a good predictor of connectedness and that well-connected scientists had a high number of co-authored papers.

---

## "Coauthorship networks and patterns of scientific collaboration" (Newman, 2004)
- \cite{newman_2004_coauthorship_networks}

### Problems/Questions
This paper aims to use co-authorship networks to answer questions about collaboration patterns, such as the number of papers authors write, the number of people they write them with, and the typical distance between scientists. It also examines how patterns of collaboration vary between subjects and over time.

### Approach
The study constructs networks from three bibliographic databases in biology, physics, and mathematics. It analyzes basic statistics such as the number of authors, papers, and collaborators, as well as network measures like average distance, clustering coefficient, and betweenness centrality.

### Results
The study found that the number of authors per paper varied substantially among subjects, with biology having the largest number and mathematics the smallest. The average number of collaborators was higher in biology than in mathematics. The networks exhibited a "small world" effect, with small average distances between scientists. The study also confirmed that preferential attachment occurs in collaboration networks and that betweenness centrality varies widely among individuals.

---

# International Collaboration

---

## "Analysing the Coauthorship Networks of Latin American Computer Science Research Groups" (Garcia et al., 2014)

- \cite{garcia_2014_analysing_the_coauthorship}

### Question/Problem

The study seeks to understand the co-authorship networks of Latin American Computer Science (CS) research groups, including their topological structures and evolution over time. It identifies influential authors and analyzes research networks arising from co-authorships.

### Approach

The study uses data from DBLP covering 20 years (1994–2013) across 35 institutions in nine Latin American countries. It uses graph theory to represent co-authorship networks, where nodes are authors and edges are co-authorship relations. Centrality metrics like degree, closeness, and betweenness are used to identify influential authors.

### Results

The research shows a significant increase in publications and collaborations in Latin America between 2004 and 2013. It identifies influential authors and finds that most collaborations occur between Brazil-Chile and Argentina-Brazil. The number and size of research groups have increased, indicating a densification process.


## "A Comparative Study on Research Performance in Computer Science of Six Countries" (Guan & Ma, 2004)

- \cite{guan_2004_comparative_study_research}

### Question/Problem

The paper aims to compare the research performance in computer science of six countries (USA, Germany, UK, Japan, India, and China) using scientometric indicators. It addresses the quantitative distribution and growth of scientific publications, communication behaviour, collaboration patterns, and research impact.

### Approach

The study uses the INSPEC database for data from 1993–2002. It employs scientometric indicators such as publication counts, activity index, and normalized impact factor (NIF). The research assesses mainstream connectivity by analyzing the distribution of scientific papers by country of publication.

### Results

The USA had the highest output, while China showed a considerable increase in publications. Chinese scientists tend to publish in domestic journals, resulting in lower international visibility compared to Indian scientists. The average number of authors for Asian countries is slightly higher than for occidental countries.

---

## "Measurement of International Scientific Collaboration" (Luukkonen et al., 1993)

- \cite{luukkonen_1993_measurement_of_international}

### Question/Problem

This paper seeks to clarify the methodology used to measure international scientific collaboration (ISC) between countries and to explore intercountry collaborative networks.

### Approach

The study discusses the use of both absolute and relative measures to analyze collaborative links, with the latter normalizing differences in country size. It uses bibliometric data, including co-authored papers, to quantify collaboration. Different measures, such as Salton's and Jaccard's measures, are applied.

### Results

The paper concludes that both absolute and relative measures are essential in analyzing collaborative links. Absolute measures identify central countries in the international science network, while relative measures indicate the intensity of collaborative links. Adjusting to differences in scale induces a more complex network marked by increasing diversity.

---

## "Network Structure and Distribution of International Research Collaboration of China" (Niu & Qiu, 2014)

- \cite{niu_2014_network_structure_distribution}

### Question/Problem

This study aims to map China's international research collaboration (IRC), examining its scale, primary collaborators (countries and fields), and key journals.

### Approach

The study analyzes 211,946 articles indexed in the Web of Science (WoS) from 2002 to 2011. It uses bibliometric and social network methods to analyze the data. The study examines the amount of collaboration, the countries and fields involved, and the journals in which the articles are published.

### Results

The study finds a stable increase in Chinese IRC, with an average annual growth of 23%. China collaborates mainly with developed countries. Physical sciences have the largest proportion of collaboration, while social sciences show a higher increase ratio.

---

## "A Geographic Analysis of the Interdisciplinary Collaborations in the Brazilian Scientific Community" (Pessoa Jr. et al., 2022)

- \cite{pessoa_jr_2022_a_geographic_analysis}

### Question/Problem

The study investigates interdisciplinary collaborations within the Brazilian scientific community and how these collaborations are spread across Brazilian geographic regions.

### Approach
 
The study uses data from the CNPq’s Lattes Platform, involving 263,264 Brazilian researchers. It analyzes interdisciplinary collaboration patterns across the eight major areas defined by CNPq and the five Brazilian geographic regions.

### Results

The research shows strong collaborative ties between the Southeast, South, and Northeast regions. Agrarian Sciences, Biological Sciences, and Health Sciences show high participation in interdisciplinary collaborations across all regions. Geographic proximity is also an important factor.

---

## "New Approach to the Visualization of International Scientific Collaboration" (Chinchilla-Rodríguez et al., 2010)

- \cite{rodriguez_2010_new_approach_visualization}

### Question/Problem

The paper aims to create visual representations to analyze international scientific collaboration, identifying the international facet of research and the main geographical axes of output.

### Approach

The study uses data from the Web of Science, including the Science Citation Index, Social Sciences Citation Index, and Arts & Humanities Citation Index. It normalizes data related to institutions, themes, geography, and journal impact factors. The study uses Pajek software and the Kamada-Kawai algorithm to generate network graphs.

### Results

The methodology allows for the characterization of communication patterns and generates graphic representations for domain analysis. It reveals the relative benefits of certain associations in terms of visibility. The visualizations provide data that can be easily processed to interpret scientific output at different levels of aggregation.

---

## "Scientific Production in Computer Science: Comparison Among Several Countries" (Wainer et al., 2009)

- \cite{wainer_2009_scientific_production}

### Question/Problem

This paper studies scientific production in Computer Science in Brazil compared to other countries, using the number of articles in journals and conference proceedings indexed by ISI and Scopus.

### Approach

The study compares Brazilian production from 2001 to 2005 with that of Latin American, Latin European, BRIC, and other countries. It classifies and compares these countries according to the ratio of publications in journals and conferences.

### Results

Brazil has the largest production among Latin American countries, about one-third of Spain’s production, and is similar to India and Russia. The growth in Brazilian publications places it in the mid-range group, and the distribution according to impact factor is similar to most countries. The similarity regarding publication efforts on conferences and journals using Scopus data is encouraging.

---

## "Exploring University–Industry Collaboration Trends in Computer Science: A Study on Hardware and Architecture and Software Engineering" (Cheng et al., 2016)

- \cite{cheng_2016_exploring_university}

### Question/Problem

This study examines research collaboration between universities and industry in computer science, focusing on global and country-level trends. It addresses the need for industrial entities to collaborate with universities to strengthen competitiveness and overcome difficulties in research. The study analyzes leading countries and their collaboration relations, filling a gap in previous studies that did not focus on computer science or offer a global analysis.

### Approach

The research employs bibliometric methods to investigate university-industry (UI) papers published between 2002 and 2011. Data was retrieved from the Science Citation Index, focusing on the "hardware and architecture" and "software engineering" subfields. Indicators such as the ratio of UI papers, density, degree centrality, betweenness centrality, and closeness centrality were calculated to ascertain core countries involved in international UI collaboration.

### Results

There was an increasing trend in UI papers and a stable UI collaboration ratio during the period. The average number of authors for UI papers was 4.13, higher than for all other papers. Most UI papers result from two-institution collaboration, but there was an increase in papers from multiple institutions.

The USA is the dominant collaborative partner with many countries and produced the highest number of UI papers globally.

The study showed different countries may prefer different modes of UI collaboration; UI collaboration in Greece, Switzerland, and Austria was mainly international collaboration, whereas the USA, Japan, and Taiwan showed a greater preference for domestic UI collaboration.

# Disciplinary in Collaboration

```markdown
## "Structure and Dynamics of Research Collaboration in Computer Science" (Bird et al., 2009)  
- \cite{bird_2009_structure_and_dynamics}

### Question/Problem  
The paper addresses the informal differences between computer science sub-areas and seeks to quantify these differences to provide "actionable intelligence" for researchers and funding agencies. It explores whether some areas are more fragmented, dominated by fewer researchers, or more interdisciplinary.

### Approach  
The study mines a collaboration graph from the DBLP bibliographic database and uses network analysis methods to study collaboration and interdisciplinary research at individual, within-area, and network-wide levels. It uses topological measures, community structure analysis, betweenness centralisation, and longitudinal assortativity as metrics. The research defines computer science research areas as sets of first-tier conferences.

### Results  
- The research compares different areas of computer science using indicators of collaborative style, such as interdisciplinarity and well-defined sub-areas. For example, programming languages and software engineering are interdisciplinary, while AI and architecture are not.
- It studies researchers and their collaborative patterns in each area, finding that many areas evolve from being dominated by a few researchers to having a more diffuse collaborative network. Security, however, shows a rapidly increasing dominance by a few researchers.
- The study also examines the degree to which research areas and key conferences are interdisciplinary, discovering that data mining and software engineering are very interdisciplinary, while theory and cryptography are not. Cryptography is highly isolated within the larger computer science community but densely interconnected within itself.

---

## "Collaboration in Computer Science: A Network Science Approach" (Franceschet, 2011)  
- \cite{franceschet_2011_collaboration_computer}

### Question/Problem  
This paper aims to study collaboration in computer science using a network science approach. It seeks to uncover properties of the field by representing collaboration in academic papers as differently grained networks. It also aims to observe how collaboration in computer science has evolved since 1960.

### Approach  
The study uses bibliometric methods to build affiliation and collaboration networks from the DBLP database. It analyses bibliometric properties such as the size of the discipline, productivity of scholars, and collaboration levels. It also investigates global network properties like reachability, average separation distance, distribution of collaborators, network resilience, clustering, and assortativity.

### Results  
- The research finds that scientific productivity in computer science is highly asymmetric, and the collaboration level is moderate compared to other fields. Conference papers are generally more collaborative than journal papers.
- The conference collaboration network is more widely and densely connected than the journal network. Journal collaboration establishes stronger social relationships among authors.
- Computer science has expanded since 1960 in terms of published papers and active authors. Computer scientists have become more productive and collaborative, though the gap between the most and least collaborative scholars is increasing. The collaboration network is moving towards a steady state with a giant connected component.
```