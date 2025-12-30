from discord.ext import commands
import youtube_dl
import discord
import sys

sys.dont_write_bytecode = False


"""
TODO:
1. Join from Play command
2. Play from both link and search
3. Spotify and Youtube
4. Queue
5. Now Playing


"""


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in the vc yet, Prove yourself ready to face it.")
        vc = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vc.connect()
            print(f"Bot joined Voice Chat {ctx.author.voice.channel.name}")
        else:
            await ctx.voice_client.move_to(vc)
            print(f"Bot moved to Voice Chat {ctx.author.voice.channel.name}")

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        print(f"Bot Disconnected from {ctx.author.voice.channel.name}")
        await ctx.send("Hallownest was never eternal.")

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {"options": "-vn"}
        YTDL_OPTIONS = {"format": "bestaudio"}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ytdl:
            info = ytdl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            await ctx.send("The song is now playing.")

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Little ghost, I have paused the player.")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("The player is resumed, little ghost.")


async def setup(client):
    await client.add_cog(Music(client))
