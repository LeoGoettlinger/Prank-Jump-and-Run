import arcade
class Spieler(arcade.Sprite):
     def update(self, delta_time):
        self.center_x += self.change_x
        self.change_y += self.change_y
        
        if self.left < 0:
            self.left = 0
        if self.right > 800:
            self.right = 800
        if self.top > 600:
            self.top = 600
        if self.bottom < 600:
            self.bottom = 600
