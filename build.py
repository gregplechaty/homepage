### Site Generator created  1/24 ###

top = open("./templates/top.html").read()
bottom = open("./templates/bottom.html").read()
index = open("./content/index.html").read()
about = open("./content/about.html").read()
projects = open("./content/projects.html").read()
thoughts = open("./content/thoughts.html").read()

index_full = top + index + bottom
about_full = top + about + bottom
projects_full = top + projects + bottom
thoughts_full = top + thoughts + bottom

open("./docs/index.html", "w+").write(index_full)
open("./docs/about.html", "w+").write(about_full)
open("./docs/projects.html", "w+").write(projects_full)
open("./docs/thoughts.html", "w+").write(thoughts_full)

print('Site complete! Please review for accuracy.')
