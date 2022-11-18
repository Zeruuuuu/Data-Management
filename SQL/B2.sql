select name as Drinker 
from Drinkers d 
left join Frequents f 
on d.name = f.drinker 
where bar is null;
/*
Empty set (0.00 sec)
This set is empty. You can see I modified everything the question asked me to do.
*/
