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

    def getUsernameById(self, user_id):
        cursor = self.conn.cursor()
        query = "select username from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getIdByUsername(self, username):
        cursor = self.conn.cursor()
        query = 'select user_id from users where username = %s;'
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getPasswordById(self, user_id):
        cursor = self.conn.cursor()
        query = "select password from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getPasswordByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select password from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getRewardsPointsById(self, user_id):
        cursor = self.conn.cursor()
        query = "select reward_points from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getRewardsPointsByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select reward_points from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getTargetGoalAmountById(self, user_id):
        cursor = self.conn.cursor()
        query = "select target_goal_amount from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getTargetGoalAmountByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select target_goal_amount from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getTargetGoalHoursById(self, user_id):
        cursor = self.conn.cursor()
        query = "select target_goal_hours from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getTargetGoalHoursByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select target_goal_hours from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getIsAdminById(self, user_id):
        cursor = self.conn.cursor()
        query = "select is_admin from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getIsAdminByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select is_admin from users where username = %s;"
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

    def updateUserUsername(self, user_id, username):
        cursor = self.conn.cursor()
        query = "update users set username = %s where user_id = %s;"
        cursor.execute(query, (username, user_id))
        self.conn.commit()
        return user_id

    def updateUserPassword(self, user_id, password):
        cursor = self.conn.cursor()
        query = "update users set password = %s where user_id = %s;"
        cursor.execute(query, (password, user_id))
        self.conn.commit()
        return user_id

    def updateUserRewardPoints(self, user_id, reward_points):
        cursor = self.conn.cursor()
        query = "update users set reward_points = %s where user_id = %s;"
        cursor.execute(query, (reward_points, user_id))
        self.conn.commit()
        return user_id

    def updateUserTargetGoalAmount(self, user_id, target_goal_amount):
        cursor = self.conn.cursor()
        query = "update users set target_goal_amount = %s where user_id = %s;"
        cursor.execute(query, (target_goal_amount, user_id))
        self.conn.commit()
        return user_id

    def updateUserTargetGoalHours(self, user_id, target_goal_hours):
        cursor = self.conn.cursor()
        query = "update users set target_goal_hours = %s where user_id = %s;"
        cursor.execute(query, (target_goal_hours, user_id))
        self.conn.commit()
        return user_id

    def updateUserIsAdmin(self, user_id, is_admin):
        cursor = self.conn.cursor()
        query = "update users set is_admin = %s where user_id = %s;"
        cursor.execute(query, (is_admin, user_id))
        self.conn.commit()
        return user_id

    def deleteUser(self, user_id):
        cursor = self.conn.cursor()
        query = "delete from users where user_id = %s;"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return user_id

    # Statistical Queries

    def getTop5UsersWithMostRewardPoints(self):
        cursor = self.conn.cursor()
        query = 'Select username, rewar_points ' \
                'from users ' \
                'order by reward_points desc ' \
                'limit 5;'
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostTargetGoalAmount(self):
        cursor = self.conn.cursor()
        query = 'Select username, target_goal_amount ' \
                'from users ' \
                'order by target_goal_amount desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostTargetGoalHours(self):
        cursor = self.conn.cursor()
        query = 'Select username, target_goal_hours ' \
                'from users ' \
                'order by target_goal_hours desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostRecyclingHours(self):
        cursor = self.conn.cursor()
        query = 'select username, recycling_hours ' \
                'from users natural inner join RecyclingEfforts ' \
                'order by recycling_hours desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostAmountRecycled(self):
        cursor = self.conn.cursor()
        query = 'select username, amount_recycled ' \
                'from users natural inner join RecyclingEfforts ' \
                'order by amount_recycled desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostPosts(self):
        cursor = self.conn.cursor()
        query = 'select username, count(*) as counter ' \
                'from users natural inner join Posts ' \
                'group by username ' \
                'order by counter desc ' \
                'limit 5'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5UsersWithMostReactions(self):
        cursor = self.conn.cursor()
        query = 'select username, count(*) counter ' \
                'from users natural inner join HasReaction ' \
                'where is_liked = true ' \
                'group by username ' \
                'order by counter desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTop5LocationsWithMostEvents(self):
        cursor = self.conn.cursor()
        query = 'select location, count(*) counter ' \
                'from Events ' \
                'group by location ' \
                'order by counter desc ' \
                'limit 5;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result



