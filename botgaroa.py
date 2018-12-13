#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  botgaroa.py
#  
#  Copyright 2018 Priscila Gutierres <priscila.gutierres@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from telegram.ext import CommandHandler, Updater
import telegram
#import logging

token = '484672472:AAEdXTHORHH8uJNfUAtl6O4QEZFpjW5QPS8'

		
def start(bot, update):
	"""Send a message when the command /start is issued."""
	bot.send_message(chat_id=update.message.chat_id, text="Hi! What you want to do? Type /help for commands.")
    

def help_(bot, update):
	"""Display all avaiable commands when /help is issued."""
	message = '/start display the welcome message'
	update.message.reply_text(message)
    
def broadcast(bot, update):
	message = 'message'
	bot.send_message(chat_id=update.message.chat_id, text=message)

bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help_)
dispatcher.add_handler(help_handler)

broadcast_handler = CommandHandler('broadcast', broadcast)
dispatcher.add_handler(broadcast_handler)

# Start the bot
updater.start_polling()

updater.idle()
