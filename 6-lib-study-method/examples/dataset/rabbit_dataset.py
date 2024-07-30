import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_records = 50

# Generate random data
data = {
  'dosage': np.random.uniform(0, 30, num_records),  # Dosage between 0 and 30 units
  'age': np.random.uniform(0, 10, num_records)  # Age between 0 and 10 years
}

dataset = pd.DataFrame(data)

# Determine normal weight based on age and dosage
def determine_weight(row):
  if row['age'] < 1 or row['age'] > 8:           return False
  elif row['dosage'] < 10 or row['dosage'] > 20: return False
  else:                                          return True

# Apply the function to determine weight
dataset['normal_weight'] = dataset.apply(determine_weight, axis=1)
