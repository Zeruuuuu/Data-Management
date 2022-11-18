select distinct first_name, last_name 
from employees e 
left join salaries s 
on e.emp_no = s.emp_no 
where  salary >= 150000;
/*   
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Tokuyasu   | Pesch     |
| Ibibia     | Junet     |
| Xiahua     | Whitcomb  |
| Lansing    | Kambil    |
| Willard    | Baca      |
| Tsutomu    | Alameldin |
| Charmane   | Griswold  |
| Weicheng   | Hatcliff  |
| Mitsuyuki  | Stanfel   |
| Sanjai     | Luders    |
| Honesty    | Mukaidono |
| Weijing    | Chenoweth |
| Shin       | Birdsall  |
| Mohammed   | Moehrke   |
| Lidong     | Meriste   |
+------------+-----------+
*/