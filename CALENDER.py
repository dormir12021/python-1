from time import sleep
def leap_year(a):
    if a % 400 == 0 or a % 4 == 0:
        print(f'\033[1;32m{year} is a leap year\033[m')
    else:
        print(f"\033[1;34m{year} is not a leap year \033[m")
    



while True:
    try:
        year = int(input('Year: '))
        print('Checking')
        sleep(2)
    except Exception:
        print('\033[1;41m Invalid!\033[m')
    else:
        if year <= 0:
            print("\033[1;41m Invalid, don't use negative numbers.\033[m")
            continue
        break
print('Loading')
sleep(2)
leap_year(year)
