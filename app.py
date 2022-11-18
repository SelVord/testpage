from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder = 'Templates', static_folder = 'Static')

con = sqlite3.connect("almond_datas.db", check_same_thread = False)
cur = con.cursor()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods = ['POST'])
def register():
    name = request.form.get('login')
    password = request.form.get('password')

    if request.method == 'POST':
        users = cur.execute("SELECT * FROM users").fetchall()

        if name in users:
            error = 'Such user already exist'
            return render_template('register.html', error = error)
        else:
            cur.execute(
                "INSERT INTO users (user_login, user_password, user_admin) VALUES (?, ?, ?)", [name, password, False]
            )
            con.commit()
            return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return render_template('register.html')

@app.route('/loggin')
def loggin():
    return render_template('login.html')

@app.route('/login')
def login():
    name = request.form.get('login')
    password = request.form.get('password')

    users = cur.execute("SELECT * FROM users").fetchall()

    for i in users:
        if name == i[1] and password == i[2]:
            return redirect(url_for('index'))
    
    

    return render_template('login', error = "Incorrect name or password")

@app.route('/infoofproduct')
def infoofproduct():
    return render_template('infoofproduct.html')




if __name__ == '__main__':
    app.run(debug = True)
