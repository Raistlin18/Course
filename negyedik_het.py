# ---------------------------------------------------------------------------
# negyedik heti első feladat
# Panda populáció
# ---------------------------------------------------------------------------

# from pprint import pformat

# data = []
# years = [1976, 1985, 1987, 1994, 1995, 2003, 2013]
# wild_numb = [1000, 800, 1000, 1200, 1000, 1596, 1864]
# a = 0
# while a != 7:
#     b = 0
#     pandas = {
#         'ev': years[b],
#         'szam': wild_numb[b]
#     }
#     a += 1
#     b += 1
#     data.append(pandas)

# eltavolitando = ['[', ']', '{', '}', "'"]
# szoveg = pformat(data, indent=3, sort_dicts=False)
# for karakter in eltavolitando:
#     szoveg = szoveg.replace(karakter, '')
# print(szoveg)

# ---------------------------------------------------------------------------
# Fő feladat:
# A hófehérke probléma :D
# ---------------------------------------------------------------------------
# dwarfs = ['Tudor', 'Vidor', 'Szende', 'Szundi', 'Hapci', 'Morgó', 'Kuka']
# torpok = 0
# osszes_torp = 7
# banyasz_torp = 4
# while torpok <= banyasz_torp - 1:
#     print(f'{dwarfs[torpok]} a bányában van')
#     torpok += 1
#     while torpok <= osszes_torp - 1:
#         print(f'{dwarfs[torpok]} még otthon van')
#         torpok += 1


# ---------------------------------------------------------------------------
# Visszaszámláló
# ---------------------------------------------------------------------------

# masodperc = 10
# while masodperc >= 0:
#     print(f'{masodperc} másodperc a kilövésig!')
#     masodperc -= 1


# ---------------------------------------------------------------------------
# Anyulak szaporodása
# ---------------------------------------------------------------------------

# rabbits = 30
# months = 1
# while months <= 12:
#     print(f'A nyulak száma a(z) {months} hónap végén: {rabbits}')
#     rabbits *= 2
#     months += 1
#     while months >= 6 and months <= 12:
#         print(f'A nyulak száma a(z) {months} hónap végén: {rabbits}')
#         rabbits *= 3
#         months += 1


all_turbines = 25
turbine_power = 2000
sum_power = 0
turbine_counter = 1
while turbine_counter <= all_turbines:
    if turbine_counter <= 10:
        sum_power += turbine_power
        print(f'A(z) {turbine_counter}. számú szélturbina teljes fordulaton működik, 2000 MWh-t termelve. A farmon termelt összenergia jelenleg {sum_power} MWh.')
    elif 10 < turbine_counter <= 20:
        sum_power += (turbine_power / 2)
        print(f'A(z) {turbine_counter}. számú szélturbina fél fordulaton működik, 1000 MWh-t termelve. A farmon termelt összenergia jelenleg {sum_power} MWh.')
    elif 20 < turbine_counter <= all_turbines:
        print(f'A(z) {turbine_counter}. számú szélturbina nem működik, 0 MWh-t termelve. A farmon termelt összenergia jelenleg {sum_power} MWh.')
    turbine_counter += 1
