from flask import g
import time

class Logware:
    def __init__(self, app=None):
        self.app = app
    
    def init_app(self, app):

        @app.before_request
        def set_timer():
            g.request_start_time = time.time()
        
        @app.after_request
        def add_logger(response):
            pass