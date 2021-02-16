import imdb 
import random

ia = imdb.IMDb()

actors = ia.search_person("Robert Pattinson")
ID = actors[0].personID
actor = ia.get_person(ID)
filmography = actor.get('filmography')
a = filmography['actor']
print(len(a))
print (filmography)