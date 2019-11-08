import anima as anima

title = anima.Anima("hi")
season = title.get_season()
episode = title.get_episode()
currentlyOnEpisode = title.get_currently_on_episode()
seasonEpisodeTag = "Season {} / {} Episodes ".format(season, episode)
currentlyOn = "On Episode {}".format(currentlyOnEpisode)


def add_tags():
    return seasonEpisodeTag + currentlyOn


def file_name_with_file_type(fileName, typeFile=".txt"):
    return fileName + typeFile


fileName = file_name_with_file_type("Anima")
print(fileName)
print(title.get_anima_title())
print(add_tags())
