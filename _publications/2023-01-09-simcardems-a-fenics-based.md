---
title: "simcardems: A FEniCS-based cardiac electro-mechanics solver"
collection: publications
permalink: /publication/simcardems:-a-fenics-based
excerpt: 'This paper presents a fully coupled electromechanical model to study the effects of cardioactive drugs on the heart. The model combines a human cell electromechanical model with a monodomain partial differential equation representation of the electrical substrate and an incompressible, anisotropic, hyperelastic continuum model. The model is implemented in the FEniCS framework and incorporates iterative conjugate gradient and sparse direct solvers to solve the equations.'
date: 2023-01-09
venue: 'Journal of Open Source Software'
paperurl: 'http://dx.doi.org/10.21105/joss.04753'
authors:': 'Henrik Nicolay Topnes Finsberg, Ilsbeth Gerarda Maria van Herck, Cécile Daversin-Catty, Hermenegild Arevalo, Samuel Wall'
---

The heart is composed of electrically excitable tissues that contract upon stimulation. During
a normal beat, the initial stimulus to drive the heart originates from a group of pacemaker
cells located in the atria, and electrically propagates first through the atria and then down
into and through the ventricles. This traveling stimulus activates the myocytes as it arrives,
driving a cascade of cellular processes that end in the release of calcium from intracellular
stores. This calcium then causes the activation and cycling of actin-myosin cross-bridges
within the myocytes, creating the muscle contraction that pumps blood throughout the body.
The propagating electrical signal and the resulting contraction of the heart tissues are tightly
coupled and highly coordinated to allow the pump to work efficiently and react to changing
needs of the body. However, this tight coupling also can drive pathology. For example, if
something is wrong in the electrical processes, it might manifest as an irregular contraction.
Or, when the heart tissue is stretched or contracts irregularly, there are mechanisms at the
cellular level that can alter the electrical behavior and drive dangerous arrhythmias.
Modeling and simulation are used extensively to describe the physics of these electrical and
mechanical processes and how they are connected. Accounting for the intertwined interactions
properly in a simulation of cardiac behavior requires a complex model that incorporates the
strong coupling between the active electrophysiological and the contractile mechanisms of
the myocardial cells, as well as the passive mechanical and electrical behavior of the overall
cardiac tissue. Such a model is referred to as an electro-mechanical model. Typically, an
electro-mechanical solver contains a number of sub-models that describe and connect the
different physics across the relevant scales, e.g., a monodomain model for the electrophysiology
coupled to and a hyperelastic continuum model for the mechanics.
Here we present a fully coupled electromechanical model in the context of evaluating the
effects of cardioactive drugs on the heart. Our framework incorporates a modern human cell
ordinary differential model (ODE) that describes the electrophysiology of the cell and how
stimulation leads to internal calcium release, and how this calcium is coupled to cross-bridge
dynamics and active force in the cell. This 0D model is embedded in a monodomain partial
differential equation (PDE) representation of the electrical substrate, as well as a corresponding
incompressible, anisotropic, hyperelastic continuum model where contraction is governed by
active stress. The expansion and contraction of the continuum are governed by boundary
conditions and the cellular calculations of calcium and cross-bridge states. At the same time,
change in the mechanical model is feedback to the cellular system, providing length and
shortening velocity feedback to the ODE model.
This strongly-coupled system is implemented in the open source finite element framework
FEniCS (Logg et al., 2012) using an iterative conjugate gradient method with a geometric
algebraic multigrid preconditioner to solve the monodomain equation, and a parallel sparse
direct solver to solve the elasticity equations. The equations in the 0D ODE model are solved
partly during the solving of the monodomain model and partly during solving of the mechanics
to ensure the stability of the strongly coupled system.
Several demos have been created, including demos using a slab-type geometry as well as one
using a more realistic ellipsoidal geometry