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

@app.route('/m/<meetup>')
def notes(meetup):
    return redirect("https://github.com/ADGPoznan/meetup-notes/blob/master/adg-{}.md".format(meetup))

if __name__ == '__main__':
    app.run()
