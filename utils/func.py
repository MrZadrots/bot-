
def check_status(string):
    if string == '0':
        return 'В рассмотрении'
    if string == '-1':
        return 'Заявка отменена'
    if string == '1':
        return 'Проблема решена'


def create_array_for_print(string):
    result = []
    flag = True
    string = string.replace(" '",'')
    string = string.replace("'",'')
    chat_id,sep,tmp = string.partition(',')
    photo,sep,tmp2 = tmp.partition(',')
    desc,sep,status = tmp2.partition(',')
    status = status.replace(' ','')
    status = check_status(status)

    result.append(chat_id)
    result.append(photo)
    result.append(desc)
    result.append(status)
    return result

if __name__ == '__main__':
    res = create_array_for_print("954825282, 'AgACAgIAAxkBAAIBmWGow3LCe0twlTlWM3pIG3xYe_ncAAIVujEbmGFJSdlnjgQiYU0jAQADAgADcwADIgQ', 'adada', 0")
    print(res)