# -*- coding: utf-8 -*-

from collections import OrderedDict as od
from collections import namedtuple


preferred_language = 'en'
backup_language = 'en'

###############################################################################
### Inventories

PROJECTS = od([
    ('pwn', 'Princeton WordNet Relation Name'),
    ('pointer', 'Princeton WordNet Pointer'),
    ('eurown', 'Euro WordNet Relation Name'),
    ('plwordnet', 'PlWordNet Relation Name'),
    ('querywn', 'PERL WordNet-QueryData Module'),
    ('skos', 'SKOS type'),
    ('ili', 'Interlingual Index Node'),
    ('SUMO', 'Sumo Relation Type'),
])


LANGUAGES = od([
    ('en', 'English'),
    ('pl', 'Polish'),
    ('ja', 'Japanese'),
    ('symbol', 'Symbol'),
])


RELATIONS = (
    'constitutive',
    'hyponym',
    'hypernym',
    'instance_hyponym',
    'instance_hypernym',
    'antonym',
    'eq_synonym',
    'similar',
    'meronym',
    'holonym',
    'mero_location',
    'holo_location',
    'mero_member',
    'holo_member',
    'mero_part',
    'holo_part',
    'mero_portion',
    'holo_portion',
    'mero_substance',
    'holo_substance',
    'other',
    'also',
    'state_of',
    'be_in_state',
    'causes',
    'is_caused_by',
    'subevent',
    'is_subevent_of',
    'manner_of',
    'in_manner',
    'attribute',
    'restricts',
    'restricted_by',
    'classifies',
    'classified_by',
    'entails',
    'is_entailed_by',
    'domain',
    'has_domain',
    'domain_topic',
    'has_domain_topic',
    'domain_region',
    'has_domain_region',
    'exemplifies',
    'is_exemplified_by',
    'role',
    'involved',
    'agent',
    'involved_agent',
    'patient',
    'involved_patient',
    'result',
    'involved_result',
    'instrument',
    'involved_instrument',
    'location',
    'involved_location',
    'direction',
    'involved_direction',
    'target_direction',
    'involved_target_direction',
    'source_direction',
    'involved_source_direction',
    'co_role',
    'co_agent_patient',
    'co_patient_agent',
    'co_agent_instrument',
    'co_instrument_agent',
    'co_agent_result',
    'co_result_agent',
    'co_patient_instrument',
    'co_instrument_patient',
    'co_result_instrument',
    'co_instrument_result',
)

PARTS = {
    'com': 'Comments',
    'df': 'Short Definition',
    'dfn': 'Long Definition',
    'ex': 'Short Example',
    'exe': 'Long Examples',
    'form': '',
    'name': 'Relation Name',
    'proj': 'Relation Name in Project',
    'test': 'Tests',
}


FORMS = {
    'reverse': 'Reverse Relation',
    'constitutive': 'Constitutive Relation',
    'inOMW': 'Relation used in OMW'
}


###############################################################################
### Data Structures

class AttrBase(dict):

    _inventory = set()

    def __getitem__(self, key):
        if key not in self._inventory:
            raise KeyError("'{}' is not defined".format(key))
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        if key not in self._inventory:
            raise KeyError("'{}' is not defined".format(key))
        dict.__setitem__(self, key, value)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'{}' is not defined".format(key))

    def __setattr__(self, key, value):
        try:
            self[key] = value
        except KeyError:
            raise AttributeError("'{}' is not defined".format(key))

    def keys(self):
        return self._inventory

    def __bool__(self):
        return any(self.get(key) is not None for key in self._inventory)


class MultiString(AttrBase):

    _inventory = LANGUAGES

    def __repr__(self):
        return '<MultiString ({!s})>'.format(self)

    def __str__(self):
        return self.get(preferred_language, self.get(backup_language, ''))

    def __len__(self):
        return len(str(self))


class Forms(AttrBase):

    _inventory = FORMS

    def __init__(self):
        for form in self._inventory:
            setattr(self, form, None)


class Projects(AttrBase):

    _inventory = PROJECTS

    def __init__(self):
        for proj in self._inventory:
            setattr(self, proj, None)


class Parts(AttrBase):

    _inventory = PARTS

    def __init__(self):
        self.com = MultiString()
        self.df = MultiString()
        self.dfn = MultiString()
        self.ex = MultiString()
        self.exe = MultiString()
        self.form = Forms()
        self.name = MultiString()
        self.proj = Projects()
        self.test = MultiString()


class Relations(AttrBase):

    _inventory = set(RELATIONS)

    def __init__(self):
        for rel in self._inventory:
            setattr(self, rel, Parts())


rels = Relations()


###############################################################################
### Relations Definitions

# rels[rel]['name'][lg]
# name of the relation in language 'lg'
# should always have English
# lg = 'symbol' for Unicode single character symbol

# rels[rel]['proj'][proj] name used in other projects
# 'pointer' for PWN pointer
# http://wordnet.princeton.edu/wordnet/man/wninput.5WN.html
# '4char' for query-wordnet character name
# 'ili' for closest ili node

# rels[rel]['df'][lg]
# short definition in a lang, suitable for mouseover in a tool,
#  or short table

# rels[rel]['dfn'][lg]  long definition

# rels[rel]['ex'][lg]   short example
# rels[rel]['exe'][lg]    long example
# rels[rel]['test'][lg]   tests (and discussion)
# rels[rel]['com'][lg]    comments


### Relation: domain

rels.domain.name.en = "Domain"
rels.domain.form.reverse = 'has_domain'


### Relation: has_domain

rels.has_domain.name.en = "In Domain"


### Relation: constitutive

rels.constitutive.name.en = "Constitutive"
rels.constitutive.df.en = "Core semantic relations that define synsets"
rels.constitutive.dfn.en = """
Core semantic relations that define synsets.

We follow the discussion in [Maziarz:Piasecki:Szpakowicz:2013]_

.. [Maziarz:Piasecki:Szpakowicz:2013] The chicken-and-egg problem in
   wordnet design: synonymy, synsets and constitutive relations.
   Language Resources and Evaluation, 47(3), pp 769–79
"""


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

rels.hypernym.name.symbol = "⊃"

rels.hypernym.form.constitutive = True
rels.hypernym.form.inOMW = True
rels.hypernym.form.reverse = "hyponym"

rels.hypernym.proj.ili = """i69569"""
rels.hypernym.proj.querywn = "hype"
rels.hypernym.proj.eurown = """HAS_HYPONYM"""
rels.hypernym.proj.plwordnet = "hyperonymy"
rels.hypernym.proj.pointer = "@"

rels.hypernym.name.en = 'Hypernym'
rels.hypernym.df.en = 'a word that is more general than a given word'
rels.hypernym.dfn.en = """
A hypernym of something is its superordinate term:
if X is a hypernym of Y, then all Y are X.
"""
rels.hypernym.ex.en = "*animal* is a hypernym of *dog*"
rels.hypernym.exe.en = """
 * *meat* ``hypernym`` *beef*
 * *edible fruit* ``hypernym`` *pear*
 * *wordbook* ``hypernym`` *dictionary*
"""
rels.hypernym.test.en = """
Hyperonymy/hyponymy between verb synsets (EWN test 11)

===     =   ===================================
yes     a   *to X is to Y + AdvP/AdjP/NP/PP*
no      b   *to Y is to X + AdvP/AdjP/NP/PP*
===     =   ===================================

Conditions:
 - X is a verb in the infinitive form
 - Y is a verb in the infinitive form
 - there is at least one specifying modifier (AdvP, NP or PP) that
   applies to the Y-phrase
"""
rels.hypernym.com.en="""
This is the fundamental relation, generally used for nouns and
verbs. In the original Princeton WordNet the name 'troponym' was used
for this relation when relating to verbs. In plWordNet it is also
extended to adjectives and adverbs.
"""

rels.hypernym.df.pl="""
Relacja łącząca znaczenie z drugim, ogólniejszym, niż to pierwsze, ale
należącym do tej samej części mowy, co ono
"""

rels.hypernym.name.ja="上位語"
rels.hypernym.dfn.ja="当該synsetが相手synsetに包含される"
rels.hypernym.ex.ja="動物は犬の上位語"


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

rels.hyponym.name.symbol = "⊂"

rels.hyponym.form.constitutive = True
rels.hyponym.form.inOMW = True
rels.hyponym.form.reverse = "hypernym"

rels.hyponym.proj.ili = "i69570"
rels.hyponym.proj.pwn = "hyponym"
rels.hyponym.proj.querywn = "hypo"
rels.hyponym.proj.eurown = "HAS_HYPERONYM"
rels.hyponym.proj.plwordnet = "hyponymy"
rels.hyponym.proj.pointer = "~"

