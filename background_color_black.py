import pandas as pd
import numpy as np

# Create a DataFrame with random values
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Define a function to apply styles
def apply_styles(val):
    return 'background-color: black; color: yellow'

# Apply the style to the DataFrame
styled_df = df.style.applymap(apply_styles)

# Display the styled DataFrame
styled_df
