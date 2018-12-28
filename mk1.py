# -*- coding: utf-8 -*-
from header_operations import *
from header_common import *
from header_dialogs import *
from module_constants import *

mk = [

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_citizen_f"),###mieszczanki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(this_or_next|eq, ":skl", 0),
(			  eq, ":skl", 1),
]," ","uwodzenie_mieszczanka_1", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_citizen_f"),###mieszczanki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 2),
]," ","uwodzenie_mieszczanka_2", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_citizen_f"),###mieszczanki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 3),
]," ","uwodzenie_mieszczanka_3", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_citizen_f"),###mieszczanki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 4),
]," ","uwodzenie_mieszczanka_4", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_citizen_f"),###mieszczanki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  ge, ":skl", 5),
]," ","uwodzenie_mieszczanka_5", []],
#===========================================================================================================
[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(this_or_next|eq, ":skl", 0),
(			  eq, ":skl", 1),
]," ","uwodzenie_szlachcianka1", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 2),
]," ","uwodzenie_szlachcianka2", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 3),
]," ","uwodzenie_szlachcianka3", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 4),
]," ","uwodzenie_szlachcianka4", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 5),
]," ","uwodzenie_szlachcianka5", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 6),
]," ","uwodzenie_szlachcianka6", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 7),
]," ","uwodzenie_szlachcianka7", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 8),
]," ","uwodzenie_szlachcianka8", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 9),
]," ","uwodzenie_szlachcianka9", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_szlachta_f"),###szlachcianki
]," ","uwodzenie_szlachcianka10", []],
#===========================================================================================================
[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(this_or_next|eq, ":skl", 0),
(			  eq, ":skl", 1),
]," ","uwodzenie_arystokratka1", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 2),
]," ","uwodzenie_arystokratka2", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 3),
]," ","uwodzenie_arystokratka3", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 4),
]," ","uwodzenie_arystokratka4", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 5),
]," ","uwodzenie_arystokratka5", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 6),
]," ","uwodzenie_arystokratka6", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 7),
]," ","uwodzenie_arystokratka7", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 8),
]," ","uwodzenie_arystokratka8", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
(store_skill_level, ":skl", "skl_seduction", "trp_player"),(1,"script_uwodzenieRandom"),
(			  eq, ":skl", 9),
]," ","uwodzenie_arystokratka9", []],

[anyone|auto_proceed,"uwodzenie",[
(eq, "$g_talk_troop", "trp_arystokrata_f"),###arystokratki
]," ","uwodzenie_arystokratka10", []],
#===========================================================================================================
[anyone,"uwodzenie",[
],"Not implemented yet.","close_window", []],


[anyone,"uwodzenie_mieszczanka",[
(display_message, "@Próba uwodzenia nieudana.", 0xd42121),
(agent_set_slot, "$g_talk_agent", DisallowTalk, 1),
],"Żegnam.","close_window", []],

[anyone,"uwodzenie_szlachcianka",[
(display_message, "@Próba uwodzenia nieudana.", 0xd42121),
(agent_set_slot, "$g_talk_agent", DisallowTalk, 1),
],"Żegnam","close_window", []],

[anyone,"uwodzenie_arystokratka",[
(display_message, "@Próba uwodzenia nieudana.", 0xd42121),
(agent_set_slot, "$g_talk_agent", DisallowTalk, 1),
],"Żegnam","close_window", []],

[anyone|plyr,"uwodzenie_mieszczanka_succees",[],"Z chęcią.","close_window", [
(1,"script_addLover", "$g_talk_agent", "$current_town"),
(finish_mission),
(change_screen_map),
(rest_for_hours, 6, 5, 0),
(assign, "$Kochanka", 1),
]],

[anyone|plyr,"uwodzenie_szlachcianka_succees",[],"Z chęcią.","close_window", [
(1,"script_addLover", "$g_talk_agent", "$current_town"),
(finish_mission),
(change_screen_map),
(rest_for_hours, 6, 5, 0),
(assign, "$Kochanka", 1),
]],

[anyone|plyr,"uwodzenie_arystokratka_succees",[],"Z chęcią.","close_window", [
(1,"script_addLover", "$g_talk_agent", "$current_town"),
(finish_mission),
(change_screen_map),
(rest_for_hours, 6, 5, 0),
(assign, "$Kochanka", 1),
]],



