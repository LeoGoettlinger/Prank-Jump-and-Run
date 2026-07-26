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
        self.hintergrundmusik_sound = None # arcade.play_sound(self.hintergrundmusik, loop=True)

        self.epic_music = arcade.load_sound("epic_music.mp3")
        self.epic_music_sound = None # arcade.play_sound(self.epic_music, loop=True)
        # arcade.stop_sound(self.epic_music_sound)

        self.advancement_sound = arcade.load_sound("achievement.mp3")
        self.advancement_player = None# arcade.play_sound(self.advancement_sound)
        # arcade.stop_sound(self.advancement_player)

        self.coin_sound = arcade.load_sound("coin_collect.mp3")
        self.coin_player = None # arcade.play_sound(self.coin_sound)
        # arcade.stop_sound(self.coin_player)

        self.trank_sound = arcade.load_sound("trank.mp3")
        self.trank_player = None # arcade.play_sound(self.trank_sound)
        # arcade.stop_sound(self.trank_player)

        self.item_sound = arcade.load_sound("item-collect.mp3")
        self.item_player = None # arcade.play_sound(self.item_sound)
        # arcade.stop_sound(self.item_player)

        self.damage_sound = arcade.load_sound("damage.mp3")
        self.damage_player = None # arcade.play_sound(self.damage_sound)
        # arcade.stop_sound(self.damage_player)

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

        self.reset = False

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

        self.verbleibende_zeit_use = False

#        self.pause = False

