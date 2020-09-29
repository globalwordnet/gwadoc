# -*- coding: utf-8 -*-

from gwadoc import relations


###############################################################################
### Relations Definitions


### Relation: domain

relations.domain.name.en = "Domain"


### Relation: has_domain

relations.has_domain.name.en = "In Domain"


### Relation: constitutive

relations.constitutive.name.en = "Constitutive"
relations.constitutive.df.en = "Core semantic relations that define synsets"
relations.constitutive.dfn.en = """
Core semantic relations that define synsets.

We follow the discussion in [Maziarz:Piasecki:Szpakowicz:2013]_

.. [Maziarz:Piasecki:Szpakowicz:2013] The chicken-and-egg problem in
   wordnet design: synonymy, synsets and constitutive relations.
   Language Resources and Evaluation, 47(3), pp 769–79
"""


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

relations.hypernym.name.en = 'Hypernym'
relations.hypernym.df.en = 'a word that is more general than a given word'
relations.hypernym.dfn.en = """
A hypernym of something is its superordinate term:
if X is a hypernym of Y, then all Y are X.
"""
relations.hypernym.ex.en = "*animal* is a hypernym of *dog*"
relations.hypernym.exe.en = """
 * *meat* ``hypernym`` *beef*
 * *edible fruit* ``hypernym`` *pear*
 * *wordbook* ``hypernym`` *dictionary*
"""
relations.hypernym.test.en = """
Hyperonymy/hyponymy between verb synsets ([EWN]_ test 11, p23)

===     =   ===================================
yes     a   *to X is to Y + AdvP/AdjP/NP/PP*
no      b   *to Y is to X + AdvP/AdjP/NP/PP*
===     =   ===================================

Conditions:
 - X is a verb in the infinitive form
 - Y is a verb in the infinitive form
 - there is at least one specifying modifier (AdvP, NP or PP) that
   applies to the Y-phrase

.. [EWN] Piek Vossen (ed.) (1999) `Euro Wordnet General Documentation <https://globalwordnet.github.io/gwadoc/pdf/EWN_general.pdf>`_ University of Amsterdam

"""
relations.hypernym.com.en="""
This is the fundamental relation, generally used for nouns and
verbs. In the original Princeton WordNet the name 'troponym' was used
for this relation when relating to verbs. In plWordNet it is also
extended to adjectives and adverbs.
"""


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

relations.hyponym.name.en = "Hyponym"
relations.hyponym.df.en = "a word that is more specific than a given word"
relations.hyponym.dfn.en = """
A relation between two concepts where concept B is a type of
concept A."""
relations.hyponym.ex.en = "*dog* is a hyponym of *animal*"
relations.hyponym.exe.en = """
 * *beef* ``hyponym`` *meat*
 * *pear* ``hyponym`` *edible fruit*
 * *dictionary* ``hyponym`` *wordbook*
"""
relations.hyponym.test.en="""
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
relations.hyponym.com.en = """
This is the fundamental relation, generally used for nouns and
verbs. In plWordNet it is also extended to adjectives and adverbs.
"""


### Relation: similar

relations.similar.name.en = "Similar"
relations.similar.df.en = "(of words) expressing closely related meanings"
relations.similar.dfn.en = """
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
relations.similar.ex.en = ""
relations.similar.exe.en = """
"""
relations.similar.com.en = """
This relation coerces PWN Similar to relation for adjectives, Verb
Group relation for verbs and EWN NEAR_SYNONYM for nouns and verbs. In
plWN Similarity relation for adjectives to nouns is a unilateral sense
relation which is why it is not given in the mappings below.
"""


### Relation: role

relations.role.name.en = "Role"
relations.role.df.en = "what something is used for"
relations.role.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
involved in the action or event expressed by concept Y. It is the
supertype of ``agent``, ``instrument``, ``patient``, ``result``,
``location``, ``direction``, ``target_direction``, and
``source_direction``.
"""
relations.role.ex.en = ""
relations.role.exe.en = """
* *hammer* ``role`` *to hammer*
"""
relations.role.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: agent

relations.agent.name.en = "Agent"
relations.agent.df.en = """
the semantic role of the animate entity that instigates or causes the
happening denoted by the verb in the clause
"""
relations.agent.dfn.en = """
X Role Y: (A/an) X is the one/that who/which does the Y, typically
intentionally. X is typically the agent of the action expressed by Y
"""
relations.agent.ex.en = ""
relations.agent.exe.en = """
* *teacher* ``agent`` *to teach*
"""
relations.agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: patient

relations.patient.name.en = "Patient"
relations.patient.df.en = """
the semantic role of an entity that is not the agent but is directly
involved in or affected by the happening denoted by the verb in the
clause
"""
relations.patient.dfn.en = """
X Role Y: (A/an) X is the one/that who/which undergoes the Y.
"""
relations.patient.ex.en = ""
relations.patient.exe.en = """
* *learner* ``patient`` *to learn*
"""
relations.patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: result

relations.result.name.en = "Result"
relations.result.df.en = """
the semantic role of the noun phrase whose referent exists only by
virtue of the activity denoted by the verb in the clause
"""
relations.result.dfn.en = """
X Role Y: (A/an) X is comes into existence as a result of Y or, (A/an)
X is the result of Y or, (A/an) X is created by Y.
"""
relations.result.ex.en = ""
relations.result.exe.en = """
* *crystal* ``result`` *to crystalize*
"""
relations.result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: instrument

relations.instrument.name.en = "Instrument"
relations.instrument.df.en = """
the semantic role of the entity (usually inanimate) that the agent
uses to perform an action or start a process
"""
relations.instrument.dfn.en = """
X Role Y: (A/an) X is either i) the instrument that or ii) what is
used to Y (with)
"""
relations.instrument.ex.en = ""
relations.instrument.exe.en = """
* *hammer* ``instrument`` *to hammer*
* *sail* ``instrument`` *to sail*
* *pen* ``instrument`` *to write*
* *ink* ``instrument`` *to write*
* *paper* ``instrument`` *to write*
"""
relations.instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: location

relations.location.name.en = "Location"
relations.location.df.en = "a point or extent in space"
relations.location.dfn.en = """
X Role Y: A relation between two concepts where concept X is the
location where the action or event expressed by concept Y takes place.
"""
relations.location.ex.en = ""
relations.location.exe.en = """
* *school* ``location`` *to teach*
"""
relations.location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: direction

relations.direction.name.en = "Direction"
relations.direction.df.en = """
a line leading to a place or point
"""
relations.direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is typically
the direction or location of the action or event expressed by concept
Y. It is possible to Y from/to/over/across/through a place (X)
"""
relations.direction.ex.en = ""
relations.direction.exe.en = """
* *place* ``direction`` *pass*
"""
relations.direction.com.en = """
"""


