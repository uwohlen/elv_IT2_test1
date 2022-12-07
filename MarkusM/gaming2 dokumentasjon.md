## Dokumentasjon av gaming2.py

### Filer
* gaming.py

_Filene under må hentes fra [github](https://github.com/uwohlen/elv_IT2_uw/tree/main/MarkusM/):_
* images
  * gdBackground.png
  * gdBlock.png
  * gdBorder3.png
  * gdPlayer.png
* sounds
  * clock_tick.wav
  * fail_0.wav
  * fail_1.wav
  * fail_2.wav
  * gdMusic.mp3
  * main_music.wav
  * menuMusic.mp3
  * win_0.wav
  * win_1.wav
  * win_2.wav
* font_test
  * MADE TOMMY Black_PERSONAL USE.otf
  * MADE TOMMY Regular_PERSONAL USE.otf
  * MADE TOMMY Regular_PERSONAL USE.otf
 
___Filene må være organisert lik mappestrukturen ovenfor, eller vil ikke spillet kjøre___

# Beskrivelse av prosjektet
Progammet er et spill, og inneholder tre spillmoduser. En der man skal stave et ord slik det er vist, et der man skal fullføre en "geometry dash" level og en (hard mode), der man skal klare begge på rad.


# Metoder
Programmet er ganske omfattende, men under skal jeg nevene hovedfunksjonene i programmet

### typegame()
* Spill der man skal stave et ord som vist over
* Metode for å displaye tekst med ulike fager
* Lett å lage like ord ved å endre på "task"
* Å lage en halvsirkel i pgygame er ikke mulig, så man må innstallere og importere PIL

### gd()
* "geometry dash" klone
* Inneholder klasser for å displaye både kvadrater og trekanter, og kollisjoner mellom disse og spiller
* Enkelt å endre levelen. Ved å endre stringen "lvl" kan man plassere ut blokker, trekanter og winconditions
* Inkluderer et kollisjonssystem som er langt fra optimalt, man kan plutselig bli teleportert til toppen av en blokk hvis man har høy nok fart.
  * harmcolissionCheck
    * Sjekker alle mulige måter spilleren kan dø på, ved å undersøke om spilleren kollidere med "harmlines"
  * safeColissionCheck
    * Sjekker om spilleren kollidere med såkalte "safelines"
    * Brukes til hopping og å hindre spilleren i å falle av banen
    * Setter alltid y-posisjonen til toppen av blokken, for å unngå å sitte fast inne i en blokk, men dette fører til at man kan teleportere opp (skjer sjeldent)
* Metode for å rendere alle objektene på skjermen, og ikke de utenfor.

### meny()
* Definerer hvordan menyen skal se ut
* Egen klasse for knapper på skjermen
* Gjør det lett å endre eller å legge til menyelementer, men man må fortsatt spesifisere at det skal rendres i menurender(), og hva slags funksjon det skal ha i menyInterract()



