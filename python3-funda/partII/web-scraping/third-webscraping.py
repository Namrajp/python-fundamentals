import urllib.request
import bs4

url = 'https://news.ycombinator.com/'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")

links = soup.select("a.storylink")

for link in links:
    print(f"{link['href']} {link.text}")
