from core.settings import DATABASES
import sqlite3


def get_price(kit):

    try:
        """ Module connects and get data into db file
        """
        connect_to_db = sqlite3.connect(DATABASES['default']['NAME'])
        cursor = connect_to_db.cursor()
        match kit:
            case "all":
                query = """select index_sheet, name_of_works, quantity, uom, cost, curency 
                            from calc_data_inner"""
            case "inner":
                query = """select index_sheet, name_of_works, quantity, uom, cost, curency 
                            from calc_data_inner 
                            where name_of_works = ' Установка видеокамеры (внутренняя) '
                            and name_of_works LIKE 'Обжим кабеля' """
                            #  'and name_of_works = " Обжим кабеля "'
                             #  'and name_of_works = " Установка распаечных коробок "')
            case "out":
                cursor.execute(
                    'select index_sheet, name_of_works, quantity, uom, cost, curency from calc_data_inner where '
                    'name_of_works = " Установка видеокамеры (уличная) "'
                    'and name_of_works = " Обжим кабеля "'
                    'and name_of_works = " Установка распаечных коробок "')

        cursor.execute(query)
        answer = cursor.fetchall()
        cursor.close()
        return answer
    except sqlite3.DatabaseError as error:
        print("Ошибка при подключении к sqlite data", error)
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (connect_to_db):
            connect_to_db.close()


print(get_price('inner'))