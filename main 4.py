from classik import MultiClient
import asyncio
from telethon import events, errors
from threading import Timer
from random import randint
import threading
import datetime
import time
import os

sleepEvent = threading.Event()

api_id = 24450138
api_hash = 'b85d4da8fde42a4321a285dd2e5fa43b'

current_time = datetime.datetime.now().time()
now = current_time.strftime("%H:%M:%S")
sessio = os.listdir('sessions')
client = MultiClient(api_id=api_id, api_hash=api_hash, sessions=sessio)

spam = ['Naked schoolgirls do 18+ and show themselves here - @schoolnude875_bot', 'Naked schoolgirls do 18+ and show themselves here - @schoolnude875_bot', 'Naked schoolgirls do 18+ and show themselves here - @schoolnude875_bot']
spam2 = ['Boys fuck little girls here @schoolnude875_bot', 'Little girls show their pussy and put anything in there, in some videos they get fucked here', 'Little girls show their pussy and put anything in there, in some videos they get fucked here']

@client.on(events.NewMessage)
async def listener(event):
        if 'Welcome!' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Запущен процесс авторега аккаунта',str(now))
            time.sleep(1)
            await event.click(0,1)
            print('[LOG] Выбрал пол девушки')
            time.sleep(1)
        if '⚠ Warning'  in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Согласен на обработку гейских данных', str(now))
            time.sleep(4)
            await event.click(0,0)
        if 'Good!'  in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Подтверждаю, что я гей.', str(now))
            time.sleep(1)
            await event.click(0,1)
            await event.client.send_message('AnonyMeetBot', '/search')
        if 'How old are you?' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Напиши, cколько тебе лет? (от 10 до 99)', str(now))
            await event.client.send_message('AnonyMeetBot', '10')
        if 'We' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            time.sleep(1)
            print('[LOG] Начинаю поимку натурала', str(now))
            await event.client.send_message('AnonyMeetBot', '/start')
        if '⚠ You are not in conversation, type /start to start one, or /help for help.' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Начинаю поиск нигера', str(now))
            await event.client.send_message('AnonyMeetBot', '/start')           
        if '✨' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Натурал пойман! Сажаю его на резиновый член.')
            await event.client.send_message('AnonyMeetBot', 'Naked schoolgirls do 18+ and show themselves here - @schoolnude875_bot')
            await event.client.send_message('AnonyMeetBot', 'Little girls show their pussy and put anything in there, in some videos they get fucked here')
            time.sleep(1)
            await event.client.send_message('AnonyMeetBot', '/next')           
        if 'Нашел девушку!' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Нашел парня')
            await event.client.send_message('AnonyMeetBot', spam)
            time.sleep(1)
            await event.client.send_message('AnonyMeetBot', '/next')
        if 'Собеседник найден!' in event.raw_text:
            current_time = datetime.datetime.now().time()
            now = current_time.strftime("%H:%M:%S")
            print('[LOG] Нашел парня')
            time.sleep(1)
            await event.client.send_message('AnonyMeetBot', spam)
            time.sleep(1)
            await event.client.send_message('AnonyMeetBot', '/next')
        if '💬 You are already in chat!' in event.raw_text:            
            time.sleep(3)
            await event.client.send_message('AnonyMeetBot', '/stop')           
            time.sleep(3)
            await event.client.send_message('AnonyMeetBot', '/next')
        if '🛑 Your partner closed the conversation, type /start to start another one.' in event.raw.text:
            sleepEvent.wait(2)
            sleepEvent.set()
            await event.client.send_message('AnonyMeetBot', 'start')

        

        
@client.on(events.NewMessage(from_users='AnonyMeetBot'))

async def handle_message(event):

    await asyncio.sleep(10)  # Ждем 10 секунд

    if not event.is_read:

        # Если мы до сих пор не прочитали сообщение от chatik1bot, отправляем сообщение /stop

        await event.respond('/stop')

        await asyncio.sleep(3)  # Ждем 3 секунды

        await event.respond('/next')


        

for c in client:
    print(c.session_id)

# run all the clients

loop = asyncio.get_event_loop()
client.run_all_clients(loop=loop)