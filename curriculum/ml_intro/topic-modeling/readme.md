---
date: w9d5
duration: 105
maintainer: todo
order: 10
title: Topic Modeling
---

# Objectives

Students will:
- Understand what "topics" are and where they fit into the data science workflow for
   - EDA: topics changing over time
   - Supervised learning: dimensionality reduction
   - Unsupervised learning: comparing topics between documents
- Understand the difference between LSA, NMF and LDA
   - Latent Semantic Analysis: how it relates to SVD and PCA
   - Non-Negative Matrix Factorization: how it's different from SVD
   - Latent Dirichlet Allocation: how to think in terms of probability distributions
- See how topic modeling works in practice
   - How it is an iterative process
   - How text preprocessing techniques are used to get strong topic vectors
      - Document-Term Matrix vs TF-IDF
      - Stop Words, min_df, max_df
      - Parts of Speech, Bi-Grams, Stemming / Lemmatizing
   - Recognize when topic vectors are "good enough"

# Sample Lesson

- [Topic Modeling Overview](Topic_Modeling.pdf) (30 minutes)
- [LSA & NMF Overview + Python Demo](Topic_Modeling_LSA_NMF.ipynb) (30 minutes)
- [LDA Overview + Python Exercise](LDA_Exercise.ipynb) (45 minutes)

# Instructor notes

The presentation is broken into three parts:
- Topic Modeling Overview: explains dimensionality reduction for text and how to interpret the results
- LSA & NMF: explains matrix factorization and how it can be applied to text data
- LDA: explains how the generative model works

After the LSA & NMF section, walk the students through the Python demo to go through syntax.

After the LDA section, walk the students through the Python demo, and then have the students break up into pairs to do the exercise at the end (spend around 20-30 minutes on this). The exercise is highly recommended because it allows students to get the hang of how tuning works for topic modeling. You can bring the class together at the end to talk about what worked best for the groups (typically this is when students discover that min_df and max_df are good parameters to tune, the number of passes, etc.)

# Additional Resources