rels.hyponym.name.en = "Hyponym"
rels.hyponym.df.en = "a word that is more specific than a given word"
rels.hyponym.dfn.en = """
A relation between two concepts where concept B is a type of
concept A."""
rels.hyponym.ex.en = "*dog* is a hyponym of *animal*"
rels.hyponym.exe.en = """
 * *beef* ``hyponym`` *meat*
 * *pear* ``hyponym`` *edible fruit*
 * *dictionary* ``hyponym`` *wordbook*
"""
rels.hyponym.test.en="""
Hyponymy-relation between nouns (EWN test 9)

===     =   ==========================================
yes     a   *A/an X is a/an Y with certain properties*
.       .   *It is a X and therefore also a Y*
.       .   *If it is a X then it must be a Y*
no      b   the converse of any of the (a) sentences.
===     =   ==========================================

Conditions:
 - both X and Y are singular nouns or plural nouns.

Hyperonymy/hyponymy between verb synsets (EWN test 11)

===     =   ===================================
yes     a   *to X is to Y + AdvP/AdjP/NP/PP*
no      b   *to Y is to X + AdvP/AdjP/NP/PP*
===     =   ===================================

Conditions:
 - X is a verb in the infinitive form
 - Y is a verb in the infinitive form
 - there is at least one specifying AdvP, NP or PP that applies to the
   Y-phrase.

"""
rels.hyponym.com.en = """
This is the fundamental relation, generally used for nouns and
verbs. In plWordNet it is also extended to adjectives and adverbs.
"""


### Relation: similar

rels.similar.form.inOMW = True
rels.similar.form.reverse = "similar"

rels.similar.proj.ili = "i13187"
rels.similar.proj.pwn = "Similar to and Verb Group"
rels.similar.proj.querywn = "sim"
rels.similar.proj.eurown = "near_synonym"
rels.similar.proj.plwordnet = "near_synonymy"
rels.similar.proj.pointer = "&"

rels.similar.name.en = "Similar"
rels.similar.df.en = "(of words) expressing closely related meanings"
rels.similar.dfn.en = """
A relation between two concepts where concept X and concept Y are
closely related in meaning but are not in the same synset. Similarity
is a self-reciprocal link (the two directions of this relation share
the same meaning) — Concept-X is similar to Concept-Y, and Concept-Y
is similar to Concept-X.

This link was originally used to relate adjectives, but we have
unconstrained this use, and we're making use of this link to relate
all parts-of-speech.

Similarity can be understood as weak synonymy, opposed to the full
synonymy that all lemmas in a concept must share.  As adjectives are
not structured hierarchically (hyponymy/hypernymy) like verbs or
nouns, the similarity link helps showing relations between them.
"""
rels.similar.ex.en = ""
rels.similar.exe.en = """
"""
rels.similar.com.en = """
This relation coerces PWN Similar to relation for adjectives, Verb
Group relation for verbs and EWN NEAR_SYNONYM for nouns and verbs. In
plWN Similarity relation for adjectives to nouns is a unilateral sense
relation which is why it is not given in the mappings below.
"""


### Relation: role

rels.role.form.inOMW = True
rels.role.form.reverse = "involved"

rels.role.proj.ili = "i64041"
rels.role.proj.eurown = "role"
rels.role.proj.plwordnet = "role_unspecified subtype and role_time"
rels.role.proj.pointer = ""

rels.role.name.en = "Role"
rels.role.df.en = "what something is used for"
rels.role.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
involved in the action or event expressed by concept Y. It is the
supertype of ``agent``, ``instrument``, ``patient``, ``result``,
``location``, ``direction``, ``target_direction``, and
``source_direction``.
"""
rels.role.ex.en = ""
rels.role.exe.en = """
* *hammer* ``role`` *to hammer*
"""
rels.role.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: agent

rels.agent.form.inOMW = True
rels.agent.form.reverse = "involved_agent"

rels.agent.proj.ili = "i69754"
rels.agent.proj.eurown = "role_agent"
rels.agent.proj.plwordnet = "role_agent"
rels.agent.proj.pointer = ""

rels.agent.name.en = "Agent"
rels.agent.df.en = """
the semantic role of the animate entity that instigates or causes the
happening denoted by the verb in the clause
"""
rels.agent.dfn.en = """
X Role Y: (A/an) X is the one/that who/which does the Y, typically
intentionally. X is typically the agent of the action expressed by Y
"""
rels.agent.ex.en = ""
rels.agent.exe.en = """
* *teacher* ``agent`` *to teach*
"""
rels.agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: patient

rels.patient.form.inOMW = True
rels.patient.form.reverse = "involved_patient"

rels.patient.proj.ili = "i69753"
rels.patient.proj.eurown = "role_patient"
rels.patient.proj.plwordnet = "role_patient"
rels.patient.proj.pointer = ""

rels.patient.name.en = "Patient"
rels.patient.df.en = """
the semantic role of an entity that is not the agent but is directly
involved in or affected by the happening denoted by the verb in the
clause
"""
rels.patient.dfn.en = """
X Role Y: (A/an) X is the one/that who/which undergoes the Y.
"""
rels.patient.ex.en = ""
rels.patient.exe.en = """
* *learner* ``patient`` *to learn*
"""
rels.patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: result

rels.result.form.inOMW = True
rels.result.form.reverse = "involved_result"

rels.result.proj.ili = "i69759"
rels.result.proj.eurown = "role_result"
rels.result.proj.plwordnet = "role_result"
rels.result.proj.pointer = ""

rels.result.name.en = "Result"
rels.result.df.en = """
the semantic role of the noun phrase whose referent exists only by
virtue of the activity denoted by the verb in the clause
"""
rels.result.dfn.en = """
X Role Y: (A/an) X is comes into existence as a result of Y or, (A/an)
X is the result of Y or, (A/an) X is created by Y.
"""
rels.result.ex.en = ""
rels.result.exe.en = """
* *crystal* ``result`` *to crystalize*
"""
rels.result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: instrument

rels.instrument.form.inOMW = True
rels.instrument.form.reverse = "involved_instrument"

rels.instrument.proj.ili = "i69756"
rels.instrument.proj.eurown = "role_instrument"
rels.instrument.proj.plwordnet = "role_instrument"
rels.instrument.proj.pointer = ""

rels.instrument.name.en = "Instrument"
rels.instrument.df.en = """
the semantic role of the entity (usually inanimate) that the agent
uses to perform an action or start a process
"""
rels.instrument.dfn.en = """
X Role Y: (A/an) X is either i) the instrument that or ii) what is
used to Y (with)
"""
rels.instrument.ex.en = ""
rels.instrument.exe.en = """
* *hammer* ``instrument`` *to hammer*
* *sail* ``instrument`` *to sail*
* *pen* ``instrument`` *to write*
* *ink* ``instrument`` *to write*
* *paper* ``instrument`` *to write*
"""
rels.instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: location

rels.location.form.inOMW = True
rels.location.form.reverse = "involved_location"

rels.location.proj.ili = "i35580"
rels.location.proj.eurown = "role_location"
rels.location.proj.plwordnet = "role_location"
rels.location.proj.pointer = ""

rels.location.name.en = "Location"
rels.location.df.en = "a point or extent in space"
rels.location.dfn.en = """
X Role Y: A relation between two concepts where concept X is the
location where the action or event expressed by concept Y takes place.
"""
rels.location.ex.en = ""
rels.location.exe.en = """
* *school* ``location`` *to teach*
"""
rels.location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: direction

rels.direction.form.inOMW = True
rels.direction.form.reverse = "involved_direction"

rels.direction.proj.ili = "i82556"
rels.direction.proj.eurown = "role_direction"
rels.direction.proj.plwordnet = ""
rels.direction.proj.pointer = ""

rels.direction.name.en = "Direction"
rels.direction.df.en = """
a line leading to a place or point
"""
rels.direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
the direction or location of the action or event expressed by concept
Y. It is possible to Y from/to/over/across/through a place (X)
"""
rels.direction.ex.en = ""
rels.direction.exe.en = """
* *place* ``direction`` *pass*
"""
rels.direction.com.en = """
"""


### Relation: target_direction

rels.target_direction.form.inOMW = True
rels.target_direction.form.reverse = "involved_target_direction"

rels.target_direction.proj.ili = "i82007" ###(ili doesn't have target in it)
rels.target_direction.proj.eurown = "role_target_direction"
rels.target_direction.proj.plwordnet = ""
rels.target_direction.proj.pointer = ""

