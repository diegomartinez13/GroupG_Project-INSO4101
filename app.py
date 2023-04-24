import os


from dotenv import load_dotenv


from flask import Flask, jsonify, request, redirect

from flask_cors import CORS

from werkzeug.security import generate_password_hash, check_password_hash


from backend.controller.users import BaseUsers

from backend.controller.events import BaseEvents

from backend.controller.recycling_centers import BaseRecyclingCenters

from backend.controller.recycling_efforts import BaseRecyclingEfforts

from backend.controller.posts import BasePosts

from backend.controller.has_reaction import BaseHasReaction


app = Flask(__name__, static_folder='build/', static_url_path='/')


load_dotenv(dotenv_path=".env")


CORS(app, origin='http://localhost:3000')


@app.route("/")

def index():

    return {'message' : 'Welcome!'}


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route("/events")

def getEvents():

    return BaseEvents().getAllEvents()


@app.route("/login", methods=['POST', 'GET'])

def login():

    if request.method == 'POST':

        print(request.json)

        username = request.json['username']

        password = request.json['password']
        

        user = BaseUsers().getUserByUsername(username)

        if user:

            if check_password_hash(user.json['password'], password):
                return user
            else:

                return jsonify(Error="Invalid Password"), 401
        else:

            return jsonify(Error="User Not Found"), 404

    elif request.method == 'GET':

        #TODO: Connect flask app to react app

        return {'message': 'Welcome to the login page'}, 200

    return 400


@app.route("/register", methods=['POST', 'GET'])

def register():

    if request.method == 'POST':

        username = request.json['username']

        password = request.json['password']

        password_confirmation = request.json['password_confirmation']
        

        if BaseUsers().checkUserExists(username):

            return jsonify(Error="User Already Exists"), 409

        elif password != password_confirmation:

            return jsonify(Error="Passwords do not match"), 401
        else:

            print(generate_password_hash(password, method='sha256'))

            result = BaseUsers().insertUser(username, generate_password_hash(password, method='sha256'), 0, 0, 0, False)
            
            return result

    elif request.method == 'GET':

        #TODO: Connect flask app to react app

        return {'message': 'Welcome to the registration page'}

    return 400


# ------------------- USER ROUTES ---------------------

@app.route("/user", methods=['GET', 'POST'])

def handleUsers():

    if request.method == 'GET':

        return BaseUsers().getAllUsers()

    elif request.method == 'POST':

        username = request.json['username']

        password = request.json['password']

        reward_points = request.json['reward_points']

        target_goal_amount = request.json['target_goal_amount']

        target_goal_hours = request.json['target_goal_hours']

        is_admin = request.json['is_admin']

        return BaseUsers().insertUser(username, password, reward_points, target_goal_amount, target_goal_hours, is_admin)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/<int:user_id>", methods=['GET', 'POST', 'DELETE'])

def handleUsersByID(user_id):

    if request.method == 'GET':

        return BaseUsers().getUserById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUser(user_id, request.json)

    elif request.method == 'DELETE':

        return BaseUsers().deleteUser(user_id)
    else:

        return jsonify('Method not Allowed'), 405



@app.route("/user/<username>", methods=['GET'])

def getUserByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getUserByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/username/<int:user_id>", methods=['GET', 'POST'])