### Relation: target_direction

relations.target_direction.name.en = "Target Direction"
relations.target_direction.df.en = """
the place designated as the end (as of a race or journey)
"""
relations.target_direction.dfn.en = """
X Role Y: (a/an/the) X is the place to which Ying happens / one Ys
"""
relations.target_direction.ex.en = ""
relations.target_direction.exe.en = """
* *ground* ``target_direction`` *to collapse, to fall heavily*
"""
relations.target_direction.com.en = """
"""


### Relation: source_direction

relations.source_direction.name.en = "Source Direction"
relations.source_direction.df.en = """
the place where something begins, where it springs into being
"""
relations.source_direction.dfn.en = """
X Role Y: A relation between two concepts where concept X is the place
from where the action or event expressed by concept Y
begins/starts/happens.
"""
relations.source_direction.ex.en = "start/race"
relations.source_direction.exe.en = """
* *the start* ``source_direction`` *to race*
"""
relations.source_direction.com.en = """
"""


### Relation: involved

relations.involved.name.en = "Involved"
relations.involved.df.en = "connected by participation or association or use"
relations.involved.dfn.en = """
Y involved X: A relation between two concepts where concept Y is
typically involved in the action or event expressed by concept
X. Involved is the supertype of ``involved_agent``,
``involved_patient``, ``involved_result``, ``involved_instrument``,
``involved_location``, ``involved_direction``,
``involved_target_direction``, and ``involved_source_direction``.
"""
relations.involved.ex.en = ""
relations.involved.exe.en = """
* *to hammer* ``involved`` *hammer*
"""
relations.involved.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_agent (EuroWordNet - page 29/30)

relations.involved_agent.name.en = "Involved Agent"
relations.involved_agent.df.en = "X is the typical agent of Y"
relations.involved_agent.dfn.en = """
Y involved X: A relation between two concepts where concept Y is typically
the agent of the action expressed by concept X.
"""
relations.involved_agent.ex.en = "teach/teacher"
relations.involved_agent.exe.en = """
* *to teach* ``involved_agent`` *teacher*
"""
relations.involved_agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_patient

relations.involved_patient.name.en = "Involved Patient"
relations.involved_patient.df.en = "X is typically the patient undergoing the action Y"
relations.involved_patient.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the patient undergoing an action or event expressed by
concept A.
"""
relations.involved_patient.ex.en = "teach/learner"
relations.involved_patient.exe.en = """
"""
relations.involved_patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_result

relations.involved_result.name.en = "Involved Result"
relations.involved_result.df.en = "X exists because of Y"
relations.involved_result.dfn.en = """
Y involved X: A relation between two concepts where concept B comes
into existence as a result of concept A.
"""
relations.involved_result.ex.en = "freeze/ice"
relations.involved_result.exe.en = """
"""
relations.involved_result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_instrument

relations.involved_instrument.name.en = "Involved Instrument"
relations.involved_instrument.df.en = "X is typically the instrument for the action Y"
relations.involved_instrument.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the instrument necessary for the action or event expressed
by concept A.
"""
relations.involved_instrument.ex.en = "paint/paint-brush"
relations.involved_instrument.exe.en = """
"""
relations.involved_instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_location

relations.involved_location.name.en = "Involved Location"
relations.involved_location.df.en = """
X is typically the location where the action Y takes place
"""
relations.involved_location.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the location where the action or event expressed by concept
A takes place.
"""
relations.involved_location.ex.en = "swim/water"
relations.involved_location.exe.en = """
"""
relations.involved_location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_direction

relations.involved_direction.name.en = "Involved Direction"
relations.involved_direction.df.en = """
X is typically the direction/location of the action Y
"""
relations.involved_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is
typically the direction or location of the action or event expressed
by concept A.
"""
relations.involved_direction.ex.en = "" ### couldn't find an example
relations.involved_direction.exe.en = """
"""
relations.involved_direction.com.en = """
"""


