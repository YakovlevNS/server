from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#def test():
#    return('<h1>Hello, world!</h1>')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def login():
    if request.method == 'POST':
        name=request.form['uname']
        password=request.form['password']
        return "Login: "+name+" <br> "+"Password: "+password

if __name__== "__main__":
    app.run(host="0.0.0.0")