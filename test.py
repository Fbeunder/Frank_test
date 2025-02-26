#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script voor Frank_test repository
Dit script test zowel de console applicatie als de GUI applicatie
"""
import os
import sys
import subprocess
import time
import platform

def clear_screen():
    """Clear het terminal scherm op een cross-platform manier"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_header(text):
    """Print een opvallende header"""
    terminal_width = 80
    print("\n" + "=" * terminal_width)
    print(text.center(terminal_width))
    print("=" * terminal_width + "\n")

def main():
    """Hoofdfunctie van het testscript"""
    clear_screen()
    
    print_header("Frank_test Repository Tester")
    
    print("Dit script helpt bij het testen van de verschillende applicaties in de repository.\n")
    
    while True:
        print("\nKies een optie om te testen:")
        print("1. Test hello_world.py (Console 3D animatie)")
        print("2. Test 3d_visualizer.py (GUI met 3D visualisatie)")
        print("3. Toon README")
        print("4. Exit")
        
        choice = input("\nJouw keuze (1-4): ").strip()
        
        if choice == "1":
            test_console_app()
        elif choice == "2":
            test_gui_app()
        elif choice == "3":
            show_readme()
        elif choice == "4":
            print("\nBedankt voor het testen. Tot ziens!\n")
            break
        else:
            print("\nOngeldig keuze. Probeer opnieuw.")

def test_console_app():
    """Test de console applicatie"""
    clear_screen()
    print_header("Test van Console 3D Animatie (hello_world.py)")
    
    print("De console applicatie zal nu starten...")
    print("Tip: Voer een korte tekst in voor het beste effect.\n")
    print("Druk op Enter om te starten...")
    input()
    
    try:
        # Roep de hello_world.py aan
        if platform.system() == "Windows":
            subprocess.call(["python", "hello_world.py"])
        else:
            subprocess.call(["python3", "hello_world.py"])
    except Exception as e:
        print(f"Fout bij het uitvoeren van hello_world.py: {e}")
    
    print("\nTest afgerond. Druk op Enter om terug te gaan naar het menu...")
    input()

def test_gui_app():
    """Test de GUI applicatie"""
    clear_screen()
    print_header("Test van GUI 3D Visualisatie (3d_visualizer.py)")
    
    print("De GUI applicatie zal nu starten...")
    print("Een browser zal automatisch openen na het klikken op 'Visualiseren in 3D'.")
    print("\nTips voor gebruik:")
    print("1. Voer een tekst in (niet te lang voor het beste resultaat).")
    print("2. Pas de rotatiesnelheid aan met de slider.")
    print("3. Kies een kleur voor de 3D tekst.")
    print("4. Klik op 'Visualiseren in 3D' om de browser te openen.")
    print("5. In de browser: gebruik de muis om de 3D tekst te draaien en zoomen.")
    print("\nDruk op Enter om te starten...")
    input()
    
    try:
        # Start de 3d_visualizer.py in een apart proces
        if platform.system() == "Windows":
            subprocess.Popen(["python", "3d_visualizer.py"])
        else:
            subprocess.Popen(["python3", "3d_visualizer.py"])
        
        print("\nDe GUI applicatie is gestart. Sluit het venster als je klaar bent met testen.")
        print("Druk op Enter om terug te gaan naar het menu...")
        input()
    except Exception as e:
        print(f"Fout bij het uitvoeren van 3d_visualizer.py: {e}")
        print("\nDruk op Enter om terug te gaan naar het menu...")
        input()

def show_readme():
    """Toon de README.md inhoud"""
    clear_screen()
    print_header("README.md Inhoud")
    
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        print(readme_content)
    except Exception as e:
        print(f"Fout bij het lezen van README.md: {e}")
    
    print("\nDruk op Enter om terug te gaan naar het menu...")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgramma onderbroken. Tot ziens!")
        sys.exit(0)
