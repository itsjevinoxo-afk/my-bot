import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓 البوت يعمل بنجاح!")


bot.run("MTU1ODU4NTYwNzg5NzQ4NTM3Mg.GiyzPR.q7PG5uDHwtTnvnspSUxr4QOgyIgyIjBMlsaIwU")
