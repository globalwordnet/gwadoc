# -*- coding: utf-8 -*-

from gwadoc.inventories import (
    PROJECTS,
    LANGUAGES,
    RELATIONS,
    PARTS,
    FORMS
)
import gwadoc.base

rels = gwadoc.base.rels


def set_preferred_language(lg):
    """
    Set the default language to *lg*.

    The preferred language determines which string is returned when a
    language is not specified. If a field is not defined for the
    preferred language, it backs off to English. For instance:

    >>> print(rels.hypernym.name.en)
    Hypernym
    >>> print(rels.hypernym.name.ja)
    上位語
    >>> print(rels.hypernym.name)
    Hypernym
    >>> gwadoc.set_preferred_language('ja')
    >>> print(rels.hypernym.name)
    上位語
    """
    LANGUAGES[lg]  # check for KeyError
    gwadoc.base.preferred_language = lg


# Import these last to avoid potential import cycles

# import gwadoc.rels_basic to load general and project-level information
import gwadoc.rels_basic
# import language-specific modules to get names, definitions, etc.
import gwadoc.rels_en
import gwadoc.rels_pl
import gwadoc.rels_ja
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
    rel = rels[rel_id]
    for part in PARTS:
        if part == 'form':
            for form in FORMS:
                _cleanup(rel[part], form)
        elif part == 'proj':
            for proj in PROJECTS:
                _cleanup(rel[part], proj)
        else:
            for lg in LANGUAGES:
                _cleanup(rel[part], lg)
