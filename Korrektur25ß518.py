import arcade
sprite_liste = arcade.SpriteList()

# Aufgabe 1 (15 Punkte)
# Rechteck aus Kästchen zeichnen

for x in range(310,  591, 20):
    sprite = arcade.Sprite("textur.png")
    sprite.center_x = x
    sprite.center_y = 150
    sprite_liste.append(sprite)