from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def main():
    return redirect("https://www.meetup.com/Poznan-Android-Developer-Group/")

@app.route('/facebook')
def facebook():
    return redirect("https://www.facebook.com/PoznanADG")

@app.route('/+')
def plus():
    return redirect("https://plus.google.com/b/110698548189316294491/110698548189316294491/posts")

@app.route('/github')
def github():
    return redirect("https://github.com/ADGPoznan")

@app.route('/jetbrains')
def jetbrains():
    return redirect("https://goo.gl/forms/Ola7S0KjIHOHyv652")

@app.route('/mobilizacja')
def mobilization():
    return redirect("https://goo.gl/forms/rjvea0dj0OwFFzRR2")

if __name__ == '__main__':
    app.run()
