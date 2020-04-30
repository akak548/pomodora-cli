from datetime import datetime
import functools
import errno
import json
import os
import uuid


class Session(object):
    def __init__(self, config_dir):

        self.config_dir = config_dir

        self._data = {}

    @property
    def session_dir(self):
        return f"{self.config_dir}/sessions"

    @property
    def session_id(self):
        try:
            return self._data['session_id']
        except KeyError:
            return self.start_time.strftime('%Y%m%d%H%M')

    @property
    def session_file(self):
        try:
            return f"{self.session_dir}/{self._data['session_id']}.json"
        except KeyError:
            return f"{self.session_dir}/curr.json"

    @property
    def session_length(self):
        try:
            return self._data['session_length']
        except KeyError:
            return "25m"
    @property
    def start_time(self):
        try:
            return self._data['start_time']
        except KeyError:
            return datetime.now()

    def start(self):
        """
        Creates new session file
        """

        # Check if session direct exists
        try:
            os.makedirs(self.session_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        # Check if session in progress
        if os.path.isfile(self.session_file):
            raise Exception("Pomo Session currently in progress...")

        data = json.dumps({
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat(),
            "session_length": self.session_length
        })

        with open(self.session_file, 'w') as fp:
            fp.write(data)

    def load(self, curr=True):
        """
        Completes session and renames file to session_id
        """

        if curr:
            with open(self.curr_session_file, 'r') as fp:
                data = json.load(fp)

        pass
