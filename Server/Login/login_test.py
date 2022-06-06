import requests

class TestLogin:

    def test_login_correctly(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myid = {"email": "melakubetty@gmail.com", "password": "123456"}
        response = requests.post(url, json=myid)
        res_data = response.json()
        assert response.status_code == 200
        assert res_data['message'] == "logged in successfully"
        assert response.elapsed.total_seconds() < 5


    def test_login_with_incorrect_email(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myid = {"email": "aaaa@gmail.com", "password": "123456"}
        response = requests.post(url, json=myid)
        res_data = response.json()
        assert response.status_code == 500
        assert res_data['message'] == 'Error logging in user'
        assert response.elapsed.total_seconds() < 5


    def test_login_with_incorrect_password(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myid = {"email": "melakubetty@gmail.com", "password": "1234567"}
        response = requests.post(url, json=myid)
        res_data = response.json()
        assert response.status_code == 403
        assert res_data['message'] == "Invalid credentials"
        assert response.elapsed.total_seconds() < 5
