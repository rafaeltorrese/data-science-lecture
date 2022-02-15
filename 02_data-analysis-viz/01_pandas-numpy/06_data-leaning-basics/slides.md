---
marp: true
title: Data Cleaning Basics
math: mathjx
size: 16:9
---

# Data Cleaning

Data Science and Business Intelligence

---

# Introduction

Data scientists commonly spend [over half their time cleaning data](https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/?sh=34411ff76f63), so knowing how to clean "messy" data is an extremely important skill.

In this lesson, we'll learn the basics of data cleaning with pandas as we work with `laptops.csv`, a CSV file containing information about 1,300 laptop computers. 

|   | Manufacturer |  Model Name |  Category | Screen Size |               Screen               |          CPU         | RAM |       Storage       |              GPU             | Operating System | Operating System Version | Weight | Price (Euros) |
|:-:|:------------:|:-----------:|:---------:|:-----------:|:----------------------------------:|:--------------------:|:---:|:-------------------:|:----------------------------:|:----------------:|:------------------------:|:------:|:-------------:|
| 0 | Apple        | MacBook Pro | Ultrabook | 13.3"       | IPS Panel Retina Display 2560x1600 | Intel Core i5 2.3GHz | 8GB | 128GB SSD           | Intel Iris Plus Graphics 640 | macOS            | NaN                      | 1.37kg | 1339,69       |
| 1 | Apple        | Macbook Air | Ultrabook | 13.3"       | 1440x900                           | Intel Core i5 1.8GHz | 8GB | 128GB Flash Storage | Intel HD Graphics 6000       | macOS            | NaN                      | 1.34kg | 898,94        |

---

We can start by reading the data into pandas. Let's look at what happens when we use the `pandas.read_csv()` [function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) with only the filename argument:

```python
laptops = pd.read_csv("laptops.csv")
```


We get an error! (The error message has been shortened.) This error references UTF-8, which is a type of encoding. Computers, at their lowest levels, can only understand binary - 0 and 1- and encodings are systems for representing characters in binary.

---

Something we can do if our file has an unknown encoding is to try the most common encodings:

* UTF-8
* Latin-1 (also known as ISO-8859-1)
* Windows-1251

The `pandas.read_csv()` [function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) has an `encoding` argument we can use to specify an encoding.

---



