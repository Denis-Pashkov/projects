import requests
import os
import datetime

def connect_to_api(todos, users):
    """Функция для загрузки данных в формате JSON

    Args:
        todos ([str]): [Ссылка на данные о задачах пользователей в формате JSON]
        users ([str]): [Ссылка на список данных о пользователях в формате JSON]
    """
    try:
        data_todos = requests.get(todos)
        data_todos = data_todos.json()
        data_users = requests.get(users)
        data_users = data_users.json()
        # Получаем 2 списка словарей с данными
        user_data_preparation(data_todos, data_users)
    except:
        # Если не удалось загрузить данные
        print('Eror of internet connection or web page not found')

def user_data_preparation(data_todos, data_users):
    """Функция для заполнения набора данных result_data(dict) информацией о пользователях

    Args:
        data_todos ([list]): [Список данных о задачах пользователей]
        data_users ([list]): [Список данных пользователей]
    """
    dateTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    # Создание переменной для хранения текущей даты и времени в формате 14.11.2021 17:44
    id_list = []
    # Создание списка для хранения идентификаторов пользователей
    result_data = {}
    # Создание результирующего набора данных
    for user in data_users:
        # Итерируемся по списку словарей пользователей
        id = user['id']
        id_list.append(id)
        # Формируем и добавляем текущий идентификатор пользователя в список id_list
        username = user['username']
        # Формируем текущий username для создания имени файла в будущем
        first_line = 'Отчет для ' + user['company']['name'] + '.'
        # Формируем 1 строку строку будущего файла с названием компании
        second_line = user['name'] + ' ' + '<' + user['email'] + '>' + ' ' + dateTime
        # Формируем 2 строку будущего файла с именем пользователя, email и текущей датой и временем
        result_data[id] = [username, first_line, second_line]
        # Заносим данные в результирующий набор result_data(dict) с ключем id и значением списка с именем пользователя, первой и второй строкой
    num_of_users_tasks(id_list, data_todos, result_data)

def normalize_length(line, actual_list):
    if len(line) <= 48:
        actual_list.append(line)
        return(actual_list)
    else:
        actual_list.append(line[:48] + '...')
        return(actual_list)

def num_of_users_tasks(id_list, data_todos, result_data):
    """Функция для определения общего количества задач, выполненных и не выполненных и занесения их в результирующий набор данных result_data

    Args:
        id_list ([list]): [Список с идентификаторами пользователей]
        data_todos ([list]): [Список данных о задачах пользователей]
        result_data ([dict]): [Результирующий набор данных с заполненными именем, первой и второй строкой будущего документа]
    """
    count_true = count_false = 0
    # Создание переменных для подсчета количества решенных и нерешенных задач у пользователя
    list_true = []
    list_false = []
    # Создание списков для хранения списка решенных и не решенных задач пользователя
    for id in id_list:
        # Итерация по списку идентификаторов пользователей
        for actual_task in data_todos:
            # Итерация по задачам, которые есть в data_todos
            try:
                if (actual_task['userId'] == id) and (actual_task['completed'] == True):
                    # Если задача относится к текущему по списку идентификаторов и она выполнена
                    count_true += 1
                    # Добавляем задачу к выполненным в счетчик count_true
                    list_true = normalize_length(actual_task['title'], list_true)
                    # Формируем список выполненных задач в функции normalize_length в список list_true
                elif (actual_task['userId'] == id) and (actual_task['completed'] == False):
                    # Если задача относится к текущему по списку идентификаторов и она не выполнена
                    count_false += 1
                    # Добавляем задачу к невыполненным в счетчик count_false
                    list_false = normalize_length(actual_task['title'], list_false)
                    # Формируем список невыполненных задач в функции normalize_length в список list_false
            except:
                True
                # Если нет ключей ['userId'] или ['completed'] или ['title'] у текущего словаря

        result_data[id].append('Всего задач: ' + str(count_true + count_false))
        # Добавляем в результирующий набор данных 3 строку с общим количеством задач у пользователя
        result_data[id].append('')
        # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
        result_data[id].append('Завершенные задачи ({}):'.format(str(count_true)))
        # Добавляем в результирующий набор данных 5 строку с общим количеством выполненных задач пользователя
        result_data[id].append(list_true)
        # # Добавляем в результирующий набор данных список с выполненными задачами пользователя
        result_data[id].append('')
        # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
        result_data[id].append('Оставшиеся задачи ({}):'.format(str(count_false)))
        # Добавляем в результирующий набор данных 5 строку с общим количеством невыполненных задач пользователя
        result_data[id].append(list_false)
        # # Добавляем в результирующий набор данных список с выполненными задачами пользователя
        list_true = []
        list_false = []
        count_true = 0
        count_false = 0
        # Обнуляем и очищаем локальные переменные и списки для внесения данных нового пользователя
    check_exist_folder()
    # Вызываем функцию проверки существования директории tasks
    create_and_filling_files(id_list, result_data)
    # Вызываем функцию создания и заполнения файлов из результирующего набора данных

