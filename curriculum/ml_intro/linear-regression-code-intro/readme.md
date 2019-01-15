---
date: w2d2
duration: 90
maintainer: ultimatist
order: 2
title: Linear Regression Code Intro
---

# Sample Lesson Plan
- (90m) [Linear Regression Code Intro](intro-to-regression-starter.ipynb)

# Learning Objectives

At the end of this notebook the students should:
- Be able to visualize data
- Look for correlations and multicollinearity
- Understand how linear regression models work
- Interpret basic regression statistics like R^2
- Do basic feature engineering and selection to improve models

# Depends On

[Linear Regression Theory Intro](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-02/linear-regression-theory-intro)
* Students should have a foundational understanding of linear regression prior to attempting this lab

[Seaborn](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/seaborn)

[Python Advanced](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/python-advanced)
* Pickling

# Instructor Notes

The goal of this notebook is to guide students through implementation of linear regression modeling. Prior theory understanding is key; still, this lab should take 90 minutes and students should attempt all exercises in the car price predictor student section.

## Details about Learning Objectives

With this notebook students will:

Be able to create linear regression in:
- [***statsmodels***](http://statsmodels.sourceforge.net/): a package mainly best at doing regressions with traditional R formula syntax
- [***scikit-learn***](http://scikit-learn.org/dev/index.html): This is the main machine learning package we'll be using throughout the course.  It has a multitude of machine learning algorithms and helpful machine learning pipeline tools.  sklearn has a tremendous amount of functionality, to get the most out of this course it will help to really explore the depth of the documentation on your own and watch as you understand more and more of the functionality as the course progresses.

Gain familiarity with the following:
- [***R formulas***](http://science.nature.nps.gov/im/datamgmt/statistics/r/formulas/): R formulas are a convenient way for encapsulating functional relationships for regressions
- [***seaborn***](http://stanford.edu/~mwaskom/software/seaborn/): We'll use seaborn for **visualization** as we go along
- [***Variable Preprocessing and Polynomial Regression***](http://scikit-learn.org/dev/modules/preprocessing.html#preprocessing) with scikit-learn:  We'll be **"standardizing"** or **"normalizing"** many of our variables to yield better model data.  We'll show how the "linear" models can be extended to basically any type of function by using functions of the different fields as the inputs to the linear model.

## Installations (if necessary)

```` bash
conda install pandas numpy statsmodels seaborn scikit-learn
````

# Additional Resources
- [Variable Preprocessing and Polynomial Regression](http://scikit-learn.org/dev/modules/preprocessing.html#preprocessing)
- [Polynomial Features](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
