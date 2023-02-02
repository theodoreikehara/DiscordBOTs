# testing python bot for discord

import os
import time
import discord as ds


token = 'PLACE TOKEN HERE'   #bot token for discord
channel_id = 'PLACE CHANNEL ID HERE'
ip_list = ['LIST IP ADD HERE']
timeout = 10

client = ds.Client()

@client.event
async def on_ready():
    pings_channel = client.get_channel(channel_id)

    while True:
        for ip in ip_list:
            response = os.popen(f"ping {ip}").read()
            if not ("Received = 4" in response):                              # host is down do this
                await pings_channel.send(f"DOWN {ip} Ping Unsuccessful, HELP ME!!!")

        time.sleep(timeout)

client.run(token)
