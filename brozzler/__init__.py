from brozzler.browser import Browser, BrowserPool
from brozzler.site import Page, Site
from brozzler.hq import BrozzlerHQ
from brozzler.worker import BrozzlerWorker

def _read_version():
    import os
    version_txt = os.path.sep.join(__file__.split(os.path.sep)[:-1] + ['version.txt'])
    with open(version_txt, 'rb') as fin:
        version_bytes = fin.read()
        return version_bytes.strip().decode('utf-8')

version = _read_version()

class ShutdownRequested(Exception):
    pass

# vim: set sw=4 et:
