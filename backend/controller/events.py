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
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    