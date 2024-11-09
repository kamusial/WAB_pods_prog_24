# program do rejestracji
# program sprawdza, czy uzytkownik juz istnieje
# haslo wpisujemy 2 razy - musi byc takie samo

# sprawdz bezpieczenstwo hasla

username_list = ['Kamil', 'Dixi', 'Warszawa01']
username = input('Podaj nazwe uzytkownika:  ')

while True:
    username = input('Podaj nazwe uzytkownika:  ')
    if username not in username_list:
        break

while True:
    pass_ok = True
    passwd1 = input('Podaj haslo: ')
    passwd2 = input('Powtorz haslo: ')
    if passwd1 != passwd2:
        print('hasla NIE SĄ takie same')
        pass_ok = False
    if len(passwd1) < 5:
        print('Haslo za krotkie')
        pass_ok = False
    if '.' not in passwd1:
        print('Brak znaku specjalnego')
        pass_ok = False
    if passwd1 == passwd1.lower():
        print('Brak duzej litery')
        pass_ok = False
    if passwd1 == passwd1.upper():
        print('Brak malej litery')
        pass_ok = False
    if pass_ok:
        print('Haslo ok')
        break


print('Dalej')
