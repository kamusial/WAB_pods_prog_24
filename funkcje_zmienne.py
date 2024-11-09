def skladka(wiek, plec, waga, czy_pali):
    total = 0
    if wiek <= 40:
        total += 100
    else:
        total += 200
    if plec == 'K':
        total -= 50
    if waga > 100:
        total += 3 * (waga - 100)
    if czy_pali:
        total += 200
    return total

my_dict = {'Kamil': 1}

def passwd_correct(passwd1, passwd2):
    pass_ok = True
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
    return pass_ok

def allowed_to_insure(age):
    if 24 < age < 80:
        return True
    return False

def skladka(rocznik, marka, przebieg, stan):
    total = 0
    total += (2025 - rocznik) * 50
    total += przebieg * 0.01
    if stan < 4:
        total += 500
    if marka == 'BMW':
        total += 200
    return total
