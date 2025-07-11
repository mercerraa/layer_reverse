"""
Layer Reverse
Copyright (C) 2025 Andrew Mercer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.core import Qgis
from qgis.core import QgsProject
from qgis.utils import iface
import os

class LayerReverse:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.toolbar = None

    def initGui(self):
        # The structure used here was suggested by ChatGPT but required many revisions to actually function
        # Set up button to run the plugin. Note that the path to the icon.png is a workaround as the path suggested by QGIS documentation did not work 
        self.action = QAction(QIcon(os.path.join( os.path.dirname(__file__), 'icon.png' )), "Reverse layer order", self.iface.mainWindow())
        self.action.triggered.connect(self.run_script)

        # Add the action to the toolbar
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Layer Reverse", self.action)

    def unload(self):
        # Remove the button and menu item when plugin is unloaded
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Layer Reverse", self.action)

    def run_script(self):
        # Get the Contents structure
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        selected = iface.layerTreeView().selectedLayers() # Create list of highlighted layers. Note that a list is always created even if it is empty
        # Loop through list of layers if that list contains elements
        if len(selected)>0:
            for layer in selected:
                node = root.findLayer(layer.id())
                if node:
                    parent = node.parent() # identify the containing element (group)
                    clone = node.clone() # clone the layer
                    parent.insertChildNode(0, clone) # place clone at the top, within the parent
                    parent.removeChildNode(node) # remove original
            iface.messageBar().pushMessage("Success", "Layer order reversed", level=Qgis.Success, duration=3)
        else:
            iface.messageBar().pushMessage("Warning", "No layers were highlighted", level=Qgis.Warning, duration=3)