import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('platform_sales.csv')

sorted_data = data.sort_values('Global_Sales', ascending=False)

platforms = sorted_data['platform'][:5]
sales = sorted_data['Global_Sales'][:5]

plt.pie(sales, labels=platforms, autopct='%.1f%%')
plt.show()
