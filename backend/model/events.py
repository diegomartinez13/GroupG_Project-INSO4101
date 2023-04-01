from backend.db.config import pg_config

import psycopg2


class EventDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllEvents(self):
        cursor = self.conn.cursor()
        query = "select * from events;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEventById(self, event_id):
        cursor = self.conn.cursor()
        query = "select * from events where event_id = %s;"
        cursor.execute(query, (event_id,))
        result = cursor.fetchone()
        return result

    def getEventInDateRange(self, start_datetime, end_datetime):
        cursor = self.conn.cursor()
        query = "select * from events where start_datetime between %s and %s;"
        cursor.execute(query, (start_datetime, end_datetime))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEventByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from events where name like %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDescriptionByEvent(self, event_id):
        cursor = self.conn.cursor()
        query = 'select description from events where event_id = %s;'
        cursor.execute(query, (event_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLocationByName(self, name):
        cursor = self.conn.cursor()
        query = "select location from events where name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getStartDateTimeByName(self, name):
        cursor = self.conn.cursor()
        query = 'select start_datetime from events where name = %s;'
        cursor.execute(query, (name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEndDateTimeByName(self, name):
        cursor = self.conn.cursor()
        query = 'select end_datetime from events where name = %s;'
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNameByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select name from events where location = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNameByStartDateTime(self, start_datetime):
        cursor = self.conn.cursor()
        query = "select name from events where start_datetime = %s;"
        cursor.execute(query, (start_datetime,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNameByEndDateTime(self, end_datetime):
        cursor = self.conn.cursor()
        query = "select name from events where end_datetime = %s;"
        cursor.execute(query, (end_datetime,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def convertStartDateTimeToString(self, event_id):
    #     cursor = self.conn.cursor()
    #     query = "select TO_CHAR(start_datetime, 'YYYY/MM/DD HH:MM:SS') from events where event_id = %s;"
    #     cursor.execute(query, (event_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def convertEndDateTimeToString(self, event_id):
    #     cursor = self.conn.cursor()
    #     query = "select TO_CHAR(end_datetime, 'YYYY/MM/DD HH:MM:SS') from events where event_id = %s;"
    #     cursor.execute(query, (event_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def insertEvent(self, name, description, location, start_datetime, end_datetime):
    #     cursor = self.conn.cursor()
    #     query = "insert into Events (name, description, location, start_datetime, end_datetime) values (%s, %s, %s, %s, %s) returning event_id;"
    #     cursor.execute(query, (name, description, location, start_datetime, end_datetime))
    #     event_id = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return event_id

    def updateNameByEvent(self, event_id, name):
        cursor = self.conn.cursor()
        query = 'update events set name = %s where event_id = %s;'
        cursor.execute(query, (name, event_id))
        self.conn.commit()
        return event_id

    def updateDescriptionByEvent(self, event_id, description):
        cursor = self.conn.cursor()
        query = 'update events set description = %s where event_id = %s;'
        cursor.execute(query, (description, event_id))
        self.conn.commit()
        return event_id

    def updateLocationByEvent(self, event_id, location):
        cursor = self.conn.cursor()
        query = 'update events set location = %s where event_id = %s;'
        cursor.execute(query, (location, event_id))
        self.conn.commit()
        return event_id

    def updateStartDateTimeByEvent(self, event_id, start_datetime):
        cursor = self.conn.cursor()
        query = 'update events set start_datetime = %s where event_id = %s;'
        cursor.execute(query, (start_datetime, event_id))
        self.conn.commit()
        return event_id

    def updateEndDateTimeByEvent(self, event_id, end_datetime):
        cursor = self.conn.cursor()
        query = 'update events set end_datetime = %s where event_id = %s;'
        cursor.execute(query, (end_datetime, event_id))
        self.conn.commit()
        return event_id

    def deleteEvent(self, event_id):
        cursor = self.conn.cursor()
        query = 'delete from events where event_id = %s;'
        cursor.execute(query, (event_id,))
        self.conn.commit()
        return event_id
