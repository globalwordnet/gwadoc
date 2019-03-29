# -*- coding: utf-8 -*-

from gwadoc import sense_rels, synset_rels


###############################################################################
### Relations Definitions


### Relation: domain

synset_rels.domain.name.en = "Domain"


### Relation: has_domain

synset_rels.has_domain.name.en = "In Domain"


### Relation: constitutive

synset_rels.constitutive.name.en = "Constitutive"
synset_rels.constitutive.df.en = "Core semantic relations that define synsets"
synset_rels.constitutive.dfn.en = """
Core semantic relations that define synsets.

We follow the discussion in [Maziarz:Piasecki:Szpakowicz:2013]_

.. [Maziarz:Piasecki:Szpakowicz:2013] The chicken-and-egg problem in
   wordnet design: synonymy, synsets and constitutive relations.
   Language Resources and Evaluation, 47(3), pp 769–79
"""


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

synset_rels.hypernym.name.en = 'Hypernym'
synset_rels.hypernym.df.en = 'a word that is more general than a given word'
synset_rels.hypernym.dfn.en = """
A hypernym of something is its superordinate term:
if X is a hypernym of Y, then all Y are X.
"""
synset_rels.hypernym.ex.en = "*animal* is a hypernym of *dog*"
synset_rels.hypernym.exe.en = """
 * *meat* ``hypernym`` *beef*
 * *edible fruit* ``hypernym`` *pear*
 * *wordbook* ``hypernym`` *dictionary*
"""
synset_rels.hypernym.test.en = """
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
synset_rels.hypernym.com.en="""
This is the fundamental relation, generally used for nouns and
verbs. In the original Princeton WordNet the name 'troponym' was used
for this relation when relating to verbs. In plWordNet it is also
extended to adjectives and adverbs.
"""


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

synset_rels.hyponym.name.en = "Hyponym"
synset_rels.hyponym.df.en = "a word that is more specific than a given word"
synset_rels.hyponym.dfn.en = """
A relation between two concepts where concept B is a type of
concept A."""
synset_rels.hyponym.ex.en = "*dog* is a hyponym of *animal*"
synset_rels.hyponym.exe.en = """
 * *beef* ``hyponym`` *meat*
 * *pear* ``hyponym`` *edible fruit*
 * *dictionary* ``hyponym`` *wordbook*
"""
synset_rels.hyponym.test.en="""
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
synset_rels.hyponym.com.en = """
This is the fundamental relation, generally used for nouns and
verbs. In plWordNet it is also extended to adjectives and adverbs.
"""


### Relation: similar

synset_rels.similar.name.en = "Similar"
synset_rels.similar.df.en = "(of words) expressing closely related meanings"
synset_rels.similar.dfn.en = """
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
synset_rels.similar.ex.en = ""
synset_rels.similar.exe.en = """
"""
synset_rels.similar.com.en = """
This relation coerces PWN Similar to relation for adjectives, Verb
Group relation for verbs and EWN NEAR_SYNONYM for nouns and verbs. In
plWN Similarity relation for adjectives to nouns is a unilateral sense
relation which is why it is not given in the mappings below.
"""


### Relation: role

synset_rels.role.name.en = "Role"
synset_rels.role.df.en = "what something is used for"
synset_rels.role.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
involved in the action or event expressed by concept Y. It is the
supertype of ``agent``, ``instrument``, ``patient``, ``result``,
``location``, ``direction``, ``target_direction``, and
``source_direction``.
"""
synset_rels.role.ex.en = ""
synset_rels.role.exe.en = """
* *hammer* ``role`` *to hammer*
"""
synset_rels.role.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: agent

synset_rels.agent.name.en = "Agent"
synset_rels.agent.df.en = """
the semantic role of the animate entity that instigates or causes the
happening denoted by the verb in the clause
"""
synset_rels.agent.dfn.en = """
X Role Y: (A/an) X is the one/that who/which does the Y, typically
intentionally. X is typically the agent of the action expressed by Y
"""
synset_rels.agent.ex.en = ""
synset_rels.agent.exe.en = """
* *teacher* ``agent`` *to teach*
"""
synset_rels.agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: patient

synset_rels.patient.name.en = "Patient"
synset_rels.patient.df.en = """
the semantic role of an entity that is not the agent but is directly
involved in or affected by the happening denoted by the verb in the
clause
"""
synset_rels.patient.dfn.en = """
X Role Y: (A/an) X is the one/that who/which undergoes the Y.
"""
synset_rels.patient.ex.en = ""
synset_rels.patient.exe.en = """
* *learner* ``patient`` *to learn*
"""
synset_rels.patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: result

synset_rels.result.name.en = "Result"
synset_rels.result.df.en = """
the semantic role of the noun phrase whose referent exists only by
virtue of the activity denoted by the verb in the clause
"""
synset_rels.result.dfn.en = """
X Role Y: (A/an) X is comes into existence as a result of Y or, (A/an)
X is the result of Y or, (A/an) X is created by Y.
"""
synset_rels.result.ex.en = ""
synset_rels.result.exe.en = """
* *crystal* ``result`` *to crystalize*
"""
synset_rels.result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: instrument

