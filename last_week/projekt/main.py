import file_handler
from platform_sales import platform_sales_list
from genre_sales import genre_sales_list
from year_sales import year_sales_list

print(file_handler.write_dicts_to_csv('platform_sales.csv', platform_sales_list))
print(file_handler.write_dicts_to_csv('genre_sales.csv', genre_sales_list))
print(file_handler.write_dicts_to_csv('year_sales.csv', year_sales_list))
