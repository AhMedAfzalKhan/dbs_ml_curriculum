---
date: w11d2
duration: 105
maintainer: zwmiller
order: 10
title: Hadoop Hive
---

# Sample Lesson

- (45 min) [Intro to Hadoop](intro_to_hadoop.pdf)
- (60 min) [MapReduce with Python Exercises](map_reduce_with_python_exercise.md)

# Instructor Notes

The goal for this lesson is to build intution about how HDFS works, why it's
important, and how it helps us solve the big data problem by combining with
MapReduce. Many engineering style details have been left out of the intro such
as heartbeat montioring, transfer protocols, CAP theorem, etc. Feel free to
add additional materials focusing on those if you please. I've tried and the
average student doesn't take much away from those discussions.

The students should understand:

* What is a cluster
* How does HDFS handle the data
* What are the node types and what do they do
* Why does HDFS replicate and why is commodity hardware used
* How do I interact with HDFS
* What is MapReduce? And where does the actual processing happen
* How does MapReduce work
* Mappers vs Reducers vs Sorting
* HDFS is the main surviving legacy of Hadoop in modern big data, though some
places still use Hive, Hadoop, etc
* Hive allows us to use SQL to query distributed systems

The exercise helps in-grain those MapReduce ideas by making the students
struggle with making MapReduce work in the comfort of Python. Three common
MapReduce Patterns are explored:

* Counting Occurences
* Computing a summary statistic
* Filtering data before processing

More examples can be added, but those 3 tend to take about an hour for
students working in pairs. I recommend going through the tweets example in
bursts: give them 5-10 minutes to think about how to approach it, then show
them an example of reading the data using `ast_literal_eval`. Then give them
5-10 minutes and show them the rest of the mapper. Then give them 5-10 minutes
and show them the reducer. Then give them the rest of the time to try things
out on the census data.

# Additional Matierals
