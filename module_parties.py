# -*- coding: utf-8 -*-
from header_common import *
from header_parties import *
from module_constants import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

Habsburgowie = fac_kingdom_4
CesarstwoRosyjskie = fac_kingdom_2

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_show_faction|pf_label_large|pf_always_visible
pf_castle = pf_is_static|pf_show_faction|pf_label_medium|pf_always_visible
pf_village = pf_is_static|pf_hide_defenders|pf_label_small|pf_always_visible

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1","Warszawa",     icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76, 6),[], 120),  
  ("town_2","Lublin",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109, -35.26),[], 170),
  ("town_3","Kraków",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.42, -92.81),[], 80),
  ("town_4","Wilno",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157, 105),[], 290), 
  ("town_5","Ryga", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127, 185),[], 175),
  ("town_6","Gdańsk",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9, 84),[], 310),
  ("town_7","Poznań",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66, 0),[], 90),  
  ("town_8","Wrocław",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.31, -61),[], 310),  
  ("town_9","Królewiec",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.3, 101),[], 150),
  ("town_10","Lwów", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(175, -98),[], 25),  
  ("town_11","Smoleńsk",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(320, 65),[], 60),
  ("town_12","Toruń",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.78, 30.17),[], 135),
  ("town_13","Słuck",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(258, 18),[], 45),     
  ("town_14","Brno",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.31, -159),[], 170),   
  ("town_15","Wiedeń",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.49, -181.75),[], 170),   
  ("town_16","Budapeszt",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.5, -209),[], 90),
  ("town_17","Koszyce",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95, -178),[], 170),
  ("town_18","Żytomierz",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274, -67),[], 170), 
  ("town_19","Petersburg",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(244, 259),[], 170),   
  ("town_20","Żylina",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36, -173),[], 170),
  ("town_21","Debreczyn",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104, -234),[], 60),
  ("town_22","Rewal", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125, 247),[], 25),
  ("town_23","Oradea",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136, -257),[], 60),

  #Zamki
  ("castle_1","Brześć",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152, -4),[],50),
  ("castle_2","Windawa",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73, 195),[],75),
  ("castle_3","Przemyśl",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.7, -98),[],100),
  ("castle_4","Goldynga",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90, 173),[],180),
  ("castle_5","Opole",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.7, -80),[],90),  
  ("castle_6","Konin",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6, -3.1),[],55),
  ("castle_7","Płock",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.38, 28.7),[],45),
  ("castle_8","Grudziądz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.6, 51.7),[],30),
  ("castle_9","Kobryń",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(195, -22),[],100),
  ("castle_10","Rzeszów",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77, -91),[],110),
  ("castle_11","Bydgoszcz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6, 41),[],75),
  ("castle_12","Kalisz",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18, -32),[],95),
  ("castle_13","Koszalin",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63, 82),[],115),
  ("castle_14","Ołomuniec",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60, -137.5),[],90),
  ("castle_15","Częstochowa",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13, -64),[],235), 
  ("castle_16","Olkusz",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8, -92),[],45),
  ("castle_17","Zamość",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132, -63),[],15),  
  ("castle_18","Poniewież",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.5, 139),[],300),
  ("castle_19","Radom",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69, -31),[],280),
  ("castle_20","Memelburg",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59, 138),[],260), 
  ("castle_21","Głogów",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.6, -34),[],120),
  ("castle_22","Sandomierz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.4, -68.4),[],260),
  ("castle_23","Preny",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(174, 83),[],80),
  ("castle_24","Żnin",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, 20),[],260),
  ("castle_25","Kielce",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42, -52),[],50),
  ("castle_26","Nowy Sącz",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38, -119),[],75),
  ("castle_27","Piła",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70, 51),[],100),
  ("castle_28","Słupsk",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, 93),[],180), 
  ("castle_29","Nowogródek",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(207, 45),[],90),
  ("castle_30","Białystok",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139, 39),[],55),
  ("castle_31","Holstin",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38, 69),[],45),  
  ("castle_32","Halicz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(198, -127),[],30),  
  ("castle_33","Równe",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(198, -70),[],110),
  ("castle_34","Opoczno",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20, -25),[],75),
  ("castle_35","Żywiec",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26, -122),[],95),
  ("castle_36","Bielawa",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81, -94),[],115),
  ("castle_37","Nitra",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15, -188),[],90),
  ("castle_38","Dyneburg",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173, 155),[],235), 
  ("castle_39","Święciany",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(189, 128),[],45),
  ("castle_40","Insterburg",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84, 94),[],15),
  ("castle_41","unused",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317, -36),[],300),
  ("castle_42","Taurogi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81, 125),[],280),
  ("castle_43","Mukaczewo",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168, -197),[],260),
  ("castle_44","Baranowicze",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(202, 25),[],260),
  ("castle_45","Mohylew",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(296, 40),[],260),
  ("castle_46","Pińsk",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236, -17),[],80),
  ("castle_47","Poprad",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60, -168),[],260),
  ("castle_48","Melk",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, -224),[],260),
  ("castle_49","Kamieniec Podolski",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(254, -143),[],260),
  ("castle_50","Linz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95, -184),[],260),
  ("castle_51","Witebsk",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(246, 131),[],260),
  ("castle_52","Gyor",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28, -197),[],260),
  ("castle_53","Bratyslawa",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54, -188),[],260),
  ("castle_54","Psków",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222, 194),[],260),
  ("castle_55","Ostróg",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230, -56),[],260),
  ("castle_56","Rawa Mazowiecka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28, -3),[],260),
  ("castle_57","Tulczyn",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317, -128),[],260), 
  ("castle_58","Ostrołęka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85, 44),[],260),  
  ("castle_59","Limbazi",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135, 205),[],260), 
  ("castle_60","Połock",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(305, 103),[],260),
  ("castle_61","Wielkie Łuki",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(298, 149),[],260),
  ("castle_62","Narwa",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197, 250),[],260), 
  ("castle_63","Juriew",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166.5, 204.7),[],260), 
  ("castle_64","Winnica",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(284, -100),[],260), 
  ("castle_65","Nowogród Wielki",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(249, 211),[],260), 
  ("castle_66","Homel",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(312, -5),[],260), 
  ("castle_67","Borysów",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(241, 78),[],260), 
  ("castle_68","Nadwórna",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(228, -120),[],260), 
  ("castle_69","Uzhhorod",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154, -180),[],260), 
  ("castle_70","Miszkolc",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106, -209),[],260), 
  ("castle_71","Chełm",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142, -40),[],260), 
