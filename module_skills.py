# -*- coding: utf-8 -*-
from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.

# skills = [
 # ("trade","Trade",sf_base_att_cha|sf_effects_party|sf_inactive,10,"Every level of this skill reduces your trade penalty by 5%%. (Drużynowa umiejętność)"),
  # ("leadership","Leadership",sf_base_att_cha,10,"Every point increases maximum number of troops you can command by 5, increases your party morale and reduces troop wages by 5%%. (Umiejętność przywódcy)"),
  # ("prisoner_management", "Prisoner Management",sf_base_att_cha,10,"Every level of this skill increases maximum number of prisoners by %d. (Umiejętność przywódcy)"), 
  # ("reserved_1","Seducing",sf_base_att_cha,10,"Every point increases chances of successful seduction."), 
  # ("reserved_2","Reserved Skill 2",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_3","Reserved Skill 3",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_4","Reserved Skill 4",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  # ("persuasion","Persuasion", sf_base_att_int,10, "This skill helps you make other people accept your point of view. It also lowers the minimum level of relationship needed to get NPCs to do what you want. (Osobista umiejętność)"),
  # ("engineer","Engineer",sf_base_att_int|sf_effects_party,10,"This skill allows you to construct siege equipment and fief improvements more efficiently. (Drużynowa umiejętność)"),
  # ("first_aid", "First Aid",sf_base_att_int|sf_effects_party,10,"Heroes regain 5%% per skill level of hit-points lost during mission. (Drużynowa umiejętność)"), 
  # ("surgery","Surgery",sf_base_att_int|sf_effects_party,10,"Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Drużynowa umiejętność)"), 
  # ("wound_treatment","Wound Treatment",sf_base_att_int|sf_effects_party,10,"Party healing speed is increased by 20%% per level of this skill. (Drużynowa umiejętność)"), 
  # ("inventory_management","Inventory Management",sf_base_att_int,10,"Increases inventory capacity by +6 per skill level. (Umiejętność przywódcy)"), 
  # ("spotting","Spotting",sf_base_att_int|sf_effects_party,10,"Party seeing range is increased by 10%% per skill level. (Drużynowa umiejętność)"),
  # ("pathfinding","Path-finding",sf_base_att_int|sf_effects_party,10,"Party map speed is increased by 3%% per skill level. (Drużynowa umiejętność)"), 
  # ("tactics","Tactics",sf_base_att_int|sf_effects_party,10,"Every two levels of this skill increases starting battle advantage by 1. (Drużynowa umiejętność)"),
  # ("tracking","Tracking",sf_base_att_int|sf_effects_party,10,"Tracks become more informative. (Drużynowa umiejętność)"),
  # ("trainer","Trainer",sf_base_att_int,10,"Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,10,16,23,30,38,46,55,65,80}. (Osobista umiejętność)"),
  # ("reserved_5","Reserved Skill 5",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_6","Reserved Skill 6",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_7","Reserved Skill 7",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_8","Reserved Skill 8",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  # ("looting","Looting",sf_base_att_agi|sf_effects_party,10,"This skill increases the amount of loot obtained by 10%% per skill level. (Drużynowa umiejętność)"), 
  # ("horse_archery","Horse Shooting",sf_base_att_agi,10,"Reduces damage and accuracy penalties for archery and throwing from horseback. (Osobista umiejętność)"),
  # ("riding","Riding",sf_base_att_agi,10,"Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Osobista umiejętność)"),
  # ("athletics","Athletics",sf_base_att_agi,10,"Improves your running speed. (Osobista umiejętność)"),
 # ("shield","Shield",sf_base_att_agi|sf_inactive,10,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. (Osobista umiejętność)"),
  # ("weapon_master","Weapon Master",sf_base_att_agi,10,"Makes it easier to learn weapon proficiencies and increases the proficiency limits. Limits go as: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420. (Osobista umiejętność)"),
  # ("reserved_9","Reserved Skill 9",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_10","Reserved Skill 10",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_11","Reserved Skill 11",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_12","Reserved Skill 12",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_13","Reserved Skill 13",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
 # ("power_draw","Power Draw",sf_base_att_str|sf_inactive,10,"Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. (Osobista umiejętność)"),
  # ("power_throw","Power Throw",sf_base_att_str,10,"Each point to this skill increases throwing damage by 10%%. (Osobista umiejętność)"),
  # ("power_strike","Power Strike",sf_base_att_str,10,"Each point to this skill increases melee damage by 8%%. (Osobista umiejętność)"),
  # ("ironflesh","Ironflesh",sf_base_att_str,10,"Each point to this skill increases hit points by +2. (Osobista umiejętność)"), 
  # ("reserved_14","Reserved Skill 14",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_15","Reserved Skill 15",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_16","Reserved Skill 16",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_17","Reserved Skill 17",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  # ("reserved_18","Reserved Skill 18",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
# ]

