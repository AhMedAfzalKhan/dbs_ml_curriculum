---
date: w9d5
duration: 60
maintainer: todo
order: 10
title: Embeddings
---

# Revision Notes

This lesson is preceeded by a Stochastic Gradient Descent lesson and a Neural Net Intro. Assume that students are familiar with

- NLP preprocessing techniques like tokenization, stemming, BOW, etc.
- SGD
- Backprop
- ANN for tabular data
- Activation functions
- Loss functions

A high-level topic that I'd like to see touched on here is the idea of transfer learning.

# Objectives

Students can

* Explain vector representations of words describe how vector representations can be used to store meaning.

* Summarize how vector representations of words can be created using Language Models/Semi-Supervised learning.

* Summarize the gist of modern approaches for building word vectors.
* Outline common uses of word vectors and apply them in code:
  * Compute simple count/tf-idf vectors with sklearn and Gensim  
  * Use Gensim to train a custom word2vec model from a corpus of text.
  * Load pre-trained embeddings for both word2vec and GloVe
  * Explore relationships between words in a corpus.


# Sample Lesson
**WordEmbeddings.ppt** (60-80 minutes): Counts, TF-IDF, word2vec, GloVe, how embeddings are evaluated, and a brief nod to contextualized word embeddings.

**Word Embeddings.ipynb** (20-30 mins): Code examples of count vectorizatin and tf-idf with sklearn and Gensim, creating and loading word2vec models with Gensim, and loading GloVe vectors into Gensim.  Student exercises include exploration of the word vector space and it's structure.

# Instructor notes
The goal of this lecture is to provide an intuition for how we can represent words as vectors so that we can apply them to downstream machine learning tasks.

The lecture starts with an intro/reminder of count vectors and then leads in to word2vec and GloVe.  It then discusses how word vectors are evaluated, and gives a brief nod to current state-of-the-art methods of producing contextualized word embeddings.

# Additional Resources
* Great Blog Post on Word2Vec Intuition: http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/

* GloVe Paper: https://nlp.stanford.edu/pubs/glove.pdf

* Word2Vec Paper: https://arxiv.org/abs/1310.4546

* Stanford Lecture notes on word vectors: http://web.stanford.edu/class/cs224n/lectures/lecture2.pdf

* TensorFlow tutorial on word vectors: https://www.tensorflow.org/tutorials/representation/word2vec
