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

    def getUsernameById(self, user_id):
        dao = UserDAO()
        row = dao.getUsernameById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getPasswordByUsername(self, username):
        dao = UserDAO()
        row = dao.getPasswordByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getRewardsPointsByUsername(self, username):
        dao = UserDAO()
        row = dao.getRewardsPointsByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getTargetGoalAmountByUsername(self, username):
        dao = UserDAO()
        row = dao.getTargetGoalAmountByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getTargetGoalHoursByUsername(self, username):
        dao = UserDAO()
        row = dao.getTargetGoalAmountByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict(row)
            return jsonify(user)

    def getIsAdminByUsername(self, username):
        dao = UserDAO()
        row = dao.getIsAdminByUsername(username)
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

    def updateUser(self, user_id, json):
        password = json['password']
        reward_points = json['reward_points']
        target_goal_amount = json['target_goal_amount']
        target_goal_hours = json['target_goal_hours']
        is_admin = json['is_admin']
        dao = UserDAO()
        if password != '':
            dao.updateUserPassword(user_id, password)
        if reward_points != '':
            dao.updateUserRewardPoints(user_id, reward_points)
        if target_goal_amount != '':
            dao.updateUserTargetGoalAmount(user_id, target_goal_amount)
        if target_goal_hours != '':
            dao.updateUserTargetGoalHours(user_id,target_goal_hours)
        if is_admin != '':
            dao.updateUserIsAdmin(user_id, is_admin)
        result = self.build_attr_dict(user_id, reward_points, target_goal_amount, target_goal_hours, is_admin)
        return jsonify(result), 200

    def updateUserUsername(self, user_id, json):
        username = json['username']
        dao = UserDAO()
        if username != '':
            dao.updateUserUsername(user_id, username)
        else:
            return jsonify('Error, we can not change username to \'\'')
        return jsonify('Username Updated'), 200

    def updateUserPassword(self, user_id, json):
        password = json['password']
        dao = UserDAO()
        if password != '':
            dao.updateUserPassword(user_id, password)
        else:
            return jsonify('Error, we can not change password to \'\'')
        return jsonify('password Updated'), 200

    def updateUserRewardPoints(self, user_id, json):
        reward_points = json['reward_points']
        dao = UserDAO()
        if reward_points != '':
            dao.updateUserRewardPoints(user_id, reward_points)
        else:
            return jsonify('Error, we can not change reward_points to \'\'')
        return jsonify('reward_points Updated'), 200

    def updateUserTargetGoalAmount(self, user_id, json):
        target_goal_amount = json['target_goal_amount']
        dao = UserDAO()
        if target_goal_amount != '':
            dao.updateUserTargetGoalAmount(user_id, target_goal_amount)
        else:
            return jsonify('Error, we can not change target_goal_amount to \'\'')
        return jsonify('target_goal_amount Updated'), 200

    def updateUserTargetGoalHours(self, user_id, json):
        target_goal_hours = json['target_goal_hours']
        dao = UserDAO()
        if target_goal_hours != '':
            dao.updateUserTargetGoalAmount(user_id, target_goal_hours)
        else:
            return jsonify('Error, we can not change target_goal_hours to \'\'')
        return jsonify('target_goal_hours Updated'), 200

    def updateUserIsAdmin(self, user_id, json):
        is_admin = json['target_goal_hours']
        dao = UserDAO()
        if is_admin != '':
            dao.updateUserTargetGoalAmount(user_id, is_admin)
        else:
            return jsonify('Error, we can not change is_admin to \'\'')
        return jsonify('is_admin Updated'), 200

    def deleteUser(self, user_id):
        dao = UserDAO()
        result = dao.deleteUser(user_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
