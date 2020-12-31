from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('CV_Liron_Dery.html')

@app.route('/assignment8')
def music():

    return render_template('assignment8.html', head='My preferences in music is:', artists=['Infected Mushroom''Chet Faker','Guy Mezig','RuPaul'],user='me')

if __name__ == '__main__':
    app.run(debug=True)
