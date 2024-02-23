import pandas as pd

# Create a sample DataFrame with missing values
data = {'A': [7001.0, None, 70002.0, 20004.0, None,70005.0,None,10010.0,70003.0,70012.0,None,70012.0],
        'B': [150.0, 270.0, 65.26, 220.50, 948.50,2400.60,5760.00,2983.43,2480.40,250,75.29,3045.60],
        'C': ['2012-10-05','2012-09-10' , None, '2012-08-07', '2012-09-10','2012-07,27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
        'D': [3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3002,3001]}


df = pd.DataFrame(data)

# Detect missing values
missing_values = df.isna()



# Display True for missing values, False for present values
print(missing_values)
