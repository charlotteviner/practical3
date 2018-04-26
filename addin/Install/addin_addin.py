import arcpy
import pythonaddins

class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        object = pythonaddins.GPToolDialog("M:/Programming/practical1/albertsurface/Models.tbx", "ExplosionScript")
        hellocombobox.items = ["Hello"]
        
class HelloComboBoxClass(object):
    """Implementation for addin_addin.hellocombobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        pythonaddins.MessageBox("Hello world", "Hello")
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass