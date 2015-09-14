#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Simple Bot to reply Telegram messages
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].


import logging
import telegram
import time
import random
import settings


LAST_UPDATE_ID = None


def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot(settings.TOKEN)

    message = 'Ya regreseee putitos!'
    chat_id = -29051226
    bot.sendMessage(chat_id=chat_id,text=message)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)


def echo(bot):
    global LAST_UPDATE_ID

    # Request updates from last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID):
        if LAST_UPDATE_ID < update.update_id:
            # chat_id is required to reply any message
            chat_id = update.message.chat_id
            sender = update.message.from_user #['from']['first_name']
            # message = update.message.text.encode('utf-8')


            messages = (
                '%s Olachiot!',
                '%s, Ahorita no joven',
                '%s, Andate por ahi, despojo!',
                '%s, eres una pobre persona falta de amor...',
                '%s, puedes irte muy lejos, alla por donde da la vuelta el viento',
                'A ti te dejaron caer de bebe, verdad %s?',
                'A veces dices cosas chidas, a veces la cagas, %s',
                'Alguien aplaudale a %s, por favor',
                'Buena esa %s, deja la anoto en mi maquina de escribir invisible',
                'Caguamase jijuelabolsa?, te hablo a ti %s',
                'Chupa mi trasero de metal, %s',
                'Come caca, %s',
                'Como castras, %s',
                'Deja de estar mamando, %s',
                'Deja de joder, %s',
                'Mejor hazte una chaquetota, %s',
                'Mejor invita las cheves, %s',
                'Mejor vamos a la quebradita, %s',
                'Neta, ya no mames %s',
                'Por que no eres un ser humano normal, %s?',
                'Puta madre, deja de joder %s',
                'Que chingados quieres, %s?',
                'Que crees que tengo tiempo para tus pendejadas, %s?',
                'Sacate por ahi, %s',
                'Si tuviera un dolar por cada vez que dices una pendejada asi...%s',
                'Te la papeas toda, %s',
                'Tienes la cara como una bola de pozol con un madrazo, %s'
                'Tu madre no se sentiria muy orgullosa de escuchar esto, %s',
                'Tu que sabes de la vida, si nunca te ha besado un policia, %s?',
                'Tu te escapaste del festival del queso, verdad %s?',
                'Un tekilita, %s?',
                'Vamos por unas frias, %s',
                'Ya ponte a programar, %s',

            )

            if sender.id == 13872946: # Eder Negro
                message = "Sacate por ahi Eder, deja de andar cagando el palo!"
            elif sender.id == 15969040: # El Xino
                message = "A sus ordenes, jefecito"
            elif sender.id == 66747007: # Daniel
                message = random.choice(
                    (
                        'Tienes pinta de mayate, Daniel',
                        'Ya estoy hasta el tushul de tus mamadas, Daniel',
                        'Buen intento maquinola pero acabo de denunciarte.',
                        'Mira como te denuncio papu!',

                    )
                )
            else:
                message = random.choice(messages) % sender.first_name

            print('sender: ' + sender.first_name)
            print('sender id: ' + str(sender.id))
            print('chat ID: ' + str(chat_id))
            print('incomming message: ' + update.message.text)
            print('outcoming message: ' + message)
            print('-'*80)

            if (message):
                # Reply the message
                bot.sendMessage(chat_id=chat_id,
                                text=message)

                # Updates global offset to get the new updates
                LAST_UPDATE_ID = update.update_id


if __name__ == '__main__':
    main()
