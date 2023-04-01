from flask import jsonify

from backend.model.posts import PostsDAO


class BasePosts:
    def build_map_dict(self, row):
        result = {'post_id': row[0], 'title': row[1], 'content': row[2], 'created_at': row[3],
                  'parent_post_id': row[4], 'user_id': row[5], 'is_admin': row[6]}
        return result

    def build_attr_dict(self, post_id, title, content, created_at, parent_post_id, user_id):
        result = {'post_id': post_id, 'title': title, 'content': content,
                  'created_at': created_at, 'parent_post_id': parent_post_id, 'user_id': user_id}
        return result

    def getAllPosts(self):
        dao = PostsDAO()
        posts_list = dao.getAllPosts()
        result_list = []
        for row in posts_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTittleByPostId(self, post_id):
        dao = PostsDAO()
        row = dao.getTittleByPostId(post_id)
        if not row:
            return jsonify("post not found"), 404
        else:
            post = self.build_map_dict(row)
        return jsonify(post)

    def getContentByPostId(self, post_id):
        dao = PostsDAO()
        row = dao.getContentByPostId(post_id)
        if not row:
            return jsonify("post not found"), 404
        else:
            post = self.build_map_dict(row)
        return jsonify(post)

    def getCreatedAtByPostId(self, post_id):
        dao = PostsDAO()
        row = dao.getCreatedAtByPostId(post_id)
        if not row:
            return jsonify("post not found"), 404
        else:
            post = self.build_map_dict(row)
        return jsonify(post)

    def getParentPostIdByPostId(self, post_id):
        dao = PostsDAO()
        row = dao.getParentPostIdByPostId(post_id)
        if not row:
            return jsonify("post not found"), 404
        else:
            post = self.build_map_dict(row)
        return jsonify(post)

    def getUserIdByPostId(self, post_id):
        dao = PostsDAO()
        row = dao.getUserIdByPostId(post_id)
        if not row:
            return jsonify("post not found"), 404
        else:
            post = self.build_map_dict(row)
        return jsonify(post)

    def updatePost(self, post_id, json):
        tittle = json['tittle']
        content = json['content']
        created_at = json['created_at']
        parent_post_id = json['parent_post_id']
        user_id = json['user_id']
        dao = PostsDAO()
        if tittle != '':
            dao.updateTittleByPostId(post_id)
        if content != '':
            dao.updateContentByPostId(post_id)
        if parent_post_id != '':
            dao.updateParentIdPostByPostId(post_id)
        result = self.build_attr_dict(post_id, tittle, content, created_at, parent_post_id, user_id)
        return jsonify(result)

    def updateTittleByPostId(self, post_id, json):
        tittle = json['tittle']
        dao = PostsDAO()
        if tittle != '':
            dao.updateTittleByPostId(post_id)
        else:
            return jsonify('Error, we can not change tittle to \'\'')
        return jsonify('tittle Updated'), 200

    def updateContentByPostId(self, post_id, json):
        content = json['content']
        dao = PostsDAO()
        if content != '':
            dao.updateContentByPostId(post_id)
        else:
            return jsonify('Error, we can not change content to \'\'')
        return jsonify('content Updated'), 200

    def updateParentIdPostByPostId(self, post_id, json):
        parent_post_id = json['parent_post_id']
        dao = PostsDAO()
        if parent_post_id != '':
            dao.updateParentIdPostByPostId(post_id)
        else:
            return jsonify('Error, we can not change parent post id to \'\'')
        return jsonify('parent post id Updated'), 200

    def deletePost(self, post_id):
        dao = PostsDAO()
        result = dao.deletePostsById(post_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
