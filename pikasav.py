# -*- coding: utf-8 -*-
'''
Created on 07/04/2011

@author: Ritchie
'''
from Tkinter import *
from Tix import *
from tkFileDialog import *
from tkMessageBox import *
from rbsav import RBSav
from gssav import GSSav
from crsav import CRSav
from rssav import RSSav
import os

items_rb = ["~0", "Master Ball (1)", "Ultra Ball (2)", "Great Ball (3)", "Poke Ball (4)", "Town Map (5)", "Bicycle (6)", "????? (7)", "Safari Ball (8)", "Pokedex (9)", "Moon Stone (10)", "Antidote (11)", "Burn Heal (12)", "Ice Heal (13)", "Awakening (14)", "Parlyz Heal (15)", "Full Restore (16)", "Max Potion (17)", "Hyper Potion (18)", "Super Potion (19)", "Potion (20)", "Boulderbadge (21)", "Cascadebadge (22)", "Thunderbadge (23)", "Rainbowbadge (24)", "Soulbadge (25)", "Marshbadge (26)", "Volcanobadge (27)", "Earthbadge (28)", "Escape Rope (29)", "Repel (30)", "Old Amber (31)", "Fire Stone (32)", "Thunderstone (33)", "Water Stone (34)", "HP Up (35)", "Protein (36)", "Iron (37)", "Carbos (38)", "Calcium (39)", "Rare Candy (40)", "Dome Fossil (41)", "Helix Fossil (42)", "Secret Key (43)", "????? (44)", "Bike Voucher (45)", "X Accuracy (46)", "Leaf Stone (47)", "Card Key (48)", "Nugget (49)", "PP Up (50)", "Poke Doll (51)", "Full Heal (52)", "Revive (53)", "Max Revive (54)", "Guard Spec (55)", "Super Repel (56)", "Max Repel (57)", "Dire Hit (58)", "Coin (59)", "Fresh Water (60)", "Soda Pop (61)", "Lemonade (62)", "S.S.Ticket (63)", "Gold Teeth (64)", "X Attack (65)", "X Defend (66)", "X Speed (67)", "X Special (68)", "Coin Case (69)", "Oak Parcel (70)", "Itemfinder (71)", "Silph Scope (72)", "Poke Flute (73)", "Lift Key (74)", "Exp.All (75)", "Old Rod (76)", "Good Rod (77)", "Super Rod (78)", "Pp Up (79)", "Ether (80)", "Max Ether (81)", "Elixer (82)", "Max Elixer (83)", "~84", "~85", "~86", "~87", "~88", "~89", "~90", "~91", "~92", "~93", "~94", "~95", "~96", "~97", "~98", "~99", "~100", "~101", "~102", "~103", "~104", "~105", "~106", "~107", "~108", "~109", "~110", "~111", "~112", "~113", "~163", "~115", "~116", "~117", "~118", "~119", "~120", "~121", "~122", "~123", "~124", "~125", "~126", "~127", "~128", "~129", "~130", "~131", "~132", "~133", "~134", "~135", "~136", "~137", "~138", "~139", "~140", "~141", "~142", "~143", "~144", "~145", "~146", "~147", "~148", "~149", "~150", "~151", "~152", "~153", "~154", "~155", "~156", "~163", "~158", "~159", "~160", "~161", "~162", "~163", "~164", "~165", "~166", "~167", "~168", "~169", "~170", "~171", "~172", "~173", "~174", "~175", "~176", "~177", "~178", "~179", "~180", "~181", "~182", "~183", "~184", "~185", "~186", "~187", "~188", "~189", "~190", "~191", "~192", "~193", "~194", "~195", "HM01 (196)", "HM02 (197)", "HM03 (198)", "HM04 (199)", "HM05 (200)", "TM01 (201)", "TM02 (202)", "TM03 (203)", "TM04 (204)", "TM05 (205)", "TM06 (206)", "TM07 (207)", "TM08 (208)", "TM09 (209)", "TM10 (210)", "TM11 (211)", "TM12 (212)", "TM13 (213)", "TM14 (214)", "TM15 (215)", "TM16 (216)", "TM17 (217)", "TM18 (218)", "TM19 (219)", "TM20 (220)", "TM21 (221)", "TM22 (222)", "TM23 (223)", "TM24 (224)", "TM25 (225)", "TM26 (226)", "TM27 (227)", "TM28 (228)", "TM29 (229)", "TM30 (230)", "TM31 (231)", "TM32 (232)", "TM33 (233)", "TM34 (234)", "TM35 (235)", "TM36 (236)", "TM37 (237)", "TM38 (238)", "TM39 (239)", "TM40 (240)", "TM41 (241)", "TM42 (242)", "TM43 (243)", "TM44 (244)", "TM45 (245)", "TM46 (246)", "TM47 (247)", "TM48 (248)", "TM49 (249)", "TM50 (250)", "TM51 (251)", "TM52 (252)", "TM53 (253)", "TM54 (254)", "-- Cancel -- (255)"]
pokemon_rb = [" (0)", "Rhydon (1)", "Kangaskhan (2)", "Nidoranm (3)", "Clefairy (4)", "Spearow (5)", "Voltorb (6)", "Nidoking (7)", "Slowbro (8)", "Ivysaur (9)", "Exeggutor (10)", "Lickitung (11)", "Exeggcute (12)", "Grimer (13)", "Gengar (14)", "Nidoranh (15)", "Nidoqueen (16)", "Cubone (17)", "Rhyhorn (18)", "Lapras (19)", "Arcanine (20)", "Mew (21)", "Gyarados (22)", "Shellder (23)", "Tentacool (24)", "Gastly (25)", "Scyther (26)", "Staryu (27)", "Blastoise (28)", "Pinsir (29)", "Tangela (30)", "Missingno (31)", "Missingno (32)", "Growlithe (33)", "Onix (34)", "Fearow (35)", "Pidgey (36)", "Slowpoke (37)", "Kadabra (38)", "Graveler (39)", "Chansey (40)", "Machoke (41)", "Mr.Mime (42)", "Hitmonlee (43)", "Hitmonchan (44)", "Arbok (45)", "Parasect (46)", "Psyduck (47)", "Drowzee (48)", "Golem (49)", "Missingno (50)", "Magmar (51)", "Missingno (52)", "Electabuzz (53)", "Magneton (54)", "Koffing (55)", "Missingno (56)", "Mankey (57)", "Seel (58)", "Diglett (59)", "Tauros (60)", "Missingno (61)", "Missingno (62)", "Missingno (63)", "Farfetch'd (64)", "Venonat (65)", "Dragonite (66)", "Missingno (67)", "Missingno (68)", "Missingno (69)", "Doduo (70)", "Poliwag (71)", "Jynx (72)", "Moltres (73)", "Articuno (74)", "Zapdos (75)", "Ditto (76)", "Meowth (77)", "Krabby (78)", "Missingno (79)", "Missingno (80)", "Missingno (81)", "Vulpix (82)", "Ninetales (83)", "Pikachu (84)", "Raichu (85)", "Missingno (86)", "Missingno (87)", "Dratini (88)", "Dragonair (89)", "Kabuto (90)", "Kabutops (91)", "Horsea (92)", "Seadra (93)", "Missingno (94)", "Missingno (95)", "Sandshrew (96)", "Sandslash (97)", "Omanyte (98)", "Omastar (99)", "Jigglypuff (100)", "Wigglytuff (101)", "Eevee (102)", "Flareon (103)", "Jolteon (104)", "Vaporeon (105)", "Machop (106)", "Zubat (107)", "Ekans (108)", "Paras (109)", "Poliwhirl (110)", "Poliwrath (111)", "Weedle (112)", "Kakuna (113)", "Beedrill (163)", "Missingno (115)", "Dodrio (116)", "Primeape (117)", "Dugtrio (118)", "Venomoth (119)", "Dewgong (120)", "Missingno (121)", "Missingno (122)", "Caterpie (123)", "Metapod (124)", "Butterfree (125)", "Machamp (126)", "Missingno (127)", "Golduck (128)", "Hypno (129)", "Golbat (130)", "Mewtwo (131)", "Snorlax (132)", "Magikarp (133)", "Missingno (134)", "Missingno (135)", "Muk (136)", "Missingno (137)", "Kingler (138)", "Cloyster (139)", "Missingno (140)", "Electrode (141)", "Clefable (142)", "Weezing (143)", "Persian (144)", "Marowak (145)", "Missingno (146)", "Haunter (147)", "Abra (148)", "Alakazam (149)", "Pidgeotto (150)", "Pidgeot (151)", "Starmie (152)", "Bulbasaur (153)", "Venusaur (154)", "Tentacruel (155)", "Missingno (156)", "Goldeen (163)", "Seaking (158)", "Missingno (159)", "Missingno (160)", "Missingno (161)", "Missingno (162)", "Ponyta (163)", "Rapidash (164)", "Rattata (165)", "Raticate (166)", "Nidorino (167)", "Nidorina (168)", "Geodude (169)", "Porygon (170)", "Aerodactyl (171)", "Missingno (172)", "Magnemite (173)", "Missingno (174)", "Missingno (175)", "Charmander (176)", "Squirtle (177)", "Charmeleon (178)", "Wartortle (179)", "Charizard (180)", "Missingno (181)", "Missingno (182)", "Missingno (183)", "Missingno (184)", "Oddish (185)", "Gloom (186)", "Vileplume (187)", "Bellsprout (188)", "Weepinbell (189)", "Victreebel (190)", "~191", "~192", "~193", "~194", "~195", "~196", "~197", "~198", "~199", "~200", "~201", "~202", "~203", "~204", "~205", "~206", "~207", "~208", "~209", "~210", "~211", "~212", "~213", "~214", "~215", "~216", "~217", "~218", "~219", "~220", "~221", "~222", "~223", "~224", "~225", "~226", "~227", "~228", "~229", "~230", "~231", "~232", "~233", "~234", "~235", "~236", "~237", "~238", "~239", "~240", "~241", "~242", "~243", "~244", "~245", "~246", "~247", "~248", "~249", "~250", "~251", "~252", "~253", "~254", "-- No Pokemon -- (255)"]
pokedex_rb = ["#000 Missingno", "#001 Bulbasaur", "#002 Ivysaur", "#003 Venusaur", "#004 Charmander", "#005 Charmeleon", "#006 Charizard", "#007 Squirtle", "#008 Wartortle", "#009 Blastoise", "#010 Caterpie", "#011 Metapod", "#012 Butterfree", "#013 Weedle", "#014 Kakuna", "#015 Beedrill", "#016 Pidgey", "#017 Pidgeotto", "#018 Pidgeot", "#019 Rattata", "#020 Raticate", "#021 Spearow", "#022 Fearow", "#023 Ekans", "#024 Arbok", "#025 Pikachu", "#026 Raichu", "#027 Sandshrew", "#028 Sandslash", "#029 Nidoranh", "#030 Nidorina", "#031 Nidoqueen", "#032 Nidoranm", "#033 Nidorino", "#034 Nidoking", "#035 Clefairy", "#036 Clefable", "#037 Vulpix", "#038 Ninetales", "#039 Jigglypuff", "#040 Wigglytuff", "#041 Zubat", "#042 Golbat", "#043 Oddish", "#044 Gloom", "#045 Vileplume", "#046 Paras", "#047 Parasect", "#048 Venonat", "#049 Venomoth", "#050 Diglett", "#051 Dugtrio", "#052 Meowth", "#053 Persian", "#054 Psyduck", "#055 Golduck", "#056 Mankey", "#057 Primeape", "#058 Growlithe", "#059 Arcanine", "#060 Poliwag", "#061 Poliwhirl", "#062 Poliwrath", "#063 Abra", "#064 Kadabra", "#065 Alakazam", "#066 Machop", "#067 Machoke", "#068 Machamp", "#069 Bellsprout", "#070 Weepinbell", "#071 Victreebel", "#072 Tentacool", "#073 Tentacruel", "#074 Geodude", "#075 Graveler", "#076 Golem", "#077 Ponyta", "#078 Rapidash", "#079 Slowpoke", "#080 Slowbro", "#081 Magnemite", "#082 Magneton", "#083 Farfetch'd", "#084 Doduo", "#085 Dodrio", "#086 Seel", "#087 Dewgong", "#088 Grimer", "#089 Muk", "#090 Shellder", "#091 Cloyster", "#092 Gastly", "#093 Haunter", "#094 Gengar", "#095 Onix", "#096 Drowzee", "#097 Hypno", "#098 Krabby", "#099 Kingler", "#100 Voltorb", "#101 Electrode", "#102 Exeggcute", "#103 Exeggutor", "#104 Cubone", "#105 Marowak", "#106 Hitmonlee", "#107 Hitmonchan", "#108 Lickitung", "#109 Koffing", "#110 Weezing", "#111 Rhyhorn", "#112 Rhydon", "#113 Chansey", "#163 Tangela", "#115 Kangaskhan", "#116 Horsea", "#117 Seadra", "#118 Goldeen", "#119 Seaking", "#120 Staryu", "#121 Starmie", "#122 Mr.Mime", "#123 Scyther", "#124 Jynx", "#125 Electabuzz", "#126 Magmar", "#127 Pinsir", "#128 Tauros", "#129 Magikarp", "#130 Gyarados", "#131 Lapras", "#132 Ditto", "#133 Eevee", "#134 Vaporeon", "#135 Jolteon", "#136 Flareon", "#137 Porygon", "#138 Omanyte", "#139 Omastar", "#140 Kabuto", "#141 Kabutops", "#142 Aerodactyl", "#143 Snorlax", "#144 Articuno", "#145 Zapdos", "#146 Moltres", "#147 Dratini", "#148 Dragonair", "#149 Dragonite", "#150 Mewtwo", "#151 Mew", "#152", "#153", "#154", "#155", "#156", "#163", "#158", "#159", "#160", "#161", "#162", "#163", "#164", "#165", "#166", "#167", "#168", "#169", "#170", "#171", "#172", "#173", "#174", "#175", "#176", "#177", "#178", "#179", "#180", "#181", "#182", "#183", "#184", "#185", "#186", "#187", "#188", "#189", "#190", "#191", "#192", "#193", "#194", "#195", "#196", "#197", "#198", "#199", "#200", "#201", "#202", "#203", "#204", "#205", "#206", "#207", "#208", "#209", "#210", "#211", "#212", "#213", "#214", "#215", "#216", "#217", "#218", "#219", "#220", "#221", "#222", "#223", "#224", "#225", "#226", "#227", "#228", "#229", "#230", "#231", "#232", "#233", "#234", "#235", "#236", "#237", "#238", "#239", "#240", "#241", "#242", "#243", "#244", "#245", "#246", "#247", "#248", "#249", "#250", "#251", "#252", "#253", "#254", "#255"]
moves_rb = ["-- No Move -- (0)", "Pound (1)", "Karate Chop (2)", "Doubleslap (3)", "Comet Punch (4)", "Mega Punch (5)", "Pay Day (6)", "Fire Punch (7)", "Ice Punch (8)", "Thunderpunch (9)", "Scratch (10)", "Vicegrip (11)", "Guillotine (12)", "Razor Wind (13)", "Swords Dance (14)", "Cut (15)", "Gust (16)", "Wing Attack (17)", "Whirlwind (18)", "Fly (19)", "Bind (20)", "Slam (21)", "Vine Whip (22)", "Stomp (23)", "Double Kick (24)", "Mega Kick (25)", "Jump Kick (26)", "Rolling Kick (27)", "Sand-attack (28)", "Headbutt (29)", "Horn Attack (30)", "Fury Attack (31)", "Horn Drill (32)", "Tackle (33)", "Body Slam (34)", "Wrap (35)", "Take Down (36)", "Thrash (37)", "Double-edge (38)", "Tail Whip (39)", "Poison Sting (40)", "Twineedle (41)", "Pin Missile (42)", "Leer (43)", "Bite (44)", "Growl (45)", "Roar (46)", "Sing (47)", "Supersonic (48)", "Sonicboom (49)", "Disable (50)", "Acid (51)", "Ember (52)", "Flamethrower (53)", "Mist (54)", "Water Gun (55)", "Hydro Pump (56)", "Surf (57)", "Ice Beam (58)", "Blizzard (59)", "Psybeam (60)", "Bubblebeam (61)", "Aurora Beam (62)", "Hyper Beam (63)", "Peck (64)", "Drill Peck (65)", "Submission (66)", "Low Kick (67)", "Counter (68)", "Seismic Toss (69)", "Strength (70)", "Absorb (71)", "Mega Drain (72)", "Leech Seed (73)", "Growth (74)", "Razor Leaf (75)", "Solarbeam (76)", "Poisonpowder (77)", "Stun Spore (78)", "Sleep Powder (79)", "Petal Dance (80)", "String Shot (81)", "Dragon Rage (82)", "Fire Spin (83)", "Thundershock (84)", "Thunderbolt (85)", "Thunder Wave (86)", "Thunder (87)", "Rock Throw (88)", "Earthquake (89)", "Fissure (90)", "Dig (91)", "Toxic (92)", "Confusion (93)", "Psychic (94)", "Hypnosis (95)", "Meditate (96)", "Agility (97)", "Quick Attack (98)", "Rage (99)", "Teleport (100)", "Night Shade (101)", "Mimic (102)", "Screech (103)", "Double Team (104)", "Recover (105)", "Harden (106)", "Minimize (107)", "Smokescreen (108)", "Confuse Ray (109)", "Withdraw (110)", "Defense Curl (111)", "Barrier (112)", "Light Screen (113)", "Haze (163)", "Reflect (115)", "Focus Energy (116)", "Bide (117)", "Metronome (118)", "Mirror Move (119)", "Selfdestruct (120)", "Egg Bomb (121)", "Lick (122)", "Smog (123)", "Sludge (124)", "Bone Club (125)", "Fire Blast (126)", "Waterfall (127)", "Clamp (128)", "Swift (129)", "Skull Bash (130)", "Spike Cannon (131)", "Constrict (132)", "Amnesia (133)", "Kinesis (134)", "Softboiled (135)", "Hi Jump Kick (136)", "Glare (137)", "Dream Eater (138)", "Poison Gas (139)", "Barrage (140)", "Leech Life (141)", "Lovely Kiss (142)", "Sky Attack (143)", "Transform (144)", "Bubble (145)", "Dizzy Punch (146)", "Spore (147)", "Flash (148)", "Psywave (149)", "Splash (150)", "Acid Armor (151)", "Crabhammer (152)", "Explosion (153)", "Fury Swipes (154)", "Bonemerang (155)", "Rest (156)", "Rock Slide (163)", "Hyper Fang (158)", "Sharpen (159)", "Conversion (160)", "Tri Attack (161)", "Super Fang (162)", "Slash (163)", "Substitute (164)", "Struggle (165)", "~166", "~167", "~168", "~169", "~170", "~171", "~172", "~173", "~174", "~175", "~176", "~177", "~178", "~179", "~180", "~181", "~182", "~183", "~184", "~185", "~186", "~187", "~188", "~189", "~190", "~191", "~192", "~193", "~194", "~195", "~196", "~197", "~198", "~199", "~200", "~201", "~202", "~203", "~204", "~205", "~206", "~207", "~208", "~209", "~210", "~211", "~212", "~213", "~214", "~215", "~216", "~217", "~218", "~219", "~220", "~221", "~222", "~223", "~224", "~225", "~226", "~227", "~228", "~229", "~230", "~231", "~232", "~233", "~234", "~235", "~236", "~237", "~238", "~239", "~240", "~241", "~242", "~243", "~244", "~245", "~246", "~247", "~248", "~249", "~250", "~251", "~252", "~253", "~254", "~255"]
types_rb = ["Normal (0)", "Fighting (1)", "Flying (2)", "Poison (3)", "Ground (4)", "Rock (5)", "Bird (6)", "Bug (7)", "Ghost (8)", "~9", "~10", "~11", "~12", "~13", "~14", "~15", "~16", "~17", "~18", "~19", "Fire (20)", "Water (21)", "Grass (22)", "Electric (23)", "Psychic (24)", "Ice (25)", "Dragon (26)", "~27", "~28", "~29", "~30", "~31", "~32", "~33", "~34", "~35", "~36", "~37", "~38", "~39", "~40", "~41", "~42", "~43", "~44", "~45", "~46", "~47", "~48", "~49", "~50", "~51", "~52", "~53", "~54", "~55", "~56", "~57", "~58", "~59", "~60", "~61", "~62", "~63", "~64", "~65", "~66", "~67", "~68", "~69", "~70", "~71", "~72", "~73", "~74", "~75", "~76", "~77", "~78", "~79", "~80", "~81", "~82", "~83", "~84", "~85", "~86", "~87", "~88", "~89", "~90", "~91", "~92", "~93", "~94", "~95", "~96", "~97", "~98", "~99", "~100", "~101", "~102", "~103", "~104", "~105", "~106", "~107", "~108", "~109", "~110", "~111", "~112", "~113", "~163", "~115", "~116", "~117", "~118", "~119", "~120", "~121", "~122", "~123", "~124", "~125", "~126", "~127", "~128", "~129", "~130", "~131", "~132", "~133", "~134", "~135", "~136", "~137", "~138", "~139", "~140", "~141", "~142", "~143", "~144", "~145", "~146", "~147", "~148", "~149", "~150", "~151", "~152", "~153", "~154", "~155", "~156", "~163", "~158", "~159", "~160", "~161", "~162", "~163", "~164", "~165", "~166", "~167", "~168", "~169", "~170", "~171", "~172", "~173", "~174", "~175", "~176", "~177", "~178", "~179", "~180", "~181", "~182", "~183", "~184", "~185", "~186", "~187", "~188", "~189", "~190", "~191", "~192", "~193", "~194", "~195", "~196", "~197", "~198", "~199", "~200", "~201", "~202", "~203", "~204", "~205", "~206", "~207", "~208", "~209", "~210", "~211", "~212", "~213", "~214", "~215", "~216", "~217", "~218", "~219", "~220", "~221", "~222", "~223", "~224", "~225", "~226", "~227", "~228", "~229", "~230", "~231", "~232", "~233", "~234", "~235", "~236", "~237", "~238", "~239", "~240", "~241", "~242", "~243", "~244", "~245", "~246", "~247", "~248", "~249", "~250", "~251", "~252", "~253", "~254", "~255"]

