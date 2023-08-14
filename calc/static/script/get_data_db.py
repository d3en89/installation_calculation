from core.settings import DATABASES
import sqlite3


def get_price():
    try:
        """ Module connects and get data into db file
        """
        connect_to_db = sqlite3.connect(DATABASES['default']['NAME'])
        cursor = connect_to_db.cursor()
        cursor.execute('select index_sheet, name_of_works, quantity, uom, cost, curency from calc_data_inner')
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
