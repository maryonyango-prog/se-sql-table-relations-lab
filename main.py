# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = """
    SELECT firstName, lastName, jobTitle
    FROM employees
    INNER JOIN offices 
        USING(officeCode)
    WHERE city = "Boston";
"""

# STEP 2
# Replace None with your code
df_zero_emp = """
    SELECT officeCode, COUNT(officeCode) AS total_per_office
    FROM offices 
    LEFT JOIN employees
        USING(officeCode)
    GROUP BY officeCode
    HAVING (employees.firstName, employees.lastName) IS NULL;
"""

# STEP 3
# Replace None with your code
df_employee = """
    SELECT employees.firstName, employees.lastName, offices.city, offices.state
    FROM employees
    LEFT JOIN offices
        USING(officeCode)
    ORDER BY employees.firstName, employees.lastName;
"""

# STEP 4
# Replace None with your code
df_contacts = """
    SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
    FROM customers
    LEFT JOIN orders
        USING(customerNumber)
    WHERE customerNumber IS NULL
    ORDER BY contactLastName;
"""

# STEP 5
# Replace None with your code
df_payment = """
    SELECT customers.contactFirstName, customers.contactLastName, CAST(payments.amount AS INTEGER), payments.paymentDate
    FROM customers
    LEFT JOIN payments
        USING(customerNumber)
    ORDER BY payments.amount DESC;
"""

# STEP 6
# Replace None with your code
df_credit = """
    SELECT employees.employeeNumber, employees.firstName, employees.lastName, SUM(customers.customerNumber) AS numberOfCustomers
    FROM employees
    INNER JOIN customers
        USING(customers.contactLastName AND customers.contactFirstName)
    WHERE customers.creditLimit > 90000
    GROUP BY no_of_customers DESC
    LIMIT 4;
"""

# STEP 7
# Replace None with your code
df_product_sold = """
    SELECT products.productName, COUNT(orderdetails.quantityOrdered) AS numorders, SUM(orderdetails.quantityOrdered) AS totalunits
    FROM products
    LEFT JOIN orderdetails
        USING(productCode)
    GROUP BY productCode
    ORDER BY totalunits DESC;
"""

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9  
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()