from flask import jsonify

from backend.model.users import UserDAO


class BaseUsers:

    def build_map_dict(self, row):
        result = {'user_id': row[0], 'username': row[1], 'password': row[2], 'reward_points': row[3], 'target_goal_amount': row[4], 'target_goal_hours': row[5], 'is_admin': row[6]}
        return result

    def build_map_dict_id(self, row):
        result = {'user_id': row[0]}
        return result

    def build_map_username(self, row):
        result = {'username': row[0]}
        return result

    def build_map_dict_password(self, row):
        result = {'password': row[0]}
        return result

    def build_map_dict_reward_points(self, row):
        result = {'reward_points': row[0]}
        return result

    def build_map_dict_target_goal_amount(self, row):
        result = {'target_goal_amount': row[0]}
        return result

    def build_map_dict_target_goal_hours(self, row):
        result = {'target_goal_hours': row[0]}
        return result

    def build_map_dict_is_admin(self, row):
        result = {'is_admin': row[0]}
        return result

    def build_map_dict_top5_most_users_reward_points(self, row):
        result = {'username': row[0], 'reward_points': row[1]}
        return result

    def build_map_dict_top5_most_users_target_goal_amount(self, row):
        result = {'username': row[0], 'target_goal_amount': row[1]}
        return result

    def build_map_dict_top5_most_users_target_goal_hours(self, row):
        result = {'username': row[0], 'target_goal_hours': row[1]}
        return result

    def build_map_dict_top5_most_users_recycling_hours(self, row):
        result = {'username': row[0], 'recycling_hours': row[1]}
        return result

    def build_map_dict_top5_most_users_amount_recycled(self, row):
        result = {'username': row[0], 'amount_recycled': row[1]}
        return result

    def build_map_dict_top5_most_users_posts(self, row):
        result = {'username': row[0], 'posts': row[1]}
        return result

    def build_map_dict_top5_most_users_reactions(self, row):
        result = {'username': row[0], 'reactions': row[1]}
        return result

    def build_map_dict_top5_locations_most_events(self, row):
        result = {'location': row[0], 'events': row[1]}
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
            user = self.build_map_username(row)
            return jsonify(user)

    def getIdByUsername(self, username):
        dao = UserDAO()
        row = dao.getIdByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_id(row)
            return jsonify(user)

    def getPasswordById(self, user_id):
        dao = UserDAO()
        row = dao.getPasswordById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_password(row)
            return jsonify(user)

    def getPasswordByUsername(self, username):
        dao = UserDAO()
        row = dao.getPasswordByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_password(row)
            return jsonify(user)

    def getRewardsPointsById(self, user_id):
        dao = UserDAO()
        row = dao.getRewardsPointsById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_reward_points(row)
            return jsonify(user)

    def getRewardsPointsByUsername(self, username):
        dao = UserDAO()
        row = dao.getRewardsPointsByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_reward_points(row)
            return jsonify(user)

    def getTargetGoalAmountById(self, user_id):
        dao = UserDAO()
        row = dao.getTargetGoalAmountById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_target_goal_amount(row)
            return jsonify(user)

    def getTargetGoalAmountByUsername(self, username):
        dao = UserDAO()
        row = dao.getTargetGoalAmountByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_target_goal_amount(row)
            return jsonify(user)

    def getTargetGoalHoursById(self, user_id):
        dao = UserDAO()
        row = dao.getTargetGoalAmountById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_target_goal_hours(row)
            return jsonify(user)

    def getTargetGoalHoursByUsername(self, username):
        dao = UserDAO()
        row = dao.getTargetGoalAmountByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_target_goal_hours(row)
            return jsonify(user)

    def getIsAdminById(self, user_id):
        dao = UserDAO()
        row = dao.getIsAdminById(user_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_is_admin(row)
            return jsonify(user)

    def getIsAdminByUsername(self, username):
        dao = UserDAO()
        row = dao.getIsAdminByUsername(username)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            user = self.build_map_dict_is_admin(row)
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

    # Statistical Queries
    def getTop5UsersWithMostRewardPoints(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostRewardPoints()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_reward_points(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5UsersWithMostTargetGoalAmount(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostTargetGoalAmount()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_target_goal_amount(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5UsersWithMostTargetGoalHours(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostTargetGoalHours()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_target_goal_hours(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5UsersWithMostRecyclingHours(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostRecyclingHours()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_recycling_hours(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5UsersWithMostPosts(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostPosts()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_posts(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5UsersWithMostReactions(self):
        dao = UserDAO()
        user_list = dao.getTop5UsersWithMostReactions()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_most_users_reactions(row)
            result_list.append(result)
        return jsonify(result_list)

    def getTop5LocationsWithMostEvents(self):
        dao = UserDAO()
        user_list = dao.getTop5LocationsWithMostEvents()
        result_list = []
        for row in user_list:
            result = self.build_map_dict_top5_locations_most_events(row)
            result_list.append(result)
        return jsonify(result_list)
