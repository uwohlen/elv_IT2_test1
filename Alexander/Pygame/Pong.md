# Multi-Pong

### Målet med spillet
- spillet er en variasjon av det klassiske spillet pong
- spillet begynner med kun en ball som spilleren må passe på faller ikke ut bunn av skjermen
- hver 10 sekunder blir det laget en ny ball som spilleren må sammen med de som ble laget fra før må holde over bunnen a vinduet

### Hvordan spillet spilles
- spillet pilles med kun høyre og vestre piltastaturene

### Strkturen av koden
- ballene har alle sine egene objekter som er definert fra en klasse
- spilleren er definert fra en innebydg klasse i pygame, Rect, som lar deg lagre posisjon og dimensjoner av et rektangulært objekt
- Rect klassen har også innebygd metoder som flytter spilleren som forenkler koden