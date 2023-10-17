import data
import requests
import configuration

#создаем нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


#Получаем динамический токен пользователя
def get_new_user_token():
    response_new_user = post_new_user(data.user_body)
    auth_token = data.headers.copy()
    auth_token['Authorization'] = "Bearer " + response_new_user.json()["authToken"] #Записываем токен в переменную
    return auth_token


#Создаем личный набор
def post_new_user_kits(kit_body):
    return requests.post(configuration.URL + configuration.CREATE_KITS_PATH,
                        json=kit_body,
                        headers=get_new_user_token()) #Получаем каждый раз новый токен




