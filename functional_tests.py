from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):

# edith has heard about a cool new online to-do app. She goes
# to check out its homepage

        self.browser.get('http://localhost:8000')

#she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
#she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

#she types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)
        inputbox.sed_keys('Buy peacock feathers')
        
#when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
        inputbox.sed_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
# There is still a text box inviting her to add another item.
# She enters "Use peacock feather's to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')
# The page updates again, and now shows both items on her list
# Edith wonders whether the site will remember her list.
# Then she sees that the site has generated a unique URL for her -- there is some explanatory text to that effect.
# she visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
