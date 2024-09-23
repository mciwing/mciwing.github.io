# Tuples

Lists and dictionaries work well for storing and manipulating data during the
execution of a program. Both lists and dictionaries are mutable.
However, sometimes you’ll want to create a collection of
elements that are immutable (can't change). Tuples allow you to do just that.

```py
# coordinates of MCI IV
coordinates = (47.262996862335854, 11.393082185178823)
print(type(coordinates))
```

```
<class 'tuple'>
```

A `#!python tuple` is created with round brackets (`()`). As with lists and dictionaries,
the elements are separated by commas. Tuples can hold any type of data.

Access the individual elements of a tuple using the index.

```py
coordinates = (47.262996862335854, 11.393082185178823)
print(coordinates[0])  # 47.262996862335854
print(coordinates[1])  # 11.393082185178823
```

Let's try to change the value of an element in a tuple.

```py
coordinates = (47.262996862335854, 11.393082185178823)
coordinates[0] = 50.102
```

we will encounter following error:

```
Traceback (most recent call last):
  File "<ipython-input-29-d74dc80ea879>", line 2, in <module>
    coordinates[0] = 50.102
    ~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

As a `#!python tuple` is immutable, you can only redefine the entire tuple.

```py
coordinates = (47.262996862335854, 11.393082185178823)
# redefine the entire tuple
coordinates = (5.513615392318705, 95.2060492604128)
```

Tuples can be unpacked, to use them separately.

```py
coordinates = (47.262996862335854, 11.393082185178823)
latitude, longitude = coordinates
```

???+ info

    Tuples are often used for constants. In the above examples, we used 
    coordinates. As these coordinates are not going to change, a tuple is a 
    fitting data type.


???+ question "Tuple unpacking"

    Use the following tuple with cities.
    ```py
    cities = ("New York", "Los Angeles", "Chicago")
    ```

    - Print the first city.
    - Use tuple unpacking and print the resulting variables.

## Recap

In this rather short section, we introduced tuples and covered:

- mutable vs. immutable
- how to define a `#!python tuple`
- accessing elements
- and `#!python tuple` unpacking.
