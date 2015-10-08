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
    return redirect("https://docs.google.com/forms/d/1a9XYQt8WbTVSuwPkZq4w_lbq_hSMFI6peDZw0LKfhJM/viewform?usp=send_form")


if __name__ == '__main__':
    app.run()
