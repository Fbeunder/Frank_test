#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

def spinning_text(text, spins=3):
    """
    Laat tekst 'ronddraaien' in de console door verschillende patronen te tonen
    
    Args:
        text: De tekst die moet ronddraaien
        spins: Aantal keer dat de tekst volledig ronddraait
    """
    # Verschillende patronen voor de animatie
    patterns = [
        f"| {text} |",
        f"/ {text} /",
        f"- {text} -",
        f"\\ {text} \\"
    ]
    
    # Totaal aantal frames (4 patronen × aantal spins)
    total_frames = len(patterns) * spins
    
    for i in range(total_frames):
        # Kies het juiste patroon voor deze frame
        pattern_index = i % len(patterns)
        
        # Print het patroon zonder naar de volgende regel te gaan
        sys.stdout.write('\r' + patterns[pattern_index])
        sys.stdout.flush()
        
        # Wacht kort voor het volgende frame
        time.sleep(0.25)
    
    # Print een lege regel na de animatie
    print("\nAnimatie voltooid!")

def main():
    """
    De hoofdfunctie van het programma
    """
    print("Hello, World!")
    print("Welkom bij mijn eerste Python script in de Frank_test repository!")
    
    # Vraag om input van de gebruiker
    user_input = input("\nVoer een tekst in om te laten ronddraaien: ")
    
    # Voer de spinning_text functie uit met de input
    print("\nLaat de tekst ronddraaien...")
    spinning_text(user_input)
    
    print(f"\nBedankt voor het uitproberen van '{user_input}'!")

if __name__ == "__main__":
    # Dit zorgt ervoor dat main() alleen wordt uitgevoerd als dit script direct wordt gestart
    # en niet als het wordt geïmporteerd als module in een ander script
    main()
