from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

@app.route('/defaultsite')
def cookies():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
