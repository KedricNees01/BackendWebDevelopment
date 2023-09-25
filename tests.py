from app import app

if __name__ == '__main__':
    with app.test_client() as client:
        #Test the day route
        response = client.get('/day')
        assert b'The current day is' in response.data
        #Test the month route
        response = client.get('/month')
        assert b'The current month is' in response.data
        #Test the year route
        response = client.get('/year')
        assert b'The current year is' in response.data