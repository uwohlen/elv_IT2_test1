## Introduksjon
Vi har i lengre tid jobbet med et prosjekt der vi har brukt biblioteket PyGames til å lage vårt eget spill. Her kommer dokumentasjonen av dette prosjektet

Vi har følgende filer som inneholder kode
* Multipong.py

Og benytter png-filer, mp3-filer og ttf-filer
* Benjamin/Fonts/pixel-font.ttf
* Benjamin/pngs/multipong
* Benjamin/Lyd

### Multipong.py
Dette programmet har følgende Klasser, funksjoner, variabler, lister og biblioteker.
#### Funksjoner
  * **Meny**, denne funksjonen setter opp menyen og inneholder andre funksjoner for blant annet: Lyd, knapper, gifs/bilder og highscore
  * **Shop**, denne funksjonen setter opp butikken og inneholder andre funksjoner for blant annet: Bilder/gifs, knapper, tekst
  * **Game**, denne funksjonen setter opp spillet og inneholder andre funksjoner for blant annet: Musikk, bilder/gifs, bevegese av plate og objekter, funksjoner for selve spillets gang og regler.
#### Klasser
  * **Pong**, denne klassen er for å lage kvadratene i spillet, og har konstruktørene: self, x, y, fartx, farty, bredde, høyde, vindusobjekt, farge, passes, image
  * **Plate**, denne klassen er for å lage platen som spilleren beveger i spillet, og har konstruktørene: self, x, y, fartx, farty, bredde, høyde, vindusobjekt, farge
  * **Arena**, denne klassen er for å lage arenaen som avgrenser spillets område, altså der kvadratene og platen vil støte på, og har konstruktørene: self,x,y,bredde,høyde,farge
  * **Button**, denne klassen er for å lage knappene som benyttes i menyen og butikken, og har konstruktørene: self, x, y, image, scale
  * **Bilder**, denne klassen er for å lage bilder, og har konstruktørene: self, x, y, image, scale
 #### variabler
   * **clock**, er en variabel som bestemmer frekvensen spillet kjører på.
   * **klokke**, er en variabel som skalerer med frekvensen og brukes for blant annet beregning av poeng og highscore.
   * **Counter variabler**, dette er flere variabler som gjør at gifen kjører gjennom alle bildene som gifen består av.
 #### Lister
   * **Gif lister** Inkluderer bakgrunnslistene som det er fler av, disse listene legger til alle bildene til en gif, som senere blir kjørt gjennom via en for-løkke og variablene *Counter*
   *  **Pongs** En liste som inneholder alle kvadratene som blir laget, bruker liste siden kan da kjøre gjennom en while-løkke og bruke indexer for å behandle alle kvadratene samtidig.
#### Biblioteker
* import pygame as pg
* from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
* import random as random
* import sys, time
* import os
* from pygame.locals import *
* from random import choice

### Bruk
For å bruke spillet har det ikke noe å si hvor selve MultiPong.py filen ligger så lenge den er i samme repositorien som de andre filene, for dette trengs for at MultiPong.py skal kunne finne frem til de andre filene. MultiPong.py filen benytter paths for å finne frem til de andre filene, og dermed er dette noe som må tas hensyn til dersom filer skal flyttes.
Programmet starter opp en meny hvor du kan velge videre hva du ønsker å gjøre: Å besøke butikken, spille selve spillet eller avslutte programmet. Butikken har som funksjon å la spilleren endre om på teksturer som blir brukt for kvadratene i spillet og platen som spilleren beveger, videre har den som funksjon å la spilleren kjøpe ny musikk, nye bilder og oppgraderinger som endrer spillets funksjonalitet eller gjør spillet lettere. Selve spillet er basert på klassikeren Multipong.
Det er mye som kan endres på, bare å bruke fantasien, eksempler er hvordan selve spillet fungerer, layouts av meny og butikk, base-tekstur for kvadratene og platen, musikk, legge til power-ups etc

#### For å bruke programmet brukes bibliotekene:
* import pygame as pg

* from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

* import random as random

* import sys, time

* import os

* from pygame.locals import *

* from random import choice


# Slutten 