synset_rels.instrument.name.en = "Instrument"
synset_rels.instrument.df.en = """
the semantic role of the entity (usually inanimate) that the agent
uses to perform an action or start a process
"""
synset_rels.instrument.dfn.en = """
X Role Y: (A/an) X is either i) the instrument that or ii) what is
used to Y (with)
"""
synset_rels.instrument.ex.en = ""
synset_rels.instrument.exe.en = """
* *hammer* ``instrument`` *to hammer*
* *sail* ``instrument`` *to sail*
* *pen* ``instrument`` *to write*
* *ink* ``instrument`` *to write*
* *paper* ``instrument`` *to write*
"""
synset_rels.instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: location

synset_rels.location.name.en = "Location"
synset_rels.location.df.en = "a point or extent in space"
synset_rels.location.dfn.en = """
X Role Y: A relation between two concepts where concept X is the
location where the action or event expressed by concept Y takes place.
"""
synset_rels.location.ex.en = ""
synset_rels.location.exe.en = """
* *school* ``location`` *to teach*
"""
synset_rels.location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: direction

synset_rels.direction.name.en = "Direction"
synset_rels.direction.df.en = """
a line leading to a place or point
"""
synset_rels.direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
the direction or location of the action or event expressed by concept
Y. It is possible to Y from/to/over/across/through a place (X)
"""
synset_rels.direction.ex.en = ""
synset_rels.direction.exe.en = """
* *place* ``direction`` *pass*
"""
synset_rels.direction.com.en = """
"""


### Relation: target_direction

synset_rels.target_direction.name.en = "Target Direction"
synset_rels.target_direction.df.en = """
the place designated as the end (as of a race or journey)
"""
synset_rels.target_direction.dfn.en = """
X Role Y: (a/an/the) X is the place to which Ying happens / one Ys
"""
synset_rels.target_direction.ex.en = ""
synset_rels.target_direction.exe.en = """
* *ground* ``target_direction`` *to collapse, to fall heavily*
"""
synset_rels.target_direction.com.en = """
"""


### Relation: source_direction

synset_rels.source_direction.name.en = "Source Direction"
synset_rels.source_direction.df.en = """
the place where something begins, where it springs into being
"""
synset_rels.source_direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is the place
from where the action or event expressed by concept Y
begins/starts/happens.
"""
synset_rels.source_direction.ex.en = "start/race"
synset_rels.source_direction.exe.en = """
* *the start* ``source_direction`` *to race*
"""
synset_rels.source_direction.com.en = """
"""


### Relation: involved

synset_rels.involved.name.en = "Involved"
synset_rels.involved.df.en = "connected by participation or association or use"
synset_rels.involved.dfn.en = """
Y involved X: A relation between two concepts where concept Y is
typically involved in the action or event expressed by concept
X. Involved is the supertype of ``involved_agent``,
``involved_patient``, ``involved_result``, ``involved_instrument``,
``involved_location``, ``involved_direction``,
``involved_target_direction``, and ``involved_source_direction``.
"""
synset_rels.involved.ex.en = ""
synset_rels.involved.exe.en = """
* *to hammer* ``involved`` *hammer*
"""
synset_rels.involved.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_agent (EuroWordNet - page 29/30)

synset_rels.involved_agent.name.en = "Involved Agent"
synset_rels.involved_agent.df.en = "X is the typical agent of Y"
synset_rels.involved_agent.dfn.en = """
Y involved X: A relation between two concepts where concept Y is typically
the agent of the action expressed by concept X.
"""
synset_rels.involved_agent.ex.en = "teach/teacher"
synset_rels.involved_agent.exe.en = """
* *to teach* ``involved_agent`` *teacher*
"""
synset_rels.involved_agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_patient

synset_rels.involved_patient.name.en = "Involved Patient"
synset_rels.involved_patient.df.en = "X is typically the patient undergoing the action Y"
synset_rels.involved_patient.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the patient undergoing an action or event expressed by
concept A.
"""
synset_rels.involved_patient.ex.en = "teach/learner"
synset_rels.involved_patient.exe.en = """
"""
synset_rels.involved_patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_result

synset_rels.involved_result.name.en = "Involved Result"
synset_rels.involved_result.df.en = "X exists because of Y"
synset_rels.involved_result.dfn.en = """
Y involved X: A relation between two concepts where concept B comes
into existence as a result of concept A.
"""
synset_rels.involved_result.ex.en = "freeze/ice"
synset_rels.involved_result.exe.en = """
"""
synset_rels.involved_result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_instrument

synset_rels.involved_instrument.name.en = "Involved Instrument"
synset_rels.involved_instrument.df.en = "X is typically the instrument for the action Y"
synset_rels.involved_instrument.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the instrument necessary for the action or event expressed
by concept A.
"""
synset_rels.involved_instrument.ex.en = "paint/paint-brush"
synset_rels.involved_instrument.exe.en = """
"""
synset_rels.involved_instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_location

synset_rels.involved_location.name.en = "Involved Location"
synset_rels.involved_location.df.en = """
X is typically the location where the action Y takes place
"""
synset_rels.involved_location.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the location where the action or event expressed by concept
A takes place.
"""
synset_rels.involved_location.ex.en = "swim/water"
synset_rels.involved_location.exe.en = """
"""
synset_rels.involved_location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_direction

synset_rels.involved_direction.name.en = "Involved Direction"
synset_rels.involved_direction.df.en = """
X is typically the direction/location of the action Y
"""
synset_rels.involved_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the direction or location of the action or event expressed
by concept A.
"""
synset_rels.involved_direction.ex.en = "" ### couldn't find an example
synset_rels.involved_direction.exe.en = """
"""
synset_rels.involved_direction.com.en = """
"""


