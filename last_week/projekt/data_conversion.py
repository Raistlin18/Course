import file_handler

'''
1. lista létrehozása a kulcsoknak
2. iterálás az eredeti kulcsokon
3. csak a Sales stringet tartalmazó kulcsok összegyűjtése
4. az új lista felhasználásával a fájlból beolvasott listában lévő értékek módosítása
5. egy új módosított lista létrehozása
'''

def get_sales_keys(lista1):
    sales_list = []
    for i in lista1[0].keys():
        if 'Sales' in i:
            sales_list.append(i)
    return sales_list

def modify_sales_number(lista1):
    sales_keys = get_sales_keys(lista1)

    for i in lista1:
        for j in sales_keys:
            i[j] = float(i[j])

    return lista1


video_game_sales = modify_sales_number(file_handler.get_dicts_from_csv('vg_sales.csv'))
sales_keys = get_sales_keys(video_game_sales)