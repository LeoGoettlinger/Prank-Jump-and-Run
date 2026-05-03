import pyglet
pyglet.options["osx_alt_loop"] = True

import arcade, random

class Plattformer(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Its a Prank! Jump and Run")

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.tile_map = arcade.load_tilemap("Jump And Run.tmx", use_spatial_hash=True)

        self.szene = arcade.Scene.from_tilemap(self.tile_map)

        #Hintergrund = arcade.Sprite("min.png")
        #Hintergrund.center_x = 20
        #Hintergrund.center_y = 10
        self.spielerliste = arcade.SpriteList()

        self.spielfigur = arcade.Sprite("creeper.png", 0.04)
        self.spielfigur.center_x = 20
        self.spielfigur.center_y = 308
        self.szene.add_sprite("Spielfigur", self.spielfigur)
        self.spielerliste.append(self.spielfigur)

        self.audio_shutdown = arcade.load_sound("Windows-XP-Shutdown.wav")
       # self.shutdownsound = arcade.play_sound(self.audio_shutdown, looping=True)
        self.shutdownsound = None

        self.audio_error = arcade.load_sound("Windows-XP-Error.wav")
        self.errorsound = None

        self.verloren_sound = arcade.load_sound("Verlorensound.wav")
        self.verloren_sound_player = None

        self.audio_hacked = arcade.load_sound("You-are-hacked_.wav")
        self.hackedsound = None

        self.audio_nebenrisiken = arcade.load_sound("zu-nebenrisiken-und-wirkungen.wav")
        self.nebenrisiken_sound = None

        self.hintergrundmusik = arcade.load_sound("hintergrundmusik.wav")
        self.hintergrundmusik_sound = arcade.play_sound(self.hintergrundmusik, loop=True)

        self.epic_music = arcade.load_sound("epic_music.mp3")
        self.epic_music_sound = arcade.play_sound(self.epic_music, loop=True)
        arcade.stop_sound(self.epic_music_sound)

        self.level_1 = False
        self.level_2 = False
        self.level_3 = False

        self.start_menu = True

        self.gamemode = "Normal"
        self.freeze_player = False

        self.camera = arcade.camera.Camera2D()

        self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke"), self.szene.get_sprite_list("Tor 1"), self.szene.get_sprite_list("Tor 2"), self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke")]

        self.münzen_spritelist = self.szene.get_sprite_list("Münzen")

        self.tor1 = [self.szene.get_sprite_list("Tor 1"), self.szene.get_sprite_list("Reader 1")]

        self.tränke_multi_jump_spritelist = self.szene.get_sprite_list("Tränke Multi_Jump")
        self.tränke_plus_ein_herz_spritelist = self.szene.get_sprite_list("Tränke + 1 Herz")
        self.tränke_plus_zwei_herzen_spritelist = self.szene.get_sprite_list("Tränke + 2 Herzen")
        self.tränke_jump_boost_spritelist = self.szene.get_sprite_list("Tränke Jump_Boost")

        self.ladder_liste = self.szene.get_sprite_list("Wasser")

        self.physik_engine = arcade.PhysicsEnginePlatformer(player_sprite=self.spielfigur, platforms=self.walls, gravity_constant=0.1, ladders=self.ladder_liste)

        self.key_schatzraum = self.szene.get_sprite_list("Schlüssel Schatz-Raum")

        self.key_level_2 = self.szene.get_sprite_list("Schlüssel 2")

        self.tor2 = [self.szene.get_sprite_list("Tor 2"), self.szene.get_sprite_list("Hebel Level 2")]

        self.schatzraum_protector = [self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke"), self.szene.get_sprite_list("Activate Schatz-Raum")]

        self.multi_jump = False

        self.plus1herz = False
        self.plus1herz_timer = -1

        self.plus2herzen = False
        self.plus2herzen_timer = -1

        self.schaden_immun = False

        self.schaden_immun_timer = 0
        
        self.schaden_immun_anzeigen = False

        self.interact = True

#        self.koordinaten_anzeigen = False

        self.springen_höhe = 0.65

        self.höher_springen = False

        self.zeit_multi_jump = 0

        self.zeit_jump_boost = 0

        self.jump_boost = False

        self.münzen = 0

        self.lives = 4

        self.schätze = 0

        self.level_3 = False
    
#        self.schatz_raum_offen = False

        self.verloren = False

        self.gewonnen = False
    
        self.schlüssel_level1 = False

        self.genutzte_zeit = 0
        
        self.verbleibende_zeit = 300

        self.verbleibende_zeit_use = True

#        self.pause = False

#        self.teleport = False

        self.verloren_sound_gespielt = False

        self.key_level_2_have = False

        self.key_schatzraum_have = False

        self.schatz_liste = self.szene.get_sprite_list("Schatz-Kiste")
    
        self.verbleibende_zeit_show = False

        self.genutzte_zeit = 0

        self.genutzte_zeit_show = True

        self.tränke = True

        self.setup()

#        self.ich_habe_keine_ahnung = print("Ich habe keine Ahnung!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#        print("Ich mag Züge!!!!!!!!(Wenn diese Nachricht angezeigt wird dann ist __init__ durchgelaufen)")

    def setup(self):

        line = "===================================================="
    
        print(line)
        print("       IT'S A PRANK JUMP & RUN Beta 0.1 - Setup             ")
        print(line)
        print("Welcome to the Prank! Viel Spaß beim Hüpfen.")
        print(f"Code & Design by: SampleCraft (Leo Göttlinger)")
        print(line)
        
        # Kurz und knackig - das Wichtigste für den Spieler
        print("STEUERUNG:")
        print("  Bewegung       : Pfeiltasten oder WASD")
        print("  Springen/Aktion: Leertaste")
        print("  Beenden (Quit) : Q")
        print("  Reset/Neustart : R")
        print("  Musik an/aus    : M")
        print(line)

        # Rechtlicher Part: Kurz, aber deutlich
        print("RECHTLICHES & COPYRIGHT:")
        print("© 2025-2026 Leo Göttlinger (SampleCraft)")
        print("Der Code und alle Assets sind mein Eigentum.")
        print("Kopieren, Verändern oder Verbreiten ohne meine Erlaubnis ist nicht gestattet!")
        print("Mehr Infos in der LICENSE-Datei!")
        print(line)
        print("Ideen oder Bugs gerne auf GitHub melden: https://github.com/LeoGoettlinger/Prank-Jump-and-Run/issues")
        print(line)

        # Die Abfrage
        check = input("Akzeptierst du die Bedingungen? (ja/nein): ").strip().lower()

        if check == "ja":
            print("Spiel wird geladen...")
            print("Lade Map... Lade Sprites... Bereite Fallen vor...")
            print("LOS GEHT'S!")
            print(line)

            print("")
            print(line)
            print("SETTINGS:")
            print(line)
        
            # Helper function to get boolean input
            def get_boolean_input(prompt, default_value):
                user_input = input(f"{prompt} (True oder False, Standard: {default_value}): ").strip().lower()
                if user_input == "true":
                    return True
                elif user_input == "false":
                    return False
                print(f"Ungültige Eingabe oder leer. Verwende Standardwert: {default_value}")
                return default_value

            # Helper function to get numeric input
            def get_numeric_input(prompt, default_value, type_converter=float):
                user_input = input(f"{prompt} (Standard: {default_value}): ").strip()
                if user_input:
                    try:
                        return type_converter(user_input)
                    except ValueError:
                        print(f"Ungültige Eingabe. Verwende Standardwert: {default_value}")
                        return default_value
                print(f"Leere Eingabe. Verwende Standardwert: {default_value}")
                return default_value

            print("It´s a Prank Jump & Run Setup/Settings:")
            
            self.verbleibende_zeit_use = get_boolean_input("Verbleibende Zeit verwenden?", True)
            if self.verbleibende_zeit_use:
                self.verbleibende_zeit = get_numeric_input("Verbleibende Zeit eingeben (in Sekunden)", 300.0)
                self.verbleibende_zeit_show = get_boolean_input("Verbleibende Zeit anzeigen?", True)
            else:
                self.verbleibende_zeit = 300.0 # Reset to default if not used, or keep initial value
                self.verbleibende_zeit_show = False

            self.tränke = get_boolean_input("Tränke aktivieren?", True)
            self.lives = get_numeric_input("Anzahl Start-Leben eingeben", 4, int)
            # Store the initial value for resetting later if needed, and set current timer
            self.schaden_immun_timer_initial = get_numeric_input("Zeit der Schaden-Immunität nach einem Treffer eingeben (in Sekunden)", 3.0)
            self.schaden_immun_timer = self.schaden_immun_timer_initial
            self.genutzte_zeit_show = get_boolean_input("Genutzte Zeit anzeigen?", True)

            # Ensure other timers are floats for arithmetic operations
            self.plus1herz_timer = -1.0
            self.plus2herzen_timer = -1.0
            self.zeit_multi_jump = 0.0
            self.zeit_jump_boost = 0.0
            self.genutzte_zeit = 0.0

        else:
            print("Schade! Ohne Zustimmung kein Spiel.")
            print("Das Programm wird geschlossen.")
            print(line)
            arcade.exit()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.exit()
        elif symbol == arcade.key.R:
            self.__init__()
        elif self.interact == True:
#            if self.start_menu:
#                if symbol == arcade.key.KEY_1:
#                    self.gamemode = "Einfach"
#                elif symbol == arcade.key.KEY_2:
#                    self.gamemode = "Normal"
#                elif symbol == arcade.key.KEY_3:
#                    self.gamemode = "Schwer"
#                elif symbol == arcade.key.ENTER or symbol == arcade.key.RETURN:
#                    print(f"Spiel gestartet mit Schwierigkeit: {self.gamemode}")
#                    self.start_menu = False
#                    self.freeze_player = False
#                return
#
#                    self.pause = False
#                # if symbol == arcade.key.UP or symbol == arcade.key.W:
#               # self.spielfigur.change_y = 3
            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.spielfigur.change_x = -1.0
            # elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
        #      self.spielfigur.change_y = -3
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.spielfigur.change_x = 1.0
            #elif symbol == arcade.key.R:
            #   self.setup()
            elif symbol == arcade.key.SPACE or symbol == arcade.key.UP or symbol == arcade.key.W:
                if self.physik_engine.can_jump() == True:
                    self.spielfigur.change_y = 2.9
                    #self.multi_jump = True
#                elif symbol == arcade.key.T:
#                    if self.teleport == False:
#                        self.teleport = True
#                    else:
#                        self.teleport = False
            #elif symbol == arcade.key.B:
        #     self.setup()
#            elif symbol == arcade.key.K:
#                if self.koordinaten_anzeigen == False:
#                    self.koordinaten_anzeigen = True
#                else:
#                    self.koordinaten_anzeigen = False
            elif symbol == arcade.key.M:
                if self.hintergrundmusik_sound.playing == True:
                    arcade.stop_sound(self.hintergrundmusik_sound)
                else:
                    self.hintergrundmusik_sound = arcade.play_sound(self.hintergrundmusik, loop=True)

       # print("Ich mag Züge3!!!!!!!!(Wenn diese Nachricht angezeigt wird dann ist on_key_press() durchgelaufen)")

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.W or symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.spielfigur.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A or symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.spielfigur.change_x = 0

    def _clamp(self, wert, min, max):
        if wert < min:
            return min
        elif wert > max:
            return max
        else:
            return wert

    def on_update(self, delta_time):
        

        self.camera.position = (self._clamp(self.spielfigur.position[0], self.width / 2, self.tile_map.width * self.tile_map.tile_width * self.tile_map.scaling - self.width / 2), self._clamp(self.spielfigur.position[1], self.height / 2, self.tile_map.height * self.tile_map.tile_height * self.tile_map.scaling - self.height / 2))

        self.physik_engine.update()

        self.spielerliste.update()

        self.zeit_multi_jump -= delta_time
        
        self.zeit_jump_boost -= delta_time

        self.plus1herz_timer -= delta_time

        self.plus2herzen_timer -= delta_time
        
        if self.zeit_multi_jump <= 0:
            self.multi_jump = False
            self.physik_engine.disable_multi_jump()
            self.zeit_multi_jump = 0
        
        if self.zeit_jump_boost <= 0:
            self.höher_springen = False
            self.springen_höhe = 0.65
            self.physik_engine.gravity_constant = 0.166
            self.zeit_jump_boost = 0

        if self.plus1herz_timer > 0:
            self.plus1herz = True
        else:
            self.plus1herz = False
            self.plus1herz_timer = 0
        
        if self.plus2herzen_timer > 0:
            self.plus2herzen = True
        else:
            self.plus2herzen = False
            self.plus2herzen_timer = 0

        if self.verbleibende_zeit_use: # This is now a boolean
            if self.verbleibende_zeit <= 0:
                self.verloren = True
            self.verbleibende_zeit_show = True

        #ifn arcade.check_for_collision_with_list(self.spielfigur, self.):
        if self.tränke == True:
            if arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_ein_herz_spritelist):
                for trank in arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_ein_herz_spritelist): # Iterate over a copy or kill outside loop
                    self.lives += 1
                    self.plus1herz_timer = 3
                trank.kill()
            
            if arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_zwei_herzen_spritelist):
                for trank in arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_zwei_herzen_spritelist):
                    self.lives += 2
                    self.plus2herzen_timer = 3
                trank.kill()

        if arcade.check_for_collision_with_list(self.spielfigur, self.schatz_liste):
            for schatz in arcade.check_for_collision_with_list(self.spielfigur, self.schatz_liste):
                self.schätze += 1 # This should be outside the loop if only one treasure is picked up at a time
            schatz.kill()

        if arcade.check_for_collision_with_list(self.spielfigur, self.key_schatzraum):
