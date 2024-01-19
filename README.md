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

Jos asennat python kirjaston pyclip, tulee kopioinnista helpompaa.

## Uusien tyylien luominen
Lisää styles/ kansioon uusi .json tiedosto, jonka sisältö on muotoa
```json
{
	"name": "tyylin nimi>",
	"tunniste": "html-väri"
}
```

Tunnisteita ovat:
* **background**: tekstin taustaväri
* **foreground**: tekstin väri
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