### Relation: involved_target_direction

synset_rels.involved_target_direction.name.en = "Involved Target Direction"
synset_rels.involved_target_direction.df.en = "X is the place where action Y leads to"
synset_rels.involved_target_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the place
where the action or event expressed by concept A leads to.
"""
synset_rels.involved_target_direction.ex.en = "go back home/home"
synset_rels.involved_target_direction.exe.en = """
"""
synset_rels.involved_target_direction.com.en = """
"""


### Relation: involved_source_direction

synset_rels.involved_source_direction.name.en = "Involved Source Direction"
synset_rels.involved_source_direction.df.en = """
X is the place from where the action Y begins
"""
synset_rels.involved_source_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the
place from where the action or event expressed by concept A
begins/starts/happens.
"""
synset_rels.involved_source_direction.ex.en = "disembark/ship"
synset_rels.involved_source_direction.exe.en = """
"""
synset_rels.involved_source_direction.com.en = """
"""


### Relation: co_role EDP31

synset_rels.co_role.name.en = "Co Role"
synset_rels.co_role.df.en = """
a pair of linked role relations without an explicit event
"""
synset_rels.co_role.dfn.en = """
A relation between two concepts where concept X undergoes an action in
which concept Y is involved (bidirectional).
"""
synset_rels.co_role.ex.en = ""
synset_rels.co_role.exe.en = """
"""
synset_rels.co_role.com.en = """
"""


### Relation: co_agent_patient EDP32

synset_rels.co_agent_patient.name.en = "Co Agent Patient"
synset_rels.co_agent_patient.df.en = "X is the patient undergoing Y"
synset_rels.co_agent_patient.dfn.en = """
A relation between two concepts where concept Y is the patient
undergoing an action carried out by concept X.

Y is the patient undergoing an action carried out by X.
"""
synset_rels.co_agent_patient.ex.en = "novel writer/poet"
synset_rels.co_agent_patient.exe.en = """
"""
synset_rels.co_agent_patient.com.en = """
"""


### Relation: co_agent_instrument EDP32

synset_rels.co_agent_instrument.name.en = "Co Agent Instrument"
synset_rels.co_agent_instrument.df.en = "guitar player/guitar"
synset_rels.co_agent_instrument.dfn.en = """
A relation between two concepts where concept Y is the instrument used
by concept X in a certain action.

Y is the instrument used by X in a certain action
"""
synset_rels.co_agent_instrument.ex.en = ""
synset_rels.co_agent_instrument.exe.en = """
"""
synset_rels.co_agent_instrument.com.en = """
"""


### Relation: co_agent_result EDP32

synset_rels.co_agent_result.name.en = "Co Agent Result"
synset_rels.co_agent_result.df.en = "X is the result of action Y"
synset_rels.co_agent_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by concept X.

Y is the result of an action carried out by X.
"""
synset_rels.co_agent_result.ex.en = "pastry dough/bread dough"
synset_rels.co_agent_result.exe.en = """
"""
synset_rels.co_agent_result.com.en = """
"""


### Relation: co_patient_agent EDP32

synset_rels.co_patient_agent.name.en = "Co Patient Agent"
synset_rels.co_patient_agent.df.en = ""
synset_rels.co_patient_agent.dfn.en = """
A relation between two concepts where concept Y undergoes an action
carried out by concept X.
"""
synset_rels.co_patient_agent.ex.en = "poet/novel writer"
synset_rels.co_patient_agent.exe.en = """
"""
synset_rels.co_patient_agent.com.en = """
"""


### Relation: co_patient_instrument EDP32

synset_rels.co_patient_instrument.name.en = "Co Patient Instrument"
synset_rels.co_patient_instrument.df.en = ""
synset_rels.co_patient_instrument.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
synset_rels.co_patient_instrument.ex.en = "ice/ice saw"
synset_rels.co_patient_instrument.exe.en = """
"""
synset_rels.co_patient_instrument.com.en = """
"""


### Relation: co_result_agent EDP32

synset_rels.co_result_agent.name.en = "Co Result Agent"
synset_rels.co_result_agent.df.en = ""
synset_rels.co_result_agent.dfn.en = """
A relation between two concepts where concept X is the result of an
action carried out by concept Y.
"""
synset_rels.co_result_agent.ex.en = "bread dough/pastry dough"
synset_rels.co_result_agent.exe.en = """
"""
synset_rels.co_result_agent.com.en = """
"""


### Relation: co_result_instrument EDP32

synset_rels.co_result_instrument.name.en = "Co Result Instrument"
synset_rels.co_result_instrument.df.en = ""
synset_rels.co_result_instrument.dfn.en = """
A relation between two concepts where concept X is the result of an
action for which the instrument expressed by concept Y is used.
"""
synset_rels.co_result_instrument.ex.en = "photograph/camera"
synset_rels.co_result_instrument.exe.en = """
"""
synset_rels.co_result_instrument.com.en = """
"""


### Relation: co_instrument_agent EDP32

synset_rels.co_instrument_agent.name.en = "Co Instrument Agent"
synset_rels.co_instrument_agent.df.en = ""
synset_rels.co_instrument_agent.dfn.en = """
A relation between two concepts where concept X is the instrument used
by concept Y for a certain action.
"""
synset_rels.co_instrument_agent.ex.en = "guitar/guitar player"
synset_rels.co_instrument_agent.exe.en = """
"""
synset_rels.co_instrument_agent.com.en = """
"""


### Relation: co_instrument_patient EDP32

synset_rels.co_instrument_patient.name.en = "Co Instrument Patient"
synset_rels.co_instrument_patient.df.en = ""
synset_rels.co_instrument_patient.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
synset_rels.co_instrument_patient.ex.en = "ice saw/ice"
synset_rels.co_instrument_patient.exe.en = """
"""
synset_rels.co_instrument_patient.com.en = """
"""


### Relation: co_instrument_result ice saw/ice

synset_rels.co_instrument_result.name.en = "Co Instrument Result"
synset_rels.co_instrument_result.df.en = ""
synset_rels.co_instrument_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by the instrument expressed by concept X.
"""
synset_rels.co_instrument_result.ex.en = "camera/photograph"
synset_rels.co_instrument_result.exe.en = """
"""
synset_rels.co_instrument_result.com.en = """
"""


