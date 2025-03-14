import pandas as pd
import numpy as np

# Create database

data = {"Name": ["Alice", "Bob"], "Age": [22, 24], "City": ["Calgary", "Edmonton"]}

df = pd.DataFrame(data)

df.head()

df = df.replace("Alice", "Curtis Massingham")

df.head(1)
