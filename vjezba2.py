kolegij = {}

kolegij["ime"] = input("Unesite ime kolegija:").upper()
kolegij["ECTS"] = int(input("Unesite ECTS bodove za kolegij:"))

#print("Kolegij", kolegij["ime"], "nosi", kolegij["ECTS"], "ECTS bodova")

ispit = {}

ispit["kolegij"] = kolegij
dan = int(input('Unesite dan ispita: '))
mjesec = int(input('Unesite mjesec ispita: '))
godina = int(input('Unesite godinu ispita: '))
from datetime import date
ispit["datum"] = date(godina, mjesec, dan)

#print("Kolegij", ispit["kolegij"]["ime"], "nosi", ispit["kolegij"]["ECTS"], "ECTS bodova")

student = {}

student["ispit"] = ispit
ime = input("Unesite ime studenta: ").capitalize()
prezime = input("Unesite prezime studenta: ").capitalize()
student["ime"] = ime + ' ' + prezime


print("Student", student["ime"], "je prijavio ispit iz kolegija",
      student["ispit"]["kolegij"]["ime"],"(", student["ispit"]["kolegij"]["ECTS"], "ECTS-a )", "koji će se održati:", student["ispit"]["datum"])