### Relation: state_of EDP37

synset_rels.state_of.name.en = "State Of"
synset_rels.state_of.df.en = """
the way something is with respect to its main attributes
"""
synset_rels.state_of.dfn.en = """
A relation between two concepts where concept Y is qualified by
concept X.
"""
synset_rels.state_of.ex.en = "poor/poor (a poor person)"
synset_rels.state_of.exe.en = """
"""
synset_rels.state_of.com.en = """
In plWordNet it is a relation between lexical units.
FCB: isn't this the same as attribute (but split into two directions)
"""


### Relation: be_in_state EDP37

synset_rels.be_in_state.name.en = "Be In State"
synset_rels.be_in_state.df.en = ""
synset_rels.be_in_state.dfn.en = """
A relation between two concepts where concept X is qualified by
concept Y.

X is qualified by Y.
"""
synset_rels.be_in_state.ex.en = "poor (a poor person)/poor"
synset_rels.be_in_state.exe.en = """
"""
synset_rels.be_in_state.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: causes EDP34

synset_rels.causes.name.en = "Causes"
synset_rels.causes.df.en = """
any entity that produces an effect or is responsible for events or
results
"""
synset_rels.causes.dfn.en = """
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
synset_rels.causes.ex.en = "kill/die"
synset_rels.causes.exe.en = """
"""
synset_rels.causes.com.en = """
EUWN's definition of CAUSES is broader than that of PWN. It
seems possible to just absorb PWN's links.
"""


### Relation: is_caused_by EDP34

synset_rels.is_caused_by.name.en = "Is Caused By"
synset_rels.is_caused_by.df.en = ""
synset_rels.is_caused_by.dfn.en = """
A relation between two concepts where concept X comes into existence
as a result of concept Y.
"""
synset_rels.is_caused_by.ex.en = "die/kill"
synset_rels.is_caused_by.exe.en = """
"""
synset_rels.is_caused_by.com.en = """
The 'is caused by' relation was missing from PWN before."""


### Relation: subevent EDP35

synset_rels.subevent.name.en = "Subevent"
synset_rels.subevent.df.en = ""
synset_rels.subevent.dfn.en = """
A relation between two concepts where concept Y takes place
during or as part of concept X, and whenever concept Y takes
place, concept X takes place.

"""
synset_rels.subevent.ex.en = "sleep/snore"
synset_rels.subevent.exe.en = """
"""
synset_rels.subevent.com.en = """
The EUWN CAUSES relation is broader than the PWN in such a
way that it actually includes links that were linked as
ENTAILMENT by the PWN (e.g. to suceed IS_CAUSED_BY to try;
to try CAUSES succeed [non-factive, intention]). This means
that HAS_SUBVENT and IS_SUBVENT_OF should not include every
relation marked as ENTAILMENT by the PWN.

"""


### Relation: is_subevent_of EDP35

synset_rels.is_subevent_of.name.en = "Is Subevent Of"
synset_rels.is_subevent_of.df.en = ""
synset_rels.is_subevent_of.dfn.en = """
A relation between two concepts where concept X takes place
during or as part of concept Y, and whenever concept X takes
place, concept Y takes place.

"""
synset_rels.is_subevent_of.ex.en = "snore/sleep"
synset_rels.is_subevent_of.exe.en = """
"""
synset_rels.is_subevent_of.com.en = """
"""


### Relation: in_manner EDP36

synset_rels.in_manner.name.en = "In Manner"
synset_rels.in_manner.df.en = ""
synset_rels.in_manner.dfn.en = """
A relation between two concepts where concept Y qualifies
the manner in which an action or event expressed by concept
X takes place.

"""
synset_rels.in_manner.ex.en = "slurp/noisely"
synset_rels.in_manner.exe.en = """
"""
synset_rels.in_manner.com.en = """
"""


### Relation: manner_of EDP36

synset_rels.manner_of.name.en = "Manner Of"
synset_rels.manner_of.df.en = "a way of acting or behaving"
synset_rels.manner_of.dfn.en = """
A relation between two concepts where concept X qualifies
the manner in which an action or event expressed by concept
Y takes place.

