from random import randint
import Klasy

def tekst(a,b):
    while a<=b:
        print(linecache.getline('kuc2.txt', a))
        a=a+1

def smierc():
    with open('dead.txt', 'r') as p:
        dead_banner = ""
        for line in p:
            dead_banner += line

        print(dead_banner)

nr = 1

def pokoj2():
    enemy = Klasy.Wielki_Szczur()
    tekst(1, 3)
    x = input()
    if x == '1':
        tekst(4, 4)
    elif x == '2':
        tekst(5, 5)
    else:
        tekst(6, 6)
        raise Klasy.WrongChoiceException()
    print("Napotykasz", enemy.name, "Wyczuwam kłopoty")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa != 15:
        return 3
    else:
        return 15


def wybor_drogi_03():
    tekst(7, 10)
    x = input()
    if x == '1':
        return 4
    elif x == '2':
        return 10
    else:
        tekst(11, 11)
        raise Klasy.WrongChoiceException()


def pokoj4():
    enemy = Klasy.Wrog_zbrodniczego_Rezimu()
    print("Droge zastepuje ci", enemy.name, " Bron sie!")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa != 15:
        return 5
    else:
        return 15


def uczta():
    tekst(12, 15)
    a = input()
    if a == '1':
        tekst(16, 16)
        return randint(2, 5)
    elif a == '2':
        tekst(17, 19)
        b = input()
        if b == '1':
            tekst(20, 20)
            return randint(6, 10)
        elif b == '2':
            tekst(21, 21)
            return 15
        else:
            tekst(22, 22)
            raise Klasy.WrongChoiceException()
    else:
        tekst(23, 23)
        return 6


def wybor_drogi_06():
    tekst(24, 27)
    x = input()
    if x == '1':
        return 7
    elif x == '2':
        return 8
    else:
        tekst(28,28)
        raise Klasy.WrongChoiceException()


def pokoj7():
    with open('pokoj7.txt') as p7:
        for line in p7:
            print(line, end='')
        print("\n")
        tknij = input()
        if tknij == '1':
            print('Coz za przezornosc!')
        elif tknij == '2':
            gracz.health = gracz.health - 5
            if gracz.health <= 0:
                tekst(29,29)
                return 15
            else:
                print(
                    "Kretyn. Glony wsysaja Twoja dlon, przez co jest poparzona, fioletowa i sliska. No i tracisz 5 zdrowia, wiec wynosi ono",
                    gracz.health, "\nGratuluje.")
        else:
            tekst(30,30)
            raise Klasy.WrongChoiceException()
        tekst(31, 31)
        podejdz = input(
            '1. Podejdz do drugiej celi. \n2. Zostan przy kocie.  \n3. Uciekaj stamtad, nie jestes tu na pogaduszkach z futrzakami.')
        if podejdz == '3':
            return 6
        elif podejdz == '2':
            tekst(32,32)
        elif podejdz == '1':
            tekst(33,35)
        enemy = Klasy.Straz_Krolowej_Kucy()
        walka = Klasy.Walka()
        walka.walka(gracz, enemy)
        tekst(36, 38)
        towarzysz = input("Kogo chcesz uwolnic? \n1. Kota \n2. Psa \n3. Obojga")
        if towarzysz == '1':
            tekst(39,40)
            gracz.add_staff('Towarzysz Kot')
            return 8
        elif towarzysz == '2':
            tekst(41,43)
            gracz.add_staff('Towarzysz Pies')
            return 8
        elif towarzysz == '3':
            tekst(44,45)
            gracz.add_staff('Towarzysz Kot')
            return 8
        else:
                raise Klasy.WrongChoiceException()


