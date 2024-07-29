import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate synthetic height (in cm) and weight (in kg) data
height = np.random.normal(loc=170, scale=10, size=20)  # Mean height: 170 cm, Std dev: 10 cm
weight = 0.5 * height + np.random.normal(loc=0, scale=5, size=20)  # Linear relationship with noise

# Create a DataFrame
dataset = pd.DataFrame({
  'Height_cm': height,
  'Weight_kg': weight
})