#        self.teleport = False

        self.verloren_sound_gespielt = False

        self.key_level_2_have = False

        self.key_schatzraum_have = False

        self.schatz_liste = self.szene.get_sprite_list("Schatz-Kiste")
    
        self.verbleibende_zeit_show = False

        self.genutzte_zeit = 0

        self.genutzte_zeit_show = True

        self.verbleibende_zeit_start = False

        self.tränke = True

        self.gewonnen_sound_gespielt = False

        self.level3_music_switched = False

        self.erstes_update = True

        self.achievement_timer = 0.0

        self.achievement_displayed = False

        self.achievement = None

        self.achievement_stack = None

        self.achievement_stack_timer = 0.0

        self.achievement_new = None

        self.achievement_timer_new = 0.0

        self.genutzte_zeit_use = True

        arcade.load_font(":resources:fonts/ttf/Kenney/Kenney_Pixel.ttf")
        arcade.load_font(":resources:fonts/ttf/Kenney/Kenney_Blocks.ttf")

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

        # Steuerung
        print("STEUERUNG:")
        print("  Bewegung       : Pfeiltasten oder WASD")
        print("  Springen/Aktion: Leertaste")
        print("  Beenden (Quit) : Q")
        print("  Reset/Neustart : R")
        print("  Musik an/aus   : M")
        print(line)

        # Rechtliches
        print("RECHTLICHES & COPYRIGHT:")
        print("© 2025-2026 Leo Göttlinger (SampleCraft)")
        print("Der Code und alle Assets sind mein Eigentum.")
        print("Kopieren, Verändern oder Verbreiten ohne meine Erlaubnis ist nicht gestattet!")
        print("Mehr Infos in der LICENSE-Datei!")
        print(line)
        print("Ideen oder Bugs gerne auf GitHub melden: https://github.com/LeoGoettlinger/Prank-Jump-and-Run/issues")
        print(line)

        # Bedingungen
        check = input("Akzeptierst du die Bedingungen? (ja/nein): ").strip().lower()
        if check != "ja":
            print("Schade! Ohne Zustimmung kein Spiel.")
            print("Das Programm wird geschlossen.")
            print(line)
            arcade.exit()
            quit()

        print("Spiel wird geladen...")
        print("Lade Map... Lade Sprites... Bereite Fallen vor...")
        print("LOS GEHT'S!")
        print(line)

        # ----- Hilfsfunktionen (müssen vor der Verwendung definiert sein) -----
        def get_boolean_input(prompt, default_value):
            user_input = input(f"{prompt} (True oder False, Standard: {default_value}): ").strip().lower()
            if user_input == "true":
                return True
            elif user_input == "false":
                return False
            print(f"Ungültige Eingabe oder leer. Verwende Standardwert: {default_value}")
            return default_value

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

        print("")
        print(line)
        print("SETTINGS:")
        print(line)

        # ----- Preset-Auswahl -----
        print("Wähle ein Schwierigkeits-Preset:")
        print("  1 = Easy")
        print("  2 = Normal")
        print("  3 = Hardcore")
        print("  4 = Custom (individuelle Einstellungen)")
        preset = input("Deine Wahl (1-4): ").strip()

        if preset == "1":          # Easy
            self.lives = 6
            self.verbleibende_zeit = 600.0
            self.tränke = True
            self.schaden_immun_timer = 2.0
            self.verbleibende_zeit_show = True
            self.verbleibende_zeit_start = True
            self.genutzte_zeit_show = True
            print("Preset 'Easy' geladen.")
        elif preset == "2":        # Normal
            self.lives = 4
            self.verbleibende_zeit = 300.0
            self.tränke = True
            self.schaden_immun_timer = 3.0
            self.verbleibende_zeit_show = True
            self.verbleibende_zeit_start = True
            self.genutzte_zeit_show = True
            print("Preset 'Normal' geladen.")
        elif preset == "3":        # Hardcore
            self.lives = 3
            self.verbleibende_zeit = 120.0
            self.tränke = False
            self.schaden_immun_timer = 0.0
            self.verbleibende_zeit_show = True
            self.verbleibende_zeit_start = True
            self.genutzte_zeit_show = True
            print("Preset 'Hardcore' geladen.")
        elif preset == "4":        # Custom
            print("Custom-Modus – du wirst nun alle Einstellungen selbst festlegen.")
            self.verbleibende_zeit_start = get_boolean_input("Verbleibende Zeit verwenden?", True)
            if self.verbleibende_zeit_start:
                self.verbleibende_zeit = get_numeric_input("Verbleibende Zeit eingeben (in Sekunden)", 300.0)
                self.verbleibende_zeit_show = get_boolean_input("Verbleibende Zeit anzeigen?", True)
            else:
                self.verbleibende_zeit_use = False
                self.verbleibende_zeit_show = False

            self.tränke = get_boolean_input("Tränke aktivieren?", True)
            self.lives = get_numeric_input("Anzahl Start-Leben eingeben", 4, int)
            self.schaden_immun_timer = get_numeric_input("Zeit der Schaden-Immunität nach einem Treffer (in Sekunden)", 3.0)
            self.genutzte_zeit_show = get_boolean_input("Genutzte Zeit anzeigen?", True)
            self.genutzte_zeit_use = get_boolean_input("Genutzte Zeit aktivieren?", True)
        else:
            print("Ungültige Eingabe – es wird das Preset 'Normal' verwendet.")

        # Timer initialisieren (einheitlich für alle Modi)
        self.plus1herz_timer = -1.0
        self.plus2herzen_timer = -1.0
        self.zeit_multi_jump = 0.0
        self.zeit_jump_boost = 0.0
        self.genutzte_zeit = 0.0
        self.verbleibende_zeit_use = self.verbleibende_zeit_start  # Timer nur aktivieren, wenn der Spieler dies gewählt hat

        # === NEU: Einstellungen für den lautlosen Reset sichern ===
        self.initial_lives = self.lives
        self.initial_verbleibende_zeit = self.verbleibende_zeit
        self.initial_tränke = self.tränke
        self.initial_schaden_immun_timer = self.schaden_immun_timer
        self.initial_verbleibende_zeit_show = self.verbleibende_zeit_show
        self.initial_verbleibende_zeit_start = self.verbleibende_zeit_start
        self.initial_verbleibende_zeit_use = self.verbleibende_zeit_use
        self.initial_genutzte_zeit_show = self.genutzte_zeit_show
        self.initial_genutzte_zeit_use = self.genutzte_zeit_use

        self.genutzte_zeit_use = self.genutzte_zeit_show

        # Hintergrundmusik starten
        self.hintergrundmusik_sound = arcade.play_sound(self.hintergrundmusik, loop=True)

        print("\nFERTIG! Das Spiel startet jetzt.")
        print(line)
        print("Funfact: Marcus hat das Game auf Hardcore mit 2 Leben und 79.3 Sekunden und auch einmal mit 1 Leben und 91.5 Sekunden noch übrig gewonnen. Schaffst du das auch? ;)")
        print(line)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.exit()
        elif symbol == arcade.key.R:
            self.reset = True
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
                if self.hintergrundmusik_sound and self.hintergrundmusik_sound.playing:
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

        if self.erstes_update:
            self.erstes_update = False
            return

        self.camera.position = (self._clamp(self.spielfigur.position[0], self.width / 2, self.tile_map.width * self.tile_map.tile_width * self.tile_map.scaling - self.width / 2), self._clamp(self.spielfigur.position[1], self.height / 2, self.tile_map.height * self.tile_map.tile_height * self.tile_map.scaling - self.height / 2))

        self.physik_engine.update()

        self.spielerliste.update()

        self.zeit_multi_jump -= delta_time
        
        self.zeit_jump_boost -= delta_time

        self.plus1herz_timer -= delta_time

        self.plus2herzen_timer -= delta_time

        # Achievement-Timer aktualisieren
        self.achievement_timer -= delta_time
        self.achievement_stack_timer -= delta_time

        # --- NEUE LOGIK FÜR ACHIEVEMENTS (angepasst an deine Beschreibung) ---
        # Wenn ein neues Achievement empfangen wird
        if self.achievement_new is not None:
            # Falls gerade *kein* Achievement angezeigt wird (Timer abgelaufen)
            if self.achievement_timer <= 0:
                # Zeige das neue Achievement direkt an
                self.achievement = self.achievement_new
                self.achievement_timer = self.achievement_timer_new
                self.achievement_displayed = True
            # Falls gerade *ein* Achievement angezeigt wird (Timer läuft noch)
            else:
                # Lege das neue Achievement in den Stack
                # (Das alte Achievement im Stack würde hier überschrieben)
                self.achievement_stack = self.achievement_new
                self.achievement_stack_timer = self.achievement_timer_new
            # Zurücksetzen der neuen Achievement-Daten
            self.achievement_new = None
            self.achievement_timer_new = 0.0

        # Wenn das *aktuelle* Achievement fertig angezeigt ist
        if self.achievement_timer <= 0 and self.achievement is not None:
            # Verstecke das aktuelle Achievement
            self.achievement_displayed = False
            self.achievement = None
            self.achievement_timer = 0.0
            # Achievement aus dem Stack (falls vorhanden) wird automatisch im nächsten Frame
            # (oder sobald ein neues Achievement eintrifft und der Timer <= 0 ist) behandelt

        # Wenn das *aktuelle* Achievement fertig ist UND ein Achievement im Stack wartet
        if self.achievement_timer <= 0 and self.achievement is None and self.achievement_stack is not None:
            # Verschiebe das Achievement aus dem Stack ins Haupt-Achievement
            self.achievement = self.achievement_stack
            self.achievement_timer = self.achievement_stack_timer
            self.achievement_displayed = True
            # Leere den Stack
            self.achievement_stack = None
            self.achievement_stack_timer = 0.0

        if self.achievement_timer <= 0:
            self.achievement_displayed = False
            self.achievement = None
            self.achievement_timer = 0.0
        
        if self.zeit_multi_jump <= 0:
            self.multi_jump = False
            self.physik_engine.disable_multi_jump()
            self.zeit_multi_jump = 0
        
        if self.zeit_jump_boost <= 0:
            self.höher_springen = False
            self.springen_höhe = 0.65
            self.physik_engine.gravity_constant = 0.1
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

        #ifn arcade.check_for_collision_with_list(self.spielfigur, self.):
        if self.tränke == True:
            hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_ein_herz_spritelist)
            for trank in hit_list:
                self.lives += 1
                self.plus1herz_timer = 3
                trank.kill()
                self.trank_player = arcade.play_sound(self.trank_sound)
            
            hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.tränke_plus_zwei_herzen_spritelist)
            for trank in hit_list:
                self.lives += 2
                self.plus2herzen_timer = 3
                trank.kill()
                self.trank_player = arcade.play_sound(self.trank_sound)

        hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.schatz_liste)
        for schatz in hit_list:
            self.schätze += 1 # This should be outside the loop if only one treasure is picked up at a time
            schatz.kill()
            self.item_player = arcade.play_sound(self.item_sound)

        if arcade.check_for_collision_with_list(self.spielfigur, self.key_schatzraum):
            self.advancement_player = arcade.play_sound(self.advancement_sound)
