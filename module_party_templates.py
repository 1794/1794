# -*- coding: utf-8 -*-
from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),
  ("marker"," ",icon_map_marker,pf_is_static|pf_no_label|pf_always_visible,fac_neutral,merchant_personality,[]),
  ("marker2"," ",icon_manifest,pf_is_static|pf_no_label|pf_always_visible,fac_neutral,merchant_personality,[]),
  ("egzekucja"," ",icon_manifest,pf_is_static|pf_no_label|pf_always_visible,fac_neutral,merchant_personality,[]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50)]),

  ("deserters","Dezerterzy",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
  ("rabusie","Łupieżcy",icon_axeman|carries_goods(3),0,fac_outlaws,bandit_personality,[]),
  ("zbojnicy","Zbójnicy",icon_axeman|carries_goods(3),0,fac_outlaws,bandit_personality,[]),
  ("przemytnicy","Przemytnicy",icon_axeman|carries_goods(10),0,fac_outlaws,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("zasadzka_x"," ",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_iksinski,1,1,pmf_is_prisoner)]),
  ("porwanakobietabandyci","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_porwanakobieta,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_iksinski,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Targowiczanie",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_zdradat1,1,1), (trp_zdradat2,1,1), (trp_zdradat3,1,1),(trp_picked_russian_cuirassier,25,25)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rp_militia,2,2),]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,8,8),]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,9,9),]),
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_lithuania_rifleman,8,8),]), 
  ("kingdom_1_reinforcements_e", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_lithuania_fusilier,9,9),]),  

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ros_militia,2,2),]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,8,8),]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,9,9),]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_prus_militia,2,2),]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_prussian_fusilier,8,8),]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_prussian_jaegar,9,9),]),

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_aus_militia,2,2),]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_austrian_fusilier,8,8),]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_austrian_pandur,9,9),]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rp_militia,2,2),]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,8,8),]), 
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,9,9),]),  

  ("kingdom_6_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ros_militia,2,2),]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,8,8),]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,9,9),]),

  ("rosja_patrol","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_kingdom_2,soldier_personality,[(trp_steppe_bandit,10,15)]),
  ("wegry_patrol","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_kingdom_4,soldier_personality,[(trp_steppe_bandit,10,15)]),

  ("powstancy_wegry_patrol","Powstańcy Węgierscy",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_kingdom_4,soldier_personality,[(trp_steppe_bandit,10,15)]),
  ("powstancy_rosja_patrol","Kozacy",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_kingdom_4,soldier_personality,[(trp_steppe_bandit,10,15)]),

  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  ("zasadzka","Zasadzka",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders|pf_quest_party|pf_always_visible,0,fac_neutral,bandit_personality,[]),#(trp_russian_grenadier,1,1),(trp_russian_fusilier,20,20),(trp_russian_grenadier,20,20)

  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),
  ("kryjowka_maruderow","Kryjowka Maruderow",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
 
#Patrole
  ("borys","Russian Border Guards",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_looter,10,20)]),
  ("qdostarczbron2","Konspirator",icon_khergit|carries_goods(2),0,fac_neutral,bandit_personality,[(trp_qdostarczbron2_1,1,1),]),
  ("regiment","Regiment",icon_gray_knight,0,fac_commoners,soldier_personality,[]),
  ("szpieg","Szpieg",icon_axeman|carries_goods(0),0,fac_neutral,soldier_personality,[(trp_szpieg,1,1)]),
  ("qszpieg","Szpieg",icon_axeman|carries_goods(0),0,fac_neutral,soldier_personality,[(trp_qszpieg,1,1)]),
  ("cannoners","Artyleria",icon_axeman|carries_goods(0)|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_looter,1,1)]),
  ("ojciec","Podróżni",icon_axeman|carries_goods(0)|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_ojciec,1,1),(trp_dama,1,1)]),
  ("qinfiltracja","Bandyta",icon_axeman|carries_goods(0)|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_qinfiltracjat1,1,1),]),
  ("qprzyczolek","Kozacy",icon_gray_knight|carries_goods(0)|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_qprzyczolekt1,1,1),(trp_looter,100,200)]),
  ("Uciekinier","Chorąży Świstacki",icon_gray_knight|carries_goods(0)|pf_quest_party,0,fac_neutral,soldier_personality,[(trp_uciekinier,1,1),]),

