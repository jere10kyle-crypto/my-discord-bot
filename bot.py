import discord
from discord.ext import commands
import os
from openai import OpenAI

# 🔑 Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ⚙️ Discord setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Bot ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 🏓 Test command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 🧠 AI command
@bot.command()
async def ai(ctx, *, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Discord bot."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content
        await ctx.send(reply)

    except Exception as e:
        await ctx.send("Error with AI.")
        print(e)

# 🚀 Run bot (KEEP THIS LAST)
bot.run(os.getenv("TOKEN"))
