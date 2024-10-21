---
title: gotranx: General ODE translator
collection: publications
permalink: /publication/gotranx:-general-ode
excerpt: 'We introduce gotranx, a General ODE Translator for automatic code generation of ordinary differential equations (ODEs).'
date: 2024-10-17
venue: 'Journal of Open Source Software'
paperurl: 'https://joss.theoj.org/papers/10.21105/joss.07063'
authors:': 'Henrik Finsberg, Johan Hake'
---

We introduce gotranx, a General ODE Translator for automatic code generation of ordinary differential equations (ODEs). The user writes the ODE in a markup language with the file extension .ode and the tool generates code with numerical schemes for solving the ODE in different programming languages. gotranx implements a domain specific language (DSL) using Lark for representing ODEs. It can parse the variables and equations into a symbolic representation (Meurer et al., 2017), and generate numerical schemes based on codeprinters from Sympy, in particular the Rush-Larsen scheme (Rush & Larsen, 1978) which is very popular in the field of computational biology. The vision for gotranx is to implement the same features in gotranx as found in gotran along with additional features.