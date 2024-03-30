# Examples
# Use these examples as a reference for commands to add to RestartBot. You can modify these for your own use, or use them as a reference to make your own.
# It is heavily advised to read the discord.py documentation and do your own research on what you can do with slash commands.

# Warning!
# These code snippets are designed to be pasted into RestartBot code and are not meant to be ran on their own!

# Basic Hello World command
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer() # Tells Discord to wait for a response.
    await interaction.followup.send("Hello World!") # Send "Hello World" as a reply to the original user.

# Basic Embed example
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer() # Tells Discord to wait for a response.
    embed = discord.Embed(name = "Embed Title", description = "Description of your Embed.") # Define an Embed, store it in the Embed variable.
    embed.add_field(name = "Field Name", value = "Field info.", inline = False) # Add a Field to your Embed. Change inline to True, to allow the Field to be displayed next to other fields. Up to 25 fields per Embed are allowed.
    await interaction.followup.send(embed = embed) # Send your embed as a reply to the slash command.

# Private (ephemeral) Message example
# Send a reply to a slash command that only the sender can see and dismiss.
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral = True) # Tells Discord to wait for a ephemeral message response.
    await interaction.followup.send("Hello World!", ephemeral = True) # Send "Hello World" as an ephemeral reply to the original user.

# Web Request Example
# Request data from the web and add it to an embed.
# In this example, a cat image will be requested using TheCatAPI.
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral = True) # Tells Discord to wait for a response.

    await interaction.followup.send("Hello World!", ephemeral = True) # Send "Hello World" as a reply to the original user.