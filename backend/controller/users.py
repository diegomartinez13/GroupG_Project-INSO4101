from flask import jsonify

from backend.model.users import UserDAO

class BaseUsers:

    def build_map_dict(self, row):
        result = {'user_id': row[0], 'username': row[1], 'password': row[2], 'reward_points': row[3], 'target_goal_amount': row[4], 'target_goal_hours': row[5], 'is_admin': row[6]}
        return result
    
    def build_attr_dict(self, user_id, reward_points, target_goal_amount, target_goal_hours, is_admin):
        result = {'user_id': user_id, 'reward_points': reward_points, 'target_goal_amount': target_goal_amount, 'target_goal_hours': target_goal_hours, 'is_admin': is_admin}
        return result

    def getAllUsers(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getUserById(self, user_id):
        dao = UserDAO()
        row = dao.getUserById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getUserByUsername(self, username):
        dao = UserDAO()
        row = dao.getUserByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)
    
    def checkUserExists(self, username):
        dao = UserDAO()
        row = dao.getUserByUsername(username)
        if not row:
            return False
        else:
            return True

    def insertUser(self, username, password, reward_points, target_goal_amount, target_goal_hours, is_admin):
        dao = UserDAO()
        user_id = dao.insertUser(username, password, reward_points, target_goal_amount, target_goal_hours, is_admin)
        result = self.build_attr_dict(user_id, 0, 0, 0, False)
        return jsonify(result), 201