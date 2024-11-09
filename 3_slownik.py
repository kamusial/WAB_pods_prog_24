lidl = {'maslo': 8, 'mleko': 3.5, 'jablko': 4, 'ser': 12}
biedronka = {'maslo': 6, 'mleko': 4.5, 'jablko': 3, 'ser': 13}
aldi = {'maslo': 9, 'mleko': 2.5, 'jablko': 0, 'ser': 15}
# user wpisuje czego i ile chce kupić
# program zwraca tajtańszy sklep

products_to_buy = {}

while True:
    product = input('Co chcesz kupic?  ')
    pcs = float(input(f'Ile {product} chcesz kupic?  '))
    products_to_buy[product] = pcs
    decission = input('Kolejny produkt?  T/N:  ')
    if decission == 'N':
        break
print(products_to_buy)

price_lidl = 0
price_biedronka = 0
price_aldi = 0

for product in products_to_buy.keys():
    price_lidl += lidl[product] * products_to_buy[product]
    price_biedronka += biedronka[product] * products_to_buy[product]
    price_aldi += aldi[product] * products_to_buy[product]

print(f'Cena w Lidl to {price_lidl}zl')
print(f'Cena w Biedronce to {price_biedronka}zl')
print(f'Cena w Aldi to {price_aldi}zl')


