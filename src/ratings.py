import imdb
import matplotlib.pyplot as plt
import sys

def plotRatings(ratings, episodes, title):
    y_ticks = list(range(1,11))
    plt.plot(episodes, ratings)
    plt.xticks(episodes, episodes)
    plt.yticks(y_ticks, ratings.sort())
    plt.xlim(1, len(ratings))
    plt.ylim(1, 10)
    plt.xlabel('episodes')
    plt.ylabel('rating')
    plt.title(title)
    plt.show()

def getRatings(name, season):
    ia = imdb.IMDb()
    show = ia.search_movie(name)[0]
    ia.update(show, 'episodes')
    s4 = show['episodes'][season]
    ratings = []
    episodes = list(range(1,len(s4)+1))
    title = name + " S" + str(season)
    for i in range(1,len(s4)+1):
        ratings.append(s4[i]['rating'])
    plotRatings(ratings, episodes, title)

def Main():
    if(len(sys.argv) < 2):
        print("Error: no arguments given")
    elif(len(sys.argv) < 3):
        print("Error: please specify show and season")
    elif(len(sys.argv) > 3):
        print("Error: too many arguments, maybe put quotes around show name")
    else:
        getRatings(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
    Main()
