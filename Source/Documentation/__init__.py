""" Documentation package """

__version__ = "1.0.0"

import wx
import os.path, sys, urllib

_sharedFrame = None

runningFromSource = not hasattr(sys, "frozen")


def baseURL():
    if runningFromSource:
        basePath = os.path.join(wx.GetApp().rootDir, 'Documentation', 'build', 'Documentation')
    else:
        basePath = os.path.join(wx.GetApp().rootDir, 'Documentation')
    
    return 'file:' + urllib.pathname2url(basePath) + '/'


def showPage(page):
    pageURL = baseURL() + page

    # Try to open an embedded WebKit-based help browser. 
    try:
        import DocumentationFrame
        DocumentationFrame.showPage(pageURL)
    except:
        raise
        # Fall back to using the user's default browser outside of Neuroptikon.
        #wx.LaunchDefaultBrowser(pageURL)