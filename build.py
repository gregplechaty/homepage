### Site Generator created  1/24 ###

#top = open("./templates/top.html").read()
bottom = open("./templates/bottom.html").read()
index = open("./content/index.html").read()
about = open("./content/about.html").read()
projects = open("./content/projects.html").read()
thoughts = open("./content/thoughts.html").read()


#trying variables
from string import Template

#index
top = Template(open("./templates/top.html").read())
top = top.safe_substitute(title='')
index_full = top + index + bottom

#about
top = Template(open("./templates/top.html").read())
top = top.safe_substitute(title=' - About')
about_full = top + about + bottom

#projects
top = Template(open("./templates/top.html").read())
top = top.safe_substitute(title=' - Projects')
projects_full = top + projects + bottom

#thoughts
top = Template(open("./templates/top.html").read())
top = top.safe_substitute(title=' - Thoughts')
thoughts_full = top + thoughts + bottom

open("./docs/index.html", "w+").write(index_full)
open("./docs/about.html", "w+").write(about_full)
open("./docs/projects.html", "w+").write(projects_full)
open("./docs/thoughts.html", "w+").write(thoughts_full)

print('Site complete! Please review for accuracy.')
