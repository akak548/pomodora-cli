
class Config(object):
    def __init__(self):
        self.main_dir = '~/.config/pomo/' 

        self.file = 'pomo.yml' 

        self.report_dir = 'sessions' 

        self.options = {
            'slack_token': None,
            'slack_api_url': None
        }
    
    """
    Sets up config environment and files for Pomo

        - If exists, load options
    """
    def setup(self):
        pass

    """
    Loads options from config file
    """
    def _load_options(self):
        pass
    
