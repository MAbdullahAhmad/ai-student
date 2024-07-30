import numpy as np
import pandas as pd

# Seed for reproducibility
np.random.seed(42)

# Generate 20 random heights between 150 cm and 200 cm
heights = np.random.uniform(150, 200, 20)

# Generate random hair color codes (e.g., 0 for Black, 1 for Brown, 2 for Blonde, etc.)
hair_colors = np.random.randint(40, 90, 20)

# Generate weights as a linear combination of height plus some noise
# We will add more weight to the height factor to ensure hair color has less impact
weights = 0.5 * heights + np.random.normal(0, 5, 20)

# Create a DataFrame
dataset = pd.DataFrame({
  'hair_darkness': hair_colors,
  'height': heights,
  'weight': weights
})