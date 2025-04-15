import unittest
from selenium import webdriver

# browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)

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