# ("kingdom_litwa_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,30,30),]),
# ("kingdom_litwa_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
# ("kingdom_litwa_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_litwa_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,50,50),]),
# ("kingdom_litwa_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,120,120)]),
# ("kingdom_litwa_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_litwa_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,30,30),]),
# ("kingdom_litwa_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,100,100),]),
# ("kingdom_litwa_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,50,50),]),
# ("kingdom_litwa_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,300,300),]),
# ("kingdom_litwa_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_litwa_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,60,60),]),
# ("kingdom_litwa_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,200,200),]),
# ("kingdom_litwa_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,100,100),]),
# ("kingdom_litwa_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,30,30),]),
# ("kingdom_litwa_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,300,300),]),
# ("kingdom_litwa_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_kosynier,120,120),]),
# ("kingdom_litwa_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,200,200),]),
# ("kingdom_korona_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,30,30),]),
# ("kingdom_korona_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
# ("kingdom_korona_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_korona_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,50,50),]),
# ("kingdom_korona_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,120,120)]),
# ("kingdom_korona_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_korona_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,30,30),]),
# ("kingdom_korona_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,100,100),]),
# ("kingdom_korona_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,50,50),]),
# ("kingdom_korona_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,300,300),]),
# ("kingdom_korona_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
# ("kingdom_korona_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,60,60),]),
# ("kingdom_korona_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,200,200),]),
# ("kingdom_korona_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,100,100),]),
# ("kingdom_korona_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,200,200),]),
# ("kingdom_korona_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,300,300),]),
# ("kingdom_korona_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_kosynier,200,200),]),
# ("kingdom_korona_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,200,200),]),
  
  
  
  
  #Porucznik "Pluton piechoty liniowej"
  ("kingdom_1_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,30,30),]),
  ("kingdom_2_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,30,30),]),
  ("kingdom_3_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_jaegar,30,30),]),
  ("kingdom_4_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_fusilier,30,30),]),
  ("kingdom_5_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,30,30),]),
  ("kingdom_6_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,30,30),]),
  ("kingdom_7_porucznik", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,30,30),]),
  
  #Kapitan "Kompania piechoty liniowej"
  ("kingdom_1_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,60,60),]),
  ("kingdom_2_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,60,60),]),
  ("kingdom_3_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_jaegar,60,60),]),
  ("kingdom_4_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_fusilier,60,60),]),
  ("kingdom_5_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
  ("kingdom_6_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
  ("kingdom_7_kapitan_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,60,60),]),
  
  #Kapitan "Pluton lekkiej piechoty"
  ("kingdom_1_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,30,30),]),
  ("kingdom_2_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,30,30),]),
  ("kingdom_3_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_fusilier,30,30),]),
  ("kingdom_4_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_pandur,30,30),]),
  ("kingdom_5_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
  ("kingdom_6_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,30,30),]),
  ("kingdom_7_kapitan_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,30,30),]),
  
  #Rotmistrz "Szwadron lekkiej kawalerii"
  ("kingdom_1_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,30,30),]),
  ("kingdom_2_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,30,30),]),
  ("kingdom_3_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_huzar,30,30),]),
  ("kingdom_4_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_huzar,30,30),]),
  ("kingdom_5_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,30,30),]),
  ("kingdom_6_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,30,30),]),
  ("kingdom_7_rotmistrz", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,30,30),]),
  
  #Major "Batalion piechoty liniowej"
  ("kingdom_1_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,100,100),]),
  ("kingdom_2_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,100,100)]),
  ("kingdom_3_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_jaegar,100,100)]),
  ("kingdom_4_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_fusilier,100,100)]),
  ("kingdom_5_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,100,100)]),
  ("kingdom_6_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,100,100)]),
  ("kingdom_7_major_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,100,100)]),

  #Major "Kompania lekkiej piechoty"
  ("kingdom_1_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,60,60),]),
  ("kingdom_2_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,60,60),]),
  ("kingdom_3_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_fusilier,60,60),]),
  ("kingdom_4_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_pandur,60,60),]),
  ("kingdom_5_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,60,60),]),
  ("kingdom_6_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,60,60),]),
  ("kingdom_7_major_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,60,60),]),
  
  #Major "Pluton grenadierów"
  ("kingdom_1_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,30,30),]),
  ("kingdom_2_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,30,30),]),
  ("kingdom_3_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_grenadier,30,30),]),
  ("kingdom_4_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_grenadier,30,30),]),
  ("kingdom_5_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,60,60),]),
  ("kingdom_6_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
  ("kingdom_7_major_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,30,30),]),
  
  #Major "Pułk lekkiej kawalerii"
  ("kingdom_1_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,60,60),]),
  ("kingdom_2_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,60,60),]),
  ("kingdom_3_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_bosniak,60,60),]),
  ("kingdom_4_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_huzar,60,60),]),
  ("kingdom_5_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,60,60),]),
  ("kingdom_6_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,60,60),]),
  ("kingdom_7_major_d", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cossack,60,60),]),
  
  #Major "Szwadron ciężkiej kawalerii"
  ("kingdom_1_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,30,30),]),
  ("kingdom_2_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,30,30),]),
  ("kingdom_3_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_huzar,30,30),]),
  ("kingdom_4_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_cuirassier,30,30),]),
  ("kingdom_5_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,30,30),]),
  ("kingdom_6_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,30,30),]),
  ("kingdom_7_major_e", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,30,30),]),
  
  #Pułkownik "Regiment piechoty liniowej"
  ("kingdom_1_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,150,150),]),
  ("kingdom_2_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,150,150),]),
  ("kingdom_3_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_jaegar,150,150),]),
  ("kingdom_4_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_fusilier,150,150),]),
  ("kingdom_5_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,150,150),]),
  ("kingdom_6_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,150,150),]),
  ("kingdom_7_pulkownik_a", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_jaegar,150,150),]),

  #Pułkownik "Batalion lekkiej piechoty"
  ("kingdom_1_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,100,100),]),
  ("kingdom_2_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,100,100),]),
  ("kingdom_3_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_fusilier,100,100),]),
  ("kingdom_4_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_pandur,100,100),]),
  ("kingdom_5_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,100,100),]),
  ("kingdom_6_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,100,100),]),
  ("kingdom_7_pulkownik_b", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,100,100),]),

  #Pułkownik "Kompania grenadierów"
  ("kingdom_1_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,60,60),]),
  ("kingdom_2_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,60,60),]),
  ("kingdom_3_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_prussian_grenadier,60,60),]),
  ("kingdom_4_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_austrian_grenadier,60,60),]),
  ("kingdom_5_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_kosynier,60,60),]),
  ("kingdom_5_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
  ("kingdom_6_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_polish_fusilier,60,60),]),
  ("kingdom_7_pulkownik_c", "{!}pt", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,60,60),]),
  
  #Pułkownik "Brygada lekkiej kawalerii"
  ("kingdom_1_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cossack,120,120),]),
  ("kingdom_2_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cossack,120,120),]),
  ("kingdom_3_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_bosniak,120,120),]),
  ("kingdom_4_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_austrian_huzar,120,120),]),
  ("kingdom_5_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,120,120),]),
  ("kingdom_6_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_comrade_national_cavalry,120,120),]),
  ("kingdom_7_pulkownik_d", "Brygada lekkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cossack,120,120),]),

  #Pułkownik "Pułk ciężkiej kawalerii"
  ("kingdom_1_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,60,60),]),
  ("kingdom_2_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,60,60),]),
  ("kingdom_3_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_prussian_huzar,60,60),]),
  ("kingdom_4_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_austrian_cuirassier,60,60),]),
  ("kingdom_5_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,60,60),]),
  ("kingdom_6_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_polish_uhlan,60,60),]),
  ("kingdom_7_pulkownik_e", "Pułk ciężkiej kawalerii", 0, 0, fac_commoners, 0, [(trp_russian_cuirassier,60,60),]),

  #General "Batalion piechoty gwardii"
  ("kingdom_1_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_grenadier,100,100),]),
  ("kingdom_2_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_grenadier,100,100),]),
  ("kingdom_3_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_prussian_grenadier,100,100),]),
  ("kingdom_4_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_austrian_fusilier,100,100),]),
  ("kingdom_5_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_polish_rifleman,100,100),]),
  ("kingdom_6_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_polish_rifleman,100,100),]),
  ("kingdom_7_general_a", "Batalion piechoty gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_grenadier,100,100),]),
  
  #General "Regiment lekkiej piechoty"
  ("kingdom_1_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,150,150),]),
  ("kingdom_2_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,150,150),]),
  ("kingdom_3_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_prussian_fusilier,150,150),]),
  ("kingdom_4_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_austrian_pandur,150,150),]),
  ("kingdom_5_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,150,150),]),
  ("kingdom_6_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_polish_rifleman,150,150),]),
  ("kingdom_7_general_b", "Regiment lekkiej piechoty", 0, 0, fac_commoners, 0, [(trp_russian_fusilier,150,150),]),
  
  #General "Batalion grenadierów"
  ("kingdom_1_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,100,100),]),
  ("kingdom_2_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,100,100),]),
  ("kingdom_3_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_prussian_grenadier,100,100),]),
  ("kingdom_4_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_austrian_grenadier,100,100),]),
  ("kingdom_5_general_c", "Batalion kosynierów", 0, 0, fac_commoners, 0, [(trp_kosynier,100,100),]),
  ("kingdom_6_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_kosynier,100,100),]),
  ("kingdom_7_general_c", "Batalion grenadierów", 0, 0, fac_commoners, 0, [(trp_russian_grenadier,100,100),]),

  #Brygadier "Brygada kawalerii gwardii"
  ("kingdom_1_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_imperial_huzar,120,120),]),
  ("kingdom_2_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_imperial_huzar,120,120),]),
  ("kingdom_3_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_prussian_huzar,120,120),]),
  ("kingdom_4_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_austrian_cuirassier,120,120),]),
  ("kingdom_5_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_polish_uhlan,120,120),]),
  ("kingdom_6_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_polish_uhlan,120,120),]),
  ("kingdom_7_brygadier", "Brygada kawalerii gwardii", 0, 0, fac_commoners, 0, [(trp_picked_russian_imperial_huzar,120,120),]),
  
  ("regiments_end", "KONIEC REGIMENTOW COKOLWIEK DODAWAC PO TYM", 0, 0, fac_commoners, 0, [(trp_picked_russian_imperial_huzar,120,120),]),
]
