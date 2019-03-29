# -*- coding: utf-8 -*-

from collections import OrderedDict as od

###############################################################################
### Inventories

PROJECTS = od([
    ('pwn',       'Princeton WordNet Relation Name'),
    ('pointer',   'Princeton WordNet Pointer'),
    ('eurown',    'Euro WordNet Relation Name'),
    ('plwordnet', 'PlWordNet Relation Name'),
    ('querywn',   'PERL WordNet-QueryData Module'),
    ('skos',      'SKOS type'),
    ('ili',       'Interlingual Index Node'),
    ('SUMO',      'Sumo Relation Type'),
])


LANGUAGES = od([
    ('en',     'English'),
    ('pl',     'Polish'),
    ('ja',     'Japanese'),
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
    'com':  'Comments',
    'df':   'Short Definition',
    'dfn':  'Long Definition',
    'ex':   'Short Example',
    'exe':  'Long Examples',
    'fa':   'Formal Attributes',
    'name': 'Relation Name',
    'proj': 'Relation Name in Project',
    'test': 'Tests',
}


FORMALATTRIBUTES = {
    'parent':  'Parent Relation',
    'reverse': 'Reverse Relation',
    'inOMW':   'Relation used in OMW'
}
