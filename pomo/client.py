from . import Config

class Client(object):
    def __init__(self):

        self.config = Config()
        
    """
    Start Pomodora Session
    
    Args:
        - time: (int) Length of session in minutes
        - task: (str) Task or goal of session

    Return:
        - bool: True if session is complete

    Exception:
        - 
    """

    def start_session(self):
        pass

    """
    Initialize the pomo environment
    """
    def initialize(self):
        pass
    
    """
    Displays state of current session

    Return:
        - str: <session_id>/<time left>
    """
    def status(self):

