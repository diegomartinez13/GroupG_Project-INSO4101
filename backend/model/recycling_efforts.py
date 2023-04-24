from backend.db.config import pg_config
import psycopg2


class RecyclingEffortsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRecyclingEfforts(self):
        cursor = self.conn.cursor()
        query = 'select * from RecyclingEfforts;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRecyclingEffortsByUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'select recycling_hours, amount_recycled, recycling_date ' \
                'from RecyclingEfforts natural inner join users ' \
                'where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRecyclingHoursByUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'select sum(recycling_hours) from RecyclingEfforts natural inner join users where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getRecyclingHoursByUserByDate(self, user_id, recycling_date):
        cursor = self.conn.cursor()
        query = 'select recycling_hours ' \
                'from RecyclingEfforts natural inner join users ' \
                'where user_id =%s ' \
                'and recycling_date = %s;'
        cursor.execute(query,(user_id, recycling_date))
        result = cursor.fetchone()
        return result

    def getRecyclingHoursByUserByDates(self, user_id):
        cursor = self.conn.cursor()
        query = 'select recycling_hours, recycling_date ' \
                'from RecyclingEfforts natural inner join users ' \
                'where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAmountRecycledByUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'select sum(amount_recycled) from RecyclingEfforts natural inner join users where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getAmountRecycledByUserByDate(self, user_id, recycling_date):
        cursor = self.conn.cursor()
        query = 'select amount_recycled ' \
                'from RecyclingEfforts natural inner join users ' \
                'where user_id = %s ' \
                'and recycling_date = %s;'
        cursor.execute(query, (user_id, recycling_date,))
        result = cursor.fetchone()
        return result

    def getAmountRecycledByUserByDates(self, user_id):
        cursor = self.conn.cursor()
        query = 'select amount_recycled, recycling_date ' \
                'from RecyclingEfforts natural inner join users ' \
                'where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRecyclingDatesByUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'select recycling_date from RecyclingEfforts natural inner join users where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertRecyclingEfforts(self, recycling_hours, amount_recycled, recycling_date, user_id):
        cursor = self.conn.cursor()
        query = "insert into recyclingEfforts(recycling_hours, amount_recyled, recycling_date, user_id) values (%s, %s, %s, %s) returning effort_id;"
        cursor.execute(query, (recycling_hours, amount_recycled, recycling_date, user_id))
        effort_id = cursor.fetchone()[0]
        self.conn.commit()
        return effort_id

    def updateRecyclingHoursById(self, effort_id, recycling_hours):
        cursor = self.conn.cusor()
        query = 'update RecyclingEfforts set recycling_hours = %s where effort_id = %s;'
        try:
            cursor.execute(query, (effort_id, recycling_hours,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return effort_id

    def updateAmountRecycledById(self, effort_id, amount_recycled):
        cursor = self.conn.cusor()
        query = 'update RecyclingEfforts set amount_recycled = %s where effort_id = %s;'
        try:
            cursor.execute(query, (effort_id,amount_recycled,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return effort_id

    def updateRecyclingDateById(self, effort_id, recycling_date):
        cursor = self.conn.cusor()
        query = 'update RecyclingEfforts set recycling_date = %s where effort_id = %s;'
        try:
            cursor.execute(query, (effort_id,recycling_date,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return effort_id

    def deleteRecyclingEfforts(self, effort_id):
        cursor = self.conn.cursor()
        query = 'delete from RecyclingEfforts where effort_id = %s;'
        try:
            cursor.execute(query, (effort_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return effort_id
