from werkzeug.exceptions import BadRequest
from flask import request

trips = [
    {
        'id': 1,
        "detination": 'Windsor',
        "activities": ['boating'],
        "attractions": ['Windsor Castle', 'Tudor Mansion'],
        "places to eat": ['Waterside Inn','Two Brewers']
},
{
        'id': 2,
        "detination": 'Winchester',
        "activities": ['Visit farmers market'],
        "attractions": ['Winchester Cathedral', 'Winchester College', 'Winchester City Mill', 'Great Hall', 'Jane Austens House'],
        "places to eat": ['Wykehame Arms', 'The Chesil Rectory']
},
{
        'id': 3,
        "detination": 'Salisbury',
        "activities": ['Sightseeing'],
        "attractions": ['Stonehenge', 'cathedral'],
        "places to eat": ['Pythouse kitchen garden']
},
{
        'id': 4,
        "detination": 'Bath',
        "activities": ['hot air balloon','hiking'],
        "attractions": ['Roman Baths','Fashion Museum'],
        "places to eat": ['The Scallop Shell', 'Noyas kitchen','The Dark Horse']
}
]

def index(req):
    return trips, 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_trip = request.json
    trips.append(new_trip)
    new_trip['id'] = len(trips)
    print(new_trip)
    
    return new_trip

def find_by_uid(uid):
    try:
        return next(trip for trip in trips if trip['id'] == uid)
    except:
        raise BadRequest(f"We don't have that trip with id {uid}!")