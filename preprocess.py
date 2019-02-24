from os import system, listdir
from os.path import join

system("rm txt/*")
system("rm fb2/*")

for author in listdir('zip'):
    for bookname in listdir(join('zip', author)):
        path = join('zip', author, bookname)
        system("unzip %s -d fb2" % path)


fnames = listdir('fb2')
for ind, fname in enumerate(fnames):
    system("unoconv -f txt fb2/%s" % fname)
    new_fname = fname[:-3] + "txt"
    system("mv fb2/%s txt/%s" % (new_fname, new_fname))
    print("converted", ind + 1, "out of", len(fnames))

system("cat txt/* >philosophy.txt")
