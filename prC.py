korisnici = {}
vozila = {}
podaci_o_kupovini = {}
vozila_lista = []
cuvanje_imena = ["1"]
def prijava():
    file = open("korisnici.txt", "r")
    for info in file.readlines():
        sadrzaj = info.split('|')
        korisnici[sadrzaj[0]] = sadrzaj[1:]
    file.close()

    print("Pre pristupa programu morate da se prijavite!")
    sa_bez_naloga = input("Unesite 1 ako vec imate nalog,a 2 ukoliko se prvi put prijavljujete >>")
    while True:
        while True:
            korisnicko_ime = input("Unesite korisnicko ime >>")
            if len(korisnicko_ime) < 1:
                print("Morate uneti korisnicko ime!!!")
            else:
                break
        if sa_bez_naloga == "2":
            if korisnicko_ime in korisnici.keys():
                print("Korisnicko ime vec postoji!")
                print("Ne mozete uneti postojece korisnicko ime! Unesite ponovo!")
            else:
                while True:
                    lozinka = input("Unesite lozinku >>")
                    if len(lozinka) < 1:
                        print("Morate uneti lozinku!!!")
                    else:
                        break
                while True:
                    ime = input("Unesite vase ime >>")
                    if len(ime) < 1:
                        print("Morate uneti ime!!!")
                    else:
                        break
                while True:
                    prezime = input("Unesite vase prezime >>")
                    if len(prezime) < 1:
                        print("Morate uneti prezime!!!")
                    else:
                        break
                while True:
                    pol = input("Unesite pol >>")
                    if len(pol) < 1:
                        print("Morate uneti pol!!!")
                    else:
                        break
                uloga0 = "kupac"
                podaci_o_korisniku = lozinka + "|" + ime + "|" + prezime + "|" + pol + "|" + uloga0 + "|"
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
                            cuvanje_imena[0] = korisnicko_ime
                            return uloga2
                        else:
                            print("Uneli ste pogresnu lozinku! Pokusajte ponovo!")
                else:
                    print("Uneli ste nepostojecu ili netacnu ulogu! Uloge su administrator ili kupac! Unesite ponovo!")


def ucitaj_vozila_u_recnik():
    file = open("vozila.txt", "r")
    for automobili in file.readlines():
        return automobili
    file.close()


def prikazi_dostupna_vozila():
    fajl = open("vozila.txt", "r")
    linije = fajl.readlines()
    for linija in linije:
        sadrzaj = linija.split("|")
        if sadrzaj[15] == "na stanju":
            print("-------------------------------------")
            print(sadrzaj[0] + ": " + sadrzaj[1])
            print(sadrzaj[2] + ": " + sadrzaj[3])
            print(sadrzaj[4] + ": " + sadrzaj[5])
            print(sadrzaj[6] + ": " + sadrzaj[7])
            print(sadrzaj[8] + ": " + sadrzaj[9])
            print(sadrzaj[10] + ": " + sadrzaj[11])
            print(sadrzaj[12] + ": " + sadrzaj[13])
            print(sadrzaj[14] + ": " + sadrzaj[15])


def meni_za_gosta():
    print("***************************Meni***************************")
    print("1. Prikazi sva vozila koja su dostupna za kupovinu")
    print("2. Pretrazi vozila po marki, boji, opisu ili vrsti goriva")
    print("3. Sortiraj vozila po broju vrata ili ceni")
    print("x  Izlaz")


