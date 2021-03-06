from flask import Blueprint, request, make_response
from Response import Response
from Models.Attendee import Attendee
from Models.Meeting import Meeting
from Services.AttendanceService import AttendanceService

AttendanceService = AttendanceService()


attendance = Blueprint("AttendanceEndpoints", __name__, url_prefix="/api/attendance")

@attendance.route("/", methods=["GET"])
def get():
    print("You are here")
    #I don't know maybe create the Meeting model and pass it the id
    

@attendance.route("/<attendance_id>", methods=["POST"])
def recordAttendance(attendance_id):
    #record that the person is attending the specific meeting 
    name = request.form["name"]
    userID = request.form["userID"]
    
    #if there is no preset userID then create a new Attendee
    if(userID == ""):
        attendee = AttendanceService.createAttendee(name)
    else:
        #update the name of the person with the userID
        attendee = AttendanceService.updateName(name, userID)
        
    AttendanceService.attendMeeting(attendee, attendance_id)
    
    return Response({"userID": str(attendee.attendeeID)}, status=200)