### Relation: involved_target_direction

relations.involved_target_direction.name.en = "Involved Target Direction"
relations.involved_target_direction.df.en = "X is the place where action Y leads to"
relations.involved_target_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the place
where the action or event expressed by concept A leads to.
"""
relations.involved_target_direction.ex.en = "go back home/home"
relations.involved_target_direction.exe.en = """
"""
relations.involved_target_direction.com.en = """
"""


### Relation: involved_source_direction

relations.involved_source_direction.name.en = "Involved Source Direction"
relations.involved_source_direction.df.en = """
X is the place from where the action Y begins
"""
relations.involved_source_direction.dfn.en = """
Y involved X: A relation between two concepts where concept B is the
place from where the action or event expressed by concept A
begins/starts/happens.
"""
relations.involved_source_direction.ex.en = "disembark/ship"
relations.involved_source_direction.exe.en = """
"""
relations.involved_source_direction.com.en = """
"""


### Relation: co_role EDP31

relations.co_role.name.en = "Co Role"
relations.co_role.df.en = """
a pair of linked role relations without an explicit event
"""
relations.co_role.dfn.en = """
A relation between two concepts where concept X undergoes an action in
which concept Y is involved (bidirectional).
"""
relations.co_role.ex.en = ""
relations.co_role.exe.en = """
"""
relations.co_role.com.en = """
"""


### Relation: co_agent_patient EDP32

relations.co_agent_patient.name.en = "Co Agent Patient"
relations.co_agent_patient.df.en = "X is the patient undergoing Y"
relations.co_agent_patient.dfn.en = """
A relation between two concepts where concept Y is the patient
undergoing an action carried out by concept X.

Y is the patient undergoing an action carried out by X.
"""
relations.co_agent_patient.ex.en = "novel writer/poet"
relations.co_agent_patient.exe.en = """
"""
relations.co_agent_patient.com.en = """
"""


### Relation: co_agent_instrument EDP32

relations.co_agent_instrument.name.en = "Co Agent Instrument"
relations.co_agent_instrument.df.en = "guitar player/guitar"
relations.co_agent_instrument.dfn.en = """
A relation between two concepts where concept Y is the instrument used
by concept X in a certain action.

Y is the instrument used by X in a certain action
"""
relations.co_agent_instrument.ex.en = ""
relations.co_agent_instrument.exe.en = """
"""
relations.co_agent_instrument.com.en = """
"""


### Relation: co_agent_result EDP32

relations.co_agent_result.name.en = "Co Agent Result"
relations.co_agent_result.df.en = "X is the result of action Y"
relations.co_agent_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by concept X.

Y is the result of an action carried out by X.
"""
relations.co_agent_result.ex.en = "pastry dough/bread dough"
relations.co_agent_result.exe.en = """
"""
relations.co_agent_result.com.en = """
"""


### Relation: co_patient_agent EDP32

relations.co_patient_agent.name.en = "Co Patient Agent"
relations.co_patient_agent.df.en = ""
relations.co_patient_agent.dfn.en = """
A relation between two concepts where concept Y undergoes an action
carried out by concept X.
"""
relations.co_patient_agent.ex.en = "poet/novel writer"
relations.co_patient_agent.exe.en = """
"""
relations.co_patient_agent.com.en = """
"""


### Relation: co_patient_instrument EDP32

relations.co_patient_instrument.name.en = "Co Patient Instrument"
relations.co_patient_instrument.df.en = ""
relations.co_patient_instrument.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
relations.co_patient_instrument.ex.en = "ice/ice saw"
relations.co_patient_instrument.exe.en = """
"""
relations.co_patient_instrument.com.en = """
"""


### Relation: co_result_agent EDP32

relations.co_result_agent.name.en = "Co Result Agent"
relations.co_result_agent.df.en = ""
relations.co_result_agent.dfn.en = """
A relation between two concepts where concept X is the result of an
action carried out by concept Y.
"""
relations.co_result_agent.ex.en = "bread dough/pastry dough"
relations.co_result_agent.exe.en = """
"""
relations.co_result_agent.com.en = """
"""


### Relation: co_result_instrument EDP32

relations.co_result_instrument.name.en = "Co Result Instrument"
relations.co_result_instrument.df.en = ""
relations.co_result_instrument.dfn.en = """
A relation between two concepts where concept X is the result of an
action for which the instrument expressed by concept Y is used.
"""
relations.co_result_instrument.ex.en = "photograph/camera"
relations.co_result_instrument.exe.en = """
"""
relations.co_result_instrument.com.en = """
"""


### Relation: co_instrument_agent EDP32

relations.co_instrument_agent.name.en = "Co Instrument Agent"
relations.co_instrument_agent.df.en = ""
relations.co_instrument_agent.dfn.en = """
A relation between two concepts where concept X is the instrument used
by concept Y for a certain action.
"""
relations.co_instrument_agent.ex.en = "guitar/guitar player"
relations.co_instrument_agent.exe.en = """
"""
relations.co_instrument_agent.com.en = """
"""


### Relation: co_instrument_patient EDP32

