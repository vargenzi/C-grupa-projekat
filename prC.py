korisnici = {}
vozila = {}
podaci_o_kupovini = {}
vozila_lista = []

def prijava():
    file = open("korisnici.txt", "r")
    for info in file.readlines():
        sadrzaj = info.split('|')
        korisnici[sadrzaj[0]] = sadrzaj[1:]
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
                file.write(korisnicko_ime + "|" + podaci_o_korisniku)
                file.close()
                return uloga0
        elif sa_bez_naloga == "1":
            while True:
                administrator_kupac = input("Unesite vasu ulogu - administrator/kupac >>")
                if administrator_kupac == "administrator" and administrator_kupac in korisnici[korisnicko_ime][4].strip("\n"):
                    while True:
                        admin_lozinka = input("Unesite lozinku >>")
                        if admin_lozinka == korisnici[korisnicko_ime][0]:
                            print("Uspesno ste se prijavili kao administrator!")
                            uloga1 = "administrator"
                            return uloga1
                        else:
                            print("Uneli ste pogresnu lozinku! Pokusajte ponovo!")
                elif administrator_kupac == "kupac" and administrator_kupac == korisnici[korisnicko_ime][4].strip("\n"):
                    while True:
                        kupac_lozinka = input("Unesite lozinku >>")
                        if kupac_lozinka == korisnici[korisnicko_ime][0]:
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
def prikaz_kupaca():
    f = open("korisnici.txt", "r")
    linije = f.readlines()
    f.close()
    for line in linije:
        sadrzaj = line.split("|")
        if sadrzaj[5].strip("\n") == "kupac":
            print("-------------------------------------------")
            print("Korisnicko ime je >>" + sadrzaj[0])
            print("Ime je >>" + sadrzaj[2])
            print("Prezime je >>" + sadrzaj[3])
            print("Pol je >>" + sadrzaj[4])

def dodavanje_kupca():
    f = open("korisnici.txt", "r")
    linije = f.readlines()
    f.close()
    for line in linije:
        sadrzaj = line.split("|")
        korisnici[sadrzaj[0]] = sadrzaj[1:]
    f = open("korisnici.txt", "a")
    while True:
        korisnicko_ime = input("Unesite korsnicko ime novog kupca:")
        if korisnicko_ime in korisnici.keys():
            print("Uneli ste ime koje ne je vec zauzeto")
        elif korisnicko_ime not in korisnici.keys():
            lozinka = input("Ueti lozinku novog kupca >>")
            ime = input("Uneti ime novog kupca >>")
            prezime = input("Uneti prezime novog kupca >>")
            pol = input("Uneti pol novog kupca >>")
            f.write("\n" + korisnicko_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + pol + "|" + "kupac")
            f.close()
            return "Uspesno dodat kupac"

def meni_izmena():
    print("1 Promenite ime kupca.")
    print("2 Promenite prezime kupca.")
    print("3 Promenite lozinku kupca.")
    print("4 Upis, zavrsavanje koda.")

def izmeni_kupca():
    f = open("korisnici.txt", "r")
    linije = f.readlines()
    f.close()
    lista2 = []
    for line in linije:
        sadrzaj = line.split("|")
        korisnici[sadrzaj[0]] = sadrzaj[1:]
        lista2.append(sadrzaj[0])

    bul = True
    while bul:
        meni_izmena()
        prov = input("Unesite vas izbor >>")
        if prov == "1":
            korisnik = input("Unesite korsnicko ime kojeg korsinika zelite da menjate >>")
            if korisnik not in korisnici.keys():
                print("Nepostojeci korisnik.")
            elif korisnik in korisnici.keys() and korisnici[korisnik][4].strip("\n") == "kupac":
                ime = input("Unesite novo ime >>")
                korisnici[korisnik][1] = ime

        elif prov == "2":
            korisnik = input("Unesite korsnicko ime kojeg korsinika zelite da menjate >>")
            if korisnik not in korisnici.keys():
                print("Nepostojeci korisnik.")
            elif korisnik in korisnici.keys() and korisnici[korisnik][4].strip("\n") == "kupac":
                prezime = input("Unesite novo prezime >>")
                korisnici[korisnik][2] = prezime

        elif prov == "3":
            korisnik = input("Unesite korsnicko ime kojeg korsinika zelite da menjate >>")
            if korisnik not in korisnici.keys():
                print("Nepostojeci korisnik.")
            elif korisnik in korisnici.keys() and korisnici[korisnik][4].strip("\n") == "kupac":
                lozinka = input("Unesite novu lozinku >>")
                korisnici[korisnik][0] = lozinka

        elif prov == "4":
            f = open("korisnici.txt", "w")
            print("Gotovo sa promenama, kraj izvrsavanja koda.")
            i = 0
            for item in korisnici:
                f.write(lista2[i] + "|" + korisnici[lista2[i]][0] + "|" + korisnici[lista2[i]][1] + "|" + korisnici[lista2[i]][2] + "|" + korisnici[lista2[i]][3] + "|" + korisnici[lista2[i]][4])
                i += 1
            f.close()
            bul = False
        elif prov not in ["1", "2", "3", "4"]:
            print("uneli ste neponudjenu komadnu. Unesite ponovo.")


def meni_brisanje():
    print("1 Banujte korsinika.")
    print("x Izadjite iz programa.")



def briasanje_kupca():
    f = open("korisnici.txt", "r")
    linije = f.readlines()
    f.close()
    lista2 = []
    for line in linije:
        sadrzaj = line.split("|")
        korisnici[sadrzaj[0]] = sadrzaj[1:]
        lista2.append(sadrzaj[0])
    bul = True
    while bul:
        meni_brisanje()
        prov = input("Unesite vas izbor >>")
        if prov == "1":
            korisnik = input("Unesite ime korisnika >>")
            if korisnik in korisnici.keys() and korisnici[korisnik][4].strip("\n"):
                korisnici[korisnik][4] = "banovan\n"
            elif korisnik not in korisnici.keys():
                print("Ovaj korisnik ne postoji u nasoj bazi podataka.")
        elif prov == "x":
            bul = False
            f = open("korisnici.txt", "w")
            print("Gotovo sa brisanjem.")
            i = 0
            for item in korisnici:
                f.write(lista2[i] + "|" + korisnici[lista2[i]][0] + "|" + korisnici[lista2[i]][1] + "|" + korisnici[lista2[i]][2] + "|" + korisnici[lista2[i]][3] + "|" + korisnici[lista2[i]][4])
                i+=1
            f.close()
        elif prov == ["1", "x"]:
            print("Uneli ste pogresnu komandu.")


def prikaz_svih_vozila():
    f = open("vozila.txt", "r")
    linije = f.readlines()
    for line in linije:
        sadrzaj = line.split("|")
        print("-------------------------------------")
        print(sadrzaj[0] + " je " + sadrzaj[1])
        print(sadrzaj[2] + " je " + sadrzaj[3])
        print(sadrzaj[4] + " je " + sadrzaj[5])
        print(sadrzaj[6] + " je " + sadrzaj[7])
        print(sadrzaj[8] + " je " + sadrzaj[9])
        print(sadrzaj[10] + " je " + sadrzaj[11])
        print(sadrzaj[12] + " je " + sadrzaj[13])
        print(sadrzaj[14] + " je " + sadrzaj[15])






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
                prikaz_kupaca()
            elif izbor == "2":
                dodavanje_kupca()
            elif izbor == "3":
                izmeni_kupca()
            elif izbor == "4":
                briasanje_kupca()
            elif izbor == "5":
                prikaz_svih_vozila()
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
