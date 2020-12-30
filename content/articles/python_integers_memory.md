---
Title: Allocating memory for integers in python
Date: 2020-12-27 08:00
Modified: 2020-12-27 08:00
Category: python
Tags: python
Slug: python-integers-memory
---

Python differs from many other programming languages in the way it represents integers. Basically everything in python is a object and and integers are no different. This naturally has some pros and cons. While you need to be careful when working with large integers in other programming langues you can basically use as large numbers as you want (it is limited by the RAM on your computer). For example in `C++` you can declare an integer using the `int` type as long as it is smaller (im absolute value) than $2^31 - 1$. Larger numbers can be declared using e.g `long`.

```C++
int small_number;  // smaller than $2^31 - 1$
long large_number;  // smaller 2^63 -1
```

In `C++` an `int` takes up 4 bytes of the memory while a `long` takes up 8 bytes of memory. In python, we can see how many byes an integer takes up by using `sys.getsizeof`

```python
>> import sys
>> print(sys.getsizeof(1))
```
meaning than an integer takes up 28 bytes. Larger numbers takes up more memory. For example `2**29` takes up 28 bytes while `2**30` takes up 32 bytes
```python
>> print(sys.getsizeof(2**29))
28
>> print(sys.getsizeof(2**30))
32
```

If your python program uses a lot of integer this can lead to a high memory usage. However, since there are some numbers that are more in use than others, python does a little trick in order to lower the memory usage. 

We know that we can check if two object in python are the same by using the `==` operator. For example
```python
>> x = 523
>> y = 523
>> print(x == y)
True
```
To check that `x` and `y` points to the same memory address we can use the `is` operator
```python
>> print(x is y)
False
```
which is the same as doing
```python
>> print(id(x) == id(y))
False
```
If we were create a new variable `z` from `x` then we would get a variable pointing to the same memory address
```python
>> z = x
>> print(z is x)
True
```

Here comes the exception: For small numbers the above example is not valid. If you try the following
```python
>> x = 42
>> y = 42
```
then you will actually find that
```python
>> print(x is y)
True
```
You will actually find that all integers between -5 and 256 share this property
```python
>> s = []
>> for i in range(-5, 257):
>>     x = eval(str(i))
>>     y = eval(str(i))
>>     s.append(x is y)
>>> print(all(y))
True
```
while
```python
>> x = -6
>> y = -6
>> print(x is y)
False
```
and
```python
>> x = 257
>> y = 257
>> print(x is y)
False
```
In other words, python pre-allocates memory for the integers between -5 and 256 and and uses these pre-allocated integers anytime you declare an integer of this size. If the integer is outside this range then python will create a new object.