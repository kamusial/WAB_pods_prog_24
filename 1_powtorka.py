# program do rejestracji
# program sprawdza, czy uzytkownik juz istnieje
# haslo wpisujemy 2 razy - musi byc takie samo

# sprawdz bezpieczenstwo hasla

import funkcje_zmienne

username_list = ['Kamil', 'Dixi', 'Warszawa01']
username = input('Podaj nazwe uzytkownika:  ')

while True:
    username = input('Podaj nazwe uzytkownika:  ')
    if username not in username_list:
        break

while True:
    passwd1 = input('Podaj haslo: ')
    passwd2 = input('Powtorz haslo: ')
    if funkcje_zmienne.passwd_correct(passwd1, passwd2):
        print('Haslo ok')
        break


print('Dalej')