items_gs = ["~0", "Master Ball (1)", "Ultra Ball (2)", "Brightpowder (3)", "Great Ball (4)", "Poké Ball (5)", "Teru-sama (6)", "Bicycle (7)", "Moon Stone (8)", "Antidote (9)", "Burn Heal (10)", "Ice Heal (11)", "Awakening (12)", "Parlyz Heal (13)", "Full Restore (14)", "Max Potion (15)", "Hyper Potion (16)", "Super Potion (17)", "Potion (18)", "Escape Rope (19)", "Repel (20)", "Max Elixer (21)", "Fire Stone (22)", "Thunderstone (23)", "Water Stone (24)", "Teru-sama (25)", "HP Up (26)", "Protein (27)", "Iron (28)", "Carbos (29)", "Lucky Punch (30)", "Calcium (31)", "Rare Candy (32)", "X Accuracy (33)", "Leaf Stone (34)", "Metal Powder (35)", "Nugget (36)", "Poké Doll (37)", "Full Heal (38)", "Revive (39)", "Max Revive (40)", "Guard Spec. (41)", "Super Repel (42)", "Max Repel (43)", "Dire Hit (44)", "Teru-sama (45)", "Fresh Water (46)", "Soda Pop (47)", "Lemonade (48)", "X Attack (49)", "Teru-sama (50)", "X Defend (51)", "X Speed (52)", "X Special (53)", "Coin Case (54)", "Itemfinder (55)", "Teru-sama (56)", "Exp.share (57)", "Old Rod (58)", "Good Rod (59)", "Silver Leaf (60)", "Super Rod (61)", "PP Up (62)", "Ether (63)", "Max Ether (64)", "Elixer (65)", "Red Scale (66)", "Secretpotion (67)", "S.s.ticket (68)", "Mystery Egg (69)", "Teru-sama (70)", "Silver Wing (71)", "Moomoo Milk (72)", "Quick Claw (73)", "Psncureberry (74)", "Gold Leaf (75)", "Soft Sand (76)", "Sharp Beak (77)", "Przcureberry (78)", "Burnt Berry (79)", "Ice Berry (80)", "Poison Barb (81)", "King's Rock (82)", "Bitter Berry (83)", "Mint Berry (84)", "Red Apricorn (85)", "Tinymushroom (86)", "Big Mushroom (87)", "Silverpowder (88)", "Blu Apricorn (89)", "Teru-sama (90)", "Amulet Coin (91)", "Ylw Apricorn (92)", "Grn Apricorn (93)", "Cleanse Tag (94)", "Mystic Water (95)", "Twistedspoon (96)", "Wht Apricorn (97)", "Blackbelt (98)", "Blk Apricorn (99)", "Teru-sama (100)", "Pnk Apricorn (101)", "Blackglasses (102)", "Slowpoketail (103)", "Pink Bow (104)", "Stick (105)", "Smoke Ball (106)", "Nevermeltice (107)", "Magnet (108)", "Miracleberry (109)", "Pearl (110)", "Big Pearl (111)", "Everstone (112)", "Spell Tag (113)", "Ragecandybar (163)", "Teru-sama (115)", "Teru-sama (116)", "Miracle Seed (117)", "Thick Club (118)", "Focus Band (119)", "Teru-sama (120)", "Energypowder (121)", "Energy Root (122)", "Heal Powder (123)", "Revival Herb (124)", "Hard Stone (125)", "Lucky Egg (126)", "Card Key (127)", "Machine Part (128)", "Teru-sama (129)", "Lost Item (130)", "Stardust (131)", "Star Piece (132)", "Basement Key (133)", "Pass (134)", "Teru-sama (135)", "Teru-sama (136)", "Teru-sama (137)", "Charcoal (138)", "Berry Juice (139)", "Scope Lens (140)", "Teru-sama (141)", "Teru-sama (142)", "Metal Coat (143)", "Dragon Fang (144)", "Teru-sama (145)", "Leftovers (146)", "Teru-sama (147)", "Teru-sama (148)", "Teru-sama (149)", "Mysteryberry (150)", "Dragon Scale (151)", "Berserk Gene (152)", "Teru-sama (153)", "Teru-sama (154)", "Teru-sama (155)", "Sacred Ash (156)", "Heavy Ball (163)", "Flower Mail (158)", "Level Ball (159)", "Lure Ball (160)", "Fast Ball (161)", "Teru-sama (162)", "Light Ball (163)", "Friend Ball (164)", "Moon Ball (165)", "Love Ball (166)", "Normal Box (167)", "Gorgeous Box (168)", "Sun Stone (169)", "Polkadot Bow (170)", "Teru-sama (171)", "Up-grade (172)", "Berry (173)", "Gold Berry (174)", "Squirtbottle (175)", "Teru-sama (176)", "Park Ball (177)", "Rainbow Wing (178)", "Teru-sama (179)", "Brick Piece (180)", "Surf Mail (181)", "Litebluemail (182)", "Portraitmail (183)", "Lovely Mail (184)", "Eon Mail (185)", "Morph Mail (186)", "Bluesky Mail (187)", "Music Mail (188)", "Mirage Mail (189)", "Teru-sama (190)", "TM01 (191)", "TM02 (192)", "TM03 (193)", "TM04 (194)", "Teru-sama (195)", "TM05 (196)", "TM06 (197)", "TM07 (198)", "TM08 (199)", "TM09 (200)", "TM10 (201)", "TM11 (202)", "TM12 (203)", "TM13 (204)", "TM14 (205)", "TM15 (206)", "TM16 (207)", "TM17 (208)", "TM18 (209)", "TM19 (210)", "TM20 (211)", "TM21 (212)", "TM22 (213)", "TM23 (214)", "TM24 (215)", "TM25 (216)", "TM26 (217)", "TM27 (218)", "TM28 (219)", "Teru-sama (220)", "TM29 (221)", "TM30 (222)", "TM31 (223)", "TM32 (224)", "TM33 (225)", "TM34 (226)", "TM35 (227)", "TM36 (228)", "TM37 (229)", "TM38 (230)", "TM39 (231)", "TM40 (232)", "TM41 (233)", "TM42 (234)", "TM43 (235)", "TM44 (236)", "TM45 (237)", "TM46 (238)", "TM47 (239)", "TM48 (240)", "TM49 (241)", "TM50 (242)", "HM01 (243)", "HM02 (244)", "HM03 (245)", "HM04 (246)", "HM05 (247)", "HM06 (248)", "HM07 (249)", "Teru-sama (250)", "Teru-sama (251)", "Teru-sama (252)", "Teru-sama (253)", "Teru-sama (254)", "-- Cancel -- (255)"]
pokemon_gs = ["~0", "Bulbasaur (1)", "Ivysaur (2)", "Venusaur (3)", "Charmander (4)", "Charmeleon (5)", "Charizard (6)", "Squirtle (7)", "Wartortle (8)", "Blastoise (9)", "Caterpie (10)", "Metapod (11)", "Butterfree (12)", "Weedle (13)", "Kakuna (14)", "Beedrill (15)", "Pidgey (16)", "Pidgeotto (17)", "Pidgeot (18)", "Rattata (19)", "Raticate (20)", "Spearow (21)", "Fearow (22)", "Ekans (23)", "Arbok (24)", "Pikachu (25)", "Raichu (26)", "Sandshrew (27)", "Sandslash (28)", "Nidoranh (29)", "Nidorina (30)", "Nidoqueen (31)", "Nidoranm (32)", "Nidorino (33)", "Nidoking (34)", "Clefairy (35)", "Clefable (36)", "Vulpix (37)", "Ninetales (38)", "Jigglypuff (39)", "Wigglytuff (40)", "Zubat (41)", "Golbat (42)", "Oddish (43)", "Gloom (44)", "Vileplume (45)", "Paras (46)", "Parasect (47)", "Venonat (48)", "Venomoth (49)", "Diglett (50)", "Dugtrio (51)", "Meowth (52)", "Persian (53)", "Psyduck (54)", "Golduck (55)", "Mankey (56)", "Primeape (57)", "Growlithe (58)", "Arcanine (59)", "Poliwag (60)", "Poliwhirl (61)", "Poliwrath (62)", "Abra (63)", "Kadabra (64)", "Alakazam (65)", "Machop (66)", "Machoke (67)", "Machamp (68)", "Bellsprout (69)", "Weepinbell (70)", "Victreebel (71)", "Tentacool (72)", "Tentacruel (73)", "Geodude (74)", "Graveler (75)", "Golem (76)", "Ponyta (77)", "Rapidash (78)", "Slowpoke (79)", "Slowbro (80)", "Magnemite (81)", "Magneton (82)", "Farfetch'd (83)", "Doduo (84)", "Dodrio (85)", "Seel (86)", "Dewgong (87)", "Grimer (88)", "Muk (89)", "Shellder (90)", "Cloyster (91)", "Gastly (92)", "Haunter (93)", "Gengar (94)", "Onix (95)", "Drowzee (96)", "Hypno (97)", "Krabby (98)", "Kingler (99)", "Voltorb (100)", "Electrode (101)", "Exeggcute (102)", "Exeggutor (103)", "Cubone (104)", "Marowak (105)", "Hitmonlee (106)", "Hitmonchan (107)", "Lickitung (108)", "Koffing (109)", "Weezing (110)", "Rhyhorn (111)", "Rhydon (112)", "Chansey (113)", "Tangela (163)", "Kangaskhan (115)", "Horsea (116)", "Seadra (117)", "Goldeen (118)", "Seaking (119)", "Staryu (120)", "Starmie (121)", "Mr.mime (122)", "Scyther (123)", "Jynx (124)", "Electabuzz (125)", "Magmar (126)", "Pinsir (127)", "Tauros (128)", "Magikarp (129)", "Gyarados (130)", "Lapras (131)", "Ditto (132)", "Eevee (133)", "Vaporeon (134)", "Jolteon (135)", "Flareon (136)", "Porygon (137)", "Omanyte (138)", "Omastar (139)", "Kabuto (140)", "Kabutops (141)", "Aerodactyl (142)", "Snorlax (143)", "Articuno (144)", "Zapdos (145)", "Moltres (146)", "Dratini (147)", "Dragonair (148)", "Dragonite (149)", "Mewtwo (150)", "Mew (151)", "Chikorita (152)", "Bayleef (153)", "Meganium (154)", "Cyndaquil (155)", "Quilava (156)", "Typhlosion (163)", "Totodile (158)", "Croconaw (159)", "Feraligatr (160)", "Sentret (161)", "Furret (162)", "Hoothoot (163)", "Noctowl (164)", "Ledyba (165)", "Ledian (166)", "Spinarak (167)", "Ariados (168)", "Crobat (169)", "Chinchou (170)", "Lanturn (171)", "Pichu (172)", "Cleffa (173)", "Igglybuff (174)", "Togepi (175)", "Togetic (176)", "Natu (177)", "Xatu (178)", "Mareep (179)", "Flaaffy (180)", "Ampharos (181)", "Bellossom (182)", "Marill (183)", "Azumarill (184)", "Sudowoodo (185)", "Politoed (186)", "Hoppip (187)", "Skiploom (188)", "Jumpluff (189)", "Aipom (190)", "Sunkern (191)", "Sunflora (192)", "Yanma (193)", "Wooper (194)", "Quagsire (195)", "Espeon (196)", "Umbreon (197)", "Murkrow (198)", "Slowking (199)", "Misdreavus (200)", "Unown (201)", "Wobbuffet (202)", "Girafarig (203)", "Pineco (204)", "Forretress (205)", "Dunsparce (206)", "Gligar (207)", "Steelix (208)", "Snubbull (209)", "Granbull (210)", "Qwilfish (211)", "Scizor (212)", "Shuckle (213)", "Heracross (214)", "Sneasel (215)", "Teddiursa (216)", "Ursaring (217)", "Slugma (218)", "Magcargo (219)", "Swinub (220)", "Piloswine (221)", "Corsola (222)", "Remoraid (223)", "Octillery (224)", "Delibird (225)", "Mantine (226)", "Skarmory (227)", "Houndour (228)", "Houndoom (229)", "Kingdra (230)", "Phanpy (231)", "Donphan (232)", "Porygon2 (233)", "Stantler (234)", "Smeargle (235)", "Tyrogue (236)", "Hitmontop (237)", "Smoochum (238)", "Elekid (239)", "Magby (240)", "Miltank (241)", "Blissey (242)", "Raikou (243)", "Entei (244)", "Suicune (245)", "Larvitar (246)", "Pupitar (247)", "Tyranitar (248)", "Lugia (249)", "Ho-oh (250)", "Celebi (251)", "????? (252)", "Egg (253)", "????? (254)", "-- No Pokemon -- (255)" ]
pokedex_gs = ["#000 Er", "#001 Bulbasaur", "#002 Ivysaur", "#003 Venusaur", "#004 Charmander", "#005 Charmeleon", "#006 Charizard", "#007 Squirtle", "#008 Wartortle", "#009 Blastoise", "#010 Caterpie", "#011 Metapod", "#012 Butterfree", "#013 Weedle", "#014 Kakuna", "#015 Beedrill", "#016 Pidgey", "#017 Pidgeotto", "#018 Pidgeot", "#019 Rattata", "#020 Raticate", "#021 Spearow", "#022 Fearow", "#023 Ekans", "#024 Arbok", "#025 Pikachu", "#026 Raichu", "#027 Sandshrew", "#028 Sandslash", "#029 Nidoranh", "#030 Nidorina", "#031 Nidoqueen", "#032 Nidoranm", "#033 Nidorino", "#034 Nidoking", "#035 Clefairy", "#036 Clefable", "#037 Vulpix", "#038 Ninetales", "#039 Jigglypuff", "#040 Wigglytuff", "#041 Zubat", "#042 Golbat", "#043 Oddish", "#044 Gloom", "#045 Vileplume", "#046 Paras", "#047 Parasect", "#048 Venonat", "#049 Venomoth", "#050 Diglett", "#051 Dugtrio", "#052 Meowth", "#053 Persian", "#054 Psyduck", "#055 Golduck", "#056 Mankey", "#057 Primeape", "#058 Growlithe", "#059 Arcanine", "#060 Poliwag", "#061 Poliwhirl", "#062 Poliwrath", "#063 Abra", "#064 Kadabra", "#065 Alakazam", "#066 Machop", "#067 Machoke", "#068 Machamp", "#069 Bellsprout", "#070 Weepinbell", "#071 Victreebel", "#072 Tentacool", "#073 Tentacruel", "#074 Geodude", "#075 Graveler", "#076 Golem", "#077 Ponyta", "#078 Rapidash", "#079 Slowpoke", "#080 Slowbro", "#081 Magnemite", "#082 Magneton", "#083 Farfetch'd", "#084 Doduo", "#085 Dodrio", "#086 Seel", "#087 Dewgong", "#088 Grimer", "#089 Muk", "#090 Shellder", "#091 Cloyster", "#092 Gastly", "#093 Haunter", "#094 Gengar", "#095 Onix", "#096 Drowzee", "#097 Hypno", "#098 Krabby", "#099 Kingler", "#100 Voltorb", "#101 Electrode", "#102 Exeggcute", "#103 Exeggutor", "#104 Cubone", "#105 Marowak", "#106 Hitmonlee", "#107 Hitmonchan", "#108 Lickitung", "#109 Koffing", "#110 Weezing", "#111 Rhyhorn", "#112 Rhydon", "#113 Chansey", "#163 Tangela", "#115 Kangaskhan", "#116 Horsea", "#117 Seadra", "#118 Goldeen", "#119 Seaking", "#120 Staryu", "#121 Starmie", "#122 Mr.mime", "#123 Scyther", "#124 Jynx", "#125 Electabuzz", "#126 Magmar", "#127 Pinsir", "#128 Tauros", "#129 Magikarp", "#130 Gyarados", "#131 Lapras", "#132 Ditto", "#133 Eevee", "#134 Vaporeon", "#135 Jolteon", "#136 Flareon", "#137 Porygon", "#138 Omanyte", "#139 Omastar", "#140 Kabuto", "#141 Kabutops", "#142 Aerodactyl", "#143 Snorlax", "#144 Articuno", "#145 Zapdos", "#146 Moltres", "#147 Dratini", "#148 Dragonair", "#149 Dragonite", "#150 Mewtwo", "#151 Mew", "#152 Chikorita", "#153 Bayleef", "#154 Meganium", "#155 Cyndaquil", "#156 Quilava", "#163 Typhlosion", "#158 Totodile", "#159 Croconaw", "#160 Feraligatr", "#161 Sentret", "#162 Furret", "#163 Hoothoot", "#164 Noctowl", "#165 Ledyba", "#166 Ledian", "#167 Spinarak", "#168 Ariados", "#169 Crobat", "#170 Chinchou", "#171 Lanturn", "#172 Pichu", "#173 Cleffa", "#174 Igglybuff", "#175 Togepi", "#176 Togetic", "#177 Natu", "#178 Xatu", "#179 Mareep", "#180 Flaaffy", "#181 Ampharos", "#182 Bellossom", "#183 Marill", "#184 Azumarill", "#185 Sudowoodo", "#186 Politoed", "#187 Hoppip", "#188 Skiploom", "#189 Jumpluff", "#190 Aipom", "#191 Sunkern", "#192 Sunflora", "#193 Yanma", "#194 Wooper", "#195 Quagsire", "#196 Espeon", "#197 Umbreon", "#198 Murkrow", "#199 Slowking", "#200 Misdreavus", "#201 Unown", "#202 Wobbuffet", "#203 Girafarig", "#204 Pineco", "#205 Forretress", "#206 Dunsparce", "#207 Gligar", "#208 Steelix", "#209 Snubbull", "#210 Granbull", "#211 Qwilfish", "#212 Scizor", "#213 Shuckle", "#214 Heracross", "#215 Sneasel", "#216 Teddiursa", "#217 Ursaring", "#218 Slugma", "#219 Magcargo", "#220 Swinub", "#221 Piloswine", "#222 Corsola", "#223 Remoraid", "#224 Octillery", "#225 Delibird", "#226 Mantine", "#227 Skarmory", "#228 Houndour", "#229 Houndoom", "#230 Kingdra", "#231 Phanpy", "#232 Donphan", "#233 Porygon2", "#234 Stantler", "#235 Smeargle", "#236 Tyrogue", "#237 Hitmontop", "#238 Smoochum", "#239 Elekid", "#240 Magby", "#241 Miltank", "#242 Blissey", "#243 Raikou", "#244 Entei", "#245 Suicune", "#246 Larvitar", "#247 Pupitar", "#248 Tyranitar", "#249 Lugia", "#250 Ho-oh", "#251 Celebi", "#252 ?????", "#253 Egg", "#254 ?????", "#255 ?????" ]
moves_gs = ["-- No Move -- (0)", "Pound (1)", "Karate Chop (2)", "Doubleslap (3)", "Comet Punch (4)", "Mega Punch (5)", "Pay Day (6)", "Fire Punch (7)", "Ice Punch (8)", "Thunderpunch (9)", "Scratch (10)", "Vicegrip (11)", "Guillotine (12)", "Razor Wind (13)", "Swords Dance (14)", "Cut (15)", "Gust (16)", "Wing Attack (17)", "Whirlwind (18)", "Fly (19)", "Bind (20)", "Slam (21)", "Vine Whip (22)", "Stomp (23)", "Double Kick (24)", "Mega Kick (25)", "Jump Kick (26)", "Rolling Kick (27)", "Sand-attack (28)", "Headbutt (29)", "Horn Attack (30)", "Fury Attack (31)", "Horn Drill (32)", "Tackle (33)", "Body Slam (34)", "Wrap (35)", "Take Down (36)", "Thrash (37)", "Double-edge (38)", "Tail Whip (39)", "Poison Sting (40)", "Twineedle (41)", "Pin Missile (42)", "Leer (43)", "Bite (44)", "Growl (45)", "Roar (46)", "Sing (47)", "Supersonic (48)", "Sonicboom (49)", "Disable (50)", "Acid (51)", "Ember (52)", "Flamethrower (53)", "Mist (54)", "Water Gun (55)", "Hydro Pump (56)", "Surf (57)", "Ice Beam (58)", "Blizzard (59)", "Psybeam (60)", "Bubblebeam (61)", "Aurora Beam (62)", "Hyper Beam (63)", "Peck (64)", "Drill Peck (65)", "Submission (66)", "Low Kick (67)", "Counter (68)", "Seismic Toss (69)", "Strength (70)", "Absorb (71)", "Mega Drain (72)", "Leech Seed (73)", "Growth (74)", "Razor Leaf (75)", "Solarbeam (76)", "Poisonpowder (77)", "Stun Spore (78)", "Sleep Powder (79)", "Petal Dance (80)", "String Shot (81)", "Dragon Rage (82)", "Fire Spin (83)", "Thundershock (84)", "Thunderbolt (85)", "Thunder Wave (86)", "Thunder (87)", "Rock Throw (88)", "Earthquake (89)", "Fissure (90)", "Dig (91)", "Toxic (92)", "Confusion (93)", "Psychic (94)", "Hypnosis (95)", "Meditate (96)", "Agility (97)", "Quick Attack (98)", "Rage (99)", "Teleport (100)", "Night Shade (101)", "Mimic (102)", "Screech (103)", "Double Team (104)", "Recover (105)", "Harden (106)", "Minimize (107)", "Smokescreen (108)", "Confuse Ray (109)", "Withdraw (110)", "Defense Curl (111)", "Barrier (112)", "Light Screen (113)", "Haze (163)", "Reflect (115)", "Focus Energy (116)", "Bide (117)", "Metronome (118)", "Mirror Move (119)", "Selfdestruct (120)", "Egg Bomb (121)", "Lick (122)", "Smog (123)", "Sludge (124)", "Bone Club (125)", "Fire Blast (126)", "Waterfall (127)", "Clamp (128)", "Swift (129)", "Skull Bash (130)", "Spike Cannon (131)", "Constrict (132)", "Amnesia (133)", "Kinesis (134)", "Softboiled (135)", "Hi Jump Kick (136)", "Glare (137)", "Dream Eater (138)", "Poison Gas (139)", "Barrage (140)", "Leech Life (141)", "Lovely Kiss (142)", "Sky Attack (143)", "Transform (144)", "Bubble (145)", "Dizzy Punch (146)", "Spore (147)", "Flash (148)", "Psywave (149)", "Splash (150)", "Acid Armor (151)", "Crabhammer (152)", "Explosion (153)", "Fury Swipes (154)", "Bonemerang (155)", "Rest (156)", "Rock Slide (163)", "Hyper Fang (158)", "Sharpen (159)", "Conversion (160)", "Tri Attack (161)", "Super Fang (162)", "Slash (163)", "Substitute (164)", "Struggle (165)", "Sketch (166)", "Triple Kick (167)", "Thief (168)", "Spider Web (169)", "Mind Reader (170)", "Nightmare (171)", "Flame Wheel (172)", "Snore (173)", "Curse (174)", "Flail (175)", "Conversion2 (176)", "Aeroblast (177)", "Cotton Spore (178)", "Reversal (179)", "Spite (180)", "Powder Snow (181)", "Protect (182)", "Mach Punch (183)", "Scary Face (184)", "Faint Attack (185)", "Sweet Kiss (186)", "Belly Drum (187)", "Sludge Bomb (188)", "Mud-slap (189)", "Octazooka (190)", "Spikes (191)", "Zap Cannon (192)", "Foresight (193)", "Destiny Bond (194)", "Perish Song (195)", "Icy Wind (196)", "Detect (197)", "Bone Rush (198)", "Lock-on (199)", "Outrage (200)", "Sandstorm (201)", "Giga Drain (202)", "Endure (203)", "Charm (204)", "Rollout (205)", "False Swipe (206)", "Swagger (207)", "Milk Drink (208)", "Spark (209)", "Fury Cutter (210)", "Steel Wing (211)", "Mean Look (212)", "Attract (213)", "Sleep Talk (214)", "Heal Bell (215)", "Return (216)", "Present (217)", "Frustration (218)", "Safeguard (219)", "Pain Split (220)", "Sacred Fire (221)", "Magnitude (222)", "Dynamicpunch (223)", "Megahorn (224)", "Dragonbreath (225)", "Baton Pass (226)", "Encore (227)", "Pursuit (228)", "Rapid Spin (229)", "Sweet Scent (230)", "Iron Tail (231)", "Metal Claw (232)", "Vital Throw (233)", "Morning Sun (234)", "Synthesis (235)", "Moonlight (236)", "Hidden Power (237)", "Cross Chop (238)", "Twister (239)", "Rain Dance (240)", "Sunny Day (241)", "Crunch (242)", "Mirror Coat (243)", "Psych Up (244)", "Extremespeed (245)", "Ancientpower (246)", "Shadow Ball (247)", "Future Sight (248)", "Rock Smash (249)", "Whirlpool (250)", "Beat Up (251)", "~252", "~253", "~254", "~255"]
types_gs = ["Normal (0)", "Fighting (1)", "Flying (2)", "Poison (3)", "Ground (4)", "Rock (5)", "Bird (6)", "Bug (7)", "Ghost (8)", "Steel (9)", "~10", "~11", "~12", "~13", "~14", "~15", "~16", "~17", "~18", "~19", "Fire (20)", "Water (21)", "Grass (22)", "Electric (23)", "Psychic (24)", "Ice (25)", "Dragon (26)", "Dark (27)", "~28", "~29", "~30", "~31", "~32", "~33", "~34", "~35", "~36", "~37", "~38", "~39", "~40", "~41", "~42", "~43", "~44", "~45", "~46", "~47", "~48", "~49", "~50", "~51", "~52", "~53", "~54", "~55", "~56", "~57", "~58", "~59", "~60", "~61", "~62", "~63", "~64", "~65", "~66", "~67", "~68", "~69", "~70", "~71", "~72", "~73", "~74", "~75", "~76", "~77", "~78", "~79", "~80", "~81", "~82", "~83", "~84", "~85", "~86", "~87", "~88", "~89", "~90", "~91", "~92", "~93", "~94", "~95", "~96", "~97", "~98", "~99", "~100", "~101", "~102", "~103", "~104", "~105", "~106", "~107", "~108", "~109", "~110", "~111", "~112", "~113", "~163", "~115", "~116", "~117", "~118", "~119", "~120", "~121", "~122", "~123", "~124", "~125", "~126", "~127", "~128", "~129", "~130", "~131", "~132", "~133", "~134", "~135", "~136", "~137", "~138", "~139", "~140", "~141", "~142", "~143", "~144", "~145", "~146", "~147", "~148", "~149", "~150", "~151", "~152", "~153", "~154", "~155", "~156", "~163", "~158", "~159", "~160", "~161", "~162", "~163", "~164", "~165", "~166", "~167", "~168", "~169", "~170", "~171", "~172", "~173", "~174", "~175", "~176", "~177", "~178", "~179", "~180", "~181", "~182", "~183", "~184", "~185", "~186", "~187", "~188", "~189", "~190", "~191", "~192", "~193", "~194", "~195", "~196", "~197", "~198", "~199", "~200", "~201", "~202", "~203", "~204", "~205", "~206", "~207", "~208", "~209", "~210", "~211", "~212", "~213", "~214", "~215", "~216", "~217", "~218", "~219", "~220", "~221", "~222", "~223", "~224", "~225", "~226", "~227", "~228", "~229", "~230", "~231", "~232", "~233", "~234", "~235", "~236", "~237", "~238", "~239", "~240", "~241", "~242", "~243", "~244", "~245", "~246", "~247", "~248", "~249", "~250", "~251", "~252", "~253", "~254", "~255"]

