from pyrogram import Client, filters
import logging
import config
import os
import traceback
#import API_ID, API_HASH, BOT_TOKEN 
from pyrogram.handlers import MessageHandler
const express = require('express')
const app = express()
const port = process.env.PORT || 4000;
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
#from pyrogram.errors import BadRequest, Forbidden, ...

#api_id = 3335796
#api_hash = "138b992a0e672e8346d8439c3f42ea78"
#bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0"


#app = Client("uploader",api_id=api_id, api_hash=api_hash, bot_token=bot_token )


#@app.on_message(filters.text & filters.private)
#async def echo(client, message):
  #  await message.reply(message.text)
    

bot = Client(
"test",
api_id = 3335796,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0",
BUN_VERSION = "1.1.0"  
)

@bot.on.message(filters.command('start') & filters.private )
def command(bot, message):
bot.send.message(message.chat.id, "Hello Baby")

print ("i am online")


#logging.basicConfig(
#format = '%(asctime)s – %(name)s – %(levelname)s – %(message)s', 
#level = logging.INFO
#)
#LOGGER = logging.getLoggor(__name__)


app.run()
