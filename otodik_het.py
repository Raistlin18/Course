guest1 = 'Béla, Kovács, +36101234567, 1017, budapest, Fő utca 10., bela.kovacs@@pelda.hu'
guest2 = 'Arnold, szabó, 06109876543, 6500, Baja, Folyó u. 24., arnold.szabo@example.com'
guest1_first_name = 'Béla'
guest1_last_name = 'Kovács'
guest1_mobile_phone = '+36101234567'
guest1_postal_code = '1017'
guest1_city = 'Budapest'
guest1_address = 'Fő utca 10.'
guest1_email = 'bela.kovacs@pelda.hu'
guest2_first_name = 'Arnold'
guest2_last_name = 'szabó'
guest2_mobile_phone = '+36109876543'
guest2_postal_code = '6500'
guest2_city = 'Baja'
guest2_address = 'Folyó utca 24.'
guest2_email = 'arnold.szabo@example.com'


def check_phone_length(phone_number):
    if len(phone_number) == 12:
        print('A telefonszám hossza megfelelő.\n')
    else:
        print('A telefonszám hossza nem megfelelő.\n')

def check_postal_code(postal_code):
    if len(postal_code) == 4:
        print('A cím magyar\n')
    else:
        print('A cím nem magyar\n')

def check_phone_country(phone_number):
    if phone_number.startswith('+36'):
        print('A telefonszám magyar\n')
    else:
        print('A telefonszám nem magyar.\n')

def check_email_country(email):
    if email.endswith('.hu'):
        print('Az e-mail cím magyar\n')
    else:
        print('Az e-mail cím nem magyar\n')

def check_email_format(email):
    if email.count('@') == 1:
        print('Az e-mail-cím formátuma megfelelő.\n')
    else:
        print('Az e-mail-cím formátuma nem megfelelő.\n')

def correct_first_name(first_name):
    print(f'{first_name}\n')
    print(f'{first_name.capitalize()}\n')

def correct_last_name(last_name):
    print(f'{last_name}\n')
    print(f'{last_name.capitalize()}\n')

def correct_city_name(city_name):
    print(f'{city_name}\n')
    print(f'{city_name.capitalize()}\n')

def correct_address(address):
    print(f'{address}\n')
    print(f'{address.replace("u.", "utca")}\n')

correct_address(guest1_address)
correct_address(guest2_address)

correct_first_name(guest1_first_name)
correct_first_name(guest2_first_name)

correct_last_name(guest1_last_name)
correct_last_name(guest2_last_name)

check_email_format(guest1_email)
check_email_format(guest2_email)

check_phone_country(guest1_mobile_phone)
check_phone_country(guest2_mobile_phone)

check_phone_length(guest1_mobile_phone)
check_phone_length(guest2_mobile_phone)

check_postal_code(guest1_postal_code)
check_postal_code(guest2_postal_code)

check_email_country(guest1_email)
check_email_country(guest2_email)

correct_city_name(guest1_city)
correct_city_name(guest2_city)
