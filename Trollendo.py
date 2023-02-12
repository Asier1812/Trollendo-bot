import discord
import base64
import datetime
import random
import os
import json
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
        self.comamnd_list = {}
        with open("commandlist.txt", "r") as f:
            self.command_list = json.load(f)
        intents = discord.Intents.default()
        intents.message_content = True
        discord.Client.__init__(self, intents=intents)
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        
    async def on_message(self, message):
            
        if (message.content.startswith("-")):
            text_channel = message.channel
            processed_message = message.content.replace("-", "").replace("?","").replace("¿","").split(" ")
            command = processed_message[0]
            print(processed_message)
            if command in self.command_list:
                if self.command_list[command]["type"] == "simpleaudio":
                    if (message.author.voice is None or message.author.voice.channel is None):
                        await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                        return
                    voice_channel = message.author.voice.channel
                    vc = message.author.guild.voice_client
                    if (not vc):
                        vc = await voice_channel.connect()                        
                    if(vc.is_playing()):
                        vc.stop()
                        
                    self.stateid += 1
                    ownid = self.stateid
                    
                    file = "audio/" + command + ".mp3"
                    vc.play(discord.FFmpegPCMAudio(file))
                    while vc.is_playing():
                        await sleep(1)
                    if (ownid == self.stateid):
                        await vc.disconnect()
                        
                elif self.command_list[command]["type"] == "randomaudio":         
                    if (message.author.voice is None or message.author.voice.channel is None):
                        await text_channel.send(message.author.mention + ", únete a un canal primero, melón.")
                        return
                    voice_channel = message.author.voice.channel
                    vc = message.author.guild.voice_client
                    if (not vc):    
                        vc = await voice_channel.connect()
                    if(vc.is_playing()):
                        vc.stop()
                    
                    self.stateid += 1
                    ownid = self.stateid

                    
                    i = random.randint(1, len(os.listdir("audio/" + command)))
                    file = "audio/" + command + "/" + command + str(i) + ".mp3"
                    vc.play(discord.FFmpegPCMAudio(file))
                    while vc.is_playing():
                        await sleep(1)
                    if (ownid == self.stateid):
                        await vc.disconnect()
                        
                elif self.command_list[command]["type"] == "claseaudio":
                    if (message.author.voice is None or message.author.voice.channel is None):
                        await text_channel.send(message.author.mention + ", como vas a saber si hay clase sin meterte a un canal, melón.")
                        return
                    voice_channel = message.author.voice.channel
                    vc = message.author.guild.voice_client
                    if (not vc):
                        vc = await voice_channel.connect()
                    if(vc.is_playing()):
                        vc.stop()

                    dia = datetime.datetime.now().weekday()
                    if (len(processed_message) > 1):
                        arg = processed_message[1].lower().replace("á","a").replace("é","e")
                        if (arg in  "lunes martes miercoles jueves viernes sabado domingo".split()):
                            dia = ("lunes martes miercoles jueves viernes sabado domingo".split()).index(arg)
                        elif arg.isdigit():
                            dia = datetime.datetime.now().weekday() + int(arg) - 1
                    

                    file = "audio/nohay.mp3"    
                    if (dia % 7 < 5):
                        file = "audio/hay.mp3"
                    
                    self.stateid += 1
                    ownid = self.stateid
                    
                    vc.play(discord.FFmpegPCMAudio(file))
                    await sleep(11.35)
                    if (ownid == self.stateid):
                        await vc.disconnect()
                        
                elif self.command_list[command]["type"] == "howtext":
                    num, dd, sd = comoestas()
                    strdiff = timedifftostr(dd, sd)
                    frases = ["Bastante bien joven. ", "Pues aqui estamos. ", "No muy bien amigo. ","El peor día de mi vida. " ,"Aburrido la verdad. Dale algun comandillo. "]
                    frasesshiny = ["Mi exmujer se ha quedado la custodia, me voy a sucidar. "]

                    frase = ""
                    i = random.randint(0, 100)
                    if (i == 0):
                        frase = frasesshiny[0]
                    else:
                        frase = frases[i%len(frases)]
                    await text_channel.send(frase + "Hasta ahora me lo han preguntado " + str(num) + " veces. " + strdiff)
                    
                elif self.command_list[command]["type"] == "helptext":
                    texto = "**Listado de comandos:**\n"
                    texto +=  "\nComandos de audio:\n"
                    texto +=  "clase <nada|días|día de la semana>  :  Indica si hay clase mañana (<nada>), en <días> días o el <día de la semana>\n"
                    texto +=  "celebrate  :  Hay que celebrar diferencias chicos\n"
                    texto +=  "cum  :  Audio aleatorio de cybercum2077\n"
                    texto +=  "cumlight  :  Moonlight pero con cum\n"
                    texto +=  "moonlight  :  Lucía cantando moonlight xd\n"
                    texto +=  "42  :  Carla haciendo buffer overflow auditivo\n"
                    texto +=  "desterrado  :  Para gente en desacuerdo político\n"
                    texto +=  "bossmusic  :  Música épica\n"
                    texto +=  "hola  :  No saludar es de maleducados\n"
                    texto +=  "adios  :  No despedirse es de maleducados\n"
                    texto +=  "marta  :  Self explanatory\n"
                    texto +=  "\nComandos de texto:\n"
                    texto +=  "how|how are you  :  El bot te cuenta como está (no funciona bien)\n"
                    texto +=  "help  :  Este mensaje con lista de comandos\n"
                    texto +=  "\nReacciones:\n"
                    texto +=  "tactico|tactica|tactique  :  El bot te contesta si mencionas algo tactico\n"
                    
                    await text_channel.send(texto)
                else:
                    print("jej")
            else:
                print("jej2")
        else:
            #Check reactions
            for r in ["tactico", "táctico", "tactica", "táctica", "tactique", "táctique"]:
                if (r in message.content.lower()):
                    if (message.author.name != "TrollendoBot"):
                        text_channel = message.channel
                        frases = [["Joer ",", es que encima es "], ["Madre mía ",",encima "],["Joer ",", que "],["Joer, madre mía, encima "]]
                                    
                        i = random.randint(0,3)
                        if (i == 3):
                            await text_channel.send(frases[i][0] + r)
                        else:
                            await text_channel.send(frases[i][0] + message.author.mention + frases[i][1] + r)
           
            print(message.author.name + " : " + message.content)


client = MyClient()
token = ""
with open("Secret.txt") as f:
    token = f.read()
client.run(token)