rels.target_direction.name.en = "Target Direction"
rels.target_direction.df.en = """
the place designated as the end (as of a race or journey)
"""
rels.target_direction.dfn.en = """
X Role Y: (a/an/the) X is the place to which Ying happens / one Ys
"""
rels.target_direction.ex.en = ""
rels.target_direction.exe.en = """
* *ground* ``target_direction`` *to collapse, to fall heavily*
"""
rels.target_direction.com.en = """
"""


### Relation: source_direction

rels.source_direction.form.inOMW = True
rels.source_direction.form.reverse = "involved_source_direction"

rels.source_direction.proj.ili = "i81759"
rels.source_direction.proj.eurown = "role_source_direction"
rels.source_direction.proj.plwordnet = ""
rels.source_direction.proj.pointer = ""

rels.source_direction.name.en = "Source Direction"
rels.source_direction.df.en = """
the place where something begins, where it springs into being
"""
rels.source_direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is the place
from where the action or event expressed by concept Y
begins/starts/happens.
"""
rels.source_direction.ex.en = "start/race"
rels.source_direction.exe.en = """
* *the start* ``source_direction`` *to race*
"""
rels.source_direction.com.en = """
"""


### Relation: involved

rels.involved.form.inOMW = True
rels.involved.form.reverse = "role"

rels.involved.proj.ili = "i8315"
rels.involved.proj.eurown = "involved"
rels.involved.proj.plwordnet = "unspecified subtype, time and causation inclusion"
rels.involved.proj.pointer = ""

rels.involved.name.en = "Involved"
rels.involved.df.en = "connected by participation or association or use"
rels.involved.dfn.en = """
Y involved X: A relation between two concepts where concept Y is
typically involved in the action or event expressed by concept
X. Involved is the supertype of ``involved_agent``,
``involved_patient``, ``involved_result``, ``involved_instrument``,
``involved_location``, ``involved_direction``,
``involved_target_direction``, and ``involved_source_direction``.
"""
rels.involved.ex.en = ""
rels.involved.exe.en = """
* *to hammer* ``involved`` *hammer*
"""
rels.involved.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_agent (EuroWordNet - page 29/30)

rels.involved_agent.form.inOMW = True
rels.involved_agent.form.reverse = "agent"

rels.involved_agent.proj.eurown = "involved_agent"
rels.involved_agent.proj.plwordnet = "agent inclusion"
rels.involved_agent.proj.pointer = ""

rels.involved_agent.name.en = "Involved Agent"
rels.involved_agent.df.en = "X is the typical agent of Y"
rels.involved_agent.dfn.en = """
Y involved X: A relation between two concepts where concept Y is typically
the agent of the action expressed by concept X.
"""
rels.involved_agent.ex.en = "teach/teacher"
rels.involved_agent.exe.en = """
* *to teach* ``involved_agent`` *teacher*
"""
rels.involved_agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_patient

rels.involved_patient.form.inOMW = True
rels.involved_patient.form.reverse = "patient"

rels.involved_patient.proj.eurown = "involved_patient"
rels.involved_patient.proj.plwordnet = "patient inclusion"
rels.involved_patient.proj.pointer = ""

rels.involved_patient.name.en = "Involved Patient"
rels.involved_patient.df.en = "X is typically the patient undergoing the action Y"
rels.involved_patient.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the patient undergoing an action or event expressed by
concept A.
"""
rels.involved_patient.ex.en = "teach/learner"
rels.involved_patient.exe.en = """
"""
rels.involved_patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_result

rels.involved_result.form.inOMW = True
rels.involved_result.form.reverse = "result"

rels.involved_result.proj.eurown = "involved_result"
rels.involved_result.proj.plwordnet = "result inclusion"
rels.involved_result.proj.pointer = ""

rels.involved_result.name.en = "Involved Result"
rels.involved_result.df.en = "X exists because of Y"
rels.involved_result.dfn.en = """
Y involved X: A relation between two concepts where concept B comes
into existence as a result of concept A.
"""
rels.involved_result.ex.en = "freeze/ice"
rels.involved_result.exe.en = """
"""
rels.involved_result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_instrument

rels.involved_instrument.form.inOMW = True
rels.involved_instrument.form.reverse = "instrument"

rels.involved_instrument.proj.eurown = "involved_instrument"
rels.involved_instrument.proj.plwordnet = "instrument inclusion"
rels.involved_instrument.proj.pointer = ""

rels.involved_instrument.name.en = "Involved Instrument"
rels.involved_instrument.df.en = "X is typically the instrument for the action Y"
rels.involved_instrument.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the instrument necessary for the action or event expressed
by concept A.
"""
rels.involved_instrument.ex.en = "paint/paint-brush"
rels.involved_instrument.exe.en = """
"""
rels.involved_instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_location

rels.involved_location.form.inOMW = True
rels.involved_location.form.reverse = "location"

rels.involved_location.proj.eurown = "involved_location"
rels.involved_location.proj.plwordnet = "location inclusion"
rels.involved_location.proj.pointer = ""

rels.involved_location.name.en = "Involved Location"
rels.involved_location.df.en = """
X is typically the location where the action Y takes place
"""
rels.involved_location.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the location where the action or event expressed by concept
A takes place.
"""
rels.involved_location.ex.en = "swim/water"
rels.involved_location.exe.en = """
"""
rels.involved_location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_direction

rels.involved_direction.form.inOMW = True
rels.involved_direction.form.reverse = "direction"

rels.involved_direction.proj.eurown = "involved_direction"
rels.involved_direction.proj.plwordnet = ""
rels.involved_direction.proj.pointer = ""

rels.involved_direction.name.en = "Involved Direction"
rels.involved_direction.df.en = """
X is typically the direction/location of the action Y
"""
rels.involved_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the direction or location of the action or event expressed
by concept A.
"""
rels.involved_direction.ex.en = "" ### couldn't find an example
rels.involved_direction.exe.en = """
"""
rels.involved_direction.com.en = """
"""


### Relation: involved_target_direction

rels.involved_target_direction.form.inOMW = True
rels.involved_target_direction.form.reverse = "target_direction"

rels.involved_target_direction.proj.eurown = "involved_target_direction"
rels.involved_target_direction.proj.plwordnet = ""
rels.involved_target_direction.proj.pointer = ""

rels.involved_target_direction.name.en = "Involved Target Direction"
rels.involved_target_direction.df.en = "X is the place where action Y leads to"
rels.involved_target_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the place
where the action or event expressed by concept A leads to.
"""
rels.involved_target_direction.ex.en = "go back home/home"
rels.involved_target_direction.exe.en = """
"""
rels.involved_target_direction.com.en = """
"""


### Relation: involved_source_direction

rels.involved_source_direction.form.inOMW = True
rels.involved_source_direction.form.reverse = "source_direction"

rels.involved_source_direction.proj.eurown = "involved_source_direction"
rels.involved_source_direction.proj.plwordnet = ""
rels.involved_source_direction.proj.pointer = ""

rels.involved_source_direction.name.en = "Involved Source Direction"
rels.involved_source_direction.df.en = """
X is the place from where the action Y begins
"""
rels.involved_source_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the
place from where the action or event expressed by concept A
begins/starts/happens.
"""
rels.involved_source_direction.ex.en = "disembark/ship"
rels.involved_source_direction.exe.en = """
"""
rels.involved_source_direction.com.en = """
"""


### Relation: co_role EDP31

rels.co_role.form.inOMW = True
rels.co_role.form.reverse = "co_role"

rels.co_role.proj.eurown = "co_role"
rels.co_role.proj.plwordnet = ""

rels.co_role.name.en = "Co Role"
rels.co_role.df.en = """
a pair of linked role relations without an explicit event
"""
rels.co_role.dfn.en = """
A relation between two concepts where concept X undergoes an action in
which concept Y is involved (bidirectional).
"""
rels.co_role.ex.en = ""
rels.co_role.exe.en = """
"""
rels.co_role.com.en = """
"""


### Relation: co_agent_patient EDP32

rels.co_agent_patient.form.inOMW = True
rels.co_agent_patient.form.reverse = "co_patient_agent"

rels.co_agent_patient.proj.eurown = "co_agent_patient"
rels.co_agent_patient.proj.plwordnet = ""

rels.co_agent_patient.name.en = "Co Agent Patient"
rels.co_agent_patient.df.en = "X is the patient undergoing Y"
rels.co_agent_patient.dfn.en = """
A relation between two concepts where concept Y is the patient
undergoing an action carried out by concept X.

