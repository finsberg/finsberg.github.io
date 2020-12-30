---
Title: Cardiac Mechanics
Date: 2018-10-05 08:00
Modified: 2018-10-05 08:00
Category: Cardiac modeling
Tags: modeling, cardiac, mechanics
Slug: cardiac-mechanics
Summary: What is cardiac modelling, and how can we model the mechanics of the heart.
---


The heart is the muscular organ responsible to pump blood in order to
supply the body with oxygen and nutrients. The heart consist of four
chambers, namely the left and right atria and the left and right
ventricles.

{{ m.figure('cardiac_modeling/CG_Heart.gif', '', '300px') }}

## What is modeling?

Before talking about cardiac modeling, it make sense to first define what we mean by modeling in general. Models are found everywhere and they are used to make the world comprehensible. Modeling it simply that are of creating and using models.

When you are driving home from work and you want to give an estimate of how long time it will take before you are home, you can start by checking how long it is, then you check what is the average speed limit and then you can simply divide the distance by the average speed limit to get an estimate of the time.
Taking the distance and dividing by the average speed limit is a very simple model, but often good enough. You could also take into account construction work along the way, or you can use data of the number of cars on the road during the time period that you are driving for previous days, but your model, which will be a collection of information and a way of putting the information together, will soon be too complicated for you to use. This is where *computational models* come in.

Models are particularly useful when we want to use computers to help us understand some type of phenomena. In this case we often call the model, computational. If you can formulate your problem in terms of mathematical equations it is very likely that you can solve it with a computer.

## What is cardiac modeling?

Cardiac modeling is simply the art of creating and applying models to the heart. As you may know, the heart exhibit a so called multi-scale nature, meaning that there are processes happening at different scales that work together. For instance, there are chemical reactions happening at the molecular level that are responsible for making the heart contract, and any perturbations in these processes might have effect on the overall pumping effect.


### Multi-scale modeling and homogenization

Modeling processes along different scales if referred to as *multi-scale modeling*, and this is an ongoing research topic. Modeling processes along different scale can be extremely hard, especially since the events are usually happening at different time scales, and the interaction between scales often goes both ways, i.e the changes in the molecular processes affect processes at the tissue level and changes in the processes at the tissue level changes gives rise to changes at the molecular level.

Since multi-scale modeling is hard it is often useful to focus the attention at one particular scale. The question is then what to do with the multi-scale issue? A common approach is to assume some type of continuity down at the lower scale. This continuity is often referred to as *homogenization*.

Lets take a realistic example. The cardiac tissue is made up by cardiac cells. Each cell can be thought of (here comes the modeling approach) as a compartment having an inside (*the intracellular space*) an outside (*the extracellular space*) and a something separating the inside from the outside (*the membrane*). Now, if you wanted to make you model of the cardiac tissue "realistic" you should be able to zoom in and be able to see some regions with only intracellular space and some region with only extracellular space. However, having this amount of detail in your model can be very expensive when you want to do computations. Therefore, a common approach is to assume that at any point you have both an extracellular and an intracellular space. Within the cardiac modeling community this modeling approach is used when trying to model the electrical current that flows through the heat, and we call this model the [bidomain model](https://en.wikipedia.org/wiki/Bidomain_model).

## Modeling the Mechanics of the heart

Since I spent a lot of my time during my PhD to look at models for the mechanics of the heart I will write a little section about this.

When modeling the mechanics of the heart at an organ level
it is common to only focus on the ventricles, and in particular the
left ventricle which is the chamber responsible to pump blood from the
heart to the body.

In other engineering disciplines such as in mechanical engineering or civil engineering, when talking about mechanics we typically talk about stress and strain. *Stress* can be thought of as the forces acting on a material whereas *strain* is the resulting change in shape as a response to a change in stresses. Stress and strain are like yin and yang. Just knowing one of them will only provide you with half the story. For example if you stretch a rubber band by 10 percent you hardly need to apply any force to achieve that, while you need to apply a massive amount of force if you want to do the same with steel.

The differences between rubber and steel lies in their material properties which in the case of the heart is generally unknown. Moreover, while it is "easy" to measure the strain (which can be achieved using imaging techniques), it is impossible to measure the stresses in the heart. Therefore *models are the only way to get an estimate of the stresses in the heart*


### The law of Laplace

The first thing we need to do in order to estimate the stresses in the heart is to make assumptions. Assumptions are an important ingredient in modeling, and how well you are going to represent the physical object you are studying depends on your modeling assumptions.

One of the first models ever used to study stresses in the left ventricle is known as the law of Laplace. Laplace is i famous mathematician from the 18th century, and although his name is probably best known from the Laplace equation or the Laplace transform, most clinicians know him for giving name to a formula that relates the stresses in the heart to a few measurable quantities. If we assume that the left ventricle is i sphere with a radius $r$, a wall thickness $w$ that is subjected to a pressure $P$, then the stress on the wall $\sigma$ is given by

$$
\sigma = \frac{P \cdot r}{2 w}
$$

I know what you are thinking; the underlying assumption here that the ventricle is similar to a sphere is pretty far from the reality. Although it is true that we cannot really trust the numbers we are getting out from this formula, we can use it to get some intuition about what is happening with the stresses when the morphology (the form and shape) of the ventricle is changing. For example we would expect that the stresses goes up when the radius goes up, while the stresses goes down it the width of the ventricular wall goes up.


### What is a realistic model?
The law of Laplace is a great model if you want to build up some intuition about how stresses are related to the shape for the left ventricle, but how can we more realistically model the stresses in the heart?

First of all, we need a more realistic geometry. For example we could use medical images of the heart, and then perform so called image segmentation in order to get a more realistic geometry.

{{ m.figure('cardiac_modeling/4decho.png', 'A 4D ultrasound image',  '300px') }}

{{ m.figure('cardiac_modeling/raw.png', 'Endocardial and epicardial surfaces segmented from an ultrasound image', '300px') }}

{{ m.figure('cardiac_modeling/mesh.png', 'Mesh obtained from the surfaces', '300px') }}

Second we need to incorporate more realistic structure of the cardiac tissue. It is well known that the cardiac tissue is a non-linear anisotropic material.
By *non-linear* we mean that the amount of force (or stress) you need to apply changes non-linearly with the amount of strain. This is similar to rubber; To begin with you can stretch rubber a lot without applying much force, but as the rubber stretches you will find that you need to apply a greater amount force to stretch the rubber further. By anisotropic we mean that the stress-strain relation is different depending on how you look at the material. For fibre-reinforced concrete, the properties along the steel wires are different that in the direction orthogonal to the steel fibers.

{{ m.figure('cardiac_modeling/orthotrophic.png', 'The cardiac tissue is an orthotropic material, meaning that we can find local orthogonal coordinate system point in the direction along the fibers, sheets and the sheet-normal axis (image src: [Holzapfel and Ogden 2009])', '400px') }}

In cardiac tissue we also have fibers (so called muscle fibers) that bundles together and varies through the wall. These fibers are again organized in a laminar structure called sheets. This microstructure is of course an important ingredient in the modeling assumptions, but it is not possible to accurately measure this microstructure in a beating heart.

In the end the level of realism in your model is determined by what you want to use the model for, and of course the availability of realistic model information.