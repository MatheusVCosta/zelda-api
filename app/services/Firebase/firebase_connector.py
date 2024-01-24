import pyrebase

from app.config.config import get_settings

class FirebaseConnector: 
    
    def saveObject():
        pyrebase.initialize_app(get_settings)
    