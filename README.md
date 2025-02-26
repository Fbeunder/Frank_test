# Frank_test Repository

Dit is een test repository voor Frank om met GitHub en Python te experimenteren, inclusief een interactieve 3D tekst visualisatie.

## Inhoud

Deze repository bevat:

- `hello_world.py`: Een eenvoudig Python script met een console-gebaseerd 3D-draaieffect voor tekst
- `3d_visualizer.py`: Een moderne GUI applicatie met geavanceerde 3D tekst visualisatie
- `requirements.txt`: Een bestand met de vereiste packages en libraries
- `web/`: Directory met HTML en JavaScript bestanden voor de 3D visualisatie

## Functionaliteit

### Console Applicatie (`hello_world.py`)

De originele console applicatie biedt de volgende functionaliteit:

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

### GUI Applicatie (`3d_visualizer.py`)

De nieuwe GUI-applicatie biedt een moderne gebruikerservaring:

1. Een gebruiksvriendelijke interface met Tkinter
2. Opties voor het aanpassen van:
   - De tekst die in 3D wordt gevisualiseerd
   - De rotatiesnelheid van de 3D tekst
   - De kleur van de 3D tekst
3. Geavanceerde 3D visualisatie met Three.js, waarbij:
   - De tekst wordt weergegeven als volwaardige 3D-objecten met diepte
   - De tekst vloeiend ronddraait in een 3D ruimte
   - De gebruiker de camera kan verplaatsen en roteren met de muis
   - Realistische belichting en schaduwen worden toegepast
4. Een ingebouwde webserver voor het tonen van de 3D visualisatie
5. Automatisch openen van de visualisatie in de standaard webbrowser

## Aan de slag

### Installatie

1. Clone de repository:
   ```
   git clone https://github.com/Fbeunder/Frank_test.git
   ```

2. Navigeer naar de repository directory:
   ```
   cd Frank_test
   ```

3. Zorg ervoor dat Python 3.6 of hoger is geïnstalleerd.

### De console applicatie gebruiken

Voer het Python script uit:
```
python hello_world.py
```

Volg de instructies in het programma om tekst in te voeren en de console 3D-animatie te bekijken.

### De GUI applicatie gebruiken

1. Voer het Python GUI script uit:
   ```
   python 3d_visualizer.py
   ```

2. In de GUI:
   - Voer de tekst in die je in 3D wilt visualiseren
   - Pas de rotatiesnelheid aan met de slider
   - Kies een kleur voor de 3D tekst
   - Klik op de "Visualiseren in 3D" knop

3. Er wordt automatisch een browser geopend met de 3D visualisatie, waar je:
   - Met de linkermuisknop de camera kunt roteren
   - Met de rechtermuisknop kunt pannen
   - Met het scrollwiel kunt in- en uitzoomen

## Vereisten

Dit project gebruikt standaard Python bibliotheken:
- `time` - voor timing in de animatie
- `sys` - voor console-output manipulatie
- `math` - voor berekeningen die de 3D-illusie mogelijk maken
- `tkinter` - voor de GUI (meegeleverd met Python maar soms apart te installeren)
- `webbrowser` - voor het openen van de browser met de 3D visualisatie
- Diverse andere standaard libraries zoals opgegeven in requirements.txt

De 3D visualisatie gebruikt de volgende JavaScript libraries (automatisch geladen via CDN):
- Three.js - Voor 3D rendering in de browser
- Three.js OrbitControls - Voor camera besturing
- Three.js FontLoader & TextGeometry - Voor het creëren van 3D tekst

## Technische details

### Console 3D-animatie
De console 3D-animatie wordt bereikt door:
- Trigonometrische functies te gebruiken om rotatie te simuleren
- De breedte van tekst aan te passen op basis van de gesimuleerde hoek
- Tekens en spatiëring dynamisch aan te passen voor het perspectief-effect
- De console te manipuleren met carriage returns (\r) om animatie te creëren

### Geavanceerde 3D visualisatie
De moderne 3D visualisatie maakt gebruik van:
- HTML5 en JavaScript voor interactieve weergave
- Three.js voor geavanceerde 3D-rendering in de browser
- WebGL voor hardware-versnelde graphics
- Een lokale webserver voor het serveren van de visualisatie
- Tkinter voor de gebruiksvriendelijke interface

## Doelen

- Leren werken met GitHub
- Python-vaardigheden ontwikkelen
- Version control begrijpen en toepassen
- GUI-ontwikkeling met Tkinter verkennen
- Web technologieën integreren met Python
- 3D-visualisatie met Three.js leren toepassen

## Bijdragen

Suggesties en verbeteringen zijn welkom! Voel je vrij om issues aan te maken of pull requests in te dienen.