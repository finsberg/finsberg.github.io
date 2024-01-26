---
title: "SMART: Spatial Modeling Algorithms for Reactions and
Transport"
collection: publications
permalink: /publication/2023-smart
excerpt: 'Finite-element-based simulation package for model specification and numerical simulation of spatially-varying reaction-transport processes.'
date: 2023-10-01
venue: 'Journal of Open Source Software'
paperurl: 'https://joss.theoj.org/papers/10.21105/joss.05580'
citation: 'Laughlin et al., (2023). SMART: Spatial Modeling Algorithms for Reactions and Transport. Journal of Open Source Software, 8(90), 5580, https://doi.org/10.21105/joss.05580'
---

Recent advances in microscopy and 3D reconstruction methods have allowed for characterization
of cellular morphology in unprecedented detail, including the irregular geometries of intracellular
subcompartments such as membrane-bound organelles. These geometries are now compatible
with predictive modeling of cellular function. Biological cells respond to stimuli through
sequences of chemical reactions generally referred to as cell signaling pathways. The propagation
and reaction of chemical substances in cell signaling pathways can be represented by coupled
nonlinear systems of reaction-transport equations. These reaction pathways include numerous
chemical species that react across boundaries or interfaces (e.g., the cell membrane and
membranes of organelles within the cell) and domains (e.g., the bulk cell volume and the
interior of organelles). Such systems of multi-dimensional partial differential equations (PDEs)
are notoriously difficult to solve because of their high dimensionality, non-linearities, strong
coupling, stiffness, and potential instabilities. In this work, we describe Spatial Modeling
Algorithms for Reactions and Transport (SMART), a finite-element-based simulation package
for model specification and numerical simulation of spatially-varying reaction-transport processes.
SMART is based on the FEniCS finite element library, provides a symbolic representation
framework for specifying reaction pathways, and supports geometries in 2D and 3D including
large and irregular cell geometries obtained from modern ultrastructural characterization
methods.