from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL # type: ignore

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#Valerio2109'
app.config['MYSQL_DB'] = 'pet'
mysql = MySQL(app)

@app.route("/contatos")
def contato():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contato")
    contato = cur.fetchall()
    cur.close()
    return render_template('contatos.html', contato=contato)
   
@app.route('/add_contato', methods=['POST', 'GET'])
def add_contato():
    if request.method == 'POST':
        con_email = request.form['email']
        con_assunto = request.form['assunto']
        con_descricao= request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (con_email,con_assnto,con_descricao) VALUES (%s, %s,%s)", (con_email,con_assunto,con_descricao))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('contato'))
    
@app.route('/mostrar_contato', methods=['POST', 'GET'])
def mostrar_contato():
    if request.method == 'POST':
        con_email = request.form['email']
        con_assunto = request.form['assunto']
        con_descricao= request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (con_email,con_assnto,con_descricao) VALUES (%s, %s,%s)", (con_email,con_assunto,con_descricao))
        mysql.connection.commit()
        cur.close()
    return render_template('contatos.html')
    
@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/sobre")
def quem_somos():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
    