# <---------> - = - = - <--------->
import discord
import asyncio
# <---------> - = - = - <--------->
client = discord.Client()
# <---------> - = - = - <--------->
email = "EMAIL"
pw = "PW"

# <---------> - = - = - <--------->
@client.event
async def on_ready():
    print("Self Join ON")
    print("Servers: {}".format(str(len(client.servers))))
    print("OK!")


@client.event
async def on_member_join(member):
  msg = "Message {} Message \n Message**".format(member.mention)
  await client.send_message(member, msg) 


client.run(email, senha)
