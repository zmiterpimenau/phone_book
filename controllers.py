from views import render_template
from models import User, Phone

def default_controller(data=None, cls=True):
    render_template(context={}, template='default.jinja2', cls=cls)
    return (input(), None)
    
def exit_controller(data=None, cls=True):
    exit()

def all_users_controller(data=None, cls=True):
    users=User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Продолжить? ")
    return 'main', None

def show_user_controller(data=None, cls=True):
    users=User.all()
    render_template(context={'users':users}, template="show_user.jinja2", cls=cls)
    username = input("Введите имя пользователя: ")
    for i in users:
        if i.name == username:
            render_template(context={'user':i.name, 'phones':i.phones}, template="show_user2.jinja2", cls=cls)
    input("Продолжить? ")
    return 'main', None


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user

def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user

def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user

def delete_user_controller(data=None, cls=True):
    users=User.all()
    render_template(context={'users': users}, template="delete_user.jinja2", cls=cls)
    username = input("Введите имя пользователя, которого нужно удалить: ")
    user = User.delete(username)
    return '1', user

def update_user_controller(data=None, cls=True):
    users=User.all()
    request = input('Введите 1, если хотите изменить имя; любую другую клавишу - если хотите изменить номер: ')
    if request == '1':
        render_template(context={'users': users}, template="update_name1.jinja2", cls=cls)
        old_name = input()
        new_name = input("Новое имя: ")
        user = User.update(old_name, new_name)
        return '1', user
    else:
        render_template(context={'users': users}, template="update_name2.jinja2", cls=cls)
        username = input("Введите имя пользователя, чей номер Вы бы хотели изменить: ")
        phones = Phone.all()
        for i in range(len(users)):
            if users[i].name == username:
                numbers_line = ''
                for k in users[i].phones:
                    numbers_line = numbers_line + k.phone + ' '
                print(f'Номера, принадлежащие пользователю {users[i].name}: {numbers_line}')
        old_phone = input("Введите номер, который хотите изменить: ")
        new_phone = input("Новый номер: ")
        phone = Phone.update(old_phone, new_phone)
        return '1', phone  

def get_controller(state):
    return controllers_dict.get(state, default_controller)

controllers_dict = {
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    '3': update_user_controller,
    '4': delete_user_controller,
    '5': show_user_controller,
    21: add_phone_controller,
    212: add_more_controller
}

