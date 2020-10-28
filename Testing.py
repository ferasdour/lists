"""
So, here's the story. 

Within repl.it, I tried to make a team, the idea being to then import a private repo, such as from keybase. It wouldn't let me do private from github and issues pulling from keybase at the time of this creation. Will try again later. 

With that said, for anyone who see this, lets have some fun.
##################

I figure, covid is such a dangerous virus because it enables other viruses, such as colds, influenza, or bacterial problems like strep and pneumonia, to form and be unable to fight off those infections. Really the sars family is pretty trippy about this because they've always been sort of a concern of mutating. Whatever. Aaaanyway, what if we made a computer virus that enabled other viruses just so it could sit and wait? 
"""
"lets start off by just grabbing some viruses. >:D"
a=__import__('requests')
b=__import__('json')
c=__import__('pip')
c.main(['install','gitpython'])
d=__import__('git')
d.Git("./stuff/").clone("git://github.com/vxunderground/MalwareSourceCode.git")

"""
Before I run this, I just wanna say sorry for the repl.it people if they have alerts going off because of this. 
"""