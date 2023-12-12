from flask import Flask,redirect,url_for,render_template,request,flash


app=Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            print(f"Received form data - Name: {name}, Email: {email}")
            print(name)
            print(email)
            print(message)

            return redirect(url_for('welcome',name=name))
            # flash('thank you')
            flash(f'Thank you, {name}, for submitting the form!')
        

    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)