"""
synset_rels.manner_of.ex.en = "noisely/slurp"
synset_rels.manner_of.exe.en = """
"""
synset_rels.manner_of.com.en = """
"""


### Relation: meronym EDP26

synset_rels.meronym.name.en = "Meronym"
synset_rels.meronym.df.en = """
a word that names a part of a larger whole
"""
synset_rels.meronym.dfn.en = """
A relation between two concepts where concept Y makes up a part of
concept X.
"""
synset_rels.meronym.ex.en = "hand/finger"
synset_rels.meronym.exe.en = """
"""
synset_rels.meronym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: holonym EDP26

synset_rels.holonym.name.en = "Holonym"
synset_rels.holonym.df.en = """
a word that names the whole of which a given word is a part
"""
synset_rels.holonym.dfn.en = """
A relation between two concepts where concept X makes up a
part of concept Y.
"""
synset_rels.holonym.ex.en = "finger/hand"
synset_rels.holonym.exe.en = """
"""
synset_rels.holonym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: mero_part EDP27

synset_rels.mero_part.name.en = "Part Meronym"
synset_rels.mero_part.df.en = ""
synset_rels.mero_part.dfn.en = """
A relation between two concepts where concept Y is a component of
concept X. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
synset_rels.mero_part.ex.en = "car/wheel"
synset_rels.mero_part.exe.en = """
hand > finger

"""
synset_rels.mero_part.com.en = """
This relation is also frequently used by PWN to denote
geographical inclusiveness relations.

"""


### Relation: holo_part EDP27

synset_rels.holo_part.name.en = "Part Holonym"
synset_rels.holo_part.df.en = ""
synset_rels.holo_part.dfn.en = """
A relation between two concepts where concept X is a component of
concept Y. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
synset_rels.holo_part.ex.en = "wheel/car"
synset_rels.holo_part.exe.en = """
"""
synset_rels.holo_part.com.en = """
"""


### Relation: mero_member EPD27

synset_rels.mero_member.name.en = "Member Meronym"
synset_rels.mero_member.df.en = ""
synset_rels.mero_member.dfn.en = """
A relation between two concepts where concept Y is a member/ element
of concept X. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
synset_rels.mero_member.ex.en = "player/team"
synset_rels.mero_member.exe.en = """
fleet > ship

"""
synset_rels.mero_member.com.en = """
"""


### Relation: holo_member EDP27

synset_rels.holo_member.name.en = "Member Holonym"
synset_rels.holo_member.df.en = ""
synset_rels.holo_member.dfn.en = """
A relation between two concepts where concept X is a member/ element
of concept Y. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
synset_rels.holo_member.ex.en = "team/player"
synset_rels.holo_member.exe.en = """
"""
synset_rels.holo_member.com.en = """
"""


### Relation: mero_substance EDP28

synset_rels.mero_substance.name.en = "Substance Meronym"
synset_rels.mero_substance.df.en = ""
synset_rels.mero_substance.dfn.en = """
A relation between two concepts where concept X is made of concept
Y. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
synset_rels.mero_substance.ex.en = "stick/wood"
synset_rels.mero_substance.exe.en = """
book > paper
"""
synset_rels.mero_substance.com.en = """
"""


### Relation: holo_substance EDP28

synset_rels.holo_substance.name.en = "Substance Holonym"
synset_rels.holo_substance.df.en = ""
synset_rels.holo_substance.dfn.en = """
A relation between two concepts where concept Y is made of concept
X. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
synset_rels.holo_substance.ex.en = "wood/stick"
synset_rels.holo_substance.exe.en = """
"""
synset_rels.holo_substance.com.en = """
"""


### Relation: mero_location EDP28

synset_rels.mero_location.name.en = "Location Meronym"
synset_rels.mero_location.df.en = ""
synset_rels.mero_location.dfn.en = """
A relation between two concepts where concept X is a place
located in concept Y.
"""
synset_rels.mero_location.ex.en = "city/centre"
synset_rels.mero_location.exe.en = """
desert > oasis
"""
synset_rels.mero_location.com.en = """
"""


### Relation: holo_location EDP28

synset_rels.holo_location.name.en = "Location Holonym"
synset_rels.holo_location.df.en = ""
synset_rels.holo_location.dfn.en = """
A relation between two concepts where concept Y is a place
located in concept X.
"""
synset_rels.holo_location.ex.en = "centre/city"
synset_rels.holo_location.exe.en = """
"""
synset_rels.holo_location.com.en = """
"""


### Relation: mero_portion EDP27

synset_rels.mero_portion.name.en = "Portion Meronym"
synset_rels.mero_portion.df.en = ""
synset_rels.mero_portion.dfn.en = """
A relation between two concepts where concept X is an
amount/piece/portion of concept Y.
"""
synset_rels.mero_portion.ex.en = "drop/liquid"
synset_rels.mero_portion.exe.en = """
bread > slice
"""
synset_rels.mero_portion.com.en = """
"""


### Relation: holo_portion EDP27

synset_rels.holo_portion.name.en = "Portion Holonym"
synset_rels.holo_portion.df.en = ""
synset_rels.holo_portion.dfn.en = """
A relation between two concepts where concept Y is an
amount/piece/portion of concept X
"""
synset_rels.holo_portion.ex.en = "liquid/drop"
synset_rels.holo_portion.exe.en = """
"""
synset_rels.holo_portion.com.en = """
"""


### Relation: eq_synonym

synset_rels.eq_synonym.name.en = "Equal Synonym"
synset_rels.eq_synonym.df.en = """
two words that can be interchanged in a context are said to be
synonymous relative to that context
"""
synset_rels.eq_synonym.dfn.en = """
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
synset_rels.eq_synonym.ex.en = ""
synset_rels.eq_synonym.exe.en = """
* 一模一样 (70100056-a) EQUALS identical (02068946-a)  identical
* (02068946-a) EQUALS  一模一样 (70100056-a)
"""
synset_rels.eq_synonym.com.en = """
"""