relations.co_instrument_patient.name.en = "Co Instrument Patient"
relations.co_instrument_patient.df.en = ""
relations.co_instrument_patient.dfn.en = """
A relation between two concepts where concept Y undergoes an action
for which the instrument expressed by concept X is used.
"""
relations.co_instrument_patient.ex.en = "ice saw/ice"
relations.co_instrument_patient.exe.en = """
"""
relations.co_instrument_patient.com.en = """
"""


### Relation: co_instrument_result ice saw/ice

relations.co_instrument_result.name.en = "Co Instrument Result"
relations.co_instrument_result.df.en = ""
relations.co_instrument_result.dfn.en = """
A relation between two concepts where concept Y is the result of an
action carried out by the instrument expressed by concept X.
"""
relations.co_instrument_result.ex.en = "camera/photograph"
relations.co_instrument_result.exe.en = """
"""
relations.co_instrument_result.com.en = """
"""


### Relation: state_of EDP37

relations.state_of.name.en = "State Of"
relations.state_of.df.en = """
the way something is with respect to its main attributes
"""
relations.state_of.dfn.en = """
A relation between two concepts where concept Y is qualified by
concept X.
"""
relations.state_of.ex.en = "poor/poor (a poor person)"
relations.state_of.exe.en = """
"""
relations.state_of.com.en = """
In plWordNet it is a relation between lexical units.
FCB: isn't this the same as attribute (but split into two directions)
"""


### Relation: be_in_state EDP37

relations.be_in_state.name.en = "Be In State"
relations.be_in_state.df.en = ""
relations.be_in_state.dfn.en = """
A relation between two concepts where concept X is qualified by
concept Y.

X is qualified by Y.
"""
relations.be_in_state.ex.en = "poor (a poor person)/poor"
relations.be_in_state.exe.en = """
"""
relations.be_in_state.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: causes EDP34

relations.causes.name.en = "Causes"
relations.causes.df.en = """
any entity that produces an effect or is responsible for events or
results
"""
relations.causes.dfn.en = """
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
relations.causes.ex.en = "kill/die"
relations.causes.exe.en = """
"""
relations.causes.com.en = """
EUWN's definition of CAUSES is broader than that of PWN. It
seems possible to just absorb PWN's links.
"""


### Relation: is_caused_by EDP34

relations.is_caused_by.name.en = "Is Caused By"
relations.is_caused_by.df.en = ""
relations.is_caused_by.dfn.en = """
A relation between two concepts where concept X comes into existence
as a result of concept Y.
"""
relations.is_caused_by.ex.en = "die/kill"
relations.is_caused_by.exe.en = """
"""
relations.is_caused_by.com.en = """
The 'is caused by' relation was missing from PWN before."""


### Relation: subevent EDP35

relations.subevent.name.en = "Subevent"
relations.subevent.df.en = ""
relations.subevent.dfn.en = """
A relation between two concepts where concept Y takes place
during or as part of concept X, and whenever concept Y takes
place, concept X takes place.

"""
relations.subevent.ex.en = "sleep/snore"
relations.subevent.exe.en = """
"""
relations.subevent.com.en = """
The EUWN CAUSES relation is broader than the PWN in such a
way that it actually includes links that were linked as
ENTAILMENT by the PWN (e.g. to suceed IS_CAUSED_BY to try;
to try CAUSES succeed [non-factive, intention]). This means
that HAS_SUBVENT and IS_SUBVENT_OF should not include every
relation marked as ENTAILMENT by the PWN.

"""


### Relation: is_subevent_of EDP35

relations.is_subevent_of.name.en = "Is Subevent Of"
relations.is_subevent_of.df.en = ""
relations.is_subevent_of.dfn.en = """
A relation between two concepts where concept X takes place
during or as part of concept Y, and whenever concept X takes
place, concept Y takes place.

"""
relations.is_subevent_of.ex.en = "snore/sleep"
relations.is_subevent_of.exe.en = """
"""
relations.is_subevent_of.com.en = """
"""


### Relation: in_manner EDP36

relations.in_manner.name.en = "In Manner"
relations.in_manner.df.en = ""
relations.in_manner.dfn.en = """
A relation between two concepts where concept Y qualifies
the manner in which an action or event expressed by concept
X takes place.

"""
relations.in_manner.ex.en = "slurp/noisely"
relations.in_manner.exe.en = """
"""
relations.in_manner.com.en = """
"""


### Relation: manner_of EDP36

relations.manner_of.name.en = "Manner Of"
relations.manner_of.df.en = "a way of acting or behaving"
relations.manner_of.dfn.en = """
A relation between two concepts where concept X qualifies
the manner in which an action or event expressed by concept
Y takes place.

"""
relations.manner_of.ex.en = "noisely/slurp"
relations.manner_of.exe.en = """
"""
relations.manner_of.com.en = """
"""


### Relation: meronym EDP26

relations.meronym.name.en = "Meronym"
relations.meronym.df.en = """
a word that names a part of a larger whole
"""
relations.meronym.dfn.en = """
A relation between two concepts where concept Y makes up a part of
concept X.
"""
relations.meronym.ex.en = "hand/finger"
relations.meronym.exe.en = """
"""
relations.meronym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: holonym EDP26

relations.holonym.name.en = "Holonym"
relations.holonym.df.en = """
a word that names the whole of which a given word is a part
"""
relations.holonym.dfn.en = """
A relation between two concepts where concept X makes up a
part of concept Y.
"""
relations.holonym.ex.en = "finger/hand"
relations.holonym.exe.en = """
"""
relations.holonym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: mero_part EDP27

relations.mero_part.name.en = "Part Meronym"
relations.mero_part.df.en = ""
relations.mero_part.dfn.en = """
A relation between two concepts where concept Y is a component of
concept X. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
relations.mero_part.ex.en = "car/wheel"
relations.mero_part.exe.en = """
hand > finger

"""
relations.mero_part.com.en = """
This relation is also frequently used by PWN to denote
geographical inclusiveness relations.

"""


