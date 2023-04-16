import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('platform_sales.csv')

sorted_data = data.sort_values('Global_Sales', ascending=False)

x = sorted_data['platform'][:5]
y = sorted_data['Global_Sales'][:5]

plt.bar(x,y)
plt.show()