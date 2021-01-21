from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
import mysql.connector

app = Flask(__name__)

from Assigment10_bluprint.assignment10 import Assignment10
app.register_blueprint(Assignment10)

@app.route('/')
def main_page():
    return render_template('CV_Liron_Dery.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')

@app.route('/assignment9', methods=['GET','POST'])
def Assignment9():
    if request.method == 'POST':
        session['logged_in'] = True
        username = request.form['username']
        return render_template('assignment9.html', username=username)

    if request.method == 'GET':
        res = ''
        list = []
        users = ['Naama Ilany Tzur', 'Arseni Pertzovsky', 'Evyatar Luvaton']
        emails = {'Naama Ilany Tzur':  'naamail@post.bgu.ac.il',
                  'Arseni Pertzovsky':  'arsenip@post.bgu.ac.il',
                  'Evyatar Luvaton': 'luvaton@post.bgu.ac.il '}
        if 'name' in request.args:
            res = request.args['name']
            User = [i for i in users if res in i]
            for j in User:
                list.append(emails[str(j)])
            submited = "True"
            return render_template('assignment9.html', name=User, email=list, submited=submited)
        else:
            return render_template('assignment9.html', name=users, email=emails)

    return render_template('assignment9.html')

@app.route('/assignment8')
def music():
    login = 'someone'
    return render_template('assignment8.html', head='My preferences in music is:', artists=['Infected Mushroom', 'Chet Faker', 'Guy Mezig','RuPaul'], user=login)

if __name__ == '__main__':
    app.run(debug=True)
