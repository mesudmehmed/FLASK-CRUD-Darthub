from flask import render_template, request, url_for, redirect, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from configuration import app, db, evenement, User
@app.route("/")
@app.route("/home")
def home():
    if "userses" in session:
        all_data = evenement.query.all()
        return render_template('index.html', evenementen=all_data)
    else:
        all_data = evenement.query.all()
        return render_template('indexN.html', evenementen=all_data)



@app.route("/eventform", methods = ["GET","POST"])
def eventform():
    if "userses" in session:
        login = session["userses"]
        return render_template('eventform.html')
    else:
        return redirect(url_for('login'))


@app.route("/eventformcomplete")
def eventformcomplete():
    return render_template('eventformcomplete.html')

@app.route("/signinform/<id>", methods = ["GET"])
def signinform(id):
    if request.method == 'GET':
        my_data = evenement.query.get(id)
        return render_template('signinform.html', signinevenement = my_data)

@app.route("/api/evenementpage")
def evenementpage():
    return render_template('signinform.html')

@app.route("/logout")
def logout():
   session.pop("userses", None)
   return redirect(url_for('login'))

@app.route("/profile")
def profile():
    if "userses" in session:
        login = session["userses"]
        all_data = evenement.query.all()
        return render_template('profile.html', evenementen=all_data)
    else:
        return redirect(url_for('login'))



@app.route("/login",  methods = ["GET","POST"])
def login():
    if "userses" in session:
        login = session["userses"]
        return redirect(url_for('profile'))
    else:
        return render_template('login.html')



@app.route("/login_user",  methods = ["GET","POST"])
def login_user():
    name = request.form.get('name')
    password = request.form.get('password')
    session.permanent = True
    session['userses'] = name
    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        flash('Check je login a sahbi !')
        return redirect(url_for('login'))
    return redirect(url_for('profile'))



@app.route("/register",  methods = ["GET","POST"])
def register():
    return render_template('signup.html')

@app.route("/signup",  methods = ["GET","POST"])
def signup():
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()
    if user:
        return redirect(url_for('auth.signup'))
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))
@app.route("/insert", methods = ["GET","POST"])
def insert():
    if request.method == 'POST':
        cafe = request.form['cafe']
        location = request.form['location']
        date = request.form['date']
        time = request.form['time']
        description = request.form['description']
        beloweighteen = request.form.get("beloweighteen")
        print(request.form);
        my_data = evenement(location=location,
                            cafe=cafe,
                            date=date,
                            time=time,
                            description=description,
                            beloweighteen=beloweighteen
                            )

        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('home'))      

## onderstaande wordt nog niet gebruikt

# wijzig event via route 'update'
@app.route("/update", methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = evenement.query.get(request.form.get('id'))
        my_data.location = request.form['location']
        my_data.date = request.form['date']
        my_data.time = request.form['time']
        my_data.description = request.form['description']
        my_data.beloweighteen = request.form.get("beloweighteen")


        db.session.commit()
        flash("Evenement succesvol ge-update")

        return redirect(url_for('home'))   


@app.route("/delete/<id>", methods = ['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        my_data = evenement.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('profile'))

   




        
        
        







