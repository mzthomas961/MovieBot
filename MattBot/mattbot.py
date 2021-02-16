
import discord
from discord.ext import commands
import imdb 
import random

ia = imdb.IMDb()


		
client = commands.Bot(command_prefix='!')

@client.command(name='good')
async def good(context):
    top = ia.get_top250_movies()    
    random_movie = random.choice(top)
    await context.message.channel.send(random_movie)  

@client.command(name='bad')
async def good(context):
    bottom = random.choice(ia.get_bottom100_movies())
    await context.message.channel.send(bottom)  

@client.command(name='random')
async def good(context, argument):
    genres = ia.search_keyword(argument)
    genre = genres[0]
    movies = ia.get_keyword(genre)
    rand_movie = random.choice(movies)
    await context.message.channel.send(rand_movie)  

@client.command(name='actor')
async def good(context, argument):
    actors = ia.search_person(argument)
    ID = actors[0].personID
    actor = ia.get_person(ID)
    filmography = actor.get("filmography")
    a = filmography['actor']
    size = len(a)
    r = random.randint(1,size)
    movie = filmography['actor'][r]['title']

    await context.message.channel.send(movie)  




    



client.run('ODExMDM4NzI0NzI5MjA4OTIy.YCsYrA.e-tJToPkP9RfhTOKawfqUcGn9DM')               