# Dodane czerwiec 2013
  ("castle_72","Arad",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65, -252),[],260), 
  ("castle_73","Szeged",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19, -240),[],260), 
  ("castle_74","unused",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(317, -34),[],260), 
  ("castle_75","Mozyrz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(284, -29),[],260), 

  ("village_1", "Warka",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.5, -15.8),[], 130),#Warszawa
  ("village_2", "Łowicz",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44, -0.5),[], 170),#Warszawa
  ("village_3", "Nieporęt",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83, 16),[], 100),#Warszawa
  ("village_4", "Kałuszyn",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106, 0),[], 100),#Warszawa  
  ("village_5", "Nasielsk",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67, 23),[], 100),#Warszawa
  ("village_6", "Łomża",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115, 40),[], 100),#Warszawa
  ("village_7","Drohiczyn",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139, 8),[], 170),#Warszawa
  ("village_8","Hajnówka",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160, 18),[], 170),#Warszawa
  
  ("village_9", "Kraśnik",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87, -60),[], 100),#Lublin
  ("village_10", "Parczew",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121, -17),[], 110),#Lublin
  ("village_11", "Bełżyce",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107, -44),[], 120),#Lublin
  ("village_12", "Chełm",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145, -41),[], 100),#Lublin
  ("village_13", "Kowel",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(178, -31),[], 100),#Lublin
  
  ("village_14", "Jedrzejów",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30,-66),[], 110),#Krakow
  ("village_15", "Bochnia",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -106),[], 120),#Krakow
  ("village_16", "Polaniec",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49, -81),[], 130),#Krakow
  ("village_17", "Miechów",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12, -76),[], 170),#Krakow 
  
  ("village_18", "Druskieniki",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150, 76),[], 100),#Wilno scn_3 18-22
  ("village_19", "Uciana",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160, 127),[], 110),#Wilno
  ("village_20", "Niemenczyn",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(216, 88),[], 120),#Wilno 
  ("village_21","Kowno",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132, 107), [], 170),#Wilno  
  ("village_22","Szawle",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107, 149),[], 170),#Wilno
  
  ("village_23","Kircholm",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141, 181),[], 170),#Ryga
  ("village_24","Jelgava",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124, 171),[], 170),#Ryga
  
  ("village_25","Elbląg",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21, 78),[], 35),#Gdansk
  ("village_26","Gdynia",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.5, 92.5),[], 170),#Gdansk
  ("village_27","Wladyslawowo",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2, 104),[], 170),#Gdansk
  ("village_28","Tczew",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7, 74),[], 170),#Gdansk
  
  ("village_29","Gniezno",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42, 10),[], 100),#Poznan
  ("village_30","Oborniki",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66, 21),[], 110),#Poznan
  ("village_31","Grodzisk",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85, -7),[], 120),#Poznan
  
  ("village_32","Legnica",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84, -55),[], 130),#Wroclaw
  ("village_33","Olesnica",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54, -48),[], 170),#Wroclaw
  ("village_34","Walbrzych",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86, -77),[], 170),#Wroclaw
  
  ("village_35","Szaki",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115, 103),[], 170),#Wilno
  
  ("village_36","village36",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),#------------
  
  ("village_37","Sambor",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136, -100),[], 170),#Lwow, scn_1 37-41
  ("village_38","Stryj",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(159, -111),[], -118),#Lwow
  ("village_39","Niecieszyn",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(199,-77),[], 100),#Lwow
  ("village_40","Belz",pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154, -70),[],100),#Lwow
  ("village_41","Turka",pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129, -116),[],100),#Lwow
  
  ("village_42","Babrujsk",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 110),#Minsk
  ("village_43","Maladzjechna",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 120),#Minsk     
  
  ("village_44","Lubicz",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8, 37),[], 130),#Torun
  ("village_45","Brzesc",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(313, -158),[], 170),#Torun
  
  ("village_46","Primorsk",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.6, 103),[], 170),#Krolewiec
  ("village_47","Frombork",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28, 87),[], 170),#Krolewiec
  ("village_48","Gwardiejsk",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37, -255),[], 170),#Krolewiec
  
  ("village_49","Hodonin",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18, -236),[], 120),#Brno
  ("village_50","Iglawa",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59, -214),[], 130),#Brno  

  ("village_51","Sopron",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, -201),[], 170),#Wieden
  ("village_52","Hainfeld",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74, -194),[], 170),#Wieden
  ("village_53","Hollabrunn",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(111, -247),[], 170), #Wieden  
  ("village_54","Wagram",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(228, -71),[], 170),#Wieden -DO QUESTA 1
 
  ("village_55","Solnok",  pf_disabled|icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4, -229),[], 10),#Budapest
  ("village_56","Miszkolc",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10, -210),[], 100),#Budapest
  ("village_57","Vesprim",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27, -232),[], 110),#Budapest
  
  ("village_58","wies_wegry_patrol",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.11, -217.55),[], 170), 
  
