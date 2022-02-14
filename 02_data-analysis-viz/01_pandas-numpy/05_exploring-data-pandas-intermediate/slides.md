---
marp: true
title: Data Science
theme: gaia
math: mathjax
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---


<!-- ![bg left:40% 80%](https://marp.app/assets/marp.svg) -->

# **Exploring Data With Pandas**

Data Science and Business Intelligence

---

#  `pandas.read_csv()`

The data dictionary for the main columns in the `f500.csv` file is below:

- `company`: Name of the company.
- `rank`: Global 500 rank for the company.
- `revenues`: Company's total revenue for the fiscal year, in millions of dollars (USD).
- `revenue_change`: Percentage change in revenue between the current and prior fiscal year.
- `profits`: Net income for the fiscal year, in millions of dollars (USD).

---

- `sector`: Sector in which the company operates.
- `previous_rank`: Global 500 rank for the company for the prior year.
- `country`: Country in which the company is headquartered.
- `hq_location`: City and country, (or city and state for the USA) where the company is headquartered.
- `employees`: Total employees (full-time equivalent, if available) at fiscal year-end.


---

We'll learn how to use the `pandas.read_csv()` [function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to read in CSV files.


Let's take a look at the first few lines of our CSV file in its raw form. To make it easier to read, we're only showing the first four columns from each line:

```
company,rank,revenues,revenue_change
Walmart,1,485873,0.8
State Grid,2,315199,-4.4
Sinopec Group,3,267518,-9.1
China National Petroleum,4,262573,-12.3
Toyota Motor,5,254694,7.7
```

---

# Sort Values

Let's continue by answering more complex questions about our data set. Suppose we wanted to find the company that employs the most people in China. We can accomplish this by first selecting all of the rows where the country column equals China:

```python
selected_rows = f500[f500["country"] == "China"] 
```


Then, we can use the `DataFrame.sort_values()` [method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) to sort the rows on the employees column. To do so, we pass the column name to the method:

```python
sorted_rows = selected_rows.sort_values("employees")
print(sorted_rows[["company", "country", "employees"]].head())
```

---

By default, the ```sort_values()``` method will sort the rows in ascending order --from smallest to largest.

To sort the rows in descending order instead, so the company with the largest number of employees appears first, we can set the `ascending` parameter to `False`

---
# Aggregation

Suppose we wanted to calculate the company that employs the most people in each of the 34 countries. Using the method from the last screen would be very inefficient, so we'll rely on a technique we haven't used yet with pandas - loops.

We've explicitly avoided using loops in pandas because one of the key benefits of pandas is that it has vectorized methods to work with data more efficiently. We'll learn more advanced techniques in later courses, but for now, we'll learn how to use loops for **aggregation**.

---

**Aggregation** is where we apply a statistical operation to groups of our data. Let's say that we wanted to calculate the average revenue for each country in the data set. Our process might look like this:

- Identify each unique country in the data set.
- For each country:
    - Select only the rows corresponding to that country.
    - Calculate the average revenue for those rows.

To identify the unique countries, we can use the `Series.unique()` [method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html). This method returns an array of unique values from any series. Then, we can loop over that array and perform our operation.


---

```python
# Create an empty dictionary to store the results
avg_rev_by_country = {}

# Create an array of unique countries
countries = f500["country"].unique()

# Use a for loop to iterate over the countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
    # Calculate the mean average revenue for just those rows
    mean = selected_rows["revenues"].mean()
    # Assign the mean value to the dictionary, using the
    # country name as the key
    avg_rev_by_country[c] = mean
```

---

# Calculating ROA

Now it's time for a challenge to bring everything together! In this challenge we're going to add a new column to our dataframe, and then perform some aggregation using that new column.

The column we create is going to contain a metric called return on assets (ROA). [ROA](https://www.investopedia.com/terms/r/returnonassets.asp) is a business-specific metric which indicates a company's ability to make profit using their available assets.

---

$$ \text{return on assets} = \frac{\text{profit}}{\text{assets}}$$

Once we've created the new column, we'll aggregate by sector, and find the company with the highest ROA from each sector.



---
