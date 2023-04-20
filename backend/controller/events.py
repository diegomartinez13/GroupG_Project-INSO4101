from flask import jsonify

from backend.model.events import EventDAO

class BaseEvents:
    def build_map_dict(self, row):
        result = {'event_id': row[0], 'name': row[1], 'description': row[2], 'location': row[3], 'start_datetime': row[4], 'end_datetime': row[5]}
        return result

    def build_attr_dict(self, event_id, name, description, location, start_datetime, end_datetime):
        result = {'event_id': event_id, 'name': name, 'description': description, 'location': location, 'start_datetime': start_datetime, 'end_datetime': end_datetime}
        return result

    def getAllEvents(self):
        dao = EventDAO()
        event_list = dao.getAllEvents()
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getEventById(self, event_id):
        dao = EventDAO()
        row = dao.getEventById(event_id)
        if not row:
            return jsonify("Event Not Found"), 404
        else:
            event = self.build_map_dict(row)
            return jsonify(event)
        
    def getEventInDateRange(self, start_datetime, end_datetime):
        dao = EventDAO()
        event_list = dao.getEventInDateRange(start_datetime, end_datetime)
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getEventByName(self, name):
        dao = EventDAO()
        event_list = dao.getEventByName(name)
        if event_list is None or len(event_list) == 0:
            return jsonify('Name not found')
        else:
            result_list = []
            for row in event_list:
                result = self.build_map_dict(row)
                result_list.append(result)
            return jsonify(result_list)

    def getDescriptionByName(self, name):
        dao = EventDAO()
        event_list = dao.getDescriptionByEvent(name)
        result_list = []
        if event_list is None or len(event_list) == 0:
            return jsonify('Name not found')
        else:
            for row in event_list:
                result = self.build_map_dict(row)
                result_list.append(result)
            return jsonify(result_list)

    def getLocationByName(self, name):
        dao = EventDAO()
        event_list = dao.getLocationByName(name)
        result_list = []
        if event_list is None or len(event_list) == 0:
            return jsonify('Name not found')
        else:
            for row in event_list:
                result = self.build_map_dict(row)
                result_list.append(result)
            return jsonify(result_list)

    def getStartDateTimeByName(self, name):
        dao = EventDAO()
        event_list = dao.getStartDateTimeByName(name)
        result_list = []
        if event_list is None or len(event_list) == 0:
            return jsonify('Name not found')
        else:
            for row in event_list:
                result = self.build_map_dict(row)
                result_list.append(result)
            return jsonify(result_list)

    def getNameByLocation(self, location):
        dao = EventDAO()
        event_list = dao.getNameByLocation(location)
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getNameByStartDateTime(self, start_datetime):
        dao = EventDAO()
        event_list = dao.getNameByStartDateTime(start_datetime)
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getNameByEndDateTime(self, end_datetime):
        dao = EventDAO()
        event_list = dao.getNameByEndDateTime(end_datetime)
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def insertEvent(self, json):
        name = json['name']
        description = json['description']
        location = json['location']
        start_datetime = json['start_datetime']
        end_datetime = json['end_datetime']

        dao = EventDAO()
        event_id = dao.insertEvent(name, description, location, start_datetime, end_datetime)
        result = self.build_attr_dict(event_id, name, description, location, start_datetime, end_datetime)
        return jsonify(result), 201

    def updateEvent(self, event_id, json):
        name = json['name']
        description = json['description']
        location = json['location']
        start_datetime = json['start_datetime']
        end_datetime = json['end_datetime']

        dao = EventDAO()
        if name != '':
            dao.updateNameByEvent(event_id, name)
        if description != '':
            dao.updateDescriptionByEvent(event_id, description)
        if location != '':
            dao.updateLocationByEvent(event_id, location)
        if start_datetime != '':
            dao.updateStartDateTimeByEvent(event_id, start_datetime)
        if end_datetime != '':
            dao.updateEndDateTimeByEvent(event_id, end_datetime)
        result = self.build_attr_dict(event_id, name, description, location, start_datetime, end_datetime)
        return jsonify(result), 200

    def updateNameByEvent(self, event_id, json):
        name = json['name']
        dao = EventDAO()
        if name != '':
            result = dao.updateNameByEvent(event_id, name)
            if result == 0:
                return jsonify('Error, the event_id does not exist')
        else:
            return jsonify('Error, we can not change name to \'\'')
        return jsonify('name Updated'), 200

    def updateDescriptionByEvent(self, event_id, json):
        description = json['description']
        dao = EventDAO()
        if description != '':
            result = dao.updateNameByEvent(event_id, description)
            if result == 0:
                return jsonify('Error, the event_id does not exist')
        else:
            return jsonify('Error, we can not change description to \'\'')
        return jsonify('description Updated'), 200

    def updateLocationByEvent(self, event_id, json):
        location = json['location']
        dao = EventDAO()
        if location != '':
            result = dao.updateNameByEvent(event_id, location)
            if result == 0:
                return jsonify('Error, the event_id does not exist')
        else:
            return jsonify('Error, we can not change location to \'\'')
        return jsonify('location Updated'), 200

    def updateStartDateTimeByEvent(self, event_id, json):
        start_datetime = json['start_datetime']
        dao = EventDAO()
        if start_datetime != '':
            result = dao.updateNameByEvent(event_id, start_datetime)
            if result == 0:
                return jsonify('Error, the event_id does not exist')
        else:
            return jsonify('Error, we can not change start_datetime to \'\'')
        return jsonify('start_datetime Updated'), 200

    def updateEndDateTimeByEvent(self, event_id, json):
        end_datetime = json['end_datetime']
        dao = EventDAO()
        if end_datetime != '':
            result = dao.updateNameByEvent(event_id, end_datetime)
            if result == 0:
                return jsonify('Error, the event_id does not exist')
        else:
            return jsonify('Error, we can not change end_datetime to \'\'')
        return jsonify('end_datetime Updated'), 200

    def deleteEvent(self, event_id):
        dao = EventDAO()
        result = dao.deleteEvent(event_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
