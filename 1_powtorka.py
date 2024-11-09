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
pass_ok = True
while True:
    passwd1 = input('Podaj haslo: ')
    passwd2 = input('Powtorz haslo: ')
    if passwd1 != passwd2:
        print('hasla NIE SĄ takie same')
        pass_ok = False
    if len(passwd1) < 5:
        print('Zla dlugosc dlugosc')
        pass_ok = False
    if '.' not in passwd1:
        print('Brak znaku specjalnego')
        pass_ok = False
    if pass_ok:
        break


print('Dalej')
