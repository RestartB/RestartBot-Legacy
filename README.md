# RestartBot Legacy
Legacy version of RestartBot by RestartBot.

## Notice
> [!IMPORTANT]
> This version of RestartBot is now considered legacy and deprecated. The modern version can now be found at:\
https://github.com/restartb/restartbot

## Commands
Coming soon!

## Required Steps

### Setup
1. Clone this GitHub repo.
2. Inside the RestartBot folder, make a folder called "tokens".
5. Run main.py after you have aquired your tokens and installed required packages.

### Discord Bot Token
A Discord bot token is required to use this bot.
1. Go to Discord Developer Portal.
2. Make a new application.
3. Under the Bot menu, make a new bot and copy the token.
4. Inside the tokens folder, create a new `.txt` file called `discord_token.txt`.
5. Generate a Discord Bot token, and place it in the text file with no other contents. (do not share your bot token with anyone!)

### Spotify Token
To use Spotify related commands, a Spotify API Client ID and Secret are required. If no key is provided, Spotify commands will be disabled.
1. Go to Spotify Developers.
2. Create a new application. Set the name and description to whatever you want, and set the fallback URI to a URL of your selection. `example.com` will work fine.
3. A client ID and Secret will be displayed. Note these down. (do not share your secret with anyone!)
4. Inside the tokens folder, create a new `.txt` file called `spotify_id.txt`, and another .txt file called `spotify_secret.txt`.
5. Place the respective item into each file with no other content.

## Required Packages

### Package List
- `discord.py` - Discord functionality
- `wikipedia` - Wikipedia command
- `psutil` - Host Info command
- `py-cpuinfo` - Host Info command
- `spotipy` - Spotify commands

### Pip Install Command
To install all required packages using Pip, you can run the following command to retrieve the packages from PyPi:\
`pip install discord.py wikipedia psutil py-cpuinfo spotipy`

## Adding a New Command
Please read examples.py to find code snippets that you can use as a reference to make your own command.\
\
It is also recommended to read the discord.py documentation and do your own reference to find out what is possible with Discord Slash Commands.
