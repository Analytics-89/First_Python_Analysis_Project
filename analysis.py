"""Initial setup and library installation"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Data
#since the file is in the same folder we will use only the name
df = pd.read_csv('netflix_data_analysis.csv')

# Step-1: to see what the data look like
print("---Top 5 row of Netflix Data----")
print(df.head())

#Step-2 : To see the general info (like how many rows, data fields)
print("\n---Data Information---")
print(df.info())

#Step-3: To count How many movies and how many TV Shows
print("\n---Content Count---")
print(df['type'].value_counts())

#step-4: Distribution of Content
#Let’s add code to answer two specific questions:
#1.Is Netflix mostly Movies or TV Shows?
print("\n--Content type Breakdown--")
type_count = df['type'].value_counts()
print(type_count)

# --- Step 3: Cleaning Data ---
# Let's fill missing 'country' and 'director' info with 'Unknown'
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')

# Check if it worked
print("\n--- Missing Values Fixed ---")
print(df.isnull().sum())

#2.Which countries produce the most content?
print("\n---Top 5 Countries")
top_countries = df['country'].value_counts().head(5)
print(top_countries)

#Step-5: visualizing
import matplotlib.pyplot as plt
import seaborn as sns

#Step-6:create visual chart
plt.figure(figsize=(8,6)) #Set the size of the window
sns.countplot(x='type', data=df, hue='type', palette='viridis', legend=False)

#add titles so people know what they are looking at
plt.title('Netflix: Movies vs TV Shows')
plt.xlabel('Content Type')
plt.ylabel('Total Count')

#this line opens a new window on your Windows PC with the chart!
plt.show()

# Save the chart as an image file in your project folder
plt.savefig('netflix_chart.png')
print("\nChart saved as netflix_chart.png!")

# Keep this if you still want the window to pop up
plt.show()





