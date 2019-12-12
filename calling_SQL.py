import pyodbc

class AirportConnection:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'airport'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_airport = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)

        self.cursor = self.docker_airport.cursor()
# cursor.execute('select * from passengers')
# row = cursor.fetchone()
# print(row)


