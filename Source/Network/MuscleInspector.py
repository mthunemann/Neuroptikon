import wx
from ObjectInspector import ObjectInspector
from Muscle import Muscle


class MuscleInspector( ObjectInspector ):
    
    @classmethod
    def objectClass(cls):
        return Muscle
