import discord
from discord.ext import commands

# Define the bot's prefix and enable necessary intents
# A command prefix tells the bot when a message is a command (e.g., !ping)
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler: runs when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command handler: a simple command
@bot.command()
async def ping(ctx):
    """Responds with 'Pong!' when a user types !ping"""
    await ctx.send('Pong!')

# Run the bot with your token
bot.run('YOUR_TOKEN')
