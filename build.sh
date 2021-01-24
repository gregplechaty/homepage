#gp workplan

#redirect each of four pages; top, content, bottom, into new file in "Docs"
#rewrite top so that the CSS reference is correct

echo Site Generator with Bash

cat templates/top.html content/index.html templates/bottom.html > docs/index.html
cat templates/top.html content/about.html templates/bottom.html > docs/about.html
cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html
cat templates/top.html content/thoughts.html templates/bottom.html > docs/thoughts.html

echo Site complete. Please review for accuracy.