def pretraga_vozila():
    i = 0
    check = 0
    ucitaj_vozila_u_listu()
    print("Dostupni parametri: \n 1. marka \n 2. boja \n 3. opis \n 4. vrsta goriva/pogona ")
    pretraga_po = input("Unesite po kom parametru zelite da pretrazite vozila >>")
    if pretraga_po == "1":
        marka = input("Unesite marku vozila koju zelite da pretrazite >>")
        while i < len(vozila_lista):
            if marka in vozila_lista[i]["marka"] and vozila_lista[i]["dostupnost"] == "na stanju":
                print(vozila_lista[i])
                check = 1
            i = i + 1

        if check == 0:
            print("Trenutno nemamo nijedno vozilo marke koje ste uneli!")
    elif pretraga_po == "2":
        boja = input("Unesite boju vozila koju zelite da pretrazite >>")
        while i < len(vozila_lista):
            if boja in vozila_lista[i]["boja"] and vozila_lista[i]["dostupnost"] == "na stanju":
                print(vozila_lista[i])
                check = 1
            i = i + 1

        if check == 0:
            print("Trenutno nemamo nijedno vozilo boje koje ste uneli!")
    elif pretraga_po == "3":
        opis = input("Unesite opis vozila koji zelite da pretrazite >>")
        while i < len(vozila_lista):
            if opis in vozila_lista[i]["opis"] and vozila_lista[i]["dostupnost"] == "na stanju":
                print(vozila_lista[i])
                check = 1
            i = i + 1

        if check == 0:
            print("Trenutno nemamo nijedno vozilo opisa kojeg ste uneli!")
    elif pretraga_po == "4":
        pogon = input("Unesite vrstu goriva vozila koju zelite da pretrazite >>")
        while i < len(vozila_lista):
            if pogon in vozila_lista[i]["Vrsta goriva"] and vozila_lista[i]["dostupnost"] == "na stanju":
                print(vozila_lista[i])
                check = 1
            i = i + 1

        if check == 0:
            print("Trenutno nemamo nijedno vozilo pogona kojeg ste uneli!")
    else:
        print("Uneli ste nepostojecu mogućnost!")


def ucitaj_vozila_u_listu():
    fajl = open("vozila.txt", "r")
    linije = fajl.readlines()
    for linija in linije:
        podaci = linija.split('|')
        vozila_lista.append(
            {podaci[0]: podaci[1], podaci[2]: podaci[3], podaci[4]: podaci[5], podaci[6]: podaci[7],
             podaci[8]: podaci[9], podaci[10]: podaci[11], podaci[12]: podaci[13], podaci[14]: podaci[15]})


def bubble_sort_rastuce(key, list_od_dicts):
    new_list = list_od_dicts.copy()
    swaps = 1
    while swaps != 0:
        swaps = 0
        for i in range(len(new_list) - 1):
            if new_list[i][key] > new_list[i + 1][key]:
                temp = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = temp
                swaps += 1
    return new_list


def bubble_sort_opadajuce(key, list_od_dicts):
    new_list = list_od_dicts.copy()
    swaps = 1
    while swaps != 0:
        swaps = 0
        for i in range(len(new_list) - 1):
            if new_list[i][key] < new_list[i + 1][key]:
                temp = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = temp
                swaps += 1
    return new_list


