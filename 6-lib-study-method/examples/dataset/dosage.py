import pandas as pd
import numpy as np

# Parameters
num_records = 100
low_threshold = 8   # Adjust as needed
high_threshold = 13 # Adjust as needed

# Generate random dosage values
np.random.seed(0)  # For reproducibility
dosage = np.random.uniform(0, 20, num_records)  # Dosage between 0 and 20

# Determine health based on dosage
def determine_health(dosage):
  if dosage < low_threshold or dosage > high_threshold: return 'not good'
  else: return 'good'

# Create DataFrame
dataset = pd.DataFrame({
  'dosage': dosage,
  'health': np.array([determine_health(d) for d in dosage])
})
