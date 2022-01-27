
from aiogram.types.message import Message
import asyncio
from aiogram import Bot


def check_status(string):
    if string == ' 0':
        return 'В рассмотрении'
    if string == ' -1':
        return 'Заявка отменена'
    if string == ' 1':
        return 'Проблема решена'


def create_array_for_print(string):
    result = []
    flag = True
    string = string.replace(" '",'')
    string = string.replace("'",'')
    
    chat_id,sep,tmp = string.partition(',')
    photo,sep,tmp2 = tmp.partition(',')
    desc,sep,tmp3 = tmp2.partition(',')
    status,sep,tmp4 = tmp3.partition(',')
    
    status = check_status(status)

    result.append(chat_id)
    result.append(photo)
    result.append(desc)
    result.append(status)
    result.append(tmp4)
    return result


def find_flor(name):
    if name == '1 корпус':
        result = 'first_flor'
    if name == '2 корпус':
        result = 'second_flor'
    if name == '3 корпус':
        result = 'third _flor'
    
    return result

async def getPhotoFromTg(message: Message,bot:Bot):
    file_info = await bot.get_file(message.photo[0].file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    src = '../src' + message.photo[1].file_id
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)


if __name__ == '__main__':
    res = create_array_for_print("954825282, 'AgACAgIAAxkBAAIGCmHyc9DyZmk6MLcnEqrpDoBRNS0oAALrtDEbcyeZS-e15kL-e15kLEQUKcAQADAgADcwADIwQ', 'возле 510', 0, '1 корпус5 этаж'")
    print(res)