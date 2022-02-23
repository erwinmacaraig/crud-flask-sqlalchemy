from flask import render_template, url_for, redirect, request
from models import db, User, app


# Flask,
# app = Flask(__name__)

@app.route('/')
def index():
    destinations = ['Boracay', 'Hundred Islands', 'Villa Escudero']
    return render_template('index.html', dest=destinations)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dog-api-call')
def dog_ceo_api():
    return render_template('show-dog.html')


@app.route('/test-db', methods=['POST'])
def test_db():
    print(request.form)
    print(request.form['name'])
    new_user = User(name=request.form['name'], lastName=request.form['lastName'], age=request.form['age'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('retrieve_users'))


@app.route('/add-user-form')
def add_user_form():
    return render_template('add-user-form.html')


@app.route('/users')
def retrieve_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/edit-user/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    if request.form:
        user.name = request.form['name']
        user.lastName = request.form['lastName']
        user.age = request.form['age']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('retrieve_users'))

    return render_template('edit-user.html', user=user)


@app.route('/process-form', methods=['GET', 'POST'])
def process_form():
    print(request.form)
    return render_template('signup.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
