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
		
		self.store = JsonStore('folders.json')
		self.data  = []

		#Retrieve items from the database
		for item in self.store: 
			self.data.append(item)

		#bind the list to the UI
		self.folders_adapter = ListAdapter(data = self.data,
			cls = ListItemButton,
			selection_mode='single')

		
		self.folders_adapter.bind(on_selection_change=self.selection_changed)
		super(ListScreen, self).__init__(**kwargs) 
		


		"""
		Tenho de colocar ao final senão o comando não funciona
		"""
	def move_to_list(self):
		if len(self.folders_adapter.selection) == 0: #So if no folder is selected, there is not way it will be used
			 print("Nenhum folder selecionado")
		else:
			"""
				Change screens on the data and pass the folder name as
				a parameter so that the screen only bring links to that
				Folder
			"""
			sm.get_screen("Lista_Screen").ids['folder_name'].text = self.folders_adapter.selection[0].text
			sm.direction = 'left'
			sm.current = "Lista_Screen"



	def add_folder(self, folder):
		self.data.append(folder) #data is being updated but GUI is not.
		
		self.update_UI_list()
		self.initialize_folder_database(folder)

	def update_UI_list(self):
		self.folders_adapter.data = self.data 

	def initialize_folder_database(self, folder):
		self.store[folder] = {}

	def add_item(self, item):
		self.data.append(item) #data is being updated but GUI is not.
		self.folders_adapter.data = self.data #Update UI
		
		self.store[item] = {'link': item}

		"""
		Remove the selected folder on GUI
		"""
	def delete_folder(self):
		folder_name = self.folders_adapter.selection[0].text
		self.store.delete(folder_name) #THE JSON IS UPDATED
		self.data.remove(folder_name) #THE BINDING IS UPDATED
		self.folders_adapter.data = self.data #UpdateUI"""

	def selection_changed(self, *args):
		"""print(' args when selection changes gets you the adapter', args)
		self.selected_item = args[0].selection[0].text
		print(self.selected_item)"""



"""
ListSelectScreen :
	List of all folders/groups available to hold links


"""

class ListSelectScreen(Screen):
	def __init__(self, **kwargs):
		
		self.store = JsonStore('folders.json')
		self.data  = []

		

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