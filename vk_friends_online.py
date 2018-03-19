import vk
import getpass

APP_ID = 6391427


def get_user_login():
    return input('Введите логин: ')


def get_user_password():
    return getpass.getpass('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api_connection_context = vk.API(session)
    online_friends_id_list = api_connection_context.friends.getOnline(
        v=5.52
    )
    online_friends_list = api_connection_context.users.get(
        user_ids=online_friends_id_list, v=5.52
    )
    return online_friends_list


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online_list = get_online_friends(login, password)
        output_friends_to_console(friends_online_list)
    except ValueError:
        print("Указаны неверные логин/пароль.")
