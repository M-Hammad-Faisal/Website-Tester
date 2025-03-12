import allure


@allure.feature("Social Links")
class TestSocialLinks:
    @allure.title("Click Twitter/X Link")
    def test_twitter_link(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.click_twitter_link()
        print(inventory_page.element.url())
        assert "x.com" in inventory_page.element.url(), "Twitter/X link not working"

    @allure.title("Click Facebook Link")
    def test_facebook_link(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.click_facebook_link()
        print(inventory_page.element.url())
        assert "facebook.com" in inventory_page.element.url(), "Facebook link not working"

    @allure.title("Click LinkedIn Link")
    def test_linkedin_link(self, pages, login_as_standard_user):
        inventory_page = pages["inventory"]
        inventory_page.click_linkedin_link()
        print(inventory_page.element.url())
        assert "linkedin.com" in inventory_page.element.url(), "LinkedIn link not working"
