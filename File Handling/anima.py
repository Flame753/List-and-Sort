class Anima:
    def __init__(self, animaTitle):
        self.animaTitle = animaTitle
        self.season = 1
        self.episode = 12
        self.currentlyOnEpisode = 1

    # getter method for anima title
    def get_anima_title(self):
        return self.animaTitle

    # setter method for anima title
    def set_anima_title(self, title):
        self.animaTitle = title

    # getter method for season
    def get_season(self):
        return self.season

    # setter method for season
    def set_episode(self, season):
        self.season = season

    # getter method for episode
    def get_episode(self):
        return self.episode

    # setter method for episode
    def set_episode(self, episode):
        self.episode= episode

    # getter method for currently on
    def get_currently_on_episode(self):
        return self.currentlyOnEpisode

    # setter method for currently on
    def set_currently_on_episode(self, currentlyOn):
        self.currentlyOn = currentlyOn


