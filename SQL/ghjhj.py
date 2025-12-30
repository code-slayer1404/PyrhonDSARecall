import pymysql

class StudentDAO:
    URL = "localhost"
    USER = "Pranshu"
    PASS = "Pranshu@123"
    DATABASE = "school"
    TABLE = "student"

    def get_connection(self):
        conn = pymysql.connect(host=self.URL, user=self.USER, password=self.PASS)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DATABASE}")
        cursor.execute(f"USE {self.DATABASE}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.TABLE} (roll INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
        return conn

    def get_student(self, roll):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT name FROM {self.TABLE} WHERE roll = {roll}")
            result = cursor.fetchone()
            if result:
                return {"roll": roll, "name": result[0]}
        except pymysql.Error as err:
            print(err)
        return None

    def add_student(self, name):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {self.TABLE} (name) VALUES ('{name}')")
            conn.commit()
            print(cursor.rowcount, "record inserted.")
        except pymysql.Error as err:
            print(err)

    def remove_student(self, roll):
        # Implement this method
        pass
