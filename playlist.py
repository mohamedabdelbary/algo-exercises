from nose.tools import assert_equals


class PlaylistItem(object):
    def __init__(self, name):
        self._name = name
        self._next = None

    def add_item(self, item):
        self._next = item

    @property
    def next_(self):
        return self._next

    @property
    def name(self):
        return self._name


class PlayList(object):
    def __init__(self, song):
        self._head = song

    def add_song(self, song):
        curr = self._head
        last = curr
        while curr:
            last = curr
            curr = curr.next_

        last.add_item(song)

    def insert_song(self, song, index):
        curr = self._head
        i = 0
        while i < index - 1:
            if curr:
                curr = curr.next_
                i += 1

        tmp = curr.next_
        curr.add_item(song)
        song.add_item(tmp)

    def add_songs(self, songs):
        curr = self._head
        last = curr
        while curr:
            last = curr
            curr = curr.next_

        last.add_item(songs.head)

    def insert_songs(self, songs, index):
        curr = self._head
        i = 0
        while i < index - 1:
            if curr:
                curr = curr.next_
                i += 1

        tmp = curr.next_
        curr.add_item(songs.head)
        inserted_curr = songs.head
        last_inserted = inserted_curr
        while inserted_curr:
            last_inserted = inserted_curr
            inserted_curr = inserted_curr.next_

        last_inserted.add_item(tmp)

    @property
    def head(self):
        return self._head

    def items(self):
        items = []
        curr = self._head
        while curr:
            items.append(curr.name)
            curr = curr.next_

        return items


def main():
    playlist = PlayList(PlaylistItem("Bohemian Rhapsody"))
    playlist.add_song(PlaylistItem("We will rock you"))
    assert_equals(playlist.items(), ["Bohemian Rhapsody", "We will rock you"])
    playlist.insert_song(PlaylistItem("Be3eed 3annak"), 1)
    assert_equals(playlist.items(), ["Bohemian Rhapsody", "Be3eed 3annak", "We will rock you"])
    to_insert = PlayList(PlaylistItem("Stairway to Heaven"))
    to_insert.add_song(PlaylistItem("El leila di"))
    playlist.insert_songs(to_insert, 2)
    assert_equals(playlist.items(),
                  ["Bohemian Rhapsody", "Be3eed 3annak", "Stairway to Heaven", "El leila di", "We will rock you"])
    new = PlayList(PlaylistItem("dary remooshik"))
    new.add_song(PlaylistItem("leily nehary"))
    playlist.add_songs(new)
    assert_equals(playlist.items(),
                  ["Bohemian Rhapsody", "Be3eed 3annak", "Stairway to Heaven", "El leila di", "We will rock you", "dary remooshik", "leily nehary"])


if __name__ == '__main__':
    main()
