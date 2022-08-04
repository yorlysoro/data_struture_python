import time


class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            return 0
        data = self.items.pop()
        self.size -= 1
        return data


class MusicPlaylist(ListQueue):
    def __init__(self):
        super().__init__()

    def add_songs(self, song: tuple):
        self.enqueue(song)

    def play_song(self):
        song = self.dequeue()
        if song:
            print(f'Playing: {song[0]} for {song[1]} min')
            time.sleep(song[1])
        else:
            print('There are no more songs')

    def play_songs(self):
        while self.items:
            self.play_song()

    def all_songs(self):
        if self.items:
            print('The songs in the playlist are:')
            for i, song in enumerate(self.items[::-1],start=1):
                print(f'Song {i}: {song[0]}, Time: {song[1]}')
        print(f'There are {self.size} songs')
        return self.size


if __name__ == '__main__':
    playlist = MusicPlaylist()

    playlist.add_songs(("REMEMBER", 5.19))
    playlist.add_songs(("comfy vibes", 3.12))
    playlist.add_songs(("Into the blue's", 4.03))
    playlist.add_songs(("E.M.A", 4.16))

    playlist.all_songs()
    print()

    playlist.play_songs()
    print()

    playlist.play_song()
    playlist.all_songs()
