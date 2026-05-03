# Aufgabe 1.2 (5 Punkte)
# Erstelle ein Arcade-Kameraobjekt, das auf die Fensterbreite 800 und Fensterhöhe 600 eingestellt ist, und speichere dieses in einer Variable kamera.
kamera = arcade.Camera(800, 600)

# Aufgabe 1.2 (5 Punkte
# Bewege kamera zur in der Variable spielerposition gespeicherten Position.
kamera.move_to(spielerposition)

# Aufgabe 1.3 (5 Punkte)
# Aktiviere kamera.
kamera.use()