import bs4
html = """
<html>
<body>
  <h3>Names</h3>
  <ul>
    <li>Tim</li>
    <li>Matt</li>
    <li>Elie</li>
    <li>Janey</li>
  </ul>
</body>
</html>
"""

soup = bs4.BeautifulSoup(html, "html.parser")

for li in soup.find_all('li'):
    print(li.text)