def check_exist_folder():
    """Функция для проверки существования директории tasks
    """
    if (os.path.exists('tasks')):
        # Если директория с названием tasks существует, то перейти в неё
        os.chdir('tasks')
    else:
        # Если не существует, то создать и перейти в неё
        os.mkdir('tasks')
        os.chdir('tasks')

def file_exist(path):
    """Функция для переименования файла в формат old_Karianne_2021-11-14T19_01
    Во времени не двоеточие, тк Windows не дает использовать его в названии файла
    
    Args:
        path ([str]): [Строка с названием будущего файла в виде Bret.txt]
    """
    currentFile = open(path, 'r')
    # Открываем текущий файл на чтение
    userName = path.split('.')
    # Получаем имя пользователя путем создания списка методом split
    oldDateTime = ''
    # Создаем переменную для хранения даты и времени старого документа
    for i, line in zip(range(1, 3), currentFile):
        # Итерируемся по строкам файла и от i == 1 до i == 2, для получения 2 строки файла где хранится время создания отчета
        if i == 2:
            oldDateTime = line
            break
            # Выходим из цикла когда получаем вторую строку в переменную oldDateTime
    currentFile.close()
    # Закрываем файл
    oldDateTime = oldDateTime[-17:]
    # Вырезаем из строки дату и время
    oldDateTime = oldDateTime.split(' ')
    # Отделяем дату и время путем создания списка методом split
    oldDate = oldDateTime[0]
    # Создаем переменную oldDate и помещаем в неё дату
    oldDate = oldDate.split('.')
    # Формируем список
    oldDate = oldDate[::-1]
    # Переворачиваем список для создания имени в нужном формате
    oldDate = '-'.join(oldDate)
    # Конвертируем список в строку с разделителем -
    oldTime = oldDateTime[1]
    # Создаем переменную oldDate и помещаем в неё время
    oldTime = oldTime[:5]
    # Приводим струку к нужному формату
    oldTime = oldTime.replace(':', '_')
    # Заменяем двоеточие на нижнее подчеркивание
    new_path = 'old_' + userName[0] + '_' + oldDate + 'T' + oldTime + '.txt'
    # Содаем переменную для сохранения в ней нового имени файла
    try:
        # Если такого файла не существует
        os.rename(path, new_path)
    except:
        # Если такой файл существует
        print('File with name {} is already exist'.format(new_path))
        print('Try to generate a report after 1 minute')

def create_and_filling_files(id_list, result_data):
    """Функция для создания и заполнения файлов из результирующего набора данных

    Args:
        id_list ([list]): [Список с идентификаторами пользователей]
        result_data ([dict]): [Результирующий набор данных с именем пользователя, всеми строками и списками задач пользователей]
    """
    for id in id_list:
        # Итерация по идентификаторам пользователей
        if os.path.exists('{}.txt'.format(result_data[id][0])):
            # Если файл с таким названием уже существует в директории tasks
            file_exist('{}.txt'.format(result_data[id][0]))
            # Вызываем функцию для переименования файла
            new_file = open('{}.txt'.format(result_data[id][0]), 'w')
            # Создаем новый файл с именем пользователя и открываем его на запись
        else:
            new_file = open('{}.txt'.format(result_data[id][0]), 'w')
            # Если нет такого файла, то создаем новый файл с именем пользователя и открываем его на запись
        
        result_data[id].pop(0)
        # Удаляем име пользователя из результирующего набора данных

        for line in result_data[id]:
            # Итерация по результирующему набору данных
            try:
                # Если нет проблем с записью на диск
                if type(line) == list:
                    # Если текущий элемент набора список
                    for task in line:
                        # Итерация по этому списку(списку задач)
                        print(task, file=new_file)
                        # Запись данных в файл построчно
                else:
                    print(line, file=new_file)
                    # Если текущий элемент набора строка
            except:
                # Если возникли проблемы с записью на диск
                print('Error while writing file to disk')
        new_file.close()
        # Закрываем файл

connect_to_api('https://json.medrating.org/todos', 'https://json.medrating.org/users')
# Вызов функции для загрузки данных в формате JSON

os.chdir('..')
# Если захотите открыть несколько раз через VSCode, не мешает выполнению программы в ином случае
