# Activate the environment:
# Before you work on your project, activate the corresponding environment:
# .venv\Scripts\activate

from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   # Conexión a la base de datos
    mycursor = mydb.cursor()

    # Obtener datos de la base de datos
    mycursor.execute('SELECT * FROM productos')
    productos = mycursor.fetchall()
    # print(productos)
    
    # Cerrar la conexión
    mycursor.close()
    # print("Todo bien")
    return render_template("catalogoProductos.html", productos=productos)

  

if __name__ == '__main__':
  app.run()