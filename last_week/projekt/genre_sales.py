import data_conversion


def get_all_genres(sales):
    genres = set()

    for sale in sales:
        genres.add(sale['Genre'])

    return genres


def get_gamesales_by_genres(sales):
    genres = get_all_genres(sales)
    all_genres = []

    for genre in genres:

        sales_list = []

        for sale in sales:
            if sale['Genre'] == genre:
                sales_list.append(sale)

        all_genres.append({genre: sales_list})

    return tuple(all_genres)


def sum_gamesales_by_territory(sales, territory):
    sum = 0

    for sale in sales:
        sum = sum + sale[territory]

    return round(sum, 2)


def sum_genre_sales(genre_sale_items, sales_keys):
    sum_sales_by_genre = {}

    for genre, sales in genre_sale_items:
        sum_sales_by_genre['Genre'] = genre

        for key in sales_keys:
            sum_sales_by_genre[key] = sum_gamesales_by_territory(sales, key)

    return sum_sales_by_genre


def create_genre_sales(genre_sales, sales_keys):
    sum_genre_sales_list = []

    for genre_sale in genre_sales:

        sum_sales_by_genre = sum_genre_sales(genre_sale.items(),
                                                   sales_keys)
        sum_genre_sales_list.append(sum_sales_by_genre)

    return sum_genre_sales_list


genre_sales_list = create_genre_sales(
    get_gamesales_by_genres(data_conversion.video_game_sales),
    data_conversion.sales_keys)
