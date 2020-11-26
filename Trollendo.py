import discord
import datetime
from asyncio import sleep


class MyClient(discord.Client):

    def __init__(self):
        self.stateid = 0
        discord.Client.__init__(self)
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if (message.content.startswith("-")):
            text_channel = message.channel
            if (message.author.voice is None or message.author.voice.channel is None):
                await text_channel.send(message.author.mention + ", como vas a saber si hay clase sin meterte a un canal, melón.")
                return
            if (message.content=="-clase"):
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):
                    vc = await voice_channel.connect()
                dia = datetime.datetime.now().weekday() + 1
                file = "nohay.mp3"
                if (dia < 4 or dia == 7):
                    file = "hay.mp3"
                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                await sleep(11.35)
                if (ownid == self.stateid):
                    await vc.disconnect()
            
            elif (message.content.startswith("-clase")):
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):    
                    vc = await voice_channel.connect()
                
                numero = message.content.split()[1]
                if (numero.lower() in "lunes martes miercoles miércoles jueves viernes sabado sábado domingo".split()):
                    dia = ("lunes martes miercoles miércoles jueves viernes sabado sábado domingo".split()).index(numero.lower())
                    if (dia >= 3):
                        dia -= 1
                    if (dia >= 7):
                        dia -= 1
                        
                else:
                    dia = (datetime.datetime.now().weekday() + int(numero)) % 7
                file = "nohay.mp3"
                if (dia < 4 or dia >= 7):
                    file = "hay.mp3"

                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                await sleep(11.5)
                if (ownid == self.stateid):
                    await vc.disconnect()


client = MyClient()
client.run("Nzc0Mzc4MDkzMzY4MTgwNzk3.X6W5zA.Z44fzZg0c_dbOeurUuqlxq3TkKc")