#            for key in arcade.check_for_collision_with_list(self.spielfigur, self.key_schatzraum):
            self.key_schatzraum_have = True
            self.szene.get_sprite_list("Schlüssel Schatz-Raum").clear()

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Activate Schatz-Raum")) and self.key_schatzraum_have == True:
#            for tor2 in arcade.check_for_collision_with_list(self.spielfigur, self.schatzraum_protector):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke")]
            self.szene.get_sprite_list("Activate Schatz-Raum").clear()
            self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke").clear()

        if arcade.check_for_collision_with_list(self.spielfigur, self.key_level_2):
#            for key in arcade.check_for_collision_with_list(self.spielfigur, self.key_level_2):
            self.key_level_2_have = True
            self.szene.get_sprite_list("Schlüssel 2").clear()
            
        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Hebel Level 2")) and self.key_level_2_have == True:
#            for tor3 in arcade.check_for_collision_with_list(self.spielfigur, self.tor2):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke")]
            self.szene.get_sprite_list("Hebel Level 2").clear()
            self.szene.get_sprite_list("Tor 2").clear()
            self.level_3 = True

        if self.tränke == True:
            if arcade.check_for_collision_with_list(self.spielfigur, self.tränke_multi_jump_spritelist): # Iterate over a copy or kill outside loop
                for trank in arcade.check_for_collision_with_list(self.spielfigur, self.tränke_multi_jump_spritelist):
                    self.zeit_multi_jump = 5.5
                    self.multi_jump = True
                    self.physik_engine.enable_multi_jump(allowed_jumps=2)
                trank.kill()
            
            if arcade.check_for_collision_with_list(self.spielfigur, self.tränke_jump_boost_spritelist):
                for trank in arcade.check_for_collision_with_list(self.spielfigur, self.tränke_jump_boost_spritelist): # Iterate over a copy or kill outside loop
                    self.zeit_jump_boost = 13
                    self.höher_springen = True
                    self.physik_engine.gravity_constant = 0.12
                    trank.kill()

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Ziel")):
            self.gewonnen = True

        if self.verloren == False:
            self.schaden_immun_timer -= delta_time 
            self.genutzte_zeit += delta_time
            if self.verbleibende_zeit_use:
                self.verbleibende_zeit -= delta_time
        
        if self.schaden_immun_timer <= 0:
            self.schaden_immun_timer = 0
            self.schaden_immun = False
            self.schaden_immun_anzeigen = False

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Teleporter Oben")): 
            self.spielfigur.center_x = 41
            self.spielfigur.center_y = 557

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Röhre")): 
            self.spielfigur.center_x = 300
            self.spielfigur.center_y = 349
        
        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Teleporter Münze")): 
            self.spielfigur.center_x = 278
            self.spielfigur.center_y = 525

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Schlüssel 1")):
#            for schlüssel in arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Schlüssel 1")):
            self.spielfigur.center_x = 788
            self.spielfigur.center_y = 370
            print("ICH MAG ZÜGE!")
            self.schlüssel_level1 = True
            self.szene.get_sprite_list("Schlüssel 1").clear()

        if arcade.check_for_collision_with_list(self.spielfigur, self.münzen_spritelist):
            for münze in arcade.check_for_collision_with_list(self.spielfigur, self.münzen_spritelist):
                self.münzen += 1 # This should be outside the loop if only one coin is picked up at a time
                münze.kill()
        
        if self.schaden_immun == False:
            if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Stachel")):
                self.lives -= 1
                self.schaden_immun = True
                self.schaden_immun_timer = 3
                self.schaden_immun_anzeigen = True

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Reader 1")) and self.schlüssel_level1 == True:
            print("Ich mag Züge!!")
