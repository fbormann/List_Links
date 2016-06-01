"""
This is the main file available to hold screens for LinkListener
"""

import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton
from kivy.storage.jsonstore import JsonStore

from kivy.uix.screenmanager import ScreenManager, Screen

#from kivy.garden.filebrowser import FileBrowser
#from kivy.garden.recycleview import RecycleView

"""
Screen available to add,remove and update a link to a list.
(Future Feature: maybe add a parameter field to it?)

fields:
	@novaurl = New URL written by the user to add to a list
"""

Builder.load_file("../design/main.kv")


class ListScreen(Screen):
	def __init__(self, **kwargs):
		self.load_data()
		self.store = JsonStore('folders.json')
		self.data  = []

		#Retrieve items from
		for item in self.store: 
			self.data.append(item)

		#bind the list to the UI
		self.folders_adapter = ListAdapter(data = self.data,
			cls = ListItemButton,
			selection_mode='single')


		
		super(ListScreen, self).__init__(**kwargs) 

		"""
		Tenho de colocar ao final senão o comando não funciona
		"""

	def add_folder(self, folder):
		self.data.append(folder) #data is being updated but GUI is not.
		self.folders_adapter.data = self.data #Update UI
		
		self.store[folder] = {}

	def add_item(self, item):
		self.data.append(item) #data is being updated but GUI is not.
		self.folders_adapter.data = self.data #Update UI
		
		self.store[item] = {'link': item}

	def load_data(self):
		pass


"""
ListSelectScreen :
	List of all folders/groups available to hold links


"""

class ListSelectScreen(Screen):
	def __init__(self, **kwargs):
		super(ListSelectScreen, self).__init__(**kwargs)



sm = ScreenManager()
sm.add_widget(ListScreen(name = 'Main_Menu'))
sm.add_widget(ListSelectScreen(name='Lista_Screen'))

class LinkListener(App):


	def build(self):
		#return ListScreen()
		return sm

if __name__ == '__main__':
    LinkListener().run()