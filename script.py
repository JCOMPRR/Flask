# Solo para CMD, para PowerShell (PS) es diferente
# Paso 1 Activate the environment:
# .venv\Scripts\activate
#Debe de salir esta ruta en consola (.venv) C:\Users\josec\Desktop\Code\flask>

# Paso 2 (Si ya estamos en la ruta no es necesario el paso 1 y solo inciar el paso 2)
# flask --app script run --debug (Para correr el codigo)

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

@app.route("/catalogoUsuarios", methods=['GET'])
def catalogoUsuarios():
    # Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM usuarios')
  usuarios = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogoUsuarios.html', usuarios = usuarios)

@app.route("/catalogoClientes", methods=['POST','GET'])
def catalogoClientes():
# Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM clientes')
  clientes = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogoClientes.html', clientes = clientes)


@app.route("/catalogoProductos", methods=['POST','GET'])
def catalogoProductos():
    # Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM productos')
  productos = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogoProductos.html', productos=productos)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
   # Conexión a la base de datos:
   mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
   mycursor.execute('SELECT * FROM productos')
   productos = mycursor.fetchall()
    
    # Cerrar la conexión:
   mycursor.close()
    
   return render_template("menu.html")

if __name__ == '__main__':
  app.run()