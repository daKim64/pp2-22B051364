# Dictionary of movies

movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# Task 1
def highscore(mname):
    for movie in range(len(movies)):
        if movies[movie]["name"] == mname:
            if movies[movie]["imdb"] > 5.5:
                return True
            return False
    return "No movie has been found"


print(highscore("We Twos"))


# Task 2
def popular():
    poplist = []
    for movie in range(len(movies)):
        if movies[movie]["imdb"] > 5.5:
            poplist.append(movies[movie]["name"])
    print(poplist)


popular()


# Task 3
def category(cat):
    catlist = []
    for movie in range(len(movies)):
        if movies[movie]["category"] == cat:
            catlist.append(movies[movie]["name"])
    print(catlist)


category("Thriller")


# Task 4
def average():
    score = 0
    for movie in range(len(movies)):
        score += movies[movie]["imdb"]
    return score / len(movies)


print(average())


# Task 5
def catscore(cat):
    score = 0
    quantity = 0
    for movie in range(len(movies)):
        if movies[movie]["category"] == cat:
            score += movies[movie]["imdb"]
            quantity += 1
    return score / quantity


print(catscore("Thriller"))
