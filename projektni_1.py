from datetime import date
korisnik = {}

ime = input("Unesite Vaše ime: ").capitalize()
prezime = input("Unesite Vaše prezime: ").capitalize()
korisnik["telefon"] = str(input("Unesite Vaš broj telefona: "))
korisnik["email"] = input("Unesite Vaš email: ").lstrip().rstrip()
korisnik["ime"] = ime + " " + prezime

artikl = {}

artikl["korisnik"] = korisnik
artikl["ime"] = input("Unesite ime artikla: ")
artikl["opis"] = input("Unesite opis artikla: ")
artikl["cijena"] = float(input("Unesite cijenu artikla:"))

prodaja = {}

prodaja["artikl"] = artikl
dan = int(input("Unesite dan: "))
mjesec = int(input("Unesite mjesec: "))
godina = int(input("Unesite godinu: "))
prodaja["datum"] = date(godina, mjesec, dan)

print("Informacije o korisniku: ")
print(prodaja["artikl"]["korisnik"]["ime"])
print("Telefon: ", prodaja["artikl"]["korisnik"]["telefon"])
print("Email: ", prodaja["artikl"]["korisnik"]["email"])
print()
print("Informacije o artiklu: ")
print("Ime artikla: ", prodaja["artikl"]["ime"])
print("Opis artikla: ", prodaja["artikl"]["opis"])
print("Cijena: ", prodaja["artikl"]["cijena"], "€")
print()
print("Datum prodaje: ", prodaja["datum"])


