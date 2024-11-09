# program przyjmuje dane o aucie:
# rocznik, marka, przebieg, stan

# program sprawdza poprawność danych
# program sprawdza, czy marka dostępna na polskim rynku
# program sprawdza, czy kierowca może ubezpieczyć auto
# program liczy składkę ubezpieczenie
import funkcje_zmienne
marki = ['BMW', 'Volvo', 'Fiat', 'Daab', 'Citroen', 'Subaru']
marki_PL = ['BMW', 'Volvo', 'Subaru']

while True:
    rocznik = int(input('Wprowadz rocznik:  '))
    marka = input('Wprowadz markę:  ')
    przebieg = float(input('Wprowadz przebieg:  '))
    stan = int(input('Wprowadz stan 1 - 5:  '))
    if 1970 < rocznik < 2025 and \
        marka in marki_PL and \
        0 < przebieg < 1000000 and \
        1 <= stan <= 5:
        print('Dane poprawne')
        break
    else:
        print('niepoprawne dane')

print('Dalej, dalej kierowny')
wiek = int(input('Wiek kierowcy: '))
if funkcje_zmienne.allowed_to_insure(wiek):
    print('Ok')
    print(f'skladka wynosi {funkcje_zmienne.skladka(rocznik, marka, przebieg, stan)}')
else:
    print('Ten kierowca nie może ubezpiecznyć pojazdu')