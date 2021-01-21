from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, jsonify
import mysql.connector

Assignment10 = Blueprint('Assignment10', __name__,
                          static_folder='static',
                          static_url_path='/Assignment_10',
                          template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

@Assignment10.route('/assignment10', methods=['GET','POST'])
def assignment10():
    user_query = "select * from users"
    result = interact_db(user_query, 'fetch')
    return render_template('/Assignment10.html', users=result)

@Assignment10.route('/insertUser', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        insert_query = "insert into users (ID, Name, Email) values ('%s','%s','%s')" % (id, name, email)
        interact_db(insert_query, 'commit')
        return redirect('/assignment10')
    return render_template('/Assignment10.html')

@Assignment10.route('/updateUser', methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        update_query = "update users set Name= '%s', Email='%s' where ID=%s" % (name, email, id)
        interact_db(update_query, 'commit')
        return redirect('/assignment10')
    return render_template('/Assignment10.html')

@Assignment10.route('/deleteUser', methods=['GET','POST'])
def delete_user():
    if request.method == 'GET':
        id = request.args['id']
        delete_query = "delete from users where id='%s'" % (id)
        interact_db(delete_query, 'commit')
        return redirect('/assignment10')
    return render_template('/Assignment10.html')

@Assignment10.route('/assignment11/users')
def assignment11_all():
    user_query = "select * from users"
    result = interact_db(user_query, 'fetch')
    return jsonify({
        'date': result
    })

@Assignment10.route('/assignment11/users/selected', defaults={'some_user_id':2})
@Assignment10.route('/assignment11/users/selected/<int:some_user_id>')
def assignment11_some_user(some_user_id):
    user_query = "select * from users where ID=%s" % (some_user_id)
    result = interact_db(user_query, 'fetch')
    if len(result) == 0:
        return jsonify({
            'message': 'there is no such ID %s in the DB' %(some_user_id)
        })
    else:
        return jsonify({
            'date': result
        })
    return f' users: {result}'

if __name__ == '__main__':
    assignment10.run(debug=True)
