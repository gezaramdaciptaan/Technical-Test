a. Buat query jika mencari employee name dan status employee?
b. Buat query untuk menampilkan nama employee yang statusnya resign berserta gaji yang diperoleh?
c. Buat query untuk menampilkan emp_code, nama, status, income dan sorting berdasarkan income
paling besar?

Jawaban : 
a. SELECT emp_name, emp_status
   FROM employee;

b. SELECT employee.emp_name, income.emp_income FROM employee
   INNER jOIN income on income.emp_code = employee.emp_code
   WHERE employee.emp_status = 'R';

c. SELECT employee.emp_code, employee.emp_name, employee.emp_status, income.emp_income FROM employee
   INNER JOIN income ON income.emp_code = employee.emp_code
   ORDER BY income.emp_income DESC;



   // vidio dokumentasi dapat di akses melalui url berikut 
   https://drive.google.com/drive/folders/1n5PaQn_U_gYXiCRhEPRTPUHMavpUcn3n?usp=sharing