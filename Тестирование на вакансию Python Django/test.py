# Вариант 1 через ООП
# -------------------------------------------------------------------------------------------

import requests
import os
import datetime


class Reports:
    def __init__(self, data_todos, data_users) -> None:
        self.__data_todos = data_todos
        self.__data_users = data_users

    @property
    def data_todos(self):
        return self.__data_todos

    @data_todos.setter
    def data_todos(self, data_todos):
        self.__data_todos = data_todos

    @data_todos.deleter
    def data_todos(self):
        del self.__data_todos

    @property
    def data_users(self):
        return self.__data_users

    @data_users.setter
    def data_users(self, data_users):
        self.__data_users = data_users

    @data_users.deleter
    def data_users(self):
        del self.__data_users

    def __repr__(self):
        return f'class_name = {self.__class__.__name__}, object_id = {id(self)}, data_todos = {self.__data_todos}, data_users = {self.__data_users}'

    @staticmethod
    def __file_exist(path) -> None:
        """Функция для переименования файла в формат old_Karianne_2021-11-14T19_01
        Во времени не двоеточие, тк Windows не дает использовать его в названии файла

        Args:
            path ([str]): [Строка с названием будущего файла в виде Bret.txt]
        """
        with open(path, 'r') as currentFile:
            # Открываем текущий файл на чтение
            oldDateTime = ''
            # Создаем переменную для хранения даты и времени старого документа
            for i, line in zip(range(1, 3), currentFile):
                # Итерация по строкам файла и от i == 1 до i == 2, для получения 2 строки файла где хранится время создания отчета
                if i == 2:
                    oldDateTime = line
                    break
                    # Выходим из цикла когда получаем вторую строку в переменную oldDateTime

        userName = path.split('.')
        # Получаем имя пользователя путем создания списка методом split
        oldDateTime = oldDateTime[-17:].split(' ')
        # Вырезаем из строки дату и время и отделяем дату и время путем создания списка методом split
        oldDate = oldDateTime[0].split('.')
        # Создаем переменную oldDate и помещаем в неё дату и формируем список
        oldDate = oldDate[::-1]
        # Переворачиваем список для создания имени в нужном формате
        oldDate = '-'.join(oldDate)
        # Конвертируем список в строку с разделителем -
        oldTime = oldDateTime[1]
        # Создаем переменную oldDate и помещаем в неё время
        oldTime = oldTime[:5].replace(':', '_')
        # Приводим строку к нужному формату
        new_path = f"old_{userName[0]}_{oldDate}T{oldTime}.txt"
        # Создаем переменную для сохранения в ней нового имени файла
        try:
            # Если такого файла не существует
            os.rename(path, new_path)
        except:
            # Если такой файл существует
            print(f'File with name {new_path} is already exist')
            print('Try to generate a report after 1 minute')

    @classmethod
    def __create_and_filling_files(cls, id_list, result_data) -> None:
        """Функция для создания и заполнения файлов из результирующего набора данных
        Args:
            id_list ([list]): [Список с идентификаторами пользователей]
            result_data ([dict]): [Результирующий набор данных с именем пользователя, всеми строками и списками задач пользователей]
        """
        for id in id_list:
            # Итерация по идентификаторам пользователей
            if os.path.exists(f'{result_data[id][0]}.txt'):
                # Если файл с таким названием уже существует в директории tasks
                cls.__file_exist(f'{result_data[id][0]}.txt')
                # Вызываем функцию для переименования файла

            with open(f'{result_data[id][0]}.txt', 'w') as new_file:
                # Создаем новый файл с именем пользователя и открываем его на запись

                result_data[id].pop(0)
                # Удаляем име пользователя из результирующего набора данных

                for line in result_data[id]:
                    # Итерация по результирующему набору данных
                    try:
                        # Если нет проблем с записью на диск
                        if isinstance(line, list):
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

    @classmethod
    def __num_of_users_tasks(cls, id_list, data_todos, result_data) -> None:
        """Функция для определения общего количества задач, выполненных и не выполненных и занесения их в результирующий набор данных result_data
        Args:
            id_list ([list]): [Список с идентификаторами пользователей]
            data_todos ([list]): [Список данных о задачах пользователей]
            result_data ([dict]): [Результирующий набор данных с заполненными именем, первой и второй строкой будущего документа]
        """

        def normalize_length(line, actual_list) -> list:
            """Функция для нормализации длины строки
            Args:
                line (line): [Строка с задачей пользователя]
                actual_list ([actual_list]): [Список данных о задачах пользователя]
            """
            if len(line) > 48:
                if line[47] == ' ':
                    # Если символ перед ... это пробел
                    actual_list.append(line[:47] + '...')
                else:
                    actual_list.append(line[:48] + '...')
            else:
                actual_list.append(line)
            return (actual_list)

        def check_exist_folder() -> None:
            """Функция для проверки существования директории tasks
            """
            if not os.path.exists('tasks'):
                os.mkdir('tasks')
                # Если не существует, то создать
            os.chdir('tasks')
            # Перейти в директорию

        count_true = 0
        count_false = 0
        # Создание переменных для подсчета количества решенных и нерешенных задач у пользователя
        list_true = []
        list_false = []
        # Создание списков для хранения списка решенных и не решенных задач пользователя
        for id in id_list:
            # Итерация по списку идентификаторов пользователей
            for actual_task in data_todos:
                # Итерация по задачам, которые есть в data_todos
                try:
                    if actual_task['userId'] == id and actual_task['completed'] == True:
                        # Если задача относится к текущему по списку идентификаторов и она выполнена
                        count_true += 1
                        # Добавляем задачу к выполненным в счетчик count_true
                        list_true = normalize_length(actual_task['title'], list_true)
                        # Формируем список выполненных задач в функции normalize_length в список list_true
                    elif actual_task['userId'] == id and actual_task['completed'] == False:
                        # Если задача относится к текущему по списку идентификаторов и она не выполнена
                        count_false += 1
                        # Добавляем задачу к невыполненным в счетчик count_false
                        list_false = normalize_length(actual_task['title'], list_false)
                        # Формируем список невыполненных задач в функции normalize_length в список list_false
                except:
                    pass
                    # Если нет ключей ['userId'] или ['completed'] или ['title'] у текущего словаря
            result_data[id].append(f"Всего задач: {str(count_true + count_false)}")
            # Добавляем в результирующий набор данных 3 строку с общим количеством задач у пользователя
            result_data[id].append('')
            # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
            result_data[id].append(f"Завершенные задачи ({count_true}):")
            # Добавляем в результирующий набор данных 5 строку с общим количеством выполненных задач пользователя
            result_data[id].append(list_true)
            # # Добавляем в результирующий набор данных список с выполненными задачами пользователя
            result_data[id].append('')
            # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
            result_data[id].append(f"Оставшиеся задачи ({count_false}):")
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
        cls.__create_and_filling_files(id_list, result_data)
        # Вызываем функцию создания и заполнения файлов из результирующего набора данных

    @classmethod
    def __user_data_preparation(cls, data_todos, data_users) -> None:
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
            # Итерация по списку словарей пользователей
            id_list.append(user['id'])
            # Формируем и добавляем текущий идентификатор пользователя в список id_list
            first_line = f"Отчет для {user['company']['name']}."
            # Формируем 1 строку будущего файла с названием компании
            second_line = f"{user['name']} <{user['email']}> {dateTime}"
            # Формируем 2 строку будущего файла с именем пользователя, email и текущей датой и временем
            result_data[user['id']] = [user['username'], first_line, second_line]
            # Заносим данные в результирующий набор result_data(dict) с ключем id и значением списка с именем пользователя, первой и второй строкой
        cls.__num_of_users_tasks(id_list, data_todos, result_data)

    def download_and_make_reports(self) -> None:
        try:
            data_todos = requests.get(self.__data_todos).json()
            data_users = requests.get(self.__data_users).json()
            # Получаем 2 списка словарей с данными
            self.__user_data_preparation(data_todos, data_users)
        except:
            # Если не удалось загрузить данные
            print('Error of internet connection or web page not found')