#  ("village_55","Olesnica",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54, -46),[], 10),#Budapest
#  ("village_56","Brzeg",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170), #Budapest  
#  ("village_57","Jedrzejow",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 100),#Budapest
#  ("village_58","Suchedniow",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 110),#Budapest

  ("village_59","Jedrzejow",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 100),#Budapest
  ("village_60","Suchedniow",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 110),#Budapest
 
  ("village_61","Ostruda",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30, 60),[], 100),#Olsztyn
  ("village_62","Mragowo",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.9, 74.36),[], 110),#Olsztyn

  ("village_63","Chelmno",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 120),
  ("village_64","Zakopane",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 130),
  ("village_65","Lubowla",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),
  ("village_66","Brzeclaw",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),
  ("village_67","Hodonin",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),
  ("village_68","Polaniec",  icon_village_a|pf_village|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),
  ("village_69","Opatow",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 170),
  ("village_70","Mir",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.91, -86.05),[], 170),
  ("village_71", "Sienno",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 100),
  ("village_72", "Braslaw",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(249, 111),[], 110), 
  ("village_73", "Brzezany",  pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[], 120), 

  ("salt_mine","Salt_Mine", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[]),
  
  ("wegry_camp","Obóz Powstańców Węgierskich", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(66, -228.67),[]),
  ("rosja_camp","Obóz Powstańców Rosyjskich", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(236, -53),[]),
  
  
  ("action_litwa","Korona", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(45,-33),[], 200),
  ("action_korona","Litwa", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(155,126),[], 200),
  ("action_prusy_1","Poznań", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(-37, 6),[], 200),
  ("action_prusy_2","Toruń", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(56, 85),[], 200),
  ("action_rosja_1","Słuck", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(225, 13),[], 200),
  ("action_rosja_2","Żytomierz", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(256, -76),[], 200),
  ("action_wegry_1","Lwów", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(133, -91),[], 200),
  ("action_wegry_2","Lwów", icon_manifest|pf_always_visible|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(24, -113),[], 200),

  ("action_end", "fdsfdsfd",icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155,126),[]),
  
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[]),# Karczmy  
# Docelowo trzeba szukać lepszych nazw dla niektórych.
  ("karczma_a","Pod Jelenim Porożem",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(110, 26),[]),#Inn Under Deer Antlers
  ("karczma_b","Pod Piórem Kogucim",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(84, -58),[]),#Inn Under Cock's Feather
  ("karczma_c","Ostatni grosz",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10, -18),[]),#The Last Penny
  ("karczma_d","Karczma Rzym",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(14, -81),[]),
  ("karczma_e","Pod Kuflem Świętego Anulfa",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230, -28),[]),
  ("karczma_f","Stara Karczma",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[]),
  ("karczma_g","Pod Kozim Kłem",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.99,-146),[]),
  ("karczma_h","Karczma Hulanka",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(82.3, 9.78),[]),
  ("karczma_i","Pod Wiedniem",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.4,52.7),[]),
  ("karczma_j","Pod Kielichem",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62,-99),[]),
  ("karczma_k","Wymysłów",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43,-62),[]),
  ("karczma_l","Piekiełko",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(116,-29),[]),
  ("karczma_m","Przekora",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(246,34),[]),
  ("karczma_n","Zawada",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(137.81,77.10),[]),
  ("karczma_o","Pod Złamana Kopią",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91,147),[]),
  ("karczma_p","Łapiguz",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(219,106),[]),
  ("karczma_r","Nazłość",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100,-40),[]),
  ("karczma_t","Utrata",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41,68),[]),
  ("karczma_u","Sodoma",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56,2),[]),
  ("karczma_w","Ucieszka",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44,-36),[]),
  ("karczma_x","Gospoda Czekaj",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35,-124),[]),
  ("karczma_y","Trzy Żubry",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(125,-85),[]),
  ("karczma_yy","Mitręga",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral2,0,ai_bhvr_hold,0,(45,-9),[]),
  ("karczma_yyy","Gospoda Bezdenna",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16,26),[]),
  ("karczma_aa","Gospoda Trzy Słowa",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(288, -47),[]),
  ("karczma_ab","Karczma Na Przełęczy",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.92, -130.89),[]),
  ("karczma_ac","Austeria Kamieniecka",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(245, -149),[]),
  ("karczma_ad","Pod Czarnym Barankiem",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107, -174),[]),
  ("karczma_ae","Gospoda Czerwony Rum",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28, -225),[]),
  ("karczma_af","Pod Królową Gęsią Nóżką",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43, -174),[]),
  ("karczma_ag","Pod Duńską Koroną",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.5, -231),[]),
  ("karczma_ah","Gospoda Czarcie Kopyto",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41, -206),[]),
