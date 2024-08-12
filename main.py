"""
Main.

Created by: Sam
Date: 17/06/2024
"""
import remi.gui as GUI
from remi import start, App
import time
import random
from typing import Any


# all text art from emojicombos.com
# all images from https://imgbin.com/
# creates all pokemon images name and everything
Pokemons: list[dict[Any, Any]] = [
    {
        "Name": ["Bulbasaur", "Ivysaur", "Venusaur"],
        "Picture": [
            GUI.Image("""/res:Bulbasaur.png"""),
            GUI.Image("""/res:Ivysaur.png"""),
            GUI.Image("""/res:Venusaur.png"""),
        ],
        "Order": 1,
        "Type": "Grass",
        "Time": 30,
        "Attack_Name": "Mud Splat",
        "Attack_Dmg": 25,
        "Attack_Eng": -40,
    },
    {
        "Name": ["Squirtle", "Wartortle", "Blastoise"],
        "Picture": [
            GUI.Image("""/res:Squirtle.png"""),
            GUI.Image("""/res:Wartortle.png"""),
            GUI.Image("""/res:Blastoise_4.png"""),
        ],
        "Order": 2,
        "Type": "Water",
        "Time": 25,
        "Attack_Name": "Splash",
        "Attack_Dmg": 30,
        "Attack_Eng": -35,
    },
    {
        "Name": ["Pichu", "Pikachu", "Raichu"],
        "Picture": [
            GUI.Image("""/res:Pichu.png"""),
            GUI.Image("""/res:Pikachu.png"""),
            GUI.Image("""/res:Raichu.png"""),
        ],
        "Order": 3,
        "Type": "Lightning",
        "Time": 20,
        "Attack_Name": "lightning Strike",
        "Attack_Dmg": 35,
        "Attack_Eng": -30,
    },
    {
        "Name": ["Charmander", "Charmeleon", "Charizard"],
        "Picture": [
            GUI.Image("""/res:Charmander.png"""),
            GUI.Image("""/res:Charmeleon.png"""),
            GUI.Image("""/res:Charizard.png"""),
        ],
        "Order": 4,
        "Type": "Fire",
        "Time": 15,
        "Attack_Name": "Fire Breath",
        "Attack_Dmg": 60,
        "Attack_Eng": -60,
    },
    {
        "Name": ["Gastly", "Haunter", "Gengar"],
        "Picture": [
            GUI.Image("""/res:Gastly.png"""),
            GUI.Image("""/res:Haunter.png"""),
            GUI.Image("""/res:Gengar.png"""),
        ],
        "Order": 5,
        "Type": "Poisen",
        "Time": 10,
        "Attack_Name": "Poison Spit",
        "Attack_Dmg": 48,
        "Attack_Eng": -30,
    },
]

# creates attacks for user that can be used instead of default ones
Attacks: dict[str, dict[str, int]] = {
    "Punch": {"Dmg": 20, "Eng": -5, "Order": 2},
    "Bite": {"Dmg": 35, "Eng": -15, "Order": 3},
    "Flying Kick": {"Dmg": 55, "Eng": -99, "Order": 4},
    "Skip": {"Dmg": 0, "Eng": 35, "Order": 5},
    }