### Relation: holo_part EDP27

relations.holo_part.name.en = "Part Holonym"
relations.holo_part.df.en = ""
relations.holo_part.dfn.en = """
A relation between two concepts where concept X is a component of
concept Y. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-X can be
separated into Concept-Y”; and Concept-Y is a part of some Concept-X.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
relations.holo_part.ex.en = "wheel/car"
relations.holo_part.exe.en = """
"""
relations.holo_part.com.en = """
"""


### Relation: mero_member EPD27

relations.mero_member.name.en = "Member Meronym"
relations.mero_member.df.en = ""
relations.mero_member.dfn.en = """
A relation between two concepts where concept Y is a member/ element
of concept X. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
relations.mero_member.ex.en = "player/team"
relations.mero_member.exe.en = """
fleet > ship

"""
relations.mero_member.com.en = """
"""


### Relation: holo_member EDP27

relations.holo_member.name.en = "Member Holonym"
relations.holo_member.df.en = ""
relations.holo_member.dfn.en = """
A relation between two concepts where concept X is a member/ element
of concept Y. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a subkind of a concept. It links groups to members
— Concept-Y is composed of many members of Concept-X; and many
instances of Concept-X form Concept-Y.
"""
relations.holo_member.ex.en = "team/player"
relations.holo_member.exe.en = """
"""
relations.holo_member.com.en = """
"""


### Relation: mero_substance EDP28

relations.mero_substance.name.en = "Substance Meronym"
relations.mero_substance.df.en = ""
relations.mero_substance.dfn.en = """
A relation between two concepts where concept X is made of concept
Y. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
relations.mero_substance.ex.en = "stick/wood"
relations.mero_substance.exe.en = """
book > paper
"""
relations.mero_substance.com.en = """
"""


### Relation: holo_substance EDP28

relations.holo_substance.name.en = "Substance Holonym"
relations.holo_substance.df.en = ""
relations.holo_substance.dfn.en = """
A relation between two concepts where concept Y is made of concept
X. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-X is made of Concept-Y; and
Concept-Y is a substance of Concept-X”.
"""
relations.holo_substance.ex.en = "wood/stick"
relations.holo_substance.exe.en = """
"""
relations.holo_substance.com.en = """
"""


### Relation: mero_location EDP28

relations.mero_location.name.en = "Location Meronym"
relations.mero_location.df.en = ""
relations.mero_location.dfn.en = """
A relation between two concepts where concept X is a place
located in concept Y.
"""
relations.mero_location.ex.en = "city/centre"
relations.mero_location.exe.en = """
desert > oasis
"""
relations.mero_location.com.en = """
"""


### Relation: holo_location EDP28

relations.holo_location.name.en = "Location Holonym"
relations.holo_location.df.en = ""
relations.holo_location.dfn.en = """
A relation between two concepts where concept Y is a place
located in concept X.
"""
relations.holo_location.ex.en = "centre/city"
relations.holo_location.exe.en = """
"""
relations.holo_location.com.en = """
"""


### Relation: mero_portion EDP27

relations.mero_portion.name.en = "Portion Meronym"
relations.mero_portion.df.en = ""
relations.mero_portion.dfn.en = """
A relation between two concepts where concept X is an
amount/piece/portion of concept Y.
"""
relations.mero_portion.ex.en = "drop/liquid"
relations.mero_portion.exe.en = """
bread > slice
"""
relations.mero_portion.com.en = """
"""


### Relation: holo_portion EDP27

relations.holo_portion.name.en = "Portion Holonym"
relations.holo_portion.df.en = ""
relations.holo_portion.dfn.en = """
A relation between two concepts where concept Y is an
amount/piece/portion of concept X
"""
relations.holo_portion.ex.en = "liquid/drop"
relations.holo_portion.exe.en = """
"""
relations.holo_portion.com.en = """
"""


### Relation: eq_synonym

relations.eq_synonym.name.en = "Equal Synonym"
relations.eq_synonym.df.en = """
two words that can be interchanged in a context are said to be
synonymous relative to that context
"""
relations.eq_synonym.dfn.en = """
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
relations.eq_synonym.ex.en = ""
relations.eq_synonym.exe.en = """
* 一模一样 (70100056-a) EQUALS identical (02068946-a)  identical
* (02068946-a) EQUALS  一模一样 (70100056-a)
"""
relations.eq_synonym.com.en = """
"""


### Relation: instance_hypernym

relations.instance_hypernym.name.en = "Instance Hypernym"
relations.instance_hypernym.df.en = "the type of an instance"
relations.instance_hypernym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
relations.instance_hypernym.ex.en = "*city/Manchester*"
relations.instance_hypernym.exe.en = """"""
relations.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
relations.instance_hypernym.com.en = """
Sometimes modelled as hyponomy/hypernymy relations.
"""


