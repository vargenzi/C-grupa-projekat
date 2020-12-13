korisnici = {}
vozila = {}
podaci_o_kupovini = {}
vozila_lista = []

def prijava():
    file = open("korisnici.txt", "r")
    for info in file.readlines():
        sadrzaj = info.split('|')
        korisnici[sadrzaj[0]] = sadrzaj[1:-1]
    file.close()

    print("Pre pristupa programu morate da se prijavite!")
    sa_bez_naloga = input("Unesite 1 ako vec imate nalog,a 2 ukoliko se prvi put prijavljujete >>")
    while True:
        korisnicko_ime = input("Unesite korisnicko ime >>")
        if sa_bez_naloga == "2":
            if korisnicko_ime in korisnici.keys():
                print("Korisnicko ime vec postoji!")
                print("Ne mozete uneti postojece korisnicko ime! Unesite ponovo!")
            else:
                lozinka = input("Unesite lozinku >>")
                ime = input("Unesite vase ime >>")
                prezime = input("Unesite vase prezime >>")
                pol = input("Unesite pol >>")
                uloga0 = "kupac"
                podaci_o_korisniku = lozinka + "|" + ime + "|" + prezime + "|" + pol + "|" + uloga0
                podaci = podaci_o_korisniku.split('|')
                korisnici[korisnicko_ime] = podaci
                print("Uspesno ste se prijavili!")
                file = open("korisnici.txt", "a")
                file.write("\n" + korisnicko_ime + "|" + podaci_o_korisniku)
                file.close()
                return uloga0
        elif sa_bez_naloga == "1":
            while True:
                administrator_kupac = input("Unesite vasu ulogu - administrator/kupac >>")
                if administrator_kupac == "administrator" and administrator_kupac in korisnici[korisnicko_ime]:
                    while True:
                        admin_lozinka = input("Unesite lozinku >>")
                        if admin_lozinka in korisnici[korisnicko_ime]:
                            print("Uspesno ste se prijavili kao administrator!")
                            uloga1 = "administrator"
                            return uloga1
                        else:
                            print("Uneli ste pogresnu lozinku! Pokusajte ponovo!")
                elif administrator_kupac == "kupac" and administrator_kupac in korisnici[korisnicko_ime]:
                    while True:
                        kupac_lozinka = input("Unesite lozinku >>")
                        if kupac_lozinka in korisnici[korisnicko_ime]:
                            print("Uspesno ste se prijavili kao kupac!")
                            uloga2 = "kupac"
                            return uloga2
                        else:
                            print("Uneli ste pogresnu lozinku! Pokusajte ponovo!")
                else:
                    print("Uneli ste nepostojecu ili netacnu ulogu! Uloge su administrator ili kupac! Unesite ponovo!")


def ucitaj_vozila_u_recnik():
    file = open("vozila.txt", "r")
    for automobili in file.readlines():
        podaci = automobili.split('|')
        vozila[podaci[0]] = podaci[1:-1]
    file.close()


def prikazi_dostupna_vozila():
    ucitaj_vozila_u_recnik()
    print("Sifra   Marka   Boja   Broj vrata            Opis            Vrsta goriva   Cena   Stanje")
    for keys, valu in vozila.items():
        if "na stanju" in vozila[keys]:
            print(keys, end="  ")
            for val in valu:
                print(val, end="   ")
            print("\n")


def meni_za_gosta():
    print("Aplikaciji pristupate kao gost!")
    print("***************************Meni***************************")
    print("1. Prikazi sva vozila koja su dostupna za kupovinu")
    print("2. Pretrazi vozila po marki, boji, opisu ili vrsti goriva")
    print("3. Sortiraj vozila po broju vrata ili ceni")
    print("x  Izlaz")


