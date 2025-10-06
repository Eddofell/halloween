#Importa de un paquete llamado, una clase llamada flask
from flask import Flask, render_template
from entities.animal import Animal
from entities.consoles import Consoles
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    animals=Animal.get_list()
    return render_template('animals.html', animals = animals)

@app.route('/consoles')
def consoles():
    consoles = Consoles.get_consoles()
    return render_template('consoles.html', consoles = consoles)

if __name__ == '__main__':
    app.run()