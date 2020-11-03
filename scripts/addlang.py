import gwadoc
import wn


lang = 'zh'
wnfile = '/home/bond/git/OMW/omw/resources/cmn/cmnwn.xml'

wn.add(wnfile)

doc = open(f'doc_{lang}.py', 'w')

def seed_docs(lang, doc, wn):
    """Print the fields to be added, and seed them if possible"""
    for relname in gwadoc.RELATIONS:
        relili = gwadoc.relations[relname].proj.ili or ''
        forms = []
        defs = []
        if relili and wn.synsets(ili=relili):
            ## normally only one
            for s in wn.synsets(ili=relili):
                if s.definition():
                    defs.append(definition)
                ## better to order by frequency if known (rarely known)
                for w in s.words():
                    for f in w.forms():
                        forms.append(f)
        
        print (f"""\n\n### {relname} {relili}\n""", file=doc)
        
        ### Name
        print (f'# relations.{relname}.name.{lang} = "{", ".join(forms)}"',
               file=doc)
            
        ### Short definition
        print (f'# relations.{relname}.df.{lang} = "{"; ".join(defs)}"',
               file=doc)

        ### Short example
        print (f'# relations.{relname}.ex.{lang} = ""',
               file=doc)





def print_header(lang, doc):
    print (f"""# -*- coding: utf-8 -*-
###
### Documentation for {lang}
###

# Pre-seeded by XXX on YYY
#
# Un-comment lines when you have checked them

from gwadoc import relations
""", file=doc)


print_header(lang, doc)
seed_docs(lang, doc, wn)
