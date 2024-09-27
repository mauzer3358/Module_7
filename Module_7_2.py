import io
from pprint import pprint


def custom_write(file_name, strings):
    list_numstrings = []
    list_text = []
    count_num = 1

    file = open(file_name, 'a', encoding='utf-8')
    list_byte = []
    file.seek(0)
    for i in strings:
        list_numstrings.append(count_num)
        list_text.append(i)
        list_byte.append(file.tell())
        file.write(f'{i}\n')
        count_num += 1
    file.close()

    my_index = tuple(zip(list_numstrings,list_byte))
    result = dict(zip((my_index),list_text))
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)