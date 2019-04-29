##
## I ran this then put the snippet in the template.html file
## and deleted snippets.html
##
style=lovelace
printf -v license '/* BSD-licensed. See: https://bitbucket.org/birkenfeld/pygments-main/src/default/pygments/styles/%s.py */' "${style}"
echo "${license}"

pygmentize -f html -o snippets.html snippets.xml
echo "${license}" >  static/pygment.css
pygmentize -S ${style}  -f html  >> static/pygment.css
