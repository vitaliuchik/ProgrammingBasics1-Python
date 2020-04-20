def filter_movies():
    movies = []
    f = open('data/title_basics.tsv', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        movie = line.split('\t')
        if movie[1] == 'movie' and movie[-1][-3:-1] != '\\N':
            movies.append(movie[0] + '\t' + movie[-1][:-1])
    f.close()

    f = open('new_title_basics.tsv', 'w', encoding='utf-8')
    print('ID\tGenre', file=f)
    for movie in movies:
        print(movie, file=f)
    f.close()


def filter_directors():
    f = open('new_title_basics.tsv', encoding='utf-8')
    movies = f.readlines()[1:]
    f.close()

    empty = []
    directors = []
    f = open('data/title_crew.tsv', encoding='utf-8')
    i = 0
    lines = f.readlines()
    for line in lines:
        crew = line.split('\t')
        if crew[0] ==  movies[i].split('\t')[0]:
            crew[1] = crew[1].split(',')[0]
            new_line = crew[0] + '\t' + crew[1]
            if crew[1] != '\\N':
                directors.append(new_line)
            else:
                empty.append(crew[0])
            if i != len(movies) - 1:
                i += 1
    f.close()

    f = open('new_title_crew.tsv', 'w', encoding='utf-8')
    print('tconst\tdirectors', file=f)
    for crew in directors:
        print(crew, file=f)
    f.close()
    return empty


def movies_without_directors(empty):
    movies = []
    f = open('new_title_basics.tsv', encoding='utf-8')
    lines = f.readlines()[1:]
    i = 0
    for line in lines:
        line = line[:-1]
        movie = line.split('\t')
        if i <= len(empty):
            if movie[0] != empty[i]:
                movies.append(line)
            else:
                i += 1
    f.close()

    f = open('new_title_basics.tsv', 'w', encoding='utf-8')
    print('ID\tGenre', file=f)
    for movie in movies:
        print(movie, file=f)
    f.close()
    return movies


def filter_names():
    f = open('new_title_crew.tsv', encoding='utf-8')
    directors = f.readlines()[1:]
    f.close()
    directors.sort(key = lambda x: int(x.split('\t')[1][2:-1]) )

    f = open('data/name_basics.tsv', encoding='utf-8')
    names = f.readlines()[1:]
    f.close()

    i = 0
    for name in names:
        name = name.split('\t')
        if i <= len(directors):
            director = directors[i][:-1].split('\t')
            if name[0] == director[1]:
                directors[i] = director[0] + '\t' + name[1]
                i += 1
                while (name[0] == directors[i][:-1].split('\t')[1]):
                    directors[i] = directors[i].split('\t')[0] + '\t' + name[1]
                    i += 1

    directors.sort(key = lambda x: int(x.split('\t')[0][2:]) )

    f = open('new_title_crew.tsv', 'w', encoding='utf-8')
    print('tconst\tdirectors', file=f)
    for director in directors:
        print(director, file=f)
    f.close()
    return directors


def filter_rating(movies):
    f = open('data/ratings.tsv', encoding='utf-8')
    ratings = f.readlines()[1:]
    f.close()

    new_ratings = []
    i = 0
    for rating in ratings:
        rating = rating[:-1].split('\t')
        while (int(rating[0][2:]) > int(movies[i].split('\t')[0][2:])):
            new_ratings.append(movies[i].split('\t')[0] + '\t' + '4.0')
            i += 1
        if rating[0] == movies[i].split('\t')[0]:
            new_ratings.append(rating[0] + '\t' + rating[1])
            if i <= len(movies) :
                i += 1

    f = open('new_ratings.tsv', 'w', encoding='utf-8')
    print('tconst\trating', file=f)
    for rating in new_ratings:
        print(rating, file=f)
    f.close()
    return new_ratings


def combine(genres, directors, ratings):
    data = []
    f = open('data.tsv', 'w', encoding='utf-8')
    print('Genre\tDirector\tRating', file=f)
    for i in range(len(ratings)):
        genre = genres[i].split('\t')[1]
        director = directors[i].split('\t')[1]
        if director[:2] == 'nm':
            continue
        rating = ratings[i].split('\t')[1]
        print(genre + '\t' + director + '\t' + rating, file=f)
        data.append([genre, director, float(rating)])
    f.close()


filter_movies()
directors = filter_directors()
genres = movies_without_directors(directors)
directors = filter_names()
ratings = filter_rating(directors)
combine(genres, directors, ratings)

# main program
f = open('data.tsv', encoding='utf-8')
lines = f.readlines()[1:]
f.close()

data = dict()
for line in lines:
    line = line[:-1].split('\t')
    lst = line[0].split(',')
    for genre in lst:
        data[genre] = data.get(genre, list())
        data[genre].append([line[1], float(line[2])])

for key in data:
    directors = dict()
    for lst in data[key]:
        directors[lst[0]] = data.get(lst[0], list())
        directors[lst[0]].append(lst[1])
    for direc in directors:
        directors[direc] = sum(directors[direc]) / len(directors[direc])
    data[key] = list(directors.items())

for genre in data:
    data[genre].sort(key = lambda x: x[1])
    data[genre].reverse()

print('Top 5 directors of each genre')
for genre in data:
    print('\n')
    print(genre + ':' + ' '*(19 - len(genre)) + '1. ' + data[genre][0][0])
    for i in range(1,5):
        print(' '*20 + str(i+1)+ '. ' + data[genre][i][0])
