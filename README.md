# ItsDiva
Tool to convert code to syntax highlighted html format

Työkalu, jolla voi muuntaa koodia html muotoon ItsLearning alustaa varten.

## Ohjelman käynnistäminen
* Kloonaa tai lataa tämä repositorio omalle koneelle.
* Mene kansioon johon latasit tiedostot
* Valitse **itsdiva.py** ja oikean napin valikosta valitse **Luo pikakuvake**
* Valitse luotu pikakuva ja oikean napin valikosta valits **Ominaisuudet**
* Lisää kentän **Kohde** alkuun sana **python** ja välilyönti. Eli esim.
```
python "C:\Users\sinä\...\itsdiva.py"
```
* Tuplaklikkaa pikakuvaketta

## Käyttö
* Valitse pudotusvalikosta ohjelmointikieli
* Valitse pudotusvalikosta väriteema.
* Kirjoita tai liitä ylempään tekstikenttään koodi
* Paina **Convert** nappia
* Klikkaa alempaa tekstikenttää, kopioi koodi painamalla **Ctrl + A**  ja **Ctrl + C**
* Paina ItsLearning muotoiluvalikosta **Koodi** nappia
* Liitä luotu hmtl haluaamaasi kohtaan painamalla **Ctrl + V**

Jos asennat python kirjaston pyclip, tulee kopioinnista helpompaa. Se asennetaan komennolla:
```bash
python -m pip install pyclip
```

## Tyylien luominen ja muokkaaminen
Lisää styles/ kansioon uusi .json tiedosto, jonka sisältö on muotoa
```json
{
	"name": "tyylin nimi",
	"tunniste": "html-väri",
	"tunniste": 
	{
		"color": "html-väri",
		"weight": "bold"
	}
}
```

Tunnisteita ovat:
* **name**: tyylin nimi. Pakollinen.
* **background**: tekstin taustaväri. Pakollinen.
* **foreground**: tekstin väri. Pakollinen.
* **line_number_bg**: rivinumeroiden taustaväri
* **line_number_fg**: rivinumeroiden väri
* **keyword**: keyword, eli kielen varatut sanat
* **number**: numerot
* **string**: merkkijonot, eli "" välissä olevat merkit
* **user_type**: user type, eli koodissa olevat luokat ja rakenteet(struct)
* **primitive_type**: primitive type, eli alkeistyypit, esim. int, float
* **operator**: operaattorit eli +, - , * jne.
* **comment**: comment, eli kommentit
* **doc_comment**: dokumentaatiokommentit
* **function**: funktioiden nimet

Värit voi antaa niminä tai muissa [tuetuissa muodoissa](https://www.w3schools.com/colors/default.asp)

Jos jotakin tunnistetta ei anneta, sen tyyppisen tekstin piirtämiseen käytetään väriä **foreground**.

Muut tunnisteet kuin *name, background ja foreground* voi määritellä myös tarkemmin. Jos haluat määritellä enemmän kuin värin, pitää värin sijaan luoda uusi lohko, jonka sisällä voi määritellä:
* color: tekstin väri
* weight: Arvo "bold" lihavoi tekstin
* style: Arvo "italic" kursivoi tekstin
* switch_colors: Arvo "True" piirtää tekstin taustan **color** värillä ja tekstin **foreground** tyylillä.

## Uuden kielen lisääminen
Lisää languages/ kansioon uusi python tiedosto. Ota mallia muista kielistä. Tämän koodin tehtävä on tarvittaessa poiketa oletuksista.

Lisää program.py alkuun uusi **from** käsky joka lisää tekemästästi tiedostosta kielen tyypin

Lisää program.py tiedostossa olevan ItsDivaGui luokan self.languages listaan tekemäsi kielen konstruktorin kutsu.