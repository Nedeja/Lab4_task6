from menu import Menu
from notebook import Notebook, Note

objects = []
for i in dir(Menu):
    if isinstance(i, object) == True:
        objects.append(i)
print('These are objects of class Menu:', objects)
objects_note = []
for j in dir(Note):
    if isinstance(j, object) == True:
        objects_note.append(j)
print('These are objects of class Note:', objects_note)
objects_notebook = []
for l in dir(Notebook):
    if isinstance(l, object) == True:
        objects_notebook.append(l)
print('These are objects of class Notebook:', objects_notebook)