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



    