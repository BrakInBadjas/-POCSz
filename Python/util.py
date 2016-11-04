import db

#Check if there exists a door with the given door_id. Returns true if this is the case.
def doorExists(door_ID):
    count = db.getDoorCount(door_ID)['count(*)'];
    return count > 0

#Adds a door if the door does not yet exist.
def addDoorIfNotExists(input):
    door_id = input['door']
    if not doorExists(door_id):
        db.addNewDoor(door_id, '123')
        return doorExists(door_id)
    else:
        return True

#Checks if a give Key UID has access to a certain door
def hasPermission(key_uid, door_id):
    person = db.getPersonByUID(key_uid)
    if person is None:
        return False

    if (int(door_id) in db.getPersonDoor(person['id'])):
        return True
    elif (int(door_id) in db.getRoleDoor(person['role_id'])):
        return True
    return False