items_rs = ["-- No Item --", "Master Ball (1)","Ultra Ball (2)","Great Ball (3)","Poke Ball (4)","Safari Ball (5)","Net Ball (6)","Dive Ball (7)","Nest Ball (8)","Repeat Ball (9)","Timer Ball (10)","Luxury Ball (11)","Premier Ball (12)","Potion (13)","Antidote (14)","Burn Heal (15)","Ice Heal (16)","Awakening (17)","Parlyz Heal (18)","Full Restore (19)","Max Potion (20)","Hyper Potion (21)","Super Potion (22)","Full Heal (23)","Revive (24)","Max Revive (25)","Fresh Water (26)","Soda Pop (27)","Lemonade (28)","Moomoo Milk (29)","Energypowder (30)","Energy Root (31)","Heal Powder (32)","Revival Herb (33)","Ether (34)","Max Ether (35)","Elixir (36)","Max Elixir (37)","Lava Cookie (38)","Blue Flute (39)","Yellow Flute (40)","Red Flute (41)","Black Flute (42)","White Flute (43)","Berry Juice (44)","Sacred Ash (45)","Shoal Salt (46)","Shoal Shell (47)","Red Shard (48)","Blue Shard (49)","Yellow Shard (50)","Green Shard (51)","???????? (52)","???????? (53)","???????? (54)","???????? (55)","???????? (56)","???????? (57)","???????? (58)","???????? (59)","???????? (60)","???????? (61)","???????? (62)","Hp Up (63)","Protein (64)","Iron (65)","Carbos (66)","Calcium (67)","Rare Candy (68)","Pp Up (69)","Zinc (70)","Pp Max (71)","???????? (72)","Guard Spec. (73)","Dire Hit (74)","X Attack (75)","X Defend (76)","X Speed (77)","X Accuracy (78)","X Special (79)","Poke Doll (80)","Fluffy Tail (81)","???????? (82)","Super Repel (83)","Max Repel (84)","Escape Rope (85)","Repel (86)","???????? (87)","???????? (88)","???????? (89)","???????? (90)","???????? (91)","???????? (92)","Sun Stone (93)","Moon Stone (94)","Fire Stone (95)","Thunderstone (96)","Water Stone (97)","Leaf Stone (98)","???????? (99)","???????? (100)","???????? (101)","???????? (102)","Tinymushroom (103)","Big Mushroom (104)","???????? (105)","Pearl (106)","Big Pearl (107)","Stardust (108)","Star Piece (109)","Nugget (110)","Heart Scale (111)","???????? (112)","???????? (113)","???????? (163)","???????? (115)","???????? (116)","???????? (117)","???????? (118)","???????? (119)","???????? (120)","Orange Mail (121)","Harbor Mail (122)","Glitter Mail (123)","Mech Mail (124)","Wood Mail (125)","Wave Mail (126)","Bead Mail (127)","Shadow Mail (128)","Tropic Mail (129)","Dream Mail (130)","Fab Mail (131)","Retro Mail (132)","Cheri Berry (133)","Chesto Berry (134)","Pecha Berry (135)","Rawst Berry (136)","Aspear Berry (137)","Leppa Berry (138)","Oran Berry (139)","Persim Berry (140)","Lum Berry (141)","Sitrus Berry (142)","Figy Berry (143)","Wiki Berry (144)","Mago Berry (145)","Aguav Berry (146)","Iapapa Berry (147)","Razz Berry (148)","Bluk Berry (149)","Nanab Berry (150)","Wepear Berry (151)","Pinap Berry (152)","Pomeg Berry (153)","Kelpsy Berry (154)","Qualot Berry (155)","Hondew Berry (156)","Grepa Berry (163)","Tamato Berry (158)","Cornn Berry (159)","Magost Berry (160)","Rabuta Berry (161)","Nomel Berry (162)","Spelon Berry (163)","Pamtre Berry (164)","Watmel Berry (165)","Durin Berry (166)","Belue Berry (167)","Liechi Berry (168)","Ganlon Berry (169)","Salac Berry (170)","Petaya Berry (171)","Apicot Berry (172)","Lansat Berry (173)","Starf Berry (174)","Enigma Berry (175)","???????? (176)","???????? (177)","???????? (178)","Brightpowder (179)","White Herb (180)","Macho Brace (181)","Exp. Share (182)","Quick Claw (183)","Soothe Bell (184)","Mental Herb (185)","Choice Band (186)","King's Rock (187)","Silverpowder (188)","Amulet Coin (189)","Cleanse Tag (190)","Soul Dew (191)","Deepseatooth (192)","Deepseascale (193)","Smoke Ball (194)","Everstone (195)","Focus Band (196)","Lucky Egg (197)","Scope Lens (198)","Metal Coat (199)","Leftovers (200)","Dragon Scale (201)","Light Ball (202)","Soft Sand (203)","Hard Stone (204)","Miracle Seed (205)","Blackglasses (206)","Black Belt (207)","Magnet (208)","Mystic Water (209)","Sharp Beak (210)","Poison Barb (211)","Nevermeltice (212)","Spell Tag (213)","Twistedspoon (214)","Charcoal (215)","Dragon Fang (216)","Silk Scarf (217)","Up-grade (218)","Shell Bell (219)","Sea Incense (220)","Lax Incense (221)","Lucky Punch (222)","Metal Powder (223)","Thick Club (224)","Stick (225)","???????? (226)","???????? (227)","???????? (228)","???????? (229)","???????? (230)","???????? (231)","???????? (232)","???????? (233)","???????? (234)","???????? (235)","???????? (236)","???????? (237)","???????? (238)","???????? (239)","???????? (240)","???????? (241)","???????? (242)","???????? (243)","???????? (244)","???????? (245)","???????? (246)","???????? (247)","???????? (248)","???????? (249)","???????? (250)","???????? (251)","???????? (252)","???????? (253)","Red Scarf (254)","Blue Scarf (255)","Pink Scarf (256)","Green Scarf (257)","Yellow Scarf (258)","Mach Bike (259)","Coin Case (260)","Itemfinder (261)","Old Rod (262)","Good Rod (263)","Super Rod (264)","S.s. Ticket (265)","Contest Pass (266)","???????? (267)","Wailmer Pail (268)","Devon Goods (269)","Soot Sack (270)","Basement Key (271)","Acro Bike (272)","Pokeblock Case (273)","Letter (274)","Eon Ticket (275)","Red Orb (276)","Blue Orb (277)","Scanner (278)","Go-goggles (279)","Meteorite (280)","Rm. 1 Key (281)","Rm. 2 Key (282)","Rm. 4 Key (283)","Rm. 6 Key (284)","Storage Key (285)","Root Fossil (286)","Claw Fossil (287)","Devon Scope (288)","TM01 (289)","TM02 (290)","TM03 (291)","TM04 (292)","TM05 (293)","TM06 (294)","TM07 (295)","TM08 (296)","TM09 (297)","TM10 (298)","TM11 (299)","TM12 (300)","TM13 (301)","TM14 (302)","TM15 (303)","TM16 (304)","TM17 (305)","TM18 (306)","TM19 (307)","TM20 (308)","TM21 (309)","TM22 (310)","TM23 (311)","TM24 (312)","TM25 (313)","TM26 (314)","TM27 (315)","TM28 (316)","TM29 (317)","TM30 (318)","TM31 (319)","TM32 (320)","TM33 (321)","TM34 (322)","TM35 (323)","TM36 (324)","TM37 (325)","TM38 (326)","TM39 (327)","TM40 (328)","TM41 (329)","TM42 (330)","TM43 (331)","TM44 (332)","TM45 (333)","TM46 (334)","TM47 (335)","TM48 (336)","TM49 (337)","TM50 (338)","HM01 (339)","HM02 (340)","HM03 (341)","HM04 (342)","HM05 (343)","HM06 (344)","HM07 (345)","HM08 (346)","???????? (347)","???????? (348)"]
pokemon_rs = ["-- No Pokemon -- (0)", "Bulbasaur (1)", "Ivysaur (2)", "Venusaur (3)", "Charmander (4)", "Charmeleon (5)", "Charizard (6)", "Squirtle (7)", "Wartortle (8)", "Blastoise (9)", "Caterpie (10)", "Metapod (11)", "Butterfree (12)", "Weedle (13)", "Kakuna (14)", "Beedrill (15)", "Pidgey (16)", "Pidgeotto (17)", "Pidgeot (18)", "Rattata (19)", "Raticate (20)", "Spearow (21)", "Fearow (22)", "Ekans (23)", "Arbok (24)", "Pikachu (25)", "Raichu (26)", "Sandshrew (27)", "Sandslash (28)", "Nidoranf (29)", "Nidorina (30)", "Nidoqueen (31)", "Nidoranm (32)", "Nidorino (33)", "Nidoking (34)", "Clefairy (35)", "Clefable (36)", "Vulpix (37)", "Ninetales (38)", "Jigglypuff (39)", "Wigglytuff (40)", "Zubat (41)", "Golbat (42)", "Oddish (43)", "Gloom (44)", "Vileplume (45)", "Paras (46)", "Parasect (47)", "Venonat (48)", "Venomoth (49)", "Diglett (50)", "Dugtrio (51)", "Meowth (52)", "Persian (53)", "Psyduck (54)", "Golduck (55)", "Mankey (56)", "Primeape (57)", "Growlithe (58)", "Arcanine (59)", "Poliwag (60)", "Poliwhirl (61)", "Poliwrath (62)", "Abra (63)", "Kadabra (64)", "Alakazam (65)", "Machop (66)", "Machoke (67)", "Machamp (68)", "Bellsprout (69)", "Weepinbell (70)", "Victreebel (71)", "Tentacool (72)", "Tentacruel (73)", "Geodude (74)", "Graveler (75)", "Golem (76)", "Ponyta (77)", "Rapidash (78)", "Slowpoke (79)", "Slowbro (80)", "Magnemite (81)", "Magneton (82)", "Farfetch'd (83)", "Doduo (84)", "Dodrio (85)", "Seel (86)", "Dewgong (87)", "Grimer (88)", "Muk (89)", "Shellder (90)", "Cloyster (91)", "Gastly (92)", "Haunter (93)", "Gengar (94)", "Onix (95)", "Drowzee (96)", "Hypno (97)", "Krabby (98)", "Kingler (99)", "Voltorb (100)", "Electrode (101)", "Exeggcute (102)", "Exeggutor (103)", "Cubone (104)", "Marowak (105)", "Hitmonlee (106)", "Hitmonchan (107)", "Lickitung (108)", "Koffing (109)", "Weezing (110)", "Rhyhorn (111)", "Rhydon (112)", "Chansey (113)", "Tangela (163)", "Kangaskhan (115)", "Horsea (116)", "Seadra (117)", "Goldeen (118)", "Seaking (119)", "Staryu (120)", "Starmie (121)", "Mr. Mime (122)", "Scyther (123)", "Jynx (124)", "Electabuzz (125)", "Magmar (126)", "Pinsir (127)", "Tauros (128)", "Magikarp (129)", "Gyarados (130)", "Lapras (131)", "Ditto (132)", "Eevee (133)", "Vaporeon (134)", "Jolteon (135)", "Flareon (136)", "Porygon (137)", "Omanyte (138)", "Omastar (139)", "Kabuto (140)", "Kabutops (141)", "Aerodactyl (142)", "Snorlax (143)", "Articuno (144)", "Zapdos (145)", "Moltres (146)", "Dratini (147)", "Dragonair (148)", "Dragonite (149)", "Mewtwo (150)", "Mew (151)", "Chikorita (152)", "Bayleef (153)", "Meganium (154)", "Cyndaquil (155)", "Quilava (156)", "Typhlosion (163)", "Totodile (158)", "Croconaw (159)", "Feraligatr (160)", "Sentret (161)", "Furret (162)", "Hoothoot (163)", "Noctowl (164)", "Ledyba (165)", "Ledian (166)", "Spinarak (167)", "Ariados (168)", "Crobat (169)", "Chinchou (170)", "Lanturn (171)", "Pichu (172)", "Cleffa (173)", "Igglybuff (174)", "Togepi (175)", "Togetic (176)", "Natu (177)", "Xatu (178)", "Mareep (179)", "Flaaffy (180)", "Ampharos (181)", "Bellossom (182)", "Marill (183)", "Azumarill (184)", "Sudowoodo (185)", "Politoed (186)", "Hoppip (187)", "Skiploom (188)", "Jumpluff (189)", "Aipom (190)", "Sunkern (191)", "Sunflora (192)", "Yanma (193)", "Wooper (194)", "Quagsire (195)", "Espeon (196)", "Umbreon (197)", "Murkrow (198)", "Slowking (199)", "Misdreavus (200)", "Unown (201)", "Wobbuffet (202)", "Girafarig (203)", "Pineco (204)", "Forretress (205)", "Dunsparce (206)", "Gligar (207)", "Steelix (208)", "Snubbull (209)", "Granbull (210)", "Qwilfish (211)", "Scizor (212)", "Shuckle (213)", "Heracross (214)", "Sneasel (215)", "Teddiursa (216)", "Ursaring (217)", "Slugma (218)", "Magcargo (219)", "Swinub (220)", "Piloswine (221)", "Corsola (222)", "Remoraid (223)", "Octillery (224)", "Delibird (225)", "Mantine (226)", "Skarmory (227)", "Houndour (228)", "Houndoom (229)", "Kingdra (230)", "Phanpy (231)", "Donphan (232)", "Porygon2 (233)", "Stantler (234)", "Smeargle (235)", "Tyrogue (236)", "Hitmontop (237)", "Smoochum (238)", "Elekid (239)", "Magby (240)", "Miltank (241)", "Blissey (242)", "Raikou (243)", "Entei (244)", "Suicune (245)", "Larvitar (246)", "Pupitar (247)", "Tyranitar (248)", "Lugia (249)", "Ho-oh (250)", "Celebi (251)", "? (252)", "? (253)", "? (254)", "? (255)", "? (256)", "? (257)", "? (258)", "? (259)", "? (260)", "? (261)", "? (262)", "? (263)", "? (264)", "? (265)", "? (266)", "? (267)", "? (268)", "? (269)", "? (270)", "? (271)", "? (272)", "? (273)", "? (274)", "? (275)", "? (276)", "Treecko (277)", "Grovyle (278)", "Sceptile (279)", "Torchic (280)", "Combusken (281)", "Blaziken (282)", "Mudkip (283)", "Marshtomp (284)", "Swampert (285)", "Poochyena (286)", "Mightyena (287)", "Zigzagoon (288)", "Linoone (289)", "Wurmple (290)", "Silcoon (291)", "Beautifly (292)", "Cascoon (293)", "Dustox (294)", "Lotad (295)", "Lombre (296)", "Ludicolo (297)", "Seedot (298)", "Nuzleaf (299)", "Shiftry (300)", "Nincada (301)", "Ninjask (302)", "Shedinja (303)", "Taillow (304)", "Swellow (305)", "Shroomish (306)", "Breloom (307)", "Spinda (308)", "Wingull (309)", "Pelipper (310)", "Surskit (311)", "Masquerain (312)", "Wailmer (313)", "Wailord (314)", "Skitty (315)", "Delcatty (316)", "Kecleon (317)", "Baltoy (318)", "Claydol (319)", "Nosepass (320)", "Torkoal (321)", "Sableye (322)", "Barboach (323)", "Whiscash (324)", "Luvdisc (325)", "Corphish (326)", "Crawdaunt (327)", "Feebas (328)", "Milotic (329)", "Carvanha (330)", "Sharpedo (331)", "Trapinch (332)", "Vibrava (333)", "Flygon (334)", "Makuhita (335)", "Hariyama (336)", "Electrike (337)", "Manectric (338)", "Numel (339)", "Camerupt (340)", "Spheal (341)", "Sealeo (342)", "Walrein (343)", "Cacnea (344)", "Cacturne (345)", "Snorunt (346)", "Glalie (347)", "Lunatone (348)", "Solrock (349)", "Azurill (350)", "Spoink (351)", "Grumpig (352)", "Plusle (353)", "Minun (354)", "Mawile (355)", "Meditite (356)", "Medicham (357)", "Swablu (358)", "Altaria (359)", "Wynaut (360)", "Duskull (361)", "Dusclops (362)", "Roselia (363)", "Slakoth (364)", "Vigoroth (365)", "Slaking (366)", "Gulpin (367)", "Swalot (368)", "Tropius (369)", "Whismur (370)", "Loudred (371)", "Exploud (372)", "Clamperl (373)", "Huntail (374)", "Gorebyss (375)", "Absol (376)", "Shuppet (377)", "Banette (378)", "Seviper (379)", "Zangoose (380)", "Relicanth (381)", "Aron (382)", "Lairon (383)", "Aggron (384)", "Castform (385)", "Volbeat (386)", "Illumise (387)", "Lileep (388)", "Cradily (389)", "Anorith (390)", "Armaldo (391)", "Ralts (392)", "Kirlia (393)", "Gardevoir (394)", "Bagon (395)", "Shelgon (396)", "Salamence (397)", "Beldum (398)", "Metang (399)", "Metagross (400)", "Regirock (401)", "Regice (402)", "Registeel (403)", "Kyogre (404)", "Groudon (405)", "Rayquaza (406)", "Latias (407)", "Latios (408)", "Jirachi (409)", "Deoxys (410)", "Chimecho (411)", "- (412)" ]
pokedex_rs = ["#000 ?????","#001 Bulbasaur","#002 Ivysaur","#003 Venusaur","#004 Charmander","#005 Charmeleon","#006 Charizard","#007 Squirtle","#008 Wartortle","#009 Blastoise","#010 Caterpie","#011 Metapod","#012 Butterfree","#013 Weedle","#014 Kakuna","#015 Beedrill","#016 Pidgey","#017 Pidgeotto","#018 Pidgeot","#019 Rattata","#020 Raticate","#021 Spearow","#022 Fearow","#023 Ekans","#024 Arbok","#025 Pikachu","#026 Raichu","#027 Sandshrew","#028 Sandslash","#029 Nidoran?","#030 Nidorina","#031 Nidoqueen","#032 Nidoran?","#033 Nidorino","#034 Nidoking","#035 Clefairy","#036 Clefable","#037 Vulpix","#038 Ninetales","#039 Jigglypuff","#040 Wigglytuff","#041 Zubat","#042 Golbat","#043 Oddish","#044 Gloom","#045 Vileplume","#046 Paras","#047 Parasect","#048 Venonat","#049 Venomoth","#050 Diglett","#051 Dugtrio","#052 Meowth","#053 Persian","#054 Psyduck","#055 Golduck","#056 Mankey","#057 Primeape","#058 Growlithe","#059 Arcanine","#060 Poliwag","#061 Poliwhirl","#062 Poliwrath","#063 Abra","#064 Kadabra","#065 Alakazam","#066 Machop","#067 Machoke","#068 Machamp","#069 Bellsprout","#070 Weepinbell","#071 Victreebel","#072 Tentacool","#073 Tentacruel","#074 Geodude","#075 Graveler","#076 Golem","#077 Ponyta","#078 Rapidash","#079 Slowpoke","#080 Slowbro","#081 Magnemite","#082 Magneton","#083 Farfetch'd","#084 Doduo","#085 Dodrio","#086 Seel","#087 Dewgong","#088 Grimer","#089 Muk","#090 Shellder","#091 Cloyster","#092 Gastly","#093 Haunter","#094 Gengar","#095 Onix","#096 Drowzee","#097 Hypno","#098 Krabby","#099 Kingler","#100 Voltorb","#101 Electrode","#102 Exeggcute","#103 Exeggutor","#104 Cubone","#105 Marowak","#106 Hitmonlee","#107 Hitmonchan","#108 Lickitung","#109 Koffing","#110 Weezing","#111 Rhyhorn","#112 Rhydon","#113 Chansey","#163 Tangela","#115 Kangaskhan","#116 Horsea","#117 Seadra","#118 Goldeen","#119 Seaking","#120 Staryu","#121 Starmie","#122 Mr. Mime","#123 Scyther","#124 Jynx","#125 Electabuzz","#126 Magmar","#127 Pinsir","#128 Tauros","#129 Magikarp","#130 Gyarados","#131 Lapras","#132 Ditto","#133 Eevee","#134 Vaporeon","#135 Jolteon","#136 Flareon","#137 Porygon","#138 Omanyte","#139 Omastar","#140 Kabuto","#141 Kabutops","#142 Aerodactyl","#143 Snorlax","#144 Articuno","#145 Zapdos","#146 Moltres","#147 Dratini","#148 Dragonair","#149 Dragonite","#150 Mewtwo","#151 Mew","#152 Chikorita","#153 Bayleef","#154 Meganium","#155 Cyndaquil","#156 Quilava","#163 Typhlosion","#158 Totodile","#159 Croconaw","#160 Feraligatr","#161 Sentret","#162 Furret","#163 Hoothoot","#164 Noctowl","#165 Ledyba","#166 Ledian","#167 Spinarak","#168 Ariados","#169 Crobat","#170 Chinchou","#171 Lanturn","#172 Pichu","#173 Cleffa","#174 Igglybuff","#175 Togepi","#176 Togetic","#177 Natu","#178 Xatu","#179 Mareep","#180 Flaaffy","#181 Ampharos","#182 Bellossom","#183 Marill","#184 Azumarill","#185 Sudowoodo","#186 Politoed","#187 Hoppip","#188 Skiploom","#189 Jumpluff","#190 Aipom","#191 Sunkern","#192 Sunflora","#193 Yanma","#194 Wooper","#195 Quagsire","#196 Espeon","#197 Umbreon","#198 Murkrow","#199 Slowking","#200 Misdreavus","#201 Unown","#202 Wobbuffet","#203 Girafarig","#204 Pineco","#205 Forretress","#206 Dunsparce","#207 Gligar","#208 Steelix","#209 Snubbull","#210 Granbull","#211 Qwilfish","#212 Scizor","#213 Shuckle","#214 Heracross","#215 Sneasel","#216 Teddiursa","#217 Ursaring","#218 Slugma","#219 Magcargo","#220 Swinub","#221 Piloswine","#222 Corsola","#223 Remoraid","#224 Octillery","#225 Delibird","#226 Mantine","#227 Skarmory","#228 Houndour","#229 Houndoom","#230 Kingdra","#231 Phanpy","#232 Donphan","#233 Porygon2","#234 Stantler","#235 Smeargle","#236 Tyrogue","#237 Hitmontop","#238 Smoochum","#239 Elekid","#240 Magby","#241 Miltank","#242 Blissey","#243 Raikou","#244 Entei","#245 Suicune","#246 Larvitar","#247 Pupitar","#248 Tyranitar","#249 Lugia","#250 Ho-oh","#251 Celebi","#252 Treecko","#253 Grovyle","#254 Sceptile","#255 Torchic","#256 Combusken","#257 Blaziken","#258 Mudkip","#259 Marshtomp","#260 Swampert","#261 Poochyena","#262 Mightyena","#263 Zigzagoon","#264 Linoone","#265 Wurmple","#266 Silcoon","#267 Beautifly","#268 Cascoon","#269 Dustox","#270 Lotad","#271 Lombre","#272 Ludicolo","#273 Seedot","#274 Nuzleaf","#275 Shiftry","#276 Taillow","#277 Swellow","#278 Wingull","#279 Pelipper","#280 Ralts","#281 Kirlia","#282 Gardevoir","#283 Surskit","#284 Masquerain","#285 Shroomish","#286 Breloom","#287 Slakoth","#288 Vigoroth","#289 Slaking","#290 Nincada","#291 Ninjask","#292 Shedinja","#293 Whismur","#294 Loudred","#295 Exploud","#296 Makuhita","#297 Hariyama","#298 Azurill","#299 Nosepass","#300 Skitty","#301 Delcatty","#302 Sableye","#303 Mawile","#304 Aron","#305 Lairon","#306 Aggron","#307 Meditite","#308 Medicham","#309 Electrike","#310 Manectric","#311 Plusle","#312 Minun","#313 Volbeat","#314 Illumise","#315 Roselia","#316 Gulpin","#317 Swalot","#318 Carvanha","#319 Sharpedo","#320 Wailmer","#321 Wailord","#322 Numel","#323 Camerupt","#324 Torkoal","#325 Spoink","#326 Grumpig","#327 Spinda","#328 Trapinch","#329 Vibrava","#330 Flygon","#331 Cacnea","#332 Cacturne","#333 Swablu","#334 Altaria","#335 Zangoose","#336 Seviper","#337 Lunatone","#338 Solrock","#339 Barboach","#340 Whiscash","#341 Corphish","#342 Crawdaunt","#343 Baltoy","#344 Claydol","#345 Lileep","#346 Cradily","#347 Anorith","#348 Armaldo","#349 Feebas","#350 Milotic","#351 Castform","#352 Kecleon","#353 Shuppet","#354 Banette","#355 Duskull","#356 Dusclops","#357 Tropius","#358 Chimecho","#359 Absol","#360 Wynaut","#361 Snorunt","#362 Glalie","#363 Spheal","#364 Sealeo","#365 Walrein","#366 Clamperl","#367 Huntail","#368 Gorebyss","#369 Relicanth","#370 Luvdisc","#371 Bagon","#372 Shelgon","#373 Salamence","#374 Beldum","#375 Metang","#376 Metagross","#377 Regirock","#378 Regice","#379 Registeel","#380 Latias","#381 Latios","#382 Kyogre","#383 Groudon","#384 Rayquaza","#385 Jirachi","#386 Deoxys"]
moves_rs = ["-- No Move -- (0)", "Pound (1)", "Karate Chop (2)", "Doubleslap (3)", "Comet Punch (4)", "Mega Punch (5)", "Pay Day (6)", "Fire Punch (7)", "Ice Punch (8)", "Thunderpunch (9)", "Scratch (10)", "Vicegrip (11)", "Guillotine (12)", "Razor Wind (13)", "Swords Dance (14)", "Cut (15)", "Gust (16)", "Wing Attack (17)", "Whirlwind (18)", "Fly (19)", "Bind (20)", "Slam (21)", "Vine Whip (22)", "Stomp (23)", "Double Kick (24)", "Mega Kick (25)", "Jump Kick (26)", "Rolling Kick (27)", "Sand-attack (28)", "Headbutt (29)", "Horn Attack (30)", "Fury Attack (31)", "Horn Drill (32)", "Tackle (33)", "Body Slam (34)", "Wrap (35)", "Take Down (36)", "Thrash (37)", "Double-edge (38)", "Tail Whip (39)", "Poison Sting (40)", "Twineedle (41)", "Pin Missile (42)", "Leer (43)", "Bite (44)", "Growl (45)", "Roar (46)", "Sing (47)", "Supersonic (48)", "Sonicboom (49)", "Disable (50)", "Acid (51)", "Ember (52)", "Flamethrower (53)", "Mist (54)", "Water Gun (55)", "Hydro Pump (56)", "Surf (57)", "Ice Beam (58)", "Blizzard (59)", "Psybeam (60)", "Bubblebeam (61)", "Aurora Beam (62)", "Hyper Beam (63)", "Peck (64)", "Drill Peck (65)", "Submission (66)", "Low Kick (67)", "Counter (68)", "Seismic Toss (69)", "Strength (70)", "Absorb (71)", "Mega Drain (72)", "Leech Seed (73)", "Growth (74)", "Razor Leaf (75)", "Solarbeam (76)", "Poisonpowder (77)", "Stun Spore (78)", "Sleep Powder (79)", "Petal Dance (80)", "String Shot (81)", "Dragon Rage (82)", "Fire Spin (83)", "Thundershock (84)", "Thunderbolt (85)", "Thunder Wave (86)", "Thunder (87)", "Rock Throw (88)", "Earthquake (89)", "Fissure (90)", "Dig (91)", "Toxic (92)", "Confusion (93)", "Psychic (94)", "Hypnosis (95)", "Meditate (96)", "Agility (97)", "Quick Attack (98)", "Rage (99)", "Teleport (100)", "Night Shade (101)", "Mimic (102)", "Screech (103)", "Double Team (104)", "Recover (105)", "Harden (106)", "Minimize (107)", "Smokescreen (108)", "Confuse Ray (109)", "Withdraw (110)", "Defense Curl (111)", "Barrier (112)", "Light Screen (113)", "Haze (163)", "Reflect (115)", "Focus Energy (116)", "Bide (117)", "Metronome (118)", "Mirror Move (119)", "Selfdestruct (120)", "Egg Bomb (121)", "Lick (122)", "Smog (123)", "Sludge (124)", "Bone Club (125)", "Fire Blast (126)", "Waterfall (127)", "Clamp (128)", "Swift (129)", "Skull Bash (130)", "Spike Cannon (131)", "Constrict (132)", "Amnesia (133)", "Kinesis (134)", "Softboiled (135)", "Hi Jump Kick (136)", "Glare (137)", "Dream Eater (138)", "Poison Gas (139)", "Barrage (140)", "Leech Life (141)", "Lovely Kiss (142)", "Sky Attack (143)", "Transform (144)", "Bubble (145)", "Dizzy Punch (146)", "Spore (147)", "Flash (148)", "Psywave (149)", "Splash (150)", "Acid Armor (151)", "Crabhammer (152)", "Explosion (153)", "Fury Swipes (154)", "Bonemerang (155)", "Rest (156)", "Rock Slide (163)", "Hyper Fang (158)", "Sharpen (159)", "Conversion (160)", "Tri Attack (161)", "Super Fang (162)", "Slash (163)", "Substitute (164)", "Struggle (165)", "Sketch (166)", "Triple Kick (167)", "Thief (168)", "Spider Web (169)", "Mind Reader (170)", "Nightmare (171)", "Flame Wheel (172)", "Snore (173)", "Curse (174)", "Flail (175)", "Conversion 2 (176)", "Aeroblast (177)", "Cotton Spore (178)", "Reversal (179)", "Spite (180)", "Powder Snow (181)", "Protect (182)", "Mach Punch (183)", "Scary Face (184)", "Faint Attack (185)", "Sweet Kiss (186)", "Belly Drum (187)", "Sludge Bomb (188)", "Mud-slap (189)", "Octazooka (190)", "Spikes (191)", "Zap Cannon (192)", "Foresight (193)", "Destiny Bond (194)", "Perish Song (195)", "Icy Wind (196)", "Detect (197)", "Bone Rush (198)", "Lock-on (199)", "Outrage (200)", "Sandstorm (201)", "Giga Drain (202)", "Endure (203)", "Charm (204)", "Rollout (205)", "False Swipe (206)", "Swagger (207)", "Milk Drink (208)", "Spark (209)", "Fury Cutter (210)", "Steel Wing (211)", "Mean Look (212)", "Attract (213)", "Sleep Talk (214)", "Heal Bell (215)", "Return (216)", "Present (217)", "Frustration (218)", "Safeguard (219)", "Pain Split (220)", "Sacred Fire (221)", "Magnitude (222)", "Dynamicpunch (223)", "Megahorn (224)", "Dragonbreath (225)", "Baton Pass (226)", "Encore (227)", "Pursuit (228)", "Rapid Spin (229)", "Sweet Scent (230)", "Iron Tail (231)", "Metal Claw (232)", "Vital Throw (233)", "Morning Sun (234)", "Synthesis (235)", "Moonlight (236)", "Hidden Power (237)", "Cross Chop (238)", "Twister (239)", "Rain Dance (240)", "Sunny Day (241)", "Crunch (242)", "Mirror Coat (243)", "Psych Up (244)", "Extremespeed (245)", "Ancientpower (246)", "Shadow Ball (247)", "Future Sight (248)", "Rock Smash (249)", "Whirlpool (250)", "Beat Up (251)", "Fake Out (252)", "Uproar (253)", "Stockpile (254)", "Spit Up (255)", "Swallow (256)", "Heat Wave (257)", "Hail (258)", "Torment (259)", "Flatter (260)", "Will-o-wisp (261)", "Memento (262)", "Facade (263)", "Focus Punch (264)", "Smellingsalt (265)", "Follow Me (266)", "Nature Power (267)", "Charge (268)", "Taunt (269)", "Helping Hand (270)", "Trick (271)", "Role Play (272)", "Wish (273)", "Assist (274)", "Ingrain (275)", "Superpower (276)", "Magic Coat (277)", "Recycle (278)", "Revenge (279)", "Brick Break (280)", "Yawn (281)", "Knock Off (282)", "Endeavor (283)", "Eruption (284)", "Skill Swap (285)", "Imprison (286)", "Refresh (287)", "Grudge (288)", "Snatch (289)", "Secret Power (290)", "Dive (291)", "Arm Thrust (292)", "Camouflage (293)", "Tail Glow (294)", "Luster Purge (295)", "Mist Ball (296)", "Featherdance (297)", "Teeter Dance (298)", "Blaze Kick (299)", "Mud Sport (300)", "Ice Ball (301)", "Needle Arm (302)", "Slack Off (303)", "Hyper Voice (304)", "Poison Fang (305)", "Crush Claw (306)", "Blast Burn (307)", "Hydro Cannon (308)", "Meteor Mash (309)", "Astonish (310)", "Weather Ball (311)", "Aromatherapy (312)", "Fake Tears (313)", "Air Cutter (314)", "Overheat (315)", "Odor Sleuth (316)", "Rock Tomb (317)", "Silver Wind (318)", "Metal Sound (319)", "Grasswhistle (320)", "Tickle (321)", "Cosmic Power (322)", "Water Spout (323)", "Signal Beam (324)", "Shadow Punch (325)", "Extrasensory (326)", "Sky Uppercut (327)", "Sand Tomb (328)", "Sheer Cold (329)", "Muddy Water (330)", "Bullet Seed (331)", "Aerial Ace (332)", "Icicle Spear (333)", "Iron Defense (334)", "Block (335)", "Howl (336)", "Dragon Claw (337)", "Frenzy Plant (338)", "Bulk Up (339)", "Bounce (340)", "Mud Shot (341)", "Poison Tail (342)", "Covet (343)", "Volt Tackle (344)", "Magical Leaf (345)", "Water Sport (346)", "Calm Mind (347)", "Leaf Blade (348)", "Dragon Dance (349)", "Rock Blast (350)", "Shock Wave (351)", "Water Pulse (352)", "Doom Desire (353)", "Psycho Boost (354)"]
types_rs = ["Normal (0)", "Fighting (1)", "Flying (2)", "Poison (3)", "Ground (4)", "Rock (5)", "Bird (6)", "Bug (7)", "Ghost (8)", "Steel (9)", "~10", "~11", "~12", "~13", "~14", "~15", "~16", "~17", "~18", "~19", "Fire (20)", "Water (21)", "Grass (22)", "Electric (23)", "Psychic (24)", "Ice (25)", "Dragon (26)", "Dark (27)", "~28", "~29", "~30", "~31", "~32", "~33", "~34", "~35", "~36", "~37", "~38", "~39", "~40", "~41", "~42", "~43", "~44", "~45", "~46", "~47", "~48", "~49", "~50", "~51", "~52", "~53", "~54", "~55", "~56", "~57", "~58", "~59", "~60", "~61", "~62", "~63", "~64", "~65", "~66", "~67", "~68", "~69", "~70", "~71", "~72", "~73", "~74", "~75", "~76", "~77", "~78", "~79", "~80", "~81", "~82", "~83", "~84", "~85", "~86", "~87", "~88", "~89", "~90", "~91", "~92", "~93", "~94", "~95", "~96", "~97", "~98", "~99", "~100", "~101", "~102", "~103", "~104", "~105", "~106", "~107", "~108", "~109", "~110", "~111", "~112", "~113", "~163", "~115", "~116", "~117", "~118", "~119", "~120", "~121", "~122", "~123", "~124", "~125", "~126", "~127", "~128", "~129", "~130", "~131", "~132", "~133", "~134", "~135", "~136", "~137", "~138", "~139", "~140", "~141", "~142", "~143", "~144", "~145", "~146", "~147", "~148", "~149", "~150", "~151", "~152", "~153", "~154", "~155", "~156", "~163", "~158", "~159", "~160", "~161", "~162", "~163", "~164", "~165", "~166", "~167", "~168", "~169", "~170", "~171", "~172", "~173", "~174", "~175", "~176", "~177", "~178", "~179", "~180", "~181", "~182", "~183", "~184", "~185", "~186", "~187", "~188", "~189", "~190", "~191", "~192", "~193", "~194", "~195", "~196", "~197", "~198", "~199", "~200", "~201", "~202", "~203", "~204", "~205", "~206", "~207", "~208", "~209", "~210", "~211", "~212", "~213", "~214", "~215", "~216", "~217", "~218", "~219", "~220", "~221", "~222", "~223", "~224", "~225", "~226", "~227", "~228", "~229", "~230", "~231", "~232", "~233", "~234", "~235", "~236", "~237", "~238", "~239", "~240", "~241", "~242", "~243", "~244", "~245", "~246", "~247", "~248", "~249", "~250", "~251", "~252", "~253", "~254", "~255"]



