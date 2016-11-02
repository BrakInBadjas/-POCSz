from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('db.kv')

# Declare both screens
class MenuScreen(Screen):
    pass

class RetrieveScreen(Screen):
	pass
	
class AddScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=NoTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(RetrieveScreen(name='retrieve'))
sm.add_widget(AddScreen(name='add'))

class dbApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    dbApp().run()