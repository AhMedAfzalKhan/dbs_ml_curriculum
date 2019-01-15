---
date: w1d2
duration: 30
maintainer: zwmiller
order: 4
title: Git Branches
---

# Sample Lesson Plan

* (30m) [Intro to Git Branches](Intro_to_Git_Branches.pdf)

# Learning Objectives

The students will learn:

* Why branches are useful
* What a pull request is and how it works
* What git clone does
* How teams can use Git/GitHub to collaborate on code

# Depends On

[Command Line](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/command-line)

[Intro to Git](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/git-1)

# Instructor Notes

This lecture will introduce the idea of collaborative git, merges, and pull
requests. It will also have the students connect to and make submissions to the class
repository.

**NOTE: You should setup an area for them to make test submissions
in the class repo before this lecture starts. I recommend making a folder called `students_submissions/test_area`**

The lecture starts by introducing a scenario where two team members are
reliant on the same code. Then one starts updating the code and the other no
longer has the most updated version. Emphasize how common this problem is and
how manually deciding whether everyone has the right version of the code is
impossible at scale. Then we introduce the idea of a branch and how one team
member can work on their own branch where their changes don't get in the way
of everyone else's code.

When talking about merges, you may want to highlight that merge conflicts are
a thing and that means someone has to be in charge of deciding how to merge
back in files if two people have modified the same lines of code. That person
is usually the code maintainer. This is not highlighted in the lecture for
brevity.

The lecture then goes through a group exercise of cloning the appropriate
class repository, having everyone create a branch and submit a test file using
that branch, as well as finishing with a pull request. When I've done this
before, I've done this along with the students to help them see it all in
action.

**Note: As discussed in the Slack channel, this assumes that your student team
has been given Write access to the repository. You should lock the master
branch so only instructors can push to it, then set the class team to have
write access. See here for help: [Video of Setting up GitHub Permissions](https://drive.google.com/file/d/1UDZswJvbczFWzhoB9WuuvwyneBKhfA0d/view)**


# Additional Resources

[Git Cheat Sheet](http://files.zeroturnaround.com/pdf/zt_git_cheat_sheet.pdf)
