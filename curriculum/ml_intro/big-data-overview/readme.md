---
date: w10d5
duration: 60
maintainer: zwmiller
order: 10
title: Big Data Overview
---

# Sample Lesson

- (15 minutes) [Big Data Overview](big_data_overview.pdf)
- (20 minutes) [Intro to Dask](../dask/intro_to_dask.pdf)
- (30 minutes) [Learning Dask Hands On](../dask/01_learning_dask_hands_on.ipynb)
- (15 minutes) [Dask with Large Data](../dask/02_dask_with_large_data.ipynb)
- (15 minutes) [Dask ML Library Demo](../dask/03_dask_ml_demo.ipynb)

# Instructor notes

The intro to big data day is about setting the scene properly for the next few
lessons. I recommend stressing these points:

* "Big Data" is an ever-changing term for what "constitutes" big data
* If you can't fit it in RAM, it needs new techniques
* We're going to go from least complicated to most complicated solutions to
the big data problems over the next lectures.
* Big data doesn't seem like it should create all the nightmares it does...
it's just bigger data. But it's a sneaky bastard.

For Dask:

The students should take-away:

* Dask looks a lot like pandas
* It works by partitioning data into chunks and cleverly processing those
chunks
* Dask is lazy in evaluation by creating DAGs
* Dask plays well with SkLearn, Numpy, Etc
* Dask can work on cluster computing and even supports it's own cluster build

Focus on building the intuition around why Dask solves those problems, then
tie that into, "what if we wanted to do that on an even bigger scale or with
data that isn't tabular?" That's why we need other technologies like Hadoop
and Spark.

I also highlight that Dask is currently a bit rough around the edges in terms
of parallelized machine learning. It has some, but not A LOT. So Spark can be
a better choice for that.
