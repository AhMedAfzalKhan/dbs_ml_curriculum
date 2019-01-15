---
date: w1d2
duration: 90
maintainer: adashofdata
order: 2
title: Pandas Intro
---

# Sample Lesson

* (30m) [EDA Presentation](Exploratory_Data_Analysis.key)
* (60m) [Pandas Basics Notebook](Intro-to-Pandas.ipynb)
* (30m + 15m Optional) [Pandas Exercise](pandas-exercise.ipynb) ([Solution](pandas-solution.ipynb))

# Learning Objectives

By the end of this lecture, the students should know:
* The basic data science workflow and where data cleaning and EDA fit in
   * Common data issues and how to resolve them (such as imputing missing data)
   * Common EDA techniques and the tools used for EDA (including visualization tools)
* How to manipulate data using pandas, including
   * Basic pandas data structures such as series and dataframes
   * How to read in data using pandas and how to view basic info and descriptive stats about dataframes
   * How to select rows and columns in a dataframe using .loc and .iloc
   * How to create masks and filter data
   * How to deal with NULL values, and the difference between NaN and None values
   * How to groupby and sort in pandas

# Depends On

[Python Review](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/python-review)
* Data Types
* Mutability

# Instructor Notes

## Structure of the day
1. **EDA Presentation:** The presentation deck emphasizes the importance of data cleaning before going into modeling, and talks about how a lot of a data scientist's job is spent on this step.
2. **Pandas Basics Notebook:** The pandas  notebook is for the instructor to walk through to review the pandas basics with students. It is mostly a cookbook the students can use for reference. There are comprehension questions sprinkled throughout.
3. **Pandas Exercise Parts 1 to 4:** The students should split into pairs / threes for problems 1-4 of the pandas exercise. It mostly focuses on groupbys, which will be challenging for most students. You can start revealing the answers as students work through the problems.
4. **Pandas Exercise Part 5 (Optional):** Part 5 of the pandas exercise is a more difficult problem that uses a merge along with a groupby and sort to solve the problem. It's good to walk through with the students to show them the power of pandas. This likely will not fit in the morning and would need to spill over to the afternoon.

# Additional Resources
