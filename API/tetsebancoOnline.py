from mysql.connector import connect
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
import os

def connection(db_name):
    connection = None
    try:
        connection = connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = db_name                       
        )
        print("Conexão realizada com sucesso!")
    except Error as err:
        print(f"Error: {err}")
    return connection


con = connection("biblioteca")

# cursor = con.cursor()

# cursor.execute('''INSERT INTO livros VALUES(default, 'Cavaleiro Real', 465, 2009, 'Ana Claudia');''')

# cursor.execute('''DELETE FROM livros where livro_id = 2''')

# cursor.execute('''SELECT * FROM livros;''')

# # con.commit()



# teste = cursor.fetchall()

# print(teste)