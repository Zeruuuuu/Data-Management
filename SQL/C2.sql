select Manufacturer, avg(Price) as Average 
from Beers2Bars 
where Price is not null 
group by Manufacturer;
/*
+----------------+---------+
| Manufacturer   | Average |
+----------------+---------+
| Anheuser-Busch |       3 |
| Pete's         |     3.5 |
| Heineken       |       2 |
+----------------+---------+
*/