Y is the patient undergoing an action carried out by X.
"""
rels.co_agent_patient.ex.en = "novel writer/poet"
rels.co_agent_patient.exe.en = """
"""
rels.co_agent_patient.com.en = """
"""


### Relation: co_agent_instrument EDP32

rels.co_agent_instrument.form.inOMW = True
rels.co_agent_instrument.form.reverse = "co_instrument_agent"

rels.co_agent_instrument.proj.eurown = "co_agent_instrument"
rels.co_agent_instrument.proj.plwordnet = ""

rels.co_agent_instrument.name.en = "Co Agent Instrument"
rels.co_agent_instrument.df.en = "guitar player/guitar"
rels.co_agent_instrument.dfn.en = """
A relation between two concepts where concept Y is the instrument used
by concept X in a certain action.

Y is the instrument used by X in a certain action
"""
rels.co_agent_instrument.ex.en = ""
rels.co_agent_instrument.exe.en = """
"""
rels.co_agent_instrument.com.en = """
"""


### Relation: co_agent_result EDP32

rels.co_agent_result.form.inOMW = True
rels.co_agent_result.form.reverse = "co_result_agent"

rels.co_agent_result.proj.eurown = "co_agent_result"
rels.co_agent_result.proj.plwordnet = ""

rels.co_agent_result.name.en = "Co Agent Result"
rels.co_agent_result.df.en = "X is the result of action Y"
rels.co_agent_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by concept X.

Y is the result of an action carried out by X.
"""
rels.co_agent_result.ex.en = "pastry dough/bread dough"
rels.co_agent_result.exe.en = """
"""
rels.co_agent_result.com.en = """
"""


### Relation: co_patient_agent EDP32

rels.co_patient_agent.form.inOMW = True
rels.co_patient_agent.form.reverse = "co_agent_patient"

rels.co_patient_agent.proj.eurown = "co_patient_agent"
rels.co_patient_agent.proj.plwordnet = ""

rels.co_patient_agent.name.en = "Co Patient Agent"
rels.co_patient_agent.df.en = ""
rels.co_patient_agent.dfn.en = """
A relation between two concepts where concept Y undergoes an action
carried out by concept X.
"""
rels.co_patient_agent.ex.en = "poet/novel writer"
rels.co_patient_agent.exe.en = """
"""
rels.co_patient_agent.com.en = """
"""


### Relation: co_patient_instrument EDP32

rels.co_patient_instrument.form.inOMW = True
rels.co_patient_instrument.form.reverse = "co_instrument_patient"

rels.co_patient_instrument.proj.eurown = "co_patient_instrument"
rels.co_patient_instrument.proj.plwordnet = ""

rels.co_patient_instrument.name.en = "Co Patient Instrument"
rels.co_patient_instrument.df.en = ""
rels.co_patient_instrument.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
rels.co_patient_instrument.ex.en = "ice/ice saw"
rels.co_patient_instrument.exe.en = """
"""
rels.co_patient_instrument.com.en = """
"""


### Relation: co_result_agent EDP32

rels.co_result_agent.form.inOMW = True
rels.co_result_agent.form.reverse = "co_agent_result"

rels.co_result_agent.proj.eurown = "co_result_agent"
rels.co_result_agent.proj.plwordnet = ""

rels.co_result_agent.name.en = "Co Result Agent"
rels.co_result_agent.df.en = ""
rels.co_result_agent.dfn.en = """
A relation between two concepts where concept X is the result of an
action carried out by concept Y.
"""
rels.co_result_agent.ex.en = "bread dough/pastry dough"
rels.co_result_agent.exe.en = """
"""
rels.co_result_agent.com.en = """
"""


### Relation: co_result_instrument EDP32

rels.co_result_instrument.form.inOMW = True
rels.co_result_instrument.form.reverse = "co_instrument_result"

rels.co_result_instrument.proj.eurown = "co_result_instrument"
rels.co_result_instrument.proj.plwordnet = ""

rels.co_result_instrument.name.en = "Co Result Instrument"
rels.co_result_instrument.df.en = ""
rels.co_result_instrument.dfn.en = """
A relation between two concepts where concept X is the result of an
action for which the instrument expressed by concept Y is used.
"""
rels.co_result_instrument.ex.en = "photograph/camera"
rels.co_result_instrument.exe.en = """
"""
rels.co_result_instrument.com.en = """
"""


### Relation: co_instrument_agent EDP32

rels.co_instrument_agent.form.inOMW = True
rels.co_instrument_agent.form.reverse = "co_agent_instrument"

rels.co_instrument_agent.proj.eurown = "co_instrument_agent"
rels.co_instrument_agent.proj.plwordnet = ""

rels.co_instrument_agent.name.en = "Co Instrument Agent"
rels.co_instrument_agent.df.en = ""
rels.co_instrument_agent.dfn.en = """
A relation between two concepts where concept X is the instrument used
by concept Y for a certain action.
"""
rels.co_instrument_agent.ex.en = "guitar/guitar player"
rels.co_instrument_agent.exe.en = """
"""
rels.co_instrument_agent.com.en = """
"""


### Relation: co_instrument_patient EDP32

rels.co_instrument_patient.form.inOMW = True
rels.co_instrument_patient.form.reverse = "co_patient_instrument"

rels.co_instrument_patient.proj.eurown = "co_instrument_patient"
rels.co_instrument_patient.proj.plwordnet = ""

rels.co_instrument_patient.name.en = "Co Instrument Patient"
rels.co_instrument_patient.df.en = ""
rels.co_instrument_patient.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
rels.co_instrument_patient.ex.en = "ice saw/ice"
rels.co_instrument_patient.exe.en = """
"""
rels.co_instrument_patient.com.en = """
"""


### Relation: co_instrument_result ice saw/ice

rels.co_instrument_result.form.inOMW = True
rels.co_instrument_result.form.reverse = "co_result_instrument"

rels.co_instrument_result.proj.eurown = "co_instrument_result"
rels.co_instrument_result.proj.plwordnet = ""

rels.co_instrument_result.name.en = "Co Instrument Result"
rels.co_instrument_result.df.en = ""
rels.co_instrument_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by the instrument expressed by concept X.
"""
rels.co_instrument_result.ex.en = "camera/photograph"
rels.co_instrument_result.exe.en = """
"""
rels.co_instrument_result.com.en = """
"""


### Relation: state_of EDP37

rels.state_of.form.inOMW = True
rels.state_of.form.reverse = "be_in_state"

rels.state_of.proj.ili = "i35578"
rels.state_of.proj.pwn = "attribute"
rels.state_of.proj.eurown = "state_of"
rels.state_of.proj.plwordnet = "state"
rels.state_of.proj.pointer = ""

rels.state_of.name.en = "State Of"
rels.state_of.df.en = """
the way something is with respect to its main attributes
"""
rels.state_of.dfn.en = """
A relation between two concepts where concept Y is qualified by
concept X.
"""
rels.state_of.ex.en = "poor/poor (a poor person)"
rels.state_of.exe.en = """
"""
rels.state_of.com.en = """
In plWordNet it is a relation between lexical units.
FCB: isn't this the same as attribute (but split into two directions)
"""


### Relation: be_in_state EDP37

rels.be_in_state.form.inOMW = True
rels.be_in_state.form.reverse = "state_of"

rels.be_in_state.proj.eurown = "be_in_state"
rels.be_in_state.proj.plwordnet = "bearer of state"
rels.be_in_state.proj.pointer = ""

rels.be_in_state.name.en = "Be In State"
rels.be_in_state.df.en = ""
rels.be_in_state.dfn.en = """
A relation between two concepts where concept X is qualified by
concept Y.

X is qualified by Y.
"""
rels.be_in_state.ex.en = "poor (a poor person)/poor"
rels.be_in_state.exe.en = """
"""
rels.be_in_state.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: causes EDP34

rels.causes.form.inOMW = True
rels.causes.form.reverse = "is_caused_by"

rels.causes.proj.ili = "i35561"
rels.causes.proj.pwn = "cause"
rels.causes.proj.querywn = "caus"
rels.causes.proj.eurown = "causes"
rels.causes.proj.plwordnet = "causation"
rels.causes.proj.pointer = ">"

rels.causes.name.en = "Causes"
rels.causes.df.en = """
any entity that produces an effect or is responsible for events or
results
"""
rels.causes.dfn.en = """
A relation between two concepts where concept Y comes into existence
as a result of concept X. Entailment is a relation that links two
verbs, and it is currently unilateral — Verb-X causes Verb-Y, without
a reciprocal or tracing link. Causation presupposes/requires that some
Verb-Y will, inevitably, take place during or after Verb-X (e.g. if
Verb-X occurs, then Verb-Y will also occur).

