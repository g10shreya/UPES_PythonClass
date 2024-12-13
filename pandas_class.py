import pandas as pd
data = {
    'name': ['Stuti', 'Shreya', 'Jai', 'SmartCity'],
    'Age': [21, 24, 22, 21],
    'City':['Jaipur', 'Kanpur', 'South Delhi', 'Tushar'],
    'Year':[1867, 1497, 2553, 2003],
    'Population': [5.1, 4.2, 10.9, 4]
}
df = pd.DataFrame(data)
#print(df)
pivot = df.pivot_table(values='Population', index = 'City', columns='Year')
print("Pivot Table:")
print(pivot)
