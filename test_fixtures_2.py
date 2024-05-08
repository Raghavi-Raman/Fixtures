def data_fixture(func):
    def wrapper():
        return func()
    return wrapper

@data_fixture
def user_fixture():
    return {
        "id": 1,
        "username": "Raghavi",
        "email": "ragvi10raman@gmail.com",
        "password": "Admin@123"
    }
 
@data_fixture
def product_fixture():
    return {
        "id": 1,
        "name": "Raghavi Raman",
        "id": 8113814,
        "department": 400
    }

def test_user_fixture():
    user_data = user_fixture()
    assert user_data["username"] == "Raghavi"
    assert user_data["email"] == "ragvi10raman@gmail.com"
 
def test_product_fixture():
    product_data = product_fixture()
    assert product_data["name"] == "Raghavi Raman"
    assert product_data["id"] == 8113814

if __name__ == "__main__":
    test_user_fixture()
    test_product_fixture()
    print("All tests passed!")
