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

# Anforderungen

- Höhenmessung
- Kamera
- Neigungssensoren

---

# Was ist MeasureMika, grobe Funktionsweise

---

<!-- _backgroundColor: #222222-->
![bg right: 33% 85%](images/StartScreen.png)
![bg right: 33% 85%](images/KameraSrceen.png)
![bg right: 33% 85%](images/ErgebnisAnsicht.png)
<!-- _footer: '' -->
<!-- _paginate: false -->

---

# Innere Logik

## Aufbau und Klassen

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
- Tiefster Punkt
- Buttons zur Navigation
- Anwendungstipps
- Index
- Live Abstand

![bg left:28% 110%](images/KameraSrceen.png)

---

### SecondWindow()

- Kamera
- Höchster Punkt

![bg right:28% 110%](images/KameraScreen2.png)

---

### ThirdWindow()

- Ergebnis Ansicht
- Ergebnis Speichern
(not implemented)

![bg left:28% 102%](images/ErgebnisAnsicht.png)

---

# Berechnen der Distanz

---

![bg 100% 100%](images/math1.png)

---

![bg 100% 100%](images/math2.png)

---

# Berechnen der Höhe

---

<!-- _footer: '' -->
<!-- _paginate: false -->

![bg 100% 100%](images/math3.png)

---

<!-- _footer: '' -->
<!-- _paginate: false -->

![bg 100% 100%](images/math4.png)

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