#            for tor1 in arcade.check_for_collision_with_list(self.spielfigur, self.tor1):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke"), self.szene.get_sprite_list("Tor 2"), self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke")]
            self.szene.get_sprite_list("Reader 1").clear()
            self.szene.get_sprite_list("Tor 1").clear()

        if self.lives == 0:
            self.verloren = True
            #self.__init__()

        if self.level_3 == True:
            if self.hintergrundmusik.is_playing():
                arcade.stop_sound(self.hintergrundmusik)
                self.epic_music.play()

            else:
                self.epic_music.play()


        if self.verloren and not self.verloren_sound_gespielt:
            arcade.play_sound(self.verloren_sound)
            self.verloren_sound_gespielt = True # Merken, damit er nicht 60x pro Sekunde startet
        # cam_x, cam_y = self.camera.position

        # self.camera.position = self.spielfigur.position
        
        # if cam_x <= 0:
        #     print(random.randint(1, 100))
        #     print(self.spielfigur.position)
        #     print(self.camera.position)
        #     self.camera.position = (0, cam_y)





        #self.verbleibende_zeit -= delta_time

    #     arcade.check_for_collision(self.spielerliste, self.spielfigur, self.gewonnen)

        #  print("Ich mag Züge4!!!!!!!!(Wenn diese Nachricht angezeigt wird dann ist on_update() durchgelaufen)")
        
                                       
    def on_draw(self):

        cam_x = self.camera.position[0]
        cam_y = self.camera.position[1]
    
