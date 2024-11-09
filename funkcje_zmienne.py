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

def passwd_correct(pass1, pass2):
    if pass1 == pass2:
        if len(pass1) >= 5:
            return True
    return False
