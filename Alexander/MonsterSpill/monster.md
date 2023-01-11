## Monster Spill

### Målet med spillet
- målet med spillet er å drepe en monster med forskjellige våpen på en brett som er skrevet ut i konsollen.

### Hvordan spillet spilles
- spillet begynnes med at de forskjellige kommandoene som spilleren kan bruke blir skrevet ut til konsollen
- brettet blir da utskrevet til konsollen og da kan spilleren skrive inn kommandoen de vil bruke
- spilleren har valget til å enten bytte våpen, flytte seg på bretter eller angrepe monsteret
- spillet er over når enten spilleren er død eller alle monsterne har blitt drept

### Strukturen av koden
- spillet bruker object orientert programmering for å ha kontrol på alle monsterne og spilleren
- klassen til monsteren lar spillet ha flere monstere på brettet sammtidig med sine egene verdier
- spillet har også et Game klasse som holder kontrol over felles variablene mens spillet kjøres og definerer metodene for hver av rundene
- Game klassen definerer metoden for å skrive ut brettet i konsollen
