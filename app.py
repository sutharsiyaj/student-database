# =====================================
# Student Performance Bar Chart
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Upload Excel file
uploaded = files.upload()

# Get uploaded file name
file_name = list(uploaded.keys())[0]

# Read Excel file
df = pd.read_excel(student_performance_dataset.xlsx)

# Display dataset
print(df.head())

# Create Bar Chart
plt.figure(figsize=(12,6))

plt.bar(df['Student Name'], df['Average'])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()