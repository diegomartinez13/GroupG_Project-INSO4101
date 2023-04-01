from flask import jsonify
from backend.model.recycling_efforts import RecyclingEffortsDAO


class BaseRecyclingEfforts:
    def build_map_dict(self, row):
        result = {'effort_id': row[0], 'recycling_hours': row[1], 'amount_recycled': row[2], 'recycling_date': row[3], 'user_id': row[4]}
        return result

    def build_attr_dict(self, effort_id, recycling_hours, amount_recycled, recycling_date, user_id):
        result = {'effort_id': effort_id, 'recycling_hours': recycling_hours, 'amount_recycled': amount_recycled, 'recycling_date': recycling_date, 'user_id': user_id}
        return result

    def getAllRecyclingEfforts(self):
        dao = RecyclingEffortsDAO()
        recyclingEfforts_list = dao.getAllRecyclingEfforts()
        result_list = []
        for row in recyclingEfforts_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return result_list

    def getAllRecyclingEffortsByUser(self, user_id):
        dao = RecyclingEffortsDAO()
        row = dao.getAllRecyclingEffortsByUser(user_id)
        if not row:
            return jsonify("User or date not found"), 404
        else:
            recyclingEffort = self.build_map_dict(row)
            return jsonify(recyclingEffort)

    def getRecyclingHoursByUserByDate(self, user_id, recycling_date):
        dao = RecyclingEffortsDAO()
        row = dao.getRecyclingHoursByUserByDate(user_id, recycling_date)
        if not row:
            return jsonify("User or date not found"), 404
        else:
            recyclingEffort = self.build_map_dict(row)
            return jsonify(recyclingEffort)

    def getRecyclingHoursByUserByDates(self, user_id):
        dao = RecyclingEffortsDAO()
        recyclingEfforts_list = dao.getRecyclingHoursByUserByDates(user_id)
        result_list = []
        for row in recyclingEfforts_list:
            result = self.build_map_dict(row)
            recyclingEfforts_list.append(result)
        return jsonify(result_list)

    def getAllAmountRecycledByUser(self, user_id):
        dao = RecyclingEffortsDAO()
        row = dao.getAllAmountRecycledByUser(user_id)
        if not row:
            return jsonify("User not found"), 404
        else:
            recyclingEffort = self.build_map_dict(row)
            return jsonify(recyclingEffort)

    def getAmountRecycledByUserByDate(self, user_id, recycling_date):
        dao = RecyclingEffortsDAO()
        row = dao.getAmountRecycledByUserByDate(user_id, recycling_date)
        if not row:
            return jsonify("User or date not found"), 404
        else:
            recyclingEffort = self.build_map_dict(row)
            return jsonify(recyclingEffort)

    def getAmountRecycledByUserByDates(self, user_id):
        dao = RecyclingEffortsDAO()
        recyclingEfforts_list = dao.getAmountRecycledByUserByDates(user_id)
        result_list = []
        for row in recyclingEfforts_list:
            result = self.build_map_dict(row)
            recyclingEfforts_list.append(result)
        return jsonify(result_list)

    def getRecyclingDatesByUser(self, user_id):
        dao = RecyclingEffortsDAO()
        recyclingDates_list = dao.getRecyclingDatesByUser(user_id)
        result_list = []
        for row in recyclingDates_list:
            result = self.build_map_dict(row)
            recyclingDates_list.append(result)
        return jsonify(recyclingDates_list)

    def updateRecyclingHours(self, effort_id, json):
        recycling_hours = json['recycling_hours']
        amount_recycled = json['amount_recycled']
        recycling_date = json['recycling_date']
        user_id = json['user_id']
        dao = RecyclingEffortsDAO()
        if recycling_hours != '':
            dao.updateRecyclingHoursById(effort_id, recycling_hours)
        if amount_recycled != '':
            dao.updateAmountRecycledById(effort_id, amount_recycled)
        if recycling_date != '':
            dao.updateRecyclingDateById(effort_id, recycling_date)
        result = self.build_attr_dict(effort_id, recycling_hours, amount_recycled, recycling_date, user_id)
        return jsonify(result), 200

    def updateRecyclingHoursById(self, json):
        effort_id = json['effort_id']
        recycling_hours = json['recycling_hours']
        dao = RecyclingEffortsDAO()
        if recycling_hours != '':
            dao.updateRecyclingHoursById(effort_id, recycling_hours)
        else:
            return jsonify('Error, we can not change recycling hours to \'\'')

        return jsonify('Information Updated'), 200

    def updateAmountRecycledById(self, effort_id, json):
        amount_recycled = json['amount_recycled']
        dao = RecyclingEffortsDAO()
        if amount_recycled != '':
            dao.updateAmountRecycledById(effort_id, amount_recycled)
        else:
            return jsonify('Error, we can not change amount recycled to \'\'')
        return jsonify('Information Updated'), 200

    def RecyclingDateById(self, effort_id, json):
        recycling_date = json['recycling_date']
        dao = RecyclingEffortsDAO()
        if recycling_date != '':
            dao.updateRecyclingDateById(effort_id, recycling_date)
        else:
            return jsonify('Error, we can not change recycling date to \'\'')
        return jsonify('Information Updated'), 200

    def deleteRecyclingEffort(self, effort_id):
        dao = RecyclingEffortsDAO()
        result = dao.deleteRecyclingEffort(effort_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
