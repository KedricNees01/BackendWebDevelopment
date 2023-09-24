from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/day")
def day():
    date = datetime.date.today()
    day = date.day
    return render_template('day.html', day = day)

@app.route("/month")
def month():
    date = datetime.date.today()
    month = date.strftime('%B')  
    return render_template('month.html' , month = month)

@app.route("/year")
def year():
    return render_template('year.html')

if __name__ == '__main__':
    app.run(debug=True)


