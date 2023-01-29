#Autor Yassin Zenasni
#Mail: a.zenasni55@gmail.com
#This Python Script is a simple Calculator with +  -  /  *
#Age 13

summe = 'Das Ergebnis ist: '


print('Geben Sie ihre Erste  Zahl ein ')
zahl1 = input()

if(zahl1.isnumeric() == False):
 print('Bitte geben sie eine zahl ein')
 exit()



print('Geben Sie ihre zweite Zahl ein ')
zahl2 = input()


if(zahl2.isnumeric() == False):
    print('Bitte geben sie eine Zahl ein')
    exit()


print('Geben sie ihren Operator ein   zb.  \n  1 => +  \n  2 => -  \n  3 => /  \n  4 => *         ')
operator = input()



if(operator == '1'):
    print(summe)
    print(int(zahl1) + int(zahl2))

if(operator == '2'):
    print(summe)
    print(int(zahl1) - int(zahl2))

if(operator == '3'):
    print(summe)
    print(int(zahl1) / int(zahl2))

if(operator == '4'):
    print(summe)
    print(int(zahl1) * int(zahl2))

