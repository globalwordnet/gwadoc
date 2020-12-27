# -*- coding: utf-8 -*-

from collections import OrderedDict as od

###############################################################################
### Inventories

### for PROJECTS
### 'nam':  Name of the project
### 'url':  URL to link to
### 'exp':  mouseover text for short explanation

PROJECTS = od([
    ('pwn',       {'nam':'Princeton WordNet Relation Name',
                   'url':'https://wordnet.princeton.edu/documentation/wngloss7wn',
                   'exp':'Name used by the Princeton Wordnet'}),
    ('pointer',   {'nam':'Princeton WordNet Pointer',
                   'url':'https://wordnet.princeton.edu/documentation/wninput5wn',
                   'exp':'Pointer symbol in the PWN text database'}),
    ('eurown',    {'nam':'Euro WordNet Relation Name',
                   'url':'pdf/EWN_general.pdf',
                   'exp':'Name used by Euro WordNet'}),
    ('plwordnet', {'nam':'PlWordNet Relation Name',
                   'url':'http://plwordnet.pwr.wroc.pl/wordnet/about',
                   'exp':'Polish name used by the Polish WordNet'}),
    ('querywn',   {'nam':'PERL WordNet-QueryData Module',
                   'url':'https://metacpan.org/pod/WordNet::QueryData#QUERYING',
                   'exp':'Relation name used by QueryData'}),
    ('skos',      {'nam':'SKOS type (Simple Knowledge Organization System)',
                   'url':'https://www.w3.org/TR/skos-reference/#semantic-relations',
                   'exp':'General relations from SKOS'}),
    ('ili',       {'nam':'Open Multilingual Wordnet Concept',
                   'url':'https://lr.soh.ntu.edu.sg/omw/omw',
                   'exp':'OMW, linked by Interlingual Index'}),
    ('SUMO',      {'nam':'Sumo Relation Type',
                   'url':'http://www.adampease.org/OP/',
                   'exp':'Relation in the Suggested Upper Merged Ontology'}),
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
    'participle',
    'pertainym',
    'derivation',
    ### new in 2021
    'simple_aspect_ip',  
    'simple_aspect_pi',  
    'secondary_aspect_ip',
    'secondary_aspect_pi',
    'feminine_form_of' , # sow    ->  pig
    'has_feminine_form' , # pig    ->  sow 
    'masculine_form_of', # boar   ->  pig 
    'has_masculine_form', # pig   ->  boar 
    'young_form_of',     # piglet ->  pig  
    'has_young_form',     # pig ->  piglet  
    'diminutive_of',     # piggy  ->  pig                       
    'has_diminutive',     # pig  ->  piggy                       
    'augmentative_of',
    'has_augmentative',
    'anto_gradable',
    'anto_simple',
    'anto_converse',
    'ir_synonym'
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


FORMAL_ATTRIBUTES = {
    'parent':  'Parent Relation',
    'synset_synset': 'Applicability to synset -> synset links',
    'sense_synset': 'Applicability to sense -> synset links',
    'sense_sense': 'Applicability to sense -> sense links',
    'reverse': 'Reverse Relation',
    'inOMW':   'Relation used in OMW',
    'schema_version': 'Which version first used this'
}
