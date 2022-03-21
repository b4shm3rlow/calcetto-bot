#!/usr/bin/env python

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          CallbackContext, CallbackQueryHandler, ConversationHandler, Filters)
from typing import Dict, Any
import logging
import os

#active logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


BOT_TOKEN_API = '5087762589:AAGGGQrKAn0IxVnnp2p1IOb0d-OcaZbQwoc'
PORT = int(os.environ.get('PORT', 5555))
#costant
SCHEDULE, SELF, GUEST = range(3)

def help_command(update, context):
    """Send a message with the utility command. Usage: /help"""
    update.message.reply_text("Calcetto Bot:\norganizza facilmente una partita tra amici con programmazione e partecipanti!\n\n"
                              "Comandi:\n"
                              "/help : ritorna i comandi utili\n"
                              "/newmatch : crea una nuova partita\n"
                              "/info <descrizione>: modifica il programma della partita\n"
                              "/presente : aggiungi te stesso per la partita\n"
                              "/guest <nome> : per aggiungere un partecipante non presente in questo gruppo\n"
                              "/remove <nome> : per rimuovere un partecipante dalla partita\n"
                              "/recap : mostra le info e partecipanti della partita\n"
                              "/presenti : lista delle persone segnati presente\n"
                              "/endmatch : per chiudere la partita\n")

def newMatch_command(update: Update, context: CallbackContext) -> str:
    """adding a new match with description"""
    if context.chat_data:
        update.message.reply_text(f'Partita già inziata')
    elif not context.args:
        context.chat_data[SCHEDULE] = "<Informazioni partita non aggiornate>"
        update.message.reply_text('⚽ Nuova partita in programma...')
    '''else:
        description = " ".join(context.args)
        update.message.text = description
        context.chat_data[SCHEDULE] = description
        update.message.reply_text(f'⚽ Nuova partita in programma...\n✏ Info della partita aggiornate da {update.message.from_user.name}.')
    '''
def editInfo_command(update: Update, context: CallbackContext) -> str:
    """adding a new match with description"""
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    if not context.args:
        update.message.reply_text('Errore! nessuna descrizione inserita.')
    else:
        description = " ".join(context.args)
        update.message.text = description
        context.chat_data[SCHEDULE] = description
        update.message.reply_text(f'⚽ Info della partita aggiornate da {update.message.from_user.name}.')

def addSelf_command(update, context) -> str:
    """command for adding self to the match. Usage: /presente"""
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata...')

    firstname = update.message.from_user.first_name
    name = update.message.from_user.name
    if name in context.chat_data.keys():
        update.message.reply_text(f'{firstname} ti sei già segnato!')
    else:
        context.chat_data[name] = SELF
        update.message.reply_text(f'{name} presente per la partita 💪')
    

def addGuest_command(update, context) -> str:
    """command for adding guest player. Usage: /guest <argument>"""
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    input = " ".join(context.args)
    if not context.args:
        update.message.reply_text('Errore! nessun nome inserito.')
    elif input in context.chat_data.keys():
        update.message.reply_text(f'{input} è già presente per la convocazione.')
    else:
        context.chat_data[input] = GUEST
        update.message.reply_text(f'{input} è stato aggiunto alla convocazione da {update.message.from_user.name}.')

def removePlayer_command(update, context) -> str:
    """command for removing guest player. Usage: /remove <argument>"""
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    input = " ".join(context.args)
    if not context.args:
        update.message.reply_text('Errore! nessun nome inserito.')
    elif input in context.chat_data.keys():
        context.chat_data.pop(input)
        update.message.reply_text(f'{input} è stato rimosso dalla convocazione per la partita.')
    elif input not in context.chat_data:
        update.message.reply_text(f'Errore! {input} non è stato aggiunto alla convocazione: impossibile rimuoverlo.')

def list_players(chat_data: Dict[str, Any]) -> str:
    """util function for print players registered for the match"""
    keys = list(chat_data.keys())
    text = ''
    if not keys[1:]:
        return 'Nessun giocatore ancora presente.'
    count = 1 #count the total of players
    for player in keys[1:]: #skip the first values because it's the schedule
        text += f'{count}) {player}\n'
        count += 1
    return text

def recap_command(update, context) -> str:
    """print recap match schedule and entry player"""       
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    match_data = context.chat_data
    schedule = match_data.get(SCHEDULE, '<Programma partita non aggiornato>')
    players = list_players(match_data)
    text = f'🗒Programma Partita:\n\n{schedule}\n\n✅Convocati:\n\n{players}'
    update.message.reply_text(text)

def registered_command(update, context) -> str:
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    match_data = context.chat_data
    players = list_players(match_data)
    text = f'Al momento siamo:\n\n{players}'
    update.message.reply_text(text)

def info_command(update, context) -> str:
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    match_data = context.chat_data
    schedule = match_data.get(SCHEDULE, '<Programma partita non aggiornato>')
    text = f'Programma Partita:\n\n{schedule}'
    update.message.reply_text(text)
    
def endMatch_command(update: Update, context: CallbackContext) -> str:
    """closing a match and clear data"""
    if not context.chat_data:
        return update.message.reply_text('Errore! nessuna partita iniziata')
    
    context.chat_data.clear()
    update.message.reply_text('Cancellazione informazioni partita . . .\n. . .\nPartita chiusa ⛔')

"""Unknown commands"""
def unknown_command(update, context) -> str:
    update.message.reply_text('Scusa, non ho capito il comando...🤌')

#main function
def main() -> None:
    """Start the bot"""
    logging.info("Bot server started...")
    #Create the Updater instance and pass the TOKEN API
    updater = Updater(BOT_TOKEN_API)
    logging.info("Token is OK...")
    #get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    #for different commands, add handler
    dispatcher.add_handler(CommandHandler('help',help_command))
    dispatcher.add_handler(CommandHandler('start', newMatch_command))
    dispatcher.add_handler(CommandHandler('info', editInfo_command))
    dispatcher.add_handler(CommandHandler('close', endMatch_command))
    dispatcher.add_handler(CommandHandler('presente', addSelf_command))
    dispatcher.add_handler(CommandHandler('guest', addGuest_command))
    dispatcher.add_handler(CommandHandler('remove', removePlayer_command))
    dispatcher.add_handler(CommandHandler('recap', recap_command))
    dispatcher.add_handler(CommandHandler('presenti', registered_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))
    
    logging.info("Successfully initialized handlers")
    #start the bot locally
    #updater.start_polling()
    #for deployment
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path= BOT_TOKEN_API)
    updater.bot.setWebhook('https://calcetto-bot.herokuapp.com/' + BOT_TOKEN_API)
    #start_polling is non-blocking and will stop the bot gracefully
    updater.idle()

if __name__ == '__main__':
    main()
