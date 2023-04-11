# tee ratkaisu tänneimport urllib.request
import urllib.request
import json

def json_tiedot(linkki):

    tulos = urllib.request.urlopen(linkki)
    data = tulos.read()

    kurssit = json.loads(data)

    return kurssit


def hae_kaikki():
    linkki = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    kurssit = json_tiedot(linkki)

    tulos = []
    for kurssi in kurssit:
        fullName = kurssi["fullName"]
        name = kurssi["name"]
        year = kurssi["year"]
        exercises = sum(map(int, kurssi["exercises"]))
        if kurssi["enabled"]:
            tulos.append((fullName, name, year, exercises))

    return tulos

def hae_kurssi(kurssi: str):
    
    linkki = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats"

    kurssi = json_tiedot(linkki)

    kurssit = 0
    opiskelijat = 0
    tunnit = 0
    tehtavat = 0

    for tiedot in kurssi.values():
        
        opiskelija = tiedot["students"]
        if opiskelijat < opiskelija:
            opiskelijat += opiskelija
        tunnit += tiedot["hour_total"]
        tehtavat += tiedot["exercise_total"]
        kurssit += 1

    kurssi_sanakirja = {}

    kurssi_sanakirja["viikkoja"] = kurssit
    kurssi_sanakirja["opiskelijoita"] = opiskelijat
    kurssi_sanakirja["tunteja"] = tunnit
    kurssi_sanakirja["tunteja_keskimaarin"] = int(tunnit / opiskelijat)
    kurssi_sanakirja["tehtavia"] = tehtavat
    kurssi_sanakirja["tehtavia_keskimaarin"] = int(tehtavat / opiskelijat)

            
    return kurssi_sanakirja

if __name__ == "__main__":
    print(hae_kaikki())
    print(hae_kurssi("docker2019"))
    
