#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import os
import json
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

class TextVisualizer3D:
    """
    Een GUI applicatie voor het visualiseren van tekst in 3D
    """
    def __init__(self, root):
        self.root = root
        self.root.title("3D Tekst Visualizer")
        self.root.geometry("800x600")
        self.root.minsize(640, 480)
        
        # Server configuratie
        self.server = None
        self.server_thread = None
        self.port = self.find_free_port()
        
        # Maak de UI componenten
        self.setup_ui()
        
        # Creëer de HTML bestanden voor 3D visualisatie
        self.create_html_files()
        
        # Start de lokale webserver
        self.start_server()
        
    def find_free_port(self):
        """Vind een vrije poort om de webserver op te starten"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
    
    def setup_ui(self):
        """Creëer alle UI componenten"""
        # Hoofdframe
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titel
        title_label = ttk.Label(
            main_frame, 
            text="3D Tekst Visualizer", 
            font=("Helvetica", 24)
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Tekst invoer", padding="10")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Uitleg
        ttk.Label(
            input_frame, 
            text="Voer hieronder de tekst in die je in 3D wilt visualiseren:",
            wraplength=700
        ).pack(pady=(0, 10))
        
        # Textinvoer
        self.text_entry = ttk.Entry(input_frame, width=50, font=("Helvetica", 12))
        self.text_entry.pack(fill=tk.X, padx=5, pady=5)
        self.text_entry.insert(0, "Python 3D")
        
        # Opties frame
        options_frame = ttk.LabelFrame(main_frame, text="Visualisatie opties", padding="10")
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Rotatiesnelheid
        speed_frame = ttk.Frame(options_frame)
        speed_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(speed_frame, text="Rotatiesnelheid:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.speed_var = tk.DoubleVar(value=1.0)
        speed_scale = ttk.Scale(
            speed_frame, 
            from_=0.1, 
            to=3.0, 
            variable=self.speed_var, 
            orient=tk.HORIZONTAL,
            length=300
        )
        speed_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Label(speed_frame, textvariable=self.speed_var).pack(side=tk.LEFT, padx=10)
        
        # Kleur opties
        color_frame = ttk.Frame(options_frame)
        color_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(color_frame, text="Tekstkleur:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.color_var = tk.StringVar(value="#4287f5")
        color_options = ["#4287f5", "#f54242", "#42f551", "#f5f242", "#f542f2", "#FFFFFF"]
        color_names = ["Blauw", "Rood", "Groen", "Geel", "Paars", "Wit"]
        
        for i, (color, name) in enumerate(zip(color_options, color_names)):
            rb = ttk.Radiobutton(
                color_frame, 
                text=name,
                variable=self.color_var,
                value=color
            )
            rb.pack(side=tk.LEFT, padx=5)
        
        # Knoppen frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, padx=10, pady=20)
        
        # Visualiseren button
        self.visualize_btn = ttk.Button(
            buttons_frame, 
            text="Visualiseren in 3D",
            command=self.visualize_text,
            style="Accent.TButton"
        )
        self.visualize_btn.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Klaar om te beginnen")
        status_label = ttk.Label(
            main_frame, 
            textvariable=self.status_var,
            font=("Helvetica", 10, "italic")
        )
        status_label.pack(side=tk.BOTTOM, pady=10)
        
        # Stel de stijl in
        self.setup_styles()
    
    def setup_styles(self):
        """Configureer de stijlen voor de UI"""
        style = ttk.Style()
        
        # Configureer de hoofdstijl
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        style.configure("TLabelframe", background="#f0f0f0")
        style.configure("TLabelframe.Label", background="#f0f0f0", font=("Helvetica", 12, "bold"))
        
        # Maak een accent button stijl
        style.configure(
            "Accent.TButton",
            font=("Helvetica", 14, "bold"),
            background="#4287f5",
            foreground="white"
        )
    
    def create_html_files(self):
        """Creëer de benodigde HTML bestanden voor de 3D visualisatie"""
        # Maak een 'web' directory als die nog niet bestaat
        if not os.path.exists("web"):
            os.makedirs("web")
        
        # Maak het hoofdbestand voor de 3D visualisatie
        with open("web/3d_viewer.html", "w", encoding="utf-8") as f:
            f.write('''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Tekst Visualisatie</title>
    <style>
        body { 
            margin: 0; 
            overflow: hidden; 
            background-color: #1a1a1a;
            font-family: Arial, sans-serif;
        }
        #info {
            position: absolute;
            top: 10px;
            width: 100%;
            text-align: center;
            color: white;
            z-index: 100;
            display: block;
            font-size: 24px;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/FontLoader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/TextGeometry.js"></script>
</head>
<body>
    <div id="info">3D Tekst Visualisatie</div>

    <script>
        // Configuratie ophalen uit URL parameters
        const urlParams = new URLSearchParams(window.location.search);
        const textToShow = urlParams.get('text') || 'Python 3D';
        const rotationSpeed = parseFloat(urlParams.get('speed') || 1.0);
        const textColor = urlParams.get('color') || '#4287f5';
        
        // ThreeJS variabelen
        let scene, camera, renderer, textMesh;
        
        // Initialiseer de scène
        function init() {
            // Update de titel
            document.getElementById('info').textContent = textToShow;
            
            // Maak een nieuwe scene
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x1a1a1a);
            
            // Camera instellen
            camera = new THREE.PerspectiveCamera(
                70, 
                window.innerWidth / window.innerHeight, 
                0.1, 
                1000
            );
            camera.position.z = 5;
            
            // Renderer instellen
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.body.appendChild(renderer.domElement);
            
            // Voeg controls toe
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            
            // Belichting toevoegen
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            
            const pointLight = new THREE.PointLight(0xffffff, 1);
            pointLight.position.set(5, 5, 5);
            scene.add(pointLight);
            
            const pointLight2 = new THREE.PointLight(0xffffff, 0.5);
            pointLight2.position.set(-5, -5, 5);
            scene.add(pointLight2);
            
            // Laad een font en maak de 3D tekst
            const fontLoader = new THREE.FontLoader();
            fontLoader.load('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/fonts/helvetiker_bold.typeface.json', function(font) {
                const textGeometry = new THREE.TextGeometry(textToShow, {
                    font: font,
                    size: 0.8,
                    height: 0.2,
                    curveSegments: 12,
                    bevelEnabled: true,
                    bevelThickness: 0.03,
                    bevelSize: 0.02,
                    bevelOffset: 0,
                    bevelSegments: 5
                });
                
                textGeometry.center();
                
                const textMaterial = new THREE.MeshStandardMaterial({ 
                    color: new THREE.Color(textColor),
                    metalness: 0.3,
                    roughness: 0.4
                });
                
                textMesh = new THREE.Mesh(textGeometry, textMaterial);
                scene.add(textMesh);
                
                animate();
            });
            
            // Event listener voor window resize
            window.addEventListener('resize', onWindowResize);
        }
        
        // Herbereken camera en renderer bij window resize
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }
        
        // Animatie loop
        function animate() {
            requestAnimationFrame(animate);
            
            if (textMesh) {
                textMesh.rotation.y += 0.01 * rotationSpeed;
                textMesh.rotation.x += 0.005 * rotationSpeed;
            }
            
            renderer.render(scene, camera);
        }
        
        // Start de applicatie
        init();
    </script>
</body>
</html>''')
    
    def start_server(self):
        """Start een lokale HTTP server om de 3D visualisatie te tonen"""
        # Handler configureren
        handler = SimpleHTTPRequestHandler
        
        # Server in een aparte thread starten
        self.server = HTTPServer(('localhost', self.port), handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        
        self.status_var.set(f"Server draait op http://localhost:{self.port}")
        print(f"Server draait op http://localhost:{self.port}")
    
    def visualize_text(self):
        """Visualiseer de ingevoerde tekst in 3D"""
        text = self.text_entry.get().strip()
        if not text:
            messagebox.showwarning("Lege tekst", "Voer eerst een tekst in om te visualiseren.")
            return
        
        # Haal de opties op
        speed = self.speed_var.get()
        color = self.color_var.get()
        
        # Update status
        self.status_var.set(f"Visualiseren van: '{text}'")
        
        # Bouw de URL
        url = f"http://localhost:{self.port}/web/3d_viewer.html?text={text}&speed={speed}&color={color}"
        
        # Open de browser
        webbrowser.open(url)
    
    def on_closing(self):
        """Cleanup voor het afsluiten van de applicatie"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        
        self.root.destroy()

if __name__ == "__main__":
    # Start de GUI applicatie
    root = tk.Tk()
    app = TextVisualizer3D(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
