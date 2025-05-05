from pages.login_page import LoginPage

def test_valid_login(setup):
    login_page=LoginPage(setup)
    login_page.login("standard_user","secret_sauce")
    assert "inventory" in setup.current_url