def remove_injured_player(lista, index):
    lista[index] = 'injured'

def add_new_player(team, player):
    team.append(player)

def add_captain(team, player):
    team.insert(0, player)

def remove_player(team, player):
    team.remove(player)

def delete_player(team, index1):
    del team[index1]

def transfer_player(our_team, rival_team, player_index):
    rival_team = [our_team.pop(player_index)]
    print(rival_team)



favorite_team = ['BJ Armstrong', 'Bill Cartwright', 'Horace Grant', 'Craig Hodges', 'Denis Hopson', 'Michael Jordan',
                  'Stacey King', 'Cliff Levingston', 'John Paxson', 'Will Perdue', 'Scottie Pippen', 'Scott Williams']

print(favorite_team[0])
print(favorite_team[1])
print(favorite_team[-1])
print(favorite_team[-2])
print(favorite_team[-3])
print(favorite_team[4:-4])

remove_injured_player(favorite_team, 0)
remove_injured_player(favorite_team, 1)
remove_injured_player(favorite_team, 2)

print(favorite_team)

add_new_player(favorite_team, 'Kukoco')

print(favorite_team)

add_captain(favorite_team, 'Michael Jordan')

print(favorite_team)

remove_player(favorite_team, 'Denis Hopson')

print(favorite_team)

delete_player(favorite_team, -2)
delete_player(favorite_team, -1)

print(favorite_team)

ellenseg = []
transfer_player(favorite_team, ellenseg, 0)

def sum_of_scores(lista):
    return sum(lista)

def calculate_averaga(lista, osszeg):
    darab = len(lista)
    return osszeg / darab

final_scores = [116, 124, 115, 102, 111, 106]
count_matches = len(final_scores)
first_quarter = [2, 2, 2, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1]
print(f'A Lakers {count_matches} meccset játszott le a fináléban')

print(calculate_averaga(final_scores, sum_of_scores(final_scores)))
