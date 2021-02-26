import sqlite3
from Employee_class import Employee
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("""CREATE  TABLE employees(
             first text,
             last text,
             pay integer
            )""")

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Jane','Doe',90000)
print(emp_1.first)
print(emp_1.last)
# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 20000)")
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first,emp_1.last,emp_1.pay))
c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_1.first,emp_1.last,emp_1.pay))
conn.commit()
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",{'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay})
conn.commit()
# c.execute("SELECT * FROM employees WHERE last = 'Doe'")
# c.execute("SELECT * FROM employees WHERE last = ?",('Schafer',))
c.execute("SELECT * FROM employees WHERE last = :l1",{'l1': 'Doe'})
print(c.fetchall())
conn.commit()
conn.close()