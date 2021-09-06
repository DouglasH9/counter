from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'omar comin!'

@app.route('/')
def log_visits():
    counter = 1
    if button.form() == 'addvisits':
        counter += 2
    session['reset'] = request.form['reset']

    return redirect('/show')

@app.route('/show')
def show_info():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)