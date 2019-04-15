import mechanize

class XSS():

    def __init__(self, web_url):
        self._web_url = web_url
        self._status = False
        #status whether website is vulnerable to XSS

    def get_status(self):
        return self._status


    def scan(self):
        browser = mechanize.Browser()
        attackNumber = 1
        with open('XSS-vectors.txt') as f:
            for line in f:
                browser.open(self._web_url)
            browser.select_form(nr=0)
            browser["fname"] = line
            res = browser.submit()
            content = res.read()
            # check the attack vector is printed in the response.
            if content.find(line) > 0:
                self._status = True
            output = open('response/' + str(attackNumber) + '.txt', 'w')
            output.write(content)
            output.close()
            attackNumber += 1


