---
Title: Setters and getters in python
Date: 2018-10-01 08:00
Modified: 2018-10-01 08:00
Category: python
Tags: python
Slug: setters-and-getters-in-python
---

Often when you want to assign some variable within a class you want to
check or do something before you assign a value to that variable.
In most programming languages a common design pattern of getting or
setting a variable on an object is to implement so called `set` and `get`
functions. For example say we have a class `Circle`, that has a
variable called `radius`. Then we should only allow a radius to be a
number, and that number should be positive (what does a circle with a
negative radius look like?). Therefore we want to check that these
conditions are met before we assign a value to radius. One way we
could do this in python is to implement one function called
`get_radius` and one function called `set_radius`.

```python
class Circle:
    """A class for working with circles

    Arguments
    ---------
    radius : float
        The radius of the circle

    """
    def __init__(self, radius):
        self.set_radius(radius)

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        assert isinstance(radius, (int, float)), \
            "Expected radius to be an integer or a float"
        assert radius > 0, "Radius must be a positive number"
        self.radius = radius

```
You can set and get the radius as follow.
```python
>>> circle = Circle(5)
>>> print(circle.get_radius())
5
>>> circle.set_radius(3)
>>> print(circle.get_radius())
3
```
And if you for example try to set the radius to a negative number it
will throw an `AssertionError`
```python
>>> circle.set_radius(-4)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
----> 1 c.set_radius(-4)
...
AssertionError: Radius must be a positive number
```

However in python, there is a more elegant and "pythonic" way of doing
this using decorators as shown in the following code
```python
class Circle:
    """A class for working with circles

    Arguments
    ---------
    radius : float
        The radius of the circle

    """
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        assert isinstance(radius, (int, float)), \
            "Expected radius to be an integer or a float"
        assert radius > 0, "Radius must be a positive number"
        self._radius = radius
```
You now can set and get the radius as follow.
```python
>>> circle = Circle(5)
>>> print(circle.radius)
5
>>> circle.radius = 3
>>> print(circle.radius)
3
```
The variable `radius` is stored internally in the "private" variable
`_radius`, but any interaction with the user can happen through the
`radius` attribute.
Note however, that if forget to add the setter-method, for example
```python
class Circle:
    """A class for working with circles

    Arguments
    ---------
    radius : float
        The radius of the circle

    """
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```
then if you want to set the radius in the same way it will throw an error.
```
>>> circle = Circle(5)
>>> print(circle.radius)
5
>>> circle.radius = 3
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
----> 1 circle.radius = 3

AttributeError: can't set attribute
```
In stead you have to use the "private" variable which can lead to
unwanted behaviour
```python
>>> circle._radius = -3
>>> print(circle.radius)
-3
```
