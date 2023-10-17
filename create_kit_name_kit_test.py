import sender_stand_request
import data

def get_kit_body(kit_body):
    current_body = data.kit_body.copy()
    current_body['name'] = kit_body
    return current_body

def positive_assert(name):
    new_kit_body = get_kit_body(name)
    kit_user_response = sender_stand_request.post_new_user_kits(new_kit_body)
    assert kit_user_response.status_code == 201
    assert kit_user_response.json()['name'] == name

def negative_assert(name):
    new_kit_body = get_kit_body(name)
    kit_user_response = sender_stand_request.post_new_user_kits(new_kit_body)
    assert kit_user_response.status_code == 400

def negative_assert_no_kit_name(kit_body):
    kit_user_response = sender_stand_request.post_new_user_kits(kit_body)
    assert kit_user_response.status_code == 400

#Тест 1.
#Допустимое количество символов (1)
def test_1_letter_name_kit():
    positive_assert('a')

#Тест 2.
#Допустимое количество символов (511)
def test_511_letters_name_kit():
    positive_assert('Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

#Тест 3. Ошибка.
#Количество символов меньше допустимого (0)
def test_empty_name_kit():
    negative_assert('')

#Тест 4. Ошибка.
#Количество символов больше допустимого (512)
def test_512_letters_name_kit():
    positive_assert('Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

#Тест 5.
#Разрешены английские буквы
def test_english_letters_name_kit():
    positive_assert('QWErty')

#Тест 6.
#Разрешены русские буквы
def test_russian_letters_name_kit():
    positive_assert('Мария')

#Тест 7.
#Разрешены спецсимволы
def test_symbols_kit_name():
    positive_assert('"№%@",')

#Тест 8.
#Разрешены пробелы
def test_spaces_kit_name():
    positive_assert(' Человек и КО ')

#Тест 9.
#Разрешены цифры
def test_numbers_kit_name():
    positive_assert('123')

#Тест 10. Ошибка.
#Параметр не передан в запросе
def test_name_not_found_kit_name():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_kit_name(kit_body)

#Тест 11. Ошибка.
#Передан другой тип параметра (число)
def test_wrong_parameter_number_kit_body():
    negative_assert(123)