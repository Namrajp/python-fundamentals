import bs4
html = """
<html>
<body>
  <div id="interesting-data">Moxie is my cat</div>
</body>
</html>
"""

soup = bs4.BeautifulSoup(html, "html.parser")

div = soup.find(id="interesting-data")
print(div.text)
