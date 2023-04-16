import data_conversion


def get_all_years(sales):
    years = set()

    for sale in sales:
        years.add(sale['Year'])

    return years


def get_gamesales_by_years(sales):
    years = get_all_years(sales)
    all_years = []

    for year in years:

        sales_list = []

        for sale in sales:
            if sale['Year'] == year:
                sales_list.append(sale)

        all_years.append({year: sales_list})

    return tuple(all_years)


def sum_gamesales_by_territory(sales, territory):
    sum = 0

    for sale in sales:
        sum = sum + sale[territory]

    return round(sum, 2)


def sum_year_sales(year_sale_items, sales_keys):
    sum_sales_by_year = {}

    for year, sales in year_sale_items:
        sum_sales_by_year['Year'] = year

        for key in sales_keys:
            sum_sales_by_year[key] = sum_gamesales_by_territory(sales, key)

    return sum_sales_by_year


def create_year_sales(year_sales, sales_keys):
    sum_year_sales_list = []

    for year_sale in year_sales:

        sum_sales_by_year = sum_year_sales(year_sale.items(),
                                                   sales_keys)
        sum_year_sales_list.append(sum_sales_by_year)

    return sum_year_sales_list


year_sales_list = create_year_sales(
    get_gamesales_by_years(data_conversion.video_game_sales),
    data_conversion.sales_keys)