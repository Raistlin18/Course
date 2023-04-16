import data_conversion

'''
Set létrehozása a platformoknak
Iterálás a beolvasott listán és a különböző platformok összegyűjtése
Lista létrehozása, amely a platformokat, és a hozzájuk tartozó listákat fogja tartalmazni, ennek a neve legyen: all_platform_sales
Set felhasználásával iterálás még egyszer a beolvasott listán
Lista létrehozása egy platformnak az eladásairól
Eladások hozzáadása a listához, amelyek az adott platformhoz tartoznak
Platform neve, és a hozzá tartozó eladások lementése egy dictionarybe
Dictionary hozzáadása az all_platform_sales-hez
'''

def get_all_platforms(lista1):
    platforms = set()

    for i in lista1:
        platforms.add(i['Platform'])

    return platforms

def get_gamesales_by_platforms(lista1):
    platforms = get_all_platforms(lista1)
    all_platform = []

    for platform in platforms:

        sales_list = []

        for elem in lista1:
            if elem['Platform'] == platform:
                sales_list.append(elem)

        all_platform.append({platform: sales_list})

    return tuple(all_platform)


'''
Egy nulla értékű változó létrehozása.
Iterálás az eladásokon, majd az egy területhez tartozó eladások összeadása.
A létrejött összeg kerekítése két tizedesjegyre.
Egy dictionary létrehozása az új értékek tárolására.
Iterálás a platformhoz tartozó eladás listán.
Iterálás az eladás kulcsokon, majd az egyes területi eladások összegének mentése.
'''

def sum_gamesales_by_territory(eladasi_lista, terulet):
    osszeg = 0
    for i in eladasi_lista:
        osszeg = osszeg + i[terulet]
    return round(osszeg, 2)

def sum_platform_sales(tupli1, eladas_kulcsok):
    szotar = {}

    for platform, eladasok in tupli1:
        szotar['platform'] = platform

        for kulcs in eladas_kulcsok:
            szotar[kulcs] = sum_gamesales_by_territory(eladasok, kulcs)

    return szotar



'''
Egy üres lista létrehozása
Iterálás a get_gamesales_by_platforms() által kapott listán.
Új dictionary létrehozása egy platform eladásainak az összegéről.
A kész dictionary hozzáadása a listához.
'''

def create_platform_sales(lista1, lista2):
    last_list =[]
    for i in lista1:
        sum_sales_by_platform = sum_platform_sales(i.items(), lista2)
        last_list.append(sum_sales_by_platform)
    return last_list


platform_sales_list = create_platform_sales(
    get_gamesales_by_platforms(data_conversion.video_game_sales),
    data_conversion.sales_keys)