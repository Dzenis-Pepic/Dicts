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


#1.zadatak

def score(x):
    if x['imdb'] <= 5.5:
        return False
    else:
        return True


#2.zadatak

def dobri(movies):
    dob=[]
    for x in movies:
        if x['imdb']>5.5:
            dob.append(x)
    return dob


# 3.zadatak
def zanr(neki):
    lista=[]
    for x in movies:
        if x['category']==neki:
            lista.append(x)
    return lista


# 4.zadatak

def avg(a):
    return sum(a)/len(a)

def sr_score(movies):
    a=[]
    for x in movies:
        a.append(x['imdb'])

    return avg(a)




# 5.zadatak

def prosek_kategorije(neki):
    s=0
    k=zanr(neki)
    for x in k:
        s=s+x['imdb']

    return s/len(k)

                  
