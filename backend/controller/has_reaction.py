from flask import jsonify

from backend.model.has_reaction import HasReactionDAO


class BaseUsers:

    def build_map_dict(self, row):
        result = {'user_id': row[0], 'post_id': row[1], 'is_liked': row[2],}
        return result

    def build_attr_dict(self, user_id, post_id, is_liked):
        result = {'user_id': user_id, 'post_id': post_id, 'is_liked': is_liked}
        return result

    def getAllHasReaction(self):
        dao = HasReactionDAO()
        user_list = dao.getAllHasRecation()
        result_list = []
        for row in user_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getIsLikedByUser(self, user_id):
        dao = HasReactionDAO()
        row = dao.getIsLikedByUser(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getIsLikedByPost(self, post_id):
        dao = HasReactionDAO()
        row = dao.getIsLikedByPost(post_id)
        if not row:
            return jsonify("Post Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def updateIsLikedByUser(self, user_id, json):
        is_liked = json['is_liked']
        dao = HasReactionDAO()
        if is_liked != '':
            dao.updateIsLikedByUser(user_id)
        else:
            return jsonify('Error, we can not change like to \'\'')
        return jsonify('like Updated'), 200

    def updateIsLikedByPost(self, post_id, json):
        is_liked = json['is_liked']
        dao = HasReactionDAO()
        if is_liked != '':
            dao.updateIsLikedByUser(post_id)
        else:
            return jsonify('Error, we can not change like to \'\'')
        return jsonify('like Updated'), 200

    def deleteHasReaction(self, user_id, post_id):
        dao = HasReactionDAO()
        result = dao.deleteHasReaction(user_id, post_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

