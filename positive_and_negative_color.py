import pandas as pd
import numpy as np

# Generate random data for the DataFrame
np.random.seed(0)  # For reproducibility
data = np.random.randn(10, 4)

# Create DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Define a function to apply color formatting
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: {}'.format(color)

# Apply color formatting to the DataFrame
styled_df = df.style
styled_df = styled_df.apply(lambda x: x.applymap(color_negative_red))

# Display the styled DataFrame
styled_df
