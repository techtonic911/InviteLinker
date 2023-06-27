import discord

intents = discord.Intents(guilds=True)
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready.")
    for guild in bot.guilds:
        if guild.system_channel:
            invite = await guild.system_channel.create_invite()
            invite_link = f"https://discord.gg/{invite.code}"
            print(f"Invite link for {guild.name}: {invite_link}")
        else:
            print(f"No system channel found for {guild.name}.")

bot.run('YOUR BOT TOKEN')
