select bar as Bar, count(beer) as Total 
from Sells 
where price >= 2 and price is not null 
group by bar;
/*
+------------+-------+
| Bar        | Total |
+------------+-------+
| Bob's bar  |     2 |
| Joe's bar  |     4 |
| Mary's bar |     2 |
+------------+-------+
*/