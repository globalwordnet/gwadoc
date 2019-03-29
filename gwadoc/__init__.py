# -*- coding: utf-8 -*-

from gwadoc.inventories import (
    PROJECTS,
    LANGUAGES,
    SENSE_RELATIONS,
    SYNSET_RELATIONS,
    PARTS,
    FORMAL_ATTRIBUTES
)
import gwadoc.base

sense_rels = gwadoc.base.Relations(SENSE_RELATIONS)
synset_rels = gwadoc.base.Relations(SYNSET_RELATIONS)


def set_preferred_language(lg):
    """
    Set the default language to *lg*.

    The preferred language determines which string is returned when a
    language is not specified. If a field is not defined for the
    preferred language, it backs off to English. For instance:

    >>> print(synset_rels.hypernym.name.en)
    Hypernym
    >>> print(synset_rels.hypernym.name.ja)
    上位語
    >>> print(synset_rels.hypernym.name)
    Hypernym
    >>> gwadoc.set_preferred_language('ja')
    >>> print(synset_rels.hypernym.name)
    上位語
    """
    LANGUAGES[lg]  # check for KeyError
    gwadoc.base.preferred_language = lg


# Import these last to avoid potential import cycles

# import gwadoc.doc_basic to load general and project-level information
import gwadoc.doc_basic
# import language-specific modules to get names, definitions, etc.
import gwadoc.doc_en
import gwadoc.doc_pl
import gwadoc.doc_ja
# add your language module here


### CLEAN UP

import textwrap

def _cleanup(obj, key):
    s = obj.get(key)
    if isinstance(s, str):
        if s.strip() == '':
            obj[key] = ''
        else:
            obj[key] = textwrap.dedent(obj[key].strip('\n'))

for rel_id in SYNSET_RELATIONS:
    rel = synset_rels[rel_id]
    for part in PARTS:
        if part == 'fa':
            for fa in FORMAL_ATTRIBUTES:
                _cleanup(rel[part], fa)
        elif part == 'proj':
            for proj in PROJECTS:
                _cleanup(rel[part], proj)
        else:
            for lg in LANGUAGES:
                _cleanup(rel[part], lg)