While not exclusive to these types of verbs, many verbs that have both
a transitive and an intransitive form will frequently be submitted to
this relation.
"""
rels.causes.ex.en = "kill/die"
rels.causes.exe.en = """
"""
rels.causes.com.en = """
EUWN's definition of CAUSES is broader than that of PWN. It
seems possible to just absorb PWN's links.
"""


### Relation: is_caused_by EDP34

rels.is_caused_by.form.inOMW = True
rels.is_caused_by.form.reverse = "causes"

rels.is_caused_by.proj.pwn = ""
rels.is_caused_by.proj.querywn = "caus"
rels.is_caused_by.proj.eurown = "is_caused_by"
rels.is_caused_by.proj.plwordnet = ""
rels.is_caused_by.proj.pointer = ""

rels.is_caused_by.name.en = "Is Caused By"
rels.is_caused_by.df.en = ""
rels.is_caused_by.dfn.en = """
A relation between two concepts where concept X comes into existence
as a result of concept Y.
"""
rels.is_caused_by.ex.en = "die/kill"
rels.is_caused_by.exe.en = """
"""
rels.is_caused_by.com.en = """
The 'is caused by' relation was missing from PWN before."""


### Relation: subevent EDP35

rels.subevent.form.inOMW = True
rels.subevent.form.reverse = "is_subevent_of"

rels.subevent.proj.querywn = "enta"
rels.subevent.proj.eurown = "has_subevent"
rels.subevent.proj.plwordnet = "verbal_holonymy"
rels.subevent.proj.pointer = "\*"

rels.subevent.name.en = "Subevent"
rels.subevent.df.en = ""
rels.subevent.dfn.en = """
A relation between two concepts where concept Y takes place
during or as part of concept X, and whenever concept Y takes
place, concept X takes place.

"""
rels.subevent.ex.en = "sleep/snore"
rels.subevent.exe.en = """
"""
rels.subevent.com.en = """
The EUWN CAUSES relation is broader than the PWN in such a
way that it actually includes links that were linked as
ENTAILMENT by the PWN (e.g. to suceed IS_CAUSED_BY to try;
to try CAUSES succeed [non-factive, intention]). This means
that HAS_SUBVENT and IS_SUBVENT_OF should not include every
relation marked as ENTAILMENT by the PWN.

"""


### Relation: is_subevent_of EDP35

rels.is_subevent_of.form.inOMW = True
rels.is_subevent_of.form.reverse = "subevent"

rels.is_subevent_of.proj.querywn = "enta"
rels.is_subevent_of.proj.eurown = "is_subevent_of"
rels.is_subevent_of.proj.plwordnet = "verbal_meronymy"
rels.is_subevent_of.proj.pointer = ""

rels.is_subevent_of.name.en = "Is Subevent Of"
rels.is_subevent_of.df.en = ""
rels.is_subevent_of.dfn.en = """
A relation between two concepts where concept X takes place
during or as part of concept Y, and whenever concept X takes
place, concept Y takes place.

"""
rels.is_subevent_of.ex.en = "snore/sleep"
rels.is_subevent_of.exe.en = """
"""
rels.is_subevent_of.com.en = """
"""


### Relation: in_manner EDP36

rels.in_manner.form.inOMW = True
rels.in_manner.form.reverse = "manner_of"

rels.in_manner.proj.querywn = "enta"
rels.in_manner.proj.eurown = "in_manner"
rels.in_manner.proj.plwordnet = ""
rels.in_manner.proj.pointer = ""

rels.in_manner.name.en = "In Manner"
rels.in_manner.df.en = ""
rels.in_manner.dfn.en = """
A relation between two concepts where concept Y qualifies
the manner in which an action or event expressed by concept
X takes place.

"""
rels.in_manner.ex.en = "slurp/noisely"
rels.in_manner.exe.en = """
"""
rels.in_manner.com.en = """
"""


### Relation: manner_of EDP36

rels.manner_of.form.inOMW = True
rels.manner_of.form.reverse = "in_manner"

rels.manner_of.proj.ili = "i62791"
rels.manner_of.proj.querywn = "enta"
rels.manner_of.proj.eurown = "manner_of"
rels.manner_of.proj.plwordnet = ""
rels.manner_of.proj.pointer = ""

rels.manner_of.name.en = "Manner Of"
rels.manner_of.df.en = "a way of acting or behaving"
rels.manner_of.dfn.en = """
A relation between two concepts where concept X qualifies
the manner in which an action or event expressed by concept
Y takes place.

"""
rels.manner_of.ex.en = "noisely/slurp"
rels.manner_of.exe.en = """
"""
rels.manner_of.com.en = """
"""


### Relation: meronym EDP26

rels.meronym.form.inOMW = True
rels.meronym.form.reverse = "holonym"

rels.meronym.proj.ili = "i69575"
rels.meronym.proj.pwn = "meronym"
rels.meronym.proj.querywn = "enta"
rels.meronym.proj.eurown = "has_meronym"
rels.meronym.proj.plwordnet = "meronym"
rels.meronym.proj.pointer = "%"

rels.meronym.name.en = "Meronym"
rels.meronym.df.en = """
a word that names a part of a larger whole
"""
rels.meronym.dfn.en = """
A relation between two concepts where concept Y makes up a part of
concept X.
"""
rels.meronym.ex.en = "hand/finger"
rels.meronym.exe.en = """
"""
rels.meronym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: holonym EDP26

rels.holonym.form.inOMW = True
rels.holonym.form.reverse = "meronym"

rels.holonym.proj.ili = "i69567"
rels.holonym.proj.querywn = "enta"
rels.holonym.proj.eurown = "has_holonym"
rels.holonym.proj.plwordnet = "holonym"
rels.holonym.proj.pointer = "#"

rels.holonym.name.en = "Holonym"
rels.holonym.df.en = """
a word that names the whole of which a given word is a part
"""
rels.holonym.dfn.en = """
A relation between two concepts where concept X makes up a
part of concept Y.
"""
rels.holonym.ex.en = "finger/hand"
rels.holonym.exe.en = """
"""
rels.holonym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: mero_part EDP27

rels.mero_part.form.inOMW = True
rels.mero_part.form.reverse = "holo_part"

rels.mero_part.proj.pwn = "part meronym"
rels.mero_part.proj.querywn = "mprt"
rels.mero_part.proj.eurown = "has_mero_part"
rels.mero_part.proj.plwordnet = "meronymy_part"
rels.mero_part.proj.pointer = "%p"

rels.mero_part.name.en = "Part Meronym"
rels.mero_part.df.en = ""
rels.mero_part.dfn.en = """
A relation between two concepts where concept Y is a component of
concept X. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
rels.mero_part.ex.en = "car/wheel"
rels.mero_part.exe.en = """
hand > finger

"""
rels.mero_part.com.en = """
This relation is also frequently used by PWN to denote
geographical inclusiveness relations.

"""


### Relation: holo_part EDP27

rels.holo_part.form.inOMW = True
rels.holo_part.form.reverse = "mero_part"

rels.holo_part.proj.pwn = "part holonym"
rels.holo_part.proj.querywn = "hprt"
rels.holo_part.proj.eurown = "has_holo_part"
rels.holo_part.proj.plwordnet = "holonymy_part"
rels.holo_part.proj.pointer = "#p"

rels.holo_part.name.en = "Part Holonym"
rels.holo_part.df.en = ""
rels.holo_part.dfn.en = """
A relation between two concepts where concept X is a component of
concept Y. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
rels.holo_part.ex.en = "wheel/car"
rels.holo_part.exe.en = """
"""
rels.holo_part.com.en = """
"""


### Relation: mero_member EPD27

rels.mero_member.form.inOMW = True
rels.mero_member.form.reverse = "holo_member"

rels.mero_member.proj.pwn = "member meronym"
rels.mero_member.proj.querywn = "mmem"
rels.mero_member.proj.eurown = "has_mero_member"
rels.mero_member.proj.plwordnet = "meronymy_member"
rels.mero_member.proj.pointer = "%m"

rels.mero_member.name.en = "Member Meronym"
rels.mero_member.df.en = ""
rels.mero_member.dfn.en = """
A relation between two concepts where concept Y is a member/ element
of concept X. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
rels.mero_member.ex.en = "player/team"
rels.mero_member.exe.en = """
fleet > ship

"""
rels.mero_member.com.en = """
"""


### Relation: holo_member EDP27

rels.holo_member.form.inOMW = True
rels.holo_member.form.reverse = "mero_member"

rels.holo_member.proj.pwn = "member holonym"
rels.holo_member.proj.querywn = "hmem"
rels.holo_member.proj.eurown = "has_holo_member"
rels.holo_member.proj.plwordnet = "holonymy_member"
rels.holo_member.proj.pointer = "#m"