def handleUserUsernameById(user_id):

    if request.method == 'GET':

        return BaseUsers().getUsernameById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserUsername(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/id/<username>", methods=['GET'])

def getUsersIdByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getIdByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/password/<int:user_id>", methods=['GET', 'POST'])

def handleUserPasswordById(user_id):

    if request.method == 'GET':

        return BaseUsers().getPasswordById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserPassword(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/password/<username>", methods=['GET'])

def getUserPasswordsByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getPasswordByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/reward_points/<int:user_id>", methods=['GET', 'POST'])

def handleUserRewardPointsById(user_id):

    if request.method == 'GET':

        return BaseUsers().getRewardsPointsById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserRewardPoints(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/reward_points/<username>", methods=['GET'])

def getUserRewardPointsByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getRewardsPointsByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/target_goal_amount/<int:user_id>", methods=['GET', 'POST'])

def handleUserTargetGoalAmountById(user_id):

    if request.method == 'GET':

        return BaseUsers().getTargetGoalAmountById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserTargetGoalAmount(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/target_goal_amount/<username>", methods=['GET'])

def getUserTargetGoalAmountByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getTargetGoalAmountByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/target_goal_hours/<int:user_id>", methods=['GET', 'POST'])

def handleUserTargetGoalHoursById(user_id):

    if request.method == 'GET':

        return BaseUsers().getTargetGoalHoursById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserTargetGoalHours(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/target_goal_amount/<username>", methods=['GET'])

def getUserTargetGoalHoursByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getTargetGoalHoursByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/is_admin/<int:user_id>", methods=['GET', 'POST'])

def handleUserIsAdminById(user_id):

    if request.method == 'GET':

        return BaseUsers().getIsAdminById(user_id)

    elif request.method == 'POST':

        return BaseUsers().updateUserIsAdmin(user_id, request.json)
    else:

        jsonify("Method Not Allowed"), 405



@app.route("/user/is_admin/<username>", methods=['GET'])

def getUserIsAdminByUsername(username):

    if request.method == 'GET':

        return BaseUsers().getIsAdminByUsername(str(username))
    else:

        jsonify("Method Not Allowed"), 405



#  STATISTICAL ROUTES

@app.route("/user/statistics/top5userswithmostrewardpoints", methods=['GET'])

def getTop5UsersWithMostRewardPoints():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostRewardPoints()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5userswithmosttargetgoalamount", methods=['GET'])

def getTop5UsersWithMostTargetGoalAmount():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostTargetGoalAmount()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5userswithmosttargetgoalhours", methods=['GET'])

def getTop5UsersWithMostTargetGoalHours():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostTargetGoalHours()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5userswithmostrecyclinghours", methods=['GET'])

def getTop5UsersWithMostRecyclingHours():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostRecyclingHours()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5userswithmostposts", methods=['GET'])

def getTop5UsersWithMostPosts():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostPosts()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5userswithmostreactions", methods=['GET'])

def getTop5UsersWithMostReactions():

    if request.method == 'GET':

        return BaseUsers().getTop5UsersWithMostReactions()
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/user/statistics/top5locationswithmostevents", methods=['GET'])

def getTop5LocationsWithMostEvents():

    if request.method == 'GET':

        return BaseUsers().getTop5LocationsWithMostEvents()
    else:

        return jsonify("Method Not Allowed"), 405



# ------------------- EVENTS ROUTES ---------------------

@app.route("/events", methods=['GET', 'POST'])

def handleEvents():

    if request.method == 'GET':

        return BaseEvents().getAllEvents()

    elif request.method == 'POST':

        return BaseEvents().insertEvent(request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/<int:event_id>", methods=['GET', 'POST', 'DELETE'])

def handleEventsByID(event_id):

    if request.method == 'GET':

        return BaseEvents().getEventById(event_id)

    elif request.method == 'POST':

        return BaseEvents().updateEvent(event_id, request.json)

    elif request.method == 'DELETE':

        return BaseEvents().deleteEvent(event_id)
    else:

        return jsonify('Method not Allowed'), 405


# Route of getEventsInDateRange is not done



@app.route("/events/<name>", methods=['Get'])

def getEventsByName(name):

    if request.method == 'GET':

        return BaseEvents().getEventByName(str(name))
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/description/<name>", methods=['GET'])

def getEventsDescriptionByName(name):

    if request.method == 'GET':

        return BaseEvents().getDescriptionByName(str(name))
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/location/<name>", methods=['GET'])

def getEventsLocationByName(name):

    if request.method == 'GET':

        return BaseEvents().getLocationByName(str(name))
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/start_date_time/<name>", methods=['GET'])

def getEventsStartDateTimeByName(name):

    if request.method == 'GET':

        return BaseEvents().getStartDateTimeByName(str(name))
    else:

        return jsonify("Method Not Allowed"), 405


# routes for getNameByLocation, getNameByStartDateTime, getNameByEndDateTime



@app.route("/events/name/<int:event_id>", methods=['POST'])

def updateEventsNameById(event_id):

    if request.method == 'POST':

        return BaseEvents().updateNameByEvent(event_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/description/<int:event_id>", methods=['POST'])

def updateEventsDescriptionById(event_id):

    if request.method == 'POST':

        return BaseEvents().updateDescriptionByEvent(event_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/location/<int:event_id>", methods=['POST'])

def updateEventsLocationById(event_id):

    if request.method == 'POST':

        return BaseEvents().updateLocationByEvent(event_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/start_date_time/<int:event_id>", methods=['POST'])

def updateEventsStartDateTimeById(event_id):

    if request.method == 'POST':

        return BaseEvents().updateStartDateTimeByEvent(event_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/events/end_date_time/<int:event_id>", methods=['POST'])

def updateEventsEndDateTimeById(event_id):

    if request.method == 'POST':

        return BaseEvents().updateEndDateTimeByEvent(event_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



# ------------------- RECYCLING CENTERS ROUTES ---------------------


@app.route("/recycling_center", methods=['GET', 'POST'])

def handleRecyclingCenter():

    if request.method == 'GET':

        return BaseRecyclingCenters().getAllRecyclingCenters()

    elif request.method == 'POST':

        return BaseRecyclingCenters().insertRecyclingCenters(request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_center/<int:center_id>", methods=['POST', 'DELETE'])

def handleRecyclingCentersById(center_id):

    if request.method == 'POST':

        return BaseRecyclingCenters().updateRecycleCenters(center_id, request.json)

    elif request.method == 'DELETE':

        return BaseRecyclingCenters().deleteRecyclingCentersById(center_id)
    else:

        return jsonify('Method not Allowed'), 405



@app.route("/recycling_center/information/<int:center_id>", methods=['GET', 'POST'])

def getRecyclingCentersInformationById(center_id):

    if request.method == 'GET':

        return BaseRecyclingCenters().getInformationByID(center_id)

    elif request.method == 'POST':

        return BaseRecyclingCenters().updateInformationById(center_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_center/Location/<int:center_id>", methods=['GET', 'POST'])

def getRecyclingCentersLocationById(center_id):

    if request.method == 'GET':

        return BaseRecyclingCenters().getLocationByID(center_id)

    elif request.method == 'POST':

        return BaseRecyclingCenters().updateLocationById(center_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_center/coordinates/<int:center_id>", methods=['GET', 'POST'])

def getRecyclingCentersCoordinatesById(center_id):

    if request.method == 'GET':

        return BaseRecyclingCenters().getCoordinatesByID(center_id)

    elif request.method == 'POST':

        return BaseRecyclingCenters().updateCoordinatesById(center_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



# ------------------- RECYCLING EFFORTS ROUTES ---------------------



@app.route("/recycling_efforts", methods=['GET', 'POST'])

def handleRecyclingEfforts():

    if request.method == 'GET':

        return BaseRecyclingEfforts().getAllRecyclingEfforts()

    elif request.method == 'POST':

        return BaseRecyclingEfforts().insertRecyclingEfforts(request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/<int:effort_id>", methods=['POST', 'DELETE'])

def handleRecyclingEffortsById(effort_id):

    if request.method == 'POST':

        return BaseRecyclingEfforts().updateRecyclingEfforts(effort_id, request.json)

    elif request.method == 'DELETE':

        return BaseRecyclingEfforts().deleteRecyclingEfforts(effort_id)
    else:

        return jsonify('Method Not Allowed'), 405


@app.route("/recycling_efforts/<int:user_id>", methods=['GET'])

def getRecyclingEffortsByUser(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getAllRecyclingEffortsByUser(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/hours/<int:user_id>", methods=['GET'])

def getRecyclingHoursByUser(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getAllRecyclingEffortsByUser(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/hours/<int:user_id>/<recycling_date>", methods=['GET'])

def getRecyclingHoursByUserByDate(user_id, recycling_date):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getRecyclingHoursByUserByDate(user_id, str(recycling_date))
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/hours_by_dates/<int:user_id>", methods=['GET'])

def getRecyclingHoursByUserByDates(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getRecyclingHoursByUserByDates(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/amount/<int:user_id>", methods=['GET'])

def getRecyclingAmountByUser(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getAllAmountRecycledByUser(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/amount/<int:user_id>/<recycling_date>", methods=['GET'])

def getRecyclingAmountByUserByDate(user_id, recycling_date):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getAmountRecycledByUserByDate(user_id, str(recycling_date))
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/amount_by_dates/<int:user_id>", methods=['GET'])

def getRecyclingAmountByUserByDates(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getAmountRecycledByUserByDates(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/dates/<int:user_id>", methods=['GET'])

def getRecyclingDatesByUser(user_id):

    if request.method == 'Get':

        return BaseRecyclingEfforts().getRecyclingDatesByUser(user_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/update_hours/<int:effort_id>", methods=['POST'])

def updateRecyclingHoursById(effort_id):

    if request.method == 'POST':

        return BaseRecyclingEfforts().updateRecyclingHoursById(effort_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/update_amount/<int:effort_id>", methods=['POST'])

def updateRecyclingAmountById(effort_id):

    if request.method == 'POST':

        return BaseRecyclingEfforts().updateAmountRecycledById(effort_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/recycling_efforts/update_date/<int:effort_id>", methods=['POST'])

def updateRecyclingDateById(effort_id):

    if request.method == 'POST':

        return BaseRecyclingEfforts().updateRecyclingDateById(effort_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



# ------------------- POSTS ROUTES ---------------------


@app.route("/posts", methods=['GET', 'POST'])

def handlePosts():

    if request.method == 'GET':

        return BasePosts().getAllPosts()

    elif request.method == 'POST':

        return BasePosts().insertPost(request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/posts/<int:post_id>", methods=['POST', 'DELETE'])

def handlePostsById(post_id):

    if request.method == 'POST':

        return BasePosts().updatePost(post_id, request.json)

    elif request.method == 'DELETE':

        return BasePosts().deletePost(post_id)
    else:

        return jsonify('Method Not Allowed'), 405


@app.route("/tittle/<int:post_id>", methods=['GET', 'POST'])

def getPostTittleById(post_id):

    if request.method == 'GET':

        return BasePosts().getTittleByPostId(post_id)

    elif request.method == 'POST':

        return BasePosts().updateTittleByPostId(post_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/content/<int:post_id>", methods=['GET', 'POST'])

def getPostContentById(post_id):

    if request.method == 'GET':

        return BasePosts().getContentByPostId(post_id)

    elif request.method == 'POST':

        return BasePosts().updateContentByPostId(post_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/created_at/<int:post_id>", methods=['GET'])

def getPostCreatedAtById(post_id):

    if request.method == 'GET':

        return BasePosts().getCreatedAtByPostId(post_id)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/parent_post_id/<int:post_id>", methods=['GET', 'POST'])

def getPostParentPostIdById(post_id):

    if request.method == 'GET':

        return BasePosts().getParentPostIdByPostId(post_id)

    elif request.method == 'POST':

        return BasePosts().updateParentIdPostByPostId(post_id, request.json)
    else:

        return jsonify("Method Not Allowed"), 405



# ------------------- HAS REACTION ROUTES ---------------------


@app.route("/has_reaction", methods=['GET', 'POST'])

def handleHasReaction():

    if request.method == 'GET':

        return BaseHasReaction().getAllHasReaction()

    elif request.method == 'POST':

        return BaseHasReaction().insertHasReaction(request.json)
    else:

        return jsonify("Method Not Allowed"), 405



@app.route("/has_reaction/isLiked_by_user/<int:user_id>", methods=['GET', 'POST'])

def handleHasReactionIsLikedByUserId(user_id):

    if request.method == 'GET':

        return BaseHasReaction().getIsLikedByUser(user_id)

    elif request.method == 'POST':

        return BaseHasReaction().updateIsLikedByUser(user_id, request.json)
    else:

        return jsonify('Method Not Allowed'), 405



@app.route("/has_reaction/isLiked_by_post/<int:post_id>", methods=['GET', 'POST'])

def handleHasReactionIsLikedByPostId(post_id):

    if request.method == 'GET':

        return BaseHasReaction().getIsLikedByPost(post_id)

    elif request.method == 'POST':

        return BaseHasReaction().updateIsLikedByPost(post_id, request.json)
    else:

        return jsonify('Method Not Allowed'), 405



@app.route("/has_reaction/<int:user_id>/<int:post_id>", methods=['DELETE'])

def handleHasReactionByUserIdByPost(user_id, post_id):

    if request.method == 'DELETE':

        return BaseHasReaction().deleteHasReaction(user_id, post_id)
    else:

        return jsonify('Method Not Allowed'), 405



if __name__ == "__main__":
    app.run()

