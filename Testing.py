"""
So, here's the story. 

Within repl.it, I tried to make a team, the idea being to then import a private repo, such as from keybase. It wouldn't let me do private from github and issues pulling from keybase at the time of this creation. Will try again later. 

With that said, for anyone who see this, lets have some fun.
##################

I figure, covid is such a dangerous virus because it enables other viruses, such as colds, influenza, or bacterial problems like strep and pneumonia, to form and be unable to fight off those infections. Really the sars family is pretty trippy about this because they've always been sort of a concern of mutating. Whatever. Aaaanyway, what if we made a computer virus that enabled other viruses just so it could sit and wait? 
"""
"lets start off by just grabbing some viruses. >:D"
import os
a=__import__('requests')
b=__import__('json')
c=__import__('pip')
c.main(['install','gitpython'])
c.main(['install','py7zr[zstd]'])
c.main(['install','angr'])
c.main(['install','ancypatch'])
d=__import__('git')
e=__import__('py7zr')
f=__import__('angr')
try:
  os.mkdir('stuff')
except:
  pass

def gitEvil():
 try:
   d.Git("./stuff/").clone("git://github.com/vxunderground/MalwareSourceCode.git")
 except:
   pass

def GetPoison():
 """
Before I run this, I just wanna say sorry for the repl.it people if they have alerts going off because of this. 

Okay well, it wouldn't let me commit with the cloned repo in it. That's okay. Still funny that it downloaded all that. 
 """
 open('TequilaQuilaPoisonInTheDarkness.7z','wb').write(a.get("https://vxug.fakedoma.in/samples/Exotic/TurlaGroup/TurlaGroupImplantsKazuar.7z").content)
 e.SevenZipFile('TequilaQuilaPoisonInTheDarkness.7z', mode='r').extractall(path="./stuff/")

def SimpleTests(filename):
  blarg=angr.Project(filename)
  arch=blarg.arch.name
  entrypoint=blarg.entry
  cfg = blarg.analyses.CFGFast()
  functions=cfg.kb.functions.items()
  