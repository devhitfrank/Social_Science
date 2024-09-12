from loguru import logger
import os
import sys
sys.path.append('../agentscope-main/src')
from agentscope.memory import TemporaryMemory
class Team:
    def __init__(self, team_name):
        # attrs
        self.team_name = team_name
        self.state = 1
        self.teammate = []
        self.memory = TemporaryMemory(None)
        self.topic = None
        self.idea = None
        self.abstract = None
        self.citation_id = None
        self.self_review = None
        self.paper_review = None

        # init log file
        self.log_file = f"logs/{self.team_name}_dialogue.log"
        os.makedirs("logs", exist_ok=True)

        # Remove the default terminal handler
        logger.remove()

        # Check if log file exists and delete it
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

        logger.add(self.log_file, format="{message}", level="INFO")
        self.logger = logger.bind(team_name=self.team_name)

    def log_dialogue(self, name, content):
        self.logger.info(name + ':' + content)

if __name__=='__main__':
    team1 = Team('LPL')
    team1.state = 2
    team1.log_dialogue('sam', 'LPL win!')
    team1.log_dialogue('sam', f'{team1.state}')
