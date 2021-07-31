import discord
import os
from helper import CheggHelper


token = os.environ['Token']

bot = discord.Client()
obj = CheggHelper()

@bot.event
async def on_ready():
  print(f'Bot is active as {bot.user}')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  if message.content.startswith('?chegg '):
    await message.channel.send('Chegg link received!!')
    try:
        ques_link = message.content.split(' ')[1]
        #print(ques_link)
				#pdf.from_url(ques_link, 'out.pdf')
        stat, filex, captionx = obj.getQAns(ques_link)
        if stat == True:
            bot.send(file=discord.File(open(filex, 'rb')))
            os.remove(filex)
        else:
            await message.channel.send(captionx)
    except Exception as e:
        await message.channel.send(str(e))
  else:
    await message.channel.send('Not a chegg link!!')

bot.run(token)