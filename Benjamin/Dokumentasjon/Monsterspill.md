### Dokumentasjonen skal inneholde følgende overskrifter
* Liste med filer
* Beskrivelse
* Bruk: Må filen ligge et bestemt sted, hva gjør programmet, hva kan du endre, hva må importeres/inkluderes av eksterne biblioteker?
* Klasser, metoder, funksjoner, variabler: gi en forklaring av det du har produsert'


## Introduksjon
Vi har i lengre tid jobbet med et prosjekt der vi har laget et tekstbasert spill i python. Her kommer dokumentasjonen av dette prosjektet

Vi har følgende filer som inneholder kode
* Monsterspill.py

### Monsterspill.py
Dette programmet har følgende Klasser, funksjoner, variabler, lister og biblioteker.

#### Funksjoner
  * **Clear** denne funksjonen sletter tekst fra konsollen slik at den blir mer ryddig
  * **Slow type / Fast type** disse funksjonene gjør at teksten blir skrevet ut til konsollen bokstav for bokstav, istedenfor at alt blir printet ut øyeblikkelig
  * **Regler** denne funksjonen skriver ut alle reglene til blackjack
  * **Deal** denne funksjonen deler ut kortene til spilelren og dealeren
  * **Play again** denne funksjonen lar spilleren spille på nytt, og nullstiller data som for eksempel kortene, og lager en ny kortstokk.
  * **Sjappe** denne funksjonen setter opp butikken som lar spilleren kjøpe diverse gjenstander.
  * **Statistikk** denne funksjonen lar spilleren se diverse statistikker om karakteren sin
  * **Total** denne funksjonen regner ut verdien til spilleren og dealeren sin hånd
  * **Hit** denne funksjonen lar spilleren trekke et nytt kort
  * **Print results** denne funksjonen printer ut resultatene, altså om spilleren eller dealeren vant
  * **Gevinst / Tape penger** disse funksjonene bestemmer om spilleren enter vinner eller taper penger, og summen påvirkes av diverse egenskaper til karakteren.
  * **Flaks** denne funksjonen gjør at dersom karakteren har mye flaks, kan du vinne mer penger enn det du betta.
  * **IQ** denne funksjonen gjør at dersom karakteren har høy IQ, kan du tape mindre penger enn det du betta.
  * **Fight** denne funksjonen lar spilleren slåss mot monsteret
  * **Blackjack** denne funksjonen finner ut om spilleren eller dealeren har blackjack
  * **Score** denne funksjonen viser spilleren hvor mange gange du har vunnet eller tapt.
  * **Game** denne funksjonen kjører hele løkken med spillet.

#### Klasser
  * **Monster** Denne klassen er for å lage monstere
  * **Spiller** Denne klassen er for å lage karakterene man kan velge mellom

#### Lister

  
#### Biblioteker
* import random
* import os
* import sys, time

### Bruk

Spillet starter med å gi en kort introduksjon, og spør deretter om spilleren om regler til spillet, deretter får spilleren valg mellom flere karakterer å bruke i spillet, disse karakterene har attributer som f. eks flaks, IQ og liv som står beskrevet over. Deretter starter blackjack hvor spilleren blir først presentert for en meny med mulige sider spilleren kan besøke, eller hvor hvor mye spilleren vil bette i blackjack mot monsteret, altså dersom spilleren skriver inn et tall som er innen spillerens penger vil dette gå inn i en pot i blackjack, dersom det blir oppgitt en sum over det spilleren har vil konsollen be om en ny input, og til slutt hvis spilleren skriver inn en tilsvarende bokstav for en av sidene vil denne siden bli åpnet opp istedenfor å spille blackjack. Videre enten taper eller vinner du de pengene du la inn, og med penger kan du kjøpe gjenstander i butikken for å øke eller forbedre attributene til karakteren, og bruke disse til å slåss mot monsteret og drepe det. 

