## Introduksjon
Vi har i lengre tid jobbet med et prosjekt der vi har laget noe i Arduino, og i mitt tilfelle en bil med to hjul og en avstandssensor for å plukke opp om noe er forann, og den vil da endre kjøreretning. Her kommer dokumentasjonen av dette prosjektet

Vi har følgende filer som inneholder kode
* avstand og motor.ino

### avstand og motor.ino
Dette programmet har følgende Klasser, funksjoner, variabler, lister og biblioteker.

#### Funksjoner
  * **Setup** setter opp de forskjellige pin-ene og sier om de skal være inputs eller outputs, og hvilke innganger som blir brukt, altså hvor strømmen skal bli sendt
  * **Loop** kjører hele programmet

#### Variabler
  * **Duration** variabel for negden av lydbølge avstanden
  * **Distance** variabel for avstandsmålingen

### Bruk
Programmet vil få bilen til å kjøre fremover og setter i gang avstandssensoren, dersom avstanden mellom sensoren og et hinder er mindre en 10cm vil bilen bytte kjøreretning.

#### Slutt