rels.holo_member.name.en = "Member Holonym"
rels.holo_member.df.en = ""
rels.holo_member.dfn.en = """
A relation between two concepts where concept X is a member/ element
of concept Y. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
rels.holo_member.ex.en = "team/player"
rels.holo_member.exe.en = """
"""
rels.holo_member.com.en = """
"""


### Relation: mero_substance EDP28

rels.mero_substance.form.inOMW = True
rels.mero_substance.form.reverse = "holo_substance"

rels.mero_substance.proj.pwn = "substance meronym"
rels.mero_substance.proj.querywn = "msub"
rels.mero_substance.proj.eurown = "has_mero_madeof"
rels.mero_substance.proj.plwordnet = "meronymy_substance"
rels.mero_substance.proj.pointer = "%s"

rels.mero_substance.name.en = "Substance Meronym"
rels.mero_substance.df.en = ""
rels.mero_substance.dfn.en = """
A relation between two concepts where concept X is made of concept
Y. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
rels.mero_substance.ex.en = "stick/wood"
rels.mero_substance.exe.en = """
book > paper
"""
rels.mero_substance.com.en = """
"""


### Relation: holo_substance EDP28

rels.holo_substance.form.inOMW = True
rels.holo_substance.form.reverse = "mero_substance"

rels.holo_substance.proj.pwn = "substance holonym"
rels.holo_substance.proj.querywn = "hsub"
rels.holo_substance.proj.eurown = "has_holo_madeof"
rels.holo_substance.proj.plwordnet = "holonymy_substance"
rels.holo_substance.proj.pointer = "#s"

rels.holo_substance.name.en = "Substance Holonym"
rels.holo_substance.df.en = ""
rels.holo_substance.dfn.en = """
A relation between two concepts where concept Y is made of concept
X. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
rels.holo_substance.ex.en = "wood/stick"
rels.holo_substance.exe.en = """
"""
rels.holo_substance.com.en = """
"""


### Relation: mero_location EDP28

rels.mero_location.form.inOMW = True
rels.mero_location.form.reverse = "holo_location"

rels.mero_location.proj.querywn = "hsub"
rels.mero_location.proj.eurown = "has_mero_location"
rels.mero_location.proj.plwordnet = "meronymy_location"

rels.mero_location.name.en = "Location Meronym"
rels.mero_location.df.en = ""
rels.mero_location.dfn.en = """
A relation between two concepts where concept X is a place
located in concept Y.
"""
rels.mero_location.ex.en = "city/centre"
rels.mero_location.exe.en = """
desert > oasis
"""
rels.mero_location.com.en = """
"""


### Relation: holo_location EDP28

rels.holo_location.form.inOMW = True
rels.holo_location.form.reverse = "mero_location"

rels.holo_location.proj.querywn = "hsub"
rels.holo_location.proj.eurown = "has_holo_location"
rels.holo_location.proj.plwordnet = "holonymy_location"

rels.holo_location.name.en = "Location Holonym"
rels.holo_location.df.en = ""
rels.holo_location.dfn.en = """
A relation between two concepts where concept Y is a place
located in concept X.
"""
rels.holo_location.ex.en = "centre/city"
rels.holo_location.exe.en = """
"""
rels.holo_location.com.en = """
"""


### Relation: mero_portion EDP27

rels.mero_portion.form.inOMW = True
rels.mero_portion.form.reverse = "holo_portion"

rels.mero_portion.proj.pwn = "portion meronym"
rels.mero_portion.proj.querywn = "hsub"
rels.mero_portion.proj.eurown = "has_mero_portion"
rels.mero_portion.proj.plwordnet = "meronymy_portion"
rels.mero_portion.proj.pointer = ""

rels.mero_portion.name.en = "Portion Meronym"
rels.mero_portion.df.en = ""
rels.mero_portion.dfn.en = """
A relation between two concepts where concept X is an
amount/piece/portion of concept Y.
"""
rels.mero_portion.ex.en = "drop/liquid"
rels.mero_portion.exe.en = """
bread > slice
"""
rels.mero_portion.com.en = """
"""


### Relation: holo_portion EDP27

rels.holo_portion.form.inOMW = True
rels.holo_portion.form.reverse = "mero_portion"

rels.holo_portion.proj.querywn = "hsub"
rels.holo_portion.proj.eurown = "has_holo_portion"
rels.holo_portion.proj.plwordnet = "holonymy_portion"
rels.holo_portion.proj.pointer = ""

rels.holo_portion.name.en = "Portion Holonym"
rels.holo_portion.df.en = ""
rels.holo_portion.dfn.en = """
A relation between two concepts where concept Y is an
amount/piece/portion of concept X
"""
rels.holo_portion.ex.en = "liquid/drop"
rels.holo_portion.exe.en = """
"""
rels.holo_portion.com.en = """
"""


### Relation: eq_synonym

rels.eq_synonym.form.inOMW = True
rels.eq_synonym.form.reverse = "eq_synonym"

rels.eq_synonym.proj.ili = "i69607"
rels.eq_synonym.proj.eurown = "eq_synonym"
rels.eq_synonym.proj.plwordnet = ""

rels.eq_synonym.name.en = "Equal Synonym"
rels.eq_synonym.df.en = """
two words that can be interchanged in a context are said to be
synonymous relative to that context
"""
rels.eq_synonym.dfn.en = """
A relation between two concepts where X and Y are equivalent concepts
but their nature requires that they remain separate.

Equality is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-X is equal to Concept-Y,
and Concept-Y is equal to Concept-X.

It denotes a special kind full synonimity that allows separation of
synonym lemmas in two different synsets. It can occur with any type of
part-of-speech.

At the moment, we're currently making use of this in order to isolate
chengyu (成语), a traditional four-character Chinese idiom.
"""
rels.eq_synonym.ex.en = ""
rels.eq_synonym.exe.en = """
* 一模一样 (70100056-a) EQUALS identical (02068946-a)  identical
* (02068946-a) EQUALS  一模一样 (70100056-a)
"""
rels.eq_synonym.com.en = """
"""


### Relation: instance_hypernym

rels.instance_hypernym.form.inOMW = True
rels.instance_hypernym.form.reverse = "instance_hyponym"

rels.instance_hypernym.proj.pwn = "Instance Hypernym"
rels.instance_hypernym.proj.querywn = "inst"
rels.instance_hypernym.proj.eurown = "HAS_INSTANCE"
rels.instance_hypernym.proj.plwordnet = "type"
rels.instance_hypernym.proj.pointer = "@i"

rels.instance_hypernym.name.en = "Instance Hypernym"
rels.instance_hypernym.df.en = "the type of an instance"
rels.instance_hypernym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
rels.instance_hypernym.ex.en = "*city/Manchester*"
rels.instance_hypernym.exe.en = """"""
rels.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
rels.instance_hypernym.com.en = """
Sometimes modelled as hyponomy/hypernymy relations.
"""


### Relation: instance_hyponym

rels.instance_hyponym.form.inOMW = True
rels.instance_hyponym.form.reverse = "instance_hypernym"

rels.instance_hyponym.proj.ili = "i75102"
rels.instance_hyponym.proj.pwn = "Instance Hypernym"
rels.instance_hyponym.proj.querywn = "hasi"
rels.instance_hyponym.proj.eurown = "BELONGS_To_CLASS"
rels.instance_hyponym.proj.plwordnet = "instance"
rels.instance_hyponym.proj.pointer = "~i"

rels.instance_hyponym.name.en = "Instance Hyponym"
rels.instance_hyponym.df.en = "an occurrence of something"
rels.instance_hyponym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
rels.instance_hyponym.ex.en = ""
rels.instance_hypernym.exe.en = """"""
rels.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
rels.instance_hyponym.exe.en = """
"""
rels.instance_hyponym.com.en = """
"""


### Relation: exemplifies

rels.exemplifies.form.inOMW = True
rels.exemplifies.form.reverse = "is_exemplified_by"

rels.exemplifies.proj.ili = "i26682"
rels.exemplifies.proj.pwn = "Domain of synset - USAGE"
rels.exemplifies.proj.querywn = "dmnu"
rels.exemplifies.proj.plwordnet = ""
rels.exemplifies.proj.pointer = ";u"

rels.exemplifies.name.en = "Exemplifies"
rels.exemplifies.df.en = "clarify by giving an example of"
rels.exemplifies.dfn.en = """
A relation between two concepts where Y is a type of concept
X. such as idiom, honorific or classifier.
"""
rels.exemplifies.ex.en = ""
rels.exemplifies.exe.en = """
"""
rels.exemplifies.com.en = """
The name was changed from "Domain of synset - USAGE" as we found it
too different from the standard meaning of domain.
"""


### Relation: is_exemplified_by

rels.is_exemplified_by.form.inOMW = True
rels.is_exemplified_by.form.reverse = "exemplifies"

rels.is_exemplified_by.proj.pwn = "domain term usage"
rels.is_exemplified_by.proj.querywn = "dmtu"
rels.is_exemplified_by.proj.plwordnet = ""
rels.is_exemplified_by.proj.pointer = "-u"

rels.is_exemplified_by.name.en = "Is Exemplified By"
rels.is_exemplified_by.df.en = ""
rels.is_exemplified_by.dfn.en = """
A relation between two concepts where A is an example of the type B.
"""
rels.is_exemplified_by.ex.en = ""
rels.is_exemplified_by.exe.en = """
"""
rels.is_exemplified_by.com.en = """
We agreed to change the name for these with Christiane! We
propose 'Exemplified_By'.

