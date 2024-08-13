import sys
import psycopg2

host='localhost'
user='iti'
password='123'
dbname='iti'

def connect():
    try:
        connection = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=5432
        )
        return connection
    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")

def insert (id, name, age, track_id):
    connection=connect()  
    cursor = connection.cursor()  
    try:
        insert_query="""INSERT INTO trainee (id, name, age, track_id) VALUES (%s, %s, %s, %s) RETURNING id;"""
        cursor.execute(insert_query, (id, name, age, track_id))
        traineeid=cursor.fetchone()[0]
        connection.commit()
    except Exception as e:
        print (f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()

def select():
    connection = connect()
    cursor = connection.cursor()
    
    try:
        select_query = "SELECT * FROM trainee;"
        cursor.execute(select_query)
        trainees = cursor.fetchall()
        for trainee in trainees:
            print(trainee)
    except Exception as error:
        print(f"Error reading employees: {error}")
    finally:
        cursor.close()
        connection.close()

def update(id, name, age, track_id):
    connection = connect()
    cursor = connection.cursor()    
    try:
        update_query = """UPDATE trainee SET name = %s, age = %s, track_id = %s WHERE id = %s;"""
        cursor.execute(update_query, (name, age, track_id, id))
        connection.commit()
        print(f"Trainee with ID {id} updated.")
    except Exception as error:
        print(f"Error updating Trainee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def delete(id):
    connection = connect()
    cursor = connection.cursor()
    
    try:
        delete_query = "DELETE FROM trainee WHERE id = %s;"
        cursor.execute(delete_query, (id,))
        connection.commit()
        print(f"Trainee with ID {id} deleted.")
    except Exception as error:
        print(f"Error deleting trainee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# insert(5,'fffe', 23, 3)
# select()
# update(4, 'veronia', 20, 5)
# delete(5)
