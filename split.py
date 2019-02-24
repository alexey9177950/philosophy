txt = open("philosophy.txt").read()
open("ph1.txt", "w").write(txt[ : len(txt)//2])
open("ph2.txt", "w").write(txt[len(txt)//2 : ])
