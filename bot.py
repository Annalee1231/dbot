import asyncio
import discord

app = discord.Client()

token = "your_token"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(game=discord.Game(name="안녕하세요 :)", type=1))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!인증":
        await app.send_message(message.channel,"https://discord.com/channels/831033031648739368/886107201712820275/886107863574011924")

app.run('ODg2NTIyMDI5OTc1Njc0OTIx.YT2z-g.VdGlYZqOgDXxDyVUQh7FGXENedY')
