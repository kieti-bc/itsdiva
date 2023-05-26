# ItsDiva
Tool to convert code to syntax highlighted html format

Työkalu, jolla voi muuntaa koodia html muotoon ItsLearning alustaa varten.


## Käyttö
* Mene hakemistoon jossa koodi on
* Käynnistä ohjelma komennolla 
```bash
python itsdiva.py
```
* Valitse pudotusvalikosta kieli
* Valitse pudotusvalikosta väriteema
* Kirjoita tai liitä ylempään tekstikenttään koodi
* Paina **Convert** nappia
* Klikkaa alempaa tekstikenttää, kopioi koodi painamalla **Ctrl + A**  ja **Ctrl + C**
* Paina ItsLearning muotoiluvalikosta **Koodi** nappia
* Liitä luotu hmtl haluaamaasi kohtaan painamalla **Ctrl + V**


## Uusien tyylien luominen
Lisää styles/ kansioon uusi .json tiedosto, jonka sisältö on muotoa
```json
{
	"name": "tyylin nimi>",
	"tunniste": "html-väri"
}
```

Tunnisteita ovat:
* **bg**: tekstin taustaväri
* **fg**: tekstin väri
* **kw**: keyword, eli kielen varatut sanat
* **ct**: constant, eli merkkijonot ja numerot
* **ut**: user type, eli koodissa olevat luokat ja rykelmät (struct)
* **pt**: primitive type, eli alkeistyypit, esim. int, float
* **cc**: comment, eli kommentit
* **dc**: dokumentaatiokommentit
* **fc**: funktioiden nimet

Värit voi antaa niminä tai muissa [tuetuissa muodoissa](https://www.w3schools.com/colors/default.asp)