#        if self.pause == True:
#            self.freeze_player = True
#            arcade.draw_lrbt_rectangle_filled(cam_x + 3, cam_y + 3, arcade.color.BROWN)
#            arcade.draw_text("PAUSE", cam_x  , cam_y  , arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center",anchor_y="center")
#            arcade.draw_text("Klicke P erneut um das Spiel fortzusetzen", cam_x + 300, cam_y  - 200, arcade.color.WHITE)
#          #   if symbol == arcade.key.P:
         #       self.freeze_player = False
          #      self.pause = False

#        if self.start_menu:
#            self.clear()
#            # Kamera NICHT benutzen im Startmenü!
#            arcade.draw_text("Hallo!", self.width , self.height - 60, arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center",anchor_y="center")
#            arcade.draw_text("Wähle ein Schwierigkeitsgrad:", self.width , self.height - 120, arcade.color.WHITE, 24, font_name="Kenney Future", anchor_x="center",anchor_y="center")
#            arcade.draw_text("Drücke 1 für Einfach, 2 für Normal, 3 für Schwer", self.width , self.height - 160, arcade.color.WHITE, 18, font_name="Kenney Future", anchor_x="center",anchor_y="center")
#            arcade.draw_text(f"Aktuelle Schwierigkeit: {self.gamemode}", self.width , self.height - 200, arcade.color.WHITE, 18, font_name="Kenney Future", anchor_x="center",anchor_y="center")
 #           arcade.draw_text("Drücke ENTER um zu starten", self.width , self.height - 240, arcade.color.WHITE, 18, font_name="Kenney Future", anchor_x="center",anchor_y="center")
