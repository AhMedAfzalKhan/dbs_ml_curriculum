---
date: w4d2
duration: 150
maintainer: ultimatist
order: 10
title: Time Series
---

# Sample Lesson Plan

* (10m - Optional) [Datetime Intro](datetime_intro_SOL.ipynb)
* (50m) [Timeseries and Autocorrelation](timeseries_autocorrelation_SOL.ipynb)
* (90m) [ARIMA Lab](ARIMA_SOL.ipynb)


# Learning Objectives

1. (Optional) Datetime Intro
	- Create and modify datetime objects
	- Extract current computer time
	- Calculate time deltas
	- Shift dates via time objects
2. Timeseries and Autocorrelation
	- Explore Rossmann data
	- Introduce technical concepts related to time series and ARIMA modeling
	- Calculate moving averages
	- Analyze autocorrelations
3. ARIMA Lab
	- Explain time series decomposition
	- Describe additive and multiplicative data
	- Stationarize data
	- Fit AR, MA, and ARIMA models on prepared data
	- Interpret model parameters and performance
	- Visualize trends and forecasts

# Depends On

[Intro to Matplotlib](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/matplotlib)


# Instructor Notes

Time series modeling is a powerful technique that has no limit to its applications. Take a moment to think about how important time is to most any study or analysis we do... it's hard to come up with scenarios where it's not a dimension worth considering!

In this series of labs, we jump into essential tools for prepping and modeling time-based data.

To ease compatibility with the notebooks, let's install a new environment:

```bash
# run this full line in bash, as one line!

conda create -n py36 python=3.6 pandas numpy seaborn matplotlib scipy patsy statsmodels jupyter

```

This will create the `py36` environment and populate with the list of packages above; rename if you already have a `py36` env, and ensure that kernel is loaded when you run your notebooks!

> Note, python 3.7 has Jupyter compatibility issues as of October 2018. Versions older than 3.6 may work but are not vetted.

## Lessons and Solutions

Each lab provided is a solution file. You can tailor the starter labs (files provided to students) to have more or fewer empty code blocks depending on how much challenge and time spend is appropriate. There's also a bit of overlap for essential concepts, in case you don't use all three labs.


# Additional Resources

Resources are also provided in the final lab:

- [Datetime package docs Python 3.6](https://docs.python.org/3.6/library/datetime.html)
- [ARIMA in R](https://www.otexts.org/fpp/8/5)
- [Duke ARIMA Guide](https://people.duke.edu/~rnau/411arim2.htm)
- [Great explanation on MA in practice](http://stats.stackexchange.com/questions/164824/moving-average-ma-process-numerical-intuition)
- [Mean Reversion Testing](https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing)
- [Box-Jenkins Method](https://en.wikipedia.org/wiki/Box–Jenkins_method)
