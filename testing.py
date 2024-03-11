import discord
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot sudah siap')

    # Mengirim pesan setiap jam sekali dengan delay 2 detik dengan 2 kata berbeda
    async def send_hourly_message():
        while True:
            await asyncio.sleep(3600)  # Delay 2 detik
            channel_ids = []  # Ganti dengan daftar ID saluran yang diinginkan
            for channel_id in channel_ids:
                channel = client.get_channel(channel_id)
                await channel.send('.hourly')
                await asyncio.sleep(2)  # Delay 2 detik
                await channel.send('.bt all')

    # Mengirim pesan setiap 24 jam sekali dengan delay 2 detik dengan 2 kata berbeda
    async def send_daily_message():
        while True:
            await asyncio.sleep(86400)  # Delay 24 jam (86400 detik)
            channel_ids = []  # Ganti dengan daftar ID saluran yang diinginkan
            for channel_id in channel_ids:
                channel = client.get_channel(channel_id)
                await channel.send('tdaily')
                await asyncio.sleep(2)  # Delay 2 detik
                await channel.send('owodaily')

    # Menjalankan tugas latar belakang
    client.loop.create_task(send_hourly_message())
    client.loop.create_task(send_daily_message())

# Ganti TOKEN_BOT dengan token bot Anda
client.run('')
