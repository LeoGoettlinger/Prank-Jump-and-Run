import arcade

#Aufgabe 1 (15 Punkte)
def on_key_press(self,symbol,modifiers):
    if symbol == arcade.key.C and modifiers & arcade.key.MOD_SHIFT:
        arcade.close_window()