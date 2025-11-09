import urllib.request
import bs4
import csv

url = 'https://news.ycombinator.com/'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")

links = soup.select("a.storylink")

with open('articles.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter="\t")
    writer.writerow( ('Link', 'Title') )
    for link in links:
        writer.writerow( (link['href'], link.text) )