if __name__ == '__main__':
    rp = Reports('https://json.medrating.org/todos', 'https://json.medrating.org/users')
    rp.download_and_make_reports()
    # Вызов метода для загрузки данных в формате JSON

    # os.chdir('..')
    # # Если захотите запустить несколько раз через VSCode

# Вариант 2 через функции
# -------------------------------------------------------------------------------------------

# import requests
# import os
# import datetime
#
#
# def file_exist(path):
#     """Функция для переименования файла в формат old_Karianne_2021-11-14T19_01
#     Во времени не двоеточие, тк Windows не дает использовать его в названии файла
#
#     Args:
#         path ([str]): [Строка с названием будущего файла в виде Bret.txt]
#     """
#     with open(path, 'r') as currentFile:
#         # Открываем текущий файл на чтение
#         oldDateTime = ''
#         # Создаем переменную для хранения даты и времени старого документа
#         for i, line in zip(range(1, 3), currentFile):
#             # Итерируемся по строкам файла и от i == 1 до i == 2, для получения 2 строки файла где хранится время создания отчета
#             if i == 2:
#                 oldDateTime = line
#                 break
#                 # Выходим из цикла когда получаем вторую строку в переменную oldDateTime
#
#     userName = path.split('.')
#     # Получаем имя пользователя путем создания списка методом split
#     oldDateTime = oldDateTime[-17:]
#     # Вырезаем из строки дату и время
#     oldDateTime = oldDateTime.split(' ')
#     # Отделяем дату и время путем создания списка методом split
#     oldDate = oldDateTime[0]
#     # Создаем переменную oldDate и помещаем в неё дату
#     oldDate = oldDate.split('.')
#     # Формируем список
#     oldDate = oldDate[::-1]
#     # Переворачиваем список для создания имени в нужном формате
#     oldDate = '-'.join(oldDate)
#     # Конвертируем список в строку с разделителем -
#     oldTime = oldDateTime[1]
#     # Создаем переменную oldDate и помещаем в неё время
#     oldTime = oldTime[:5]
#     # Приводим строку к нужному формату
#     oldTime = oldTime.replace(':', '_')
#     # Заменяем двоеточие на нижнее подчеркивание
#     new_path = f"old_{userName[0]}_{oldDate}T{oldTime}.txt"
#     # Создаем переменную для сохранения в ней нового имени файла
#     try:
#         # Если такого файла не существует
#         os.rename(path, new_path)
#     except:
#         # Если такой файл существует
#         print(f'File with name {new_path} is already exist')
#         print('Try to generate a report after 1 minute')
#
#
# def create_and_filling_files(id_list, result_data):
#     """Функция для создания и заполнения файлов из результирующего набора данных
#     Args:
#         id_list ([list]): [Список с идентификаторами пользователей]
#         result_data ([dict]): [Результирующий набор данных с именем пользователя, всеми строками и списками задач пользователей]
#     """
#     for id in id_list:
#
#         # Итерация по идентификаторам пользователей
#         if os.path.exists(f'{result_data[id][0]}.txt'):
#             # Если файл с таким названием уже существует в директории tasks
#             file_exist(f'{result_data[id][0]}.txt')
#             # Вызываем функцию для переименования файла
#
#         with open(f'{result_data[id][0]}.txt', 'w') as new_file:
#             # Создаем новый файл с именем пользователя и открываем его на запись
#
#             result_data[id].pop(0)
#             # Удаляем име пользователя из результирующего набора данных
#
#             for line in result_data[id]:
#                 # Итерация по результирующему набору данных
#                 try:
#                     # Если нет проблем с записью на диск
#                     if isinstance(line, list):
#                         # Если текущий элемент набора список
#                         for task in line:
#                             # Итерация по этому списку(списку задач)
#                             print(task, file=new_file)
#                             # Запись данных в файл построчно
#                     else:
#                         print(line, file=new_file)
#                         # Если текущий элемент набора строка
#                 except:
#                     # Если возникли проблемы с записью на диск
#                     print('Error while writing file to disk')
#
#
# def num_of_users_tasks(id_list, data_todos, result_data):
#     """Функция для определения общего количества задач, выполненных и не выполненных и занесения их в результирующий набор данных result_data
#     Args:
#         id_list ([list]): [Список с идентификаторами пользователей]
#         data_todos ([list]): [Список данных о задачах пользователей]
#         result_data ([dict]): [Результирующий набор данных с заполненными именем, первой и второй строкой будущего документа]
#     """
#
#     def normalize_length(line, actual_list):
#         """Функция для нормализации длины строки
#         Args:
#             line (line): [Строка с задачей пользователя]
#             actual_list ([actual_list]): [Список данных о задачах пользователя]
#         """
#         if len(line) > 48:
#             if line[47] == ' ':
#                 # Если символ перед ... это пробел
#                 actual_list.append(line[:47] + '...')
#             else:
#                 actual_list.append(line[:48] + '...')
#         else:
#             actual_list.append(line)
#         return (actual_list)
#
#     def check_exist_folder():
#         """Функция для проверки существования директории tasks
#         """
#         if not os.path.exists('tasks'):
#             os.mkdir('tasks')
#             # Если не существует, то создать
#         os.chdir('tasks')
#         # Перейти в директорию
#
#     count_true = 0
#     count_false = 0
#     # Создание переменных для подсчета количества решенных и нерешенных задач у пользователя
#     list_true = []
#     list_false = []
#     # Создание списков для хранения списка решенных и не решенных задач пользователя
#     for id in id_list:
#         # Итерация по списку идентификаторов пользователей
#         for actual_task in data_todos:
#             # Итерация по задачам, которые есть в data_todos
#             try:
#                 if actual_task['userId'] == id and actual_task['completed'] == True:
#                     # Если задача относится к текущему по списку идентификаторов и она выполнена
#                     count_true += 1
#                     # Добавляем задачу к выполненным в счетчик count_true
#                     list_true = normalize_length(actual_task['title'], list_true)
#                     # Формируем список выполненных задач в функции normalize_length в список list_true
#                 elif actual_task['userId'] == id and actual_task['completed'] == False:
#                     # Если задача относится к текущему по списку идентификаторов и она не выполнена
#                     count_false += 1
#                     # Добавляем задачу к невыполненным в счетчик count_false
#                     list_false = normalize_length(actual_task['title'], list_false)
#                     # Формируем список невыполненных задач в функции normalize_length в список list_false
#             except:
#                 pass
#                 # Если нет ключей ['userId'] или ['completed'] или ['title'] у текущего словаря
#         result_data[id].append(f"Всего задач: {str(count_true + count_false)}")
#         # Добавляем в результирующий набор данных 3 строку с общим количеством задач у пользователя
#         result_data[id].append('')
#         # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
#         result_data[id].append(f"Завершенные задачи ({count_true}):")
#         # Добавляем в результирующий набор данных 5 строку с общим количеством выполненных задач пользователя
#         result_data[id].append(list_true)
#         # # Добавляем в результирующий набор данных список с выполненными задачами пользователя
#         result_data[id].append('')
#         # Добавляем в результирующий набор данных пустой список для формирования пустой строки в будущем
#         result_data[id].append(f"Оставшиеся задачи ({count_false}):")
#         # Добавляем в результирующий набор данных 5 строку с общим количеством невыполненных задач пользователя
#         result_data[id].append(list_false)
#         # # Добавляем в результирующий набор данных список с выполненными задачами пользователя
#         list_true = []
#         list_false = []
#         count_true = 0
#         count_false = 0
#         # Обнуляем и очищаем локальные переменные и списки для внесения данных нового пользователя
#     check_exist_folder()
#     # Вызываем функцию проверки существования директории tasks
#     create_and_filling_files(id_list, result_data)
#     # Вызываем функцию создания и заполнения файлов из результирующего набора данных
#
#
# def user_data_preparation(data_todos, data_users):
#     """Функция для заполнения набора данных result_data(dict) информацией о пользователях
#     Args:
#         data_todos ([list]): [Список данных о задачах пользователей]
#         data_users ([list]): [Список данных пользователей]
#     """
#     dateTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
#     # Создание переменной для хранения текущей даты и времени в формате 14.11.2021 17:44
#     id_list = []
#     # Создание списка для хранения идентификаторов пользователей
#     result_data = {}
#     # Создание результирующего набора данных
#     for user in data_users:
#         # Итерация по списку словарей пользователей
#         id_list.append(user['id'])
#         # Формируем и добавляем текущий идентификатор пользователя в список id_list
#         first_line = f"Отчет для {user['company']['name']}."
#         # Формируем 1 строку будущего файла с названием компании
#         second_line = f"{user['name']} <{user['email']}> {dateTime}"
#         # Формируем 2 строку будущего файла с именем пользователя, email и текущей датой и временем
#         result_data[user['id']] = [user['username'], first_line, second_line]
#         # Заносим данные в результирующий набор result_data(dict) с ключем id и значением списка с именем пользователя, первой и второй строкой
#     num_of_users_tasks(id_list, data_todos, result_data)
#
#
# def connect_to_api(todos, users):
#     """Функция для загрузки данных в формате JSON
#     Args:
#         todos ([str]): [Ссылка на данные о задачах пользователей в формате JSON]
#         users ([str]): [Ссылка на список данных о пользователях в формате JSON]
#     """
#     try:
#         data_todos = requests.get(todos).json()
#         data_users = requests.get(users).json()
#         # Получаем 2 списка словарей с данными
#         user_data_preparation(data_todos, data_users)
#     except:
#         # Если не удалось загрузить данные
#         print('Error of internet connection or web page not found')
#
#
# if __name__ == '__main__':
#     connect_to_api('https://json.medrating.org/todos', 'https://json.medrating.org/users')
#     # Вызов функции для загрузки данных в формате JSON
#
#     os.chdir('..')
#     # Если захотите открыть несколько раз через VSCode, не мешает выполнению программы в ином случае
