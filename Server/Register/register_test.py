import requests

class TestRegister:

    def test_register_correctly(self):
        url = "https://wetechsocial.herokuapp.com/auth/register"
        myid = {"city": "New York","coverPicture": "https://www.thespruce.com/thmb/GXWSYLeNjoCgNichOYUFMkthTzI="
                                                   "/941x0/filters:no_upscale():max_bytes(150000):"
                                                   "strip_icc():format(webp)/the-difference-between-trees-and-"
                                                   "shrubs-3269804-hero-a4000090f0714f59a8ec6201ad250d90.jpg",
                "email": "jjj8j@gmail.com","from": "USA","password": "123456789","profilePicture": "hhhhhhh","userLastName": "Ayasso","userName": "Anat"}
        response = requests.post(url, json=myid)
        res_data = response.json()
        assert response.status_code == 200
        assert res_data['message'] == "User as been added successfully"
        assert response.elapsed.total_seconds() < 5

    def test_register_with_incorrect_email(self):
        url = "https://wetechsocial.herokuapp.com/auth/register"
        myid = {"city": "New York","coverPicture": "https://www.thespruce.com/thmb/GXWSYLeNjoCgNichOYUFMkthTzI="
                                                   "/941x0/filters:no_upscale():max_bytes(150000):"
                                                   "strip_icc():format(webp)/the-difference-between-trees-and-"
                                                   "shrubs-3269804-hero-a4000090f0714f59a8ec6201ad250d90.jpg",
                "email": "jjj8j@gmail.co","from": "USA","password": "123456789","profilePicture": "hhhhhhh","userLastName": "Ayasso","userName": "Anat"}
        response = requests.post(url, json=myid)
        res_data = response.json()
        assert response.status_code == 200
        assert res_data['message'] == "User as been added successfully"
        assert response.elapsed.total_seconds() < 5
