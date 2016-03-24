song = "Somewhere over the rainbow"

needle = "o"

pos = song.find(needle)
print pos
pos = song.find(needle, pos + 1)
print pos
pos = song.find(needle, pos + 1)
print pos