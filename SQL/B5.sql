select distinct drinker as Drinker 
from Likes 
where drinker not in (
select distinct l1.drinker 
from Likes l1 
join Likes l2 
on l1.drinker = l2.drinker 
where (l1.beer = 'Bud' and l2.beer = 'Summerbrew') or (l2.beer = 'Bud' and l1.beer = 'Summerbrew'));
/*
+----------+
| Drinker  |
+----------+
| Bill     |
| Jennifer |
+----------+
*/
