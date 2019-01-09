---
date: w02d05
duration: 60
maintainer: jeddy92
order: 1
title: Cross Validation
---

# Sample Lesson Plan

- (60m) [CV and Testing Deck](CV_and_testing.key) - Validation/CV and testing workflow breakdown
- (30m) [Validation Workflow Code](validation_workflow_+_utilities.ipynb) - Code examples of the validation/testing workflow with a few bonus utility examples (dummy variables, polynomial features, etc.)

# Learning Objectives

With this lesson, students can:

- Understand the importance of estimating generalization error through testing
- Understand how out-of-sample data can also be used for model selection (validation), and why this is different than testing
- Introduce and practice (in code) two common modeling frameworks: train/validation/test and CV/test

# Depends On

[Linear Regression Code Intro](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-02/linear-regression-code-intro)

[Regularization](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-02/regularization)

# Instructor Notes

The lecture goal is to introduce rigorous methodologies for estimating model generalization error
and performing model selection via validation. It follow the philosophy of trying to teach students
the right way of doing things from the start, in the sense that it emphasizes the difference
between using out-of-sample data for selection (validation) and for estimating generalization error (testing).

The notebook pairs with the slides, implementing the two suggested frameworks (train/validation/test, CV/test)
in code and pointing to several convenient sklearn methods like cross_val_score.

# Additional Resources

[Old slides and notebooks](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-02/cross-validation/additional_resources)
