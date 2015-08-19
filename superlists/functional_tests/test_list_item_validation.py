from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys



class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # Edit goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #She tries again with some text for the item, which now works
        inputbox.send_keys('Get milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Get milk')

        #Pervsersely, she now decides to submit a second blank list item
        inputbox.send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Get milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #And she can correct it by filling some text in
        inputbox.send_keys('Make tea')
        self.check_for_row_in_list_table('1: Get milk')
        self.check_for_row_in_list_table('2: Make tea')


