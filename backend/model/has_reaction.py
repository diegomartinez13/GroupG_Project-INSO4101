from backend.db.config import pg_config

import psycopg2


class HasReactionDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (
        pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHasRecation(self):
        cursor = self.conn.cursor()
        query = 'select * from HasReaction;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIsLikedByUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'select is_liked from HasReaction where user_id = %s;'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIsLikedByPost(self, post_id):
        cursor = self.conn.cursor()
        query = 'select is_liked from HasReaction where post_id = %s;'
        cursor.execute(query, (post_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertHasReaction(self, user_id, post_id, is_liked):
        cursor = self.conn.cursor()
        query ="insert into HasReaction(user_id, post_id, is_liked) values (%s, %s, %s) returning post_id ;"
        cursor.execute(query, (user_id, post_id, is_liked,))
        post_id = cursor.fetchone()[1]
        self.conn.commit()
        return post_id

    def updateIsLikedByUser(self, user_id, is_liked):
        cursor = self.conn.cursor()
        query = 'update Hasreaction set is_liked = %s where user_id = %s;'
        cursor.execute(query, (is_liked, user_id))
        self.conn.commit()
        return user_id

    def updateIsLikedByPost(self, post_id, is_liked):
        cursor = self.conn.cursor()
        query = 'update Hasreaction set is_liked = %s where post_id = %s;'
        cursor.execute(query, (is_liked, post_id))
        self.conn.commit()
        return post_id

    def deleteHasReaction(self, user_id, post_id):
        cursor = self.conn.cursor()
        query = 'delete from HAsReaction where user_id = %s and post_id = %s;'
        cursor.execute(query, (user_id, post_id,))
        self.conn.commit()
        return user_id
