def klein_gross_rechner (zahl1, zahl2):


    if (zahl1.isnumeric() == False):
        print('Bitte geben sie eine zahl ein')
        exit()



    if (zahl2.isnumeric() == False):
        print('Bitte geben sie eine Zahl ein')
        exit()

    if (zahl1 == zahl2):
        print('Die beiden Zahlen sind Gleich')

    if (zahl1 > zahl2):
        print(zahl1 + ' ist größer als ' + zahl2)

    if (zahl1 < zahl2):
        print(zahl1 + ' ist kleiner als ' + zahl2)

klein_gross_rechner('2', '5')

