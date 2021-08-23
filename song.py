class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        previous_songs = set()
        current = self
        while True:
            if (current.next == None):
                return False
            elif (current.next.name not in previous_songs):
                previous_songs.add(current.name)
                current = current.next
            else:
                return True
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())