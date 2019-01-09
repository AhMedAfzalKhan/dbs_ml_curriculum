---
date: w9d5
duration: 10
maintainer: zwmiller
order: 10
title: Big Data Prep
---

Install Notes:

The installation guide will work for ubuntu or mac os. If the students can't
get it to work locally, they can spin up an EC2 instance and try to install it
there as well. They will need a T2.large at least. The guide has been tested
on MacOSX 10.13 (High Sierra) and Ubuntu 16.02.

If all else fails, they can resort to using the spark_install_docker guide,
which uses the metis docker container to get them up and running. That's not
ideal because there's a lot of ssh tunnel magic that happens that generally
confuses people. However, I've left it there in case all else fails.
