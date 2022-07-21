from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from config import open_weather_token

import requests
import datetime


async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!\n'
                                                     '/Интересный_факт - команда для получения интересного факта\n'
                                                     '/Погода (название города) - команда для получения прогноза погоды в заданном городе\n'
                                                     '/Помощь - команда для обратной связи', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему, он не пожет вам написать первым! @geometrywork_bot')


# @dp.message_handler(commands=['Интересный_факт'])
async def interesting_fact(message : types.Message):
    await bot.send_message(message.from_user.id, 'В 1889 году королева Италии Маргарита Савойская заказала первую доставку пиццы')


# @dp.message_handler(commands=['Помощь'])
async def helper(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://t.me/liftersan')

async def get_wether(message:types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь\U00002614",
        "Drizzle": "Дождь\U00002614",
        "Thunderstorm": "Гроза\U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F328"
    }

    text = message.text[8:]
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "На улице все плохо, мы все умрем"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Прогноз погоды: {city}\nТемпература: {cur_weather}C` {wd}\n"
              f"Влажность: {humidity}%\nДавление:{pressure} мм.рт.ст.\nВетер: {wind}м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"***Удачи!***\n"
              "\n"
              "Test project"
              )
    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(interesting_fact, commands=['Интересный_факт'])
    dp.register_message_handler(helper, commands=['Помощь'])
    dp.register_message_handler(get_wether, commands=['Погода'])