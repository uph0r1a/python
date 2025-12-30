from discord import Color
from discord.ext import commands
import asyncio
import discord
import sys

sys.dont_write_bytecode = False


class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ["s", "m", "h", "d"]:
            return (int(amount), unit)
        raise commands.BadArgument(
            message="Little ghost, that's not a *valid* duration."
        )


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount > 1000:
            await ctx.send(f"Too many messages to purge given. (**{amount}**/1000).")
        elif amount > -1:
            await ctx.channel.purge(limit=amount + int(1))

        if amount == 1:
            itshumpday = await ctx.send("**1 message** was deleted.")
            await asyncio.sleep(7)
            await itshumpday.delete()
        elif amount == 0:
            itshumpday = await ctx.send("Nothing was deleted.")
            await asyncio.sleep(7)
            await itshumpday.delete()
        elif amount < 0:
            itshumpday = await ctx.send(
                "The purge was halted, little ghost. \n the amount is *negative*."
            )
            await asyncio.sleep(7)
            await itshumpday.delete()
        elif amount > 1000:
            pass
        else:
            itshumpday = await ctx.send(f"**{amount} messages** were deleted.")
            await asyncio.sleep(7)
            await itshumpday.delete()

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "Litte ghost, you should pass in the amount of messages you wish to expunge."
            )

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(
        self, ctx, member: commands.MemberConverter, duration: DurationConverter
    ):
        multiplier = {"s": 1, "m": 60, "h": 3600, "w": 604800}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(
            f"**{member}** has been banished from Hallownest for {amount}{unit}.\n\nOnly pity for their cursed kind."
        )
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @tempban.error
    async def tempban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to do so, little ghost.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing required arguments.")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"That user does not exist, {ctx.author.mention}.")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have the permissions to do so.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        if member == ctx.message.author:
            await ctx.channel.send("Ghost, you know you can't ban yourself.")
            return
        elif member == None:
            await ctx.channel.send(
                "Ghost, tell me the identity of the bug you wish to banish."
            )
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(
            f"**{member}** has forever been banished from Hallownest.\n\n**Reason:** {reason}"
        )

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to do so, little ghost.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"That user does not exist, {ctx.author.mention}.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        if member == ctx.message.author:
            await ctx.channel.send("Ghost, you know you can't kick yourself.")
            return
        elif member == None:
            await ctx.channel.send("Little one, specify the bug you wish to **kick**.")
            return
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(
            f"**{member}** has been kicked out of Hallownest.\n\n**Reason:** {reason}"
        )

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to do so, little ghost.")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"That user does not exist, {ctx.author.mention}.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name="Muted")
        if not role:
            muted = await ctx.guild.create_role(name="Muted")
            for (
                channel
            ) in (
                ctx.guild.channels
            ):  # removes permission to view and send in the channels
                await channel.set_permissions(muted, send_messages=False)
        await member.add_roles(role)
        await ctx.send(f"Succesfully quietened **{member}**.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name="Muted")
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"**{member}** has been granted freedom of speech.")
        else:
            await ctx.send(f"**{member}** already has freedom of speech.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def tempmute(self, ctx, member: discord.Member, duration: DurationConverter):
        multiplier = {"s": 1, "m": 60, "h": 3600, "w": 604800}
        amount, unit = duration
        role = discord.utils.get(member.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(
                "Muted", permissions=discord.Permissions(send_messages=False)
            )
        await member.add_roles(role)
        await ctx.send(
            f"Succesfully quietened **{member}** for {amount}{unit}.\n\nI know what you are. I know what you'd try to do. I can't allow it."
        )
        await asyncio.sleep(amount * multiplier[unit])
        await member.remove_roles(role)

    @tempmute.error
    async def tempmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to do so, little ghost.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing required arguments.")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"That user does not exist, {ctx.author.mention}.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member, *, role: discord.Role):
        # if the role is above users top role it sends error
        if (
            role.position < ctx.author.top_role.position
            or ctx.guild.owner == ctx.author
        ):
            if role in user.roles:
                # removes the role if user already has
                await user.remove_roles(role)
                await ctx.send(f"Took away **{role}** from **{user}**")
            else:
                # adds role if not already has it
                await user.add_roles(role)
                await ctx.send(f"**{user}** has been blessed with the role **{role}**")
        else:
            await ctx.send("Sorry Ghost.. **But that command shall not be executed**")


async def setup(client):
    await client.add_cog(Utilities(client))
