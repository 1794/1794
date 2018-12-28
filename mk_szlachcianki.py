# -*- coding: utf-8 -*-
from header_operations import *
from header_common import *
from header_dialogs import *

mk_szlachcianki = [

[anyone|plyr,"uwodzenie_szlachcianka1",[(eq, "$UwodzenieRandom", 0)],"Eeyye, pięękny dziś m-mamy d-dzień, nieprawdaż?","uwodzenie_szlachcianka1_1", []],
	[anyone,"uwodzenie_szlachcianka1_1",[],"Dzień? Wtorek, o ile mnie pamięć nie myli. Ostańcie w zdrowiu.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka1",[(eq, "$UwodzenieRandom", 1)],"YYy...echem... ładna pogoda dziś jest...","uwodzenie_szlachcianka1_2", []],
	[anyone,"uwodzenie_szlachcianka1_2",[],"Słucham? Nic nie rozumiem... jak jeść to karczma jest za rogiem i w lewo.","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka1",[(eq, "$UwodzenieRandom", 2)],"Powiadają, że w Kaliskim wichura silna stuletni dąb obaliła...","uwodzenie_szlachcianka1_3", []],
	[anyone,"uwodzenie_szlachcianka1_3",[],"Powiadają, żegnam.","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka2",[(eq, "$UwodzenieRandom", 0)],"Eeyye, pięękny dziś m-mamy d-dzień, nieprawdaż?","uwodzenie_szlachcianka2_1", []],
	[anyone,"uwodzenie_szlachcianka2_1",[],"Dzień? Wtorek, o ile mnie pamięć nie myli. Ostańcie w zdrowiu.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka2",[(eq, "$UwodzenieRandom", 1)],"YYy...echem... ładna pogoda d-dziśś jes-st...","uwodzenie_szlachcianka2_2", []],
	[anyone,"uwodzenie_szlachcianka2_2",[],"Słucham? Nic nie rozumiem... jak jeść to karczma jest za rogiem i w lewo.","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka2",[(eq, "$UwodzenieRandom", 2)],"Powiadają, że w na Wiśle szkuta pełna dorsza poszła na dno...","uwodzenie_szlachcianka2_3", []],
	[anyone,"uwodzenie_szlachcianka2_3",[],"Powiadają, żegnam.","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka3",[(eq, "$UwodzenieRandom", 0)],"Eeyye, pięękny dziś m-mamy d-dzień, nieprawdaż?","uwodzenie_szlachcianka3_1", []],
	[anyone,"uwodzenie_szlachcianka3_1",[],"Dzień? Wtorek, o ile mnie pamięć nie myli. Ostańcie w zdrowiu.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka3",[(eq, "$UwodzenieRandom", 1)],"YYy...echem... ładna pogoda dziś jesst...","uwodzenie_szlachcianka3_2", []],
	[anyone,"uwodzenie_szlachcianka3_2",[],"Słucham? Nic nie rozumiem... jak jeść to karczma jest za rogiem i w lewo.","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka3",[(eq, "$UwodzenieRandom", 2)],"Powiadają, że w Bracławiu spaliła się cerkiew...","uwodzenie_szlachcianka3_3", []],
	[anyone,"uwodzenie_szlachcianka3_3",[],"Powiadają, żegnam.","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka4",[(eq, "$UwodzenieRandom", 0)],"Eeyye, pięękny dziś m-mamy d-dzień, nieprawdaż?","uwodzenie_szlachcianka4_1", []],
	[anyone,"uwodzenie_szlachcianka4_1",[],"Dzień? Wtorek, o ile mnie pamięć nie myli. Ostańcie w zdrowiu.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka4",[(eq, "$UwodzenieRandom", 1)],"YYy...echem... ładna pogoda dziś jesst...","uwodzenie_szlachcianka4_2", []],
	[anyone,"uwodzenie_szlachcianka4_2",[],"Słucham? Nic nie rozumiem... jak jeść to karczma jest za rogiem i w lewo.","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka4",[(eq, "$UwodzenieRandom", 2)],"Powiadają, że w Bracławiu spaliła się cerkiew...","uwodzenie_szlachcianka4_3", []],
	[anyone,"uwodzenie_szlachcianka4_3",[],"Powiadają, żegnam.","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka5",[(assign, reg41, 30),(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka5_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka5_1",[(lt, reg40, reg41)],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka5_1",[],"Mi również kręci się w głowie, na tyle, że muszę udać się do cyrulika. Waszmości też to radzę, krwi nieco upuści, a następnie do zamtuzu, to też powinno pomóc. Przez życzliwość tylko radzę.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka5",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii...","uwodzenie_szlachcianka5_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka5_2",[(lt, reg40, reg41)],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka5_2",[],"Wybaczcie, lecz ktoś już was uprzedził w ofercie...","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka5",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka5_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka5_3",[(lt, reg40, reg41)],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka5_3",[],"Wybaczcie, lecz nie wchodzę w takie układy z nieznajomymi...","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka6",[(assign, reg41, 40),(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka6_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka6_1",[(lt, reg40, reg41)],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka6_1",[],"Mi również kręci się w głowie, na tyle, że muszę udać się do cyrulika. Waszmości też to radzę, krwi nieco upuści, a następnie do zamtuzu, to też powinno pomóc. Przez życzliwość tylko radzę.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka6",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii...","uwodzenie_szlachcianka6_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka6_2",[(lt, reg40, reg41)],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka6_2",[],"Wybaczcie, lecz ktoś już was uprzedził w ofercie...","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka6",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka6_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka6_3",[(lt, reg40, reg41)],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka6_3",[],"Wybaczcie, lecz nie wchodzę w takie układy z nieznajomymi...","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka7",[(assign, reg41, 60),(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka7_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka7_1",[(lt, reg40, reg41)],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka7_1",[],"Mi również kręci się w głowie, na tyle, że muszę udać się do cyrulika. Waszmości też to radzę, krwi nieco upuści, a następnie do zamtuzu, to też powinno pomóc. Przez życzliwość tylko radzę.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka7",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii...","uwodzenie_szlachcianka7_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka7_2",[(lt, reg40, reg41)],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka7_2",[],"Wybaczcie, lecz ktoś już was uprzedził w ofercie...","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka7",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka7_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka7_3",[(lt, reg40, reg41)],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka7_3",[],"Wybaczcie, lecz nie wchodzę w takie układy z nieznajomymi...","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka8",[(assign, reg41, 80),(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka8_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka8_1",[(lt, reg40, reg41)],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka8_1",[],"Mi również kręci się w głowie, na tyle, że muszę udać się do cyrulika. Waszmości też to radzę, krwi nieco upuści, a następnie do zamtuzu, to też powinno pomóc. Przez życzliwość tylko radzę.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka8",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii...","uwodzenie_szlachcianka8_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka8_2",[(lt, reg40, reg41)],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka8_2",[],"Wybaczcie, lecz ktoś już was uprzedził w ofercie...","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka8",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka8_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka8_3",[(lt, reg40, reg41)],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka8_3",[],"Wybaczcie, lecz nie wchodzę w takie układy z nieznajomymi...","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka9",[(assign, reg41, 80),(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka9_1", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka9_1",[(lt, reg40, reg41)],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka9_1",[],"Mi również kręci się w głowie, na tyle, że muszę udać się do cyrulika. Waszmości też to radzę, krwi nieco upuści, a następnie do zamtuzu, to też powinno pomóc. Przez życzliwość tylko radzę.","uwodzenie_szlachcianka", []],

[anyone|plyr,"uwodzenie_szlachcianka9",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii...","uwodzenie_szlachcianka9_2", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka9_2",[(lt, reg40, reg41)],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka9_2",[],"Wybaczcie, lecz ktoś już was uprzedził w ofercie...","uwodzenie_szlachcianka", []],
	
[anyone|plyr,"uwodzenie_szlachcianka9",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka9_3", [(store_random_in_range, reg40, 0, 100)]],
	[anyone,"uwodzenie_szlachcianka9_3",[(lt, reg40, reg41)],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
	[anyone,"uwodzenie_szlachcianka9_3",[],"Wybaczcie, lecz nie wchodzę w takie układy z nieznajomymi...","uwodzenie_szlachcianka", []],
#==========================================================================================================================================================================
[anyone|plyr,"uwodzenie_szlachcianka10",[(eq, "$UwodzenieRandom", 0)],"Czarująco waćpanna wygląda, proszę o wybaczenie śmiałości, lecz urok przyćmił mi zmysły...","uwodzenie_szlachcianka10_1", []],
	[anyone,"uwodzenie_szlachcianka10_1",[],"Ah, miło mi to słyszeć z ust tak szykownego kawalera...","uwodzenie_szlachciankacheck", []],

[anyone|plyr,"uwodzenie_szlachcianka10",[(eq, "$UwodzenieRandom", 1)],"Oczarowany urodą waćpanny, chciałbym zaoferować swe usługi w każdej materii…","uwodzenie_szlachcianka10_2", []],
	[anyone,"uwodzenie_szlachcianka10_2",[],"Niezwykle to uprzejme ze strony waszmości...","uwodzenie_szlachciankacheck", []],

[anyone|plyr,"uwodzenie_szlachcianka10",[(eq, "$UwodzenieRandom", 2)],"Dziś właśnie filharmonicy Paryscy goszczą w mieście, proszę wybaczyć śmiałości, lecz czy nie wybrałaby się waćpanna na występ w mym towarzystwie?","uwodzenie_szlachcianka10_3", []],
	[anyone,"uwodzenie_szlachcianka10_3",[],"Oh, nie znam zupełnie waćpana… z przykrością odmówię, z tego względu. Mam inną jednak propozycję...","uwodzenie_szlachciankacheck", []],
#==========================================================================================================================================================================
]