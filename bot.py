import discord
from discord.ext import commands
import os
import openai   # 👈 add this

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 👇 AI setup
openai.api_key = os.getenv("OPENAI_API_KEY")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 👇 your commands
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 👇 ADD THE AI COMMAND HERE
@bot.command()
async def ai(ctx, *, prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Discord bot."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        await ctx.send(reply)

    except Exception as e:
        await ctx.send("Error with AI.")
        print(e)

# 👇 ALWAYS keep this at the VERY BOTTOM
bot.run(os.getenv("TOKEN"))
