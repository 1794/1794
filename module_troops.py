# -*- coding: utf-8 -*-
import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

from troops import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3|knows_spotting_5
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_spotting_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_spotting_5
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_spotting_5
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_spotting_5

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_5|agi_5|int_5|cha_5,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_civilian_outfit_a, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_civilian_outfit_a,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_civilian_outfit_a,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],
  ["1794","Settings","Settings",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_noz,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_noz,itm_club,itm_quarter_staff,itm_dagger,itm_stones,itm_leather_cap,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Gołota","Gołota",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_zupan_e,itm_zupan_f,itm_polish_coat_c,itm_steppe_horse, itm_saddle_horse, itm_polish_coat_d, itm_polish_coat_e, itm_zupan,itm_cav_pants,itm_civil_pants,itm_civil_pants_a,itm_civil_pants_b, itm_zupan_d,itm_rapier15,itm_rapier17,itm_rapier22,itm_rapier12,itm_rapier19,itm_rapier27,itm_rapier24,],   def_attrib|level(9),wp(110),knows_common|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Najemnik","Najemnicy",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_zupan_e,
   itm_polish_coat_c,
   itm_steppe_horse,
   itm_saddle_horse,
   itm_polish_coat_d,
   itm_polish_coat_e,
   itm_zupan,
   itm_cav_pants,
   itm_civil_pants,
   itm_civil_pants_a,
   itm_civil_pants_b,
   itm_zupan_d,
   itm_huc1,
   itm_huc2,
   itm_huc3,
   itm_pistolet1,
   itm_rapier14,
   itm_rapier24,],
   def_attrib|level(14),wp(1005),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_przemytnik","Przemytnik","Przemytnicy",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_huc2,
	itm_huc3,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   def_attrib|level(14),wp(110),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_golota2","Gołota","Gołota",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_zupan_e,
   itm_polish_coat_c,
   itm_steppe_horse,
   itm_saddle_horse,
   itm_polish_coat_d,
   itm_polish_coat_e,
   itm_zupan,
   itm_cav_pants,
   itm_civil_pants,
   itm_civil_pants_a,
   itm_civil_pants_b,
   itm_zupan_d,
   itm_huc1,
   itm_huc2,
   itm_huc3,
   itm_pistolet1,
   itm_rapier14,
   itm_rapier24,],
   def_attrib|level(14),wp(110),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],

  # ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   # [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_civilian_outfit_a,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet, itm_helmet_with_neckguard],
   # def_attrib|level(20),wp(100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  # ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   # [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,itm_haubergeon,itm_mail_chausses,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   # def_attrib|level(25),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  # ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   # [itm_bolts,itm_spiked_club,itm_french_rapier,itm_sword_medieval_a,itm_boar_spear,itm_french_rapier,itm_padded_cloth,itm_civilian_outfit_a,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   # def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (130) | wp_throwing (90),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  # ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   # [itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_mail_shirt,itm_haubergeon,itm_leather_boots,itm_norman_helmet,itm_mail_coif,itm_helmet_with_neckguard,itm_saddle_horse,itm_courser],
   # def_attrib|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  # ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   # [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_cuir_bouilli,itm_banded_armor,itm_hide_boots,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_hunter],
   # def_attrib|level(25),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],
  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

#peasant - retainer - footman - man-at-arms -  knight
  ["swadian_recruit","Swadian Recruit","Swadian Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_civilian_outfit_a,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  ["swadian_militia","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_bolts,itm_spiked_club,itm_french_rapier,itm_boar_spear,itm_french_rapier,
    itm_padded_cloth,itm_arming_cap,itm_arming_cap,itm_ankle_boots,itm_wrapping_boots],
   def_attrib|level(9),wp(75),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_spear,itm_french_rapier,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet],
   def_attrib|level(14),wp_melee(85),knows_common|knows_ironflesh_2|knows_shield_2|knows_athletics_2|knows_power_strike_2,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry","Swadian Infantry","Swadian Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pike,itm_french_rapier,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
    itm_civilian_outfit_a,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   def_attrib|level(25),wp_melee(135),knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_french_rapier,itm_french_rapier,itm_club,itm_voulge,
    itm_padded_cloth,itm_ankle_boots,itm_arming_cap,itm_arming_cap],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_b,
    itm_civilian_outfit_a,itm_leather_boots,itm_ankle_boots,itm_norman_helmet,itm_segmented_helmet],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (100) | wp_throwing (90),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter","Swadian Sharpshooter","Swadian Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bolts,],
   str_14 | agi_10 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_lance,itm_french_rapier,itm_bastard_sword_b,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,
    itm_haubergeon,itm_mail_with_surcoat,itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_warhorse,itm_hunter],
   def_attrib|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    itm_civilian_outfit_a,itm_cuir_bouilli,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_charger,itm_warhorse,itm_gauntlets,itm_mail_mittens],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves,itm_french_rapier,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_french_rapier,itm_french_rapier,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_civilian_outfit_a,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman?
  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_stones,itm_tab_shield_kite_a, itm_tab_shield_kite_a,
    itm_civilian_outfit_a, itm_rawhide_coat,itm_austrian_fusiliers_shoes],
   def_attrib|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_spear,itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(60),knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_sword_khergit_1,itm_french_rapier,itm_french_rapier,itm_french_rapier,
    itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (110) | wp_crossbow (70) | wp_throwing (70),knows_ironflesh_1|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_voulge,itm_sword_khergit_2,itm_french_rapier,itm_french_rapier,itm_french_rapier,
    itm_studded_leather_coat,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (140) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_3|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_c,itm_spear,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_civilian_outfit_a,itm_studded_leather_coat,itm_austrian_fusiliers_shoes,itm_saddle_horse],
   def_attrib|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,
    itm_civilian_outfit_a,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   def_attrib|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_fighting_axe,itm_bardiche,itm_battle_axe,itm_fighting_axe,
    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   def_attrib|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_spear,
    itm_studded_leather_coat,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_hunter],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe,itm_lance,itm_lance,
    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_boots,itm_plate_boots,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_hunter, itm_warhorse_steppe,itm_leather_gloves],
   def_attrib|level(26),wp_one_handed (120) | wp_two_handed (140) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves,itm_french_rapier,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],


  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows,itm_club,itm_spear,itm_french_rapier,
    itm_steppe_cap,itm_nomad_cap_b,itm_steppe_armor,itm_austrian_fusiliers_shoes,itm_khergit_leather_boots],
   def_attrib|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_french_rapier,itm_javelin,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_a,itm_khergit_armor,itm_steppe_armor,itm_austrian_fusiliers_shoes,itm_khergit_leather_boots,itm_steppe_horse,itm_saddle_horse],
   def_attrib|level(10),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (80) | wp_crossbow (60) | wp_throwing (80),knows_common|knows_riding_4|knows_power_draw_3|knows_power_throw_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
  [itm_arrows,itm_light_lance,itm_french_rapier,itm_sword_khergit_2,itm_spear,
   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,itm_khergit_leather_boots,itm_hide_boots,itm_spiked_helmet,itm_nomad_cap,itm_steppe_horse,itm_hunter],
   def_attrib|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_power_throw_2|knows_horse_archery_3|knows_shield_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_french_rapier,itm_bodkin_arrows,itm_arrows,itm_javelin,
    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (110) | wp_crossbow (80) | wp_throwing (110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_spear,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_javelin,itm_tab_shield_small_round_c,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser],
   def_attrib|level(21),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (130) | wp_crossbow (90) | wp_throwing (130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_horse_archery_7|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_c,itm_courser,itm_warhorse_steppe,itm_warhorse_steppe,itm_warhorse_steppe],
   def_attrib|level(23),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (150) | wp_archery (110) | wp_crossbow (110) | wp_throwing (110),knows_riding_7|knows_power_strike_4|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_4|knows_horse_archery_1|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves,itm_french_rapier,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_austrian_fusiliers_shoes],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],


  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_hatchet,itm_spear,
    itm_blue_tunic,itm_hide_boots,itm_austrian_fusiliers_shoes],
   def_attrib|level(6),wp(50),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_fighting_axe,itm_one_handed_war_axe_a,itm_spear,itm_javelin,itm_throwing_axes,
    itm_leather_cap,itm_skullcap,itm_nomad_vest,itm_leather_boots,itm_austrian_fusiliers_shoes],
   def_attrib|level(10),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,
    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_javelin,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_civilian_outfit_a,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_sword_viking_3_small,itm_great_axe,itm_one_handed_battle_axe_c,itm_throwing_spears,itm_heavy_throwing_axes,itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_rawhide_coat,itm_hatchet,itm_french_rapier,itm_hide_boots],
   str_10 | agi_5 | int_4 | cha_4|level(11),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (60) | wp_throwing (60),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_axe,itm_french_rapier,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
   str_11 | agi_5 | int_4 | cha_4|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (95) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_sword_viking_2,itm_fighting_axe,itm_two_handed_axe,itm_french_rapier,itm_mail_shirt,itm_mail_shirt,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (95) | wp_two_handed (95) | wp_polearm (95) | wp_archery (120) | wp_crossbow (95) | wp_throwing (95),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves,itm_french_rapier,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_civilian_outfit_a,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_civilian_outfit_a,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],


  ["rhodok_tribesman","Rhodok Tribesman","Rhodok Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_pitch_fork,
    itm_civilian_outfit_a,itm_wrapping_boots,itm_austrian_fusiliers_shoes,itm_head_wrappings,itm_straw_hat],
   def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_spear,itm_pike,itm_spear,itm_falchion,
    itm_felt_hat_b,itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_wrapping_boots,itm_austrian_fusiliers_shoes],
   def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_pike,itm_war_spear,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_aketon_green,itm_ragged_outfit,itm_austrian_fusiliers_shoes,itm_leather_boots],
   def_attrib|level(14),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (115) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_glaive,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   def_attrib|level(19),wp_one_handed (115) | wp_two_handed (115) | wp_polearm (130) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_glaive,itm_military_hammer,itm_military_cleaver_c,
    itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (115) | wp_polearm (155) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_french_rapier,itm_bolts,
    itm_arena_tunic_green,itm_felt_hat_b,itm_common_hood,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_french_rapier,itm_bolts,
    itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_austrian_fusiliers_shoes],
   def_attrib|level(15),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (105) | wp_throwing (90),knows_common|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_french_rapier,itm_club_with_spike_head,itm_french_rapier,itm_bolts,
    itm_leather_cap,itm_felt_hat_b,itm_aketon_green,itm_leather_boots],
   def_attrib|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_flintlock_rifle,itm_steel_bolts,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (100) | wp_crossbow (140) | wp_throwing (100),knows_common|knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_medieval_b,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves,itm_french_rapier,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight


 ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,
    itm_civilian_outfit_a, itm_civilian_outfit_a],
   def_attrib|level(4),wp(60),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,itm_desert_turban,
    itm_skirmisher_armor,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
   def_attrib|level(9),wp(75),knows_common|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_arabian_sword_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_sarranid_leather_armor,itm_jarid,itm_arabian_sword_a,itm_mace_3],
   def_attrib|level(14),wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_athletics_2|knows_power_throw_2|knows_ironflesh_1|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_infantry","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_jarid,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (105) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3 | knows_power_throw_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_d, itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves,],
   def_attrib|level(25),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (75) | wp_crossbow (75) | wp_throwing (140),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_4|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_sarranid_warrior_cap,itm_sarranid_boots_a],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
 ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_arrows,itm_french_rapier,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (100) | wp_crossbow (90) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_throw_3|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_barbed_arrows,itm_arabian_sword_b,itm_mace_3,itm_french_rapier,itm_french_rapier,
    itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (130) | wp_crossbow (100) | wp_throwing (130),knows_common|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_mamluke","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_scimitar_b,itm_sarranid_two_handed_mace_1,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,
    itm_mamluke_mail,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_sarranid_veiled_helmet,itm_arabian_horse_b,itm_warhorse_sarranid,itm_scale_gauntlets,itm_mail_mittens],
   def_attrib|level(27),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

   ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],


