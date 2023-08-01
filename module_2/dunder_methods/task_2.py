class MusicPlayList:
    def __init__(self, name_of_the_group, name_of_the_track, duration):
        self.name_of_the_group = name_of_the_group
        self.name_of_the_track = name_of_the_track
        self.duration = duration

    def __str__(self):
        return f"\nThe name of the track: {self.name_of_the_track}\nThe name of the group: {self.name_of_the_group}"

    def __gt__(self, other):
        if self.duration > other.duration:
            return f"\nThe duration of the song '{self.name_of_the_track}' more," \
                   f" than duration of the song '{other.name_of_the_track}'"
        else:
            return f"\nThe duration of the song '{other.name_of_the_track}' more," \
                   f" than duration of the song '{self.name_of_the_track}'"

    def __eq__(self, other):
        if self.duration == other.duration:
            return f"\nThe duration of the songs: '{self.name_of_the_track}' and '{other.name_of_the_track}'" \
                   f" are the same"
        else:
            return f"\nThe duration of two songs: '{self.name_of_the_track}' and '{other.name_of_the_track}'" \
                   f" aren't the same"


first_track = MusicPlayList("Darude", "Sandstorm", 247)
second_track = MusicPlayList("Rammstein", "Ohne Dich", 360)

print(first_track.__str__())
print(second_track.__str__())
print(second_track.__gt__(first_track))
print(first_track.__gt__(second_track))
print(first_track.__eq__(second_track))
