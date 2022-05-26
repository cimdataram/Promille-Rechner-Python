def promille_rechner():
    # Input und Plausibilibätskontrolle für Gewicht
    while True:
        print('Bitte Gewicht in kg angeben: ') 
        try:
            m = int(input())
            while m < 45:
                print(
    '''Ihr Gewicht sollte mindestens 45kg betragen,
    sonst bitte sofort einen Arzt aufsuchen,
    oder ein Gewicht ab 45 kg eingeben: ''')
                m = int(input())
        except ValueError:
            print('Bitte eine Ganzzahl angeben: ')
            continue
        break

    # Input und Plausibilibätskontrolle für Geschlecht
    rkey = ''
    while rkey != 'm' and rkey != 'w':
        print('Sind Sie (m)ännlich oder (w)eiblich?')
        rkey = input()

    geschlecht = {'w' : 6, 'm' : 7}
    r = geschlecht[rkey]

    # Input und Plausibilibätskontrolle für Getränk
    trunk = 0
    print('Was haben Sie getrunken?')
    trunk = input()
    while len(trunk) < 2 or trunk == trunk.strip() == '':
        print('Bitte geben Sie ein echtes Getränk ein: ')
        trunk = input()

    # Input und Plausibilibätskontrolle für Menge
    status = ''
    while True:
        print('Wie viel Liter '+trunk+' haben Sie getrunken?')
        try:
            V = float(input())
            while V < 0.01:
                print('Dann ist doch alles gut. keine Sorge :-)')
                status = 'stop'
                break
        except ValueError:
            print('Bitte eine Zahl angeben: ')
            continue
        break


    # Input und Plausibilibätskontrolle für Alkoholanteil
    if status != 'stop':
        while True:
            print('Wie viel Prozent Alkohol hatte Ihr '+trunk+'?:')
            E = input()
            e = E.strip('%')
            e = e.strip(' ')
            try:
                e = float(e)
                while e > 100:
                    print('Bitte geben Sie maximal 100% an')
                    E = input()
                    e = E.strip('%')
                while e > 85:
                    print('Suchen Sie umgehend einen Arzt auf, falls Sie das hier überhaupt noch lesen können.')
                    E = input()
                    e = E.strip('%')
                while e < 0.001:
                    print('Dann ist doch alles gut. keine Sorge :-)')
                    status = 'stop'
                    break
            except ValueError:
                print('Bitte eine Prozentzahl angeben. ')
                continue
            break


        if status != 'stop':
            A = ((float(V)*1000)/1) * (float(e)/100) * 0.8
            print('Aufgenommene Masse Alkohol: ', round(A, 2), 'Gramm')

            w = A / ((float(m)/1) * (float(r)/10))
            print('Promille: ', round(w, 2))


    return round(w, 2)


promille_rechner()

