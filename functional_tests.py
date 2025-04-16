import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




# browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("http://localhost:8000")

        # Check the title and header of the page.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do",header_text)

        # check the input box, and what is the placeholder
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # User enters the item in input box
        inputbox.send_keys("Buy peacock feathers")

        # When the user hits enter, the page updates and shows the item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1:Buy peacock feathers" for row in rows))


        self.fail("Finsih the test!")


if __name__ == "__main__":
    unittest.main()




# Open the web application
# Make sure you have the server running on localhost:8000
# and the browser can access it.
# browser.get("http://localhost:8000")

# # Check the title of the page
# assert "To-Do" in browser.title

# # Entering the first to-do item

# # when submitted it should, the page should refresh and show the item

# # It should show the text box to add in the next item

# # when submitted it should, the page should refresh and show both the items

# # done entering the items

# browser.quit()

