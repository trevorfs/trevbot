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
            channel_ids = [1161883711353135214, 1161883899425722368, 1161883867163144223, 1161883932443291721, 1161883972276600922, 1161884002051952650, 1161884035824500747, 1161884072935706634, 1161884110533443704, 1161884144733798565]  # Ganti dengan daftar ID saluran yang diinginkan
            for channel_id in channel_ids:
                channel = client.get_channel(channel_id)
                await channel.send('.hourly')
                await asyncio.sleep(2)  # Delay 2 detik
                await channel.send('.bt all')

    # Mengirim pesan setiap 24 jam sekali dengan delay 2 detik dengan 2 kata berbeda
    async def send_daily_message():
        while True:
            await asyncio.sleep(86400)  # Delay 24 jam (86400 detik)
            channel_ids = [1161883711353135214, 1161883899425722368, 1161883867163144223, 1161883932443291721, 1161883972276600922, 1161884002051952650, 1161884035824500747, 1161884072935706634, 1161884110533443704, 1161884144733798565]  # Ganti dengan daftar ID saluran yang diinginkan
            for channel_id in channel_ids:
                channel = client.get_channel(channel_id)
                await channel.send('tdaily')
                await asyncio.sleep(2)  # Delay 2 detik
                await channel.send('owodaily')

    # Menjalankan tugas latar belakang
    client.loop.create_task(send_hourly_message())
    client.loop.create_task(send_daily_message())

# Ganti TOKEN_BOT dengan token bot Anda
client.run('NDQ4ODYyODgxODI4NTY5MDk5.GjncxD.HOUG-Ib-7miT6MiCcIQ1ltbk8lC6ZadmnB_i4E')
