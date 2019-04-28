##
## I ran this then put the snippet in the template.html file
## and deleted snippets.html
##

pygmentize -f html -o snippets.html snippets.xml
pygmentize -S lovelace  -f html  > static/pygment.css
