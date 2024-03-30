# Examples
# Use these examples as a reference for commands to add to RestartBot. You can modify these for your own use, or use them as a reference to make your own.
# It is heavily advised to read the discord.py documentation and do your own research on what you can do with slash commands.

# Warning!
# These code snippets are designed to be pasted into RestartBot code and are not meant to be ran on their own!

# Basic Hello World command
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer() # Tells Discord to wait for an interaction.
    await interaction.followup.send("Hello World!") # Send "Hello World" as a reply to the original user.

# Basic Embed Example.
@tree.command(name = "command-name", description = "Description of your command.")
@app_commands.checks.cooldown(1, 5) # Adds a cooldown to your command. Edit the second number to change the time in seconds, or delete the line to remove the cooldown.
async def self(interaction: discord.Interaction):
    await interaction.response.defer() # Tells Discord to wait for an interaction.
    embed = discord.Embed(name = "Embed Title", description = "Description of your Embed.") # Define an Embed, store it in the Embed variable.
    embed.add_field(name = "Field Name", value = "Field info.", inline = False) # Add a Field to your Embed. Change inline to True, to allow the Field to be displayed next to other fields. Up to 12 fields per Embed are allowed.