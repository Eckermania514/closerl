import discord
import psutil
from discord.ext import commands

# Define the bot's prefix and enable necessary intents
# A command prefix tells the bot when a message is a command (e.g., !ping)
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler: runs when the bot is ready
@bot.event
async def on_ready():
    print(f'enderman is online')

# Command handler: a simple command
@bot.command()
async def run_batch(ctx):
    """Runs the specified batch file."""
    batch_file_path = r'C:\scripts\main.bat' # Use a raw string (r'') for file paths

    if not os.path.exists(batch_file_path):
        await ctx.send(f"Error: Batch file not found at {batch_file_path}")
        return

    try:
        # Use subprocess.Popen to run the batch file without blocking the bot
        # creationflags=subprocess.CREATE_NEW_CONSOLE will open a new CMD window
        # or just run it in the background
        process = subprocess.Popen([batch_file_path], shell=True) 
        
        await ctx.send(f"closing rocket league in 600 seconds")
        time.sleep(600)
        await ctx.send(f"closing rocket league")

    except Exception as e:
        await ctx.send(f"error: {e}")

@bot.command()
async def rlstatus(ctx):
    process_name = "rocketleague.exe"
    is_running = False
    
    # Iterate over all running processes
    for proc in psutil.process_iter(['name']):
        try:
            # Check if process name matches (case-insensitive)
            if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                is_running = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Send result to Discord
    if is_running:
        await ctx.send("rl is open")
    else:
        await ctx.send("rl is not open")
"""
should show discord prescence updates
@bot.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    # Check if the user's activity has changed from not playing to playing something
    # or if the game name is different from the previous one.

    # Extract the name of the program being played
    playing_activity_after = next((activity.name for activity in after.activities if activity.type == discord.ActivityType.playing), None)
    playing_activity_before = next((activity.name for activity in before.activities if activity.type == discord.ActivityType.playing), None)

    if playing_activity_after != playing_activity_before:
        if playing_activity_after:
            print(f"{after.name} is playing {playing_activity_after}")
            # You can also send a message to a specific channel
            # channel = bot.get_channel(YOUR_CHANNEL_ID)
            # await channel.send(f"{after.name} is now playing {playing_activity_after}")
        elif playing_activity_before:
            print(f"{after.name} stopped playing {playing_activity_before}")
"""

# Run the bot with your token
bot.run('YOUR_TOKEN')