skills = [
  # ("seduction","Uwodzenie",sf_base_att_cha,0,"Każdy punkt zwiększa szansę na pomyślne uwodzenie, daje dostęp do nowych kochanek."),
  ("seduction"," ",sf_base_att_cha,0,"  "),
  ("leadership","Przywództwo",sf_base_att_cha,10,"Każdy kolejny poziom tej umiejętności podwyższa morale o 12 punktów, a koszty utrzymania armii obniżają się o 5%% (umiejętność przywódcy)."),
  ("prisoner_management", "Zarządzanie więźniami",sf_base_att_cha,10,"Każdy punkt tej umiejętności zwiększa maksymalną ilość więźniów o %d. (Umiejętność przywódcy)"), 
  ("reserved_1","Reserved Skill 1",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_2","Reserved Skill 2",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_3","Reserved Skill 3",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_4","Reserved Skill 4",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("persuasion","Perswazja", sf_base_att_int,10, "Ta umiejętność pomaga przekonywać innych ludzi aby zaakceptowali twój punkt widzenia. (Osobista umiejętność)"),
  ("engineer"," ",sf_base_att_int|sf_effects_party,0," "),
  ("first_aid", "Leczenie",sf_base_att_int|sf_effects_party,10,"Bohater odzyskuje 5%% zdrowia, na każdy poziom umiejętności w trakcie trwania bitwy. (Drużynowa umiejętność)"), 
  ("surgery","Chirurgia",sf_base_att_int|sf_effects_party,10,"Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Drużynowa umiejętność)"), 
  ("wound_treatment","Opatrywanie ran",sf_base_att_int|sf_effects_party,10,"Szybkość leczenia zwiększa się o 20%% na każdy poziom umiejętności. (Drużynowa umiejętność)"), 
  ("inventory_management","Zarządzanie ekwipunkiem",sf_base_att_int,10,"Pojemność inwentarza zwiększa się o 6 miejsc, na każdy poziom umiejętności. (Umiejętność przywódcy)"), 
  ("spotting","Spostrzegawczość",sf_base_att_int|sf_effects_party,10,"Zasięg widzialności zwiększa się o 10%% na każdy poziom umiejętności. (Drużynowa umiejętność)"),
  ("pathfinding","Tropienie",sf_base_att_int|sf_effects_party,10,"Szybkość porszuania się na mapie świata zwiększa się o 3%% na każdy poziom umiejętności. (Drużynowa umiejętność)"), 
  ("tactics","Taktyka",sf_base_att_int|sf_effects_party,10,"Każde dwa poziomy tej umiejętności zwiększają początkową bitewną przewagę o 1. (Drużynowa umiejętność)"),
  ("tracking","Tropienie",sf_base_att_int|sf_effects_party,10,"Tropienie dostarcza więcej informacji. (Drużynowa umiejętność)"),
  ("trainer","Szkolenie",sf_base_att_int,10,"Każdego dnia, bohater z tą umiejętnością dodaje doświadczenie innym członkom oddziału, których poziom jest niższy. Doświadczenie zdobywane: {0,4,10,16,23,30,38,46,55,65,80}. (Osobista umiejętność)"),
  ("reserved_5","Reserved Skill 5",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_6","Reserved Skill 6",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_7","Reserved Skill 7",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_8","Reserved Skill 8",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("looting","Plądrowanie",sf_base_att_agi|sf_effects_party,10,"Ta umiejętność zwiększa ilość zdobywanego łupu o 10%% na każdy poziom umiejętności. (Drużynowa umiejętność)"), 
  ("horse_archery","Strzelectwo konne",sf_base_att_agi,10,"Redukuje obrażenia i kary celności dla strzelców konnych. (Osobista umiejętność)"),
  ("riding","Jazda konna",sf_base_att_agi,10,"Umiejętność umożliwia jazdę na lepszych koniach, zwiększa szybkość i zwrotność. (Osobista umiejętność)"),
  ("athletics","Atletyka",sf_base_att_agi,10,"Każdy punkt poprawia umiejętność biegania.(Osobista umiejętność)"),
  ("shield"," ",sf_base_att_agi,0," "),
  ("weapon_master","Mistrzostwo broni",sf_base_att_agi,10,"Umiejętność umożliwia szybszą naukę posługiwania się bronią i zwiększa limity umiejętności. Limity: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420. (Osobista umiejętność)"),
  ("reserved_9","Reserved Skill 9",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_10","Reserved Skill 10",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_11","Reserved Skill 11",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_12","Reserved Skill 12",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_13","Reserved Skill 13",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("power_draw"," ",sf_base_att_str,0," "),
  ("power_throw","Mocna głowa",sf_base_att_str,10," "),
  ("power_strike","Potężne uderzenie",sf_base_att_str,10,"Każdy punkt tej umiejętności zwiększa siłę uderzenia o 8%%. (Osobista umiejętność)"),
  ("ironflesh","Wytrzymałość",sf_base_att_str,10,"Każdy punkt zwiększa wytrzymałość o +2. (Osobista umiejętność)"), 
  ("reserved_14","Reserved Skill 14",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_15","Reserved Skill 15",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_16","Reserved Skill 16",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_17","Reserved Skill 17",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_18","Reserved Skill 18",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
]
