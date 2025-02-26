# Frank_test Repository

Dit is een test repository voor Frank om met GitHub en Python te experimenteren.

## Inhoud

Deze repository bevat:

- `hello_world.py`: Een Python script met een indrukwekkend 3D-draaieffect voor tekst
- `requirements.txt`: Een bestand met de vereiste packages (momenteel alleen standaard libraries)

## Functionaliteit

Het script biedt de volgende functionaliteit:

1. Toont een welkomstbericht
2. Vraagt de gebruiker om tekstinvoer
3. Creëert een 3D-draaieffect in de console waarbij:
   - De tekst lijkt te draaien in een driedimensionale ruimte
   - Perspectief wordt gesimuleerd door tekstbreedte en spatiëring aan te passen
   - Haakjes veranderen van richting om rotatie aan te geven
   - Een verticale lijn wordt getoond wanneer de tekst vanaf de zijkant wordt "bekeken"
   - De animatie draait de tekst vloeiend met 36 frames per volledige rotatie
4. Voert drie volledige rotaties uit
5. Toont een afsluitbericht

## Aan de slag

Om met deze repository te werken:

1. Clone de repository:
   ```
   git clone https://github.com/Fbeunder/Frank_test.git D:\Python\Projects\Frank_test
   ```

2. Navigeer naar de repository directory:
   ```
   cd D:\Python\Projects\Frank_test
   ```

3. Voer het Python script uit:
   ```
   python hello_world.py
   ```

4. Volg de instructies in het programma om tekst in te voeren en de 3D-animatie te bekijken

## Vereisten

Dit project gebruikt de volgende standaard Python bibliotheken:
- `time` - voor timing in de animatie
- `sys` - voor console-output manipulatie
- `math` - voor berekeningen die de 3D-illusie mogelijk maken

Er zijn geen externe packages nodig om dit script uit te voeren.

## Technische details

De 3D-animatie wordt bereikt door:
- Trigonometrische functies te gebruiken om rotatie te simuleren
- De breedte van tekst aan te passen op basis van de gesimuleerde hoek
- Tekens en spatiëring dynamisch aan te passen voor het perspectief-effect
- De console te manipuleren met carriage returns (\r) om animatie te creëren

## Doelen

- Leren werken met GitHub
- Python-vaardigheden ontwikkelen
- Version control begrijpen en toepassen
- Creatieve console-animaties maken met standaard Python
- Basisprincipes van 3D-simulatie verkennen

## Bijdragen

Suggesties en verbeteringen zijn welkom! Voel je vrij om issues aan te maken of pull requests in te dienen.
