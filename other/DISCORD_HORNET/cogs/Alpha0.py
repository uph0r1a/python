from discord.ext import commands
import spotipy
from spotipy_random import get_random
from spotipy.oauth2 import SpotifyClientCredentials
from translate import Translator
from random_words import RandomWords
from pydictionary import Dictionary
from googlesearch import search
import random
import json


spotify_client = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id="No", client_secret="No")
)


class ServerExclusive(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def randomsong(self, ctx, *, genre="pop"):
        try:
            random_pop_song_json: str = get_random(
                spotify_client,
                type="track",
                genre=genre,
            )
            song_url = random_pop_song_json["external_urls"]["spotify"]
            song_name = random_pop_song_json["name"]
            await ctx.send(
                f"Song name: **{song_name}** \nURL: {song_url} \nGenre: {genre}"
            )
        except IndexError:
            await ctx.send(f"Silly ghost, **{genre}** is not an actual genre.")

    @commands.command()
    async def searchsong(self, ctx, *, q):
        result = spotify_client.search(q, limit="1", type="track")
        SName = result["tracks"]["items"][0]["name"]
        SURL = result["tracks"]["items"][0]["external_urls"]["spotify"]
        await ctx.send(f"Song name: **{SName}**\nURL: {SURL}")

    @commands.command()
    async def searchartist(self, ctx, *, q):
        result = spotify_client.search(q, limit="1", type="artist")
        AName = result["artists"]["items"][0]["name"]
        ALink = result["artists"]["items"][0]["external_urls"]["spotify"]
        AFollowers = result["artists"]["items"][0]["followers"]["total"]
        AMainGenre = result["artists"]["items"][0]["genres"][0]
        await ctx.send(
            f"**__{AName}__**\nHas a total of **{AFollowers}** followers\nMost active in *{AMainGenre}* genre.\n__URL:__ {ALink}"
        )

    @commands.command()
    async def korean(self, ctx):
        rw = RandomWords()
        word = rw.random_word().capitalize()
        dict = Dictionary(word)
        meanings_list = dict.meanings()
        result = meanings_list[0].capitalize()
        translator = Translator(to_lang="ko")
        translation = translator.translate(word)
        await ctx.send(f"**{translation}**: {word}\n__Definition:__ {result}")

    @korean.error
    async def korean_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(
                "My apologies little ghost, but the word i received is not valid. \n**Please try again.**"
            )

    @commands.command()
    async def google(self, ctx, *, query):
        results = search(query, num_results=1)
        for result in results:
            await ctx.send(result)

    @commands.command()
    async def tarot(self, ctx):
        with open("tarot.json", "r") as f:
            cardset = json.load(f)
            await ctx.send(random.choice(cardset["cards"]))


async def setup(client):
    await client.add_cog(ServerExclusive(client))
