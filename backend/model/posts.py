from backend.db.config import pg_config

import psycopg2

class PostsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = 'select * from Posts'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTittleByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'select tittle from posts natural inner join users where post_id = %s;'
        cursor.execute(query, post_id,)
        result = cursor.fethone()
        return result

    def getContentByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'select content from posts natural inner join users where post_id = %s;'
        cursor.execute(query, post_id, )
        result = cursor.fethone()
        return result

    def getCreatedAtByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'select created_at from posts natural inner join users where post_id = %s;'
        cursor.execute(query, post_id, )
        result = cursor.fethone()
        return result

    def getParentPostIdByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'select parent_post_id from posts natural inner join users where post_id = %s;'
        cursor.execute(query, post_id, )
        result = cursor.fethone()
        return result

    def getUserIdByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'select user_id from posts natural inner join users where post_id = %s;'
        cursor.execute(query, post_id, )
        result = cursor.fethone()
        return result

    def insertPost(self, tittle, content, created_at, parent_post_id, user_id):
        cursor = self.conn.cursor()
        query = "insert into Posts(tittle, content, cretaed_at, parent_post_id, user_id) values (%s, %s, %s, %s, %s) returning post_id ;"
        cursor.execute(query, (tittle, content, created_at, parent_post_id, user_id))
        post_id = cursor.fetchone()[0]
        self.conn.commit()
        return post_id

    def updateTittleByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'update posts set tittle = %s where post_id = %s;'
        try:
            cursor.execute(query, (post_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return post_id

    def updateContentByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'update posts set content = %s where post_id = %s;'
        try:
            cursor.execute(query, (post_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return post_id

    def updateParentIdPostByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'update posts set parent_post_id = %s where post_id = %s;'
        try:
            cursor.execute(query, (post_id,))
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return 0
        self.conn.commit()
        return post_id

    def deletePostsById(self, post_id):
        cursor = self.conn.cursor()
        query = "delete from Posts where post_id = %s;"
        cursor.execute(query, (post_id,))
        self.conn.commit()
        return post_id

