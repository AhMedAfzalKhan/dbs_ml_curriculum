---
date: w03d5
duration: 60
maintainer: jeddy92
order: 10
title: Stochastic Gradient Descent
---

# Sample Lesson

Gradient Descent walkthrough notebook (~45-60 minutes)

# Objectives

- Understand the math and concepts underpinning gradient descent
- Be able to implement simple GD in code
- Understand how GD can be used to learn coefficients in a linear regression model
- Explain the value of stochastic gradient descent relative to other methods of optimizing models.

# Instructor notes

The lecture goal is to introduce gradient descent in a gradual manner by walking through the single variable then multi-variable cases (generically), then tying it explicitly to linear regression weight-finding. There are several (animated) visuals that are meant to be interactive and illustrative. The code that generates the visuals has components that are likely not immediately accessible to students -- the lecture emphasis is meant to be placed on the concepts and demonstrations, not the plotting code.

Sophie: These figures are slow to generate (the later ones take 1-2 seconds per frame). I looked around for methods to speed up inline figure updates in Jupyter or to use quicker animations and didn't come up with much. Here's some resources if someone wants to explore this further.

- Working example of different methods to generate and display animations inline: http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/
- Relevant issue on matplotlib repo for problems regenerating figures in jupyter: https://github.com/matplotlib/matplotlib/issues/9606

# Additional Resources

[Old slides visualizing GD and discussing SGD](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-02/stochastic-gradient-descent/additional_resources)
