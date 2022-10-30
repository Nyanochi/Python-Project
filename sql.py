import mysql.connector

def delete_from(emp_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='nyanochi',
                                             user='root',
                                             password='panochitihon1997')
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM employee WHERE emp_id = %s""", (emp_id, ))
        connection.commit()
        print(cursor.rowcount, "rows affected!")
        print(f'The employee ID {emp_id} has been deleted!')

    except mysql.connector.Error as error:
        print(f'Failed to delete from table in MySQL: {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


delete_from(109)
