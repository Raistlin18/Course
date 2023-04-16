import file_handler
import data_conversion
import platform_sales
from pprint import pp

test_eladasok = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
# print(test_eladasok)
# print(file_handler.write_dicts_to_csv('teset_sales.csv', test_eladasok))

# pp(data_conversion.get_sales_keys(test_eladasok))
# pp(data_conversion.modify_sales_number(test_eladasok))

# pp(platform_sales.get_all_platforms(test_eladasok))
# pp(platform_sales.get_gamesales_by_platforms(test_eladasok))

test_eladasok = data_conversion.modify_sales_number(file_handler.get_dicts_from_csv('vg_sales.csv')[:3])

# pp(platform_sales.sum_gamesales_by_territory(test_eladasok, 'Global_Sales'))
# pp(platform_sales.sum_platform_sales(platform_sales.get_gamesales_by_platforms(test_eladasok)[0].items(), data_conversion.get_sales_keys(test_eladasok)))

pp(platform_sales.create_platform_sales(platform_sales.get_gamesales_by_platforms(test_eladasok), data_conversion.get_sales_keys(test_eladasok)))