["looter","Rabuś","Rabusie", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap,],
def_attrib|agi_11|level(12),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_riding_1|knows_athletics_2,man_face_middle_1, man_face_older_2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_toporek1,
    itm_club,
    itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,],
   def_attrib|level(10),wp(20),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_french_rapier,itm_leather_cap,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_cav_pants,itm_polish_coat_d,itm_rapier17,itm_rapier18,itm_leather_gloves, itm_polish_coat_e,itm_civil_pants,itm_civil_pants_b,itm_rapier11,itm_rapier25,itm_rapier14,itm_toporek1,],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
[itm_cav_pants,itm_polish_coat_d,itm_rapier17,itm_rapier18,itm_leather_gloves, itm_polish_coat_e,itm_civil_pants,itm_civil_pants_b,itm_rapier11,itm_rapier25,itm_rapier14,itm_toporek1,],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_french_rapier,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_nomad_vest,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_austrian_fusiliers_shoes],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_jarid,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_hide_boots,itm_austrian_fusiliers_shoes,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_hide_boots,itm_austrian_fusiliers_shoes,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_jarid,itm_french_rapier,itm_french_rapier,itm_jarid,itm_civilian_outfit_a, itm_civilian_outfit_a, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_civilian_outfit_a,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_austrian_fusiliers_shoes,itm_wrapping_boots,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_french_rapier,itm_french_rapier,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_civilian_outfit_a,itm_nordic_shield,itm_austrian_fusiliers_shoes,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_civilian_outfit_a,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_french_rapier,itm_club,itm_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_french_rapier,itm_club,itm_dress,itm_civilian_outfit_a, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_french_rapier,itm_french_rapier,itm_french_rapier,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_french_rapier,itm_civilian_outfit_a,itm_civilian_outfit_a,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_noz,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_civilian_outfit_a, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_noz,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

 
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
     itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [ itm_civilian_outfit_a,    itm_arena_tunic_white, itm_civilian_outfit_a, itm_civilian_outfit_a, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a, itm_dress,   itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_civilian_outfit_a, itm_civilian_outfit_a],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a, itm_dress,   itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_civilian_outfit_a, itm_civilian_outfit_a],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_civilian_outfit_a,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [ itm_civilian_outfit_a,   itm_civilian_outfit_a, itm_civilian_outfit_a, itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a, itm_dress,   itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [ itm_civilian_outfit_a,    itm_civilian_outfit_a, itm_civilian_outfit_a, itm_civilian_outfit_a, itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_civilian_outfit_a, itm_dress,   itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_civilian_outfit_a,itm_civilian_outfit_a,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_civilian_outfit_a,itm_civilian_outfit_a,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_civilian_outfit_a,itm_civilian_outfit_a,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_civilian_outfit_a,itm_civilian_outfit_a,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_civilian_outfit_a,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_civilian_outfit_a,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[ itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[ itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[ itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_austrian_fusiliers_shoes,itm_knife],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_civilian_outfit_a,itm_hide_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_civilian_outfit_a,itm_austrian_fusiliers_shoes, itm_sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_austrian_fusiliers_shoes, itm_sword_khergit_1],
   str_9|agi_9|int_12|cha_7|level(5),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_austrian_fusiliers_shoes, itm_sword_medieval_a],
   str_10|agi_12|int_10|cha_5|level(6),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_french_rapier, itm_arrows, itm_quarter_staff],
   str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_austrian_fusiliers_shoes, itm_sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_austrian_fusiliers_shoes, itm_sword_medieval_b_small],
   str_11|agi_8|int_7|cha_8|level(2),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_civilian_outfit_a,itm_austrian_fusiliers_shoes, itm_french_rapier, itm_bolts, itm_pickaxe],
   str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_civilian_outfit_a, itm_falchion, itm_wrapping_boots],
   str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_austrian_fusiliers_shoes, itm_staff],
   str_8|agi_7|int_13|cha_7|level(4),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_austrian_fusiliers_shoes, itm_scimitar, itm_courser],
   str_7|agi_7|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_civilian_outfit_a,itm_austrian_fusiliers_shoes, itm_sword_medieval_b_small],
   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_austrian_fusiliers_shoes, itm_sword_medieval_b_small],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_austrian_fusiliers_shoes, itm_dagger, itm_throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
   
