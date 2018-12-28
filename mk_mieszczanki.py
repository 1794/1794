# -*- coding: utf-8 -*-
from header_operations import *
from header_common import *
from header_dialogs import *

mk_mieszczanki = [

[anyone|plyr,"uwodzenie_mieszczanka_1",[(eq, "$UwodzenieRandom", 0)],"Podobno dobrze dziś pranie schnie, nie?","uwodzenie_mieszczanka_1_1", []],
	[anyone,"uwodzenie_mieszczanka_1_1",[],"Ano, to  pójdę rozwiesić. Żegnam.","uwodzenie_mieszczanka", []],

[anyone|plyr,"uwodzenie_mieszczanka_1",[(eq, "$UwodzenieRandom", 1)],"Ładną mamy dziś pogodę.","uwodzenie_mieszczanka_1_2", []],
	[anyone,"uwodzenie_mieszczanka_1_2",[],"Nie to ładne co jest ładne, tylko to co komu się podoba. Ja tam wolę chłodniejszą.","uwodzenie_mieszczanka", []],
	
[anyone|plyr,"uwodzenie_mieszczanka_1",[(eq, "$UwodzenieRandom", 2)],"Pięknie pannie  w tej sukni.","uwodzenie_mieszczanka_1_3", []],
	[anyone,"uwodzenie_mieszczanka_1_3",[],"W tym fartuchu? Chyba na wzroku nie domagacie. A po drugie, to nie pannie, lecz pani, ot co.","uwodzenie_mieszczanka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_mieszczanka_2",[(eq, "$UwodzenieRandom", 0)],"Podobno dobrze dziś pranie schnie, nie?","uwodzenie_mieszczanka_2_1", []],
	[anyone,"uwodzenie_mieszczanka_2_1",[],"Ano, to  pójdę rozwiesić. Żegnam.","uwodzenie_mieszczanka", []],

[anyone|plyr,"uwodzenie_mieszczanka_2",[(eq, "$UwodzenieRandom", 1)],"Ładną mamy dziś pogodę.","uwodzenie_mieszczanka_2_2", []],
	[anyone,"uwodzenie_mieszczanka_2_2",[],"Nie to ładne co jest ładne, tylko to co komu się podoba. Ja tam wolę chłodniejszą.","uwodzenie_mieszczanka", []],
	
[anyone|plyr,"uwodzenie_mieszczanka_2",[(eq, "$UwodzenieRandom", 2)],"Pięknie pannie  w tej sukni.","uwodzenie_mieszczanka_2_3", []],
	[anyone,"uwodzenie_mieszczanka_2_3",[],"W tym fartuchu? Chyba na wzroku nie domagacie. A po drugie, to nie pannie, lecz pani, ot co.","uwodzenie_mieszczanka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_mieszczanka_3",[(eq, "$UwodzenieRandom", 0)],"Ah, piękną dziś mamy pogodę? Dawno tak ciepło nie było...","uwodzenie_mieszczanka_3_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_3_1",[(lt, reg40, 40)],"Oj prawda, prawda, też w takiej się lubuje, choć pragnienie większe, a może...","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_3_1",[],"Tylko cuchną wszyscy wokół, ja tam lubię jak jest zimno.","uwodzenie_mieszczanka", []],

[anyone|plyr,"uwodzenie_mieszczanka_3",[(eq, "$UwodzenieRandom", 1)],"Podobno kupcy ormiańscy zjadą dziś popołudniem, wiecie coś o tym? ","uwodzenie_mieszczanka_3_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_3_2",[(lt, reg40, 40)],"O, tak, ale kramy rozłożą dopiero jutro. Wiedzę jednak, że waszmość też czeka, to może...","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_3_2",[],"Ano może tak, może nie, kto kupca ormiańskiego wie? ","uwodzenie_mieszczanka", []],
	
[anyone|plyr,"uwodzenie_mieszczanka_3",[(eq, "$UwodzenieRandom", 2)],"Pewnikiem zanosi się na deszcz...","uwodzenie_mieszczanka_3_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_3_3",[(lt, reg40, 40)],"Trzeba zawczasu poszukać dobrego schronienia, nie uważa waszmość?","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_3_3",[],"Doprawdy? W takim razie odejdę zwinąć pranie.","uwodzenie_mieszczanka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_mieszczanka_4",[(eq, "$UwodzenieRandom", 0)],"Zapach wiosny unosi się już w powietrzu  i słowiki śpiewają...","uwodzenie_mieszczanka_4_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_4_1",[(lt, reg40, 60)],"O tak, porządki trzeba by poczynić, choć może  nie w tej chwili jeszcze...","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_4_1",[],"Ten odór? To stara zgniłą kapustę wywaliła. A wiosna to będzie, ale w kwietniu.","uwodzenie_mieszczanka", []],

[anyone|plyr,"uwodzenie_mieszczanka_4",[(eq, "$UwodzenieRandom", 1)],"Proszę o wybaczenie, lecz przyznać muszę, że wygląda pani dziś uroczo...","uwodzenie_mieszczanka_4_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_4_2",[(lt, reg40, 60)],"Dziękuję waćpanu, miło mi to słyszeć od tak szanowanego człowieka...","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_4_2",[],"Znalazł się, zakichany uwodziciel. Żegnam ozięble.","uwodzenie_mieszczanka", []],
	
[anyone|plyr,"uwodzenie_mieszczanka_4",[(eq, "$UwodzenieRandom", 2)],"Panna taka markotna, a dziś muzycy przyjeżdżają z Zagrzebia...","uwodzenie_mieszczanka_4_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_mieszczanka_4_3",[(lt, reg40, 60)],"Oh, naprawdę? Z chęcią więcej bym o nich się dowiedziała nim ich zobaczę...","uwodzenie_mieszczanka_check", []],
	[anyone,"uwodzenie_mieszczanka_4_3",[],"Doprawdy? Pewno zbereźniki i pijusy.","uwodzenie_mieszczanka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_mieszczanka_5",[(eq, "$UwodzenieRandom", 0)],"Ah, zapomniałem z domu szkicownika... cóż za szkoda! Pierś pełna, lico mleczne! Godne to utrwalenia, jako wzorzec piękna dla potomnych...","uwodzenie_mieszczanka_5_1", []],
	[anyone,"uwodzenie_mieszczanka_5_1",[],"Ah, prawdziwy artysta! Pozwólcie, że dotknę bo nie uwierzę... aj, może nie tu.","uwodzenie_mieszczanka_check", []],

[anyone|plyr,"uwodzenie_mieszczanka_5",[(eq, "$UwodzenieRandom", 1)],"Cóż za cud... jakież to bóstwo nawiedziło ten padół opłakany. Ledwie myśl ludzka pojąć to może, każdy na około spuszcza oczy w pokorze... czar, to urok, siła sprawcza piękna. Ah, któż to opisać zdoła, nie podobnym to...","uwodzenie_mieszczanka_5_2", []],
	[anyone,"uwodzenie_mieszczanka_5_2",[],"Ah, prawdziwy poeta! Pozwólcie, że dotknę bo nie uwierzę... aj, może nie tu.","uwodzenie_mieszczanka_check", []],
	
[anyone|plyr,"uwodzenie_mieszczanka_5",[(eq, "$UwodzenieRandom", 2)],"Wybaczcie śmiałość, lecz widząc pannę pomyślałem, że brak jej rozrywki... dziś wieczorem do miasta zjeżdżają Frankfurccy kuglarze, co powiecie na towarzyszenie mi?","uwodzenie_mieszczanka_5_3", []],
	[anyone,"uwodzenie_mieszczanka_5_3",[],"Wybaczcie, lecz nie znamy się dostatecznie... warto jednakby to zmienić.","uwodzenie_mieszczanka_check", []],
#==========================================================================================================================================================================

]
	