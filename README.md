# lsh-covid19
locality sensitive hashing for COVID-19 genomes

I used locality sensitive hashing to analyze a set of COVID-19 genomes. I aimed to use this technique to essentially cluster genomes based on location. Though the dataset I used was limited and hence prevented me from performing a complete analysis, I carried out a theoretical analysis on the algorithm and believe this concept can be applied on a larger dataset for more relevant results. 

*Please see my writeup (Writeup.pdf) for a more complete summary.*

---

**Background**

Locality sensitive hashing (LSH) is a *probabilistic* algorithm for identifying pairs of similar sets. Similarity is defined by the Jaccard index which represents the size of the intersection of two sets divided by the size of the union of two sets. This can be applied to finding similarity between two strings by dividing the string into "k-mers" or subsequences of length k. In LSH, a set of hash functions are applied on the k-mers in the set, and the minimum hash is computed for each string. Probabilistically, collisions (i.e., identical min hashes between two strings) correspond to the Jaccard similarity. Several parameters can be modified to set a threshold similarity for strings assigned as similar.

Kaggle had a dataset of 367 COVID-19 genome sequences along with their source locations. I wanted to use LSH to find candidate pairs of similar sequences, expecting to find sequences from nearby locations to be paired. 

---

**Findings**

Most of the candidate pairs identified had high Jaccard similarity, and this is expected by its deterministic counterpart. When looking more closely at the sequences, it seems like they shared a large part of the sequence with each other. This could explain the high similarities. Ideally, I would have set a threshold and collected all candidate pairs with Jaccard similarity higher than that, but this is meaningless with this data. Nevertheless, I have obtained useful information about the runtime and space complexity of this algorithm. Specifically, I found that generating the signature matrix is the bottleneck in terms of runtime and that computing Jaccard indices is also slow. I also identified appropriate parameters for this application.

---

**Usage**

The best way to follow this code is to read through my writeup (Writeup.pdf)! Here, I describe the LSH algorithm in detail, discussing its intuition and its probabilistic analysis. I also discuss runtime and space complexity of this algorithm, my goal in this project, and I walk through my analysis of the algorithm.

The helper functions can also be used for general purpose LSH.

---

**Files**

* ``genomes.csv`` : a copy of the data used
* ``lsh.ipynb`` : the actual code for the exploration. Here, I perform LSH on the COVID-19 genomes, recording the runtime and the similarity of candidate pairs identified for various parameters. I also run the deterministic counterpart of LSH.
* ``lsh_algorithm.py`` : helper functions for the LSH algorithm

To run this code, first install requirements with ``pip install -r requirements.txt``. Then, use Python3 to run the notebook.

---

**Future Work**

As aforementioned, applying this algorithm on a larger dataset would be quite neat. For example, in the current dataset and implementation, it seemed like most genomes had a Jaccard similarity of close to 1.
Additionally, it would be interesting to compare the results of this algorithm to hierarchical clustering and to develop visualizations to this end.

---

** References**

1. https://www.kaggle.com/ritamenezes/covid19-complete-genomes

2. https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134