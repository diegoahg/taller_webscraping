import pandas as pd

# Webpage url                                                                                                               
url = 'https://en.wikipedia.org/wiki/History_of_Python'
# Extract tables
dfs = pd.read_html(url)
# Get first table                                                                                                           
df = dfs[0]

# Extract columns                                                                                                           
df2 = df[['Latest micro version','Release date']]

print(df2)