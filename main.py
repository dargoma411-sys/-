from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def post_str():
    return render_template('post.html')

@app.route('/post1')
def post_str1():
    return render_template('post1.html')

@app.route('/post2')
def post_str2():
    return render_template('post2.html')

app.run(debug=True)