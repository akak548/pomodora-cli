import click
from .config import Config
from .session import Session
import os


class Client(object):

    def __init__(self):

        self.app_dir = "{}/.config/pomo".format(os.environ['HOME'])
        pass

    def start(self):
        """
        Start Pomodora Session
        """
        session = Session(self.app_dir)
        session.start()

    def check(self):
        """
        Displays state of current session
        """
        pass
