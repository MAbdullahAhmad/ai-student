import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100

# Generate height (in cm) - normally distributed around 170 cm with a standard deviation of 10 cm
height = np.random.normal(170, 10, n_samples)

# Generate age (in years) - uniformly distributed between 18 and 60 years
age = np.random.uniform(18, 60, n_samples)

# Generate weight (in kg) - linear relation with height and age plus some random noise
# Assume weight = 0.5 * height + 0.3 * age + random noise
noise = np.random.normal(0, 5, n_samples)
weight = 0.5 * height + 0.3 * age + noise

# Create a DataFrame
dataset = pd.DataFrame({
  'height': height,
  'age': age,
  'weight': weight
})
