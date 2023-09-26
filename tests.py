from app import app
import datetime

if __name__ == '__main__':
    with app.test_client() as client:
        date = datetime.date.today()
        day = str(date.day).encode('utf-8')
        month = (date.strftime('%B')).encode('utf-8')
        year = str(date.year).encode('utf-8')
        #Test the day route
        response = client.get('/day')
        assert day in response.data
        #Test the month route
        response = client.get('/month')
        assert month in response.data
        #Test the year route
        response = client.get('/year')
        assert year in response.data