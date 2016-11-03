from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import db

Builder.load_file('db.kv')

class MenuScreen(Screen):
    pass

class AddScreen(Screen):
	pass
    
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
    
class AddRoleScreen(Screen):
    def addRole(self, name):
        name = name.split(":")
        
        db.addNewRole(name[1].strip())
        popup = Popup(title='Added Role',
                    content=Label(text='Succesfully added {} to Database'.format(name[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()
    
class AddPermPersScreen(Screen):
    def addPermPers(self, person_id, door_id):
        person_id = person_id.split(":")
        door_id = door_id.split(":")
        
        db.addNewPersonDoor(person_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Added Permission for Person',
                    content=Label(text='Succesfully added permission for door {} for person {} to Database'.format(person_id[1].strip(), door_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()

class AddPermRoleScreen(Screen):
    def addPermRole(self, role_id, door_id):
        role_id = role_id.split(":")
        door_id = door_id.split(":")
        
        db.addNewRoleDoor(role_id[1].strip(), door_id[1].strip())
        popup = Popup(title='Added Permission for Role',
                    content=Label(text='Succesfully added permission for door {} for role {} to Database'.format(role_id[1].strip(), door_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()
    
class RemoveScreen(Screen):
    pass
    
class RemovePersonScreen(Screen):
    def removePerson(self, person_id):
        person_id = person_id.split(":")
        
        db.removeAllPermPers(person_id[1].strip())
        db.removePerson(person_id[1].strip())
        popup = Popup(title='Removed Person And Permissions',
                    content=Label(text='Succesfully removed Person {} from Database'.format(person_id[1].strip()), font_size=20),
                    size_hint=(None, None), size=(800, 200))
        popup.open()
    
class RemoveRoleScreen(Screen):
    pass
    
class RemovePermPersScreen(Screen):
    pass

class RemovePermRoleScreen(Screen):
    pass
    
class SelectScreen(Screen):
    pass
    
class SelectPersonScreen(Screen):
    pass
    
class SelectPersonIDScreen(Screen):
    pass

class SelectPersonKey_UIDScreen(Screen):
    pass

class SelectPersonNameScreen(Screen):
    pass

class SelectPersonRole_IDScreen(Screen):
    pass    

class SelectRoleScreen(Screen):
    pass
    
class SelectRoleIDScreen(Screen):
    pass
    
class SelectRoleNameScreen(Screen):
    pass
    
class SelectDoorScreen(Screen):
    pass
    
class SelectPermPersScreen(Screen):
    pass
    
class SelectPermPersPerson_IDScreen(Screen):
    pass
    
class SelectPermPersDoor_IDScreen(Screen):
    pass
    
class SelectPermRoleScreen(Screen):
    pass
    
class SelectPermRoleRole_IDScreen(Screen):
    pass
    
class SelectPermRoleDoor_IDScreen(Screen):
    pass
    
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