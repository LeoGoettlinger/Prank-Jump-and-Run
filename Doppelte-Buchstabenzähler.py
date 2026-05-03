#wort = input("Bitte gib ein Wort ein: ")
import arcade

class MyWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)

        self.text_input_x = self.width 
        self.text_input_y = self.height * 3 / 4
        self.text_input_width = 200
        self.text_input_height = 30
        self.text_input_text = "Hallo"

        self.analyze_button_x = self.width 
        self.analyze_button_y = self.height 
        self.analyze_button_width = 200
        self.analyze_button_height = 30

        self.result_text = ""
        self.font_size = 12

    def on_draw(self):
        self.clear()

        # Draw text input
        arcade.draw_rectangle_filled(self.text_input_x, self.text_input_y,
                                     self.text_input_width, self.text_input_height, arcade.color.WHITE)
        arcade.draw_text(self.text_input_text, self.text_input_x - self.text_input_width  + 5,
                          self.text_input_y - self.text_input_height  + 5,
                          arcade.color.BLACK, font_size=self.font_size)

        # Draw button
        arcade.draw_rectangle_filled(self.analyze_button_x, self.analyze_button_y,
                                     self.analyze_button_width, self.analyze_button_height, arcade.color.LIGHT_GRAY)
        arcade.draw_text("Analysieren", self.analyze_button_x - self.analyze_button_width  + 5,
                          self.analyze_button_y - self.analyze_button_height  + 5,
                          arcade.color.BLACK, font_size=self.font_size)

        # Draw result text
        arcade.draw_text(self.result_text, self.width , self.height / 4, arcade.color.BLACK,
                          font_size=self.font_size, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.analyze_button_x - self.analyze_button_width  < x < self.analyze_button_x + self.analyze_button_width  and \
           self.analyze_button_y - self.analyze_button_height  < y < self.analyze_button_y + self.analyze_button_height :
            self.on_analyze_click()

        if self.text_input_x - self.text_input_width  < x < self.text_input_x + self.text_input_width  and \
           self.text_input_y - self.text_input_height  < y < self.text_input_y + self.text_input_height :
            self.on_text_input_click()

    def on_text_input(self, text):
        self.text_input_text += text

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            self.text_input_text = self.text_input_text[:-1]
        elif key == arcade.key.ENTER:
            self.on_analyze_click()

    def on_analyze_click(self):
        word = self.text_input_text
        counts = {}
        for char in word:
            counts[char] = counts.get(char, 0) + 1

        twice_chars = [char for char, count in counts.items() if count >= 2]
        self.result_text = f"Buchstaben, die mindestens zweimal vorkommen: {', '.join(twice_chars)}"

    def on_text_input_click(self):
        self.text_input_text = ""

def main():
    window = MyWindow(600, 400, "Buchstabenanalyse")
    arcade.run()

if __name__ == "__main__":
    main()