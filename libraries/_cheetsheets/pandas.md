### Pandas Cheat Sheet

#### Importing Pandas
```python
import pandas as pd
```

#### Creating DataFrames
```python
# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# From a CSV file
df = pd.read_csv('file.csv')

# From a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}
]
df = pd.DataFrame(data)
```

#### Viewing Data
```python
df.head()  # First 5 rows
df.tail()  # Last 5 rows
df.sample(3)  # Random 3 rows
df.shape  # Shape of the DataFrame (rows, columns)
df.info()  # Summary of the DataFrame
df.describe()  # Statistical summary
```

#### Selecting Data
```python
# Selecting columns
df['Name']  # Single column
df[['Name', 'City']]  # Multiple columns

# Selecting rows
df.iloc[0]  # First row by index
df.loc[0]  # First row by label

# Conditional selection
df[df['Age'] > 30]  # Rows where age > 30
df[(df['Age'] > 25) & (df['City'] == 'New York')]  # Multiple conditions
```

#### Modifying Data
```python
# Adding a new column
df['Salary'] = [50000, 60000, 70000]

# Updating values
df.loc[0, 'Age'] = 26

# Dropping columns
df.drop('Salary', axis=1, inplace=True)

# Dropping rows
df.drop(0, axis=0, inplace=True)

# Renaming columns
df.rename(columns={'Name': 'Full Name'}, inplace=True)
```

#### Handling Missing Data
```python
# Checking for missing values
df.isnull().sum()

# Dropping missing values
df.dropna(inplace=True)

# Filling missing values
df.fillna({'Age': df['Age'].mean()}, inplace=True)
```

#### Grouping and Aggregating Data
```python
# Group by a column and aggregate
df.groupby('City').mean()

# Multiple aggregations
df.groupby('City').agg({'Age': ['mean', 'max'], 'Salary': 'sum'})
```

#### Merging DataFrames
```python
# Concatenation
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
pd.concat([df1, df2])

# Merging
left = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
right = pd.DataFrame({'key': ['A', 'B'], 'value2': [3, 4]})
pd.merge(left, right, on='key')
```

#### Saving Data
```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', index=False)
```

#### Plotting Data
```python
import matplotlib.pyplot as plt

# Line plot
df.plot(kind='line', x='Name', y='Age')

# Bar plot
df.plot(kind='bar', x='Name', y='Age')

# Show plot
plt.show()
```

This cheat sheet covers the basic operations you might need while working with pandas. For more detailed information, refer to the [pandas documentation](https://pandas.pydata.org/docs/).