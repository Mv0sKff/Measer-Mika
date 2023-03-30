---
marp: true
title: MeasureMika
theme: uncover
paginate: true
footer: 'MeasureMika - Jonas Geiger, Marcel Pfaff und Sascha Schrempp'
backgroundColor: white
---

<style>
    footer {
        font-size: 25px;
    }
</style>

<!-- _paginate: false -->
<!-- _footer: 'Jonas Geiger, Marcel Pfaff und Sascha Schrempp' -->

<style scoped>
    h1 {
        font-size: 124px;
    }
    footer {
        font-size: 40px;
        color: black;
    }
</style>

# MeasureMika
Höhenmessung mit App
<!-- Powereinstieg  -->

---

# Was ist MeasureMika, grobe funktionsweise

---

# Innere Logik
## Aufbau / Klassen

---

### MeasureMikaApp()
- Hauptklasse
- Permissions
- Initialisiert Unterklassen

---

### MainWindow()
- Eingabe der Größe
- CheckData()
- Anleitung
- Button

![bg right:28% 100%](images/StartScreen.png)

---

### SecondWindow()
- Kamera
- Buttons zur Navigation
- Anwendungstipps
- Index
- Live Abstand

![bg left:28% 110%](images/KameraSrceen.png)

---

### ThirdWindow()
- Ergebnis Ansicht
- Ergebnis Speichern 
(not implemented)

![bg right:28% 110%](images/ErgebnisAnsicht.png)

---

# Berechnen der Distanz

---

# Berechnen der Höhe

---

<style scoped>
    tr {
        font-size: 30px;
        font-weight: bold;
    }
    h1 {
        font-size: 60px;
    }
</style>

# Danke für Eure Aufmerksamkeit

![bg right:49% 110%](images/RocketStonks.jpg)