[anyone,"uwodzenie_mieszczanka_check",[
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
(this_or_next|ge, ":gold", 3000),
(ge, ":renown", 350),
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Wstąpi waszmość do mnie na herbatę? "),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@Napije się waszmość ze mną herbaty? Mieszkam tu, nieopodal."),
(try_end),
(display_message, "@Próba uwodzenia udana.", 0x007f00),
],"{s20}","uwodzenie_mieszczanka_succees", []],

[anyone,"uwodzenie_mieszczanka_check",[
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Chociaż nie, zapomniałam, że dziś kuzyn z bratem w mieście bawi i zajdą wieczorem."),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@A, mąż mój z wyprawy handlowej dziś wraca z pewnością będę zajęta..."),
(try_end),
],"{s20}","uwodzenie_mieszczanka", [
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
(try_begin),
	(neg|ge, ":gold", 3000),
	(display_message, "@Brak wymaganej sumy pieniędzy(3000).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, ":renown", 350),
	(display_message, "@Brak wymaganej renomy(350).", 0xd42121),
(try_end),
]],

#==========================================
[anyone,"uwodzenie_szlachciankacheck",[
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),

(assign, ":ok", 0),
(try_begin),
	(ge, ":gold", 10000),
	(val_add, ":ok", 1),
(try_end),
(try_begin),
	(ge, ":renown", 650),
	(val_add, ":ok", 1),
(try_end),
(try_begin),
	(ge, "$player_honor", 10),
	(val_add, ":ok", 1),
(try_end),
(ge, ":ok", 2),
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Może zechcielibyście wypić kawę? Mieszkam niedaleko stąd. "),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@Może zechciałby waszmość wypić wraz ze mną kawę? Mieszkam niedaleko stąd."),
(try_end),
(display_message, "@Próba uwodzenia udana.", 0x007f00),
],"{s20}","uwodzenie_szlachcianka_succees", []],

[anyone,"uwodzenie_szlachciankacheck",[
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Przepraszam jednak, coś przypomniało mi się. "),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@Oh, przepraszam najmocniej, przypomniało mi się, że już jestem umówiona."),
(try_end),
],"{s20}","uwodzenie_szlachcianka", [
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
(try_begin),
	(neg|ge, ":gold", 10000),
	(display_message, "@Brak wymaganej sumy pieniędzy(10000).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, ":renown", 650),
	(display_message, "@Brak wymaganej renomy(650).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, "$player_honor", 10),
	(display_message, "@Brak wymaganej liczby punktów honoru(10).", 0xd42121),
(try_end),
]],
#==========================================
[anyone,"uwodzenie_arystokratkacheck",[
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
(troop_get_slot, ":rank", "trp_player", Ranga),

(assign, ":ok", 0),
(try_begin),
	(ge, ":gold", 10000),
	(val_add, ":ok", 1),
(try_end),
(try_begin),
	(ge, ":renown", 650),
	(val_add, ":ok", 1),
(try_end),
(try_begin),
	(ge, "$player_honor", 10),
	(val_add, ":ok", 1),
(try_end),
(ge, ":ok", 2),
(ge, ":rank", rKapitan),
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Zapraszam na kawę, nie odmówicie chyba damie towarzystwa?"),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@Pozwólcie do mnie na kawę, nie chcę sama spędzać dziś popołudnia..."),
(try_end),
(display_message, "@Próba uwodzenia udana.", 0x007f00),
],"{s20}","uwodzenie_arystokratka_succees", []],

[anyone,"uwodzenie_arystokratkacheck",[
(store_random_in_range, ":r", 0, 2),
(try_begin),
	(eq, ":r", 0),
	(str_store_string, s20, "@Przepraszam jednak, coś przypomniało mi się. "),
(else_try),
	(eq, ":r", 1),
	(str_store_string, s20, "@Oh, przepraszam najmocniej, przypomniało mi się, że już jestem umówiona."),
(try_end),
],"{s20}","uwodzenie_arystokratka", [
(store_troop_gold, ":gold", "trp_player"),
(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
(troop_get_slot, ":rank", "trp_player", Ranga),

(try_begin),
	(neg|ge, ":gold", 10000),
	(display_message, "@Brak wymaganej sumy pieniędzy(10000).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, ":renown", 650),
	(display_message, "@Brak wymaganej renomy(650).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, "$player_honor", 10),
	(display_message, "@Brak wymaganej liczby punktów honoru(10).", 0xd42121),
(try_end),
(try_begin),
	(neg|ge, ":rank", rKapitan),
	(display_message, "@Brak wymaganego stopnia oficerskiego(Kapitan/Rotmistrz).", 0xd42121),
(try_end),
]],





]



