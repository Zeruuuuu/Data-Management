select dept_no, count(distinct e.emp_no) as employeeNum 
from employees e 
left join dept_emp d 
on e.emp_no = d.emp_no 
where from_date = '1988-10-20' 
group by dept_no 
order by employeeNum desc;
/*
+---------+-------------+
| dept_no | employeeNum |
+---------+-------------+
| d005    |          20 |
| d004    |           9 |
| d007    |           9 |
| d001    |           4 |
| d006    |           4 |
| d008    |           3 |
| d002    |           2 |
| d003    |           2 |
| d009    |           1 |
+---------+-------------+
*/