import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    respuesta = update.message.reply_text('Hola, Geeks!')
    return respuesta

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    respuesta = update.message.reply_text('Ayudame!')
    return respuesta

def mayus(update, context):
    respuesta = ''
    
    for i in range(0, len(context.args), 1):
        palabra = list(context.args[i])
        for j in range(0, len(palabra), 1):
            if 96 < ord(palabra[j]) < 123:
                respuesta += chr(ord(palabra[j]) - 32)
            else:
                respuesta += palabra[j]
        if len(context.args) > 1:
            respuesta += ' '
    respuesta = update.message.reply_text(respuesta)
    return respuesta

def alreves(update, context):
    """Repite el mensaje del usuario."""
    respuesta = ''

    for i in range(len(update.message.text), 0, -1):
        respuesta += update.message.text[i - 1]
    respuesta = update.message.reply_text(respuesta)
    return respuesta

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater(token = open('./bot_token').read(), use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('mayus', mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    dp.add_handler(CommandHandler('alreves', alreves))
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()