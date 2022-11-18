create table Beers2Bars as (
select manf as Manufacturer, beer as Beer, bar as Bar, price as Price 
from Sells 
left join Beers 
on Sells.beer = Beers.name);
select * from Beers2Bars;
/*
+----------------+------------+------------+-------+
| Manufacturer   | Beer       | Bar        | Price |
+----------------+------------+------------+-------+
| Anheuser-Busch | Bud        | Bob's bar  |     3 |
| Pete's         | Summerbrew | Bob's bar  |     3 |
| Anheuser-Busch | Bud        | Joe's bar  |     3 |
| Anheuser-Busch | Bud Lite   | Joe's bar  |     3 |
| Anheuser-Busch | Michelob   | Joe's bar  |     3 |
| Pete's         | Summerbrew | Joe's bar  |     4 |
| Anheuser-Busch | Bud        | Mary's bar |  NULL |
| Anheuser-Busch | Bud Lite   | Mary's bar |     3 |
| Heineken       | Budweiser  | Mary's bar |     2 |
+----------------+------------+------------+-------+
*/