"""


### Relation: domain_topic

rels.domain_topic.form.inOMW = True
rels.domain_topic.form.reverse = "has_domain_topic"

rels.domain_topic.proj.pwn = "domain category"
rels.domain_topic.proj.querywn = "Domain of synset - TOPIC"
rels.domain_topic.proj.plwordnet = ""
rels.domain_topic.proj.pointer = ";c"

rels.domain_topic.name.en = "Domain Topic"
rels.domain_topic.df.en = ""
rels.domain_topic.dfn.en = """
A relation between two concepts where Y is a scientific
domain (e.g. computing, sport, biology, etc.) of concept X.
"""
rels.domain_topic.ex.en = ""
rels.domain_topic.exe.en = """
"""
rels.domain_topic.com.en = """
"""


### Relation: has_domain_topic

rels.has_domain_topic.form.inOMW = True
rels.has_domain_topic.form.reverse = "domain_topic"

rels.has_domain_topic.proj.querywn = "dmtc"
rels.has_domain_topic.proj.plwordnet = ""
rels.has_domain_topic.proj.pointer = "-c"

rels.has_domain_topic.name.en = "Has Domain Topic"
rels.has_domain_topic.df.en = ""
rels.has_domain_topic.dfn.en = """
A relation between two concepts where X is a scientific
domain (e.g. computing, sport, biology, etc.) of concept Y.
"""
rels.has_domain_topic.ex.en = ""
rels.has_domain_topic.exe.en = """
"""
rels.has_domain_topic.com.en = """
"""


### Relation: domain_region

rels.domain_region.form.inOMW = True
rels.domain_region.form.reverse = "has_domain_region"

rels.domain_region.proj.pwn = "Domain of synset - REGION"
rels.domain_region.proj.querywn = "dmnr"
rels.domain_region.proj.plwordnet = ""
rels.domain_region.proj.pointer = ";r"

rels.domain_region.name.en = "Domain Region"
rels.domain_region.df.en = ""
rels.domain_region.dfn.en = """
A relation between two concepts where Y is a geographical / cultural
domain of concept X. Domain(Region) and Domain-Term(Region) is a
paired relation between terms/concepts of any part-of-speech and a
related geographical region.
"""
rels.domain_region.ex.en = ""
rels.domain_region.exe.en = """
"""
rels.domain_region.com.en = """
We also agreed to change the name for these (to include both
geographical and cultural regions)! But I'm not sure to
what...
"""


### Relation: has_domain_region

rels.has_domain_region.form.inOMW = True
rels.has_domain_region.form.reverse = "domain_region"

rels.has_domain_region.proj.querywn = "dmtr"
rels.has_domain_region.proj.plwordnet = ""
rels.has_domain_region.proj.pointer = "-r"

rels.has_domain_region.name.en = "Has Domain Region"
rels.has_domain_region.df.en = ""
rels.has_domain_region.dfn.en = """
A relation between two concepts where X is a geographical /
cultural domain of concept Y.
"""
rels.has_domain_region.ex.en = ""
rels.has_domain_region.exe.en = """
"""
rels.has_domain_region.com.en = """
We have discussed changing the name for these (as they include both
geographical and cultural regions).  But we have not yet come up with
a good name.
"""


### Relation: attribute

rels.attribute.form.inOMW = True
rels.attribute.form.reverse = "attribute"

rels.attribute.proj.ili = "i35577"
rels.attribute.proj.pwn = "attribute"
rels.attribute.proj.querywn = "attr"
rels.attribute.proj.plwordnet = "value_of_the_attribute"
rels.attribute.proj.pointer = "="

rels.attribute.name.en = "Attribute"
rels.attribute.df.en = """
an abstraction belonging to or characteristic of an entity
"""
rels.attribute.dfn.en = """
A relation between nominal and adjectival concepts where the concept X
is an attribute of concept Y. ‘Attributes’ is a self-reciprocal link
(the two directions of this relation share the same meaning) —
Concept-X attributes to Concept-Y, and Concept-Y attributes to
Concept-X.