def sortiraj_vozila():
    element = 0
    ucitaj_vozila_u_listu()
    while True:
        sort_izbor = input("Unesite po cemu zelite da srtirate vozila \n 1. Po broju vrata \n 2. Po ceni \n >>")
        if sort_izbor == "1":
            while True:
                opadajuce_rasuce_izbor = input("Zelite li da sortirate 1. Opadajuce ili 2. Rastuce?"
                                               " Unesite vas izbor >>")
                if opadajuce_rasuce_izbor == "1":
                    print('Vozila sortirana opadajuce po broju vrata: \n')
                    sort_lista = bubble_sort_opadajuce("broj vrata", vozila_lista)
                    while element < len(sort_lista):
                        if sort_lista[element]["dostupnost"] == "na stanju":
                            print(sort_lista[element])
                        element += 1
                    break
                elif opadajuce_rasuce_izbor == "2":
                    print('Vozila sortirana rastuce po broju vrata: \n')
                    sort_lista = bubble_sort_rastuce("broj vrata", vozila_lista)
                    while element < len(sort_lista):
                        if sort_lista[element]["dostupnost"] == "na stanju":
                            print(sort_lista[element])
                        element += 1
                    break
                else:
                    print("Uneli ste ne postojecu opciju! Unesite ponovo!")
            break

        elif sort_izbor == "2":
            while True:
                opadajuce_rasuce_izbor = input("Zelite li da sortirate 1. Opadajuce ili 2. Rastuce? "
                                               "Unesite vas izbor >>")
                if opadajuce_rasuce_izbor == "1":
                    print('Vozila sortirana opadajuce po ceni: \n')
                    sort_lista = bubble_sort_opadajuce("cena", vozila_lista)
                    while element < len(sort_lista):
                        if sort_lista[element]["dostupnost"] == "na stanju":
                            print(sort_lista[element])
                        element += 1
                    break
                elif opadajuce_rasuce_izbor == "2":
                    print('Vozila sortirana rastuce po ceni: \n')
                    sort_lista = bubble_sort_rastuce("cena", vozila_lista)
                    while element < len(sort_lista):
                        if sort_lista[element]["dostupnost"] == "na stanju":
                            print(sort_lista[element])
                        element += 1
                    break
                else:
                    print("Uneli ste nepostojecu opciju! Unesite ponovo!")
            break
        else:
            print("Uneli ste nepostojecu opciju! Unesite ponovo!")


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
                f.write(lista2[i] + "|" + korisnici[lista2[i]][0] + "|" + korisnici[lista2[i]][1] + "|" +
                        korisnici[lista2[i]][2] + "|" + korisnici[lista2[i]][3] + "|" + korisnici[lista2[i]][4])
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
                f.write(lista2[i] + "|" + korisnici[lista2[i]][0] + "|" + korisnici[lista2[i]][1] + "|" +
                        korisnici[lista2[i]][2] + "|" + korisnici[lista2[i]][3] + "|" + korisnici[lista2[i]][4])
                i += 1
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


def prikaz_dostupnih_vozila():
        f = open("vozila.txt", "r")
        linije = f.readlines()
        print("Dostupna vozila su:")
        for line in linije:
            sadrzaj = line.split("|")
            if sadrzaj[15].strip("\n") == "na stanju":
                print("-------------------------------------")
                print(sadrzaj[0] + " je " + sadrzaj[1])
                print(sadrzaj[2] + " je " + sadrzaj[3])
                print(sadrzaj[4] + " je " + sadrzaj[5])
                print(sadrzaj[6] + " je " + sadrzaj[7])
                print(sadrzaj[8] + " je " + sadrzaj[9])
                print(sadrzaj[10] + " je " + sadrzaj[11])
                print(sadrzaj[12] + " je " + sadrzaj[13])
            elif sadrzaj[15].strip("\n") != "na stanju":
                print("Nema dostupnih vozila.")
                quit()




def kupovina_vozila():
    f = open("vozila.txt", "r")
    lala = f.readlines()
    recnik = {}
    listan = []
    i = 0
    f.close()
    for item in lala:
        sadrzaj = item.split("|")
        recnik[sadrzaj[1]] = sadrzaj
    for item in lala:
        sadrzaj = item.split("|")
        listan.append(sadrzaj[1])
    while True:
        print("-------------------------------------")
        sifra_vozila = input("Unesite sifru vozila koje zelite:")
        if sifra_vozila in recnik.keys():
            f = open("vozila.txt", "w")
            for item in listan:
                if sifra_vozila == listan[i]:
                    f.write("sifra" + "|" + listan[i] + "|" + "marka" + "|" + recnik[listan[i]][3] + "|" + "boja" + "|" +
                            recnik[listan[i]][5] + "|" + "broj vrata" + "|" + recnik[listan[i]][7] + "|" + "opis" + "|" +
                            recnik[listan[i]][9] + "|" + "vrsta goriva" + "|" + recnik[listan[i]][11] + "|" + "cena" + "|" +
                            recnik[listan[i]][13] + "|" + "dostupnost" + "|" + "nije na stanju" + "\n")
                elif sifra_vozila != listan[i]:
                    f.write("sifra" + "|" + listan[i] + "|" + "marka" + "|" + recnik[listan[i]][3] + "|" + "boja" + "|" +
                            recnik[listan[i]][5] + "|" + "broj vrata" + "|" + recnik[listan[i]][7] + "|" + "opis" + "|" +
                            recnik[listan[i]][9] + "|" + "vrsta goriva" + "|" + recnik[listan[i]][11] + "|" + "cena" + "|" +
                            recnik[listan[i]][13] + "|" + "dostupnost" + "|" + recnik[listan[i]][15])
                i += 1
            print("Uspenso je upisano u file.")
            return sifra_vozila
        elif sifra_vozila not in recnik.keys():
            print("Unesite ponovo sifru vozila, uneli ste neposotjecu.")


