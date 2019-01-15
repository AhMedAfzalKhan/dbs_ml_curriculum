---
date: w12d2
duration: 200
maintainer: zwmiller
order: 10
title: Pyspark Lab
---

# Sample Lesson

* (30 min) [Intro to Spark](../spark-intro/intro_to_spark.pptx)
* (30 min) [Intro to Spark API](../pyspark-lab/intro_to_spark_api.ipynb)
* (20 min) [Word Count Exercise](../pyspark-lab/word_count_exercise.ipynb)
* (20 min) [Spark SQL Exercise](../pyspark-lab/airline_delays_sparksql_exercise.ipynb)
* (45-60 min) [ML with Spark](../pyspark-lab/machine_learning_with_spark.ipynb)

Optionals if there's time:

* (20 min) [Spam Classification with
Spark](../pyspark-lab/spam_classification_with_spark.ipynb)
* (20 min) [Recommendations in Spark](../pyspark-lab/spark_recommendation_systems.ipynb)

Note that there are 2 days for Spark. You can spread this content across both days, focusing on
theory/API the first day and getting as far as possible into the exercises. Then on the second
day revisiting the API and covering as much of the other material as possible.


# Instructor Notes

The goal of this set of lectures and exercises is to build a lot of hands on
experience with Spark and the API. The slides go more in depth with DAGs and
the style of lazy evaluation that Spark uses. On top of that, it will
introduce why Spark is faster than Hadoop and how it manages to do so using
RAM and DAGs. It will also discuss Spark 1.0, even though we won't use it for
any exercises.

After that, we jump straight into getting used to the Spark API. We'll focus
exclusively on the DataFrame version of Spark (Spark 2.0). The goal of the
exercises and the Intro to Spark API is to just give the students practice
seeing how the API looks. If the students need more time during any of the
exercises, grant it. There's a lot of good learning that happens during those
sections.

The ML part will also require a lot of time. Spending a lot of time on
VectorAssembler and Pipeline is mandatory, as is explaining the difference
between SparkML and Spark MLlib as well as how to use different metrics.
Focusing on the idiosyncrasies between SkLearn and SparkML is big as well.

At the end of this lesson the students should:

* Understand how Spark differs from MapReduce/Hadoop
* Know what a DAG is and why it makes Spark go
* Know what an RDD is
* Be familiar with the Spark DataFrame API
* Know how to use SparkSQL
* Know how Spark ML works
* Know what Vector Assembler and Pipeline are and why they're important
* Have a sense of how flexible Spark is in dealing with tabular and text data

# Additional Materials

Setting up a Spark Cluster on Amazon EMR:
[walkthrough](setting_up_EMR_spark.md)

Reading and writing directly to S3 with Spark:
[Example](linking_spark_to_s3.ipynb)