### Relation: instance_hypernym

synset_rels.instance_hypernym.name.en = "Instance Hypernym"
synset_rels.instance_hypernym.df.en = "the type of an instance"
synset_rels.instance_hypernym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
synset_rels.instance_hypernym.ex.en = "*city/Manchester*"
synset_rels.instance_hypernym.exe.en = """"""
synset_rels.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
synset_rels.instance_hypernym.com.en = """
Sometimes modelled as hyponomy/hypernymy relations.
"""


### Relation: instance_hyponym

synset_rels.instance_hyponym.name.en = "Instance Hyponym"
synset_rels.instance_hyponym.df.en = "an occurrence of something"
synset_rels.instance_hyponym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
synset_rels.instance_hyponym.ex.en = ""
synset_rels.instance_hypernym.exe.en = """"""
synset_rels.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
synset_rels.instance_hyponym.exe.en = """
"""
synset_rels.instance_hyponym.com.en = """
"""


### Relation: exemplifies

synset_rels.exemplifies.name.en = "Exemplifies"
synset_rels.exemplifies.df.en = "clarify by giving an example of"
synset_rels.exemplifies.dfn.en = """
A relation between two concepts where Y is a type of concept
X. such as idiom, honorific or classifier.
"""
synset_rels.exemplifies.ex.en = ""
synset_rels.exemplifies.exe.en = """
"""
synset_rels.exemplifies.com.en = """
The name was changed from "Domain of synset - USAGE" as we found it
too different from the standard meaning of domain.
"""


### Relation: is_exemplified_by

synset_rels.is_exemplified_by.name.en = "Is Exemplified By"
synset_rels.is_exemplified_by.df.en = ""
synset_rels.is_exemplified_by.dfn.en = """
A relation between two concepts where A is an example of the type B.
"""
synset_rels.is_exemplified_by.ex.en = ""
synset_rels.is_exemplified_by.exe.en = """
"""
synset_rels.is_exemplified_by.com.en = """
We agreed to change the name for these with Christiane! We
propose 'Exemplified_By'.

"""


### Relation: domain_topic

synset_rels.domain_topic.name.en = "Domain Topic"
synset_rels.domain_topic.df.en = ""
synset_rels.domain_topic.dfn.en = """
A relation between two concepts where Y is a scientific
domain (e.g. computing, sport, biology, etc.) of concept X.
"""
synset_rels.domain_topic.ex.en = ""
synset_rels.domain_topic.exe.en = """
"""
synset_rels.domain_topic.com.en = """
"""


### Relation: has_domain_topic

synset_rels.has_domain_topic.name.en = "Has Domain Topic"
synset_rels.has_domain_topic.df.en = ""
synset_rels.has_domain_topic.dfn.en = """
A relation between two concepts where X is a scientific
domain (e.g. computing, sport, biology, etc.) of concept Y.
"""
synset_rels.has_domain_topic.ex.en = ""
synset_rels.has_domain_topic.exe.en = """
"""
synset_rels.has_domain_topic.com.en = """
"""


### Relation: domain_region

synset_rels.domain_region.name.en = "Domain Region"
synset_rels.domain_region.df.en = ""
synset_rels.domain_region.dfn.en = """
A relation between two concepts where Y is a geographical / cultural
domain of concept X. Domain(Region) and Domain-Term(Region) is a
paired relation between terms/concepts of any part-of-speech and a
related geographical region.
"""
synset_rels.domain_region.ex.en = ""
synset_rels.domain_region.exe.en = """
"""
synset_rels.domain_region.com.en = """
We also agreed to change the name for these (to include both
geographical and cultural regions)! But I'm not sure to
what...
"""


### Relation: has_domain_region

synset_rels.has_domain_region.name.en = "Has Domain Region"
synset_rels.has_domain_region.df.en = ""
synset_rels.has_domain_region.dfn.en = """
A relation between two concepts where X is a geographical /
cultural domain of concept Y.
"""
synset_rels.has_domain_region.ex.en = ""
synset_rels.has_domain_region.exe.en = """
"""
synset_rels.has_domain_region.com.en = """
We have discussed changing the name for these (as they include both
geographical and cultural regions).  But we have not yet come up with
a good name.
"""


### Relation: attribute