#NPC system changes end
#Piss begin
#governers olgrel rasevas 
  ["kingdom_1_lord",  "Przywódca Konfederacji Targowickiej",  "Stanislaw August",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "Przywódca Imperium Rosyjskiego",  "Czarina Katarzyna",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Król Fryderyk II Wielki",  "Fryderyk Wilhelm",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "Cesarz Franciszek II Habsburg",  "Franciszek Habsburg",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "Generał Tadeusz Kościuszko",  "Kosciuszko",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_polish_general_uniform,     itm_rapier_b,          itm_kosciuszko_cap,       itm_cav_pants,  itm_bolts,      itm_pistolet,    itm_steppe_horse],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x000000043400200f36446db6e36db2db00000000001db6db0000000000000000, rhodok_face_old_2],
#Piss end

# Targowica

  ["knight_1_1", "Szymon Korwin-Kossakowski", "Targowica Porucznik 3", tf_hero, 0, reserved,  fac_kingdom_1, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap, itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_1_2", "Teofil Zaluski", "Targowica Porucznik 3", tf_hero, 0, reserved,  fac_kingdom_1, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap, itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_1_3", "Józef Komorowski", "Targowica Kapitan A", tf_hero, 0, reserved,  fac_kingdom_1, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap, itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_1_4", "Joachim Chreptowicz", "Targowica Rotmistrz A", tf_hero, 0, reserved,  fac_kingdom_1, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap, itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_1_5", "Józef Ankiewicz", "Major", tf_hero, 0, reserved,  fac_kingdom_1, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_1_6", "Pułkownik Antoni Swiatopelk-Czetwertynski", "Pułkownik", tf_hero, 0, reserved,  fac_kingdom_1, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_1_7", "General Franciszek Ksawery Branicki", "General Franciszek Ksawery Branicki", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_1_8", "Generał Szymon Kossakowski", "Generał Józef Kossakowski", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],

# Rosja	

# Grupa 1
  ["knight_2_1", "Porucznik A", "Rosja Porucznik A", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap, itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_2_2", "Kapitan A", "Rosja Kapitan A", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_2_3", "Major A", "Rosja Major A", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_2_4", "Pułkownik A", "Rosja Pułkownik A", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_2_5", "Generał Fiodor Denisow", "Rosja Generał A", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
# Grupa 2
  ["knight_2_6", "Porucznik B", "Rosja Porucznik 2", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_2_7", "Kapitan B", "Rosja Kapitan 2", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_2_8", "Major B", "Rosja Major B", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_2_9", "Pułkownik B", "Rosja Pułkownik B", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_2_10", "Generał Aleksander Tormasow", "Rosja Generał B", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
# Grupa 3
  ["knight_2_11", "Porucznik Piotr Bagration", "Rosja Porucznik 3", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_2_12", "Kapitan Iwan Essen", "Rosja Kapitan 3", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_2_13", "Major Fiodor Drewicz", "Rosja Major C", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_2_14", "Pułkownik  Thomas Hrabia Tomatis", "Rosja Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_2_15", "Generał Aleksandr Suworow", "Rosja Generał C", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
# Grupa 4
  ["knight_2_16", "Porucznik D", "Rosja Porucznik 4", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_2_17", "Kapitan D", "Rosja Kapitan 4", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_2_18", "Major D", "Rosja Major D", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_2_19", "Pułkownik D", "Rosja Pułkownik D", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_2_20", "Generał Mikołaj Rachmanow", "Rosja Generał D", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],  
# Grupa 5
  ["knight_2_21", "Porucznik E", "Rosja Porucznik 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_22", "Kapitan E", "Rosja Kapitan 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_23", "Major E", "Rosja Major E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_24", "Pułkownik E", "Rosja Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_25", "Generał Aleksiej Chruszczow", "Rosja Generał E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
# Grupa 6
  ["knight_2_26", "Porucznik F", "Rosja Porucznik 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_27", "Kapitan F", "Rosja Kapitan 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_28", "Major F", "Rosja Major E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_29", "Pułkownik F", "Rosja Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_30", "Generał Iwan Fersen", "Rosja Brygadier", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
# Grupa 7
  ["knight_2_31", "Porucznik G", "Rosja Porucznik 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_32", "Kapitan Michaił Lewicki", "Rosja Kapitan 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_33", "Major Adrian Denisow", "Rosja Major E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_34", "Pułkownik G", "Rosja Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_35", "Brygadier G", "Rosja Brygadier", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
# Grupa 8
  ["knight_2_36", "Porucznik H", "Rosja Porucznik 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_37", "Kapitan Jakow Kulniew", "Rosja Kapitan 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_2_38", "Major H", "Rosja Major E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2], 
  ["knight_2_39", "Pułkownik Fiodor Apraksin", "Rosja Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_officers_coat,itm_russian_officers_pants,itm_russian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2], 
  ["knight_2_40", "Generał Mikołaj Arseniew", "Rosja Brygadier", tf_hero, 0, reserved,  fac_kingdom_2, [itm_russian_general_uniform,itm_cav_pants,itm_russian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

# Prusy

# Grupa 1
  ["knight_3_1", "Por Andreas Ernst Köhn von Jaski", "Prusy Porucznik A", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_3_2", "Kapitan Gotthilf Benjamin Keibel", "Prusy Kapitan A", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_3_3", "Major Christian Friedrich von Knebel", "Prusy Major A", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_4", "Płk Friedrich Heinrich d’Embers", "Prusy Pułkownik A", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_3_5", "Książe Fryderyk Ludwik Hohenlohe", "Prusy Generał A", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
# Grupa 2  
  ["knight_3_6", "Por Franz Otto von Kleist", "Prusy Porucznik B", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_7", "Kapitan Karl Friedrich Hermann von Beeren", "Prusy Kapitan B", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_8", "Major Friedrich August von Kauffberg", "Prusy Major B", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_3_9", "Płk Johann Anton Freund", "Prusy Pułkownik B", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_3_10", "Gen Franz Ludolph Ferdinand von Wildau", "Prusy Generał B", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
# Grupa 3 
  ["knight_3_11", "Por Hermann von Boyen", "Prusy Porucznik C", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_3_12", "Kapitan Johann Friedrich von Brehmer", "Prusy Kapitan C", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_13", "Major C", "Prusy Major C", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_14", "Płk Johann Friedrich Székely", "Prusy Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],  
  ["knight_3_15", "Gen Franz Andreas von Favrat", "Prusy Generał C", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
# Grupa 4  
  ["knight_3_16", "Porucznik Lutwitz", "Prusy Porucznik D", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_3_17", "Kapitan D", "Prusy Kapitan D", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_18", "Major D", "Prusy Major D", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_3_19", "Płk Otto Christoph von Eltester", "Prusy Pułkownik D", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_20", "Gen Wilhelm Friedrich Karl von Schwerin", "Prusy Generał D", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
# Grupa 5
  ["knight_3_21", "Porucznik E", "Prusy Porucznik E", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],    
  ["knight_3_22", "Kapitan E", "Prusy Kapitan E", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_3_23", "Major E", "Prusy Major E", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_3_24", "Płk Friedrich Wilhelm Christian von Zastrow", "Prusy Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_25", "Gen Bogislav Ernst von Bonin", "Prusy Generał E", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
# Grupa 6  
  ["knight_3_26", "Porucznik G", "Prusy Porucznik G", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_27", "Kapitan G", "Prusy Kapitan G", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_28", "Major G", "Prusy Major G", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_3_29", "Płk Karl Friedrich von Langen", "Prusy Pułkownik G", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_3_30", "Gen Friedrich Leopold von Ruits", "Prusy Brygadier G", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
# Grupa 7
  ["knight_3_31", "Porucznik H", "Prusy Porucznik H", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_32", "Kapitan H", "Prusy Kapitan H", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_33", "Major H", "Prusy Major H", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_3_34", "Płk Friedrich Gottlieb von Laurens", "Prusy Pułkownik H", tf_hero, 0, reserved,  fac_kingdom_3, [itm_prussian_general_uniform,itm_cav_pants,itm_prussian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],


# Monarchia Habsburgów  
  
# Grupa 1
  ["knight_4_1", "Austria Porucznik A", "Austria Porucznik A", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(200),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_4_2", "Austria Kapitan A", "Austria Kapitan A", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(200),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_4_3", "Austria Major A", "Austria Major A", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(200),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_4", "Austria Pułkownik A", "Austria Pułkownik A", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(200),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_4_5", "Austria Generał A", "Austria Generał A", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
# Grupa 2
  ["knight_4_6", "Austria Porucznik B", "Austria Porucznik B", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_7", "Austria Kapitan B", "Austria Kapitan B", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_8", "Austria Major B", "Austria Major B", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(200),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_4_9", "Austria Pułkownik B", "Austria Pułkownik B", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(200),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_4_10", "Austria Generał B", "Austria Generał B", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(200),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
# Grupa 3
  ["knight_4_11", "Austria Porucznik C", "Austria Porucznik C", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(200),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_4_12", "Austria Kapitan C", "Austria Kapitan C", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_13", "Austria Major C", "Austria Major C", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_14", "Austria Pułkownik C", "Austria Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(200),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],  
  ["knight_4_15", "Austria Generał C", "Austria Generał C", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(220),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
# Grupa 4
  ["knight_4_16", "Austria Porucznik D", "Austria Major D", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(220),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_4_17", "Austria Kapitan D", "Austria Kapitan D", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(220),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_18", "Austria Major D", "Austria Major D", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_4_19", "Austria Pułkownik D", "Austria Pułkownik D", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(220),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_20", "Austria Generał D", "Austria Generał D", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(220),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
# Grupa 5
  ["knight_4_21", "Austria Porucznik E", "Austria Porucznik E", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(220),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],  
  ["knight_4_22", "Austria Kapitan E", "Austria Kapitan E", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(250),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_4_23", "Austria Major E", "Austria Major E", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(250),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_4_24", "Austria Pułkownik E", "Austria Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(250),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_25", "Austria Generał E", "Austria Generał E", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(250),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
# Grupa 6
  ["knight_4_26", "Austria Porucznik G", "Austria Porucznik G", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_27", "Austria Kapitan G", "Kapitan G", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_28", "Austria Major G", "Austria Major G", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_officers_coat,itm_austrian_officers_pants,itm_austrian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_4_29", "Austria Pułkownik G", "Austria Pułkownik G", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],      knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_4_30", "Austria Brygadier G", "Austria Generał G", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
# Grupa 7
  ["knight_4_31", "Austria Porucznik H", "Austria Porucznik H", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_32", "Austria Kapitan H", "Austria Kapitan H", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_33", "Austria Major H", "Austria Major H", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_4_34", "Austria Pułkownik H", "Austria Pułkownik H", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],   knight_attrib_4,wp(300),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_4_35", "Austria Brygadier H", "Austria Brygadier H", tf_hero, 0, reserved,  fac_kingdom_4, [itm_austrian_general_uniform,itm_cav_pants,itm_austrian_officers_cap,itm_hunter,itm_rapier_a, itm_pistol, itm_cartridges,],knight_attrib_5,wp(300),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

# Powstańcy Kościuszkowscy
  
  ["knight_5_1", "Porucznik Fryderyk Zugehoer", "Kosciuszkowcy Porucznik 1", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Porucznik Ludwik Brunett", "Kosciuszkowcy Porucznik 2", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Porucznik Teodor Radziejowski", "Kosciuszkowcy Porucznik 3", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Porucznik Józef Sowiński", "Kosciuszkowcy Porucznik 4", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Porucznik Walenty Borowski", "Kosciuszkowcy Porucznik 5", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  ["knight_5_6", "Kapitan Jakub Epstein", "Kosciuszkowcy Kapitan 2", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Kapitan Roch Wągrowski", "Kosciuszkowcy Kapitan 2", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Kapitan Jan Kamsetzer", "Kosciuszkowcy Kapitan 3", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Kapitan Antoni Sałacki", "Kosciuszkowcy Kapitan 4", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Kapitan Antoni Gaszyński", "Kosciuszkowcy Kapitan 5", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  ["knight_5_11", "Major Józef Pągowski", "Kosciuszkowcy Major A", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Major Augustyn Karłowski", "Kosciuszkowcy Major B", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Major Ignacy Berens", "Kosciuszkowcy Major C", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Major Konstanty Lucke", "Kosciuszkowcy Major D", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Major Maciej Walewski", "Kosciuszkowcy Major E", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  ["knight_5_16", "Pułkownik Berek Joselewicz", "Kosciuszkowcy Pułkownik A", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Pułkownik Józef Wodzicki", "Kosciuszkowcy Pułkownik B", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Pułkownik Józef Kopeć", "Kosciuszkowcy Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Pułkownik Aleksander Chlebowski", "Kosciuszkowcy Pułkownik D", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Pułkownik Piotr Strzyżewski", "Kosciuszkowcy Pułkownik E", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  ["knight_5_21", "General Jan Grochowski", "Kosciuszkowcy General A", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_a,itm_hunter,itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_22", "General Jakub Jasiński", "Kosciuszkowcy General B", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_23", "Książe Józef Poniatowski", "Kosciuszkowcy General C", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_c,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_24", "Brygadier Antoni Madaliński", "Kosciuszkowcy Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_a,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_25", "Brygadier Michal Piotrowski", "Kosciuszkowcy Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  ["knight_5_26", "Brygadier Antoni Madaliński", "Kosciuszkowcy Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_a,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_27", "Brygadier Michal Piotrowski", "Kosciuszkowcy Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_28", "Brygadier Franciszek Niesiołowski", "Kosciuszkowcy Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_polish_general_uniform,itm_cav_pants,itm_rapier_b,itm_hunter,itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_29", "Pułkownik Stefan Grabowski", "Kosciuszkowcy Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_5, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_30", "Pułkownik Jan Czyż", "Kosciuszkowcy Pułkownik D", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter,itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  
  ["knight_5_31", "Pułkownik Franciszek Bukowski", "Kosciuszkowcy Pułkownik E", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_32", "Major Kacper Cieszkowski", "Kosciuszkowcy Major D", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_33", "Major Antoni Brzechwa", "Kosciuszkowcy Major E", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],  
  ["knight_5_34", "Major Antoni Dąbrowski", "Kosciuszkowcy Major D", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_35", "Major Karol Jan Fiszer", "Kosciuszkowcy Major E", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
 
  ["knight_5_36", "Kapitan Szymon Białowiejski", "Kosciuszkowcy Kapitan 4", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_c,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_37", "Kapitan Stanisław Dulfus", "Kosciuszkowcy Kapitan 5", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_38", "Porucznik Aleksander Chlebowski", "Kosciuszkowcy Porucznik 4", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_39", "Porucznik Mikołaj Chopin", "Kosciuszkowcy Porucznik 5", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_40", "Porucznik Ignacy Neve", "Kosciuszkowcy Porucznik 5", tf_hero, 0, reserved,  fac_neutral, [itm_polish_officer_coat,itm_cav_pants,itm_rapier_b,itm_hunter, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

# Unused
  ["knight_6_1", "Kozacy Porucznik 1", "Kozacy Porucznik 1", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Kozacy Porucznik 2", "Kozacy Porucznik 2", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Kozacy Porucznik 3", "Kozacy Porucznik 3", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Kozacy Porucznik 4", "Kozacy Porucznik 4", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Kozacy Porucznik 5", "Kozacy Porucznik 5", tf_hero, 0, reserved,  fac_kingdom_6, [], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  
  ["knight_6_6", "Kozacy Kapitan 1", "Kozacy Kapitan 2", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Kozacy Kapitan 2", "Kozacy Kapitan 2", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Kozacy Kapitan 3", "Kozacy Kapitan 3", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Kozacy Kapitan 4", "Kozacy Kapitan 4", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Kozacy Kapitan 5", "Kozacy Kapitan 5", tf_hero, 0, reserved,  fac_kingdom_6, [], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
       
  ["knight_6_11", "Kozacy Major A", "Kozacy Major A", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Kozacy Major B", "Kozacy Major B", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Kozacy Major C", "Kozacy Major C", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Kozacy Major D", "Kozacy Major D", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Kozacy Major E", "Kozacy Major E", tf_hero, 0, reserved,  fac_kingdom_6, [], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  
  ["knight_6_16", "Kozacy Pułkownik A", "Kozacy Pułkownik A", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Kozacy Pułkownik B", "Kozacy Pułkownik B", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Kozacy Pułkownik C", "Kozacy Pułkownik C", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Kozacy Pułkownik D", "Kozacy Pułkownik D", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Kozacy Pułkownik E", "Kozacy Pułkownik E", tf_hero, 0, reserved,  fac_kingdom_6, [], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  
  ["knight_6_21", "Antoni Hołowaty", "Kozacy General B", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],  
  ["knight_6_22", "Kozacy General B", "Kozacy General B", tf_hero, 0, reserved,  fac_kingdom_6, [],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_6_23", "Kozacy General C", "Kozacy General C", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_6_24", "Kozacy Brygadier", "Kozacy Brygadier", tf_hero, 0, reserved,  fac_kingdom_6, [],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_6_25", "Kozacy Brygadier", "Kozacy Brygadier", tf_hero, 0, reserved,  fac_kingdom_6, [], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

# Powstańcy Węgierscy  
  
  ["knight_7_1", "Węgry Porucznik 1", "Węgry Porucznik 1", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_7_2", "Węgry Porucznik 2", "Węgry Porucznik 2", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_3", "Węgry Porucznik 3", "Węgry Porucznik 3", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_4", "Węgry Porucznik 4", "Węgry Porucznik 4", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_5", "Węgry Porucznik 5", "Węgry Porucznik 5", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  
  ["knight_7_6", "Węgry Kapitan 1", "Węgry Kapitan 2", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_7_7", "Węgry Kapitan 2", "Węgry Kapitan 2", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_8", "Węgry Kapitan 3", "Węgry Kapitan 3", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_9", "Węgry Kapitan 4", "Węgry Kapitan 4", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_10", "Węgry Kapitan 5", "Węgry Kapitan 5", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
       
  ["knight_7_11", "Węgry Major A", "Węgry Major A", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_7_12", "Węgry Major B", "Węgry Major B", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_13", "Węgry Major C", "Węgry Major C", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_14", "Węgry Major D", "Węgry Major D", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_15", "Węgry Major E", "Węgry Major E", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  
  ["knight_7_16", "Węgry Pułkownik A", "Węgry Pułkownik A", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_7_17", "Węgry Pułkownik B", "Węgry Pułkownik B", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_18", "Węgry Pułkownik C", "Węgry Pułkownik C", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_19", "Węgry Pułkownik D", "Węgry Pułkownik D", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_20", "Węgry Pułkownik E", "Węgry Pułkownik E", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_7_21", "Węgry General A", "Węgry General B", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_22", "Węgry General B", "Węgry General B", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_23", "Węgry General C", "Węgry General C", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_24", "Węgry Brygadier", "Węgry Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_25", "Węgry Brygadier", "Węgry Brygadier", tf_hero, 0, reserved,  fac_neutral, [itm_prussian_officers_coat,itm_prussian_officers_pants,itm_prussian_officers_cap,itm_rapier_a, itm_pistol, itm_cartridges,], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],

  #######################################################################################################################################################
  #######################################################################################################################################################  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_hunter,    itm_civilian_outfit_a,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_hunter,        itm_leather_boots,              itm_mail_boots,                 itm_brigandine_red,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_neutral,[itm_warhorse,  itm_civilian_outfit_a,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_civilian_outfit_a,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [             itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [         itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [           itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [            itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [         itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[           itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[      itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_a,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  # ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[      itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  # ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,   fac_commoners,[itm_civilian_outfit_a,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[      itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, 0,reserved,  fac_commoners,[itm_civilian_outfit_a,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_civilian_outfit_a,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_civilian_outfit_a,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_civilian_outfit_a,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[      itm_austrian_fusiliers_shoes         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_civilian_outfit_a,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[     itm_austrian_fusiliers_shoes         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,          itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[       itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[        itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[         itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[         itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[         itm_austrian_fusiliers_shoes     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,     itm_austrian_fusiliers_shoes],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_d,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_e,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_c,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_e,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_c,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_c,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_e,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_e,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_cav_pants,itm_polish_coat_e,itm_rapier27],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_civilian_outfit_a,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_civilian_outfit_a,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_civilian_outfit_a,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_civilian_outfit_a,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_civilian_outfit_a,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[        itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[        itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[        itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_civilian_outfit_a,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_civilian_outfit_a,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_civilian_outfit_a,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_civilian_outfit_a, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_civilian_outfit_a, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_civilian_outfit_a,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_civilian_outfit_a,          itm_austrian_fusiliers_shoes,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_civilian_outfit_a,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_civilian_outfit_a,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_civilian_outfit_a,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[        itm_austrian_fusiliers_shoes],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_civilian_outfit_a,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[        itm_austrian_fusiliers_shoes],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_civilian_outfit_a,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_civilian_outfit_a,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_civilian_outfit_a,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_civilian_outfit_a,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_civilian_outfit_a itm_kontush itm_kontush itm_kontush itm_civilian_outfit_a itm_rich_outfit
  ["town_1_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Kasztelan", "{!}Kasztelan", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,   [itm_frock_b, itm_frock_c, itm_civil_pants, itm_frock_a,itm_civil_pants_a,itm_civil_pants_b, itm_polish_coat_a, itm_polish_coat_b,itm_frock_e, itm_frock_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_austrian_fusiliers_shoes,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_austrian_fusiliers_shoes],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_civilian_outfit_a, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_civilian_outfit_a,       itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[            itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,     itm_austrian_fusiliers_shoes],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_civilian_outfit_a,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
   #############################################################################################
   ################### Werbownik NPC #############################################################
   #############################################################################################   
  ["werbownik_a","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_b","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_c","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_d","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_e","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_f","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_g","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_h","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_i","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_j","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["werbownik_end","Werbownik","Werbownik",tf_guarantee_armor,0,reserved,fac_commoners,[itm_polish_officer_coat,itm_cav_pants,itm_rapier_a,itm_hunter, itm_pistol, itm_cartridges,],def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],

#################################################################################### 
########################## NAJEMNICY ###############################################
####################################################################################  
  
  ["golota","Gołota","Gołota",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kosynier,
    itm_spiked_mace,
    itm_rogatywka,
    itm_cartridges,
	itm_flintlock_pistol,
	itm_fighting_axe,
	itm_austrian_fusiliers_shoes],
   def_attrib|level(6),wp(70),knows_power_strike_3|knows_power_throw_1|knows_riding_1|knows_athletics_3,nord_face_younger_1, nord_face_old_2],
  
 ["klusownicy","Kłusownik","Kłusownicy",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kosynier,
    itm_spiked_mace,
    itm_rogatywka,
    itm_noz,
	itm_cartridges,
	itm_flintlock_pistol,
	itm_fighting_axe,
	itm_austrian_fusiliers_shoes],
   def_attrib|level(6),wp(70),knows_power_strike_3|knows_power_throw_1|knows_riding_1|knows_athletics_3,nord_face_younger_1, nord_face_old_2], 
   
 ["przemytnik","Przemytnik","Przemytnicy",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
  [itm_club,
   itm_butchering_knife,
   itm_falchion,
   itm_civilian_outfit_a,
   itm_pelt_coat,
   itm_woolen_cap,
   itm_cartridges,
   itm_flintlock_pistol,
   itm_rawhide_coat,
   itm_wrapping_boots],
   def_attrib|level(6),wp(70),knows_power_strike_3|knows_power_throw_1|knows_riding_1|knows_athletics_3,nord_face_younger_1, nord_face_old_2], 
  
  ["najemnik","Najemnik","Najemnicy",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kosynier,
    itm_spiked_mace,
    itm_rogatywka,
    itm_noz,
    itm_cartridges,
	itm_flintlock_pistol,
	itm_fighting_axe,
	itm_austrian_fusiliers_shoes],
   def_attrib|level(6),wp(70),knows_power_strike_3|knows_power_throw_1|knows_riding_1|knows_athletics_3,nord_face_younger_1, nord_face_old_2], 
  
#################################################################################### 
########################## REGIMENTY, MOZLIWE DO NAJECIA. ##########################
####################################################################################
# Litwa
  ["lithuania_rifleman","Litewski Strzelec","Litewscy Strzelcy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(18),wp_one_handed (140)| wp_crossbow (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["lithuania_rifleman_veteran","Litewski Strzelec Weteran","Litewscy Strzelcy Weterani",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(22),wp_one_handed (160)| wp_crossbow (170) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_lithuania_rifleman","Doborowy Litewski Strzelec","Doborowi Litewscy Strzelcy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(28),wp_one_handed (190)| wp_crossbow (190) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],


  ["lithuania_fusilier","Litewski Fizylier","Litewscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (100)| wp_crossbow (110) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["lithuania_fusilier_veteran","Litewski Fizylier Weteran","Litewscy Fizylierzy Weterani",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (120)| wp_crossbow (140) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_lithuania_fusilier","Doborowy Litewski Fizylier","Doborowi Litewscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (150)| wp_crossbow (170) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
    
   
 ["kosynier","Kosynier","Kosynierzy",tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_polish_coat_a,
    itm_polish_coat_b,
    itm_kosa_a, itm_kosa_b, itm_kosa_a, itm_kosa_b,
    itm_rogatywka,itm_rogatywka_b,
	itm_civil_pants, itm_civil_pants_a,],
   def_attrib|level(6),wp(70),knows_ironflesh_1|knows_power_strike_4|knows_athletics_3,nord_face_younger_1, nord_face_old_2],
   
  ["kosynier_veteran","Kosynier Weteran","Kosynierzy Weterani",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kosynier,
   itm_rogatywka, itm_rogatywka_b,
#   itm_obuch_a, itm_obuch_b, itm_obuch_c, itm_obuch_d,
   itm_kosynier_a,
#   itm_noz,
   itm_kosa_a, itm_kosa_b, itm_kosa_a, itm_kosa_b,
   itm_civil_pants, itm_civil_pants_a,
   itm_austrian_fusiliers_shoes],
   def_attrib|level(15),wp(100),knows_ironflesh_4|knows_power_strike_5|knows_athletics_4,nord_face_young_1, nord_face_old_2],
   
 ["picked_kosynier","Grenadier","Grenadierzy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
  [itm_kosynier,
   itm_rogatywka, itm_rogatywka_b,
 #  itm_obuch_a, itm_obuch_b, itm_obuch_c, itm_obuch_d,
   itm_kosynier_a,
#   itm_kord_c, itm_kord_b, itm_kord_d, itm_kord_e,
   itm_kosa_a, itm_kosa_b, itm_kosa_a, itm_kosa_b,
   itm_civil_pants, itm_civil_pants_a, itm_civil_pants_b,
   itm_austrian_fusiliers_shoes],
   def_attrib|level(30),wp(190),wp_crossbow(90),knows_ironflesh_5|knows_power_strike_8|knows_athletics_5,nord_face_young_1, nord_face_old_2], 
   
   ["comrade_national_cavalry","Towarzysz Kawalerii Narodowej","Towarzysze Kawalerii Narodowej", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka, itm_rogatywka_b,
   itm_hunter,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_national_cavalry_pants],
   str_11 | agi_7 | int_10 | cha_6|level(14),wp_one_handed (110)| wp_firearm (90) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
     ["comrade_national_cavalry_veteran","Weteran Kawalerii Narodowej","Weterani Kawalerii Narodowej", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka, itm_rogatywka_b,
   itm_hunter,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_national_cavalry_pants],
   str_11 | agi_7 | int_10 | cha_6|level(20),wp_one_handed (150)| wp_firearm (100) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
     ["picked_comrade_national_cavalry","Doborowy Towarzysz Kawalerii Narodowej","Doborowi Towarzysze Kawalerii Narodowej", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka, itm_rogatywka_b,
   itm_hunter,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_national_cavalry_pants],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp_one_handed (190)| wp_firearm (130) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],    
   
  ["lithuania_uhlan","Litewski Ułan","Litewscy Ułani", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(18),wp_one_handed (130)| wp_firearm (180) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
  ["lithuania_uhlan_veteran","Litewski Ułan Weteran","Litewscy Ułani Weterani", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(24),wp_one_handed (180)| wp_firearm (180) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
  ["picked_lithuania_uhlan","Doborowy Litewski Ułan","Doborowi Litewscy Ułani", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(28),wp_one_handed (240)| wp_firearm (180) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],   

#Wraz z awansami rosna statystyki, nie zmienia sie ekwipunek.
   
  ["polish_rifleman","Polski Strzelec","Polscy Strzelcy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_bolts,
   itm_polish_rifleman_coat,
   itm_polish_rifleman_cap,
	itm_polish_rifleman_pants],
   str_9 | agi_6 | int_10 | cha_6|level(18),wp_polearm (140)| wp_crossbow (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["polish_rifleman_veteran","Polski Strzelec Weteran","Polscy Strzelcy Weterani",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_bolts,
   itm_polish_rifleman_coat,
   itm_polish_rifleman_cap,
	itm_polish_rifleman_pants],
   str_9 | agi_6 | int_10 | cha_6|level(24),wp_polearm (170)| wp_crossbow (180) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_polish_rifleman","Polski Doborowy Strzelec","Polscy Doborowi Strzelcy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_bolts,
   itm_polish_rifleman_coat,
   itm_polish_rifleman_cap,
	itm_polish_rifleman_pants],
   str_9 | agi_6 | int_10 | cha_6|level(28),wp_polearm (200)| wp_crossbow (210) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],


  ["polish_fusilier","Polski Fizylier","Polscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(16),wp_polearm (120)| wp_crossbow (115) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["polish_fusilier_veteran","Polski Fizylier Weteran","Polscy Fizylierzy Weterani",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(22),wp_polearm (150)| wp_crossbow(130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_polish_fusilier","Polski Doborowy Fizylier","Polscy Doborowi Fizylierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_rifle,
   itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
   itm_bolts,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(28),wp_polearm (180)| wp_crossbow (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["polish_uhlan","Polski Ułan","Polscy Ułani", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(14),wp(140)| wp_firearm (80) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
  ["polish_uhlan_veteran","Polski Ułan Weteran","Polscy Ułani Weterani", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(20),wp(180)| wp_firearm (100) ,knows_ironflesh_3|knows_athletics_1,nord_face_young_1, nord_face_old_2],
   
  ["picked_polish_uhlan","Doborowy Polski Ułan","Doborowi Polscy Ułani", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_lance,
    itm_hunter,
    itm_kosciuszkowska_szabla,
    itm_polish_uhlan_cap,
    itm_polish_uhlan_coat,
    itm_polish_uhlan_pants,],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp(230)| wp_firearm (120) ,knows_ironflesh_4|knows_athletics_1,nord_face_young_1, nord_face_old_2],    

#milicja
  ["rp_militia","Polska Milicja","Polska Milicja", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_uhlan_pants],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp_one_handed (140)| wp_crossbow (100) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2], 

  ["ros_militia","Rosyjska Milicja","Rosyjska Milicja", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_uhlan_pants],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp_one_handed (140)| wp_crossbow (100) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],  
  
  ["prus_militia","Pruska Milicja","Pruska Milicja", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_national_cavalry_pants],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp_one_handed (140)| wp_crossbow (100) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],   
   
  ["aus_militia","Austriacka Milicja","Austriacka Milicja", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_4,
   [itm_flintlock_pistol,
   itm_polish_national_cavalry_uniform,
   itm_rogatywka,
   itm_kosciuszkowska_szabla,
   itm_cartridges,
	itm_polish_uhlan_pants],
   str_11 | agi_7 | int_10 | cha_6|level(30),wp_one_handed (140)| wp_crossbow (100) ,knows_ironflesh_2|knows_athletics_1,nord_face_young_1, nord_face_old_2],   
   
   ["russian_lieutenant","Rosyjski Porucznik","Rosyjscy Porucznicy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
    itm_cartridges,
	itm_rapier_a,
    itm_rapier_b,
	itm_rapier_c,
	itm_hunter,
    itm_russian_officers_coat,
    itm_russian_officers_pants,
	itm_russian_officers_cap],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   ["prussian_lieutenant","Pruski Porucznik","Pruscy Porucznicy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
    itm_cartridges,
	itm_rapier_a,
    itm_rapier_b,
	itm_rapier_c,
	itm_hunter,
    itm_prussian_officers_coat,
    itm_prussian_officers_pants,
	itm_prussian_officers_cap],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   ["polish_lieutenant","Polski Porucznik","Polscy Porucznicy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
    itm_cartridges,
    itm_karabela,
	itm_hunter,
    itm_polish_officer_coat,
    itm_polish_officer_pants,
	itm_polish_officer_cap],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   ["austrian_lieutenant","Austriacki Porucznik","Austriaccy Porucznicy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_flintlock_pistol,
    itm_cartridges,
	itm_rapier_a,
    itm_rapier_b,
	itm_rapier_c,
	itm_hunter,
    itm_austrian_huzar_uniform,
    itm_austrian_huzar_cap,
	itm_austrian_huzar_shoes],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["zaopatrzeniowiec_1","Borys","Borys",tf_hero,0,0,fac_outlaws,
  [itm_civilian_outfit_a,
   itm_wrapping_boots],
   def_attrib|level(10),wp(160),knows_common,bandit_face1, 0x000000019a0844127b9a2854a288ad2b00000000000ee2da0000000000000000],
   
  ["zaopatrzeniowiec_2","Istvan","Istvan",tf_hero,0,0,fac_outlaws,
  [itm_falchion,
   itm_civilian_outfit_a,
   itm_wrapping_boots],
   def_attrib|level(10),wp(160),knows_common,bandit_face1, 0x000000019a0844127b9a2854a288ad2b00000000000ee2da0000000000000000],
   
 ["camp_troops","Partyzant","Partyzanci", tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_huc1,
	itm_pistolet1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   def_attrib|level(10),wp(150),knows_common,nord_face_young_1, nord_face_old_2],
  
  ###Russian TROOPS###
  
#Jaegars

  ["russian_jaegar","Rosyjski Jegier","Rosyjscy Jegrzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_execution_rifle,
   itm_russian_jaeger_coat,
   itm_russian_jaeger_cap,
	itm_bolts,
	itm_russian_jaeger_pants],
   str_13 | agi_8 | int_15 | cha_6|level(20),wp_polearm (130)| wp_crossbow (160) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
     ["russian_jaegar_veteran","Rosyjski Jegier Weteran","Rosyjscy Jegrzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
   itm_russian_jaeger_coat,
   itm_russian_jaeger_cap,
	itm_bolts,
	itm_russian_jaeger_pants],
   str_13 | agi_8 | int_15 | cha_6|level(25),wp_polearm (150)| wp_crossbow (180) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_russian_jaegar","Doborowy Rosyjski Jegier","Doborowi Rosyjscy Jegrzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
   itm_russian_jaeger_coat,
   itm_russian_jaeger_cap,
	itm_bolts,
	itm_russian_jaeger_pants],
   str_13 | agi_8 | int_15 | cha_6|level(33),wp_polearm (180)| wp_crossbow (190) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  #fusilers
  
  ["russian_fusilier","Rosyjski Fizylier","Rosyjscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_9 | agi_6 | int_10 | cha_6|level(18),wp_polearm (135)| wp_crossbow (145) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["russian_fusilier_veteran","Rosyjski Fizylier Weteran","Rosyjscy Fizylierzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_9 | agi_6 | int_10 | cha_6|level(28),wp_polearm (150)| wp_crossbow (165) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_russian_fusilier","Doborowy Fizylier","Doborowi Fizylierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_11 | agi_7 | int_10 | cha_6|level(35),wp_polearm (190)| wp_crossbow (180) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  #grenadiers
  
  ["russian_grenadier","Rosyjski Grenadier","Rosyjscy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_10 | agi_8 | int_10 | cha_6|level(20),wp_polearm (220)| wp_crossbow (170) ,knows_ironflesh_2|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["russian_grenadier_veteran","Rosyjski Grenadier Weteran","Rosyjscy Grenadierzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_11 | agi_6 | int_10 | cha_6|level(25),wp_polearm (250)| wp_crossbow (200) ,knows_ironflesh_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
   
  ["picked_russian_grenadier","Doborowy Rosyjski Grenadier","Doborowi Rosyjscy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_flintlock_rifle,
    itm_rus_fus_coat,
	itm_rus_fus_helmet,
	itm_bolts,
	itm_rus_fus_pants],
   str_12 | agi_8 | int_10 | cha_6|level(34),wp_polearm (300)| wp_crossbow (220) ,knows_ironflesh_5|knows_athletics_7,nord_face_young_1, nord_face_old_2],
   
   #Cuirassiers
   
  ["russian_cuirassier","Rosyjski Kirasjer","Rosyjscy Kirasjerzy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_french_rapier,
   itm_russian_cav_armour,
   itm_russian_cav_helmet,
   itm_russian_cav_pants,
	itm_hunter],
   def_attrib|level(17),wp(130),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_5|knows_riding_2|knows_athletics_2|knows_shield_6,nord_face_middle_1, nord_face_older_2],
   
  ["russian_cuirassier_veteran","Rosyjski Kirasjer Weteran","Rosyjscy Kirasjerzy Weterani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_french_rapier,
   itm_russian_cav_armour,
   itm_cav_pants,
	itm_leather_gloves,
	itm_hunter],
   def_attrib|level(24),wp(150),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_5|knows_riding_3|knows_athletics_3|knows_shield_6,nord_face_middle_1, nord_face_older_2],
   
  ["picked_russian_cuirassier","Doborowy Rosyjski Kirasjer","Doborowi Rosyjscy Kirasjerzy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_french_rapier,
   itm_russian_cav_armour,
   itm_cav_pants,
	itm_leather_gloves,
	itm_hunter],
   def_attrib|level(30),wp(180),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_5|knows_riding_5|knows_athletics_5|knows_shield_6,nord_face_middle_1, nord_face_older_2],
   
   #Huzars
   
  ["russian_imperial_huzar","Rosyjski Huzar","Rosyjscy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_russian_huzar_uniform,
    itm_russian_huzar_gloves,
	itm_russian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_bolts,
	itm_pistol,
	itm_russian_huzar_shoes,
	itm_hunter],
  str_13 | agi_8 | int_15 | cha_6|level(22),wp_one_handed (170)| wp_firearm (130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["russian_imperial_huzar_veteran","Rosyjski Huzar Weteran","Rosyjscy Huzarzy Weterani",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_russian_huzar_uniform,
    itm_russian_huzar_gloves,
	itm_russian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_bolts,
	itm_pistol,
	itm_russian_huzar_shoes,
	itm_hunter],
	   str_16 | agi_10 | int_17 | cha_6|level(29),wp_one_handed (200)| wp_firearm (150) ,knows_ironflesh_2|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["picked_russian_imperial_huzar","Doborowy Rosyjski Huzar","Doborowi Rosyjscy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_russian_huzar_uniform,
    itm_russian_huzar_gloves,
	itm_russian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_bolts,
	itm_pistol,
	itm_russian_huzar_shoes,
	itm_hunter],
	   str_21 | agi_14 | int_19 | cha_6|level(33),wp_one_handed (260)| wp_firearm (190) ,knows_ironflesh_3|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],

   #Cossacks
  ["russian_cossack","Rosyjski Kozak","Rosyjscy Kozacy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_11 | agi_6 | int_10 | cha_6|level(15),wp_one_handed (150)| wp_firearm (110) ,knows_ironflesh_2|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
     ["russian_cossack_veteran","Rosyjski Kozak Weteran","Rosyjscy Kozacy Weterani",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(25),wp_one_handed (190)| wp_firearm (140) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   ["picked_russian_cossack","Doborowy Rosyjski Kozak","Doborowi Rosyjscy Kozacy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(33),wp_one_handed (200)| wp_firearm (160) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
###PRUSSIA TROOPS###
   #Jaegars
  ["prussian_jaegar","Pruski Jegier","Pruscy Jegrzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_13 | agi_8 | int_15 | cha_6|level(20),wp_polearm (125)| wp_crossbow (140) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
    
 ["prussian_jaegar_veteran","Pruski Jegier Weteran","Pruscy Jegrzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_13 | agi_8 | int_15 | cha_6|level(25),wp_polearm (150)| wp_crossbow (160) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_prussian_jaegar","Doborowy Pruski Jegier","Doborowi Pruscy Jegrzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_13 | agi_8 | int_15 | cha_6|level(33),wp_polearm (180)| wp_crossbow (190) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
#Fusiliers
  ["prussian_fusilier","Pruski Fizylier","Pruscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_fusiliers_coat,
    itm_prussian_fusilier_cap,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(18), wp_polearm(180)| wp_crossbow (130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["prussian_fusilier_veteran","Pruski Fizylier Weteran","Pruscy Fizylierzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_fusiliers_coat,
    itm_prussian_fusilier_cap,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(25),wp_polearm(220)| wp_crossbow (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_prussian_fusilier","Doborowy Pruski Fizylier","Doborowi Pruscy Fizylierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_fusiliers_coat,
    itm_prussian_fusilier_cap,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(38),wp_polearm(260)| wp_crossbow (180) ,knows_ironflesh_2|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
#Grenadiers

  ["prussian_grenadier","Pruski Grenadier","Pruscy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_9 | agi_6 | int_10 | cha_6|level(22),wp_polearm (200)| wp_crossbow (180) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["prussian_grenadier_veteran","Pruski Grenadier Weteran","Pruscy Grenadierzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_9 | agi_6 | int_10 | cha_6|level(28),wp_polearm (220)| wp_crossbow (220) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_prussian_grenadier","Doborowy Pruski Grenadier","Doborowi Pruscy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_infantry_cap,
    itm_prussian_infantry_coat,
	itm_bolts,
    itm_1782_rifle,
	itm_prussian_infantry_pants],
   str_12 | agi_8 | int_10 | cha_6|level(34),wp_polearm (300)| wp_crossbow (250) ,knows_ironflesh_5|knows_athletics_7,nord_face_young_1, nord_face_old_2],
   
   #Bosniak
   
   ["bosniak","Bośniak","Bośniacy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_jatagan1,
    itm_jatagan2,
    itm_jatagan3,
    itm_bosniak_coat,
	itm_bosniak_cap,
	itm_lance,
	itm_bosniak_pants,
	itm_steppe_horse],
   def_attrib|level(17),wp(100),knows_ironflesh_1|knows_power_strike_1|knows_riding_2,nord_face_middle_1, nord_face_older_2],
   
  ["bosniak_veteran","Bośniak Weteran","Bośniacy Weterani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_jatagan1,
    itm_jatagan2,
    itm_jatagan3,
    itm_bosniak_coat,
	itm_bosniak_cap,
	itm_lance,
	itm_bosniak_pants,
	itm_steppe_horse],
   def_attrib|level(22),wp(130),knows_ironflesh_2|knows_power_strike_2|knows_riding_3,nord_face_middle_1, nord_face_older_2],
   
  ["picked_bosniak","Doborowy Bośniak","Doborowi Bośniacy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_jatagan1,
    itm_jatagan2,
    itm_jatagan3,
    itm_bosniak_coat,
	itm_bosniak_cap,
	itm_lance,
	itm_bosniak_pants,
    itm_steppe_horse,
	itm_hunter],
   def_attrib|level(26),wp(150),knows_ironflesh_3|knows_power_strike_3|knows_riding_4,nord_face_middle_1, nord_face_older_2],
   
 #Huzars
  ["prussian_huzar","Pruski Huzar","Pruscy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_huzar_uniform,
	itm_prussian_huzar_cap,
	itm_pistol,
	itm_bolts,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_prussian_huzar_shoes,
	itm_hunter],
  str_13 | agi_8 | int_15 | cha_6|level(18),wp_one_handed (170)| wp_crossbow (130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["prussian_huzar_veteran","Pruski Huzar Weteran","Pruscy Huzarzy Weterani",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_huzar_uniform,
	itm_prussian_huzar_cap,
	itm_pistol,
	itm_bolts,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_prussian_huzar_shoes,
	itm_hunter],
  str_16 | agi_10 | int_17 | cha_6|level(26),wp_one_handed (200)| wp_crossbow (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["picked_prussian_huzar","Doborowy Pruski Huzar","Doborowi Pruscy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_prussian_huzar_uniform,
	itm_prussian_huzar_cap,
	itm_pistol,
	itm_bolts,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_prussian_huzar_shoes,
	itm_hunter],
   str_21 | agi_14 | int_19 | cha_6|level(34),wp_one_handed (260)| wp_firearm (190) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  
   ###AUSTRIAN TROOPS###
  #Austrian Huzar 
  
  ["austrian_huzar","Austriacki Huzar","Austriaccy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [itm_austrian_huzar_uniform,
    itm_austrian_huzar_gloves,
	itm_austrian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_austrian_huzar_shoes,
	itm_hunter],
   str_13 | agi_8 | int_15 | cha_6|level(18),wp_one_handed (170)| wp_firearm (130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["austrian_huzar_veteran","Austriacki Huzar Weteran","Austriaccy Huzarzy Weterani",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [itm_austrian_huzar_uniform,
    itm_austrian_huzar_gloves,
	itm_austrian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_austrian_huzar_shoes,
	itm_hunter],
  str_16 | agi_10 | int_17 | cha_6|level(30),wp_one_handed (200)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
  ["picked_austrian_huzar","Doborowy Austriacki Huzar","Doborowi Austriaccy Huzarzy",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [itm_austrian_huzar_uniform,
    itm_austrian_huzar_gloves,
	itm_austrian_huzar_cap,
	itm_rapier19,
	itm_rapier20,
	itm_rapier21,
	itm_austrian_huzar_shoes,
	itm_hunter],
  str_21 | agi_14 | int_19 | cha_6|level(42),wp_one_handed (260)| wp_firearm (190) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
	   
	#Austrian Grenadiers
	
  ["austrian_grenadier","Austriacki Grenadier","Austriaccy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_1782_rifle,
   	itm_bolts,
	itm_austrian_grenadiers_cap,
    itm_austrian_grenadiers_uniform,
	itm_austrian_grenadiers_shoes],
   str_10 | agi_8 | int_10 | cha_6|level(20),wp_polearm (200)| wp_crossbow (150) ,knows_ironflesh_2|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["austrian_grenadier_veteran","Austriacki Grenadier Weteran","Austriaccy Grenadierzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_1782_rifle,
   	itm_bolts,
	itm_austrian_grenadiers_cap,
    itm_austrian_grenadiers_uniform,
	itm_austrian_grenadiers_shoes],
   str_10 | agi_8 | int_10 | cha_6|level(25),wp_polearm (220)| wp_crossbow (160) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_austrian_grenadier","Doborowy Austriacki Grenadier","Doborowi Austriaccy Grenadierzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_1782_rifle,
   	itm_bolts,
	itm_austrian_grenadiers_cap,
    itm_austrian_grenadiers_uniform,
	itm_austrian_grenadiers_shoes],
   str_10 | agi_8 | int_10 | cha_6|level(38),wp_polearm (260)| wp_crossbow (170) ,knows_ironflesh_2|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   	#Austrian Fusiliers
	
  ["austrian_fusilier","Austriacki Fizylier","Austriaccy Fizylierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_austrian_fusiliers_cap,
    itm_austrian_fusiliers_uniform,
	itm_flintlock_rifle,
	itm_bolts,
	itm_austrian_fusiliers_shoes],
   str_9 | agi_5 | int_6 | cha_6|level(18), wp_polearm(100)| wp_crossbow (110) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["austrian_fusilier_veteran","Austriacki Fizylier Weteran","Austriaccy Fizylierzy Weterani",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_austrian_fusiliers_cap,
    itm_austrian_fusiliers_uniform,
	itm_flintlock_rifle,
	itm_bolts,
	itm_austrian_fusiliers_shoes],
   str_11 | agi_6 | int_8 | cha_6|level(25),wp_polearm(120)| wp_crossbow (130) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_austrian_fusilier","Doborowy Austriacki Fizylier","Doborowy Austriacki Fizylier",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_austrian_fusiliers_cap,
    itm_austrian_fusiliers_uniform,
	itm_flintlock_rifle,
	itm_bolts,
	itm_austrian_fusiliers_shoes],
   str_13 | agi_7 | int_9 | cha_6|level(38),wp_polearm(150)| wp_crossbow (170) ,knows_ironflesh_2|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
   #Austrian Cuirassier
   ["austrian_cuirassier","Austriacki Kirasjer","Austriaccy Kirasjerzy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_french_rapier,
    itm_austrian_cav_armour,
    itm_austrian_cav_helmet,
    itm_austrian_cav_pants,
	itm_hunter],
   def_attrib|level(20),wp(150),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
   
  ["austrian_cuirassier_veteran","Austriacki Kirasjer Weteran","Austriaccy Kirasjerzy Weterani",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_french_rapier,
    itm_austrian_cav_armour,
    itm_austrian_cav_helmet,
    itm_austrian_cav_pants,
	itm_hunter],
   def_attrib|level(26),wp(180),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
   
  ["picked_austrian_cuirassier","Doborowy Austriacki Kirasjer","Doborowi Austriaccy Kirasjerzy",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_french_rapier,
    itm_austrian_cav_armour,
    itm_austrian_cav_helmet,
    itm_austrian_cav_pants,
	itm_hunter],
   def_attrib|level(32),wp(220),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  
  #Pandurs
  ["austrian_pandur","Pandur","Pandurzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_kaukaska_rifle,
	itm_huc1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(15),wp_polearm (120)| wp_crossbow (90) ,knows_ironflesh_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["austrian_pandur_veteran","Pandur Weteran","Pandurzy Weterani",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_kaukaska_rifle,
    itm_1782_rifle_a,
	itm_huc1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(23),wp_polearm (150)| wp_crossbow (130) ,knows_ironflesh_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["picked_austrian_pandur","Doborowy Pandur","Doborowi Pandurzy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
    itm_1782_rifle_a,
	itm_bolts,
	itm_kaukaska_rifle,
	itm_huc1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(30),wp_polearm (190)| wp_crossbow (160) ,knows_ironflesh_2|knows_athletics_3,nord_face_young_1, nord_face_old_2], 
   
 #Austrian Guards
  ["austrian_mounted_guard","Austriacki Konny Gwardzista","Austriacki Konny Gwardzista",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [],
   str_9 | agi_6 | int_10 | cha_6|level(25),wp_polearm (150)| wp_firearm (110) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
 ["austrian_mounted_guards_officer","Austriacki Oficer Konnej Gwardii","Austriacki Oficer Konnej Gwardii",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [],
  str_9 | agi_6 | int_10 | cha_6|level(45),wp_one_handed (150)| wp_firearm (110) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
     
 ["polish_cannoneer","Polski Kanonier","Polscy Kanonierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["russian_cannoneer","Rosyjski Kanonier","Rosyjscy Kanonierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["prussian_cannoneer","Pruski Kanonier","Pruscy Kanonierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["austrian_cannoneer","Austriacki Kanonier","Austriaccy Kanonierzy",tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_polish_fusiliers_coat,
   itm_polish_fusilier_cap,
	itm_polish_fusiliers_pants],
   str_9 | agi_6 | int_10 | cha_6|level(14),wp_one_handed (140)| wp_firearm (150) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  
  ##################################################################
  ####################Unique pNPC#############################
  ##################################################################
  ["szpieg","Szpieg","Captain Johann Von Schewerin",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_pistolet,
	itm_bolts,
	itm_hunter,
	itm_french_rapier,
	itm_leather_boots,
	itm_austrian_fusiliers_shoes],
    str_16 | agi_7 | int_16 | cha_10|level(50),wp_one_handed (250)| wp_firearm (210) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,0x0000000eaf00138522eb6db6db6db6db00000000001dbe000000000000000000],
  

##################################################################
#######1794 BANDITS###############################################
##################################################################
 ###OPRYSZKOWIE### 
  ["opryszek","Opryszek","Opryszkowie",0,0,0,fac_outlaws,
  [itm_club,
   itm_butchering_knife,
   itm_falchion,
   itm_civilian_outfit_a,
   itm_pelt_coat,
   itm_woolen_cap,
   itm_rawhide_coat,
   itm_wrapping_boots],
   def_attrib|level(10),wp(160),knows_common,bandit_face1, bandit_face2],
   ["chieftain","Chieftain","Chieftains",0,0,0,fac_outlaws,
   [itm_noz,
   itm_rawhide_coat,
   itm_pistolet1,
   itm_pelt_coat,
   itm_civilian_outfit_a,
   itm_bolts,
   itm_wrapping_boots],
   def_attrib|level(20),wp(160),knows_common,bandit_face1, bandit_face2],
  ["bandit_rifleman","Bandit Rifleman","Bandit Riflemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_hatchet,
   itm_club,
   itm_butchering_knife,
   itm_falchion,
   itm_rawhide_coat,
   itm_pelt_coat,
   itm_civilian_outfit_a,
   itm_civilian_outfit_a,
   itm_woolen_cap,
   itm_woolen_cap,
   itm_austrian_fusiliers_shoes,
   itm_wrapping_boots],
   def_attrib|level(20),wp(140),knows_common,bandit_face1, bandit_face2], 
  ["bandit_rider","Bandit Rider","Bandit Riders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_hatchet,
   itm_club,
   itm_butchering_knife,
   itm_falchion,
   itm_rawhide_coat,
   itm_pelt_coat,
   itm_civilian_outfit_a,
   itm_civilian_outfit_a,
   
   itm_hunter,
   itm_austrian_fusiliers_shoes,
   itm_wrapping_boots],
   def_attrib|level(20),wp(140),knows_common,bandit_face1, bandit_face2], 
  ###KOZACCY BANDYCI####
  ["cossack_rider","Cossack Serf","Cossack Riders",tf_guarantee_boots|tf_guarantee_armor|tf_mounted,0,0,fac_outlaws,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_huc1,
	itm_pistolet1,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   def_attrib|level(10),wp(100),knows_common,bandit_face1, bandit_face2], 
   ["cossack_bandit","Cossack Bandit","Cossack Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   def_attrib|level(15),wp(130),knows_common,bandit_face1, bandit_face2], 
  ["cossack_mounted_rifleman","Cossack Mounted Rifleman","Cossack Mounted Rifleman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   def_attrib|level(15),wp(130),knows_common,bandit_face1, bandit_face2], 
   
   
   #Cossacks
  ["cossack","Russian Cossack","Russian Cossacks",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(15),wp_one_handed (150)| wp_firearm (110) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
  ["cossack_veteran","Russian Cossack Vetaran","Rosyjscy Kozacy Weterani",tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_austrian_pandur_uniform_a,
    itm_austrian_pandur_uniform,
	itm_austrian_pandur_shoes,
	itm_austrian_pandur_shoes_a,
	itm_head_wrappings,
	itm_wrapping_boots,
	itm_bolts,
	itm_steppe_horse,
    itm_saddle_horse,
	itm_huc1,
	itm_pistolet1,
	itm_lance,
	itm_rapier14,
	itm_toporek1,
	itm_jatagan1,
    itm_austrian_pandur_cap_a,
	itm_austrian_pandur_cap],
   str_9 | agi_6 | int_10 | cha_6|level(25),wp_one_handed (190)| wp_firearm (140) ,knows_ironflesh_1|knows_power_draw_1|knows_athletics_3,nord_face_young_1, nord_face_old_2],
   
####Vain-END####
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_french_rapier,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_noz,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Chłop","Chłop",tf_guarantee_boots|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_coarse_tunic,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a,   itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a,   itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_civilian_outfit_a,   itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_civilian_outfit_a,   itm_woolen_hose, itm_austrian_fusiliers_shoes, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_civilian_outfit_a,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_civilian_outfit_a, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_civilian_outfit_a,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_civilian_outfit_a,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_noz,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_hide_boots, itm_saddle_horse,  itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_noz,itm_dagger,itm_french_rapier,itm_dress,itm_civilian_outfit_a, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_austrian_fusiliers_shoes, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_french_rapier, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [],
   def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [],
   def_attrib|level(21),wp(90)|wp_archery(150),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
    [],
   def_attrib|level(23),wp(130),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
    [],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_french_rapier,itm_sword_medieval_b_small,itm_red_shirt,itm_ankle_boots],
   def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_red_tunic,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wp_melee(110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_french_rapier,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_french_rapier,
    itm_civilian_outfit_a,itm_hide_boots],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_civilian_outfit_a,itm_hide_boots],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_civilian_outfit_a,itm_hide_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_french_rapier,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   def_attrib_multiplayer|level(21),wpe(80,150,60,100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5|knows_athletics_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   def_attrib_multiplayer|level(21),wp(115),knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_2|knows_horse_archery_1|knows_power_strike_2|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_french_rapier,
    itm_blue_tunic,itm_leather_boots],
   def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,
    itm_blue_tunic,itm_leather_boots],
   def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wp(105),knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_french_rapier,itm_bolts,itm_french_rapier,
    itm_tunic_with_green_cape,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_french_rapier,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wp(100),knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_french_rapier,
    itm_civilian_outfit_a, itm_sarranid_boots_b],
   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_civilian_outfit_a, itm_sarranid_boots_b],
   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,
    itm_civilian_outfit_a, itm_sarranid_boots_b,itm_saddle_horse],
   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_civilian_outfit_a,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_prussian_officers_coat,
   itm_rapier_b,
	itm_prussian_officers_pants],
   str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000ff30010c536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_french_rapier, itm_barbed_arrows, itm_scimitar, itm_tab_shield_small_round_c, itm_sumpter_horse,
    itm_leather_armor, itm_splinted_greaves],
   str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_two_handed_b, itm_sword_medieval_c, itm_tab_shield_heater_c, itm_warhorse,
    itm_guard_helmet, itm_civilian_outfit_a, itm_mail_mittens, itm_mail_boots],
   str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_mace_4, 
    itm_bascinet_3, itm_scale_armor, itm_mail_mittens, itm_mail_boots],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,
   [itm_long_axe, itm_sword_viking_1, itm_light_throwing_axes, 
    itm_nordic_fighter_helmet, itm_byrnie, itm_leather_gloves, itm_leather_boots],
   str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_french_rapier, itm_barbed_arrows, itm_barbed_arrows, itm_shortened_spear,
    itm_leather_warrior_cap, itm_civilian_outfit_a, itm_leather_gloves, itm_ankle_boots],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_french_rapier, itm_bolts, itm_sword_medieval_b_small, 
    itm_nasal_helmet, itm_civilian_outfit_a, itm_leather_gloves, itm_leather_boots],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_scimitar, itm_leather_covered_round_shield,
    itm_desert_turban, itm_skirmisher_armor, itm_leather_gloves, itm_sarranid_boots_b],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_french_rapier, itm_barbed_arrows, itm_barbed_arrows, itm_scimitar_b,
    itm_splinted_greaves, itm_lamellar_vest],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_french_rapier, itm_bodkin_arrows, itm_bodkin_arrows, itm_arabian_horse_b,
    itm_sarranid_felt_head_cloth_b, itm_sarranid_common_dress, itm_sarranid_boots_b],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar,  itm_war_spear, itm_courser,
    itm_leather_gloves, itm_fur_hat, itm_leather_boots, ],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_austrian_fusiliers_shoes],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_austrian_fusiliers_shoes],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_civilian_outfit_a,itm_austrian_fusiliers_shoes,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_austrian_fusiliers_shoes],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_civilian_outfit_a, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_civilian_outfit_a, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a,  itm_austrian_fusiliers_shoes], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a,  itm_austrian_fusiliers_shoes], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_civilian_outfit_a, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_civilian_outfit_a, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_french_rapier,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_civilian_outfit_a,itm_leather_boots, itm_austrian_fusiliers_shoes],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_bolts,itm_pistolet,itm_falchion,itm_cheap_shirt, itm_pelt_coat,itm_linen_tunic,itm_civil_pants_b,itm_spiked_club,],
   def_attrib|level(4),wp(160),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_civilian_outfit_a,itm_austrian_fusiliers_shoes],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     
  
  # 1794
  

  #Dodawac przed tym
  
] + troops1794

upgrade(troops,"prussian_fusilier","prussian_fusilier_veteran")
upgrade(troops,"prussian_fusilier_veteran","picked_prussian_fusilier")

upgrade(troops, "austrian_pandur", "austrian_pandur_veteran")
upgrade(troops, "austrian_pandur_veteran","picked_austrian_pandur")

upgrade(troops, "austrian_cuirassier", "austrian_cuirassier_veteran")
upgrade (troops, "austrian_cuirassier_veteran", "picked_austrian_cuirassier")

upgrade (troops, "austrian_grenadier","austrian_grenadier_veteran"),
upgrade (troops, "austrian_grenadier_veteran","picked_austrian_grenadier"),

upgrade (troops, "austrian_fusilier","austrian_fusilier_veteran"),
upgrade (troops, "austrian_fusilier_veteran","picked_austrian_fusilier"),

upgrade (troops, "austrian_huzar","austrian_huzar_veteran"),
upgrade (troops, "austrian_huzar_veteran","picked_austrian_huzar"),

upgrade (troops, "prussian_jaegar","prussian_jaegar_veteran"),
upgrade (troops, "prussian_jaegar_veteran","picked_prussian_jaegar"),

upgrade (troops, "comrade_national_cavalry","comrade_national_cavalry_veteran"),
upgrade (troops, "comrade_national_cavalry_veteran","picked_comrade_national_cavalry"),

upgrade (troops, "prussian_huzar","prussian_huzar_veteran"),
upgrade (troops, "prussian_huzar_veteran","picked_prussian_huzar"),

upgrade(troops,"polish_fusilier","polish_fusilier_veteran")
upgrade(troops,"polish_fusilier_veteran","picked_polish_fusilier")

upgrade(troops,"polish_uhlan","polish_uhlan_veteran")
upgrade(troops,"polish_uhlan_veteran","picked_polish_uhlan")

upgrade(troops,"polish_rifleman","polish_rifleman_veteran")
upgrade(troops,"polish_rifleman_veteran","picked_polish_rifleman")

upgrade(troops,"prussian_grenadier","prussian_grenadier_veteran")
upgrade(troops,"prussian_grenadier_veteran","picked_prussian_grenadier")

upgrade(troops,"russian_cuirassier","russian_cuirassier_veteran")
upgrade(troops,"russian_cuirassier_veteran","picked_russian_cuirassier")

upgrade(troops,"russian_fusilier","russian_fusilier_veteran")
upgrade(troops,"russian_fusilier_veteran","picked_russian_fusilier")

upgrade(troops, "lithuania_fusilier","lithuania_fusilier_veteran")
upgrade(troops, "lithuania_fusilier_veteran","picked_lithuania_fusilier")

upgrade(troops,"russian_imperial_huzar","russian_imperial_huzar_veteran")
upgrade(troops,"russian_imperial_huzar_veteran","picked_russian_imperial_huzar")

upgrade(troops,"russian_jaegar","russian_jaegar_veteran")
upgrade(troops,"russian_jaegar_veteran","picked_russian_jaegar")

upgrade(troops,"lithuania_rifleman","lithuania_rifleman_veteran")
upgrade(troops,"lithuania_rifleman_veteran","picked_lithuania_rifleman")

upgrade(troops,"lithuania_uhlan","lithuania_uhlan_veteran")
upgrade(troops,"lithuania_uhlan_veteran","picked_lithuania_uhlan")

upgrade(troops,"russian_grenadier","russian_grenadier_veteran")
upgrade(troops,"russian_grenadier_veteran","picked_russian_grenadier")

upgrade(troops,"kosynier","kosynier_veteran")
upgrade(troops,"kosynier_veteran","picked_kosynier")

upgrade(troops,"russian_cossack","russian_cossack_veteran")
upgrade(troops,"russian_cossack_veteran","picked_russian_cossack")

upgrade(troops,"bosniak","bosniak_veteran")
upgrade(troops, "bosniak_veteran","picked_bosniak")