### Relation: instance_hyponym

relations.instance_hyponym.name.en = "Instance Hyponym"
relations.instance_hyponym.df.en = "an occurrence of something"
relations.instance_hyponym.dfn.en = """
A relation between two concepts where concept X (``instance_hyponym``)
is a type of concept Y (``instance_hypernym``), and where X is an
individual entity.  X will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
relations.instance_hyponym.ex.en = ""
relations.instance_hypernym.exe.en = """"""
relations.instance_hypernym.test.en = """
=== ==================
Yes X is one of the Ys
No  Y is one of the Xs
=== ==================

Condition: X is a proper noun (or named entity), Y is a common noun.
"""
relations.instance_hyponym.exe.en = """
"""
relations.instance_hyponym.com.en = """
"""


### Relation: exemplifies

relations.exemplifies.name.en = "Exemplifies"
relations.exemplifies.df.en = "clarify by giving an example of"
relations.exemplifies.dfn.en = """
A relation between two concepts where Y is a type of concept
X. such as idiom, honorific or classifier.
"""
relations.exemplifies.ex.en = ""
relations.exemplifies.exe.en = """
"""
relations.exemplifies.com.en = """
The name was changed from "Domain of synset - USAGE" as we found it
too different from the standard meaning of domain.
"""


### Relation: is_exemplified_by

relations.is_exemplified_by.name.en = "Is Exemplified By"
relations.is_exemplified_by.df.en = ""
relations.is_exemplified_by.dfn.en = """
A relation between two concepts where A is an example of the type B.
"""
relations.is_exemplified_by.ex.en = ""
relations.is_exemplified_by.exe.en = """
"""
relations.is_exemplified_by.com.en = """
We agreed to change the name for these with Christiane! We
propose 'Exemplified_By'.

"""


### Relation: domain_topic

relations.domain_topic.name.en = "Domain Topic"
relations.domain_topic.df.en = ""
relations.domain_topic.dfn.en = """
A relation between two concepts where Y is a scientific
domain (e.g. computing, sport, biology, etc.) of concept X.
"""
relations.domain_topic.ex.en = ""
relations.domain_topic.exe.en = """
"""
relations.domain_topic.com.en = """
"""


### Relation: has_domain_topic

relations.has_domain_topic.name.en = "Has Domain Topic"
relations.has_domain_topic.df.en = ""
relations.has_domain_topic.dfn.en = """
A relation between two concepts where X is a scientific
domain (e.g. computing, sport, biology, etc.) of concept Y.
"""
relations.has_domain_topic.ex.en = ""
relations.has_domain_topic.exe.en = """
"""
relations.has_domain_topic.com.en = """
"""


### Relation: domain_region

relations.domain_region.name.en = "Domain Region"
relations.domain_region.df.en = ""
relations.domain_region.dfn.en = """
A relation between two concepts where Y is a geographical / cultural
domain of concept X. Domain(Region) and Domain-Term(Region) is a
paired relation between terms/concepts of any part-of-speech and a
related geographical region.
"""
relations.domain_region.ex.en = ""
relations.domain_region.exe.en = """
"""
relations.domain_region.com.en = """
We also agreed to change the name for these (to include both
geographical and cultural regions)! But I'm not sure to
what...
"""


### Relation: has_domain_region

relations.has_domain_region.name.en = "Has Domain Region"
relations.has_domain_region.df.en = ""
relations.has_domain_region.dfn.en = """
A relation between two concepts where X is a geographical /
cultural domain of concept Y.
"""
relations.has_domain_region.ex.en = ""
relations.has_domain_region.exe.en = """
"""
relations.has_domain_region.com.en = """
We have discussed changing the name for these (as they include both
geographical and cultural regions).  But we have not yet come up with
a good name.
"""


### Relation: attribute

relations.attribute.name.en = "Attribute"
relations.attribute.df.en = """
an abstraction belonging to or characteristic of an entity
"""
relations.attribute.dfn.en = """
A relation between nominal and adjectival concepts where the concept X
is an attribute of concept Y. ‘Attributes’ is a self-reciprocal link
(the two directions of this relation share the same meaning) —
Concept-X attributes to Concept-Y, and Concept-Y attributes to
Concept-X.