# Karczmy  
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -22),[]),
  #pf_no _label-umiejscowianie modeli na mapie i wylaczanie funkcji lokacji.

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28,-178),[], 100),


#  bridge_a
 ("Bridge_1","{!}1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.7, -47.10),[], -140.8),
 ("Bridge_2","{!}2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.7, -83.7),[], 4.28),
 ("Bridge_3","{!}3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.8, -20.6),[], 64.5),
 ("Bridge_4","{!}4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.9, 27.4),[], -5.13),
 ("Bridge_5","{!}5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.36, 4.9),[], -73.5),
 ("Bridge_6","{!}6",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.3, -91.3),[], -73.5),
 ("Bridge_7","{!}7",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.7, 12.84),[], -64),
 ("Bridge_8","{!}8",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.8, 90.3),[], -90),
 ("Bridge_9","{!}9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.3, 15.4),[], 6),
 ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.28, -122.77),[], -73.5),
 ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -99),[], 6),
 ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.5, -68.2),[], -90),
 ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79, 35),[], -17.7),
 ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.59, -120.08),[], 66.6),
 ("Bridge_15","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.36, -43.59),[], 35),
 ("Bridge_16","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.67, -31.01),[], -45),
 ("Bridge_17","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.45, -189.1),[], 3),
 ("Bridge_18","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.48, -102.58),[], -63.5),
 ("Bridge_19","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155, -18.8),[], -53.5), 
 ("Bridge_20","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.43, 246.69),[], -53.5), 
 ("Bridge_21","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.24, 183.9),[], -33.5), 
 ("Bridge_22","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(218.2, 161.24),[], -33.5),  
 ("Bridge_23","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(278.52, -129),[], -53.5), 
 ("Bridge_24","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.28, -263.36),[], 0), 
 ("Bridge_25","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.86, -208.03),[], 85), 
 
 ("Windmill_1","{!}1", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.84, -72.80),[], -140.8),
 ("Windmill_2","{!}2", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(284, -61),[], 4.28),
 ("Windmill_3","{!}3", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118, 121),[], 64.5),
 ("Windmill_4","{!}4", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167, -111),[], -2.13),
 ("Windmill_5","{!}5", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(281, -140),[], 71),
 ("Windmill_6","{!}6", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90, -82),[], -73.5),
 ("Windmill_7","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72, -76),[], -64),
 ("Windmill_8","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62, 34),[], 312),
 ("Windmill_9","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79, -11),[], 192),
 ("Windmill_10","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19, 80),[], -112),
 ("Windmill_11","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68, 84),[], 12),
 ("Windmill_12","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(240, 163),[], 112),
 ("Windmill_13","{!}7", icon_map_windmill|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15, -237),[], -112),

 
  ("polish_guards_spawn_point"  ,"polish_guards_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77, -1),[(trp_looter,15,0)]),
  ("russian_guards_spawn_point"  ,"russian_guards_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.93, -124.53),[(trp_looter,15,0)]),
  ("austrian_guards_spawn_point"  ,"austrian_guards_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62, -31),[(trp_looter,15,0)]),
  ("prussian_guards_spawn_point"  ,"prussian_gruards_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130,-55),[(trp_looter,15,0)]),
  ("kosynierzy_lubelscy_spawn_point"  ,"kosynierzy_lubelscy_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134, -56),[(trp_looter,15,0)]),
  ("kosynierzy_krakowscy_spawn_point"  ,"kosynierzy_krakowscy_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27, -62),[(trp_looter,15,0)]),
  ("kosynierzy_spawn_point"  ,"kosynierzy_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27, -62),[(trp_looter,15,0)]),
  ("kosynierzy_a_spawn_point"  ,"kosynierzy_a_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27, -62),[(trp_looter,15,0)]),
  ("powstancy_kosciuszkowscy_spawn_point"  ,"powstancy_kosciuszkowscy_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95, 53),[(trp_looter,15,0)]),
  ("wisnicka_straz_zamkowa_spawn_point" ,"wisnicka_straz_zamkowa_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20, -126),[(trp_looter,15,0)]),
  ("russian_cossacks_spawn_point"  ,"russian_cossacks_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(223, -97),[(trp_looter,15,0)]),
  ("kosciuszkowcy"  ,"kosciuszkowcy_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41, -83),[(trp_looter,15,0)]),
  
  
  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("cossack_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("opryszkowie_spawn_point","the robbers",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-81, -101),[(trp_looter,4,60)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, 110),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(75.89, -4.35),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(75.89, -4.35),[(trp_looter,15,0)]),



 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

  ("1podroz_1", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19, -92),[], 100),
  ("1podroz_2", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29, -86),[], 100),
  ("1podroz_3", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40, -81),[], 100),
  ("1podroz_4", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52, -76),[], 100),
  ("1podroz_5", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63, -66),[], 100),
  ("1podroz_6", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68, -56),[], 100),
  ("1podroz_7", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78, -44),[], 100),
  ("1podroz_8", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89, -49),[], 100),
  ("1podroz_9", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95, -41),[], 100),
  ("1podroz_10", "Training Field",  icon_training_ground|pf_disabled|pf_hide_defenders|pf_is_static|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108, -36),[], 100),
  
  ("spawn_point_wojsko1"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(245,-52),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko2"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(248, -108),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko3"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(245, -30),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko4"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(276, -148),[(trp_looter,15,0)],0),  
  ("spawn_point_wojsko5"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(323, -81),[(trp_looter,15,0)],0),
  # Markery wlaczone
  ("spawn_point_wojsko6"   ,"{!}looter_sp",pf_disabled|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(127, -175),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko7"   ,"{!}looter_sp",pf_disabled|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(155, -212),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko8"   ,"{!}looter_sp",pf_disabled|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(80, -205),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko9"   ,"{!}looter_sp",pf_disabled|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(36, -216),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko10"   ,"{!}looter_sp",pf_disabled|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(70, -160),[(trp_looter,15,0)],0),
#Pierwsze 5 dla kozakow, drugie 5 dla powstancow wegierskich 
  ("spawn_point_wojsko11"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(143, 167),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko12"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(156, 204),[(trp_looter,15,0)],0),  
  ("spawn_point_wojsko13"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(225, 211),[(trp_looter,15,0)],0),  
  ("spawn_point_wojsko14"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(302, 126),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko15"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(248, 108),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko16"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(260, 41),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko17"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(230, -141),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko18"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(280, -147),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko19"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(301, -111),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko20"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(299, 54),[(trp_looter,15,0)],0),
  
  ("spawn_point_wojsko21"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(6, -217),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko22"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(84, -184),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko23"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(22, -187),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko24"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(37, -218),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko25"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(1, -175),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko26"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(115, -240),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko27"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(130, -203),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko28"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(66, -156),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko29"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(108, -170),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko30"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(53, -251),[(trp_looter,15,0)],0),
  ("spawn_point_wojsko31"   ,"{!}looter_sp",pf_disabled|pf_is_static|icon_manifest, no_menu, pt_none, fac_kingdom_7,0,ai_bhvr_hold,0,(58, -196),[(trp_looter,15,0)],0),
  
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(237, -72),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(135, -253),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  
  
  ("zasadzka_spawn_wegry_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(44.44, -199.38), [(trp_looter,15,0)]),
  ("zasadzka_spawn_wegry_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(62.18, -201.26 ),[(trp_looter,15,0)]),
  ("zasadzka_spawn_wegry_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(85, -156),[(trp_looter,15,0)]),
  ("zasadzka_spawn_wegry_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(49.47, -197),[(trp_looter,15,0)]),
  ("zasadzka_spawn_wegry_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(129, -258),[(trp_looter,15,0)]),
  ("zasadzka_spawn_rosja_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(277.32, -122.32),[(trp_looter,15,0)]),
  ("zasadzka_spawn_rosja_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(236.45, -74.01),[(trp_looter,15,0)]),
  ("zasadzka_spawn_rosja_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(235.69, -39.62),[(trp_looter,15,0)]),
  ("zasadzka_spawn_rosja_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(288, -71),[(trp_looter,15,0)]),
  ("zasadzka_spawn_rosja_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(238.89, 23.56),[(trp_looter,15,0)]),
  ("zasadzka_spawn_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(238.89, 23.56),[(trp_looter,15,0)]),
  
  
  ("qbron1"                  ,"{!}last_spawn_point",    icon_map_marker|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(117.7,-165.5),[]),
  ("qbron2"                  ,"{!}last_spawn_point",    icon_map_marker|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(126,-213),[]),
  ("qoboz"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(236, -53),[]),
  ("qoboz2"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(11.5, -209),[]),
  ("qmanifest1"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  ("qmanifest2"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  
  ("q3zdrajcy1"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  ("q3zdrajcy2"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  ("q3zdrajcy3"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  
  ("quniwersal1"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  ("quniwersal2"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  ("quniwersal3"                  ,"{!}last_spawn_point",    icon_manifest|pf_disabled|pf_is_static|pf_no_label|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(226, -104),[]),
  
  ("dowodca4"                  ,"Wiejska parafia",    icon_village_snow_burnt_a|pf_disabled|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(98, -186),[]),


  ("looters_spawn_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(110, 26),[(trp_looter,15,0)]),
  ("looters_spawn_b","Pod Piórem Kogucim",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84, -58),[]),
  ("looters_spawn_c","Ostatni grosz",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10, -18),[]),
  ("looters_spawn_d","Karczma Rzym",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14, -81),[]),
  ("looters_spawn_e","Pod Kuflem Świętego Anulfa",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230, -28),[]),
  ("looters_spawn_f","Stara Karczma",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.23,-161.09),[]),
  ("looters_spawn_g","Pod Kozim Kłem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.71,-147.28),[]),
  ("looters_spawn_h","Karczma Hulanka",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.3, 9.78),[]),
  ("looters_spawn_i","Pod Wiedniem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.4,52.7),[]),
  ("looters_spawn_j","Pod Kielichem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62,-99),[]),
  ("looters_spawn_k","Wymysłów",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43,-62),[]),
  ("looters_spawn_l","Piekiełko",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116,-29),[]),
  ("looters_spawn_m","Przekora",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(254,29),[]),
  ("looters_spawn_n","Zawada",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136,77),[]),
  ("looters_spawn_o","Pod Złamaną Kopią",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63,124),[]),
  ("looters_spawn_p","Łapiguz",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(219,106),[]),
  ("looters_spawn_r","Nazłość",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188, 179),[]),
  ("looters_spawn_t","Utrata",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41,68),[]),
  ("looters_spawn_u","Sodoma",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56,2),[]),
  ("looters_spawn_w","Ucieszka",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44,-36),[]),
  ("looters_spawn_x","Gospoda Czekaj",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35,-124),[]),
  ("looters_spawn_y","Trzy Żubry",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125,-85),[]),
  ("looters_spawn_y","none",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138,-214),[]),
  ("looters_spawn_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
 
  ("zbojnicy_spawn_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(110, 26),[(trp_looter,15,0)]),
  ("zbojnicy_spawn_b","Pod Piorem Kogucim",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84, -58),[]),
  ("zbojnicy_spawn_c","Ostatni grosz",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10, -18),[]),
  ("zbojnicy_spawn_d","Karczma Rzym",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14, -81),[]),
  ("zbojnicy_spawn_e","Pod Kuflem Swietego Anulfa",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(230, -28),[]),
  ("zbojnicy_spawn_f","Stara Karczma",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.23,-161.09),[]),
  ("zbojnicy_spawn_g","Pod Kozim Klem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15,-146),[]),
  ("zbojnicy_spawn_h","Karczma Hulanka",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.3, 9.78),[]),
  ("zbojnicy_spawn_i","Pod Wiedniem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.4,52.7),[]),
  ("zbojnicy_spawn_j","Pod Kielichem",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62,-99),[]),
  ("zbojnicy_spawn_k","Wymyslow",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43,-62),[]),
  ("zbojnicy_spawn_l","Piekielko",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116,-29),[]),
  ("zbojnicy_spawn_m","Przekora",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(254,29),[]),
  ("zbojnicy_spawn_n","Zawada",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136,77),[]),
  ("zbojnicy_spawn_o","Pod Zlamana Kopia",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63,124),[]),
  ("zbojnicy_spawn_p","Lapiguz",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(219,106),[]),
  ("zbojnicy_spawn_r","Nazlosc",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100,-40),[]),
  ("zbojnicy_spawn_t","Utrata",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41,68),[]),
  ("zbojnicy_spawn_u","Sodoma",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56,2),[]),
  ("zbojnicy_spawn_w","Ucieszka",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44,-36),[]),
  ("zbojnicy_spawn_x","Gospoda Czekaj",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35,-124),[]),
  ("zbojnicy_spawn_y","Trzy Zubry",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125,-85),[]),
  ("zbojnicy_spawn_y","none",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138,-214),[]),
  ("zbojnicy_spawn_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  
  ("przemytnicy_spawn_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(9, -91),[(trp_looter,15,0)]),
  ("przemytnicy_spawn_b","Pod Piorem Kogucim",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154, 99),[]),
  ("przemytnicy_spawn_c","Ostatni grosz",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114, 187),[]),
  ("przemytnicy_spawn_d","Karczma Rzym",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(306, -65),[]),
  ("przemytnicy_spawn_e","Pod Kuflem Swietego Anulfa",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163, -188),[]),
  ("przemytnicy_spawn_f","Stara Karczma",icon_village_a|pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79,-185),[]),
  ("przemytnicy_spawn_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(-2, -225),[(trp_looter,15,0)]),
 
  ("qinfiltracja","Kryjówka", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127, -104),[]),

  ("ataman_1","Stanica Kozacka", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68, -252),[], 120),  
  ("ataman_2","Stanica Kozacka", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(267, -45),[], 120),  
  ("ataman_3","Stanica Kozacka", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(289, -149),[], 120),  
  ("ataman_4","Stanica Kozacka", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(264, -87),[], 120),  
  
  ("ataman_5","Stanica Węgierska", pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68, -252),[], 120),  
  ("ataman_6","Stanica Węgierska", pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68, -252),[], 120),  
  ("ataman_7","Stanica Węgierska", pf_disabled|icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68, -252),[], 120),  

  ("wojsko_1","Obóz Wojsk", icon_village_snow_deserted_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.6, -73),[], 120),  
  ("wojsko_2","Obóz Wojsk", icon_village_snow_deserted_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.28, -18.58),[], 120),  
  ("wojsko_3","Obóz Wojsk", icon_village_snow_deserted_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121, -3),[], 120),  
  ("wojsko_4","Obóz Wojsk", icon_village_snow_deserted_a|pf_disabled|pf_is_static|pf_hide_defenders|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152, 125),[], 120),  
  
  
  ("terrain_mountains","Hideout", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1, -143),[]),
  ("terrain_plain","Hideout", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41, -27),[]),
  ("terrain_steppe","Hideout", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(323, -96),[]),
  ("terrain_end","Hideout", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1, -143),[]),
  ("qkryjowkamaruderow","Kryjówka", icon_camp|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81, -244),[]),

  ]
