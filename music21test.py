from music21 import *
from collections import Counter

allBach = corpus.search('bach')
cnt = Counter()


for song in allBach:
    
    s = song.parse()    
    schords = s.flat.makeChords()
    for parts in schords:
        if type(parts) is chord.Chord:
            cnt[parts.pitchedCommonName] += 1


#print(cnt) -- To see all of them
print(cnt.most_common(10))
    
    
    


