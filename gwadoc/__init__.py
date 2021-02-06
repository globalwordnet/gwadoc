# -*- coding: utf-8 -*-

from gwadoc.inventories import (
    PROJECTS,
    LANGUAGES,
    RELATIONS,
    PARTS,
    FORMAL_ATTRIBUTES
)
import gwadoc.base

relations = gwadoc.base.Relations(RELATIONS)


def set_preferred_language(lg):
    """
    Set the default language to *lg*.

    The preferred language determines which string is returned when a
    language is not specified. If a field is not defined for the
    preferred language, it backs off to English. For instance:

    >>> print(relations.hypernym.name.en)
    Hypernym
    >>> print(relations.hypernym.name.ja)
    上位語
    >>> print(relations.hypernym.name)
    Hypernym
    >>> gwadoc.set_preferred_language('ja')
    >>> print(relations.hypernym.name)
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
import gwadoc.doc_zh
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

for rel_id in RELATIONS:
    rel = relations[rel_id]
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
