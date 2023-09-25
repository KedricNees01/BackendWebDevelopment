from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "<p><a href='/'>Home</a> | <a href='/day'>Day</a> | <a href='/month'>Month</a> | <a href='/year'>Year</a></p>"

@app.route("/day")
def day():
    date = datetime.date.today()
    day = date.day
    return f"<p>The current day is: { day }</p> <br> <p><a href = '/'>Home test</a>"

@app.route("/month")
def month():
    date = datetime.date.today()
    month = date.strftime('%B')  
    return f"<p>The current month is: { month }</p> <br> <p><a href = '/'>Home</a>"

@app.route("/year")
def year():
    date = datetime.date.today()
    year = date.year
    return f"<p>The current year is: { year }</p> <br> <p><a href = '/'>Home</a>"

if __name__ == '__main__':
    app.run(debug=True)

