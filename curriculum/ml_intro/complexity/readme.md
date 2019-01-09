---
date: w01d5
duration: 50
maintainer: artificialsoph
order: 2
title: Complexity Intro
---

# Sample Lesson Plan

- (30 m) [Complexity Slides](Complexity.pptx)
- (20 m) [Complexity in practice notebook](complexity-in-practice-solutions.ipynb)

# Learning Objectives

Students should be able to:

- Explain the value of complexity analysis and how it would be applied to projects in theory.
- Apply complexity analysis to their existing and futoure work.
  - Meaure the wall clock time of real code.
  - Programmatically measure wall clock time of real code.
  - Use a line profiler to check and inform big-O complexity analysis.
- Use the heuristic method to find Big-O complexity

# Depends On

[Python Review](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/python-review)

[Intro to Matplotlib](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/matplotlib)

# Instructor Notes

**Very important** Before starting this, update the notebook to use solutions that students have submitted for pair problems so far. I've included two pairs often taught in the first week (Reverse String and Can You Spell) but you may be teaching something different. If so, update the solutions in the notebook.

This lecture teaches a heuristic method for finding the big-O complexity of an alorithm. At the end of the slide deck is an optional component with an example of using a proof.

# Additional Resources
 - [Lecture Notes - USF CS](https://www.cs.usfca.edu/~galles/cs245/lecture/lecture2.pdf)
 - [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850) has many examples with solutions & explanations
 - [Rob Bell's Guide to Big O Notation](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/)

### Details

[Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850)

 - High level, assumes familiarity already
 - Touches on space complexity
 - Good review questions

Chad's [lecture notes](https://github.com/thisismetis/dscurriculum_beta/blob/master/class_lectures/week01-benson/02-git_viz/Introduction_to_complexity.ipynb)

 - Dives in w/ examples
 - Better academic coverage
 - Tradeoff between maintainability and complexity

USF CS 245 [lecture notes](https://www.cs.usfca.edu/~galles/cs245/lecture/lecture2.pdf)

 - From David Galles
 - Touches on benchmarking algorithms
   - Wall clock vs mathemtatical model
 - Touches on space / time trade off
 - Discussion of best, worst and average
 - Comparison of linear vs binary search
 - Big O
   - Leading terms, dropping constants
 - General guidelines
 - A handful of examples

Rob Bell's [blog](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/)

 - Describes each common complexity