def pokoj8():
    enemy = Klasy.Wrog_zbrodniczego_Rezimu()
    print("O nie! to kolejny", enemy.name, " chce cie powstrzymac przed dotarciem na bal!")
    print("Jego zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa != 15:
        return 9
    else:
        return 15


def szafa():
    tekst(46,53)
    a = 0
    while a == 0:
        x = int(input())
        if x == 1:
            tekst(54,54)
        elif x > 1 and x < 4:
            tekst(55,55)
            return 11
        elif x == 4:
            tekst(56,56)
            return 15
        else:
            tekst(57,57)

def szyfr():
    tekst(58,60)
    a = input()
    if a == '1':
        return 3
    elif a == '2':
        tekst(61,63)
        szanse = 0
        z = 5
        y = randint(0, 9)
        x = randint(0, 9)
        if x > y:
            y, x = x, y
        else:
            pass
        suma = z + y + x
        print("Suma:", suma)
        while szanse < 3:
            szanse += 1
            a = int(input("Wpisz pierwsza cyfre"))
            b = int(input("Wpisz druga cyfre"))
            c = int(input("Wpisz trzecia cyfre"))
            if a != z or b != y or c != x:
                tekst(64,64)
                if szanse == 3:
                    tekst(65,65)
                    return 3
            else:
                tekst(66,67)
                return 11
    else:
        tekst(68,68)
        return 3

def medrzec():
    zg = 0
    zm = 0
    tekst(69,69)
    while zm < 3 and zg < 3:
        m = randint(1, 3)
        tekst(70,73)
        g = int(input())
        if m == g:
            print("Mamy impas. Sprobujmy ponownie")
        elif m == 1 and g == 2:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 1 and g == 3:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 2 and g == 1:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 2 and g == 3:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 3 and g == 1:
            print("HA! Wiedzialem, ze tak zrobisz!")
            zm += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        elif m == 3 and g == 2:
            print("Miales zwyczajnie szczescie...")
            zg += 1
            print("//Zwycięstwa gracza =", zg)
            print("//Zwycięstwa medrca =", zm)
        else:
            tekst(74,75)
            zm += 1

        if zg == 3:
            tekst(76,76)
            return 12
        elif zm == 3:
            tekst(77,77)
            return 4


def pokoj12():
    enemy = Klasy.Siostry_Godlewskie()
    print("Tego sie nie spodziewales. Przejscia pilnuja", enemy.name, "Probujesz uciec, ale drzwi sie za toba zamknely.\n")
    print("Ich zycie to", enemy.health)
    walka = Klasy.Walka()
    pa = walka.walka(gracz, enemy)
    if pa==15:
        tekst(78,79)
        if gracz.staff[1] != '':
            tekst(80,80)
            if gracz.staff[1] == 'Towarzysz Pies':
                tekst(81,81)
            elif gracz.staff[1] == 'Towarzysz Kot':
                tekst(82,82)
            else:
                return 15
            tekst(83,83)
            return 13
        else:
            tekst(84,84)
            return 15
    else:
        return 15


def pokoj13():
    if gracz.staff[1] == 'Towarzysz Pies':
        tekst(85,85)
        pogladz = int(input('Chcesz poglaskac pieska?\n 1. Jasne, ze tak, nie jestem kutafonem/bezdusznym sukinsynem \n 2.Jestem kutafonem'))
        if pogladz == 1:
          tekst(86,86)
          return 14
        else:
          raise Klasy.WrongChoiceException()
    else:
        tekst(87,87)
        odpowiedz = int(input('1. Odkrzyknij: Niech żyje zdbrodniczy rezim\n2. Zwyzywaj kota za zdrade'))
        if odpowiedz == 1:
            tekst(88,88)
            return 15
        elif odpowiedz == 2:
            tekst(89,89)
            return 15
        else:
            raise Klasy.WrongChoiceException()


def zakonczenie():
    str = "  GRATULACJE  "
    print(str.center(80, '*'))
    tekst(90,116)


while nr != 15:
    print("Pokoj nr ", nr)
    if nr == 1:
        with open('kuc.txt') as prt:
            for line in prt:
                print(line, end='')
        print("\n")
        with open('prologue.txt') as pro:
            for line in pro:
                print(line, end='')
        print("\n")
        a = input('Wybierz postac:\n1. Nikt Ciekawy \n2. Ogr \n3. Elf \n\nNumer mojej postaci to ')
        if a == '1':
            gracz = Klasy.Nikt_Ciekawy()
            gracz.name = input(
                'Nazwij swoją nudną i przecietna postac...nie chce straszyc ale ogrem przynajmniej mialbys szansę...')
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        elif a == '2':
            gracz = Klasy.Ogr()
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        elif a == '3':
            gracz = Klasy.Elf()
            gracz.name = input(
                'Z takim życiem daję Ci dwa pokoje, to najprawdopodobniej Twój największy błąd. Pasowałby Ci Nikt Ciekawy ;p. No dajesz, nazwij się jakoś oryginalnie')
            print("Twoje parametry to")
            print("imie:", gracz.name)
            print("zycie:", gracz.health)
            print("atak:", gracz.atak1)
            print("zacny atak:", gracz.atak2)
        else:
            print('Jestes idiota')
            raise Klasy.WrongChoiceException()
        czy = input("Czy chcesz wylosować tajemniczy przedmiot? \n1. Tak \n2. Nie ")
        if czy == '1':
            x = randint(1, 10)
            if x < 5:
                print("wylosowałeś noz! gratki, +4 do ataku")
                gracz.add_staff('noz')
                gracz.atak1 = gracz.atak1 + 4
                gracz.atak2 = gracz.atak2 + 4
                print("Twoje ataki to teraz\natak", gracz.atak1, "\nzacny atak", gracz.atak2, "\n a wyposazenie to",
                      gracz.staff)
                nr = 2
            elif x > 4 and x < 9:
                print("wylosowałes chelm, +4 do zycia. Nie ciesz sie, i tak zginiesz zanim dojdziesz do polowy gry")
                gracz.add_staff('chelm')
                gracz.health = gracz.health + 4
                print("Twoje zycie to teraz", gracz.health, "\na wyposazenie to", gracz.staff)
                nr = 2
            else:
                print("wylosowales 'Nagly zgon'. brawo. nie zyjesz")
                nr = 15
        elif czy == '2':
            print("Jestes tchorzem! Skoro nie chcesz nawet losowac, to nie możesz pojechać na bal. Giniesz deklu")
            nr = 15
        else:
            print("Nie umiesz odpowiadać na pytania. Wedle woli wszechwładnej Krolowej Kucy oznacza to smierc!")
            raise Klasy.WrongChoiceException()

    elif nr == 2:
        nr = pokoj2()
    elif nr == 3:
        nr = wybor_drogi_03()
    elif nr == 4:
        nr = pokoj4()
    elif nr == 5:
        nr = uczta()
    elif nr == 6:
        nr = wybor_drogi_06()
    elif nr == 7:
        nr = pokoj7()
    elif nr == 8:
        nr = pokoj8()
    elif nr == 9:
        nr = szafa()
    elif nr == 10:
        nr = szyfr()
    elif nr == 11:
        nr = medrzec()
    elif nr == 12:
        nr = pokoj12()
    elif nr == 13:
        nr = pokoj13()
    elif nr == 14:
        nr = zakonczenie()
    else:
        print("ciekawe")

if nr == 15:
    smierc()
