import urllib.request
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

def getSeasonData(url):
    content = urllib.request.urlopen(url)
    read_content = content.read()
    soup = BeautifulSoup(read_content,'html.parser')
    return soup.find_all("span", {"class": "ipl-rating-star__rating"})

def extractRatins(data):
    ratings = list(map(float, re.findall(r'\d+\.\d+', str(data))))
    return ratings

def plotRatings(ratings, episodes, title):
    ticks = list(range(len(episodes)))
    plt.plot(episodes, ratings)
    plt.xticks(ticks, episodes)
    plt.yticks(ticks, ratings)
    plt.xlim(1, len(ratings))
    plt.ylim(1, ratings[len(ratings)-1]+1)
    plt.xlabel('episodes')
    plt.ylabel('ratings')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    url = 'https://www.imdb.com/title/tt0903747/episodes?season=4'
    data = getSeasonData(url)
    ratings = extractRatins(data)
    episodes = list(range(len(ratings)))
    title = "Breaking bad S4"
    plotRatings(ratings, episodes, title)
