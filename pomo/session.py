import uuid
import yaml

class Session(object):
    def __init__(self, session_dir, session_id, start_time):
        self.session_id = session_id

        self.session_dir = session_dir

        self.curr_session = 'curr.yml' 

        self.start_time = start_time
   
    """
    Creates new session file
    """
    def new(object):
        pass

    """
    Completes session and renames file to session_id
    """
    def done(object):

