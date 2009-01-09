import wx
from ObjectInspector import ObjectInspector
from GapJunction import GapJunction


class GapJunctionInspector( ObjectInspector ):
    
    def objectClass(self):
        return GapJunction
    
    
    def inspectObjects(self):
        
        # Lazily create our UI
        if not hasattr(self, ''):
#            self.GetSizer().Add(foo, 0, wx.EXPAND)
            self.GetSizer().Layout()
