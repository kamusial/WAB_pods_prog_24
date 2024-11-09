def welcome():
    print('Witamy w programie')


passwd = '1234'
user_passwd = input('Podaj haslo:   ')
if user_passwd == passwd:
    welcome()


