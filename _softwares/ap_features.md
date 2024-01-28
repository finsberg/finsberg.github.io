---
title: "ap_features"
excerpt: "Package to compute features of traces from action potential models"
collection: softwares
paperurl: "https://github.com/ComputationalPhysiology/ap_features"
---

ap_features is package for computing features of action potential traces. This includes chopping, background correction and feature calculations.

Parts of this library is written in numba and is therefore highly performant. This is useful if you want to do feature calculations on a large number of traces.