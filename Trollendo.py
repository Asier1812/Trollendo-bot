import discord
import datetime
import random
from asyncio import sleep

def comoestas():
    num = 0
    tim = 0
    with open("file.txt") as f:
        line = f.readline()
        num = line.split("==")[0]
        tim = datetime.datetime.strptime(line.split("==")[1], '%Y-%m-%d %H:%M:%S.%f')
        f.close()

    now = datetime.datetime.now()
    nowstr = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    with open("file.txt", "w") as f:
        f.write(str(int(num) + 1) + "==" + str(nowstr))
        f.close()


    daysdiff = abs((now - tim).days)
    secondsdiff = abs((now - tim).seconds)

    return int(num), daysdiff, secondsdiff


def timedifftostr(daysdiff, secondsdiff):

    hours = secondsdiff // 3600
    minutes = (secondsdiff % 3600) // 60
    seconds = secondsdiff % 60

    ret = "Ya han pasado "
    aux = False
    appendix = ""
    if (daysdiff >= 1):
        ret += str(daysdiff) + " días"
        appendix = ", "
        aux = True
    if (hours >= 1):
        ret += appendix + str(hours) + " horas"
        appendix = ", "
        aux = True
    if (minutes >= 1):
        ret += appendix + str(minutes) + " minutos"
        aux = True

    if (aux):
        ret += " y "
    ret += str(seconds) + " segundos desde la última vez."

    return ret

class MyClient(discord.Client):

    def __init__(self):
        self.stateid = 0
        discord.Client.__init__(self)
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        
    async def on_message(self, message):
        if (message.content.startswith("-")):
            text_channel = message.channel
            if (message.content=="-clase"):
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", como vas a saber si hay clase sin meterte a un canal, melón.")
                    return
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
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", como vas a saber si hay clase sin meterte a un canal, melón.")
                    return
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
                    
            elif (message.content.startswith("-celebrate")):
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                    return
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):    
                    vc = await voice_channel.connect()
                           
                file = "celebrate.aac"

                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                await sleep(13)
                if (ownid == self.stateid):
                    await vc.disconnect()
                    
            elif (message.content.startswith("-cumlight")):
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                    return
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):    
                    vc = await voice_channel.connect()

                file = "cumlight.mp3"

                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                while vc.is_playing():
                    await sleep(1)
                if (ownid == self.stateid):
                    await vc.disconnect()
                    
            elif (message.content.startswith("-cum")):
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                    return
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):    
                    vc = await voice_channel.connect()


                i = random.randint(1,6)
                file = "cum"+str(i)+".mp3"

                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                while vc.is_playing():
                    await sleep(1)
                if (ownid == self.stateid):
                    await vc.disconnect()

            
            elif (message.content.startswith("-moonlight")):
                if (message.author.voice is None or message.author.voice.channel is None):
                    await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                    return
                voice_channel = message.author.voice.channel
                vc = message.author.guild.voice_client
                if (not vc):    
                    vc = await voice_channel.connect()

                file = "moonlight.mp3"

                if(vc.is_playing()):
                    vc.stop()
                self.stateid += 1
                ownid = self.stateid
                vc.play(discord.FFmpegPCMAudio(file))
                while vc.is_playing():
                    await sleep(1)
                if (ownid == self.stateid):
                    await vc.disconnect()
            elif (message.content.replace("?","").replace("¿","").startswith("-how") or message.content.replace("?","").replace("¿","").startswith("-how are you") ):
                num, dd, sd = comoestas()
                strdiff = timedifftostr(dd, sd)
                frases = ["Bastante bien joven. ", "Pues aqui estamos. ", "No muy bien amigo. ","El peor día de mi vida. " ,"Aburrido la verdad. Dale algun comandillo. "]
                frasesshiny = ["Mi exmujer se ha quedado la custodia, me voy a sucidar. "]

                frase = ""
                i = random.randint(1, 100)
                if (i == 100):
                    frase = frasesshiny[0]
                else:
                    frase = frases[i%len(frases)]
                await text_channel.send(frase + "Hasta ahora me lo han preguntado " + str(num) + " veces. " + strdiff)
                
            
        elif ("tactico" in message.content.lower() or "táctico" in  message.content.lower()):
            if (message.author.name != "ClaseBot"):
                text_channel = message.channel
                frases = [["Joer ",", es que encima es táctico"], ["Madre mía ",",encima táctico"],["Joer ",", que táctico"],["Joer, madre mía, encima táctico"]]
                
                i = random.randint(0,3)
                if (i == 3):
                    await text_channel.send(frases[i][0])
                else:
                    await text_channel.send(frases[i][0] + message.author.mention + frases[i][1])
        elif ("tactica" in message.content.lower() or "táctica" in  message.content.lower()):
            if (message.author.name != "ClaseBot"):
                text_channel = message.channel
                frases = [["Joer ",", es que encima es táctica"], ["Madre mía ",",encima táctica"],["Joer ",", que táctica"],["Joer, madre mía, encima táctica"]]
                
                i = random.randint(0,3)
                if (i == 3):
                    await text_channel.send(frases[i][0])
                else:
                    await text_channel.send(frases[i][0] + message.author.mention + frases[i][1])
        elif ("tactique" in message.content.lower() or "táctique" in  message.content.lower()):
            if (message.author.name != "ClaseBot"):
                text_channel = message.channel
                frases = [["Joer ",", es que encima es táctique"], ["Madre mía ",",encima táctique"],["Joer ",", que táctique"],["Joer, madre mía, encima táctique"]]
                
                i = random.randint(0,3)
                if (i == 3):
                    await text_channel.send(frases[i][0])
                else:
                    await text_channel.send(frases[i][0] + message.author.mention + frases[i][1])
        else:
            print(message.author.name + " : " + message.content)

client = MyClient()
client.run("Nzc0Mzc4MDkzMzY4MTgwNzk3.X6W5zA.Z44fzZg0c_dbOeurUuqlxq3TkKc")
