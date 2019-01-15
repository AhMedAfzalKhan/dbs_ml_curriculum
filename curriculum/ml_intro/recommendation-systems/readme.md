---
date: w10d2
duration: 60
maintainer: todo
order: 10
title: Recommendation Systems
---

# Sample Lesson

- [RecSys Lecture](./what_is_a_recommendation_engine.pdf) (30 min, check and personallize presenter notes for tips)
- [Simple SVD Recommender lab](./simple_SVD_recommender.ipynb) (20 min)
- [Surprise lab](./Surprise_lab_solutions.ipynb) (20 min)
- (Optional) [svdRec lab](./svdRec_lab_solutions.ipynb) (15 min)

# Instructor notes

Remind the students often that RecSys is simply an application of Dimensionality Reduction methods to a business problem common to many industries. Students should have an intuitive understanding of latent features and quantification of objects into vector space.

## Objectives
- Introduce Content-Based and Collaborative Filtering methods
- Perform Collaborative Filtering from ratings matrices using `pandas` and `sklearn` on movie data
- Understand why this approach represents Collaborative Filtering, how Content-Based would differ, and how it might be implemented in a hybrid approach.
- Use the [Surprise](http://surpriselib.com) library that provides some nice built-in recommender functionality
- Understand how SVDs and other matrix decompositions are employed by recommender algorithms

# Additional Resources
- [svdRec](https://github.com/ZWMiller/svdRec), a simple package created by one of our former instructors, Zach Miller
- [Surprise](http://surpriselib.com), a full-featured approach
- [10 RecSys papers](https://medium.com/@ACMRecSys/10-recsys-papers-everyone-should-read-ad69bcd7feed) everyone should read