def zapisivanje_kupovinu(sifra_vozila, cuvanje_imena):
    i = 0
    f = open("kupovina.txt", "r")
    linije = f.readlines()
    for item in linije:
        i += 1
    f.close()
    sifrak = 0
    f = open("vozila.txt", "r")
    linije = f.readlines()
    for line in linije:
        sadrzaj = line.split("|")
        if sadrzaj[1] == sifra_vozila:
            cena = sadrzaj[13]
            sifricav = sifra_vozila
            sifrak = i + 1
    f.close()
    f = open("kupovina.txt", "a")
    f.write(str(sifrak) + "|" + cuvanje_imena[0] + "|" + sifricav +"|" + cena + "\n")
    f.close()



def prikaz_licnih_vozila(sacuvano_ime):
    f = open("kupovina.txt", "r")
    s = open("vozila.txt", "r")
    linije = f.readlines()
    linije2 = s.readlines()
    for item in linije:
        sadrzaj = item.split("|")
        if sacuvano_ime[0] == sadrzaj[1]:
            for info in linije2:
                sadrzaj2 = info.split("|")
                if sadrzaj[2] == sadrzaj2[1]:
                    print("----------------------------------")
                    print(sadrzaj2[2] + " je " + sadrzaj2[3])
                    print(sadrzaj2[4] + " je " + sadrzaj2[5])
                    print(sadrzaj2[6] + " je " + sadrzaj2[7])
                    print(sadrzaj2[8] + " je " + sadrzaj2[9])
                    print(sadrzaj2[10] + " je " + sadrzaj2[11])
                    print("-----------------------------------")
    f.close()
    s.close()




def administrator_meni():

    print("***************************Meni***************************")
    print("1. Prikazi sve kupce")
    print("2. Dodaj kupca")
    print("3. Izmeni postojeceg kupca")
    print("4. Obrisi kupca")
    print("5. Prikazi sva vozila")
    print("6. Dodaj vozilo")
    print("7. Izmeni postojece vozilo")
    print("x  Izlaz")

def kupac_meni():
    print("***************************Meni***************************")
    print("1. Prikazi sva dostupna vozila")
    print("2. Prikazi moja vozila")
    print("3. Kupi vozilo")
    print("x Izlaz")

if __name__ == '__main__':
    print("******Dobrodosli u aplikaciju prodavnice vozila!******")
    prijavi_se = input("Zelite li da se prijavite? \n 1. Da \n 2. Ne \n Unesite broj >>")
    if prijavi_se == "1":
        uloga = prijava()
        if uloga == "administrator":
            print("Aplikaciji pristupate kao administrator!")
            while True:
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
        elif uloga == "kupac":
            print("Aplikaciji pristupate kao kupac!")
            bul = True
            while True:
                kupac_meni()
                izbor = input("Izaberite opciju >>")
                if izbor == "1":
                    prikaz_dostupnih_vozila()
                if izbor == "2":
                    prikaz_licnih_vozila(cuvanje_imena)
                if izbor == "3" and bul == True:
                    sifra = kupovina_vozila()
                    zapisivanje_kupovinu(sifra, cuvanje_imena)
                    bul = False
                if izbor == "x":
                    quit()

    elif prijavi_se == "2":
        print("Aplikaciji pristupate kao gost!")
        while True:
            meni_za_gosta()
            izbor = input("Izaberite opciju >>")
            if izbor == "1":
                prikazi_dostupna_vozila()
            elif izbor == "2":
                pretraga_vozila()
            elif izbor == "3":
                sortiraj_vozila()
            elif izbor == "x":
                quit()
