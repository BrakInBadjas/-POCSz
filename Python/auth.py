import db

#Checks if a give Key UID has access to a certain door
def hasPermission(key_uid, door_id):
    person = db.getPersonByUID(key_uid)
    
    if ([door_id] in db.getPersonDoor(person[0])):
        return True
    elif ([door_id] in db.getRoleDoor(person[3])):
        return True
    return False