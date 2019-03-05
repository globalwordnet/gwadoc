# -*- coding: utf-8 -*-

from gwadoc.base import rels


###############################################################################
### Relations Definitions


### Relation: domain

rels.domain.name.en = "Domain"


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


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

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
