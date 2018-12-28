# -*- coding: utf-8 -*-
from header_common import *
from header_operations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *
from ID_parties import *
from ID_quests import *

MinimumPartySize = 75

WaveLordsLimit = 7 #12

etap4_scripts = [
	("getClosestRegion",[
		(store_script_param_1, ":faction"),
		(store_script_param_2, ":faction2"),
		
		(call_script, "script_faction_get_position", ":faction"),
			
		(assign, ":region", -1),
			
		(assign, ":min", 9999999),
		(try_for_range, ":party", towns_begin, towns_end),
			(party_slot_ge, ":party", TownRegionSize, 1),
			(store_faction_of_party, ":fac", ":party"),
			(eq, ":fac", ":faction2"),
			(party_get_position, pos1, ":party"),
			(get_distance_between_positions, ":dist", pos0, pos1),
			(lt, ":dist", ":min"),
			(assign, ":min", ":dist"),
			(assign, ":region", ":party"),
		(try_end),
		
		(assign, ReturnValue, ":region"),
	]),
	
	
	("getFactionTarget",
	[
		(store_script_param_1, ":faction"),
		
		(faction_set_slot, Rosja, RegionPrior+0, "p_town_13"),
		(faction_set_slot, Rosja, RegionPrior+1, "p_town_18"),
		(faction_set_slot, Rosja, RegionPrior+2, "p_town_10"),
		(faction_set_slot, Rosja, RegionPrior+3, "p_town_7"),
		(faction_set_slot, Rosja, RegionPrior+4, "p_town_12"),
		(faction_set_slot, Rosja, RegionPrior+5, "p_town_4"),
		(faction_set_slot, Rosja, RegionPrior+6, "p_town_2"),
		(faction_set_slot, Rosja, RegionPrior+7, "p_town_1"),
		(faction_set_slot, Rosja, RegionPrior+8, "p_town_3"),

			
		(faction_set_slot, Austria, RegionPrior+0, "p_town_2"),
		(faction_set_slot, Austria, RegionPrior+1, "p_town_1"),
		(faction_set_slot, Austria, RegionPrior+2, "p_town_3"),
		(faction_set_slot, Austria, RegionPrior+3, "p_town_4"),
		(faction_set_slot, Austria, RegionPrior+4, "p_town_7"),
		(faction_set_slot, Austria, RegionPrior+5, "p_town_10"),
		(faction_set_slot, Austria, RegionPrior+6, "p_town_12"),
		(faction_set_slot, Austria, RegionPrior+7, "p_town_13"),
		(faction_set_slot, Austria, RegionPrior+8, "p_town_18"),
		
		(faction_set_slot, Prusy, RegionPrior+0, "p_town_1"),
		(faction_set_slot, Prusy, RegionPrior+1, "p_town_2"),
		(faction_set_slot, Prusy, RegionPrior+2, "p_town_3"),
		(faction_set_slot, Prusy, RegionPrior+3, "p_town_4"),
		(faction_set_slot, Prusy, RegionPrior+4, "p_town_7"),
		(faction_set_slot, Prusy, RegionPrior+5, "p_town_10"),
		(faction_set_slot, Prusy, RegionPrior+6, "p_town_12"),
		(faction_set_slot, Prusy, RegionPrior+7, "p_town_13"),
		(faction_set_slot, Prusy, RegionPrior+8, "p_town_18"),
		
		(assign, ":region", -1),
		(assign, ":end", 9),
		(try_for_range, ":i", 0, ":end"),
			(store_add, ":slot", RegionPrior, ":i"),
			(faction_get_slot, ":region", ":faction", ":slot"),
			(store_faction_of_party, ":fac", ":region"),
			(eq, ":fac", Kosciuszkowcy),
			(assign, ":end", -1),
		(try_end),
		(assign, ReturnValue, ":region"),
	]),
	
	("waveStart",
	[
		(store_script_param_1, ":faction"),
		(store_script_param_2, ":region"),
		
		(assign, "$Etap4CurrentWaveFaction", ":faction"),
		(try_begin),
			(neg|is_between, ":region", towns_begin, towns_end), # invalid region given
			##take the closest enemy region
			# (call_script, "script_getClosestRegion", ":faction", Kosciuszkowcy),
			
			(call_script, "script_getFactionTarget", ":faction"),
			(assign, ":region", ReturnValue),
			
			
		(try_end),
		
		(try_begin),
			(eq, ":region", -1),
			]+debugMessage("@ERROR: [waveStart] region == -1", 0xd42121)+[
		(try_end),
		
		
		(str_store_party_name, s1, ":region"),
		(str_store_faction_name, s0, ":faction"),
		]+debugMessage("@INFO: [waveStart] {s0} started wave towards {s1}", 0x00007f)+[
		(faction_get_slot, ":waves", ":faction", FactionWaves),
		(val_add, ":waves", 1),
		(faction_set_slot, ":faction", FactionWaves, ":waves"),
		
		(faction_get_slot, ":no", ":faction", WaveNo),
		(val_add, ":no", 1),
		
		(faction_set_slot, ":faction", WaveActive, 1),
		(faction_set_slot, ":faction", WaveNo, ":no"),
		(faction_set_slot, ":faction", WaveRegion, ":region"),
		(faction_set_slot, ":faction", WaveHours, 40),
		(faction_set_slot, ":faction", WaveState, WaveState_Wait),
		
		(assign, "$Etap4State", Etap4_Wave),
		(assign, "$Etap4Substate",0),
		
		(try_for_range, ":lord", lords_begin, lords_end),
			# (store_troop_faction, ":fac", ":lord"),
			# (eq, ":fac", ":faction"),
			(troop_set_slot, ":lord", TroopActiveInWave, 0),
		(try_end),
	]),
	
	("waveActive",
	[
		(store_script_param_1, ":faction"),
		(faction_slot_eq, ":faction", WaveActive, 1),
	]),
	
	("waveEnd",
	[
		(store_script_param_1, ":faction"),
		(faction_set_slot, ":faction", WaveActive, 0),
		(faction_set_slot, ":faction", WaveState, -1),
		(assign, "$Etap4LastWaveFaction", ":faction"),
		
		(try_for_range, ":lord", lords_begin, lords_end),
			(store_troop_faction, ":fac", ":lord"),
			(eq, ":fac", ":faction"),
			(troop_set_slot, ":lord", TroopActiveInWave, 0),
			(troop_get_slot, ":party", ":lord", slot_troop_leaded_party),
			(gt, ":party", 0),
			(party_is_active, ":party"),
			
			(troop_get_slot, ":bound", ":lord", BoundLocation),
			
			(try_begin),
				(gt, ":bound", 0),
				(call_script, "script_PartyGiveOrder", ":party", spai_holding_center, ":bound"),
			(else_try),
				(call_script, "script_PartyGiveOrder", ":party", spai_undefined, -1),
			(try_end),
		(try_end),
		(assign, "$Etap4State", Etap4_CounterWave),
		(assign, "$Etap4Substate",0),
		(assign, "$Etap4Time",20*24),
		# (assign, "$Etap4State", Etap4_Wait),
		# (assign, "$Etap4Substate",0),
		# (assign, "$Etap4Time",24*5),
	]),
	
	("waveSetState",
	[
		(store_script_param_1, ":faction"),
		(store_script_param_2, ":state"),
		(faction_set_slot, ":faction", WaveState, ":state"),
	]),
	
	("waveGetNextCastleTarget",
	[
		(store_script_param_1, ":faction"),
		
		(faction_get_slot, ":region", ":faction", WaveRegion),
		(assign, ReturnValue, -1),
		
		(party_get_slot, ":num", ":region", TownRegionSize),
		(store_add, ":end", TownRegion, ":num"),
		(try_for_range, ":slot", TownRegion+0, ":end"),
			(party_get_slot, ":castle", ":region", ":slot"),
			
			(store_faction_of_party, ":fac", ":castle"),
			(store_relation, ":relation", ":fac", ":faction"),
			
			(neq, ":fac", ":faction"),
			(lt, ":relation", 0),
			
			(assign, ReturnValue, ":castle"),
			(assign, ":end", 0),
		(try_end),
	]),
	
	("waveUpdate",
	[
		(store_script_param_1, ":faction"),
		
		(faction_get_slot, ":state", ":faction", WaveState),
		
		(faction_get_slot, ":hrs", ":faction", WaveHours),
		(val_sub, ":hrs", 1),
		(faction_set_slot, ":faction", WaveHours, ":hrs"),
		
		(assign, reg0, ":hrs"),
		(assign, reg1, ":state"),
		]+debugMessage("@INFO: [waveUpdate][{reg1}] wave will last for {reg0} hours", 0x00007f)+[
		
		(try_begin),
			(neq, ":state", WaveState_Wait),
			(le, ":hrs", 0),
			(call_script, "script_waveEnd", ":faction"),
		(try_end),
		
		(faction_get_slot, ":state", ":faction", WaveState),
		
		(try_begin),
			(eq, ":state", WaveState_Wait),
			(neg|faction_slot_ge, ":faction", WaveHours, 2),
			
			(faction_set_slot, ":faction", WaveHours, 24*20),
			(call_script, "script_waveSetState", ":faction", WaveState_Gather),
		(else_try),
			(eq, ":state", WaveState_Gather),
			
			(assign, ":total_lords_num", 0),
			(assign, ":active_lords_num", 0),
			
			(try_for_range, ":lord", lords_begin, lords_end),
				(lt, ":active_lords_num", WaveLordsLimit),
				(store_troop_faction, ":fac", ":lord"),
				(eq, ":fac", ":faction"),
				
				(val_add, ":total_lords_num", 1),
				
				(troop_get_slot, ":party",":lord",slot_troop_leaded_party),
				(party_is_active, ":party"),
				(gt, ":party", 0),
				
				(1,"script_GetPartyLimit", ":party"),
				(assign, ":max_size", reg0),
				(party_get_num_companions, ":cur_size", ":party"),
				(store_mul, ":ratio",":cur_size", 100),
				(val_div, ":ratio", ":max_size"),
				(ge, ":ratio", MinimumPartySize),
				
				(troop_set_slot, ":lord", TroopActiveInWave, 1),
				(val_add, ":active_lords_num", 1),
			(try_end),
			
			
			
			(assign, reg0, ":active_lords_num"),
			(assign, reg1, ":total_lords_num"),
			]+debugMessage("@{reg0}/{reg1}")+[
	
			(call_script, "script_waveSetState", ":faction", WaveState_Mayhem),
			
		(else_try),
			(eq, ":state", WaveState_Mayhem),
			
			(assign, ":active_lords", 0),
			
			##Call back weakened lords
			(try_for_range, ":lord", lords_begin, lords_end),
				(store_troop_faction, ":fac", ":lord"),
				(eq, ":fac", ":faction"),
				(troop_slot_ge, ":lord", TroopActiveInWave, 1),
				(val_add, ":active_lords", 1),
				(troop_get_slot, ":party",":lord",slot_troop_leaded_party),
				(try_begin),
					(party_is_active, ":party"),
					(gt, ":party", 0),
					
					(1,"script_GetPartyLimit", ":party"),
					(assign, ":max_size", reg0),
					(party_get_num_companions, ":cur_size", ":party"),
					(store_mul, ":ratio",":cur_size", 100),
					(val_div, ":ratio", ":max_size"),
					(lt, ":ratio", 40),
					
					
					(troop_get_slot, ":bound", ":lord", BoundLocation),
					(call_script, "script_party_set_ai_state", ":party", spai_holding_center, ":bound"),
					(assign, ":party", -1),
				(try_end),
				
				(neg|party_is_active, ":party"),
				(troop_set_slot, ":lord", TroopActiveInWave, 0),
				(val_sub, ":active_lords", 1),
			(try_end),
			
			##Summon new lords
			(try_for_range, ":lord", lords_begin, lords_end),
				(lt, ":active_lords", WaveLordsLimit),
				(store_troop_faction, ":fac", ":lord"),
				(eq, ":fac", ":faction"),
				
				(val_add, ":total_lords_num", 1),
				
				(troop_get_slot, ":party",":lord",slot_troop_leaded_party),
				(party_is_active, ":party"),
				(gt, ":party", 0),
				
				(1,"script_GetPartyLimit", ":party"),
				(assign, ":max_size", reg0),
				(party_get_num_companions, ":cur_size", ":party"),
				(store_mul, ":ratio",":cur_size", 100),
				(val_div, ":ratio", ":max_size"),
				(ge, ":ratio", MinimumPartySize),
				
				(troop_set_slot, ":lord", TroopActiveInWave, 1),
				(val_add, ":active_lords", 1),
			(try_end),
			
					
			(faction_get_slot, ":region", ":faction", WaveRegion),
			(assign, ReturnValue, -1),
			
			(party_get_slot, ":region_size", ":region", TownRegionSize),
			(store_faction_of_party, ":town_owner", ":region"),
			
			(assign, reg0, ":region"),
			(assign, reg1, ":region_size"),
			]+debugMessage("@{reg0} size: {reg1}")+[
			(assign, ":captured", 0),
			
			(store_add, ":end", TownRegion, ":region_size"),
			
			(try_for_range, ":slot", TownRegion+0, ":end"),
				(party_get_slot, ":castle", ":region", ":slot"),
				
				(store_faction_of_party, ":fac", ":castle"),
				(store_relation, ":relation", ":fac", ":faction"),
				(this_or_next|eq, ":fac", ":faction"),
				(ge, ":relation", 0),
				(str_store_party_name, s0, ":castle"),
				]+debugMessage("@{s0} considered captured...")+[
				(val_add, ":captured", 1),
			(try_end),
			
			(store_div, ":half_region_size", ":region_size", 2),
			
			(store_relation, ":rel", ":faction", ":town_owner"),
			
			(try_begin),
				(neq, ":town_owner", ":faction"),
				(lt, ":rel", 0),
				(ge, ":captured", ":half_region_size"),
				(assign, ":target", ":region"),
			(else_try),
				(call_script, "script_waveGetNextCastleTarget", ":faction"),
				(assign, ":target", ReturnValue),
			(try_end),
			(assign, reg0, ":target"),
			]+debugMessage("@{reg0} is next target")+[
			(try_begin),
				(eq, ":target", -1),# no more targets
				## TODO
			(try_end),
			
			(try_begin),
				(neq, ":target", -1),
				
				(try_for_range, ":lord", lords_begin, lords_end),
					(store_troop_faction, ":fac", ":lord"),
					(eq, ":fac", ":faction"),
					
					(str_store_troop_name, s1, ":lord"),
					
					(troop_get_slot, ":party",":lord",slot_troop_leaded_party),
					(party_is_active, ":party"),
					(gt, ":party", 0),
					(troop_slot_eq, ":lord", TroopActiveInWave, 1),
					(neg|party_slot_eq, ":party", slot_party_ai_object, ":target"),
					(neg|party_slot_eq, ":party", slot_party_ai_state, spai_besieging_center),
					
					
					(str_store_party_name, s0, ":target"),
					
					]+debugMessage("@{s1} to attack {s0}")+[
					(call_script, "script_partyGiveOrder", ":party", spai_besieging_center, ":target"),
					(party_set_aggressiveness, ":party", 14),
					(party_set_courage, ":party", 14),
					(troop_raise_skill, ":lord", "skl_spotting", 5),
					# (party_ignore_player, ":party", 0),
				(try_end),
			(try_end),
			
			(assign, ":break", 0),
			(try_for_range, ":lord", lords_begin, lords_end),
				(eq, ":break", 0),
				(store_troop_faction, ":fac", ":lord"),
				(eq, ":fac", ":faction"),
				(troop_slot_eq, ":lord", TroopActiveInWave, 1),
				(troop_get_slot, ":party",":lord",slot_troop_leaded_party),
				(party_is_active, ":party"),
				(gt, ":party", 0),
					
					
				(store_distance_to_party_from_party, ":dist", ":party", "p_main_party"),
				(le, ":dist", 5),
				
				(party_get_num_companions, ":enemy", ":party"),
				(party_get_num_companions, ":player", "p_main_party"),
				
				(ge, ":enemy", ":player"),
				
				(assign, ":break", 1),
				
				(gt, ":party", 0),
				(party_is_active, ":party"),
				(call_script, "script_partyGiveOrder", ":party", spai_engaging_army, "p_main_party"),
			(try_end),
		(try_end),
	]),
	
	
	
	
	("regionGetFaction",
	[
		(store_script_param, ":region", 1),
		
		(party_get_slot, ":num", ":region", TownRegionSize),
		(store_add, ":end", TownRegion, ":num"),
		
		(store_faction_of_party, ":town_owner", ":region"),
		
		(assign, ":castles", 0),
		
		(try_for_range, ":slot", TownRegion+0, ":end"),
			(party_get_slot, ":castle", ":region", ":slot"),
			(store_faction_of_party, ":fac", ":castle"),
			
			(eq, ":fac", ":town_owner"),
			(val_add, ":castles", 1), 
		(try_end),
		
		(assign, ReturnValue, -1),
		(store_div, ":half", ":num", 2),
		(try_begin),
			(ge, ":castles", ":half"),
			(assign, ReturnValue, ":town_owner"),
		(else_try),
			(party_get_slot, ReturnValue, ":region", TownRegionLastOwner),
		(try_end),
	]),
	
	("factionUpdate",
	[
		(store_script_param_1, ":faction"),
		
		(faction_get_slot, ":state", ":faction", FactionState),
		
		(try_begin),
			(eq, ":state", FactionState_CounterWave),
			
			
		(try_end),
	
	]),
	
	("regionLocationsString",
	[
		(store_script_param_1, ":region"),
		(store_script_param_2, ":base"),
		
		(party_get_slot, ":num", ":region", TownRegionSize),
		(store_add, ":end", TownRegion, ":num"),
		(assign, ":begin", TownRegion),
		
		(assign, ":first", ":region"),
		
		(try_begin),
			(eq, ":base", 0),
			(val_add, ":begin", 1),
			(party_get_slot, ":first", ":region", TownRegion),
		(try_end),
		
		(str_clear, s25),
		

		(str_store_party_name, s25, ":first"),
		(str_store_party_name_link, s26, ":first"),
		
		(try_for_range, ":slot", ":begin", ":end"),
			(party_get_slot, ":loc", ":region", ":slot"),
			(str_store_party_name, s0, ":loc"),
			(str_store_party_name_link, s1, ":loc"),
			(str_store_string, s25, "@{s25}, {s0}"),
			(str_store_string, s26, "@{s26}, {s1}"),
		(try_end),
	]),
	
	("CounterWaveEnd",
	[
		(try_begin),
			(eq, "$Etap4NextAttacker", Rosja),
			(str_store_string, s20, "@Imperium Rosyjskiego"),
		(else_try),
			(eq, "$Etap4NextAttacker", Prusy),
			(str_store_string, s20, "@Królestwa Prus"),
		(else_try),
			(eq, "$Etap4NextAttacker", Austria),
			(str_store_string, s20, "@Monarchii Habsburgów"),
		(try_end),
		
		# (call_script, "script_getClosestRegion", "$Etap4NextAttacker", Kosciuszkowcy),
		(call_script, "script_getFactionTarget", "$Etap4NextAttacker"),
		(str_store_party_name, s21, ReturnValue),
		
		(call_script, "script_regionLocationsString", ReturnValue, 1),
		(try_begin),
			(eq, "$FirstWave", 0),
			(assign, "$FirstWave", 1),
			(str_store_string, s100, "str_atak_0"),
			(quest_set_slot, "qst_Wojna", QuestSlot+1, "str_atak_1log"),
		(else_try),
			(gt, "$Etap4Region", 0),
			(party_is_active, "$Etap4Region"),
			(call_script, "script_regionGetFaction", "$Etap4Region"),
			(eq, ReturnValue, Kosciuszkowcy),
			(str_store_string, s100, "str_atak_1"),
			(quest_set_slot, "qst_Wojna", QuestSlot+1, "str_atak_1log"),
		(else_try),
			(str_store_string, s100, "str_atak_2"),
			(quest_set_slot, "qst_Wojna", QuestSlot+1, "str_atak_2log"),
		(try_end),
		(call_script, "script_quest_update", "qst_Wojna", 2),
		(start_presentation, "prsnt_letter"),
		
		(try_for_range, ":lord", lords_begin, lords_end),
			(store_troop_faction, ":fac", ":lord"),
			(eq, ":fac", Kosciuszkowcy),
			(troop_slot_ge, ":lord", TroopActiveInWave, 1),
			(troop_set_slot, ":lord", TroopActiveInWave, 0),
			
			(troop_get_slot, ":party", ":lord", slot_troop_leaded_party),
			(party_is_active, ":party"),
			
			(troop_get_slot, ":bound", ":lord", BoundLocation),
			(try_begin),
				(gt, ":bound", 0),
				(party_is_active, ":bound"),
				(call_script, "script_partyGiveOrder", ":party", spai_holding_center, ":bound"),
			(else_try),
				(call_script, "script_partyGiveOrder", ":party", spai_undefined, -1),
			
			(try_end),
		(try_end),
	]),
	
	("etap4Update",
	[
		(try_begin),
			# (this_or_next|eq, "$Etap4State", Etap4_Wait),
			(eq, "$Etap4State", Etap4_CounterWave),
			
			(val_sub, "$Etap4Time", 1),
			(le, "$Etap4Time", 1),
			(assign, "$Etap4Substate", -1),
			
			(eq, "$Etap4State", Etap4_CounterWave),
			
			(try_begin),
				(eq, "$Etap4NextAttacker", "fac_kingdom_2"),
				(try_begin),
					(faction_slot_ge, "fac_kingdom_3", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_3"),
				(else_try),
					(faction_slot_ge, "fac_kingdom_4", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_4"),
				(else_try),
					(neg|faction_slot_ge, "$Etap4NextAttacker", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", -1),
				(try_end),
			(else_try),
				(eq, "$Etap4NextAttacker", "fac_kingdom_3"),
				(try_begin),
					(faction_slot_ge, "fac_kingdom_4", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_4"),
				(else_try),
					(faction_slot_ge, "fac_kingdom_2", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_2"),
				(else_try),
					(neg|faction_slot_ge, "$Etap4NextAttacker", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", -1),
				(try_end),
			(else_try),
				(eq, "$Etap4NextAttacker", "fac_kingdom_4"),
				(try_begin),
					(faction_slot_ge, "fac_kingdom_2", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_2"),
				(else_try),
					(faction_slot_ge, "fac_kingdom_3", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", "fac_kingdom_3"),
				(else_try),
					(neg|faction_slot_ge, "$Etap4NextAttacker", FactionWaves, 1),
					(assign, "$Etap4NextAttacker", -1),
				(try_end),
			(try_end),
			
			
			(call_script, "script_CounterWaveEnd"),
		(try_end),
		
		(assign, reg0, "$Etap4State"),
		(assign, reg1, "$Etap4Time"),
		]+debugMessage("@[etap4Update]: {reg0} time: {reg1}", 0x00007f)+[
		(try_begin),
			(this_or_next|eq, "$Etap4State", Etap4_None),
			(eq, "$Etap4State", Etap4_Wave),
			###nothing
		# (else_try),
			# (eq, "$Etap4State", Etap4_Wait),
			# (eq, "$Etap4Substate", -1),
			# (assign, "$Etap4State", Etap4_CounterWave),
			# (assign, "$Etap4Substate",0),
			# (assign, "$Etap4Time",20*24),
		(else_try),
			(eq, "$Etap4State", Etap4_CounterWave),
			
			(try_begin),
				(eq, "$Etap4Substate", 0),
				
				(faction_get_slot, ":last_region", "$Etap4LastWaveFaction", WaveRegion),
				(assign, "$Etap4Time", 20*24),
				# (party_get_slot, ":num", ":last_region", TownRegionSize),
				
				(call_script, "script_regionGetFaction", ":last_region"),
				
				(assign, ":region", -1),
				
				(try_begin),
					(neq, ReturnValue, Kosciuszkowcy),
					(assign, ":region", ":last_region"),
					(call_script, "script_regionLocationsString", ":region", 1),
					(str_store_party_name, s20, ":region"),
					
					(str_store_string, s100, "str_kontratak_1"),
					(quest_set_slot, "qst_Wojna", QuestSlot+1, "str_kontratak_1log"),
				(else_try),
					(call_script, "script_getClosestRegion", Kosciuszkowcy, "$Etap4LastWaveFaction"),
					(assign, ":region", ReturnValue),
					(call_script, "script_regionLocationsString", ReturnValue, 1),
					(str_store_party_name, s20, ":region"),
					
					(str_store_string, s100, "str_kontratak_2"),
					(quest_set_slot, "qst_Wojna", QuestSlot+1, "str_kontratak_2log"),
				(try_end),
				(call_script, "script_quest_update", "qst_Wojna", 2),
				(party_get_slot, ":marker", ":region", TownRegionActionMarker),
				(try_begin),
					(gt, ":marker", 0),
					(party_set_flags, ":marker", pf_disabled, 1),
					(party_set_flags, ":marker", pf_always_visible, 1),
				(try_end),
				(assign, "$Etap4Region", ":region"),
				
				(party_set_slot, "$Etap4Region", Town4Etap, 0),
				(party_set_slot, "$Etap4Region", Town4EtapBonus, 0),
				
				(str_store_party_name, s20, ":region"),
				(start_presentation, "prsnt_letter"),
				
				
				
				(assign, "$Etap4Substate", 1),
				
			(else_try),
				(eq, "$Etap4Substate", 1),
			
				(try_for_range, ":lord", lords_begin, lords_end),
					(store_troop_faction, ":faction", ":lord"),
					(eq, ":faction", Kosciuszkowcy),
					(troop_slot_ge, ":lord", TroopActiveInWave, 1),
					
					(troop_get_slot, ":party", ":lord", slot_troop_leaded_party),
					(party_is_active, ":party"),
					
					(call_script, "script_partyGiveOrder", ":party", spai_accompanying_army, "p_main_party"),
					# (neg|troop_slot_ge, ":lord", GrupaAtaku, 1),
					
					# (party_get_slot, ":region_size", "$Etap4Region", TownRegionSize),
					# (store_add, ":end", TownRegion, ":region_size"),
			
					# (assign, ":result", -1),
			
					# (try_for_range, ":slot", TownRegion+0, ":end"),
						# (party_get_slot, ":castle", "$Etap4Region", ":slot"),
						
						# (store_faction_of_party, ":fac", ":castle"),
						# (store_relation, ":relation", ":fac", ":faction"),
						# (neq, ":fac", ":faction"),
						# (lt, ":relation", 0),
						# (str_store_party_name, s0, ":castle"),
						# ]+debugMessage("@{s0} considered captured...")+[
						# (assign, ":result", ":castle"),
					# (try_end),
					# (gt, ":result", 0),
					# (troop_set_slot, ":lord", GrupaAtaku, ":result"),
				(try_end),
				
				##Check if all locations were captured
				(party_get_slot, ":region_size", "$Etap4Region", TownRegionSize),
				(store_add, ":end", TownRegion, ":region_size"),
		
				(assign, ":result", -1),
				(store_faction_of_party, ":fac", "$Etap4Region"),
				
				(eq, ":fac", Kosciuszkowcy),
		
				(try_for_range, ":slot", TownRegion+0, ":end"),
					(party_get_slot, ":castle", "$Etap4Region", ":slot"),
					
					(store_faction_of_party, ":fac", ":castle"),
					(store_relation, ":relation", ":fac", Kosciuszkowcy),
					(neq, ":fac", Kosciuszkowcy),
					(lt, ":relation", 0),
					(str_store_party_name, s0, ":castle"),
					(assign, ":result", ":castle"),
				(try_end),
				
				(eq, ":result", -1),
				##End counterwave
				
				(assign, "$Etap4Time", 1),
			
			(else_try),
				(eq, "$Etap4Substate", -1),
				
				(try_begin),				
					(gt, "$Etap4Region", 0),
					(party_is_active, "$Etap4Region"),
					
					(party_get_slot, ":marker", "$Etap4Region", TownRegionActionMarker),
					(party_set_flags, ":marker", pf_disabled, 1),
				(try_end),
				
				(try_for_range, ":lord", lords_begin, lords_end),
					(store_troop_faction, ":faction", ":lord"),
					(eq, ":faction", Kosciuszkowcy),
					
					(troop_get_slot, ":party", ":lord", slot_troop_leaded_party),
					
					(gt, ":party", 0),
					(party_is_active, ":party"),
					(call_script, "script_partyGiveOrder", ":party", spai_undefined, -1),
				(try_end),
				
				(try_begin),
					
					(try_begin),
						(eq, "$Etap4NextAttacker", -1),
						## Waves ended
						
						(jump_to_menu, "mnu_etap4_end"),					
					(else_try),
						(faction_slot_ge, "$Etap4NextAttacker", FactionWaves, 1),
						(call_script, "script_waveStart", "$Etap4NextAttacker", -1),
						
						# (assign, "$Etap4State", Etap4_Wave),
						# (assign, "$Etap4Substate", 0),
					
					(try_end),
					
				(try_end),
				
			(try_end),
			
		(try_end),
	
	]),
]