from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Builder.load_file('db.kv')

class MenuScreen(Screen):
    pass

class AddScreen(Screen):
	pass
    
class AddPersonScreen(Screen):
    pass
    
class AddRoleScreen(Screen):
    pass
    
class AddPermPersScreen(Screen):
    pass

class AddPermRoleScreen(Screen):
    pass
    
class RemoveScreen(Screen):
    pass
    
class RemovePersonScreen(Screen):
    pass
    
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



class DatabaseApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    DatabaseApp().run()