import pyjokes
import imdb
import billboard
import randfacts
import random
from tqdm import tqdm


def tq():
    for i in tqdm(range(int(9e6))):
        pass


def joke():
    """Random joke"""
    tq()
    print('\nJoke for you:\n', pyjokes.get_joke(language='en', category='neutral'))
    while True:
        print('\nWould you like another joke?')
        user_choose = input('Try (y/n): ').lower()
        match user_choose:
            case 'y':
                print('\n', pyjokes.get_joke(language='en', category='neutral'))
            case 'n':
                break


def movie():
    """Movie recommendation from IMDB Top-250 """
    tq()
    ia = imdb.Cinemagoer()
    get_movie = ia.get_top250_movies()
    recommend_movie = random.choice(get_movie)
    print('\nMovie recommendation from Top-250 IMDB:\n', recommend_movie['title'], recommend_movie['year'])
    while True:
        print('\nWould you like another movie?')
        user_choose = input('Try (y/n): ').lower()
        match user_choose:
            case 'y':
                print('\n', random.choice(get_movie)['title'], random.choice(get_movie)['year'])
            case 'n':
                break


def series():
    """TV series recommendation from IMDB Top-100"""
    tq()
    io = imdb.Cinemagoer()
    get_ser = io.get_popular100_tv()
    recommend_tv = random.choice(get_ser)
    print('\nTV series recommendation from Top-100 IMDB:', recommend_tv['title'], recommend_tv['year'])
    while True:
        print('\nWould you like another TV serial?')
        user_choose = input('Try (y/n): ').lower()
        match user_choose:
            case 'y':
                print('\n', random.choice(get_ser)['title'], random.choice(get_ser)['year'])
            case 'n':
                break


def fact():
    """Random fact"""
    tq()
    print('\nFact for you:\n\n', randfacts.get_fact(), '\nAnyway we can\'t check is it True')
    while True:
        print('\nWould you like another interesting fact?')
        user_choose = input('Try (y/n): ').lower()
        match user_choose:
            case 'y':
                x = randfacts.get_fact()
                print('\n', x)
            case 'n':
                break


def music():
    """Music recommendation from Billboards Hot-100"""
    tq()
    chart = billboard.ChartData('hot-100')
    get_chart = chart.entries
    get_song = random.choice(get_chart)
    print('\nBillboard\'s Hot-100 random song for you:\n', get_song)
    while True:
        print('\nWould you like another song?')
        user_choose = input('Try (y/n): ').lower()
        match user_choose:
            case 'y':
                print('\n', random.choice(get_chart))
            case 'n':
                break
