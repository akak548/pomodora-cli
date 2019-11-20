from datetime import datetime
import errno
import json
import os
import uuid


class Session(object):
    def __init__(self, config_dir):

        self.config_dir = config_dir

        self.session_dir = f"{config_dir}/sessions"

        self.current_session = 'curr.json'

        self.start_time = datetime.now()

        self.session_id = datetime.now().strftime('%Y%m%d%H%M')

    def start(self):
        """
        Creates new session file
        """

        session_file = f"{self.session_dir}/{self.current_session}"

        # Check if session direct exists
        try:
            os.makedirs(self.session_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        # Check if session in progress
        if os.path.isfile(session_file):
            raise Exception("Pomo Session currently in progress...")

        data = json.dumps({
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat()
        })

        with open(session_file, 'w') as _session_file:
            _session_file.write(data)

    def done(self):
        """
        Completes session and renames file to session_id
        """
        pass

    def load(self, session_id=None):
        """
        Completes session and renames file to session_id
        """
        pass