items = None
pokemon = None
pokedex = None
moves = None
types = None

class PikaSav():
             
             
    def repair_rby(self):
        global items
        global pokemon
        global pokedex
        global moves
        global types
        file = askopenfilename(filetypes = [ ("R/B/Y SaveGame",".sav") ])
        if (file):
            sav=RBSav(file,True)
            self.gen = 1
            self.bn = 12
            self.root.title(self.title + " - Red/Blue/Yellow")
            items = items_rb[:]
            pokemon = pokemon_rb[:]
            pokedex = pokedex_rb[:]
            moves = moves_rb[:]
            types = types_rb[:]    
            self.sav = sav           
            self.show_data()
            self.close_frames()
            
    def repair_gs(self):
        global items
        global pokemon
        global pokedex
        global moves
        global types
        file = askopenfilename(filetypes = [ ("G/S SaveGame",".sav") ])
        if (file):
            sav=GSSav(file,True)
            items = items_gs[:]
            pokemon = pokemon_gs[:]
            pokedex = pokedex_gs[:]
            moves = moves_gs[:]
            types = types_gs[:]
            self.gen = 2
            self.bn = 14
            self.root.title(self.title + " - Gold/Silver")
            self.sav = sav           
            self.show_data()
            self.close_frames()
        
    def repair_cr(self):
        global items
        global pokemon
        global pokedex
        global moves
        global types
        file = askopenfilename(filetypes = [ ("Crystal SaveGame",".sav") ])
        if (file):
            sav=CRSav(file,True)
            items = items_gs[:]
            pokemon = pokemon_gs[:]
            pokedex = pokedex_gs[:]
            moves = moves_gs[:]
            types = types_gs[:]
            self.gen = 2
            self.bn = 14
            self.root.title(self.title + " - Crystal")
            self.sav = sav           
            self.show_data()
            self.close_frames()
    
    def repair_rs(self):
        global items
        global pokemon
        global pokedex
        global moves
        global types
        file = askopenfilename(filetypes = [ ("Ruby/Sapphire SaveGame",".sav") ])
        if (file):
            sav=RSSav(file,1)
            items = items_rs[:]
            pokemon = pokemon_rs[:]
            pokedex = pokedex_rs[:]
            moves = moves_rs[:]
            types = types_rs[:]
            self.gen = 3
            self.bn = 14
            self.root.title(self.title + " - Ruby/Sapphire")
            self.sav = sav
            self.show_data()
            self.close_frames()
        
            
    def open_sav(self):
        global items
        global pokemon
        global pokedex
        global moves
        global types
        
        file = askopenfilename(filetypes = [ ("RBY/GS/Cr/RS SaveGame",".sav"),("All files","*.*") ])
        if (file):
            sav = RSSav(file)
            if not sav.ok:
                sav = CRSav(file)
                if not sav.ok:
                    sav=GSSav(file)
                    if not sav.ok:
                        sav=RBSav(file)
                        if not sav.ok:
                            showerror("Something went wrong =(","The .sav is corrupted or not supported by this program.\nIn case of corruption, use the 'File -> Force SAV' function.")
                            return False;
                        else:
                            self.gen = 1
                            self.bn = 12
                            self.root.title(self.title + " - Red/Blue/Yellow")
                            items = items_rb[:]
                            pokemon = pokemon_rb[:]
                            pokedex = pokedex_rb[:]
                            moves = moves_rb[:]
                            types = types_rb[:]
                    else:
                        items = items_gs[:]
                        pokemon = pokemon_gs[:]
                        pokedex = pokedex_gs[:]
                        moves = moves_gs[:]
                        types = types_gs[:]
                        self.gen = 2
                        self.bn = 14
                        self.root.title(self.title + " - Gold/Silver")
                else:
                    items = items_gs[:]
                    pokemon = pokemon_gs[:]
                    pokedex = pokedex_gs[:]
                    moves = moves_gs[:]
                    types = types_gs[:]
                    self.gen = 2
                    self.bn = 14
                    self.root.title(self.title + " - Crystal")
            else:
                items = items_rs[:]
                pokemon = pokemon_rs[:]
                pokedex = pokedex_rs[:]
                moves = moves_rs[:]
                types = types_rs[:]
                self.gen = 3
                self.bn = 14
                self.root.title(self.title + " - Ruby/Sapphire")
                    
            self.sav = sav           
            self.show_data()
            self.close_frames()
            
    def save_sav(self):
        if (self.sav != None):
            self.store_changes()
            self.sav.save()
        else:
            showerror("Something went wrong =(","You need to load a .sav first")
     
    def saveas_sav(self):
        if (self.sav != None):
            self.store_changes()
            file = asksaveasfilename(filetypes = [ ("RBY/GS/Cr SaveGame",".sav") ])
            
            if (file):
                self.sav.saveas(file)
        else:
            showerror("Something went wrong =(","You need to load a .sav first")
    
    def store_changes(self):
        if (self.trname.get() != self.sav.name): self.sav.set("name",self.trname.get())
        if (self.rivalname.get() != self.sav.rivalname): self.sav.set("rivalname",self.rivalname.get())
        self.sav.set("money",self.money.get())
        self.sav.set("chips",self.chips.get())
        self.sav.set("hours",self.hours.get())
        self.sav.set("minutes",self.minutes.get())
        self.sav.set("seconds",self.seconds.get())
        self.store_items()
        self.store_pcitems()
        self.store_pokedex1()
        self.store_pokedex2()
        self.store_pokemon()
        self.store_pokeedit()
        self.store_boxedit()
        self.sav.refresh()
                    
    def show_data(self):
        self.bp = 20
        if self.gen == 3:
            self.bp = 30
        self.trname.delete(0,END);
        self.trname.insert(0,self.sav.name);
        self.rivalname.delete(0,END);
        self.rivalname.insert(0,self.sav.rivalname);
        self.money.delete(0,END);
        self.money.insert(0,self.sav.money);
        self.chips.delete(0,END);
        self.chips.insert(0,self.sav.chips);
        self.hours.delete(0,END);
        self.hours.insert(0,self.sav.hours);
        self.minutes.delete(0,END);
        self.minutes.insert(0,self.sav.minutes);
        self.seconds.delete(0,END);
        self.seconds.insert(0,self.sav.seconds);
        
    def add_menus(self):
        menu = Menu(self.root)
        menu_repair = Menu(menu,tearoff=0)
        menu_repair.add_command(label="Red/Blue/Yellow",command=self.repair_rby)
        menu_repair.add_command(label="Gold/Silver",command=self.repair_gs)
        menu_repair.add_command(label="Crystal",command=self.repair_cr)
        menu_repair.add_command(label="Ruby/Sapphire",command=self.repair_rs)
        
        menu_file = Menu(menu,tearoff=0)
        menu_file.add_command(label="Open SAV",command=self.open_sav)
        menu_file.add_separator()
        menu_file.add_command(label="Save SAV",command=self.save_sav)
        menu_file.add_command(label="Save SAV As..",command=self.saveas_sav)
        menu_file.add_separator()
        menu_file.add_cascade(label="Force SAV",menu=menu_repair)
        menu_file.add_separator()
        menu_file.add_command(label="Exit",command=self.exit)
        menu.add_cascade(label="File",menu=menu_file)    
        menu_help = Menu(menu,tearoff=0)
        menu_help.add_command(label="SAV Info",command=self.show_savinfo)
        menu_help.add_separator()
        menu_help.add_command(label="About",command=self.show_about)
        menu.add_cascade(label="Help",menu=menu_help)
        self.root.configure(menu=menu)

    
    def add_fields(self):
        
        self.frame.grid_forget()
        
        Label(self.root,text="   ").grid(row=1000,column=1000)
        
        Label(text="").grid(row=0)
        Label(text="      Trainer Name:  ",anchor=W).grid(row=1,sticky=W)
        self.trname = Entry()
        self.trname.grid(row=1,column=1)
        
        Label(text="      Rival Name:  ").grid(row=1,column=2,sticky=W)
        self.rivalname = Entry()
        self.rivalname.grid(row=1,column=3)
        
        Label(text="      Money:  ").grid(row=2,column=0,sticky=W)
        self.money = Entry()
        self.money.grid(row=2,column=1)
        
        Label(text="      Casino Chips:  ").grid(row=2,column=2,sticky=W)
        self.chips = Entry()
        self.chips.grid(row=2,column=3)
        Label(text="      h/m/s Played  ").grid(row=3,column=0,sticky=W)
        self.hours = Entry(width=5)
        self.hours.grid(row=3,column=1,sticky=W)
        self.minutes = Entry(width=5)
        self.minutes.grid(row=3,column=1)
        self.seconds = Entry(width=5)
        self.seconds.grid(row=3,column=1,sticky=E)
        Label(text="").grid(row=4)
        Button(text="Pokémon",width=10,command=self.show_pokemon).grid(row=5)
        Label(text="Edit the Pokémon from the party.").grid(row=5,column=1,sticky=W,columnspan=3)
        Label(text="",font=("Times",4)).grid(row=6)
        Button(text="PC Pokémon",width=10,command=self.show_boxes).grid(row=7)
        Label(text="Edit the Pokémon stored at Bill's PC.").grid(row=7,column=1,sticky=W,columnspan=3)
        Label(text="",font=("Times",4)).grid(row=8)
        Button(text="Bag Items",width=10,command=self.show_items).grid(row=9)
        Label(text="Change the class or quantity of every item in the bag.").grid(row=9,column=1,sticky=W,columnspan=3)
        Label(text="",font=("Times",4)).grid(row=10)
        Button(text="PC Items",width=10,command=self.show_pcitems).grid(row=11)
        Label(text="Change the class or quantity of every item in the PC.").grid(row=11,column=1,sticky=W,columnspan=3)
        Label(text="",font=("Times",4)).grid(row=12)
        Button(text="Pokedex 1/2",width=10,command=self.show_pokedex1).grid(row=13)
        Label(text="Mark a certain Pokémon as seen or catched at the Pokédex.").grid(row=13,column=1,sticky=W,columnspan=3)
        Label(text="",font=("Times",4)).grid(row=14)
        Button(text="Pokedex 2/2",width=10,command=self.show_pokedex2).grid(row=15)
        Label(text="Mark a certain Pokémon as seen or catched at the Pokédex.").grid(row=15,column=1,sticky=W,columnspan=3)
    
    def show_frame(self):
        self.title = "PikaSav v0.3"
        self.root.title(self.title)
        self.frame = Frame(self.root)
        self.add_fields()
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.frame.mainloop()
    
    def close_frames(self):
        if self.items != None:
            self.items.destroy()
            self.items = None
        if self.pcitems != None:
            self.pcitems.destroy()
            self.pcitems = None
        if self.pokemon != None:
            self.pokemon.destroy()
            self.pokemon = None
        if self.boxes != None:
            self.boxes.destroy()
            self.boxes = None
        if self.boxedit != None:
            self.boxedit.destroy()
            self.boxedit = None
        if self.pokedex1 != None:
            self.pokedex1.destroy()
            self.pokedex1 = None
        if self.pokedex2 != None:
            self.pokedex2.destroy()
            self.pokedex2 = None
        if self.pokeedit != None:
            self.pokeedit.destroy()
            self.pokeedit = None
    
    def exit(self):
        self.close_frames()
        self.root.destroy()
    
    def __init__(self):
        self.gen = 0
        self.root = Tk()
        self.sav = None
        self.pokemon = None
        self.items = None
        self.boxes = None
        self.pokeedit = None
        self.pcpokeedit = None
        self.boxedit = None
        self.pcitems = None
        self.pokedex1 = None
        self.pokedex2 = None
        self.iclass = [None]*163
        self.icount = [None]*163
        self.pciclass = [None]*50
        self.pcicount = [None]*50
        self.dexseen = [None]*387
        self.dexcatched = [None]*387
        self.add_menus()
        self.show_frame()
        return
    
    def save_items(self):
        if self.items != None:
            for i in range(20):
                self.sav.items[i][1]=self.icount[i]
    
    def show_items(self):
        global items
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.items != None:
            return
        self.items = Toplevel()
        self.items.title("Bag Items - %s" % (self.title))
        self.items.protocol('WM_DELETE_WINDOW', self.wmdel_items)
        Label(self.items,text="   ").grid(row=1000,column=1000)
        Label(self.items,text="Item class").grid(row=0,column=1)
        Label(self.items,text="Quantity").grid(row=0,column=2)
        array = items*1
        array.sort(reverse=True)
        inum = 20
        if self.gen >= 3: inum = 33
        for i in range(inum):
            iclass = self.sav.items[i][0]
            if (iclass < len(items)): iclass = items[iclass]
            else: iclass = str(iclass)
            icount = self.sav.items[i][1]
            Label(self.items,text="    Item %d" % (i+1)).grid(row=i+1,sticky=W)
            self.iclass[i] = ComboBox(self.items,dropdown=1,editable=1,width=20,value=iclass)
            for t in array:
                self.iclass[i].insert(0,t)
            self.iclass[i].grid(row=i+1,column=1)
            self.icount[i] = Entry(self.items,width=4)
            self.icount[i].insert(0,icount)
            self.icount[i].grid(row=i+1,column=2)
        
        if self.gen >= 3:
            Label(self.items,text="Item class").grid(row=0,column=4)
            Label(self.items,text="Quantity").grid(row=0,column=5)
            for i in range(33,33*2):
                iclass = self.sav.items[i][0]
                if (iclass < len(items)): iclass = items[iclass]
                else: iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items,text="    Item %d" % (i+1)).grid(row=i%33+1,column=3,sticky=W)
                self.iclass[i] = ComboBox(self.items,dropdown=1,editable=1,width=20,value=iclass)
                for t in array:
                    self.iclass[i].insert(0,t)
                self.iclass[i].grid(row=i%33+1,column=4)
                self.icount[i] = Entry(self.items,width=4)
                self.icount[i].insert(0,icount)
                self.icount[i].grid(row=i%33+1,column=5)
        
            Label(self.items,text="Item class").grid(row=0,column=7)
            Label(self.items,text="Quantity").grid(row=0,column=8)
            for i in range(33*2,33*3):
                iclass = self.sav.items[i][0]
                if (iclass < len(items)): iclass = items[iclass]
                else: iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items,text="    Item %d" % (i+1)).grid(row=i%33+1,column=6,sticky=W)
                self.iclass[i] = ComboBox(self.items,dropdown=1,editable=1,width=20,value=iclass)
                for t in array:
                    self.iclass[i].insert(0,t)
                self.iclass[i].grid(row=i%33+1,column=7)
                self.icount[i] = Entry(self.items,width=7)
                self.icount[i].insert(0,icount)
                self.icount[i].grid(row=i%33+1,column=8)
        
            Label(self.items,text="Item class").grid(row=0,column=10)
            Label(self.items,text="Quantity").grid(row=0,column=11)
            for i in range(33*3,33*4):
                iclass = self.sav.items[i][0]
                if (iclass < len(items)): iclass = items[iclass]
                else: iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items,text="    Item %d" % (i+1)).grid(row=i%33+1,column=9,sticky=W)
                self.iclass[i] = ComboBox(self.items,dropdown=1,editable=1,width=20,value=iclass)
                for t in array:
                    self.iclass[i].insert(0,t)
                self.iclass[i].grid(row=i%33+1,column=10)
                self.icount[i] = Entry(self.items,width=7)
                self.icount[i].insert(0,icount)
                self.icount[i].grid(row=i%33+1,column=11)
        
            Label(self.items,text="Item class").grid(row=0,column=13)
            Label(self.items,text="Quantity").grid(row=0,column=14)
            for i in range(33*4,163):
                iclass = self.sav.items[i][0]
                if (iclass < len(items)): iclass = items[iclass]
                else: iclass = str(iclass)
                icount = self.sav.items[i][1]
                Label(self.items,text="    Item %d" % (i+1)).grid(row=i%33+1,column=12,sticky=W)
                self.iclass[i] = ComboBox(self.items,dropdown=1,editable=1,width=20,value=iclass)
                for t in array:
                    self.iclass[i].insert(0,t)
                self.iclass[i].grid(row=i%33+1,column=13)
                self.icount[i] = Entry(self.items,width=7)
                self.icount[i].insert(0,icount)
                self.icount[i].grid(row=i%33+1,column=14)
        
        if self.gen <= 2:    
            Label(self.items,text="    Item # (Set this to number of items)").grid(row=21,columnspan=2,sticky=W)
            self.itemcount = Entry(self.items,width=4)
            self.itemcount.insert(0,str(self.sav.itemcount))
            self.itemcount.grid(row=21,column=2)
        
        return    
    
    def show_pcitems(self):
        global items
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.pcitems != None:
            return
        self.pcitems = Toplevel()
        self.pcitems.title("PC Items - %s" % (self.title))
        self.pcitems.protocol('WM_DELETE_WINDOW', self.wmdel_pcitems)
        Label(self.pcitems,text="   ").grid(row=1000,column=1000)
        Label(self.pcitems,text="Item class").grid(row=0,column=1)
        Label(self.pcitems,text="Quantity").grid(row=0,column=2)
        array = items*1
        array.sort(reverse=True)
        for i in range(25):
            iclass = self.sav.pcitems[i][0]
            if (iclass < len(items)): iclass = items[iclass]
            else: iclass = str(iclass)
            icount = self.sav.pcitems[i][1]
            Label(self.pcitems,text="    Item %d" % (i+1)).grid(row=i+1,sticky=W)
            self.pciclass[i] = ComboBox(self.pcitems,dropdown=1,editable=1,width=20,value=iclass)
            for t in array:
                self.pciclass[i].insert(0,t)
            self.pciclass[i].grid(row=i+1,column=1)
            self.pcicount[i] = Entry(self.pcitems,width=4)
            self.pcicount[i].insert(0,icount)
            self.pcicount[i].grid(row=i+1,column=2)
                    
        Label(self.pcitems,text="Item class").grid(row=0,column=4)
        Label(self.pcitems,text="Quantity").grid(row=0,column=5)
        for i in range(25,50):
            iclass = self.sav.pcitems[i][0]
            if (iclass < len(items)): iclass = items[iclass]
            else: iclass = str(iclass)
            icount = self.sav.pcitems[i][1]
            Label(self.pcitems,text="    Item %d" % (i+1)).grid(row=i%25+1,column=3,sticky=W)
            self.pciclass[i] = ComboBox(self.pcitems,dropdown=1,editable=1,width=20,value=iclass)
            for t in array:
                self.pciclass[i].insert(0,t)
            self.pciclass[i].grid(row=i%25+1,column=4)
            self.pcicount[i] = Entry(self.pcitems,width=4)
            self.pcicount[i].insert(0,icount)
            self.pcicount[i].grid(row=i%25+1,column=5)
        if self.gen <= 2:
            Label(self.pcitems,text="    Item # (Set this to number of items)").grid(row=26,columnspan=2,sticky=W)
            self.pcitemcount = Entry(self.pcitems,width=4)
            self.pcitemcount.insert(0,str(self.sav.pcitemcount))
            self.pcitemcount.grid(row=26,column=2)
        return
    
    def store_items(self):
        if (self.items != None):
            if self.gen <= 2:
                for i in range(20):
                    self.sav.setitem(i,items.index(self.iclass[i]["selection"]),int(self.icount[i].get()))
                self.sav.set("itemcount",self.itemcount.get())
            if self.gen >= 3:
                for i in range(163):
                    self.sav.setitem(i,items.index(self.iclass[i]["selection"]),int(self.icount[i].get()))
            self.sav.refresh()
    
    def store_pokemon(self):
        if (self.pokemon != None):
            if self.gen <= 2:
                self.sav.set("pokemoncount",self.pokecount.get())
                self.sav.refresh()
    
    def store_boxedit(self):
        if (self.boxedit != None):
            if self.gen <= 2:
                self.sav.set("box%dpokemoncount" % (self.curbox),self.boxpokecount.get())
                self.sav.refresh()
    
    def store_pokedex1(self):
            if (self.pokedex1 != None):
                stop = 76
                if self.gen == 2:
                    stop = 125                    
                if self.gen == 3:
                    stop = 196
                for p in range(stop):
                    self.sav.setpokedex(p+1,self.dexseen[p].get(),self.dexcatched[p].get())
                self.sav.refresh()
    
    def store_pokedex2(self):
            if (self.pokedex2 != None):
                start = 76
                stop = 151
                if self.gen == 2:
                    start = 125
                    stop = 251
                if self.gen == 3:
                    start = 196
                    stop = 386
                for p in range(start,stop):
                    self.sav.setpokedex(p+1,self.dexseen[p].get(),self.dexcatched[p].get())
                self.sav.refresh()
    
    def store_pcitems(self):
        global items
        if (self.pcitems != None):
            for i in range(50):
                if self.gen <= 2:
                    self.sav.setitem(i+20,items.index(self.pciclass[i]["selection"]),int(self.pcicount[i].get()))
                if self.gen >= 3:
                    self.sav.setitem(i+163,items.index(self.pciclass[i]["selection"]),int(self.pcicount[i].get()))
            if self.gen <= 2:
                self.sav.set("pcitemcount",self.pcitemcount.get())
            self.sav.refresh()
    
    def store_pokeedit(self):
        global pokemon
        global types
        global moves
        if (self.pokeedit != None):
            p = self.p
            b = self.b
            pkm = self.pkm
            snames = ["maxhp","attack","defense","speed","special"]
            snames2 = snames[:]
            if self.gen == 2:
                snames2 = ["maxhp","attack","defense","speed","specialattack","specialdefense"]
            if self.gen >= 3:
                snames = ["maxhp","attack","defense","speed","specialattack","specialdefense"]
                snames2 = snames[:]
            if self.gen == 1 or b == None:
                pkm = self.sav.pkm_set(pkm,"hp",int(self.curhp.get()))
            if self.gen == 1:
                pkm = self.sav.pkm_set(pkm,"catchrate",int(self.catchrate.get()))
            else:
                pkm = self.sav.pkm_set(pkm,"item",items.index(self.helditem["selection"]))
                pkm = self.sav.pkm_set(pkm,"pokerus",int(self.pokerus.get()))
                pkm = self.sav.pkm_set(pkm,"happiness",int(self.happiness.get()))
                pkm = self.sav.pkm_set(pkm,"caughtlocation",int(self.caughtlocation.get()))
                if self.gen == 2:
                    pkm = self.sav.pkm_set(pkm,"caughttime",int(self.caughttime.get()))
                if self.gen >= 3:
                    pkm = self.sav.pkm_set(pkm,"caughtball",int(self.caughtball.get()))
                pkm = self.sav.pkm_set(pkm,"caughtlevel",int(self.caughtlevel.get()))
            pkm = self.sav.pkm_set(pkm,"otnum",int(self.otnum.get()))
            if self.gen == 3:
                pkm = self.sav.pkm_set(pkm,"pid",int(self.pid.get()))
                pkm = self.sav.pkm_set(pkm,"secretid",int(self.secretid.get()))
            pkm = self.sav.pkm_set(pkm,"exp",int(self.exp.get()))
            pkm = self.sav.pkm_set(pkm,"otname",self.otname.get())
            pkm = self.sav.pkm_set(pkm,"name",self.nickname.get())
            pkm = self.sav.pkm_set(pkm,"num",pokemon.index(self.pokeclass["selection"]))
            if self.gen <= 2:
                pkm = self.sav.pkm_set(pkm,"sprite",pokemon.index(self.pokesprite["selection"]))
            if self.gen == 1: 
                pkm = self.sav.pkm_set(pkm,"type1",types.index(self.type1["selection"]))
                pkm = self.sav.pkm_set(pkm,"type2",types.index(self.type2["selection"]))
            if self.gen <= 2:
                if (len(pkm) >= 67):
                    pkm = self.sav.pkm_set(pkm,"curlevel",int(self.level.get()))
                else:
                    pkm = self.sav.pkm_set(pkm,"level",int(self.level.get()))
            if self.gen >= 3:
                if (len(pkm) >= 100):
                    pkm = self.sav.pkm_set(pkm,"level",int(self.level.get()))
            
            if self.gen == 1 or b == None:
                pkm = self.sav.pkm_set(pkm,"asleep",self.asleep.get())
                pkm = self.sav.pkm_set(pkm,"poisoned",self.poisoned.get())
                pkm = self.sav.pkm_set(pkm,"frozen",self.frozen.get())
                pkm = self.sav.pkm_set(pkm,"paralyzed",self.paralyzed.get())
            
            for m in range(4):
                pkm = self.sav.pkm_set(pkm,"move%d" % (m+1),moves.index(self.moveclass[m]["selection"]))
                pkm = self.sav.pkm_set(pkm,"move%dpp" % (m+1),int(self.movepp[m].get()))
                pkm = self.sav.pkm_set(pkm,"move%dppup" % (m+1),int(self.moveppup[m].get()))

            for s in range(len(snames)):
                if s != 5 or self.gen == 3:
                    if s or self.gen == 3:
                        pkm = self.sav.pkm_set(pkm,"%siv" % (snames[s]),int(self.stativs[s].get()))
                    pkm = self.sav.pkm_set(pkm,"%sev" % (snames[s]),int(self.statevs[s].get()))
                if b == None:
                    if s != 5 or self.gen >= 2:
                        pkm = self.sav.pkm_set(pkm,snames2[s],int(self.statcur[s].get()))
            
            if self.gen >= 3:
                cnames = ["coolness","beauty","cuteness","smartness","toughness","feel"]
                for s in range(len(cnames)):
                    pkm = self.sav.pkm_set(pkm,cnames[s],int(self.constat[s].get()))
            
            if b == None:
                self.sav.setpokemon(p,pkm)
            else:
                self.sav.setpcpokemon(b*self.bp+p,pkm)
            self.sav.refresh()

    
    
    def wmdel_items(self):
        self.store_items()
        self.items.destroy()
        self.items = None
        
    def wmdel_boxes(self):
        self.boxes.destroy()
        self.boxes = None
        
    def wmdel_pcitems(self):
        self.store_pcitems()
        self.pcitems.destroy()
        self.pcitems = None
    
    def wmdel_pokedex1(self):
        self.store_pokedex1()
        self.pokedex1.destroy()
        self.pokedex1 = None
    
    def wmdel_pokedex2(self):
        self.store_pokedex2()
        self.pokedex2.destroy()
        self.pokedex2 = None
        
    def wmdel_pokeedit(self):
        self.store_pokeedit()
        self.pokeedit.destroy()
        if self.b == None:
            if self.pokemon != None:
                self.wmdel_pokemon()
                self.show_pokemon()
            else:
                if self.boxedit != None:
                    if self.curbox == self.b:
                        self.wmdel_boxedit()
                        self.show_boxedit(self.curbox)
        self.pokeedit = None
        
    def wmdel_pokemon(self):
        self.store_pokemon()
        self.pokemon.destroy()
        self.pokemon = None
        
    def wmdel_boxedit(self):
        self.store_boxedit()
        self.boxedit.destroy()
        if self.boxes != None:
            self.wmdel_boxes()
            self.show_boxes()
        self.boxedit = None
    
    def show_pokemon(self):
        global pokedex
        global pokemon
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.pokemon != None:
            return
        self.pokemon = Toplevel()
        self.pokemon.title("Party Pokémon - %s" % (self.title))
        Label(self.pokemon,text="   ").grid(row=1000,column=1000)
        self.pokemon.protocol('WM_DELETE_WINDOW', self.wmdel_pokemon)
        #Label(self.pokemon,text="Level").grid(row=1,column=1)
        #Label(self.pokemon,text="Class").grid(row=1,column=2)
        Label(self.pokemon,text="",font=("Times",4)).grid(row=0)
        for p in range(6):
            pclass = self.sav.pkm_get(self.sav.pokemon[p],"num")
            plevel = self.sav.pkm_get(self.sav.pokemon[p],"curlevel")
            Label(self.pokemon,text="    Pokémon %d" % (p+1)).grid(row=p*2+2,column=0,sticky=W)
            Label(self.pokemon,text="    Lv. %d    " % (plevel)).grid(row=p*2+2,column=1)
            Label(self.pokemon,text=pokemon[pclass]+"    ").grid(row=p*2+2,column=2,sticky=W)
            Button(self.pokemon,text="Edit",width=6,command=lambda p=p: self.show_pokeedit(p)).grid(row=p*2+2,column=3)
        if self.gen <= 2:
            Label(self.pokemon,text="",font=("Times",4)).grid(row=13)
            Label(self.pokemon,text="    Pokémon #  (Pokémon in the party)").grid(row=14,columnspan=3,sticky=W)
            self.pokecount = Entry(self.pokemon,width=7)
            self.pokecount.insert(0,str(self.sav.pokemoncount))
            self.pokecount.grid(row=14,column=3)
    
    def show_boxes(self):
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.boxes != None:
            return
        self.boxes = Toplevel()
        self.boxes.title("PC Boxes - %s" % (self.title))
        Label(self.boxes,text="   ").grid(row=1000,column=1000)
        self.boxes.protocol('WM_DELETE_WINDOW', self.wmdel_boxes)
        Label(self.boxes,text="",font=("Times",4)).grid(row=0)
        curbox = self.sav.currentbox
        for b in range(self.bn):
            boxnum = self.sav.boxpokemoncount[b]
            if (b == curbox):
                Label(self.boxes,text="    Box %d (Selected)" % (b+1)).grid(row=b*2+2,column=0,sticky=W)
            else:
                Label(self.boxes,text="    Box %d" % (b+1)).grid(row=b*2+2,column=0,sticky=W)
            if self.gen < 3:
                Label(self.boxes,text="    %d / 20 Pokémon    " % (boxnum)).grid(row=b*2+2,column=1)
            else:
                Label(self.boxes,text="    %d / 30 Pokémon    " % (boxnum)).grid(row=b*2+2,column=1)
            Button(self.boxes,text="Edit",width=6,command=lambda b=b: self.show_boxedit(b)).grid(row=b*2+2,column=3)
    
    def show_boxedit(self,b):
        global pokedex
        global pokemon
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.boxedit != None:
            return
        self.curbox = b
        self.boxedit = Toplevel()
        self.boxedit.title("Box %d - %s" % (b+1,self.title))
        Label(self.boxedit,text="   ").grid(row=1000,column=1000)
        self.boxedit.protocol('WM_DELETE_WINDOW', self.wmdel_boxedit)
        Label(self.boxedit,text="",font=("Times",4)).grid(row=0) 
        plevel = 0
        for p in range(self.bp):
            pclass = self.sav.pkm_get(self.sav.pcpokemon[b*self.bp+p],"num")
            if self.gen <= 2:
                plevel = self.sav.pkm_get(self.sav.pcpokemon[b*self.bp+p],"level")
            Label(self.boxedit,text="    Pokémon %d" % (p+1)).grid(row=p*2+2,column=0,sticky=W)
            Label(self.boxedit,text="    Lv. %d    " % (plevel)).grid(row=p*2+2,column=1)
            text = "??????????"
            if pclass < len(pokemon):
                text = pokemon[pclass]
            Label(self.boxedit,text=text+"    ").grid(row=p*2+2,column=2,sticky=W)
            Button(self.boxedit,text="Edit",width=6,command=lambda p=p: self.show_pokeedit(p,b)).grid(row=p*2+2,column=3)
        if self.gen <= 2:
            Label(self.boxedit,text="",font=("Times",4)).grid(row=self.bp*2+1)
            Label(self.boxedit,text="    Pokémon #  (Pokémon in the box)").grid(row=self.bp*2+2,columnspan=3,sticky=W)
            self.boxpokecount = Entry(self.boxedit,width=7)
            self.boxpokecount.insert(0,str(self.sav.boxpokemoncount[b]))
            self.boxpokecount.grid(row=self.bp*2+2,column=3)
        pass
    
    def show_pokeedit(self,p,b=None):
        global pokedex
        global pclass
        global moves
        global types
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.pokeedit != None:
            return
        
        self.pokeedit = Toplevel()
        
        if b==None:
            pkm = self.sav.pokemon[p]
            self.pkm = pkm
            self.p = p
            self.b = None
            self.pokeedit.title("Party Pokémon %d - %s" % (p+1,self.title))
        else:
            pkm = self.sav.pcpokemon[b*self.bp+p]
            self.pkm = pkm
            self.p = p
            self.b = b
            self.pokeedit.title("PC Box %d, Pokémon %d - %s" % (b+1,p+1,self.title))

        
        Label(self.pokeedit).grid()
        Label(self.pokeedit,text="   ").grid(row=1000,column=1000)
        self.pokeedit.protocol('WM_DELETE_WINDOW', self.wmdel_pokeedit)
        Label(self.pokeedit,text="    Pokémon Class:  ").grid(row=10,column=10,columnspan=10)
        if (self.gen <= 2):
            Label(self.pokeedit,text="    Pokémon Sprite:  ").grid(row=20,column=10,columnspan=10)
        else:
            Label(self.pokeedit,text = "    Personality / PID:  ").grid(row=20,column=10,columnspan=10,sticky=E)    
            self.pid = Entry(self.pokeedit,width=22)
            self.pid.insert(0,self.sav.pkm_get(pkm,"pid"));
            self.pid.grid(row=20,column=20,columnspan=10)
        Label(self.pokeedit,text="    Nickname:  ").grid(row=25,column=10,columnspan=10)
        Label(self.pokeedit,text="    OT Num / OT Name:  ").grid(row=10,column=30,columnspan=10)
        Label(self.pokeedit,text="    Level / Exp. Points:  ").grid(row=20,column=30,columnspan=10)
        
        self.otnum = Entry(self.pokeedit,width=6)
        self.otnum.insert(0,self.sav.pkm_get(pkm,"otnum"));
        self.otnum.grid(row=10,column=40,columnspan=10)
        self.otname = Entry(self.pokeedit,width=10)
        self.otname.insert(0,self.sav.pkm_get(pkm,"otname"));
        self.otname.grid(row=10,column=50,columnspan=10)
        
        if self.gen >= 2:
            Label(self.pokeedit,text="    Held Item:  ").grid(row=23,column=10,columnspan=10)
            self.helditem = ComboBox(self.pokeedit,dropdown=1,editable=1,width=20,value=items[self.sav.pkm_get(pkm,"item")])
            
            array = items*1
            array.sort(reverse=False)
            for x in range(len(array)):
                if len(array[x]) > 4:
                    self.helditem.insert(END,array[x])
            self.helditem.grid(row=23,column=20,columnspan=10)
            
            if self.gen <= 2:
                Label(self.pokeedit,text="    Pokérus:  ").grid(row=25,column=30,columnspan=10)
            else:
                Label(self.pokeedit,text="    Pokérus / Secret ID:  ").grid(row=25,column=30,columnspan=10)
                self.secretid = Entry(self.pokeedit,width=10)
                self.secretid.insert(0,self.sav.pkm_get(pkm,"secretid"));
                self.secretid.grid(row=25,column=50,columnspan=10)
            self.pokerus = Entry(self.pokeedit,width=6)
            self.pokerus.insert(0,self.sav.pkm_get(pkm,"pokerus"));
            self.pokerus.grid(row=25,column=40,columnspan=10)
            
            if self.gen == 2:
                Label(self.pokeedit,text="    Caught zone / level / time:  ").grid(row=23,column=30,columnspan=10)
            if self.gen >= 3:
                Label(self.pokeedit,text="    Caught zone / level / Ball:  ").grid(row=23,column=30,columnspan=10)
            
            self.caughtlocation = Entry(self.pokeedit,width=6)
            self.caughtlocation.insert(0,self.sav.pkm_get(pkm,"caughtlocation"));
            self.caughtlocation.grid(row=23,column=40,columnspan=10)
            self.caughtlevel = Entry(self.pokeedit,width=5)
            self.caughtlevel.insert(0,self.sav.pkm_get(pkm,"caughtlevel"));
            self.caughtlevel.grid(row=23,column=50,columnspan=5)
        if self.gen == 2:
            self.caughttime = Entry(self.pokeedit,width=4)
            self.caughttime.insert(0,self.sav.pkm_get(pkm,"caughttime"));
            self.caughttime.grid(row=23,column=55,columnspan=5)
        if self.gen >= 3:
            self.caughtball = Entry(self.pokeedit,width=4)
            self.caughtball.insert(0,self.sav.pkm_get(pkm,"caughtball"));
            self.caughtball.grid(row=23,column=55,columnspan=5)
            
        
        self.level = Entry(self.pokeedit,width=6)
        
        if (b == None):
            self.level.insert(0,self.sav.pkm_get(pkm,"curlevel"));
        else:
            if self.gen <= 2:
                self.level.insert(0,self.sav.pkm_get(pkm,"level"));
        self.level.grid(row=20,column=40,columnspan=10)
        self.exp = Entry(self.pokeedit,width=10)
        self.exp.insert(0,self.sav.pkm_get(pkm,"exp"));
        self.exp.grid(row=20,column=50,columnspan=10)        
        
        self.nickname = Entry(self.pokeedit,width=22)
        self.nickname.insert(0,self.sav.pkm_get(pkm,"name"));
        self.nickname.grid(row=25,column=20,columnspan=10)
        
        Label(self.pokeedit).grid(row=30)
        
        if self.gen == 1 or b == None:
            Label(self.pokeedit,text="    Curr. HP:  ").grid(row=40,column=10,columnspan=10,sticky=W)
            self.curhp = Entry(self.pokeedit,width=6)
            self.curhp.insert(0,self.sav.pkm_get(pkm,"hp"));
            self.curhp.grid(row=40,column=10,columnspan=10,sticky=E)
        
        self.asleep=IntVar()
        self.poisoned=IntVar()
        self.paralyzed=IntVar()
        self.frozen=IntVar()
        
        if self.gen == 1 or b == None:
            Checkbutton(self.pokeedit,variable=self.asleep,text="SLP").grid(row=40,column=20,columnspan=5,sticky=E)
            if (self.sav.pkm_get(pkm,"asleep")): self.asleep.set(1);
            Checkbutton(self.pokeedit,variable=self.poisoned,text="PSN").grid(row=40,column=25,columnspan=5,sticky=E)
            if (self.sav.pkm_get(pkm,"poisoned")): self.poisoned.set(1);
            Checkbutton(self.pokeedit,variable=self.frozen,text="FRZ").grid(row=40,column=30,columnspan=5,sticky=E)
            if (self.sav.pkm_get(pkm,"frozen")): self.frozen.set(1);
            Checkbutton(self.pokeedit,variable=self.paralyzed,text="PAR").grid(row=40,column=35,columnspan=5,sticky=E)
            if (self.sav.pkm_get(pkm,"paralyzed")): self.paralyzed.set(1);
        
        if self.gen == 1:
            Label(self.pokeedit,text="    Catch rate:").grid(row=40,column=40,columnspan=10,sticky=W)
            self.catchrate = Entry(self.pokeedit,width=6)
            self.catchrate.insert(0,self.sav.pkm_get(pkm,"catchrate"));
            self.catchrate.grid(row=40,column=50,columnspan=10,sticky=W)
        else:
            Label(self.pokeedit,text="    Happiness:").grid(row=40,column=40,columnspan=10,sticky=W)
            self.happiness = Entry(self.pokeedit,width=6)
            self.happiness.insert(0,self.sav.pkm_get(pkm,"happiness"));
            self.happiness.grid(row=40,column=50,columnspan=10,sticky=W)
        
        if self.gen == 1:
            Label(self.pokeedit,text="    Type1 / Type2:").grid(row=28,column=10,columnspan=10)
            self.type1 = ComboBox(self.pokeedit,dropdown=1,editable=1,value=types[self.sav.pkm_get(pkm,"type1")])
            array = types*1
            array.sort(reverse=False)
            self.type2 = ComboBox(self.pokeedit,dropdown=1,editable=1,value=types[self.sav.pkm_get(pkm,"type2")])
            for x in range(256):
                if len(array[x]) > 4:
                    self.type1.insert(END,array[x])
                    self.type2.insert(END,array[x])
            self.type1.grid(row=28,column=20,columnspan=10,sticky=E)
            self.type2.grid(row=28,column=30,columnspan=10,sticky=E)
        
        self.pokeclass = ComboBox(self.pokeedit,dropdown=1,editable=1,width=20,value=pokemon[self.sav.pkm_get(pkm,"num")])
        if (self.gen <= 2):
            self.pokesprite = ComboBox(self.pokeedit,dropdown=1,editable=1,width=20,value=pokemon[self.sav.pkm_get(pkm,"sprite")])
        array = pokemon*1
        array.sort(reverse=False)
        for x in range(len(array)):
            if len(array[x]) > 4:
                self.pokeclass.insert(END,array[x])
                if (self.gen <= 2):
                    self.pokesprite.insert(END,array[x])
        
        self.pokeclass.grid(row=10,column=20,columnspan=10)
        if (self.gen <= 2):
            self.pokesprite.grid(row=20,column=20,columnspan=10)

        self.moveclass = [None]*4
        self.movepp = [None]*4
        self.moveppup = [None]*4
        
        Label(self.pokeedit).grid(row=50)
        
        for m in range(4):
            self.moveclass[m] = ComboBox(self.pokeedit,dropdown=1,editable=1,width=20,value=moves[self.sav.pkm_get(pkm,"move%d" % (m+1))])
            array = moves*1
            array.sort(reverse=False)
            Label(self.pokeedit,text = "Move %d:" % (m+1)).grid(row=60+10*m,column=10,columnspan=10)
            Label(self.pokeedit,text = "PP / PP up:").grid(row=60+10*m,column=30,columnspan=10)
            for x in range(256):
                if len(array[x]) > 4:
                    self.moveclass[m].insert(END,array[x])
            self.moveclass[m].grid(row=60+10*m,column=20,columnspan=10)
            self.movepp[m]=Entry(self.pokeedit,width=6)
            self.movepp[m].insert(0,self.sav.pkm_get(pkm,"move%dpp" % (m+1)))
            self.movepp[m].grid(row=60+10*m,column=40,columnspan=5)
            self.moveppup[m]=Entry(self.pokeedit,width=6)
            self.moveppup[m].insert(0,self.sav.pkm_get(pkm,"move%dppup" % (m+1)))
            self.moveppup[m].grid(row=60+10*m,column=45,columnspan=5)
            
        Label(self.pokeedit).grid(row=100)
        Label(self.pokeedit,text = "HP (Max.)").grid(row=110,column=20,columnspan=5)
        Label(self.pokeedit,text = "Attack").grid(row=110,column=25,columnspan=5)
        Label(self.pokeedit,text = "Defense").grid(row=110,column=30,columnspan=5)
        Label(self.pokeedit,text = "Speed").grid(row=110,column=35,columnspan=5)
        if self.gen == 1:Label(self.pokeedit,text = "Special").grid(row=110,column=40,columnspan=5)
        if self.gen > 1: Label(self.pokeedit,text = "Special Att./Def.").grid(row=110,column=40,columnspan=10)
        Label(self.pokeedit,text = "Individual values:   ").grid(row=120,column=10,columnspan=10,sticky=E)
        Label(self.pokeedit,text = "Effort values:   ").grid(row=130,column=10,columnspan=10,sticky=E)
        
        if b==None:
            Label(self.pokeedit,text = "Current values:   ").grid(row=140,column=10,columnspan=10,sticky=E)
        
        scol = 20
        snames = ["maxhp","attack","defense","speed","special"] 
        snames2 = ["maxhp","attack","defense","speed","specialattack","specialdefense"]
        if self.gen == 1: snames2 = snames
        if self.gen >= 3: snames = snames2
        self.statevs=[None]*6
        self.stativs=[None]*6
        self.statcur=[None]*6
        self.constat=[None]*6
        
        for s in range(len(snames)):
            if (scol > 20 and s != 5) or self.gen >= 3:
                self.stativs[s]=Entry(self.pokeedit,width=6)
                self.stativs[s].insert(0,self.sav.pkm_get(pkm,"%siv" % (snames[s])))
                self.stativs[s].grid(row=120,column=scol,columnspan=5)
            if s != 5 or self.gen >= 3:
                self.statevs[s]=Entry(self.pokeedit,width=6)
                self.statevs[s].insert(0,self.sav.pkm_get(pkm,"%sev" % (snames[s])))
                self.statevs[s].grid(row=130,column=scol,columnspan=5)
            if b==None:
                self.statcur[s]=Entry(self.pokeedit,width=6)
                self.statcur[s].insert(0,self.sav.pkm_get(pkm,snames2[s]))
                self.statcur[s].grid(row=140,column=scol,columnspan=5)
            scol+=5
        
        if self.gen >= 3:   
            cnames = ["coolness","beauty","cuteness","smartness","toughness","feel"]
            Label(self.pokeedit).grid(row=150)
            Label(self.pokeedit,text = "Contest values:   ").grid(row=170,column=10,columnspan=10,sticky=E)
            Label(self.pokeedit,text = "Coolness").grid(row=160,column=20,columnspan=5)
            Label(self.pokeedit,text = "Beauty").grid(row=160,column=25,columnspan=5)
            Label(self.pokeedit,text = "Cuteness").grid(row=160,column=30,columnspan=5)
            Label(self.pokeedit,text = "Smartness").grid(row=160,column=35,columnspan=5)
            Label(self.pokeedit,text = "Toughness").grid(row=160,column=40,columnspan=5)
            Label(self.pokeedit,text = "Feel").grid(row=160,column=45,columnspan=5)
            scol = 20
            for s in range(len(cnames)):
                self.constat[s]=Entry(self.pokeedit,width=6)
                self.constat[s].insert(0,self.sav.pkm_get(pkm,"%s" % (cnames[s])))
                self.constat[s].grid(row=170,column=scol,columnspan=5)
                scol+=5 

        
        
        
    def show_pokedex1(self):
        global pokedex
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.pokedex1 != None:
            return
        self.pokedex1 = Toplevel()
        self.pokedex1.title("Pokédex 1/2 - %s" % (self.title))
        self.pokedex1.protocol('WM_DELETE_WINDOW', self.wmdel_pokedex1)
        Label(self.pokedex1,text="   ").grid(row=1000,column=1000)
        
        start = 0
        stop = 76
        step = 4
        if self.gen == 2:
            start = 0
            stop = 125
            step = 5
        if self.gen == 3:
            start = 0
            stop = 196
            step = 7
                
        for p in range(step):
            Label(self.pokedex1,text=" S").grid(row=0,column=1+3*p,sticky=W)
            Label(self.pokedex1,text=" C").grid(row=0,column=2+3*p,sticky=W)
        for p in range(start,stop):
            Label(self.pokedex1,text="    "+pokedex[p+1]).grid(row=(p//step)+1,column=(p%step)*3,sticky=W)
            self.dexseen[p]=IntVar()
            var = IntVar()
            Checkbutton(self.pokedex1,variable=var).grid(row=(p//step)+1,column=(p%step)*3+1,sticky=W)
            self.dexseen[p]=var
            del var
            var = IntVar()
            Checkbutton(self.pokedex1,variable=var).grid(row=(p//step)+1,column=(p%step)*3+2,sticky=W)
            self.dexcatched[p]=var
            del var
            if (self.sav.catched[p+1]): self.dexcatched[p].set(1)
            if (self.sav.seen[p+1]): self.dexseen[p].set(1)
        return
    
        
    def show_pokedex2(self):
        global pokedex
        if self.sav == None:
            showerror("Something went wrong =(","You need to load a .sav first")
            return
        if self.pokedex2 != None:
            return
        self.pokedex2 = Toplevel()
        self.pokedex2.title("Pokédex 2/2 - %s" % (self.title))
        self.pokedex2.protocol('WM_DELETE_WINDOW', self.wmdel_pokedex2)
        Label(self.pokedex2,text="   ").grid(row=1000,column=1000)
         
        start = 76
        stop = 151
        step = 4
        if self.gen == 2:
            start = 125
            stop = 251
            step = 5
        if self.gen == 3:
            start = 196
            stop = 386
            step = 7
         
        for p in range(step):
            Label(self.pokedex2,text=" S").grid(row=0,column=1+3*p,sticky=W)
            Label(self.pokedex2,text=" C").grid(row=0,column=2+3*p,sticky=W)
        for p in range(start,stop):
            Label(self.pokedex2,text="    "+pokedex[p+1]).grid(row=((p-start)//step)+1,column=(p%step)*3,sticky=W)
            self.dexseen[p]=IntVar()
            var = IntVar()
            Checkbutton(self.pokedex2,variable=var).grid(row=((p-start)//step)+1,column=(p%step)*3+1,sticky=W)
            self.dexseen[p]=var
            del var
            var = IntVar()
            Checkbutton(self.pokedex2,variable=var).grid(row=((p-start)//step)+1,column=(p%step)*3+2,sticky=W)
            self.dexcatched[p]=var
            del var
            if (self.sav.catched[p+1]): self.dexcatched[p].set(1)
            if (self.sav.seen[p+1]): self.dexseen[p].set(1)
        return
        
        
        
    def show_about(self):
        showinfo("About PikaSav","Made by Ritchie. I'm cool. Yes, you're cool too.")
        return

    def show_savinfo(self):
        if self.sav == None:
            showinfo("SAV Info","There is no .sav file loaded.")
        else:
            showinfo("SAV Info","Handler: %s\n- Sav filesize: %d\n- %d bytes loaded" % (self.sav.version,os.path.getsize(self.sav.file),len(self.sav.buffer)))
        return

pikasav = PikaSav()