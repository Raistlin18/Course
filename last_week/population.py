from pprint import pprint as pp

hungarian_cities = {'Budapest': 1750216,
                    'Debrecen': 201112,
                    'Szeged': 160258,
                    'Miskolc': 167754,
                    'Pécs': 141843,
                    'Győr': 133946,
                    'Nyíregyháza': 116814,
                    'Kecskemét': 110373,
                    'Székesfehérvár': 96529,
                    'Szombathely': 78591
                    }

hungarian_cities_bad = {
    'BudaPest': 1750216,
    'Derecen': 201112,
    'Szeged': 160258,
    'Miskol': 167754,
    'Pécs': 141843,
    'Győr': 133946,
    'Nyíregháza': 116814,
    'Kecskemét': 110373,
    'Székesfehérvár': 96529,
    'Szombathely': 78591
}


def print_city_population(dictionary, key):
    if get_city_population(dictionary, key) == -1:
        print(f'Erről a városról nincs adat: {key}')
    else:
        print(f'{key} népessége a legutóbbi népszámlálás szerint: {dictionary[key]}')

def get_city_population(dictionary, key):
    return dictionary.get(key, -1)

def update_population(dictionary, list, modificator):
    for elem in list:
        dictionary[elem] += modificator

def add_cities(dictionary, tupli_in_list):
    for i in tupli_in_list:
        dictionary[i[0]] = i[1]

def update_population(dict1, dict2):
    dict1.update(dict2)

def delete_cities(dict1, list1):
    for i in list1:
        del dict1[i]

def get_over_populated_cities(dict1, list1):
    dict2 = {}
    for i in list1:
        dict2.update({i: dict1.pop(i)})
    pp(dict2)

def swap_cities(dict1, list1):
    for i in list1:
        dict1.update({i[1]: dict1.pop(i[0])})



# update_population(hungarian_cities, ['Budapest', 'Miskolc', 'Győr'], 1000)
# update_population(hungarian_cities, {'Budapest': 1749812, 'Érd': 69431})
# delete_cities(hungarian_cities, ['Debrecen', 'Kecskemét'])
# get_over_populated_cities(hungarian_cities, ['Budapest', 'Debrecen'])
# swap_cities(hungarian_cities_bad, [('BudaPest', 'Budapest'), ('Derecen', 'Debrecen'), ('Miskol', 'Miskolc'), ('Nyíregháza', 'Nyíregyháza')])
# pp(hungarian_cities_bad)


# lecso = {
#   'paradicsom': '40 dkg',
#   'paprika': '80 dkg',
#   'hagyma': '2 fej',
#   'szalonna': '5 dkg',
#   'olaj': '2 kanál',
#   'őrölt paprika': '1 teáskanál'
# }
#
# print(lecso.get('padlizsán', 'Padlizsán nincs a lecsóban'))


top_10_population = {
  'Hungary': {
      'Budapest': 1750216,
      'Debrecen': 201112,
      'Szeged': 160258,
      'Miskolc': 167754,
      'Pécs': 141843,
      'Győr': 133946,
      'Nyíregyháza': 116814,
      'Kecskemét': 110373,
      'Székesfehérvár': 96529,
      'Szombathely': 78591
  },
  'Germany': {
      'Berlin': 3520031,
      'Hamburg': 1787408,
      'Munich': 1450381,
      'Cologne': 1060582,
      'Frankfurt am Main': 732688,
      'Stuttgart': 623738,
      'Düsseldorf': 612178,
      'Dortmund': 586181,
      'Essen': 582624,
      'Leipzig': 560472
  },
  'France': {
      'Paris': 2187526,
      'Marseille': 863310,
      'Lyon': 516092,
      'Toulouse': 479553,
      'Nice': 340017,
      'Nantes': 309346,
      'Montpellier': 285121,
      'Strasbourg': 280966,
      'Bordeaux': 254436,
      'Lille': 232787
  }
}

def is_city_in_top_10(dict1, dict2, varos):
    if varos in dict1[dict2]:
        return dict1[dict2][varos]
    else:
        return f'{varos} máshol van'

def print_country_population(dict1, key1):
    for i in dict1[key1]:
        print(f'{i} : {dict1[key1][i]}')

def get_cities(dict1, key1):
    cities = list(dict1[key1].keys())
    print(cities)

def sum_cities(varosok):
    nepesseg = 0
    for i, menny in varosok.items():
        nepesseg += menny
    return nepesseg

def get_countries_population(population):
    orszag_nepesseg = {}
    for orszag, ossz_nepesseg in population.items():
        orszag_nepesseg[orszag] = sum_cities(ossz_nepesseg)
    return orszag_nepesseg


print(get_countries_population(top_10_population))
# get_cities(top_10_population, 'France')
# print_country_population(top_10_population, 'Hungary')
# print('The population of Cologne is: ' + str(is_city_in_top_10(top_10_population, 'Germany', 'Cologne')))