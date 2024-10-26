import mysql.connector as con

class Storage:
    message=''
    try:
        @staticmethod
        def Connect():
            connection=con.connect(
                host="localhost",
                user='root',
                password='',
                database='taxi_booking_system'
            )
            if connection.is_connected():
                Storage.message="Connected"
                return connection
            connection.close()
    except Exception as e:
        print(e)

