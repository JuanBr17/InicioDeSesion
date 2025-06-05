from flask import Flask, jsonify, render_template, request, flash
import mysql.connector

app= Flask(__name__)

@app.route('/inicio', methods=['GET', 'POST'])
def Inicio(): 
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['passw']
        flash('Credenciales correctas')
    else: 
        flash('Credenciales incorrectas')
    return render_template('index.html')

def connect_to_db():
    mysql.connector.connect(
        host="localhost",
        user="root",
        password="17112006",
        database="ejemplo"
    )

if __name__ == '__main__': 
    app.run()