def pretraga_vozila():
    i = 0
    ucitaj_vozila_u_recnik()
    print("Dostupni parametri: \n 1. marka \n 2. boja \n 3. opis \n 4. vrsta goriva/pogona ")
    pretraga_po = input("Unesite po kom parametru zelite da pretrazite vozila >>")
    if pretraga_po == "1":
        marka = input("Unesite marku vozila koju zelite da pretrazite >>")
        for keys, valu in vozila.items():
            if marka in vozila[keys] and "na stanju" in vozila.keys():
                print(keys, end="  ")
                for val in valu:
                    print(val, end="   ")
                print("\n")
                i = 1

        if i == 0:
            print("Trenutno nemamo nijedno vozilo marke koje ste uneli!")
    elif pretraga_po == "2":
        boja = input("Unesite boju vozila koju zelite da pretrazite >>")
        for keys, valu in vozila.items():
            if boja in vozila[keys] and "na stanju" in vozila[keys]:
                print(keys, end="  ")
                for val in valu:
                    print(val, end="   ")
                print("\n")
                i = 1

        if i == 0:
            print("Trenutno nemamo nijedno vozilo boje koje ste uneli!")
    elif pretraga_po == "3":
        opis = input("Unesite opis vozila koji zelite da pretrazite >>")
        for keys, valu in vozila.items():
            if opis in vozila[keys] and "na stanju" in vozila.keys():
                print(keys, end="  ")
                for val in valu:
                    print(val, end="   ")
                print("\n")
                i = 1

        if i == 0:
            print("Trenutno nemamo nijedno vozilo opisa kojeg ste uneli!")
    elif pretraga_po == "4":
        pogon = input("Unesite boju vozila koju zelite da pretrazite >>")
        for keys, valu in vozila.items():
            if pogon in vozila[keys] and "na stanju" in vozila.keys():
                print(keys, end="  ")
                for val in valu:
                    print(val, end="   ")
                print("\n")
                i = 1

        if i == 0:
            print("Trenutno nemamo nijedno vozilo pogona kojeg ste uneli!")
    else:
        print("Uneli ste nepostojecu mogućnost!")


def ucitaj_vozila_iz_recnika_u_listu(line):
    podaci = line.split('|')
    return podaci


def BrojanjeRedova():
    file = open("vozila.txt", "r")
    j = 0
    for item in file.readlines():
        j += 1
    return j


def ucitaj_u_recnik(l):
    vozila_lista.append({l[0]:l[1], l[2]:l[3], l[4]:l[5], l[6]:l[7], l[8]:l[9], l[10]:l[11], l[12]:l[13], l[14]:l[15]})



def bubble_sort(key, list_od_dicts):
    new_list = list_od_dicts.copy()
    swaps = 1  # True
    while swaps != 0:  # while swaps:
        swaps = 0  # swaps = False
        for i in range(len(new_list) - 1):
            if new_list[i][key] > new_list[i + 1][key]:
                temp = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = temp
                swaps += 1  # swaps = True
    return new_list


def sortiraj_vozila():
    ucitaj_vozila_iz_recnika_u_listu()
    print(vozila_lista)
    # print('Sort po broju vrata! (rastuce):', bubble_sort("broj vrata", vozila_lista))
    """
    for keys, valu in vozila.items():
        if valu[2] == "2":
            print(keys, end=" ")
            print(valu)
    for keys, valu in vozila.items():
        if valu[2] == "4":
            print(keys, end=" ")
            print(valu)
    """


def administrator_meni():
    print("Aplikaciji pristupate kao administrator!")
    print("***************************Meni***************************")
    print("1. Prikazi sve kupce")
    print("2. Dodaj kupca")
    print("3. Izmeni postojeceg kupca")
    print("4. Obrisi kupca")
    print("5. Prikazi sva vozila")
    print("6. Dodaj vozilo")
    print("7. Izmeni postojece vozilo")
    print("x  Izlaz")


if __name__ == '__main__':
    print("******Dobrodosli u aplikaciju prodavnice vozila!******")
    prijavi_se = input("Zelite li da se prijavite? \n 1. Da \n 2. Ne \n Unesite broj >>")
    if prijavi_se == "1":
        uloga = prijava()
        if uloga == "administrator":
            administrator_meni()
            izbor = input("Izaberite opciju >>")
            if izbor == "1":
                print()
            elif izbor == "2":
                print()
            elif izbor == "3":
                print()
            elif izbor == "4":
                print()
            elif izbor == "5":
                print()
            elif izbor == "6":
                print()
            elif izbor == "7":
                print()
            elif izbor == "x":
                quit()
    elif prijavi_se == "2":
        meni_za_gosta()
        izbor = input("Izaberite opciju >>")
        if izbor == "1":
            prikazi_dostupna_vozila()
        elif izbor == "2":
            pretraga_vozila()
        elif izbor == "3":
            file = open("vozila.txt", "r")
            f = file.readlines()
            i = 0
            for line in f:
                l = ucitaj_vozila_iz_recnika_u_listu(line)
                vozila = ucitaj_u_recnik(l)
            print(vozila_lista)
        elif izbor == "x":
            quit()