synset_rels.attribute.name.en = "Attribute"
synset_rels.attribute.df.en = """
an abstraction belonging to or characteristic of an entity
"""
synset_rels.attribute.dfn.en = """
A relation between nominal and adjectival concepts where the concept X
is an attribute of concept Y. ‘Attributes’ is a self-reciprocal link
(the two directions of this relation share the same meaning) —
Concept-X attributes to Concept-Y, and Concept-Y attributes to
Concept-X.

It denotes a relation between a noun and its adjectival attributes,
and vice-versa — for this reason it should only link adjectives to
nouns and vice-versa.
"""
synset_rels.attribute.ex.en = ""
synset_rels.attribute.exe.en = """
* fertile (01001689-a) ATTRIBUTES:  fertility (14051494-n)
* fertility (14051494-n) ATTRIBUTES: fertile (01001689-a)
"""
synset_rels.attribute.com.en = """
In plWN Value_of_the_attribute is a unilateral relation from
adjectives to nouns.
"""


### Relation: restricts

synset_rels.restricts.name.en = "Restricts"
synset_rels.restricts.df.en = """
place limits on (extent or amount or access)
"""
synset_rels.restricts.dfn.en = """
A relation between an adjectival concept X (quantifier/determiner) and
a nominal (pronominal) concept Y.
"""
synset_rels.restricts.ex.en = ""
synset_rels.restricts.exe.en = """
"""
synset_rels.restricts.com.en = """
This would work for features like 'medial' or 'proximal' in
pronouns, or 'every' in everybody, or 'male' for male
personal pronouns, but not masculine agreeement in gendered
languages. This relation will include some things that are
now marked as domain usage. (to be corrected soon'ish)
"""


### Relation: restricted_by

synset_rels.restricted_by.name.en = "Restricted By"
synset_rels.restricted_by.df.en = ""
synset_rels.restricted_by.dfn.en = """
A relation between nominal (pronominal) concept Y and an
adjectival concept X (quantifier/determiner).
"""
synset_rels.restricted_by.ex.en = ""
synset_rels.restricted_by.exe.en = """
* this-a (77000061-a) QUANTIFIES [qant] this-n (77000061-n)
* this-n (77000061-n) QUANTIFIER: [hasq] this-a (77000061-a)
"""
synset_rels.restricted_by.com.en = """
"""


### Relation: classifies

synset_rels.classifies.name.en = "Classifies"
synset_rels.classifies.df.en = """
assign to a class or kind
"""
synset_rels.classifies.dfn.en = """
A relation between a classifier concept X and concept Y. A relation
between a classifier X and Y
"""
synset_rels.classifies.ex.en = ""
synset_rels.classifies.exe.en = """
"""
synset_rels.classifies.com.en = """
currently we only have links for nominal concepts, but we
will do it for other POS (e.g. v)
"""


### Relation: classified_by

synset_rels.classified_by.name.en = "Classified By"
synset_rels.classified_by.df.en = """
arrange or order by classes or categories
"""
synset_rels.classified_by.dfn.en = """
A relation between concept Y and a classifier concept X. A relation
between Y and a classifier X
"""
synset_rels.classified_by.ex.en = ""
synset_rels.classified_by.exe.en = """
"""
synset_rels.classified_by.com.en = """
"""


### Relation: also (no ili)

synset_rels.also.name.en = "See also"
synset_rels.also.df.en = """
a word having a loose or fuzzy semantic relation to another word
"""
synset_rels.also.dfn.en = """
‘See Also’ is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-X relates to Concept-Y, and
Concept-Y relates to Concept-X.

It denotes a relation of related meaning with another concept (going
beyond synonymy and similarity).

This link was originally used to relate adjectives, but we have
unconstrained this use, and we're making use of this link to relate
all parts-of-speech.
"""
synset_rels.also.ex.en = ""
synset_rels.also.exe.en = """
"""
synset_rels.also.com.en = """
Also known as fuzzynym
"""


### Relation: antonym

synset_rels.antonym.name.en = "Antonym"
synset_rels.antonym.df.en = """
a word that expresses a meaning opposed to the meaning of another
word, in which case the two words are antonyms of each other
"""
synset_rels.antonym.dfn.en = """
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
synset_rels.antonym.ex.en = ""
synset_rels.antonym.exe.en = """
"""
synset_rels.antonym.com.en = """
It is primarily a relation between senses, but sense level antonymy
implies a looser synset level relation, which we automatically add to
make it avaiable for wordnets that do not yet have sense level links.
"""


### Relation: entails

synset_rels.entails.name.en = "Entails"
synset_rels.entails.df.en = """
impose, involve, or imply as a necessary accompaniment or result
"""
synset_rels.entails.dfn.en = """
Entailment is a relation that links two verbs, and it is currently
unilateral — Verb-X entails Verb-Y, without a reciprocal or tracing
link.  This relation presupposes/requires a semantic restriction in
which Verb-Y has to take place before or during Verb-X.
"""
synset_rels.entails.ex.en = ""
synset_rels.entails.exe.en = """
"""
synset_rels.entails.com.en = """
"""


### Relation: is_entailed_by

synset_rels.is_entailed_by.name.en = "Is Entailed By"
synset_rels.is_entailed_by.df.en = ""
synset_rels.is_entailed_by.dfn.en = """
"""
synset_rels.is_entailed_by.ex.en = ""
synset_rels.is_entailed_by.exe.en = """
"""
synset_rels.is_entailed_by.com.en = """
"""


### Relation: other

synset_rels.other.name.en = "Other"
synset_rels.other.df.en = "any other semantic relation"
synset_rels.other.dfn.en = """
This is used for semantic relation types not currently supported by
the OMW DTD.  The exact relation type can be given with ``dc:type``:

.. code:: xml

    <SynsetRelation relType="other" dc:type="emotion" target="example-en-1234-n"/>

"""
synset_rels.other.ex.en = ""
synset_rels.other.exe.en = """
"""
synset_rels.other.com.en = """
Because we don't know what it means, we cannot give it a reverse relation.
"""


### New short definitions based on http://globalwordnet.github.io/schemas/

synset_rels.agent.df.en = "X is typically the agent of the action expressed by Y"
synset_rels.antonym.df.en = "An opposite and inherently incompatible word"
synset_rels.be_in_state.df.en = "X is qualified by Y"
synset_rels.classified_by.df.en = "A relation between Y and a classifier X"
synset_rels.classifies.df.en = "A relation between a classifier X and Y"
synset_rels.co_agent_instrument.df.en = "Y is the instrument used by X in a certain action"
synset_rels.co_agent_patient.df.en = "Y is the patient undergoing an action carried out by X"
synset_rels.co_agent_result.df.en = "Y is the result of an action carried out by X"
synset_rels.co_instrument_agent.df.en = "X is the instrument used by Y for a certain action"
synset_rels.co_instrument_patient.df.en = "Y undergoes an action for which the instrument expressed by X is used"
synset_rels.co_instrument_result.df.en = "Y is the result of an action carried out by the instrument expressed by X"
synset_rels.co_patient_agent.df.en = "Y undergoes an action carried out by X"
synset_rels.co_patient_instrument.df.en = "X undergoes an action for which the instrument expressed by X is used"
synset_rels.co_result_agent.df.en = "X is the result of an action carried out by Y"
synset_rels.co_result_instrument.df.en = "X is the result of an action for which the instrument expressed by Y is used"
synset_rels.co_role.df.en = "One concept undergoes an action in which the other concept is involved (bidirectional)"
synset_rels.direction.df.en = "X is typically the direction or location of the action or event expressed by Y"
synset_rels.eq_synonym.df.en = "X and Y are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)"
synset_rels.holo_location.df.en = "Y is a place located in X"
synset_rels.holo_portion.df.en = "Y is an amount/piece/portion of X"
synset_rels.holonym.df.en = "X makes up a part of Y"
synset_rels.in_manner.df.en = "Y qualifies the manner in which an action or event expressed by X takes place"
synset_rels.instrument.df.en = "X is the instrument necessary for the action or event expressed by Y"
synset_rels.involved_agent.df.en = "Y is typically the agent of the action expressed by X"
synset_rels.involved_direction.df.en = "Y is typically the direction or location of the action or event expressed by X"
synset_rels.involved_instrument.df.en = "Y is typically the instrument necessary for the action or event expressed by X"
synset_rels.involved_location.df.en = "Y is typically the location where the action or event expressed by X takes place"
synset_rels.involved_patient.df.en = "Y is typically the patient un-dergoing an action or event expressed by X"
synset_rels.involved_result.df.en = "Y comes into existence as a result of X"
synset_rels.involved_source_direction.df.en = "Y is the place from where the action or event expressed by X begins/starts/happens"
synset_rels.involved_target_direction.df.en = "Y is the place where the action or event expressed by X leads to"
synset_rels.involved.df.en = "Y is typically involved in the action or event expressed by X"
synset_rels.is_caused_by.df.en = "X comes about because of Y"
synset_rels.is_entailed_by.df.en = "Opposite of entails"
synset_rels.is_subevent_of.df.en = "X takes place during or as part of Y, and whenever X takes place, Y takes place"
synset_rels.location.df.en = "X is the location where the action or event expressed by Y takes place"
synset_rels.manner_of.df.en = "X qualifies the manner in which an action or event expressed by Y takes place"
synset_rels.mero_location.df.en = "X is a place located in Y"
synset_rels.mero_portion.df.en = "X is an amount/piece/portion of Y"
synset_rels.meronym.df.en = "Y makes up a part of X"
synset_rels.other.df.en = "Any relation not otherwise specified"
synset_rels.patient.df.en = "X is the patient undergoing an action or event expressed by Y"
#rels.pertainym.df.en =  "X is of or pertaining to Y"
synset_rels.restricted_by.df.en = "A relation between nominal (pronominal) Y and an adjectival X (quantifier/determiner)"
synset_rels.restricts.df.en = "A relation between an adjectival X (quantifier/determiner) and a nominal (pronominal) Y"
synset_rels.result.df.en = "X comes into existence as a result of Y"
synset_rels.role.df.en = "X is typically involved in the action or event expressed by Y"
synset_rels.source_direction.df.en = "X is the place from where the event expressed by Y begins"
synset_rels.state_of.df.en = "Y is qualified by X"
synset_rels.subevent.df.en = "Y takes place during or as part of X, and whenever Y takes place, X takes place"
synset_rels.target_direction.df.en = "X is the place to which the action or event expressed by Y leads"