It denotes a relation between a noun and its adjectival attributes,
and vice-versa — for this reason it should only link adjectives to
nouns and vice-versa.
"""
relations.attribute.ex.en = ""
relations.attribute.exe.en = """
* fertile (01001689-a) ATTRIBUTES:  fertility (14051494-n)
* fertility (14051494-n) ATTRIBUTES: fertile (01001689-a)
"""
relations.attribute.com.en = """
In plWN Value_of_the_attribute is a unilateral relation from
adjectives to nouns.
"""


### Relation: restricts

relations.restricts.name.en = "Restricts"
relations.restricts.df.en = """
place limits on (extent or amount or access)
"""
relations.restricts.dfn.en = """
A relation between an adjectival concept X (quantifier/determiner) and
a nominal (pronominal) concept Y.
"""
relations.restricts.ex.en = ""
relations.restricts.exe.en = """
"""
relations.restricts.com.en = """
This would work for features like 'medial' or 'proximal' in
pronouns, or 'every' in everybody, or 'male' for male
personal pronouns, but not masculine agreeement in gendered
languages. This relation will include some things that are
now marked as domain usage. (to be corrected soon'ish)
"""


### Relation: restricted_by

relations.restricted_by.name.en = "Restricted By"
relations.restricted_by.df.en = ""
relations.restricted_by.dfn.en = """
A relation between nominal (pronominal) concept Y and an
adjectival concept X (quantifier/determiner).
"""
relations.restricted_by.ex.en = ""
relations.restricted_by.exe.en = """
* this-a (77000061-a) QUANTIFIES [qant] this-n (77000061-n)
* this-n (77000061-n) QUANTIFIER: [hasq] this-a (77000061-a)
"""
relations.restricted_by.com.en = """
"""


### Relation: classifies

relations.classifies.name.en = "Classifies"
relations.classifies.df.en = """
assign to a class or kind
"""
relations.classifies.dfn.en = """
A relation between a classifier concept X and concept Y. A relation
between a classifier X and Y
"""
relations.classifies.ex.en = ""
relations.classifies.exe.en = """
"""
relations.classifies.com.en = """
currently we only have links for nominal concepts, but we
will do it for other POS (e.g. v)
"""


### Relation: classified_by

relations.classified_by.name.en = "Classified By"
relations.classified_by.df.en = """
arrange or order by classes or categories
"""
relations.classified_by.dfn.en = """
A relation between concept Y and a classifier concept X. A relation
between Y and a classifier X
"""
relations.classified_by.ex.en = ""
relations.classified_by.exe.en = """
"""
relations.classified_by.com.en = """
"""


### Relation: also (no ili)

relations.also.name.en = "See also"
relations.also.df.en = """
a word having a loose or fuzzy semantic relation to another word
"""
relations.also.dfn.en = """
‘See Also’ is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-X relates to Concept-Y, and
Concept-Y relates to Concept-X.

It denotes a relation of related meaning with another concept (going
beyond synonymy and similarity).

This link was originally used to relate adjectives, but we have
unconstrained this use, and we're making use of this link to relate
all parts-of-speech.
"""
relations.also.ex.en = ""
relations.also.exe.en = """
"""
relations.also.com.en = """
Also known as fuzzynym
"""


### Relation: antonym

relations.antonym.name.en = "Antonym"
relations.antonym.df.en = """
a word that expresses a meaning opposed to the meaning of another
word, in which case the two words are antonyms of each other
"""
relations.antonym.dfn.en = """
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
relations.antonym.ex.en = ""
relations.antonym.exe.en = """
"""
relations.antonym.com.en = """
It is primarily a relation between senses, but sense level antonymy
implies a looser synset level relation, which we automatically add to
make it avaiable for wordnets that do not yet have sense level links.
"""


### Relation: entails

relations.entails.name.en = "Entails"
relations.entails.df.en = """
impose, involve, or imply as a necessary accompaniment or result
"""
relations.entails.dfn.en = """
Entailment is a relation that links two verbs, and it is currently
unilateral — Verb-X entails Verb-Y, without a reciprocal or tracing
link.  This relation presupposes/requires a semantic restriction in
which Verb-Y has to take place before or during Verb-X.
"""
relations.entails.ex.en = ""
relations.entails.exe.en = """
"""
relations.entails.com.en = """
"""


### Relation: is_entailed_by

relations.is_entailed_by.name.en = "Is Entailed By"
relations.is_entailed_by.df.en = ""
relations.is_entailed_by.dfn.en = """
"""
relations.is_entailed_by.ex.en = ""
relations.is_entailed_by.exe.en = """
"""
relations.is_entailed_by.com.en = """
"""


### Relation: other

relations.other.name.en = "Other"
relations.other.df.en = "any other semantic relation"
relations.other.dfn.en = """
This is used for semantic relation types not currently supported by
the OMW DTD.  The exact relation type can be given with ``dc:type``:

.. code:: xml

    <SynsetRelation relType="other" dc:type="emotion" target="example-en-1234-n"/>

"""
relations.other.ex.en = ""
relations.other.exe.en = """
"""
relations.other.com.en = """
Because we don't know what it means, we cannot give it a reverse relation.
"""

### Relation: participle

relations.participle.name.en = "Participle"
relations.participle.df.en = "links from a participial adjective to a verb"
relations.participle.dfn.en = """A relation where X is a participial adjective and Y is the verb it is derived from"""
relations.participle.ex.en = "*interesting* is the participial adjective from *interest*"
relations.participle.exe.en = ""
relations.participle.com.en = "These are not linked in the NLTK interface so are not shown in OMW 1.0 (or as far as I can see, anywhere FCB)"

### Relation: pertainym

relations.pertainym.name.en = "Pertainym"
relations.pertainym.df.en = "X is of or pertaining to Y"
relations.pertainym.dfn.en = "links a relational adjective X  to the noun Y it is about, or an adverb X to the adjective it is about Y"
relations.pertainym.ex.en = "*naval* has pertainym *navy*; *slowly* has pertainym *slow*"
relations.pertainym.exe.en = """
* `lunar <ILIURL/15548>`_ has pertainym `moon <ILIURL/85806>`_
* `naval <ILIURL/15629>`_ has pertainym `navy <ILIURL/80195>`_
* `slowly <ILIURL/19235>`_ has pertainym `slow <ILIURL/5362>`_
* `English <ILIURL/17163>`_ has pertainym `England <ILIURL/83374>`_
* `subclinical <ILIURL/16413>`_ has pertainym `clinical <ILIURL/16412>`_
* `clinical <ILIURL/16412>`_ has pertainym `clinic <ILIURL/79534>`_
"""
relations.pertainym.com.en = ""


### Relation: derivation

relations.derivation.name.en = "Derivation"
relations.derivation.df.en = "X is a derivationally related form of Y"
relations.derivation.dfn.en = """X is a derivationally related form of Y, this may be specialized
 further.  It includes zero derivations.  Gnerally it is used for different
 syntactic categories that have the same root form and are
 semantically related.  Wordnet does not say which is the baseform,
 the relationship is fully reversible.  """
relations.derivation.ex.en = "*yearly* is derivationally related to *year*"
relations.derivation.exe.en = """*yearly* is derivationally related to *year*
*want n* is derivationally related to *want v*
*wanter n* is derivationally related to *want v*
*provision n* is derivationally related to *provide v*
"""
relations.derivation.com.en = ""


### New short definitions based on http://globalwordnet.github.io/schemas/

relations.agent.df.en = "X is typically the agent of the action expressed by Y"
relations.antonym.df.en = "An opposite and inherently incompatible word"
relations.be_in_state.df.en = "X is qualified by Y"
relations.classified_by.df.en = "A relation between Y and a classifier X"
relations.classifies.df.en = "A relation between a classifier X and Y"
relations.co_agent_instrument.df.en = "Y is the instrument used by X in a certain action"
relations.co_agent_patient.df.en = "Y is the patient undergoing an action carried out by X"
relations.co_agent_result.df.en = "Y is the result of an action carried out by X"
relations.co_instrument_agent.df.en = "X is the instrument used by Y for a certain action"
relations.co_instrument_patient.df.en = "Y undergoes an action for which the instrument expressed by X is used"
relations.co_instrument_result.df.en = "Y is the result of an action carried out by the instrument expressed by X"
relations.co_patient_agent.df.en = "Y undergoes an action carried out by X"
relations.co_patient_instrument.df.en = "X undergoes an action for which the instrument expressed by X is used"
relations.co_result_agent.df.en = "X is the result of an action carried out by Y"
relations.co_result_instrument.df.en = "X is the result of an action for which the instrument expressed by Y is used"
relations.co_role.df.en = "One concept undergoes an action in which the other concept is involved (bidirectional)"
relations.direction.df.en = "X is typically the direction or location of the action or event expressed by Y"
relations.eq_synonym.df.en = "X and Y are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)"
relations.holo_location.df.en = "Y is a place located in X"
relations.holo_portion.df.en = "Y is an amount/piece/portion of X"
relations.holonym.df.en = "X makes up a part of Y"
relations.in_manner.df.en = "Y qualifies the manner in which an action or event expressed by X takes place"
relations.instrument.df.en = "X is the instrument necessary for the action or event expressed by Y"
relations.involved_agent.df.en = "Y is typically the agent of the action expressed by X"
relations.involved_direction.df.en = "Y is typically the direction or location of the action or event expressed by X"
relations.involved_instrument.df.en = "Y is typically the instrument necessary for the action or event expressed by X"
relations.involved_location.df.en = "Y is typically the location where the action or event expressed by X takes place"
relations.involved_patient.df.en = "Y is typically the patient un-dergoing an action or event expressed by X"
relations.involved_result.df.en = "Y comes into existence as a result of X"
relations.involved_source_direction.df.en = "Y is the place from where the action or event expressed by X begins/starts/happens"
relations.involved_target_direction.df.en = "Y is the place where the action or event expressed by X leads to"
relations.involved.df.en = "Y is typically involved in the action or event expressed by X"
relations.is_caused_by.df.en = "X comes about because of Y"
relations.is_entailed_by.df.en = "Opposite of entails"
relations.is_subevent_of.df.en = "X takes place during or as part of Y, and whenever X takes place, Y takes place"
relations.location.df.en = "X is the location where the action or event expressed by Y takes place"
relations.manner_of.df.en = "X qualifies the manner in which an action or event expressed by Y takes place"
relations.mero_location.df.en = "X is a place located in Y"
relations.mero_portion.df.en = "X is an amount/piece/portion of Y"
relations.meronym.df.en = "Y makes up a part of X"
relations.other.df.en = "Any relation not otherwise specified"
relations.patient.df.en = "X is the patient undergoing an action or event expressed by Y"
#rels.pertainym.df.en =  "X is of or pertaining to Y"
relations.restricted_by.df.en = "A relation between nominal (pronominal) Y and an adjectival X (quantifier/determiner)"
relations.restricts.df.en = "A relation between an adjectival X (quantifier/determiner) and a nominal (pronominal) Y"
relations.result.df.en = "X comes into existence as a result of Y"
relations.role.df.en = "X is typically involved in the action or event expressed by Y"
relations.source_direction.df.en = "X is the place from where the event expressed by Y begins"
relations.state_of.df.en = "Y is qualified by X"
relations.subevent.df.en = "Y takes place during or as part of X, and whenever Y takes place, X takes place"
relations.target_direction.df.en = "X is the place to which the action or event expressed by Y leads"