# making questions
Questions = [
    [
        ["7 x 6", 42],
        ["6 x 8", 48],
        ["9 x 7", 63],
        [
            "4³",
            64,
            "since its ³ its times by itself 3x",
            "4³ = 4x4x4",
            "4x4 = 16",
            "16 x 4 = 64"
        ],
        ["√36", 6],
        ["9 x 9", 81],
        ["11 x 7", 77],
        ["26 - 8", 18],
        ["99 - 35", 64],
        ["18 / 6", 3],
        ["17 + 34", 51],
        ["48 ÷ 6", 8],
        ["72 - 29", 43],
        [
            "5²",
            25,
            "since its ² its times by itself",
            "5x5 = 25",
        ],
        ["√64", 8],
        ["98 ÷ 7", 14],
        ["63 - 28", 35],
        ["144 ÷ 12", 12],
        ["37 + 58", 95],
        ["291 - 141", 150],
        ["√81", 9],
        ["175 ÷ 25", 7],
        ["98 - 63", 35],
        ["12 + 25", 37],
        ["36 ÷ 6", 6],
        ["49 - 18", 31],
        [
            "4²",
            16,
            "since its ² its times by itself",
            "4x4 = 16",
        ],
        ["√49", 7],
        ["9 x 8", 72],
        ["72 ÷ 9", 8],
        ["25 - 12", 13],
        ["6 x 9", 54],
        ["50 ÷ 10", 5],
    ],
    [
        ["150 x 7", 1050],
        ["√144", 12],
        [
            "4(3³ - 2)",
            100,
            "brackets fist so",
            "3³ = 3x3x3, since its ³ its x by itself 3x",
            "3x3 = 9",
            "9x3 = 27",
            "then (27 - 2) = 25",
            "then x that by the 4 from outside the brackets to get 100",
        ],
        [
            "5⁸ / 5⁵",
            125,
            "minus the powers",
            "8-5 = 3",
            "then you are left with 5³",
            "since its ³ its x by itself 3x",
            "5³ = 5x5x5",
            "5x5 = 25",
            "25x5 = 125",
        ],
        ["150 / 6", 25],
        [
            "√121 + 5",
            16,
            "√121 = 11",
            "11+5 = 16",
        ],
        ["1243 - 154", 1089],
        [
            "99 / 3 + 17",
            50,
            "99 / 3 = 33",
            "33 + 17 = 50",
        ],
        ["1947 + 1231", 3178],
        ["84 / 4", 21],
        ["240 ÷ 16", 15],
        ["16 x 7", 112],
        ["13 x 18", 234],
        ["126 ÷ 3", 42],
        ["23 x 19", 437],
        [
            "7³",
            343,
            "7x7 = 49",
            "49 x 7 = 343",
            "or you can do",
            "50 x 7 = 350",
            "350 - 7 = 343",
            "the minus 7 is from us timeing by 50 7x instead of 49"
        ],
        ["√169", 13],
        [
            "5⁴ - 3",
            747,
            "5⁴ = 5x5x5x5, since ⁴ it times by itself 4x",
            "5x5 = 25",
            "25x5 = 125",
            "125 x 5 = 750",
            "5⁴ = 750",
            "750 - 3 = 747"
        ],
        [
            "6⁶ / 6³",
            216,
            "minus the powers",
            "7 - 3 = 4",
            "now we are left with 6³",
            "6³ = 6x6x6, since ³ it times by itself 3x",
            "6x6 = 36,",
            "36 x 6 = 216",
        ],
        ["180 / 9", 20],
        [
            "√144 + 10",
            22,
            "√144 = 12",
            "12 + 10 = 22",
        ],
        ["1245 - 143", 1102],
        [
            "110 / 2 + 34",
            89,
            "110 / 2 = 55."
            "55 +34 = 89",
        ],
        ["2020 + 1425", 3445],
        ["88 / 4", 22],
        [
            "4³ + 5²",
            89,
            "4³ = 4x4x4 since its ³ its times by itself 3x,",
            "4x4 = 16",
            "16 x 4 = 64", 
            "4³ = 64",
            "5² = 5x5 since its ² its times by itself",
            "5x5 = 25",
            "5² = 25",
            "64 + 25 = 89",
        ],
        [
            "6⁴ / 6²",
            36,
            "minus the powers,"
            "4-2 = 2"
            "then you are left with 6²,"
            "since its ² its x by itself 2x,"
            "6² = 6x6"
            "6x6 = 36",
        ],
        [
            "√121 + 8",
            19,
            "√121 = 11",
            "11+8 = 19",
        ],
        ["899 - 123", 776],
        [
            "66 / 2 + 14",
            47,
            "66 / 2 = 33",
            "33 + 14 = 47",
        ],
        ["1350 + 430", 1780],
        ["64 / 8", 8],
    ],
    [
        [
            "where x = 2, (x + 5)²",
            49,
            "(x + 5)² = (2 + 5)²",
            "2 + 5 = 7",
            "(7)² = 49"
,
        ],
        [
            "where x = 4 and y = 3, 2/x + 6/y",
            2.5,
            "2/x + 6/y = 2/4 + 6/3",
            "2/4 = 0.5",
            "6/3 = 2",
            "0.5 + 2 = 2.5"
,
        ],
        [
            "where x = 12, (x/6)⁻¹",
            0.5,
            "(x/6)⁻¹ = (12/6)⁻¹",
            "(12/6)⁻¹ = 6/12",
            "6/12 = 0.5"
        ],
        [
            "where x = 3, (√121)(x² - 2)",
            77,
            "(√121)(x² - 2) = (√121)(3² - 2)",
            "first bracket",
            "(√121) = 11",
            "second bracket",
            "3² = 3x3 since it's ² it's times by itself,",
            "3x3 = 9",
            "9 - 2 = 7",
            "11 x 7 = 77"
        ],
        [
            "where x = 6 and y = 1, 3y(x² - 5²)",
            122,
            "2y(x² - 5²) = 2(1)(6² - 5²)",
            "first bracket",
            "1x2 = 2",
            "second bracket",
            "6² = 6x6 since it's ² it's times by itself,",
            "6x6 = 36",
            "5² = 5x5 since it's ² it's times by itself,",
            "5x5 = 25",
            "36 - 25 = 11",
            "multiply first bracket by second bracket",
            "2x11 = 22"
        ],
        [
            "where x = 5, 4x(3/9)⁻¹",
            60,
            "4x(3/9)⁻¹ = 4(5)(3/9)⁻¹",
            "first bracket",
            "4x5 = 20",
            "second bracket",
            "(3/9)⁻¹ = 9/3",
            "9/3 = 3",
            "multiply together",
            "20 x 3 = 60"
        ],
        [
            "where x = 2.5, 3x(21/7)",
            22.5,
            "3x(21/7) = 3(2.5)(21/7)",
            "first bracket",
            "3x2.5 = 7.5",
            "second bracket",
            "21/7 = 3",
            "multiply together",
            "7.5 x 3 = 22.5"
        ],
        [
            "where x = 2 and y = 2.5, x(2x + 3y)",
            23,
            "x(2x + 3y) = 2(2)(2(2) + 3(2.5))",
            "first bracket",
            "2(2) = 4",
            "second main bracket",
            "2(2) = 4",
            "3(2.5) = 7.5",
            "4 + 7.5 = 11.5",
            "multiply brackets together",
            "11.5 x 2 = 23"
        ],
        ["156 / 5", 31.2],
        ["3.45 x 8", 27.6],
        [
            "where x = 9 and y = 2, 5x/y + 3",
            22.5,
            "5x/y + 3 = 5(9)/2",
            "5(9) = 45",
            "45/2 = 22.5"
        ],
        [
            "where x = 4, (√144)(x² - 3)",
            156,
            "(√144)(x² - 3) = (√144)(4² - 3)",
            "first bracket",
            "√144 = 12",
            "second bracket",
            "4² = 4x4 since it's ² it's times by itself,",
            "4x4 = 16",
            "16 - 3 = 13",
            "multiply brackets together",
            "12 x 13 = 156"
        ],
        [
            "where x = 8 and y = 4, 2y(x² - 7²)",
            120,
            "2y(x² - 7²) = 2(4)((8)² - 7²)",
            "first bracket",
            "2(4) = 8",
            "second main bracket",
            "(8)² = 8x8 since it's ² it's times by itself,",
            "8x8 = 64",
            "(7)² = 7x7 since it's ² it's times by itself,",
            "7x7 = 49",
            "64-49 = 15",
            "multiply brackets together",
            "8x15 = 120"
        ],
        [
            "where x = 6, 5x(2/3)⁻¹",
            45,
            "5(2/3)⁻¹ = 5(6)(2/3)⁻¹"
            "first brackert",
             "5(6) = 30",
             "second bracket",
             "(2/3)⁻¹ = 3/2",
             "3/2 = 1.5",
             "multiply brackets together",
             "30 x 1.5 = 45"
        ],
        [
            "where x = 3.5, 4x(18/6)",
            42,
            "4x(18/6) = 4(3.5)(18/6)",
            "first bracket",
            "4(3.5) = 14",
             "second bracket",
            "18/6 = 3",
             "multiply brackets together",
             "14 x 3 = 42"
        ],
        [
            "where x = 3 and y = 2, x(3x + 2y)",
            13.5,
            "x(3x + 2y) = 2(3(1.5) + 2(2))",
            "3(1.5) = 4.5",
            "2(2) = 4",
            "4+4.5 = 8.5",
            "2x8.5 = 17",
        ],
        ["7.8 x 6", 46.8],
        ["2.5 x 10.4", 26],
        ["4.6 x 5.5", 25.3],
        ["11.2 x 2.5", 28],
    ],
]       
# starting app up
class MyAmazingApp(App):
    """A class for the entire app."""

    def __init__(self, *args):
        """Allows game to run."""
        import os

        abs_path: str = os.path.abspath(__file__)
        dir_name: str = os.path.dirname(abs_path)
        res_path: str = os.path.join(dir_name, "res")
        super().__init__(*args, static_file_path={"res": res_path})

    def main(self):
        # setting up modes
        self.ask_user_mode = GUI.Label("Would you like to play on")
        self.easy_but = GUI.Button("Easy")
        self.order = -1
        self.med_but = GUI.Button("Medium")
        self.hard_but = GUI.Button("Hard")
        # giving player health and energy
        self.Player_stats: dict[str, int] = {"Energy": 200, "Health": 200}
        self.mode = 5
        self.easy_but.onclick.do(self.easy_button)
        self.med_but.onclick.do(self.med_button)
        self.hard_but.onclick.do(self.hard_button)
        self.button_box = GUI.HBox([self.easy_but, self.med_but, self.hard_but])
        self.mode_box = GUI.HBox([self.ask_user_mode, self.button_box])
        return(self.mode_box)
    
    def easy_button(self, easy_but: GUI.Button):
        # putting in mode
        self.mode = 0
        self.sel_poke()

    def med_button(self, med_but: GUI.Button):
        # putting in mode
        self.mode = 1
        self.sel_poke()

    def hard_button(self, hard_but: GUI.Button):
        # putting in mode
        self.mode = 2
        self.sel_poke()

    def sel_poke(self):
        self.mode_box.empty()
        self.Pokemons_prop = GUI.HBox()
        # selecting spefic pokemon
        for i in range (5):
            # adding all pokemon in
            self.Poke_butt = GUI.Button(Pokemons[i]["Name"][self.mode])
            self.Pokemons_box = GUI.VBox([Pokemons[i]["Picture"][self.mode], self.Poke_butt, ])
            self.Pokemons_Vbox = GUI.VBox([self.Pokemons_box, self.Poke_butt])
            self.Pokemons_prop.append([self.Pokemons_box])
            self.Poke_butt.onclick.do(self.poke_selected)
            self.Poke_butt.onclick.do(lambda _, i=i: self.poke_selected(i))  
        self.mode_box.append([self.Pokemons_prop])

    def poke_selected(self, Poke_butt: GUI.Button):
        # gets what poekmon is chosen
        self.chosen_pokemon = Poke_butt
        self.set_fighting()
        
    def set_fighting(self):
        self.questions()
        self.mode_box.empty()
        # creating enimie counter
        self.order = self.order + 1
        # resetting pokemon stats
        self.Pokemon_stats: dict[str, int] = {"Energy": 100, "Health": 100}
        # sends user to win screen if won
        if self.order == 5:
            self.win()
        else:
            # puts new pokemon in if user beat the previous one
            self.user_attack = True
            self.fighting()

    def fighting(self):
        # adding if statements to ensure they cant attack if they dont have energy
        if self.Player_stats["Health"] > 0:
            if self.Pokemon_stats["Health"] > 0:
                if self.Player_stats["Energy"] > 0:
                    self.mode_box.empty()
                    # setting up enimes
                    comp_pokemon = GUI.Label(Pokemons[self.order]["Name"][self.mode])
                    comp_pic = GUI.HBox(Pokemons[self.order]["Picture"][self.mode])
                    comp_health = GUI.Label("Health:{}".format(self.Pokemon_stats["Health"]))
                    comp_eng = GUI.Label("Energy:{}".format(self.Pokemon_stats["Energy"]))
                    self.comp_poke = GUI.VBox([comp_pokemon, comp_pic, comp_health, comp_eng])

                    # setting up users pokemon
                    user_pokemon = GUI.Label(Pokemons[self.chosen_pokemon]["Name"][self.mode])
                    user_pic = GUI.HBox(Pokemons[self.chosen_pokemon]["Picture"][self.mode])
                    user_health = GUI.Label("Health:{}".format(self.Player_stats["Health"]))
                    user_eng = GUI.Label("Energy:{}".format(self.Player_stats["Energy"]))
                    self.user_poke = GUI.VBox([user_pokemon, user_pic, user_health, user_eng])

                    # setting up users attacks
                    if self.user_attack == True:
                        self.user_attack = False
                        self.attacks = GUI.Label(f"{Pokemons[self.chosen_pokemon]["Attack_Dmg"]} damage, {Pokemons[self.chosen_pokemon]["Attack_Eng"]} energy!")
                        self.attack_buts = GUI.Button(Pokemons[self.chosen_pokemon]["Attack_Name"])
                        neg_eng = self.Player_stats["Energy"] + Pokemons[self.chosen_pokemon]["Attack_Eng"]
                        if neg_eng < 0:
                            self.attack_buts.set_enabled(False)
                        # adding specail attack in
                        self.attack_boxs = GUI.HBox([self.attack_buts, self.attacks])
                        self.attack_choice = GUI.VBox(self.attack_boxs)
                        self.attack_buts.onclick.do(self.spec_attack)
                        # adding defult attacks in
                        for name in Attacks.keys():
                            self.attack = GUI.Label(f"{Attacks[name]["Dmg"]} damage, {Attacks[name]["Eng"]} energy!")
                            self.attack_but = GUI.Button(name)
                            neg_eng = self.Player_stats["Energy"] + Attacks[name]["Eng"]
                            if neg_eng < 0:
                                self.attack_but.set_enabled(False)
                            self.attack_box = GUI.HBox([self.attack_but, self.attack])
                            self.attack_choice.append(self.attack_box)
                            self.attack_but.onclick.do(self.attacking)
                            self.attack_but.onclick.do(lambda _, i=Attacks[name]["Order"]: self.attacking(i))
                        user = GUI.HBox([self.user_poke, self.attack_choice])
                        Fight = GUI.VBox([self.comp_poke, user])
                        self.mode_box.append([Fight])
                    else:
                        self.comp_attack()
                else:
                    # if player runs out of energy they have to gain some
                    self.Player_stats["Energy"] = self.Player_stats["Energy"] + 35
                    self.user_attack = True
                    self.fighting()
            else:
                self.set_fighting()
        else:
            self.lose()
        
    def comp_attack(self):
        self.user_attack = True
        neg_eng = self.Pokemon_stats["Energy"] + Pokemons[self.order]["Attack_Eng"]
        print(neg_eng)
        if neg_eng > 0:
            self.Player_stats["Health"] = self.Player_stats["Health"] - Pokemons[self.order]["Attack_Dmg"]
            self.Pokemon_stats["Energy"] = self.Pokemon_stats["Energy"] + Pokemons[self.order]["Attack_Eng"]
        else:
            self.Pokemon_stats["Energy"] = self.Pokemon_stats["Energy"] + 35

        self.fighting()

    def questions(self):
        question_num = 3
        
        for question in Questions[self.mode]:
            print(question)

        
    def attacking(self, attack_but: GUI.Button):
        self.ordering = attack_but
        for at in Attacks.keys():
            if Attacks[at]["Order"] == self.ordering:
                # finding specfic attack and taking away adamge and health
                self.Pokemon_stats["Health"] = self.Pokemon_stats["Health"] - Attacks[at]["Dmg"]
                self.Player_stats["Energy"] = self.Player_stats["Energy"] + Attacks[at]["Eng"]
                self.fighting()
    


    def spec_attack(self, attack_buts: GUI.Button):
        # finding specail attack and using it
        self.Pokemon_stats["Health"] = self.Pokemon_stats["Health"] - Pokemons[self.chosen_pokemon]["Attack_Dmg"]
        self.Player_stats["Energy"] = self.Player_stats["Energy"] + Pokemons[self.chosen_pokemon]["Attack_Eng"]
        self.fighting()

    def win(self):
        # tells user they won
        self.mode_box.empty()
        win = GUI.Label("CONGRATS U WON!!!")
        self.mode_box.append([win])
    
    def lose(self):
        # tells user they lost
        self.mode_box.empty()
        win = GUI.Label("CONGRATS U LOST!!!")
        self.mode_box.append([win])

start(MyAmazingApp)