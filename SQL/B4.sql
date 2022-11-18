select distinct bar as Bar 
from Sells 
where price >= all(select price from Sells where price is not null);
/* 
+-----------+
| Bar       |
+-----------+
| Joe's bar |
+-----------+
*/