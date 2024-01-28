---
title: "pulse: A python package based on FEniCS for solving problems in cardiac mechanics"
collection: publications
permalink: /publication/pulse:-a-python
excerpt: 'pulse is a python package based on FEniCS for solving problems in cardiac mechanics. The user can pick any of the built-in meshes or choose a custom user-defined mesh. A collection of different demos showing how to use the pulse library is found in the repository.'
date: 2019-9-24
venue: 'Journal of Open Source Software'
paperurl: 'http://dx.doi.org/10.21105/joss.01539'
authors:': 'Henrik Finsberg'
---

pulse is a software package based on FEniCS that aims to
solve problems in cardiac mechanics (but is easily extended to solve more general problems in
continuum mechanics). pulse is a result of the author’s PhD thesis, where most of the relevant background for the code can be found.
While FEniCS offers a general framework for solving PDEs, pulse specifically targets problems
in continuum mechanics. Therefore, most of the code for applying compatible boundary
conditions, formulating the governing equations, choosing appropriate spaces for the solutions
and applying iterative strategies, etc., are already implemented, so that the user can focus on
the actual problem he/she wants to solve rather tha