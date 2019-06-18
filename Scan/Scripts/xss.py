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
        url = str.encode(self._web_url)
        with open('Scan/Scripts/XSS-vectors.txt') as f:
            for line in f:
                browser.open(url)
            browser.select_form(nr=0)
            browser["searchkey"] = line
            #https://www.woodlandworldwide.com/wnew/faces/search.jsp?searchkey=%3Cscript%3Ealert(1)%3C/script%3E&clg=10
            res = browser.submit()
            content = res.read()
            # check the attack vector is printed in the response.
            if content.find(line) > 0:
                self._status = True
            output = open('response/' + str(attackNumber) + '.txt', 'w')
            output.write(content)
            output.close()
            attackNumber += 1