#            for key in arcade.check_for_collision_with_list(self.spielfigur, self.key_schatzraum):
            self.key_schatzraum_have = True
            self.szene.get_sprite_list("Schlüssel Schatz-Raum").clear()
            self.achievement_timer_new = 2
            self.achievement_displayed = True
            self.achievement_new = "Key gefunden!"

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Activate Schatz-Raum")) and self.key_schatzraum_have == True:
#            for tor2 in arcade.check_for_collision_with_list(self.spielfigur, self.schatzraum_protector):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke")]
            self.szene.get_sprite_list("Activate Schatz-Raum").clear()
            self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke").clear()
            self.advancement_player = arcade.play_sound(self.advancement_sound)
            self.achievement_timer_new = 3
            self.achievement_displayed = True
            self.achievement_new = "Schatzraum geöffnet!"

        if arcade.check_for_collision_with_list(self.spielfigur, self.key_level_2):
#            for key in arcade.check_for_collision_with_list(self.spielfigur, self.key_level_2):
            self.key_level_2_have = True
            self.szene.get_sprite_list("Schlüssel 2").clear()
            self.advancement_player = arcade.play_sound(self.advancement_sound)
            self.achievement_timer_new = 2
            self.achievement_displayed = True
            self.achievement_new = "Key gefunden!"
            
        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Hebel Level 2")) and self.key_level_2_have == True:
#            for tor3 in arcade.check_for_collision_with_list(self.spielfigur, self.tor2):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke")]
            self.szene.get_sprite_list("Hebel Level 2").clear()
            self.szene.get_sprite_list("Tor 2").clear()
            self.advancement_player = arcade.play_sound(self.advancement_sound)
            self.level_3 = True
            self.achievement_timer_new = 4
            self.achievement_displayed = True
            self.achievement_new = "Level 3 geöffnet!"

        if self.tränke == True:
            hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.tränke_multi_jump_spritelist)
            for trank in hit_list:
                self.zeit_multi_jump = 5.5
                self.multi_jump = True
                self.physik_engine.enable_multi_jump(allowed_jumps=2)
                trank.kill()
                self.trank_player = arcade.play_sound(self.trank_sound)
            
            hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.tränke_jump_boost_spritelist)
            for trank in hit_list:
                self.zeit_jump_boost = 13
                self.höher_springen = True
                self.physik_engine.gravity_constant = 0.12
                trank.kill()
                self.trank_player = arcade.play_sound(self.trank_sound)

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Ziel")):
            if not self.gewonnen_sound_gespielt:
                self.advancement_player = arcade.play_sound(self.advancement_sound)
                self.gewonnen_sound_gespielt = True
            self.gewonnen = True

        if self.verloren == False:
            self.schaden_immun_timer -= delta_time 
            self.genutzte_zeit += delta_time
            # Use boolean logic (no bitwise &). verbleibende_zeit_start is a float timestamp here.
            if self.verbleibende_zeit_use and self.verbleibende_zeit_start:
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
            self.schlüssel_level1 = True
            self.advancement_player = arcade.play_sound(self.advancement_sound)
            self.szene.get_sprite_list("Schlüssel 1").clear()
            self.achievement_timer_new = 2
            self.achievement_displayed = True
            self.achievement_new = "Key gefunden!"

        hit_list = arcade.check_for_collision_with_list(self.spielfigur, self.münzen_spritelist)
        for münze in hit_list:
            self.münzen += 1 # This should be outside the loop if only one coin is picked up at a time
            münze.kill()
            self.coin_player = arcade.play_sound(self.coin_sound)
        
        if self.schaden_immun == False:
            if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Stachel")):
                self.damage_player = arcade.play_sound(self.damage_sound)
                self.lives -= 1
                self.schaden_immun = True
                self.schaden_immun_timer = 3
                self.schaden_immun_anzeigen = True
                
        if self.reset == True:
            # Alle eventuell laufenden Sounds stoppen
            if self.hintergrundmusik_sound:
                arcade.stop_sound(self.hintergrundmusik_sound)
            if self.epic_music_sound:
                arcade.stop_sound(self.epic_music_sound)
            if self.verloren_sound_player:
                arcade.stop_sound(self.verloren_sound_player)

            # Shutdown abspielen und neu initialisieren
            arcade.play_sound(self.audio_shutdown)
            self.reset_gameplay()
            return

        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("Reader 1")) and self.schlüssel_level1 == True:
#            for tor1 in arcade.check_for_collision_with_list(self.spielfigur, self.tor1):
            self.walls = [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Röhre"), self.szene.get_sprite_list("Unsichtbare Blöcke"), self.szene.get_sprite_list("Tor 2"), self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke")]
            self.szene.get_sprite_list("Reader 1").clear()
            self.szene.get_sprite_list("Tor 1").clear()
            self.advancement_player = arcade.play_sound(self.advancement_sound)
            self.achievement_timer_new = 4
            self.achievement_displayed = True
            self.achievement_new = "Level 2 freigeschaltet!"

        if self.lives == 0:
            self.verloren = True
            #self.__init__()

        if self.level_3:
            if self.level_3 and not self.level3_music_switched:
                # Hintergrundmusik stoppen
                if self.hintergrundmusik_sound and self.hintergrundmusik_sound.playing:
                    arcade.stop_sound(self.hintergrundmusik_sound)
                
                # Epische Musik starten (falls noch nicht)
                if not self.epic_music_sound or not self.epic_music_sound.playing:
                    self.epic_music_sound = arcade.play_sound(self.epic_music, loop=True)
                
                # Achievement-Sound einmal abspielen
                self.advancement_player = arcade.play_sound(self.advancement_sound)
                
                # Flag setzen, damit der Block nicht nochmal ausgeführt wird
                self.level3_music_switched = True


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

    def reset_gameplay(self):
        # 1. Preset-Einstellungen aus dem ersten Terminal-Setup wiederherstellen
        self.lives = self.initial_lives
        self.verbleibende_zeit = self.initial_verbleibende_zeit
        self.tränke = self.initial_tränke
        self.schaden_immun_timer = self.initial_schaden_immun_timer
        self.verbleibende_zeit_show = self.initial_verbleibende_zeit_show
        self.verbleibende_zeit_start = self.initial_verbleibende_zeit_start
        self.verbleibende_zeit_use = self.initial_verbleibende_zeit_use
        self.genutzte_zeit_show = self.initial_genutzte_zeit_show
        self.genutzte_zeit_use = self.initial_genutzte_zeit_use

        # 2. Spiel-Timer und Sammel-Werte komplett nullen
        self.plus1herz_timer = -1.0
        self.plus2herzen_timer = -1.0
        self.zeit_multi_jump = 0.0
        self.zeit_jump_boost = 0.0
        self.genutzte_zeit = 0.0
        self.münzen = 0
        self.schätze = 0

        # 3. Alle Status-Flags ausnahmslos in den Startzustand versetzen
        self.reset = False
        self.interact = True
        self.gewonnen = False
        self.verloren = False
        self.verloren_sound_gespielt = False
        self.gewonnen_sound_gespielt = False
        self.level3_music_switched = False
        self.erstes_update = True
        self.key_level_2_have = False
        self.key_schatzraum_have = False
        self.schlüssel_level1 = False
        self.level_1 = False
        self.level_2 = False
        self.level_3 = False
        self.multi_jump = False
        self.höher_springen = False
        self.jump_boost = False
        self.schaden_immun = False
        self.schaden_immun_anzeigen = False
        self.start_menu = True
        self.freeze_player = False
        self.springen_höhe = 0.65
        self.achievement_timer_new = 0.0
        self.achievement_displayed = False
        self.achievement_timer = 0.0
        self.achievement_new = None
        self.achievement_stack = None
        self.achievement_stack_timer = 0.0
        self.achievement = None
        self.achievement_timer_new = 0.0

        # 4. Aktive Sound-Kanäle und Player-Referenzen bereinigen
        self.shutdownsound = None
        self.errorsound = None
        self.verloren_sound_player = None
        self.hackedsound = None
        self.nebenrisiken_sound = None
        self.epic_music_sound = None
        self.advancement_player = None
        self.coin_player = None
        self.trank_player = None
        self.item_player = None
        self.damage_player = None

        # 5. Kamera-Position zurücksetzen (verhindert Bild-Sprünge beim Instaspawn)
        self.camera.position = (self.width / 2, self.height / 2)

        # 6. Die Map komplett neu von der Festplatte laden, damit alle gelöschten Objekte wieder da sind!
        self.tile_map = arcade.load_tilemap("Jump And Run.tmx", use_spatial_hash=True) # <-- DIESE ZEILE HIER ERGÄNZEN
        self.szene = arcade.Scene.from_tilemap(self.tile_map)

        # 7. Spielerfigur zurücksetzen und der neuen Szene hinzufügen
        self.spielfigur.center_x = 20
        self.spielfigur.center_y = 308
        self.spielfigur.change_x = 0
        self.spielfigur.change_y = 0
        self.spielerliste = arcade.SpriteList()
        self.spielerliste.append(self.spielfigur)
        self.szene.add_sprite("Spielfigur", self.spielfigur)

        # 8. ALLE Sprite-Listen-Referenzen (Mauern, Schlüssel, Tore) neu an die frische Map binden
        self.walls = [
            self.szene.get_sprite_list("Tile Layer 1"), 
            self.szene.get_sprite_list("Röhre"), 
            self.szene.get_sprite_list("Unsichtbare Blöcke"), 
            self.szene.get_sprite_list("Tor 1"), 
            self.szene.get_sprite_list("Tor 2"), 
            self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke")
        ]
        self.münzen_spritelist = self.szene.get_sprite_list("Münzen")
        self.tor1 = [self.szene.get_sprite_list("Tor 1"), self.szene.get_sprite_list("Reader 1")]
        self.tränke_multi_jump_spritelist = self.szene.get_sprite_list("Tränke Multi_Jump")
        self.tränke_plus_ein_herz_spritelist = self.szene.get_sprite_list("Tränke + 1 Herz")
        self.tränke_plus_zwei_herzen_spritelist = self.szene.get_sprite_list("Tränke + 2 Herzen")
        self.tränke_jump_boost_spritelist = self.szene.get_sprite_list("Tränke Jump_Boost")
        self.ladder_liste = self.szene.get_sprite_list("Wasser")
        self.key_schatzraum = self.szene.get_sprite_list("Schlüssel Schatz-Raum")
        self.key_level_2 = self.szene.get_sprite_list("Schlüssel 2")
        self.tor2 = [self.szene.get_sprite_list("Tor 2"), self.szene.get_sprite_list("Hebel Level 2")]
        self.schatzraum_protector = [self.szene.get_sprite_list("Schatz-Raum Verschließ-Blöcke"), self.szene.get_sprite_list("Activate Schatz-Raum")]
        self.schatz_liste = self.szene.get_sprite_list("Schatz-Kiste")

        # 9. Physik-Engine mit der komplett zurückgesetzten Wall-Liste neu initialisieren
        self.physik_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.spielfigur, platforms=self.walls, gravity_constant=0.1, ladders=self.ladder_liste
        )

        # 10. Normale Hintergrundmusik wieder von vorne starten
        self.hintergrundmusik_sound = arcade.play_sound(self.hintergrundmusik, loop=True)
        

    def on_draw(self):
        cam_x = self.camera.position[0]
        cam_y = self.camera.position[1]

        self.clear()
        self.camera.use()
        self.szene.draw()
        self.spielerliste.draw()

        arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", cam_x + 385, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(f"Leben: {round(self.lives, 1)}", cam_x - 307, cam_y + 270, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        arcade.draw_text(f"Schätze: {round(self.schätze, 1)}", cam_x - 282, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")

        if self.schaden_immun_anzeigen:
            arcade.draw_text(f"Du kriegst noch für: {round(self.schaden_immun_timer, 1)} keinen Schaden!", cam_x + 225, cam_y - 225, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.höher_springen:
            arcade.draw_text(f"Du hast noch für {round(self.zeit_jump_boost, 1)} Sekunden Jump Boost!", cam_x + 245, cam_y - 250, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.multi_jump:
            arcade.draw_text(f"Du hast noch für {round(self.zeit_multi_jump, 1)} Sekunden Multi Jump!", cam_x + 245, cam_y - 260, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.plus1herz:
            arcade.draw_text(f"+1 Herz", cam_x + 35, cam_y - 200, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.plus2herzen:
            arcade.draw_text(f"+2 Herzen", cam_x + 35, cam_y - 210, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.verbleibende_zeit_show:
            arcade.draw_text(f"Verbleibende Zeit: {round(self.verbleibende_zeit, 1)} Sekunden", cam_x + 385, cam_y + 265, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        if self.genutzte_zeit_show:
            arcade.draw_text(f"Genutzte Zeit: {round(self.genutzte_zeit, 1)} Sekunden", cam_x + 385, cam_y + 245, font_size=24, font_name="Kenney Pixel", anchor_x="right")
        # Achievement anzeigen (das Haupt-Achievement)
        if self.achievement_displayed and self.achievement is not None:
            # Zeichne das aktuell angezeigte Achievement
            arcade.draw_text(f"{self.achievement}", cam_x - 10, cam_y + 70, font_size=24, font_name="Kenney Pixel", anchor_x="center", anchor_y="center", color=arcade.color.AQUA) # Farbe optional

        # Achievement aus dem Stack anzeigen (z.B. darunter), wenn es existiert
        # Korrektur: Prüfe auf None, nicht auf True
        if self.achievement_stack is not None:
            # Zeige das Achievement im Stack leicht unterhalb des aktuellen an
            arcade.draw_text(f"{self.achievement_stack}", cam_x - 10, cam_y + 40, font_size=24, font_name="Kenney Pixel", anchor_x="center", anchor_y="center", color=arcade.color.AQUAMARINE) # Farbe optional


        if self.gewonnen:
            self.verbleibende_zeit_start = False
            self.interact = False
            if self.hintergrundmusik_sound and self.hintergrundmusik_sound.playing:
                arcade.stop_sound(self.hintergrundmusik_sound)
            arcade.draw_lrbt_rectangle_filled(cam_x - 400, cam_x + 400, cam_y - 300, cam_y + 300, arcade.color.GREEN)
            arcade.draw_text("GEWONNEN", cam_x, cam_y, arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
            arcade.draw_text("Klicke R um das Spiel erneut zu starten", cam_x - 125, cam_y - 70, arcade.color.WHITE)
            arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", cam_x + 385, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            arcade.draw_text(f"Leben: {round(self.lives, 1)}", cam_x - 307, cam_y + 270, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            arcade.draw_text(f"Schätze: {round(self.schätze, 1)}", cam_x - 282, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            if self.verbleibende_zeit_use == True:
                arcade.draw_text(f"Verbleibende Zeit: {round(self.verbleibende_zeit, 1)} Sekunden", cam_x + 385, cam_y + 265, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            if self.genutzte_zeit_use == True:
                self.genutzte_zeit_use = False  # Verhindert, dass die Zeit weiterläuft, nachdem das Spiel gewonnen wurde
            if self.genutzte_zeit_show == True:
                arcade.draw_text(f"Genutzte Zeit: {round(self.genutzte_zeit, 1)} Sekunden", cam_x + 385, cam_y + 245, font_size=24, font_name="Kenney Pixel", anchor_x="right")

        if self.verloren:
            self.interact = False
            self.verbleibende_zeit_start = False
            if self.hintergrundmusik_sound and self.hintergrundmusik_sound.playing:
                arcade.stop_sound(self.hintergrundmusik_sound)
            if self.epic_music_sound and self.epic_music_sound.playing:
                arcade.stop_sound(self.epic_music_sound)
            arcade.draw_lrbt_rectangle_filled(cam_x - 400, cam_x + 400, cam_y - 300, cam_y + 300, arcade.color.RED)
            arcade.draw_text("VERLOREN", cam_x, cam_y, arcade.color.WHITE, 50, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
            arcade.draw_text("Klicke R um das Spiel erneut zu starten", cam_x - 125, cam_y - 70, arcade.color.WHITE)
            arcade.draw_text(f"Münzen: {round(self.münzen, 1)}", cam_x + 385, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            arcade.draw_text(f"Leben: {round(self.lives, 1)}", cam_x - 307, cam_y + 270, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            arcade.draw_text(f"Schätze: {round(self.schätze, 1)}", cam_x - 282, cam_y - 285, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            if self.verbleibende_zeit_use == True:
                arcade.draw_text(f"Verbleibende Zeit: {round(self.verbleibende_zeit, 1)} Sekunden", cam_x + 385, cam_y + 265, font_size=24, font_name="Kenney Pixel", anchor_x="right")
            if self.genutzte_zeit_use == True:
                self.genutzte_zeit_use = False  # Verhindert, dass die Zeit weiterläuft, nachdem das Spiel verloren wurde
            if self.genutzte_zeit_show == True:
                arcade.draw_text(f"Genutzte Zeit: {round(self.genutzte_zeit, 1)} Sekunden", cam_x + 385, cam_y + 245, font_size=24, font_name="Kenney Pixel", anchor_x="right")

Plattformer()
arcade.run()