It denotes a relation between a noun and its adjectival attributes,
and vice-versa — for this reason it should only link adjectives to
nouns and vice-versa.
"""
rels.attribute.ex.en = ""
rels.attribute.exe.en = """
* fertile (01001689-a) ATTRIBUTES:  fertility (14051494-n)
* fertility (14051494-n) ATTRIBUTES: fertile (01001689-a)
"""
rels.attribute.com.en = """
In plWN Value_of_the_attribute is a unilateral relation from
adjectives to nouns.
"""


### Relation: restricts

rels.restricts.form.inOMW = True
rels.restricts.form.reverse = "restricted_by"

rels.restricts.proj.ili = "i22888"
rels.restricts.proj.plwordnet = ""
rels.restricts.proj.pointer = ""

rels.restricts.name.en = "Restricts"
rels.restricts.df.en = """
place limits on (extent or amount or access)
"""
rels.restricts.dfn.en = """
A relation between an adjectival concept X (quantifier/determiner) and
a nominal (pronominal) concept Y.
"""
rels.restricts.ex.en = ""
rels.restricts.exe.en = """
"""
rels.restricts.com.en = """
This would work for features like 'medial' or 'proximal' in
pronouns, or 'every' in everybody, or 'male' for male
personal pronouns, but not masculine agreeement in gendered
languages. This relation will include some things that are
now marked as domain usage. (to be corrected soon'ish)
"""


### Relation: restricted_by

rels.restricted_by.form.inOMW = True
rels.restricted_by.form.reverse = "restricts"

rels.restricted_by.proj.plwordnet = ""
rels.restricted_by.proj.pointer = ""

rels.restricted_by.name.en = "Restricted By"
rels.restricted_by.df.en = ""
rels.restricted_by.dfn.en = """
A relation between nominal (pronominal) concept Y and an
adjectival concept X (quantifier/determiner).
"""
rels.restricted_by.ex.en = ""
rels.restricted_by.exe.en = """
* this-a (77000061-a) QUANTIFIES [qant] this-n (77000061-n)
* this-n (77000061-n) QUANTIFIER: [hasq] this-a (77000061-a)
"""
rels.restricted_by.com.en = """
"""


### Relation: classifies

rels.classifies.form.inOMW = True
rels.classifies.form.reverse = "classified_by"

rels.classifies.proj.ili = "i25399"
rels.classifies.proj.plwordnet = ""
rels.classifies.proj.pointer = ""

rels.classifies.name.en = "Classifies"
rels.classifies.df.en = """
assign to a class or kind
"""
rels.classifies.dfn.en = """
A relation between a classifier concept X and concept Y. A relation
between a classifier X and Y
"""
rels.classifies.ex.en = ""
rels.classifies.exe.en = """
"""
rels.classifies.com.en = """
currently we only have links for nominal concepts, but we
will do it for other POS (e.g. v)
"""


### Relation: classified_by

rels.classified_by.form.inOMW = True
rels.classified_by.form.reverse = "classifies"

rels.classified_by.proj.ili = "i25002"
rels.classified_by.proj.plwordnet = ""
rels.classified_by.proj.pointer = ""

rels.classified_by.name.en = "Classified By"
rels.classified_by.df.en = """
arrange or order by classes or categories
"""
rels.classified_by.dfn.en = """
A relation between concept Y and a classifier concept X. A relation
between Y and a classifier X
"""
rels.classified_by.ex.en = ""
rels.classified_by.exe.en = """
"""
rels.classified_by.com.en = """
"""


### Relation: also (no ili)

rels.also.form.inOMW = True
rels.also.form.reverse = 'also'

rels.also.proj.pwn = "also see"
rels.also.proj.querywn = "also"
rels.also.proj.eurown = ""
rels.also.proj.plwordnet = "inchoativity, iterativity, distributivity, anteriority"
rels.also.proj.pointer = "^"

rels.also.name.en = "See also"
rels.also.df.en = """
a word having a loose or fuzzy semantic relation to another word
"""
rels.also.dfn.en = """
‘See Also’ is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-X relates to Concept-Y, and
Concept-Y relates to Concept-X.

It denotes a relation of related meaning with another concept (going
beyond synonymy and similarity).

This link was originally used to relate adjectives, but we have
unconstrained this use, and we're making use of this link to relate
all parts-of-speech.
"""
rels.also.ex.en = ""
rels.also.exe.en = """
"""
rels.also.com.en = """
Also known as fuzzynym
"""


### Relation: antonym

rels.antonym.form.inOMW = True
rels.antonym.form.reverse = 'antonym'

rels.antonym.proj.ili = "i69547"
rels.antonym.proj.pwn = ""
rels.antonym.proj.querywn = "antonym"
rels.antonym.proj.eurown = ""
rels.antonym.proj.plwordnet = "complementary, proper and converse antonymy"
rels.antonym.proj.pointer = "!"

rels.antonym.name.en = "Antonym"
rels.antonym.df.en = """
a word that expresses a meaning opposed to the meaning of another
word, in which case the two words are antonyms of each other
"""
rels.antonym.dfn.en = """
Antonymy is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-X's antonym is Concept-Y,
and Concept-Y's antonym is Concept-X.

It denotes any kind of proper antonymy between two concepts. It
accounts for most types of antonymy, including gradable antonyms
(e.g. hot vs. cold), complementary antonyms (e.g. superior
vs. inferior) and converse or relational antonyms (e.g. buy
vs. sell). Antonymy can link any two members of any part-of-speech —
verbs (e.g. dress vs. undress), adverbs (e.g. naturally
vs. unnaturally), adjectives (e.g. superior vs. inferior) and nouns
(e.g. catalyst vs. anti-catalyst), and should only ever link concepts
with the same part-of-speech.

An opposite and inherently incompatible word.
"""
rels.antonym.ex.en = ""
rels.antonym.exe.en = """
"""
rels.antonym.com.en = """
It is primarily a relation between senses, but sense level antonymy
implies a looser synset level relation, which we automatically add to
make it avaiable for wordnets that do not yet have sense level links.
"""


### Relation: entails

rels.entails.form.inOMW = True
rels.entails.form.reverse = 'is_entailed_by'

rels.entails.proj.ili = "i34846"
rels.entails.proj.pwn = "entailment"
rels.entails.proj.querywn = "participle"
rels.entails.proj.eurown = ""
rels.entails.proj.plwordnet = ""
rels.entails.proj.pointer = ""

rels.entails.name.en = "Entails"
rels.entails.df.en = """
impose, involve, or imply as a necessary accompaniment or result
"""
rels.entails.dfn.en = """
Entailment is a relation that links two verbs, and it is currently
unilateral — Verb-X entails Verb-Y, without a reciprocal or tracing
link.  This relation presupposes/requires a semantic restriction in
which Verb-Y has to take place before or during Verb-X.
"""
rels.entails.ex.en = ""
rels.entails.exe.en = """
"""
rels.entails.com.en = """
"""


### Relation: is_entailed_by

rels.is_entailed_by.form.inOMW = True

rels.is_entailed_by.proj.pwn = ""
rels.is_entailed_by.proj.querywn = "participle"
rels.is_entailed_by.proj.eurown = ""
rels.is_entailed_by.proj.plwordnet = ""
rels.is_entailed_by.proj.pointer = ""

rels.is_entailed_by.name.en = "Is Entailed By"
rels.is_entailed_by.df.en = ""
rels.is_entailed_by.dfn.en = """
"""
rels.is_entailed_by.ex.en = ""
rels.is_entailed_by.exe.en = """
"""
rels.is_entailed_by.com.en = """
"""


### Relation: other

rels.other.form.inOMW = True

rels.other.proj.ili = "i11342"

rels.other.name.en = "Other"
rels.other.df.en = "any other semantic relation"
rels.other.dfn.en = """
This is used for semantic relation types not currently supported by
the OMW DTD.  The exact relation type can be given with ``dc:type``:

.. code:: xml

    <SynsetRelation relType="other" dc:type="emotion" target="example-en-1234-n"/>

"""
rels.other.ex.en = ""
rels.other.exe.en = """
"""
rels.other.com.en = """
Because we don't know what it means, we cannot give it a reverse relation.
"""


### New short definitions based on http://globalwordnet.github.io/schemas/

rels.agent.df.en = "X is typically the agent of the action expressed by Y"
rels.antonym.df.en = "An opposite and inherently incompatible word"
rels.be_in_state.df.en = "X is qualified by Y"
rels.classified_by.df.en = "A relation between Y and a classifier X"
rels.classifies.df.en = "A relation between a classifier X and Y"
rels.co_agent_instrument.df.en = "Y is the instrument used by X in a certain action"
rels.co_agent_patient.df.en = "Y is the patient undergoing an action carried out by X"
rels.co_agent_result.df.en = "Y is the result of an action carried out by X"
rels.co_instrument_agent.df.en = "X is the instrument used by Y for a certain action"
rels.co_instrument_patient.df.en = "Y undergoes an action for which the instrument expressed by X is used"
rels.co_instrument_result.df.en = "Y is the result of an action carried out by the instrument expressed by X"
rels.co_patient_agent.df.en = "Y undergoes an action carried out by X"
rels.co_patient_instrument.df.en = "X undergoes an action for which the instrument expressed by X is used"
rels.co_result_agent.df.en = "X is the result of an action carried out by Y"
rels.co_result_instrument.df.en = "X is the result of an action for which the instrument expressed by Y is used"
rels.co_role.df.en = "One concept undergoes an action in which the other concept is involved (bidirectional)"
rels.direction.df.en = "X is typically the direction or location of the action or event expressed by Y"
rels.eq_synonym.df.en = "X and Y are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)"
rels.holo_location.df.en = "Y is a place located in X"
rels.holo_portion.df.en = "Y is an amount/piece/portion of X"
rels.holonym.df.en = "X makes up a part of Y"
rels.in_manner.df.en = "Y qualifies the manner in which an action or event expressed by X takes place"
rels.instrument.df.en = "X is the instrument necessary for the action or event expressed by Y"
rels.involved_agent.df.en = "Y is typically the agent of the action expressed by X"
rels.involved_direction.df.en = "Y is typically the direction or location of the action or event expressed by X"
rels.involved_instrument.df.en = "Y is typically the instrument necessary for the action or event expressed by X"
rels.involved_location.df.en = "Y is typically the location where the action or event expressed by X takes place"
rels.involved_patient.df.en = "Y is typically the patient un-dergoing an action or event expressed by X"
rels.involved_result.df.en = "Y comes into existence as a result of X"
rels.involved_source_direction.df.en = "Y is the place from where the action or event expressed by X begins/starts/happens"
rels.involved_target_direction.df.en = "Y is the place where the action or event expressed by X leads to"
rels.involved.df.en = "Y is typically involved in the action or event expressed by X"
rels.is_caused_by.df.en = "X comes about because of Y"
rels.is_entailed_by.df.en = "Opposite of entails"
rels.is_subevent_of.df.en = "X takes place during or as part of Y, and whenever X takes place, Y takes place"
rels.location.df.en = "X is the location where the action or event expressed by Y takes place"
rels.manner_of.df.en = "X qualifies the manner in which an action or event expressed by Y takes place"
rels.mero_location.df.en = "X is a place located in Y"
rels.mero_portion.df.en = "X is an amount/piece/portion of Y"
rels.meronym.df.en = "Y makes up a part of X"
rels.other.df.en = "Any relation not otherwise specified"
rels.patient.df.en = "X is the patient undergoing an action or event expressed by Y"
#rels.pertainym.df.en =  "X is of or pertaining to Y"
rels.restricted_by.df.en = "A relation between nominal (pronominal) Y and an adjectival X (quantifier/determiner)"
rels.restricts.df.en = "A relation between an adjectival X (quantifier/determiner) and a nominal (pronominal) Y"
rels.result.df.en = "X comes into existence as a result of Y"
rels.role.df.en = "X is typically involved in the action or event expressed by Y"
rels.source_direction.df.en = "X is the place from where the event expressed by Y begins"
rels.state_of.df.en = "Y is qualified by X"
rels.subevent.df.en = "Y takes place during or as part of X, and whenever Y takes place, X takes place"
rels.target_direction.df.en = "X is the place to which the action or event expressed by Y leads"


if __name__ == '__main__':
    import json
    d = {'relations': [rels[relname] for relname in RELATIONS]}
    print(json.dumps(d, indent=2))
