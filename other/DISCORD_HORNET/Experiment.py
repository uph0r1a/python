from discord.ext import commands
from discord.ui import Button, View
import discord
from discord import Color
import asyncio


class Experiment(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def buttontest(self, ctx):
        button1 = Button(
            label="SHUT THE FUCK UP NI",
            style=discord.ButtonStyle.danger,
            emoji="<:Extreme_Demon:598408597696675859>",
        )
        button2 = Button(
            label="Sure, let's be friends!", style=discord.ButtonStyle.green
        )
        button3 = Button(label="Show me yo ass honey", emoji="❤️")

        embed = discord.Embed(
            title="My name is Hornet!",
            description="I want to be everyone's best friend! Will you be my friend?",
            colour=Color.blue(),
        )

        async def callback1(interaction):
            await interaction.response.send_message(
                "https://cdn.discordapp.com/attachments/987672644377788447/1015499244037230652/FA82B4A9-07B4-4E79-BE61-9DAAA37878AB.jpg",
                ephemeral=True,
            )

        async def callback2(interaction):
            await interaction.response.send_message(
                "im over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealim over here strokin my dick i got lotion on my dick right now im just stroking my shit im horny as fuck man im a freak man like forrealYOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU YOU ARE STUF STUF FUCK FUCK SHIT FUCK BITCH CUNT FUCKING YOU",
                ephemeral=True,
            )

        async def callback3(interaction):
            await interaction.response.defer()
            await interaction.followup.send("Ok.....", ephemeral=True)
            await asyncio.sleep(3)
            await interaction.followup.send(
                "Please wait, im taking off my cloths.. ;)", ephemeral=True
            )
            await asyncio.sleep(5)
            await interaction.followup.send("Taking picture now! :D", ephemeral=True)
            await asyncio.sleep(2)
            await interaction.followup.send(
                "https://media.discordapp.net/attachments/894835555882401802/1011664080311951442/unknown.png",
                ephemeral=True,
            )
            await interaction.followup.send(
                "I hope you enjpy it, call me later ;)", ephemeral=True
            )

        button1.callback = callback1
        button2.callback = callback2
        button3.callback = callback3
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        await ctx.send(embed=embed, view=view)


async def setup(client):
    await client.add_cog(Experiment(client))
