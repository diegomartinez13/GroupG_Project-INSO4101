from backend.db.config import pg_config
import psycopg2


class RecyclingCentersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRecyclingCenters(self):
        cursor = self.conn.cursor()
        query = "select * from RecyclingCenters;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInformationById(self, center_id):
        cursor = self.conn.cursor()
        query = 'select information from RecyclingCenters where center_id = %s;'
        cursor.execute(query,(center_id, ))
        result = cursor.fetchone()
        return result

    def getLocationById(self, center_id):
        cursor = self.conn.cursor()
        query = 'select location from RecyclingCenters where center_id = %s;'
        cursor.execute(query,(center_id,))

    def getCoordinatesById(self, center_id):
        cursor = self.conn.cursor()
        query = 'select coordinates from RecyclingCenters where ceter_id = %s;'
        cursor.execute(query,(center_id, ))
        result = cursor.fetchone()
        return result

    def insertRecyclingCenters(self, information, location, coordinates):
        cursor = self.conn.cursor()
        query = "insert into RecyclinCenters(information, location, coordinates) values (%s, %s, %s) returning center_id ;"
        cursor.execute(query, (information, location, coordinates))
        center_id = cursor.fetchone()[0]
        self.conn.commit()
        return center_id

    def updateInformationById(self, information, center_id):
        cursor = self.conn.cursor()
        query = 'update RecyclingCenters set information = %s where center_id = %s;'
        try:
            cursor.execute(query,(information, center_id, ))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return center_id

    def updateLocationById(self, location, center_id):
        cursor = self.conn.cursor()
        query = 'update RecyclingCenters set location = %s where center_id = %s;'
        try:
            cursor.execute(query, (location, center_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return center_id

    def updateCoordinatesById(self, coordinates, center_id):
        cursor = self.conn.cursor()
        query = 'update RecyclingCenters set coordinates = %s where center_id =%s;'
        try:
            cursor.execute(query, (coordinates, center_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.coomit()
        return center_id

    def deleteRecyclingCenter(self, center_id):
        cursor = self.conn.cursor()
        query = 'delete from recyclingCenters where center_id = %s;'
        try:
            cursor.execute(query, (center_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return center_id
