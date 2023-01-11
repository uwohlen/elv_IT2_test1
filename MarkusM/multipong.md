## Dokumentasjon av gaming2.py

### Filer
* multipong.py

_Filene under må hentes fra [github](https://github.com/uwohlen/elv_IT2_uw/tree/main/MarkusM/):_

* images
  * coinicon.png
* sounds
  * menumusic.mp3
* fonts
  * MADE TOMMY Black_PERSONAL USE.otf
  * MADE TOMMY Regular_PERSONAL USE.otf
  * coolvetica rg.otf
 
___Filene må være organisert lik mappestrukturen ovenfor, med en overordnet mappe som heter MarkusM, ellers vil ikke spillet kjøre___

___Hvis hele repositoriet er hentet fra github, trenger man ikke å gjøre noe___

# Beskrivelse av prosjektet
Programmet er et "pong" spill. Spilleren skal bevege en "rekkert" for å slå firkanter opp, slik at de ikke treffer bunnen av skjermen. Programmet inneholder også et menysytem, hvor brukeren kan enten spille på nytt, avslutte eller åpne butikk

# Metoder
Programmet er omfattende, men under er noen av hovedfunksjonene til programmet

### class: block
* lages underveis mens spillet kjører, gjennom funksjonen addBlock()
* når en blokk initieres, lages det en tilfeldig farge og hastighet, men med en konstant størrelse
* inneholder metoder for å rendere, sprette og registrer om man har tapt spillet

## class: player
* 
