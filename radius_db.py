import sqlite3
from sys import platform
from dataset import PROPERTY_DATA, REQUIREMENT_DATA


class RadiusDB(object):
    def __init__(self):
        if platform == "darwin":
            self.conn = sqlite3.connect('/tmp/radius.db', check_same_thread=False)
        else:
            self.conn = sqlite3.connect('radius.db', check_same_thread=False)

        self.c = self.conn.cursor()

    def create_tables(self):
        """
        Create Tables
        :return: None
        """
        self.c.execute('''CREATE TABLE if not exists Property
                 (
                 id INTEGER primary key autoincrement,
                 latitude DECIMAL(10, 8) NOT NULL,
                 longitude DECIMAL(10, 8) NOT NULL,
                 price DECIMAL(10, 2),
                 number_of_bedrooms INTEGER,
                 number_of_bathrooms INTEGER,
                 UNIQUE(id) ON CONFLICT REPLACE
                 )''')
        self.c.execute('''CREATE TABLE if not exists UserRequirement
                 (
                 id INTEGER primary key autoincrement,
                 latitude DECIMAL(10, 8) NOT NULL,
                 longitude DECIMAL(10, 8) NOT NULL,
                 min_price DECIMAL(10, 2),
                 max_price DECIMAL(10, 2),
                 min_number_of_bedrooms INTEGER,
                 max_number_of_bedrooms INTEGER,
                 min_number_of_bathrooms INTEGER,
                 max_number_of_bathrooms INTEGER,
                 UNIQUE(id) ON CONFLICT REPLACE
                 )''')

    def bulk_insert(self, tablename, column_name_list, value_list, format_value):
        """
        :param tablename: Table Name
        :param item_list: List of tuples of items for the table
        :return:
        """
        self.c.executemany(
            """
                Insert into {0} ({1}) values ({2})
            """.format(tablename, ",".join(column_name_list), format_value),
            value_list)
        self.conn.commit()

    def _fetch_all_from_table(self, table_obj):
        return self.c.execute("Select * from %s ;" % (table_obj.get('table_name')))

    def __exit__(self):
        self.conn.close()


if __name__ == '__main__':
    my_inst = RadiusDB()
    my_inst.create_tables()
    my_inst.bulk_insert(
        'Property',
        PROPERTY_DATA.get('COLUMN_NAMES'),
        PROPERTY_DATA.get('VALUES'),
        ",".join(map(lambda x: '?', PROPERTY_DATA.get('VALUES')[0]))
    )
    my_inst.bulk_insert(
        'UserRequirement',
        REQUIREMENT_DATA.get('COLUMN_NAMES'),
        REQUIREMENT_DATA.get('VALUES'),
        ",".join(map(lambda x: '?', REQUIREMENT_DATA.get('VALUES')[0]))
    )
