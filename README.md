# ItsDiva
Tool to convert code to syntax highlighted html format

Työkalu, jolla voi muuntaa koodia html muotoon ItsLearning alustaa varten.



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