#        else:
        self.clear()

        self.camera.use()

        self.szene.draw()

        self.spielerliste.draw()

        #self.hindernisliste.draw()

        arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", cam_x + 385, cam_y  - 285,  font_size=18, font_name="Kenney", anchor_x="right")

        arcade.draw_text(f"Leben: {round(self.lives, 1)}", cam_x + -288, cam_y  - -270,  font_size=18, font_name="Kenney", anchor_x="right")

        arcade.draw_text(f"Schätze: {round(self.schätze, 1)}", cam_x + -273, cam_y  - 285,  font_size=18, font_name="Kenney", anchor_x="right")

#        if self.koordinaten_anzeigen == True:
#            arcade.draw_text(f"Koordinaten: X: {round(self.spielfigur.center_x)}, Y: {round(self.spielfigur.center_y)}", cam_x + 150, cam_y - 215,  font_size=18, anchor_x="right")

        if self.schaden_immun_anzeigen == True:
            arcade.draw_text(f"Du kriegst noch für: {round(self.schaden_immun_timer, 1)} keinen Schaden!", cam_x + 230, cam_y  - 225,  font_size=18, font_name="Kenney", anchor_x="right")
        
        if self.höher_springen == True:
            arcade.draw_text(f"Du hast noch für {round(self.zeit_jump_boost, 1)} Sekunden Jump Boost!", cam_x + 250, cam_y  - 250,  font_size=18, font_name="Kenney", anchor_x="right")
        
        if self.multi_jump == True:
            arcade.draw_text(f"Du hast noch für {round(self.zeit_multi_jump, 1)} Sekunden Multi Jump!", cam_x + 250, cam_y  - 260,  font_size=18, font_name="Kenney", anchor_x="right")
            
        if self.plus1herz == True:
            arcade.draw_text(f"+1 Herz", cam_x + 45, cam_y  - 200,  font_size=18, font_name="Kenney", anchor_x="right")
        
        if self.plus2herzen == True:
            arcade.draw_text(f"+2 Herzen", cam_x + 45, cam_y  - 210,  font_size=18, font_name="Kenney", anchor_x="right")
        
        if self.verbleibende_zeit_show == True:
            arcade.draw_text(f"Verbleibende Zeit: {round(self.verbleibende_zeit, 1)} Sekunden", cam_x + 385, cam_y  - 265,  font_size=18, font_name="Kenney", anchor_x="right")
        if self.genutzte_zeit_show == True:
            arcade.draw_text(f"Genutzte Zeit: {round(self.genutzte_zeit, 1)} Sekunden", cam_x + 385, cam_y  - 245,  font_size=18, font_name="Kenney", anchor_x="right")

    #  arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", 780, 20,  font_size=18, font_name="Kenney", anchor_x="right")

    #   arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", 780, 20,  font_size=18, font_name="Kenney", anchor_x="right")
        
    #  arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", 780, 20,  font_size=18, font_name="Kenney", anchor_x="right")

        #print("Ich mag Züge5!!!!!!!!(Wenn diese Nachricht angezeigt wird dann ist on_draw() durchgelaufen)")
        if self.gewonnen == True:
            self.interact = False
#                arcade.play_sound(self.audio_shutdown)
            arcade.stop_sound(self.hintergrundmusik_sound)
            arcade.draw_lrbt_rectangle_filled(cam_x, cam_x , cam_y , cam_y, arcade.color.GREEN)
            arcade.draw_text("GEWONNEN", cam_x + 3, cam_y + 3, arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center",anchor_y="center")
            arcade.draw_text("Klicke R um das Spiel erneut zu starten", cam_x - 125, cam_y - 70, arcade.color.WHITE)

        if self.verloren == True:
            self.interact = False
            arcade.stop_sound(self.hintergrundmusik_sound)
            arcade.stop_sound(self.epic_music_sound)
            arcade.draw_lrbt_rectangle_filled(cam_x, cam_x , cam_y , cam_y, arcade.color.RED)
            # arcade.draw_lrtb_rectangle_filled(0, self.camera, self.camera.position , 0, arcade.color.RED)
            arcade.draw_text("VERLOREN", cam_x + 3, cam_y + 3, arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center",anchor_y="center")
            arcade.draw_text("Klicke R um das Spiel erneut zu starten", cam_x - 125, cam_y - 70, arcade.color.WHITE)



Plattformer()
arcade.run()