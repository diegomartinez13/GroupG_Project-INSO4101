from backend.db.config import pg_config

import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def insertUser(self, username, password, reward_points, target_goal_amount, target_goal_hours, is_admin):
        cursor = self.conn.cursor()
        query = "insert into users(username, password, reward_points, target_goal_amount, target_goal_hours, is_admin) values (%s, %s, %s, %s, %s, %s) returning user_id;"
        cursor.execute(query, (username, password, reward_points, target_goal_amount, target_goal_hours, is_admin))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id

    def updateUser(self, user_id, password, reward_points, target_goal_amount, target_goal_hours, is_admin):
        cursor = self.conn.cursor()
        query = "update users set password = %s, reward_points = %s, target_goal_amount = %s, target_goal_hours = %s, is_admin = %s where user_id = %s;"
        cursor.execute(query, (password, reward_points, target_goal_amount, target_goal_hours, is_admin, user_id))
        self.conn.commit()
        return user_id

    def deleteUser(self, user_id):
        cursor = self.conn.cursor()
        query = "delete from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return user_id