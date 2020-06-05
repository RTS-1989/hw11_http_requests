import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(input_file, output_file, from_lang, to_lang='ru'):

    with open(input_file, encoding='utf8') as file_to_translate:
        with open(output_file, 'w', encoding='utf8') as res_translate:
            params = {
                'key': API_KEY,
                'text': file_to_translate.read(),
                'lang': f'{from_lang}-{to_lang}'.format(to_lang),
            }
            response = requests.get(URL, params=params)
            json_ = response.json()
            res_translate.write(''.join(json_['text']))
    return output_file

if __name__ == '__main__':
    translate_it('DE.txt', 'translate.txt', 'de', 'ru')
