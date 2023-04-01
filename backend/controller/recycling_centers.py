from flask import jsonify
from backend.model.recycling_centers import RecyclingCentersDAO


class BaseRecyclingCenters:
    def build_map_dict(self, row):
        result = {'center_id': row[0], 'information': row[1], 'location': row[2], 'coordinates': row[3]}
        return result

    def build_attr_dict(self, center_id, information, location, coordinates):
        result = {'center_id': center_id, 'information': information, 'location': location, 'coordinates': coordinates}
        return result

    def getAllRecyclingCenters(self):
        dao = RecyclingCentersDAO()
        event_list = dao.getAllRecyclingCenters()
        result_list = []
        for row in event_list:
            result = self.build_map_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getInformationByID(self, center_id):
        dao = RecyclingCentersDAO()
        row = dao.getInformationById(center_id)
        if not row:
            return jsonify("User Not Found"), 404
        else:
            event = self.build_map_dict(row)
            return jsonify(event)

    def getLocationByID(self, center_id):
        dao = RecyclingCentersDAO()
        row = dao.getLocationById(center_id)
        if not row:
            return jsonify("Event Not Found"), 404
        else:
            event = self.build_map_dict(row)
            return jsonify(event)

    def getcoordinatesByID(self, center_id):
        dao = RecyclingCentersDAO()
        row = dao.getCoordinatesById(center_id)
        if not row:
            return jsonify("Event Not Found"), 404
        else:
            event = self.build_map_dict(row)
            return jsonify(event)

    def updateRecycleCenters(self, center_id, json):
        information = json['information']
        location = json['location']
        coordinates = json['coordinates']
        dao = RecyclingCentersDAO()
        if information != '':
            dao.updateInformationById(center_id, information)
        if location != '':
            dao.updateLocationById(center_id, location)
        if coordinates != '':
            dao.updateCoordinatesById(center_id, coordinates)

        result = self.build_attr_dict(center_id, information, location, coordinates)
        return jsonify(result), 200

    def updateInformationById(self ,center_id, json):
        information = json['information']
        dao = RecyclingCentersDAO()
        if information != '':
            dao.updateInformationById(information, center_id)
        else:
            return jsonify('Error, we can not change information to \'\'')
        return jsonify('Information Updated')

    def updateLocationById(self, center_id, json):
        location = json['location']
        dao = RecyclingCentersDAO()
        if location != '':
            dao.updateLocationById(location, center_id)
        else:
            return jsonify('Error, we can not change location to \'\'')
        return jsonify('Location Updated')

    def updateCoordinatesById(self, center_id, json):
        coordinates = json['coordinates']
        dao = RecyclingCentersDAO()
        if coordinates != '':
            dao.updateCoordinatesById(coordinates, center_id)
        else:
            return jsonify('Error, we can not change coordinates to \'\'')
        return jsonify('coordinates Updated')

    def deleteRecyclingCentersById(self, center_id):
        dao = RecyclingCentersDAO()
        result = dao.deleteRecyclingCenter(center_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
