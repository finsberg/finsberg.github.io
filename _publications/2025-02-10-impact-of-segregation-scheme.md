---
title: Impact of Segregation Scheme on Performance of a Strongly Coupled Electromechanical Solver
collection: publications
permalink: /publication/impact-of-segregation-scheme
excerpt: 'Fully coupled cardiac electromechanics simulations have in the last few years become feasible on a tissue and organ scale'
date: 2025-02-10
venue: ''
paperurl: 'https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=5128775'
authors:': 'Lena Myklebust, Hermenegild Arevalo, Cécile Daversin-Catty, Samuel Wall, Henrik Finsberg'
---

Fully coupled cardiac electromechanics simulations have in the last few years become feasible on a tissue and organ scale. However, free and open-source tools for running these simulations are still limited. Furthermore, due to the high computational expense of coupling electrophysiology (EP) and mechanics, investigations into choice of coupling scheme is warranted. In this study, we investigate the effect of the selected coupling scheme on accuracy and run time, implemented in a freely accessible, open-source software, Simcardems. We used the monodomain model and the ToR-ORd-dynCI model to describe EP on a tissue and cellular scale, respectively. Mechanics was modeled using an active stress approach. To represent passive tissue we used a Holzapfel-Ogden model of a transversely isotropic material, whereas the Land model was used to represent active contraction. The EP and mechanics components were strongly coupled; each subsystem was solved separately and variables interpolated between them at each mechanics time step. This enabled the use of different temporal and spatial resolutions for EP and mechanics, reducing the computational cost considerably. Here, we implemented three different schemes of variable transfer between EP and mechanics, which we denoted Cai-, CaTRPN-and ζ's split. For each scheme, a different set of variables within the Land model were transferred between the EP and mechanics components of the model. We investigated how simulation time and error depended on the chosen scheme, as well as the selected temporal and spatial resolution of the mechanics mesh. The three …
