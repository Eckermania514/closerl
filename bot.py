import discord
import subprocess

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot online. Listening for commands.".format(client))

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check for the specific message
    if message.content == "!run":
        try:
            # Run the batch file
            subprocess.run(["C:/scripts/main.bat"], check=True, shell=True)
            await message.channel.send("Executing. Please allow up to 10 minutes for it to process.")
        except subprocess.CalledProcessError as e:
            await message.channel.send(f"Error executing.")
        except FileNotFoundError:
            await message.channel.send("Error executing.")

# Run the bot with your token
client.run("YOUR_BOT_TOKEN")
