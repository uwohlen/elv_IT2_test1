# Arduino Bil

### Målet med bilen
målet med bilen var å lage en bil med kun to hjul som har muligheten å kjøre og snu på en presis måte

### Bygging av bilen

- vi tok en papp bit og skar en trekant ut av den
- vi limte to motorer med hjul på bilen med spissen av trekanten pekende bakover
- vi tok en bit av en 3D-printed vinge og limte den til bunn av bilen for å støtte bilen sånn at den gikk rett når den kjørte
- for å få bilen til å snu med mindre friksjon lagde vi en arm med lodd styrt av en servo motor. Motoren kunne vippe armen opp og ned sånn att bilen kunne balansere når det trengs.
- En bug/feature av denne armen var at den kunne brukes for ødelege andre ting eller seg selv (noe som vi løste med en papp beskytter bak bilen)

### Koden
- vi brukte en bibliotek for servo motoren som styrte armen opp og ned med bruk ov noen innebygd funksjoner
- vi lagde noen funsjoner for å styre motorene ved bruk av HIGH og LOW output av arduino pinnene
- etter vi hadde definert disse bevegelse funksjonene kunne vi lage kombinasjoner av de for å lage mer avansert bevegelser

### Sluttresultat
- vi klarte å få bilen til å balansere seg når servo motoren flyttet armen ned
- bilen klarte og kjøre i alle retninger med rimlig presisjon
- takk til noen feil i brettet opplevde vi problemer med batteri bruk og torque i motorene.
