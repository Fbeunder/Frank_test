#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import math

def simulate_3d_spinning(text, spins=3):
    """
    Simuleert een 3D-draaien effect voor tekst in de console
    
    Args:
        text: De tekst die moet ronddraaien in '3D'
        spins: Aantal volledige rotaties
    """
    # Aantal frames per rotatie bepaalt de vloeiendheid
    frames_per_rotation = 36
    total_frames = frames_per_rotation * spins
    
    # Teken de originele lengte van de tekst + marges
    text_width = len(text) + 8
    
    for i in range(total_frames):
        # Bereken de hoek in radialen
        angle = (i * 2 * math.pi) / frames_per_rotation
        
        # Bepaal de effectieve breedte gebaseerd op de hoek (voor perspectief)
        # Bij 0 of pi radialen zien we de tekst van de zijkant (smaller)
        # Bij pi/2 of 3pi/2 radialen zien we de tekst van voren (volle breedte)
        width_factor = abs(math.sin(angle))
        effective_width = int(text_width * width_factor)
        
        # Bepaal de fontgrootte (voor diepte-effect)
        # Dit simuleren we door spaties toe te voegen aan weerszijden
        spaces = int((text_width - effective_width) / 2)
        
        # Bepaal de letter-spacing voor perspectief
        if effective_width <= 1:
            # Als de tekst bijna volledig zijdelings is, toon een verticale lijn
            displayed_text = "|"
        else:
            # Voeg variabele spatiëring toe tussen karakters op basis van effectieve breedte
            spacing = " " * (1 if effective_width < text_width * 0.7 else 0)
            displayed_text = spacing.join(text)
            
            # Voeg 3D-effect toe door brackets te gebruiken die afhankelijk zijn van de hoek
            if angle % (2 * math.pi) < math.pi:
                left_bracket = "("
                right_bracket = ")"
            else:
                left_bracket = ")"
                right_bracket = "("
        
            # Combineer alles tot de uiteindelijk weergegeven tekst
            displayed_text = f"{' ' * spaces}{left_bracket} {displayed_text} {right_bracket}"
        
        # Print de geformatteerde tekst
        sys.stdout.write('\r' + ' ' * text_width + '\r')  # Wis de vorige tekst
        sys.stdout.write(displayed_text)
        sys.stdout.flush()
        
        # Wacht kort voor het volgende frame
        time.sleep(0.03)
    
    # Print een lege regel na de animatie
    print("\n3D-animatie voltooid!")

def main():
    """
    De hoofdfunctie van het programma
    """
    print("Hello, World!")
    print("Welkom bij mijn Python script met 3D animatie-effect!")
    
    # Vraag om input van de gebruiker
    user_input = input("\nVoer een tekst in om in 3D te laten ronddraaien: ")
    
    if not user_input:
        user_input = "Python"
        print(f"Geen tekst ingevoerd, we gebruiken '{user_input}' als voorbeeld.")
    
    # Voer de 3D spinanimatie uit
    print("\nStart 3D-animatie...")
    simulate_3d_spinning(user_input)
    
    print(f"\nBedankt voor het uitproberen van de 3D-animatie met '{user_input}'!")

if __name__ == "__main__":
    # Dit zorgt ervoor dat main() alleen wordt uitgevoerd als dit script direct wordt gestart
    main()
