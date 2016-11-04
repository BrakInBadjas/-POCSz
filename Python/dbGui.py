from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import db
import hashlib

Builder.load_file('db.kv')

#Creates functions from the menuscreen
class MenuScreen(Screen):
    pass

#Creates functions from the addscreen
class AddScreen(Screen):
	pass

#Creates the functions of the screen where you add a person.    
class AddPersonScreen(Screen):
    def addPerson(self, key_uid, name, role):
        key_uid = key_uid.split(":")
        name = name.split(":")
        role = role.split(":")
        
        db.addNewPerson(key_uid[1].strip(), name[1].strip(), role[1].strip())
        
        popup = Popup(title='Added Person',
                    content=Label(text='Succesfully added {} to Database with Key_UID: {} and Role: {}'.format(name[1].strip(), key_uid[1].strip(), role[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of the screen that adds a role.       
class AddRoleScreen(Screen):
    def addRole(self, name):
        name = name.split(":")
        
        db.addNewRole(name[1].strip())
        popup = Popup(title='Added Role',
                    content=Label(text='Succesfully added {} to Database'.format(name[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that adds a permission for a person.        
class AddPermPersScreen(Screen):
    def addPermPers(self, person_id, door_id):
        person_id = person_id.split(":")
        door_id = door_id.split(":")
        
        db.addNewPersonDoor(person_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Added Permission for Person',
                    content=Label(text='Succesfully added permission for door {} for person {} to Database'.format(door_id[1].strip(), person_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that adds a permission for a role.
class AddPermRoleScreen(Screen):
    def addPermRole(self, role_id, door_id):
        role_id = role_id.split(":")
        door_id = door_id.split(":")
        
        db.addNewRoleDoor(role_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Added Permission for Role',
                    content=Label(text='Succesfully added permission for door {} for role {} to Database'.format(door_id[1].strip(), role_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions for the removescreen.        
class RemoveScreen(Screen):
    pass

#Creates the functions of a screen that removes a person.    
class RemovePersonScreen(Screen):
    def removePerson(self, person_id):
        person_id = person_id.split(":")
        
        db.removeAllPermPers(person_id[1].strip())
        db.removePerson(person_id[1].strip())
        popup = Popup(title='Removed Person And Permissions',
                    content=Label(text='Succesfully removed Person {} from Database'.format(person_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that removes a role.        
class RemoveRoleScreen(Screen):
    def removeRole(self, role_id):
        role_id = role_id.split(":")
        
        db.removeAllPermRole(role_id[1].strip())
        db.removeRolePers(role_id[1].strip())
        db.removeRole(role_id[1].strip())
        popup = Popup(title='Removed Role And Permissions',
                    content=Label(text='Succesfully removed Role {} from Database'.format(role_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that removes a permission of a person.        
class RemovePermPersScreen(Screen):
    def removePermPers(self, person_id, door_id):
        person_id = person_id.split(":")
        door_id = door_id.split(":")
        
        db.removePermPers(person_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Removed Permission for Person',
                    content=Label(text='Succesfully removed permission for door {} for Person {} to Database'.format(door_id[1].strip(), person_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that removes a permission of a role.
class RemovePermRoleScreen(Screen):
    def removePermRole(self, role_id, door_id):
        role_id = role_id.split(":")
        door_id = door_id.split(":")
        
        db.removePermRole(role_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Removed Permission for Role',
                    content=Label(text='Succesfully removed permission for door {} for Role {} to Database'.format(door_id[1].strip(), role_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of the selectscreen.        
class SelectScreen(Screen):
    pass

#Creates the functions of the selectpersonscreen.    
class SelectPersonScreen(Screen):
    pass

#Creates the functions of a screen that selects a person by person_id.    
class SelectPersonIDScreen(Screen):
    def selectPersonID(self, person_id):
        person_id = person_id.split(":")
        
        person = db.getPerson(person_id[1].strip())
        popup = Popup(title = 'Results',
                    content=Label(text='ID: {}, Key_UID: {}\nName: {}, Role_ID: {}'.format(person["id"],person["key_uid"],person["name"],person["role_id"])),
                    size_hint=(None, None), size=(800, 200))
        popup.open()        

#Creates the functions of a screen that selects a person by key_uid. 
class SelectPersonKey_UIDScreen(Screen):
    def selectPersonKeyUID(self, key_uid):
        key_uid = key_uid.split(":")
        
        person = db.getPersonByUID(key_uid[1].strip())
        popup = Popup(title = 'Results',
                    content=Label(text='ID: {}, Key_UID: {}\nName: {}, Role_ID: {}'.format(person["id"],person["key_uid"],person["name"],person["role_id"])),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that selects a person by name. 
class SelectPersonNameScreen(Screen):
    def selectPersonName(self, name):
        name = name.split(":")
        
        person = db.getPersonByName(name[1].strip())
        popup = Popup(title = 'Results',
                    content=Label(text='ID: {}, Key_UID: {}\nName: {}, Role_ID: {}'.format(person["id"],person["key_uid"],person["name"],person["role_id"])),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

#Creates the functions of a screen that selects a person by role_id.
class SelectPersonRole_IDScreen(Screen):
    def selectPersonRole(self, role_id):
        role_id = role_id.split(":")
        
        persons = db.getPersonByRole(role_id[1].strip())
        string = ''
        
        for person in persons:
            string += 'ID: {}, Key_UID: {}\n-- Name: {}, Role_ID: {}\n'.format(person["id"],person["key_uid"],person["name"],person["role_id"])
        
        popup = Popup(title = 'Results',
                    content=Label(text=string),
                    size_hint=(None, None), size=(800, 400))
        popup.open()  

#Create the functions of the selectrolescreen.
class SelectRoleScreen(Screen):
    pass

#Creates the functions of a screen that selects a role by role_id.     
class SelectRoleIDScreen(Screen):
    def selectRoleID(self, role_id):
        role_id = role_id.split(":")
        
        role = db.getRole(role_id[1].strip())
        popup = Popup(title = 'Results',
                    content=Label(text='ID: {}, Name: {}'.format(role["id"],role["name"])),
                    size_hint=(None, None), size=(800, 200))
        popup.open()      

#Creates the functions of a screen that selects a role by name.     
class SelectRoleNameScreen(Screen):
    def selectRoleID(self, role_name):
        role_name = role_name.split(":")
        
        role = db.getRoleByName(role_name[1].strip())
        popup = Popup(title = 'Results',
                    content=Label(text='ID: {}, Name: {}'.format(role["id"],role["name"])),
                    size_hint=(None, None), size=(800, 200))
        popup.open() 

#Creates the functions of the selectdoorscreen.        
class SelectDoorScreen(Screen):
    pass

#Creates the functions of the selectpermpersscreen.    
class SelectPermPersScreen(Screen):
    pass

#Creates the functions of a screen that selects a permission of a person by person_id.     
class SelectPermPersPerson_IDScreen(Screen):
    def selectPermPersPersonID(self, person_id):
        person_id = person_id.split(":")
        
        perms = db.getPersonDoor(person_id[1].strip())
        string = "Person with ID: {} has access to doors:\n".format(person_id[1].strip())
        
        for perm in perms:
            string += "Door ID: {}\n".format(perm)
        
        popup = Popup(title = 'Results',
                    content=Label(text=string),
                    size_hint=(None, None), size=(800, 400))
        popup.open()  

#Creates the functions of a screen that selects a permission of a person by door_id.          
class SelectPermPersDoor_IDScreen(Screen):
    def selectPermPersDoorID(self, door_id):
        door_id = door_id.split(":")
        
        perms = db.getDoorPerson(door_id[1].strip())
        string = "Door with ID: {} can be accessed by:\n".format(door_id[1].strip())
        
        for perm in perms:
            string += "Person ID: {}\n".format(perm)
        
        popup = Popup(title = 'Results',
                    content=Label(text=string),
                    size_hint=(None, None), size=(800, 400))
        popup.open()

#Creates the functions of the selectpermrolescreen.        
class SelectPermRoleScreen(Screen):
    pass

#Creates the functions of a screen that selects a permission of a role by role_id.      
class SelectPermRoleRole_IDScreen(Screen):
    def selectPermRoleRoleID(self, role_id):
        role_id = role_id.split(":")
        
        perms = db.getRoleDoor(role_id[1].strip())
        string = "Role with ID: {} has access to doors:\n".format(role_id[1].strip())
        
        for perm in perms:
            string += "Door ID: {}\n".format(perm)
        
        popup = Popup(title = 'Results',
                    content=Label(text=string),
                    size_hint=(None, None), size=(800, 400))
        popup.open() 

#Creates the functions of a screen that selects a permission of a role by door_id.          
class SelectPermRoleDoor_IDScreen(Screen):
    def selectPermRoleDoorID(self, door_id):
        door_id = door_id.split(":")
        
        perms = db.getDoorRole(door_id[1].strip())
        string = "Door with ID: {} can be accessed by:\n".format(door_id[1].strip())
        
        for perm in perms:
            string += "Role ID: {}\n".format(perm)
        
        popup = Popup(title = 'Results',
                    content=Label(text=string),
                    size_hint=(None, None), size=(800, 400))
        popup.open()
    
# Create the screen manager
sm = ScreenManager(transition=NoTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AddScreen(name='add'))
sm.add_widget(AddPersonScreen(name='addPerson'))
sm.add_widget(AddRoleScreen(name='addRole'))
sm.add_widget(AddPermPersScreen(name='addPermPers'))
sm.add_widget(AddPermRoleScreen(name='addPermRole'))


sm.add_widget(RemoveScreen(name='remove'))
sm.add_widget(RemovePersonScreen(name='removePerson'))
sm.add_widget(RemoveRoleScreen(name='removeRole'))
sm.add_widget(RemovePermPersScreen(name='removePermPers'))
sm.add_widget(RemovePermRoleScreen(name='removePermRole'))


sm.add_widget(SelectScreen(name='select'))

sm.add_widget(SelectPersonScreen(name='selectPerson'))
sm.add_widget(SelectPersonIDScreen(name='selectPersonID'))
sm.add_widget(SelectPersonKey_UIDScreen(name='selectPersonKey_UID'))
sm.add_widget(SelectPersonNameScreen(name='selectPersonName'))
sm.add_widget(SelectPersonRole_IDScreen(name='selectPersonRole_ID'))

sm.add_widget(SelectRoleScreen(name='selectRole'))
sm.add_widget(SelectRoleIDScreen(name='selectRoleID'))
sm.add_widget(SelectRoleNameScreen(name='selectRoleName'))

sm.add_widget(SelectDoorScreen(name='selectDoor'))

sm.add_widget(SelectPermPersScreen(name='selectPermPers'))
sm.add_widget(SelectPermPersPerson_IDScreen(name='selectPermPersPerson_ID'))
sm.add_widget(SelectPermPersDoor_IDScreen(name='selectPermPersDoor_ID'))

sm.add_widget(SelectPermRoleScreen(name='selectPermRole'))
sm.add_widget(SelectPermRoleRole_IDScreen(name='selectPermRoleRole_ID'))
sm.add_widget(SelectPermRoleDoor_IDScreen(name='selectPermRoleDoor_ID'))

class DatabaseApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    DatabaseApp().run()