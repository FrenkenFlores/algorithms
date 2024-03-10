# Жизнь в изгнании
|Ограничение времени|Ограничение памяти|Ввод|Вывод|
|---|---|---|---|
|5 секунда|64Mb|стандартный ввод|стандартный вывод|


Тридцать пятый год своей жизни Ходжа Насреддин встретил в пути.
Больше десяти лет провел он в изгнании, странствуя из города в город, из одной страны в другую, пересекая моря и пустыни, ночуя как придется – на голой земле у скудного пастушеского костра, или в тесном караван-сарае, где в пыльной темноте до утра вздыхают и чешутся верблюды и глухо позвякивают бубенцами, или в чадной, закопченной чайхане, среди лежащих вповалку водоносов, нищих, погонщиков и прочего бедного люда, с наступлением рассвета наполняющего своими пронзительными криками базарные площади и узкие улички городов.

Напишите программу для выбора воспоминаний Ходжи Насреддина, относящихся к определенному временному периоду.
В файле journey.csv записаны воспоминания по следующим полям (разделитель – точка с запятой):
id, event, city, year
id, событие, город, год

Вводится строка, в которой диапазон годов для выбора записан через пробел. Оба года включаются в диапазон.
Выведите события (и в скобках город) в порядке перечисления в файле.

Использовать модуль csv обязательно!


## Пример

|Ввод|Вывод|
|---|---|
|# Содержимое потока stdin:|help (Adrianople)|
|1243 1253|hunger (Nowhere)|
|# Содержимое файла journey.csv:|storm (Adrianople)
|id;event;city;year|caravanserai (Isfahan)|
|1;help;Adrianople;1248|sunset (Edirne)|
|2;hunger;Nowhere;1249||
|3;storm;Adrianople;1253||
|4;comet;Baghdad;1257||
|5;caravanserai;Isfahan;1249||
|6;sunset;Edirne;1245||