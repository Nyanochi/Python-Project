import mysql.connector

connection = mysql.connector.connect(host="localhost", database="nyanochi",
                                     user="root", password="panochitihon1997")
cursor = connection.cursor()


class employee:
    def __init__(self, emp_id, first_name):
        self.emp_id = emp_id
        self.first_name = first_name
        #self.last_name = last_name
        #self.birth_day = birth_day
        #self.sex = sex
        #self.salary = salary
        #self.super_id = super_id
        #self.branch_id = branch_id


def menu():
    print("Welcome to Employee manage app")
    print("1. List all emp")
    print("2. Add new emp")
    print("3. Update emp")
    print("4. Delete emp")
    print("Press number to use, press 'quit' to exit app")


def list_emp():
    query = "SELECT * FROM employee"
    cursor.execute(query)
    result = cursor.fetchall()
    for key in result:
        print(f"ID: {key[0]} ,Name: {key[1]}")



def add_emp():
    new_emp = employee(input("Enter employee ID: "), input("Enter first name: "))
    query = f"INSERT INTO employee(emp_id, first_name) VALUES(%s, %s)"
    record = (new_emp.emp_id, new_emp.first_name)
    cursor.execute(query, record)
    connection.commit()
    print(f'{cursor.rowcount} rows affected. New employee added')


def update_emp():
    update = employee(input("Enter employee ID: "), input("Enter first name: "))
    query = "UPDATE employee SET first_name = %s WHERE emp_id = %s"
    record = (update.first_name, update.emp_id)
    cursor.execute(query, record)
    connection.commit()
    print(f'{cursor.rowcount} rows affected. {update.emp_id} has been deleted')


def del_emp():
    emp_id = input("Enter employee ID: ")
    query = "DELETE FROM employee WHERE emp_id = %s"
    record = (emp_id, )
    cursor.execute(query, record)
    connection.commit()
    print(f'{cursor.rowcount} rows affected. {emp_id} has been deleted')


while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        list_emp()
    elif choice == "2":
        add_emp()
    elif choice == "3":
        update_emp()
    elif choice == "4":
        del_emp()
    elif choice == "quit":
        break
    else:
        continue



