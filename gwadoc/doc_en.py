# -*- coding: utf-8 -*-

from gwadoc import relations


###############################################################################
### Relations Definitions


### Relation: domain

relations.domain.name.en = "Domain"
relations.domain.df.en = "A concept which is a Topic, Region or Usage pointer of a given concept."
relations.domain.dfn.en = """
Domain is an underspecified relation between two concepts where Concept B is a Topic (scientific category), 
Region or Usage pointer of Concept A.
"""
relations.domain.ex.en = "`Contribute an example <https://github.com/globalwordnet/gwadoc/>`_"
relations.domain.exe.en = ""
relations.domain.test.en = ""
relations.domain.com.en = """
This is an underspecified relation that covers Domain Topic, Domain Region, and Is Exemplified By. 
As such, it is not specified as a relation directly by wordnets, but a wordnet application may 
employ it as a general relation covering all its subtypes. 

In EuroWordNet, Domain is moved to a separate ontology.(EuroWordNet General Document pp 8–10)
 """


### Relation: has_domain

relations.has_domain.name.en = "In Domain"
relations.has_domain.df.en = "A concept which is a term of a given Topic, Region or Usage concept."
relations.has_domain.dfn.en = """
In Domain is an underspecified relation between two concepts where Concept A is a Topic (scientific category, 
Region or Usage term of Concept B.
"""
relations.has_domain.ex.en = ""
relations.has_domain.exe.en = ""
relations.has_domain.test.en = ""
relations.has_domain.com.en = """
This is an underspecified relation that covers Has Domain Topic, Has Domain Region, and Exemplifies. 
As such, it is not specified as a relation directly by wordnets, but a wordnet application may 
employ it as a general relation covering all its subtypes. 

In EuroWordNet, In Domain is moved to a separate ontology.(EuroWordNet General Document pp 8–10)
 """


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
A relation between two concepts where concept A and concept B are
closely related in meaning but are not in the same synset. Similarity
is a self-reciprocal link (the two directions of this relation share
the same meaning) — Concept-A is similar to Concept-B, and Concept-B
is similar to Concept-A.

This link was originally used to relate adjectives, but we have
unconstrained this use, and we're making use of this link to relate
all parts-of-speech.

Similarity can be understood as weak synonymy, opposed to the full
synonymy that all lemmas in a concept must share.  As adjectives are
not structured hierarchically (hyponymy/hypernymy) like verbs or
nouns, the similarity link helps showing relations between them.
"""
relations.similar.ex.en = "tools near_synonym instrument"
relations.similar.exe.en = """
 * `instrument <ILIURL/i33440>`_ has near_synonym `tools <ILIURL/36325>`_
"""

relations.similar.test.en = """
Similar-relation between nouns (EWN 3)

===     =   ======================================================
yes     a   *if it is a/an A then it is also a kind of B but you usually do not call Cn Bs*
.       b   *if it is a/an B then it is also a kind of A but you usually do not call Cm As*

===     =   ======================================================

Conditions:
 - Cn are hyponyms of A, Cm are hypnyms of B.

"""

relations.similar.com.en = """
This relation coerces PWN Similar to relation for adjectives, Verb
Group relation for verbs and EWN NEAR_SYNONYM for nouns and verbs. In
plWN Similarity relation for adjectives to nouns is a unilateral sense
relation which is why it is not given in the mappings below.
"""


### Relation: role

relations.role.name.en = "Role"
relations.role.df.en = "A concept which is involved in the action or event expressed by a given concept."
relations.role.dfn.en = """
Role is an underspecified relation between two concepts where concept A is typically involved 
in the action or event expressed by concept B.
"""
relations.role.ex.en = ""
relations.role.exe.en = ""
relations.role.test.en = """
Role / Involved as general relation (EWN test 29)

===========    ================================================================
yes            (a/an) A is the one/that who/which is typically involved in Bing
Conditions     A is a noun
.              B is a verb in the infinitive form
Example:       A hammer is that which is typically involved in hammering
Effect:        {\ hammer}\ (A)     ROLE      {\ to hammer}\ (B)
.              {\ to hammer}\ (B)  INVOLVED  {\ hammer}\ (A)
===========    ================================================================

"""
relations.role.com.en = """
This is an underspecified relation that covers Agent, Patient, Result, Instrument, 
Location, Direction, Target Direction, and Source Direction. 
As such, it is not specified as a relation directly by wordnets, but a wordnet application may 
employ it as a general relation covering all its subtypes. 

In plWordNet it is a relation between lexical units.
"""


### Relation: agent

relations.agent.name.en = "Agent"
relations.agent.df.en = "A concept which is typically the one/that who/which does the action denoted by a given concept."
relations.agent.dfn.en = """
Agent is a relation between two concepts where Concept A is the semantic role of the 
animate entity that instigates or causes the happening of Concept B, typically intentionally. 
"""
relations.agent.ex.en = "`teacher <ILIURL/93557>`_ is the agent of `to teach <ILIURL/25800>`_ "
relations.agent.exe.en = """
* `teacher <ILIURL/93557>`_ is the agent of `to teach <ILIURL/25800>`_
"""
relations.agent.test.en = """
Agent Involvement (EWN test 28)

===========     =   ======================================================================
yes             a   (A/an) A is the one/that who/which does the B, typically intentionally
Conditions:     .   - A is a noun
.               .   - Y is a verb in the gerundive form
Example:        a   A teacher is the one who does the teaching intentionally
Effect:         .   {\ teacher}\ (A) AGENT {\ to teach}\ (B)
.               .   {\ to teach}\ (B) INVOLVED AGENT {\ teacher}\ (A) 
===========     =   ======================================================================

"""
relations.agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: patient

relations.patient.name.en = "Patient"
relations.patient.df.en = "A concept which is the one/that who/which undergoes a given concept."
relations.patient.dfn.en = """
Patient is a relation between two concepts where Concept A is the semantic role of an entity 
that is not the agent but is directly involved in or affected by the happening denoted by Concept B.
"""
relations.patient.ex.en = "`learner <ILIURL/90958>`_ is the patient of `to learn <ILIURL/24750>`_ "
relations.patient.exe.en = """
* `learner <ILIURL/90958>`_ is the patient of `to learn <ILIURL/24750>`_ 
"""
relations.patient.test.en = """
Patient Involvement (EWN test 29)

===========     =   ===================================================
yes             a   (A/an) A is the one/that who/which undergoes the B 
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form
Example:        a   A learner is the one who undergoes the learning
Effect:         .   {\ learner}\ (A) PATIENT {\ to learn}\ (B) 
.               .   {\ to learn}\ (B) INVOLVED PATIENT {\ learner}\ (A) 
===========     =   ===================================================

"""
relations.patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: result

relations.result.name.en = "Result"
relations.result.df.en = "A concept which comes into existence as a result of a given concept."
relations.result.dfn.en = """
Result is a relation between two concepts where Concept A exists as a result only by virtue of 
the activity denoted by Concept B.
"""
relations.result.ex.en = "`crystal <ILIURL/85286>`_ is the result of `to crystalize <ILIURL/23949>`_ "
relations.result.exe.en = """
* `crystal <ILIURL/85286>`_ is the result of `to crystalize <ILIURL/23949>`_ 
* `ice <ILIURL/115475>`_ is the result of `to freeze <ILIURL/23605>`_
"""
relations.result.test.en = """
Result Involvement (EWN test 30)

===========     =   ===================================================================================
yes             a   (A/an) A comes into existence as a result of B
yes             b   (A/an) A is the result of B
yes             c   (A/an) A is created by B 
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form and a hyponym of “make”, “produce”, “enerate”.
Example:        a   a crystal comes into existence as a result of crystalizing
.               b   a crystal is the result of crystalizing
.               c   a crystal is created by crystalizing
Effect:         .   {\ crystal}\ (A) RESULT {\ to crystalize}\ (B)
.               .   {\ to crystalize}\ (B) INVOLVED RESULT {\ crystal}\ (A) 
===========     =   ===================================================================================

"""
relations.result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: instrument

relations.instrument.name.en = "Instrument"
relations.instrument.df.en = "A concept which is the instrument necessary for the action or event expressed by a given concept."
relations.instrument.dfn.en = """
Instrument is a relation between two concepts where Concept A is the semantic role of 
the entity (usually inanimate) that the agent uses to perform an action or start a process
expressed by Concept B.
"""
relations.instrument.ex.en = "`hammer <ILIURL/54582>`_ is the instrument of `to hammer <ILIURL/28810>`_ "
relations.instrument.exe.en = """
* `hammer <ILIURL/54582>`_ is the instrument of `to hammer <ILIURL/28810>`_ 
* `sail <ILIURL/58403>`_ is the instrument of `to sail <ILIURL/31452>`_ 
* `pen <ILIURL/28810>`_ is the instrument of `to write <ILIURL/30198>`_ 
* `ink <ILIURL/115490>`_ is the instrument of `to write <ILIURL/30198>`_ 
* `paper <ILIURL/69377>`_ is the instrument of `to write <ILIURL/30198>`_ 
"""
relations.instrument.test.en = """
Instrument Involvement (EWN test 31)

============     =   =========================================================================
yes              a   (A/an) A is either i) the instrument that or ii) what is used to Y (with) 
Conditions:      .   - A is a noun
.                .   - B is a verb in the infinitive form
Example (1):     .   An hammer is the instrument that is used to hammer
Effect:          .   {\ hammer}\ (A) INSTRUMENT {\ to hammer}\ (B) 
Effect:          .   {\ to hammer}\ (B) INVOLVED INSTRUMENT {\ hammer}\ (A)
Example (2):     .   A sailing boat is what is used to sail with
Effect:          .   {\ sail}\ (A) INSTRUMENT {\ to sail}\ (B) 
Example (3):     .   Pen/Ink/Paper is what is used to write
Effect:          .   {\ pen}\ (A) INSTRUMENT {\ to write}\ (B) 
.                .   {\ ink}\ (A) INSTRUMENT {\ to write}\ (B) 
.                .   {\ paper}\ (A) INSTRUMENT {\ to write}\ (B) 
============     =   =========================================================================

"""
relations.instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: location

relations.location.name.en = "Location"
relations.location.df.en = "A concept which is the place where the event expressed by a given concept happens."
relations.location.dfn.en = """
Location is a relation between two concepts where concept A is the
location where the action or event expressed by concept B takes place.
"""
relations.location.ex.en = "`school <ILIURL/58518>`_ is the location of `to teach <ILIURL/25800>`_"
relations.location.exe.en = """
* `school <ILIURL/58518>`_ is the location of `to teach <ILIURL/25800>`_
* `water <ILIURL/85104>`_ is the location of `to swim <ILIURL/31242>`_
"""
relations.location.test.en = """
Location Involvement (EWN test 32)

===========     =   ===================================================
yes             a   (A/an) A is the place where the B happens
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form
Example:        a   A school is the place where the teaching happens 
Effect:         .   {\ school}\ (A) LOCATION {\ to teach}\ (B) 
.               .   {\ to teach}\ (B) INVOLVED LOCATION {\ school}\ (A) 
===========     =   ===================================================

"""
relations.location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: direction

relations.direction.name.en = "Direction"
relations.direction.df.en = "A concept which is the direction of the action or event expressed by a given concept."
relations.direction.dfn.en = """
Direction is a relation between two concepts where concept A is typically
the direction or location of the action or event expressed by concept B.
"""
relations.direction.ex.en = "`place <ILIURL/82372>`_ is the direction of `to pass <ILIURL/27684>`_"
relations.direction.exe.en = """
* `place <ILIURL/82372>`_ is the direction of `to pass <ILIURL/27684>`_
"""
relations.direction.test.en = """
Direction Involvement (EWN test 33)

===========     =   ===========================================================
yes             a   It is possible to B from/to/over/across/through a place (A) 
Conditions:     .   - B is a verb in the infinitive form
Example:        a   It is possible to pass though a place 
Effect:         .   {\ place}\ (A) DIRECTION {\ to pass}\ (B)
.               .   {\ to pass}\ (B) INVOLVED DIRECTION {\ place}\ (A) 
===========     =   ===========================================================

"""
relations.direction.com.en = """
"""


### Relation: target_direction

relations.target_direction.name.en = "Target Direction"
relations.target_direction.df.en = "A concept which is the place where the action or event expressed by a given concept leads to."
relations.target_direction.dfn.en = """
Target Direction is a relation between two concepts where Concept A is the place designated as the 
end (as of a race or journey) of an action or event expressed by Concept B.
"""
relations.target_direction.ex.en = "`ground <ILIURL/85674>`_ is the target direction of `to collapse <ILIURL/113799>`_, `to fall <ILIURL/31590>`_ heavily"
relations.target_direction.exe.en = """
* `ground <ILIURL/85674>`_ is the target direction of `to collapse <ILIURL/113799>`_, to `fall <ILIURL/31590>`_ heavily
* `home <ILIURL/53274>`_ is the target direction of `to go back <ILIURL/26394>`_ 
"""
relations.target_direction.test.en = """
Target-Direction Involvement (EWN test 35)

===========     =   ===============================================================================
yes             a   (a/an/the) A is the place to which Ying happens / one Bs
Conditions:     .   - A is a noun
.               .   - B is a verb
Example:        a   The ground is the place to which one collapses/falls heavily 
Effect:         .   {\ ground}\ (A)  TARGET DIRECTION {\ to collapse, to fall heavily}\ (B)
.               .   {\ to collapse, to fall heavily}\ (B) INVOLVED TARGET DIRECTION {\ ground}\ (A) 
===========     =   ===============================================================================

"""
relations.target_direction.com.en = """
"""


### Relation: source_direction

relations.source_direction.name.en = "Source Direction"
relations.source_direction.df.en = "A concept which is the place from where the event expressed by a given concept begins."
relations.source_direction.dfn.en = """
Source Direction is a relation between two concepts where concept A is the place
from where the action or event expressed by concept B begins/starts/happens.
"""
relations.source_direction.ex.en = "the `start <ILIURL/75187>`_ is the source direction of `to race <ILIURL/27023>`_ "
relations.source_direction.exe.en = """
* the `start <ILIURL/75187>`_ is the source direction of `to race <ILIURL/27023>`_ 
* `ship <ILIURL/58798>`_ is the source direction of `to debark <ILIURL/31629>`_
"""
relations.source_direction.test.en = """
Source-Direction Involvement (EWN test 34)

===========     =   ========================================================================
yes             a   (A/an/the) A is the place from where Bing begins/starts/happens / one Bs 
Conditions:     .   - A is a noun
.               .   - B is a verb
Example:        a   The start is the place from where the racing starts
Effect:         .   {\ the start}\ (A) SOURCE DIRECTION {\ to race}\ (B)
.               .   {\ to race}\ (B) INVOLVED SOURCE DIRECTION {\ the start}\ (A) 
===========     =   ========================================================================

"""
relations.source_direction.com.en = """
"""


### Relation: involved

relations.involved.name.en = "Involved"
relations.involved.df.en = "A concept which is the action or event a given concept typically involved in."
relations.involved.dfn.en = """
Involved is an underspecified relation between two concepts where concept B is the action 
or event concept A typically involved in. 
"""
relations.involved.ex.en = ""
relations.involved.exe.en = ""
relations.involved.test.en = """
Role / Involved as general relation (EWN test 29)

===========    ================================================================
yes            (a/an) A is the one/that who/which is typically involved in Bing
Conditions     A is a noun
.              B is a verb in the infinitive form
Example:       A hammer is that which is typically involved in hammering
Effect:        {\ hammer}\ (A)     ROLE      {\ to hammer}\ (B)
.              {\ to hammer}\ (B)  INVOLVED  {\ hammer}\ (A)
===========    ================================================================

"""
relations.involved.com.en = """
This is an underspecified relation that covers Involved Agent, Involved Patient, Involved Result, 
Involved Instrument, Involved Location, Involved Direction, Involved Target Direction, and 
Involved Source Direction. 
As such, it is not specified as a relation directly by wordnets, but a wordnet application may 
employ it as a general relation covering all its subtypes. 

In plWordNet it is a relation between lexical units.
"""


### Relation: involved_agent (EuroWordNet - page 29/30)

relations.involved_agent.name.en = "Involved Agent"
relations.involved_agent.df.en = "A concept which is the action done by an agent expressed by a given concept."
relations.involved_agent.dfn.en = """
Involved Agent is a relation between two concepts where concept B is typically the action 
done by the agent expressed by concept A.
"""
relations.involved_agent.ex.en = "`to teach <ILIURL/25800>`_ involved agent `teacher <ILIURL/93557>`_ "
relations.involved_agent.exe.en = """
* `to teach <ILIURL/25800>`_ involved agent `teacher <ILIURL/93557>`_ 
"""
relations.involved_agent.test.en = """
Agent Involvement (EWN test 28)

===========     =   ======================================================================
yes             a   (A/an) A is the one/that who/which does the B, typically intentionally
Conditions:     .   - A is a noun
.               .   - Y is a verb in the gerundive form
Example:        a   A teacher is the one who does the teaching intentionally
Effect:         .   {\ teacher}\ (A) AGENT {\ to teach}\ (B)
.               .   {\ to teach}\ (B) INVOLVED AGENT {\ teacher}\ (A) 
===========     =   ======================================================================

"""
relations.involved_agent.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_patient

relations.involved_patient.name.en = "Involved Patient"
relations.involved_patient.df.en = "A concept which is the action that the patient expressed by a given concept undergoing."
relations.involved_patient.dfn.en = """
Involved Patient is a relation between two concepts where Concept B is
typically an action or event that the patient expressed by Concept A undergoing.
"""
relations.involved_patient.ex.en = "`to learn <ILIURL/24750>`_ involved patient `learner <ILIURL/90958>`_ "
relations.involved_patient.exe.en = """
* `to learn <ILIURL/24750>`_ involved patient `learner <ILIURL/90958>`_ 
"""
relations.involved_patient.test.en = """
Patient Involvement (EWN test 29)

===========     =   ===================================================
yes             a   (A/an) A is the one/that who/which undergoes the B 
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form
Example:        a   A learner is the one who undergoes the learning
Effect:         .   {\ learner}\ (A) PATIENT {\ to learn}\ (B) 
.               .   {\ to learn}\ (B) INVOLVED PATIENT {\ learner}\ (A) 
===========     =   ===================================================

"""
relations.involved_patient.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_result

relations.involved_result.name.en = "Involved Result"
relations.involved_result.df.en = "A concept which is the action or event with a result of a given concept comes into existence."
relations.involved_result.dfn.en = """
Involved Result is a relation between two concepts where concept B comes
into existence as a result of concept A.
"""
relations.involved_result.ex.en = "`to crystalize <ILIURL/23949>`_ involved result of `crystal <ILIURL/85286>`_"
relations.involved_result.exe.en = """
* `to crystalize <ILIURL/23949>`_ involved result of `crystal <ILIURL/85286>`_
* `to freeze <ILIURL/23605>`_ involved result of `ice <ILIURL/115475>`_
"""
relations.involved_result.test.en = """
Result Involvement (EWN test 30)

===========     =   ===================================================================================
yes             a   (A/an) A comes into existence as a result of B
yes             b   (A/an) A is the result of B
yes             c   (A/an) A is created by B 
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form and a hyponym of “make”, “produce”, “enerate”.
Example:        a   a crystal comes into existence as a result of crystalizing
.               b   a crystal is the result of crystalizing
.               c   a crystal is created by crystalizing
Effect:         .   {\ crystal}\ (A) RESULT {\ to crystalize}\ (B)
.               .   {\ to crystalize}\ (B) INVOLVED RESULT {\ crystal}\ (A) 
===========     =   ===================================================================================

"""
relations.involved_result.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_instrument

relations.involved_instrument.name.en = "Involved Instrument"
relations.involved_instrument.df.en = "A concept which is typically the action with the instrument expressed by a given concept."
relations.involved_instrument.dfn.en = """
Involved Instrument is a relation between two concepts where concept B is
typically the action or event with the usage of instrument expressed by concept A.
"""
relations.involved_instrument.ex.en = "`to hammer <ILIURL/28810>`_ involved instrument `hammer <ILIURL/54582>`_"
relations.involved_instrument.exe.en = """
* `to hammer <ILIURL/28810>`_ involved instrument `hammer <ILIURL/54582>`_
* `to sail <ILIURL/31452>`_ involved instrument `sail <ILIURL/58403>`_
* `to write <ILIURL/30198>`_ involved instrument `pen <ILIURL/28810>`_
* `to write <ILIURL/30198>`_ involved instrument `ink <ILIURL/115490>`_ 
* `to write <ILIURL/30198>`_ involved instrument `paper <ILIURL/69377>`_
"""
relations.involved_instrument.test.en = """
Instrument Involvement (EWN test 31)

============     =   =========================================================================
yes              a   (A/an) A is either i) the instrument that or ii) what is used to Y (with) 
Conditions:      .   - A is a noun
.                .   - B is a verb in the infinitive form
Example (1):     .   An hammer is the instrument that is used to hammer
Effect:          .   {\ hammer}\ (A) INSTRUMENT {\ to hammer}\ (B) 
Effect:          .   {\ to hammer}\ (B) INVOLVED INSTRUMENT {\ hammer}\ (A)
Example (2):     .   A sailing boat is what is used to sail with
Effect:          .   {\ sail}\ (A) INSTRUMENT {\ to sail}\ (B) 
Example (3):     .   Pen/Ink/Paper is what is used to write
Effect:          .   {\ pen}\ (A) INSTRUMENT {\ to write}\ (B) 
.                .   {\ ink}\ (A) INSTRUMENT {\ to write}\ (B) 
.                .   {\ paper}\ (A) INSTRUMENT {\ to write}\ (B) 
============     =   =========================================================================

"""
relations.involved_instrument.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_location

relations.involved_location.name.en = "Involved Location"
relations.involved_location.df.en = "A concept which is the event happening in a place expressed by a given concept."
relations.involved_location.dfn.en = """
Involved Location is a relation between two concepts where concept B is
typically the action or event which takes place in the location expressed by concept A.
"""
relations.involved_location.ex.en = "`to teach <ILIURL/25800>`_ involved location `school <ILIURL/58518>`_"
relations.involved_location.exe.en = """
* `to teach <ILIURL/25800>`_ involved location `school <ILIURL/58518>`_
* `to swim <ILIURL/31242>`_ involved location `water <ILIURL/85104>`_
"""
relations.involved_location.test.en = """
Location Involvement (EWN test 32)

===========     =   ===================================================
yes             a   (A/an) A is the place where the B happens
Conditions:     .   - A is a noun
.               .   - B is a verb in the gerundive form
Example:        a   A school is the place where the teaching happens 
Effect:         .   {\ school}\ (A) LOCATION {\ to teach}\ (B) 
.               .   {\ to teach}\ (B) INVOLVED LOCATION {\ school}\ (A) 
===========     =   ===================================================

"""
relations.involved_location.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: involved_direction

relations.involved_direction.name.en = "Involved Direction"
relations.involved_direction.df.en = "A concept which is the action with the direction expressed by a given concept."
relations.involved_direction.dfn.en = """
Involved Direction is a relation between two concepts where concept B is
typically the action or event with the direction or location expressed by concept A.
"""
relations.involved_direction.ex.en = "`to pass <ILIURL/27684>`_ involved direction `place <ILIURL/82372>`_ " 
relations.involved_direction.exe.en = """
* `to pass <ILIURL/27684>`_ involved direction `place <ILIURL/82372>`_
"""
relations.involved_direction.test.en = """
Direction Involvement (EWN test 33)

===========     =   ===========================================================
yes             a   It is possible to B from/to/over/across/through a place (A) 
Conditions:     .   - B is a verb in the infinitive form
Example:        a   It is possible to pass though a place 
Effect:         .   {\ place}\ (A) DIRECTION {\ to pass}\ (B)
.               .   {\ to pass}\ (B) INVOLVED DIRECTION {\ place}\ (A) 
===========     =   ===========================================================

"""
relations.involved_direction.com.en = """
"""


### Relation: involved_target_direction

relations.involved_target_direction.name.en = "Involved Target Direction"
relations.involved_target_direction.df.en = "A concept which is the action or event leading to a place expressed by a given concept."
relations.involved_target_direction.dfn.en = """
Involved Target Direction is a relation between two concepts where concept B is the the action 
or event leading to a place expressed by concept A.
"""
relations.involved_target_direction.ex.en = "`to collapse <ILIURL/113799>`_, `to fall <ILIURL/31590>`_ heavily involved target direction `ground <ILIURL/85674>`_"
relations.involved_target_direction.exe.en = """
* `to collapse <ILIURL/113799>`_, `to fall <ILIURL/31590>`_ heavily involved target direction `ground <ILIURL/85674>`_
* `to go back <ILIURL/26394>`_ involved target direction `home <ILIURL/53274>`_
"""
relations.involved_target_direction.test.en = """
Target-Direction Involvement (EWN test 35)

===========     =   ===============================================================================
yes             a   (a/an/the) A is the place to which Ying happens / one Bs
Conditions:     .   - A is a noun
.               .   - B is a verb
Example:        a   The ground is the place to which one collapses/falls heavily 
Effect:         .   {\ ground}\ (A)  TARGET DIRECTION { \to collapse, to fall heavily}\ (B)
.               .   {\ to collapse, to fall heavily}\ (B) INVOLVED TARGET DIRECTION {\ ground}\ (A) 
===========     =   ===============================================================================

"""
relations.involved_target_direction.com.en = """
"""


### Relation: involved_source_direction

relations.involved_source_direction.name.en = "Involved Source Direction"
relations.involved_source_direction.df.en = "A concept which is the action beginning from a place of a given concept."
relations.involved_source_direction.dfn.en = """
Involved Source Direction is a relation between two concepts where concept B is the action or event 
which begins/starts/happens from a place expressed by concept A.
"""
relations.involved_source_direction.ex.en = "`to race <ILIURL/27023>`_ involved source direction the `start <ILIURL/75187>`_ "
relations.involved_source_direction.exe.en = """
* `to race <ILIURL/27023>`_ involved source direction the `start <ILIURL/75187>`_  
* `to debark <ILIURL/31629>`_ involved source direction `ship <ILIURL/58798>`_ 
"""
relations.involved_source_direction.test.en = """
Source-Direction Involvement (EWN test 34)

===========     =   ========================================================================
yes             a   (A/an/the) A is the place from where Bing begins/starts/happens / one Bs 
Conditions:     .   - A is a noun
.               .   - B is a verb
Example:        a   The start is the place from where the racing starts
Effect:         .   {\ the start}\ (A) SOURCE DIRECTION {\ to race}\ (B)
.               .   {\ to race}\ (B) INVOLVED SOURCE DIRECTION {\ the start}\ (A) 
===========     =   ========================================================================

"""
relations.involved_source_direction.com.en = """
"""


### Relation: co_role EDP31

relations.co_role.name.en = "Co Role"
relations.co_role.df.en = "A concept undergoes an action in which a given concept is involved."
relations.co_role.dfn.en = """
Co Role is an underspecified relation between two concepts where Concept A undergoes an action in
which Concept B is involved (bidirectional).
"""
relations.co_role.ex.en = ""
relations.co_role.exe.en = """
"""
relations.co_role.test.en = """
"""
relations.co_role.com.en = """
This is an underspecified relation that covers Co Agent Patient, Co Patient Agent, 
Co Agent Instrument, Co Instrument Agent, Co Agent Result, Co Result Agent, 
Co Patient Instrument, Co Instrument Patient, Co Result Instrument, and Co Instrument Result. 
As such, it is not specified as a relation directly by wordnets, but a wordnet application may 
employ it as a general relation covering all its subtypes. 
"""


### Relation: co_agent_patient EDP32

relations.co_agent_patient.name.en = "Co Agent Patient"
relations.co_agent_patient.df.en = "A concept which is the patient undergoing an action carried out by a given concept."
relations.co_agent_patient.dfn.en = """
Co Agent Patient is a relation between two concepts where Concept B is the patient
undergoing an action carried out by Concept A.
"""
relations.co_agent_patient.ex.en = "`victim <ILIURL/93927>`_ is the co agent patient of `criminal <ILIURL/89309>`_"
relations.co_agent_patient.exe.en = """
* `victim <ILIURL/93927>`_ is the co agent patient of `criminal <ILIURL/89309>`_
"""
relations.co_agent_patient.com.en = """
"""


### Relation: co_patient_agent EDP32

relations.co_patient_agent.name.en = "Co Patient Agent"
relations.co_patient_agent.df.en = "A concept which carries out an action a given concept undergoing."
relations.co_patient_agent.dfn.en = """
Co Patient Agent is a relation between two concepts where Concept A carries out an action 
Concept B undergoing.
"""
relations.co_patient_agent.ex.en = "`criminal <ILIURL/89309>`_ is the co patient agent of `victim <ILIURL/93927>`_ "
relations.co_patient_agent.exe.en = """
* `criminal <ILIURL/89309>`_ is the co patient agent of `victim <ILIURL/93927>`_ 
"""
relations.co_patient_agent.test.en = """
"""
relations.co_patient_agent.com.en = """
"""


### Relation: co_agent_instrument EDP32

relations.co_agent_instrument.name.en = "Co Agent Instrument"
relations.co_agent_instrument.df.en = "A concept which is the instrument used by a given concept in an action."
relations.co_agent_instrument.dfn.en = """
Co Agent Instrument is a relation between two concepts where Concept B is the instrument used
by Concept A in a certain action.
"""
relations.co_agent_instrument.ex.en = "`guitar <ILIURL/54496>`_ is the co agent instrument of `guitar player <ILIURL/90355>`_"
relations.co_agent_instrument.exe.en = """
* `guitar <ILIURL/54496>`_ is the co agent instrument of `guitar player <ILIURL/90355>`_
"""
relations.co_agent_instrument.test.en = """
"""
relations.co_agent_instrument.com.en = """
"""


### Relation: co_instrument_agent EDP32

relations.co_instrument_agent.name.en = "Co Instrument Agent"
relations.co_instrument_agent.df.en = "A concept which carries out an action by using a given concept as an instrument."
relations.co_instrument_agent.dfn.en = """
Co Instrument Agent is a relation between two concepts where Concept A carries out an action 
by using Concept B as an instrument.
"""
relations.co_instrument_agent.ex.en = "`guitar player <ILIURL/90355>`_ is the co instrument agent of `guitar <ILIURL/54496>`_ "
relations.co_instrument_agent.exe.en = """
* `guitar player <ILIURL/90355>`_ is the co instrument agent of `guitar <ILIURL/54496>`_  
"""
relations.co_instrument_agent.test.en = """
"""
relations.co_instrument_agent.com.en = """
"""


### Relation: co_agent_result EDP32

relations.co_agent_result.name.en = "Co Agent Result"
relations.co_agent_result.df.en = "A concept which is the result of an action taken by a given concept."
relations.co_agent_result.dfn.en = """
Co Agent Result is a relation between two concepts where Concept B is the result of an
action carried out by Concept A.
"""
relations.co_agent_result.ex.en = "`pastry <ILIURL/76902>`_ is the co agent result of `pastry cook <ILIURL/91893>`_"
relations.co_agent_result.exe.en = """
* `pastry <ILIURL/76902>`_ is the co agent result of `pastry cook <ILIURL/91893>`_
"""
relations.co_agent_result.com.en = """
"""


### Relation: co_result_agent EDP32

relations.co_result_agent.name.en = "Co Result Agent"
relations.co_result_agent.df.en = "A concept which takes an action resulting in a given concept."
relations.co_result_agent.dfn.en = """
Co Result Agent is a relation between two concepts where Concept A takes an action resulting 
in Concept B.
"""
relations.co_result_agent.ex.en = "`pastry cook <ILIURL/91893>`_ is the co result agent of `pastry <ILIURL/76902>`_"
relations.co_result_agent.exe.en = """
* `pastry cook <ILIURL/91893>`_ is the co result agent of `pastry <ILIURL/76902>`_  
"""
relations.co_result_agent.test.en = """
"""
relations.co_result_agent.com.en = """
"""


### Relation: co_patient_instrument EDP32

relations.co_patient_instrument.name.en = "Co Patient Instrument"
relations.co_patient_instrument.df.en = "A concept which is used as an instrument in an action a given concept undergoes."
relations.co_patient_instrument.dfn.en = """
Co Patient Instrument is a relation between two concepts where Concept B is the instrument 
used in an action which Concept A undergoes.
"""
relations.co_patient_instrument.ex.en = "`bread knife <ILIURL/51098>`_ is the co patient instrument of `bread <ILIURL/77313>`_ "
relations.co_patient_instrument.exe.en = """
* `bread knife <ILIURL/51098>`_ is the co patient instrument of `bread <ILIURL/77313>`_ 
"""
relations.co_patient_instrument.test.en = """
"""
relations.co_patient_instrument.com.en = """
"""


### Relation: co_instrument_patient EDP32

relations.co_instrument_patient.name.en = "Co Instrument Patient"
relations.co_instrument_patient.df.en = "A concept which undergoes an action with the use of a given concept as an instrument."
relations.co_instrument_patient.dfn.en = """
Co Instrument Patient is a relation between two concepts where Concept A undergoes an action
for which the instrument expressed by Concept B is used.
"""
relations.co_instrument_patient.ex.en = "`bread <ILIURL/77313>`_ is the co instrument patient of `bread knife <ILIURL/51098>`_"
relations.co_instrument_patient.exe.en = """
* `bread <ILIURL/77313>`_ is the co instrument patient of `bread knife <ILIURL/51098>`_
"""
relations.co_instrument_patient.test.en = """
"""
relations.co_instrument_patient.com.en = """
"""


### Relation: co_result_instrument EDP32

relations.co_result_instrument.name.en = "Co Result Instrument"
relations.co_result_instrument.df.en = "A concept which is used as an instrument in an action resulting in a given concept."
relations.co_result_instrument.dfn.en = """
Co Result Instrument is a relation between two concepts where Concept B is an instrument used 
in an action resulting in Concept A.
"""
relations.co_result_instrument.ex.en = "`photograpic camera <ILIURL/51401>`_ is the co result instrument of `photo <ILIURL/57211>`_"
relations.co_result_instrument.exe.en = """
* `photograpic camera <ILIURL/51401>`_ is the co result instrument of `photo <ILIURL/57211>`_
"""
relations.co_result_instrument.test.en = """
"""
relations.co_result_instrument.com.en = """
"""


### Relation: co_instrument_result ice saw/ice

relations.co_instrument_result.name.en = "Co Instrument Result"
relations.co_instrument_result.df.en = "A concept which is the result of an action using an instrument of a given concept."
relations.co_instrument_result.dfn.en = """
Co Instrument Result is a relation between two concepts where Concept A is the result of an
action carried out by the instrument expressed by Concept B.
"""
relations.co_instrument_result.ex.en = "`photo <ILIURL/57211>`_ is the co instrument result of `photograpic camera <ILIURL/51401>`_"
relations.co_instrument_result.exe.en = """
* `photo <ILIURL/57211>`_ is the co instrument result of `photograpic camera <ILIURL/51401>`_
"""
relations.co_instrument_result.test.en = """
"""
relations.co_instrument_result.com.en = """
"""


### Relation: state_of EDP37

relations.state_of.name.en = "State Of"
relations.state_of.df.en = """
the way something is with respect to its main attributes
"""
relations.state_of.dfn.en = """
A relation between two concepts where concept B is qualified by
concept A.
"""
relations.state_of.ex.en = "poor state_of poor (a poor person)"
relations.state_of.exe.en = """
 * `poor <ILIURL/11083>`_ state_of `have-not <ILIURL/92132>`_
 * `rich <ILIURL/11080>`_ state_of `rich person <ILIURL/92571>`_

"""
relations.state_of.test.en = """
State Of - relation between noun (EWN 44)

===     =   ======================================================
yes     a   *B is the state that applies to A*

===     =   ======================================================

Conditions:
 - B is an adjective/adverb.
 - A is a noun.

"""
relations.state_of.com.en = """
In plWordNet it is a relation between lexical units.
FCB: isn't this the same as attribute (but split into two directions)
"""


### Relation: be_in_state EDP37

relations.be_in_state.name.en = "Be In State"
relations.be_in_state.df.en = "Concept A is qualified by B"
relations.be_in_state.dfn.en = """
A relation between two concepts where concept A is qualified by
concept B.

A is qualified by B.
"""
relations.be_in_state.ex.en = "poor (a poor person) be_in_State poor"
relations.be_in_state.exe.en = """
 * `have-not <ILIURL/92132>`_ be in state `poor <ILIURL/11083>`_
 * `rich person <ILIURL/92571>`_ be in state `rich <ILIURL/11080>`_
"""
relations.be_in_state.test.en = """
Be In State - relation between adjective/adverb (EWN 44)

===     =   ======================================================
yes     a   *a/an/the A is the one/that to whom/which the state B applies*

===     =   ======================================================

Conditions:
 - A is a noun.
 - B is an adjective/adverb.

"""

relations.be_in_state.com.en = """
In plWordNet it is a relation between lexical units.
"""


### Relation: causes EDP34

relations.causes.name.en = "Causes"
relations.causes.df.en = """
Concept A is an entity that produces an effect or is responsible for events or
results of Concept B.
"""
relations.causes.dfn.en = """
A relation between two concepts where concept B comes into existence
as a result of concept A. Entailment is a relation that links two
verbs, and it is currently unilateral — Verb-A causes Verb-B, without
a reciprocal or tracing link. Causation presupposes/requires that some
Verb-B will, inevitably, take place during or after Verb-A (e.g. if
Verb-A occurs, then Verb-B will also occur).

While not exclusive to these types of verbs, many verbs that have both
a transitive and an intransitive form will frequently be submitted to
this relation.
"""
relations.causes.ex.en = "kill causes die"
relations.causes.exe.en = """
 * `kill <ILIURL/28306>`_ causes `die <ILIURL/23529>`_
"""
relations.causes.test.en = """
Causes - relation  (EWN 36)

===     =   ======================================================
yes     a   *(To/A/an) A causes (to/a/an) B to take place*
.       .   *(To/A/an) A has (to/a/an) B as a consequence*
.       .   *(To/A/an) A leads to (to/a/an) B*
no      b   *the converse of (a)*

===     =   ======================================================

Conditions:
 - A is a verb in the infinitive form or A is a noun in the singular 
 - B is a verb in the infinitive form or B is a noun in the singular
 
Causes - relation between verbs and adjectives (or adverbs)  (EWN 37)

===     =   ======================================================
yes     a   *A causes to be B*
.       .   *A has being B as a consequence*
.       .   *A leads to be(ing) B*
no      b   *the converse of (a)*

===     =   ======================================================

Conditions:
- A is a verb in the infinitive form
- B is and adjective

"""
relations.causes.com.en = """
EUWN's definition of CAUSES is broader than that of PWN. It
seems possible to just absorb PWN's links.
"""


### Relation: is_caused_by EDP34

relations.is_caused_by.name.en = "Is Caused By"
relations.is_caused_by.df.en = "Concept A comes about because of concept B"
relations.is_caused_by.dfn.en = """
A relation between two concepts where concept A comes into existence
as a result of concept B.
"""
relations.is_caused_by.ex.en = "die is_caused_by kill"
relations.is_caused_by.exe.en = """
 * `die <ILIURL/23529>`_ is caused by `kill <ILIURL/28306>`_

"""
relations.is_caused_by.test.en = """
Is Caused By - relation  (EWN 36)

===     =   ======================================================
yes     a   *(To/A/an) B takes place because of A*
.       .   *(To/A/an) B is the consequence A*
.       .   *(To/A/an) B is the result of A*
no      b   *the converse of (a)*

===     =   ======================================================

Conditions:
 - A is a verb in the infinitive form or A is a noun in the singular 
 - B is a verb in the infinitive form or B is a noun in the singular

Is Caused By - relation between verbs and adjectives (or adverbs)  (EWN 37)

===     =   ======================================================
yes     a   *B is caused by A*
.       .   *B is the consequence of A*
.       .   *B is the result of A*
no      b   *the converse of (a)*

===     =   ======================================================

Conditions:

- A is a verb in the infinitive form
- B is and adjective

"""
relations.is_caused_by.com.en = """
The 'is caused by' relation was missing from PWN before."""


### Relation: subevent EDP35

relations.subevent.name.en = "Subevent"
relations.subevent.df.en = "Concept B takes place during or as part of concept A, and whenever concept B takes place, concept A takes place"
relations.subevent.dfn.en = """
A relation between two concepts where concept B takes place
during or as part of concept A, and whenever concept B takes
place, concept A takes place.

"""
relations.subevent.ex.en = "sleep has subevent snore"
relations.subevent.exe.en = """
 * `sleep <ILIURL/21840>`_ has subevent `snore <ILIURL/21852>`_

"""
relations.subevent.test.en = """
Subevent - relation between verbs/nouns (a)  (EWN 41)

===     =   ======================================================
yes     a   *B takes place during or as a part of A, and whenever B takes place, A takes place*

no      b   *the converse of (a)*

===     =   ======================================================

Conditions:

- A is a verb in the gerundive form
- B is a verb in the gerundive form

Subevent - relation between verbs/nouns (b)  (EWN 42)

===     =   ======================================================
yes     a   *A consists of B and other events or processes*

no      b   *the converse of (a)*

===     =   ======================================================

Conditions:

- B is a verb in the gerundive form
- A is a verb in the gerundive form buying consists of paying and other events or processes

"""
relations.subevent.com.en = """
The SUBEVENT relation is very useful for many closely related verbs and appeals more directly to human-intuitions
(parallel to part-whole relation of concrete entities).

"""


### Relation: is_subevent_of EDP35

relations.is_subevent_of.name.en = "Is Subevent Of"
relations.is_subevent_of.df.en = "Concept A takes place during or as part of concept B, and whenever concept A takes place, concept B takes place"
relations.is_subevent_of.dfn.en = """
A relation between two concepts where concept A takes place
during or as part of concept B, and whenever concept A takes
place, concept B takes place.

"""
relations.is_subevent_of.ex.en = "snore is_subevent_of sleep"
relations.is_subevent_of.exe.en = """
 * `snore <ILIURL/21852>`_ is subevent of `sleep <ILIURL/21840>`_
 * `pay <ILIURL/i32996>`_ is subevent of `buy <ILIURL/33154>`_
 
"""
relations.is_subevent_of.test.en = """
Is Subevent Of - relation between verbs/nouns (a)  (EWN 41)

===     =   ======================================================
yes     a   *A takes place during or as a part of B, and whenever A takes place, B takes place*

no      b   *the converse of (a)*

===     =   ======================================================

Conditions:

- A is a verb in the gerundive form
- B is a verb in the gerundive form

Is Subevent Of - relation between verbs/nouns (b)  (EWN 42)

===     =   ======================================================
yes     a   *A consists of B and other events or processes*

no      b   *the converse of (a)*

===     =   ======================================================

Conditions:

- B is a verb in the gerundive form
- A is a verb in the gerundive form buying consists of paying and other events or processes

"""
relations.is_subevent_of.com.en = """
"""


### Relation: in_manner EDP36

relations.in_manner.name.en = "In Manner"
relations.in_manner.df.en = "B qualifies the manner in which an action or event expressed by A takes place"
relations.in_manner.dfn.en = """
A relation between two concepts where concept B qualifies
the manner in which an action or event expressed by concept
A takes place.

"""
relations.in_manner.ex.en = "slurp in manner noisely"
relations.in_manner.exe.en = """
 * `slurp <ILIURL/27462>`_ in manner `noisily <ILIURL/19718>`_
"""
relations.in_manner.test.en = """
In Manner - relation between verbs/adverb (EWN 43)

===     =   ======================================================
yes     a   *to A is to B in a C manner/way.*

===     =   ======================================================

Conditions:

- A and B are verbs
- B is the hyperonym of A
- C is an adjective/adverb

"""
relations.in_manner.com.en = """
In EuroWordNet, we decided not to differentiate between troponymy and hyponymy but to use the IN_MANNER and MANNER_OF
relation in addition to normal hyponymy to make the manner component explicit (if it is significant in the meaning of the verb):
"""


### Relation: manner_of EDP36

relations.manner_of.name.en = "Manner Of"
relations.manner_of.df.en = "a way of acting or behaving"
relations.manner_of.dfn.en = """
A relation between two concepts where concept A qualifies
the manner in which an action or event expressed by concept
B takes place.

"""
relations.manner_of.ex.en = "noisely manner of slurp"
relations.manner_of.exe.en = """
 * `noisily <ILIURL/19718>`_  manner of `slurp <ILIURL/27462>`_
"""
relations.manner_of.test.en = """
Manner Of - relation between verbs/adverb (EWN 43)

===     =   ======================================================
yes     a   *a manner of B which qualifies A*

===     =   ======================================================

Conditions:

- A and B are verbs
- B is the hyperonym of A
- C is an adjective/adverb

"""
relations.manner_of.com.en = """
"""


### Relation: meronym EDP26

relations.meronym.name.en = "Meronym"
relations.meronym.df.en = """
a word that names a part of a larger whole
"""
relations.meronym.dfn.en = """
A relation between two concepts where concept A makes up a part of
concept B.
"""
relations.meronym.ex.en = "hand has part-meronym finger"
relations.meronym.exe.en = """
 * `hat <ILIURL/54674>`_ has part-meronym `crown <ILIURL/52548>`_
 * `people <ILIURL/79059>`_ has member-meronym `person <ILIURL/35562>`_
 * `water <ILIURL/115069>`_ has substance-meronym `hydrogen <ILIURL/113946>`_
"""
relations.meronym.test.en="""
Meronymy-relation between nouns (EWN test 21)

===     =   ======================================================
yes     a   *A/an A makes up a part of A/an B*
.       .   *A/an Y has A/an Xs*
.       .   *A is a meronym of "B" if As are parts of B(s)*

no      b   the converse of the (a) relations.
===     =   ======================================================

Conditions:
- A and B are concrete nouns and are interpreted generically.
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
A relation between two concepts where concept A makes up a
part of concept B.
"""
relations.holonym.ex.en = "finger has part-holonym hand"
relations.holonym.exe.en = """
 * `eye <ILIURL/64868>`_ has part-holonym `face <ILIURL/87210>`_
 * `planet <ILIURL/85986>`_ has member-holonym `solar system <ILIURL/86215>`_
 * `kibibyte <ILIURL/108305>`_ has part-holonym `mebibyte <ILIURL/108309>`_
"""
relations.holonym.test.en = """
Holonymy-relation between nouns

===     =   ======================================================
yes     a   *A is a holonym of B if Bs are parts of As*
.       .   *A is a holonym of B if Bs are members of As*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================
"""
relations.holonym.com.en = """
This is an unspecified relation that covers all the
relations below. This can be computed automatically, it
shouldn't be a special relation.
"""


### Relation: mero_part EDP27

relations.mero_part.name.en = "Part Meronym"
relations.mero_part.df.en = "concept A is a component of concept B"
relations.mero_part.dfn.en = """
A relation between two concepts where concept A is a component of
concept B. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-A can be
separated into Concept-B”; and Concept-B is a part of some Concept-A.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
relations.mero_part.ex.en = "car mero-part wheel"
relations.mero_part.exe.en = """
 * `glove <ILIURL/54319>`_ has part-meronym `finger <ILIURL/53712>`_
"""

relations.mero_part.test.en = """
Meronymy-relation between nouns (EWN test 24)

===     =   ======================================================
yes     a   *a/an A is a component of a/an B*
.       b   *a/an B is a whole/system/complex/network/arrangement/construction of parts/components among which a/an A*

===     =   ======================================================

Condition: 

- A and B are concrete nouns denoting objects, there must be several As

"""
relations.mero_part.com.en = """
This relation is also frequently used by PWN to denote
geographical inclusiveness relations.

"""


### Relation: holo_part EDP27

relations.holo_part.name.en = "Part Holonym"
relations.holo_part.df.en = "Concept B is the whole where Concept A is a part"
relations.holo_part.dfn.en = """
A relation between two concepts where concept B is the whole of the different component of
concept A. Meronym and Holonym Part is a paired relation that denotes
proper parts (separable, in principle), which preserve a belonging
relation even if the physical link is broken — Concept-A can be
separated into Concept-B”; and Concept-B is a part of some Concept-A.

This relation is also frequently used to denote geographical
inclusiveness relations.
"""
relations.holo_part.ex.en = "wheel holo-part car"
relations.holo_part.exe.en = """
 * `thumb <ILIURL/60231>`_ has part-holonym `glove <ILIURL/54319>`_
"""
relations.holo_part.test.en = """
Holonymy-relation between nouns (EWN test 24)

===     =   ======================================================
yes     a   *a/an B is a whole/system/complex/network/arrangement/construction of parts/components among which a/an A*
.       b   *a/an A is a component of a/an B*

===     =   ======================================================

Condition:

- B and A are concrete nouns denoting objects, B typically includes a larger entity

"""
relations.holo_part.com.en = """
The has_holo-part relation typically relates components to their wholes, namely: something which is either topologically or temporally included in a larger entity and which as well bears some kind of autonomy (non-arbitrary boundaries) and a definite function with respect to the whole.
"""


### Relation: mero_member EPD27

relations.mero_member.name.en = "Member Meronym"
relations.mero_member.df.en = "Concept A is a member of Concept B"
relations.mero_member.dfn.en = """
A relation between two concepts where concept A is a member/ element
of concept B. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a sub-kind of a concept. It links groups to members
— Many instances of Concept-A form Concept-B; and Concept-B is composed of many members of Concept-A. 
"""
relations.mero_member.ex.en = "player has mero-member team"
relations.mero_member.exe.en = """
 * `fleet <ILIURL/80725>`_ has member-meronym `ship <ILIURL/58798>`_
"""
relations.mero_member.test.en = """
Member meronymy -relation between nouns (EWN test 22)

===     =   ======================================================
yes     a   *a/an A is a member/element of (a/an/the) B*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- A is a single object-denoting noun
- B is a multiform noun (either a group-noun, a collective-noun or as a lexicalized plural denoting multiple objects)
- preferably humans, animals, plants or vehicles or closed sets such as the number system, or the alphabet.

"""
relations.mero_member.com.en = """
"""


### Relation: holo_member EDP27

relations.holo_member.name.en = "Member Holonym"
relations.holo_member.df.en = "Concept B is a member of Concept A"
relations.holo_member.dfn.en = """
A relation between two concepts where concept B is a member/ element
of concept A. Meronym and Holonym Membership is a paired relation that
denotes group formation and membership. Is different from hyponym as
it does not relates a sub-kind of a concept. It links groups to members
— Concept-B is composed of many members of Concept-A; and many
instances of Concept-A form Concept-B.
"""
relations.holo_member.ex.en = "team has holo-member player"
relations.holo_member.exe.en = """
 * `ship <ILIURL/58798>`_ has member-holonym `fleet <ILIURL/80725>`_
"""
relations.holo_member.test.en = """
Member holonymy -relation between nouns (EWN test 22)

===     =   ======================================================
yes     a   *a/an B is a member/element of (a/an/the) A*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- B is a multiform noun (either a group-noun, a collective-noun or as a lexicalized plural denoting multiple objects)
- A is a single object-denoting noun
- preferably humans, animals, plants or vehicles or closed sets such as the number system, or the alphabet.

"""
relations.holo_member.com.en = """
"""


### Relation: mero_substance EDP28

relations.mero_substance.name.en = "Substance Meronym"
relations.mero_substance.df.en = "Concept A is made of concept B."
relations.mero_substance.dfn.en = """
A relation between two concepts where concept A is made of concept
B. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-A is made of Concept-B; and
Concept-B is a substance of Concept-A”.
"""
relations.mero_substance.ex.en = "stick has mero-substance wood"
relations.mero_substance.exe.en = """
 * `paper <ILIURL/115832>`_ has substance-meronym `cellulose <ILIURL/114776>`_
 * `wood <ILIURL/116549>`_ has substance-meronym `lignin <ILIURL/115606>`_
"""
relations.mero_substance.test.en = """
Substance meronymy -relation between nouns (EWN test 25)

===     =   ======================================================
yes     a   *a/an A is made of B*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- A is a concrete object
- B is a concrete substance

"""
relations.mero_substance.com.en = """
There are two basic ways of viewing entities in the world, 
namely either as an individuated thing or as the stuff from 
which they are made of. This way, for instance a book can
be alternatively named “a book” or “paper”.
The relation between things and the stuff which compose them is called MADE_OF.
"""


### Relation: holo_substance EDP28

relations.holo_substance.name.en = "Substance Holonym"
relations.holo_substance.df.en = "Concept-B is a substance of Concept-A"
relations.holo_substance.dfn.en = """
A relation between two concepts where concept B is made of concept
A. Meronym and Holonym Substance is a paired relation that denotes a
higher bound between part and whole. Separating/removing the substance
part, will change the whole — Concept-A is made of Concept-Y; and
Concept-B is a substance of Concept-A”.
"""
relations.holo_substance.ex.en = "wood/stick"
relations.holo_substance.exe.en = """
 * `wood <ILIURL/116549>`_ has substance-holonym `beam <ILIURL/50617>`_
"""
relations.holo_substance.test.en = """
Substance holonymy -relation between nouns (EWN test 25)

===     =   ======================================================
yes     a   *a/an B is substance of A*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- B is a concrete substance
- A is a concrete object

"""
relations.holo_substance.com.en = """
Complex holonyms can also contain substances but in that case the MADE_OF relation is used.
"""


### Relation: mero_location EDP28

relations.mero_location.name.en = "Location Meronym"
relations.mero_location.df.en = "A is a place located in B"
relations.mero_location.dfn.en = """
A relation between two concepts where concept A is a place
located in concept B.
"""
relations.mero_location.ex.en = "city has mero-location centre"
relations.mero_location.exe.en = """
 * `desert <ILIURL/81751>`_ has part-meronym `oasis <ILIURL/81753>`_
"""
relations.mero_location.test.en = """
Location meronymy -relation between nouns (EWN test 26)

===     =   ======================================================
yes     a   *a/an/the A is a place located in a/an/the B*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- A is a concrete noun
- B is a concrete noun

"""
relations.mero_location.com.en = """
"""


### Relation: holo_location EDP28

relations.holo_location.name.en = "Location Holonym"
relations.holo_location.df.en = "B is a place located in A"
relations.holo_location.dfn.en = """
A relation between two concepts where concept B is a place
located in concept A.
"""
relations.holo_location.ex.en = "centre has holo-location city"
relations.holo_location.exe.en = """
 * `space <ILIURL/81724>`_ has part-holonym `aerospace <ILIURL/81733>`_
"""
relations.holo_location.test.en = """
Location meronymy -relation between nouns (EWN test 26)

===     =   ======================================================
yes     a   *a/an/the B is a place located in a/an/the A*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- B is a concrete noun
- A is a concrete noun

"""
relations.holo_location.com.en = """
"""


### Relation: mero_portion EDP27

relations.mero_portion.name.en = "Portion Meronym"
relations.mero_portion.df.en = "Concept A is an amount of Concept B"
relations.mero_portion.dfn.en = """
A relation between two concepts where concept A is an
amount/piece/portion of concept B.
"""
relations.mero_portion.ex.en = "drop has mero-portion liquid"
relations.mero_portion.exe.en = """
 * `Nigeria <ILIURL/83853>`_ has part-meronym `Abuja <ILIURL/83854>`_
"""
relations.mero_portion.test.en = """
Portion meronymy -relation between nouns (EWN test 26)

===     =   ======================================================
yes     a   *(a/an) A is an (amount/piece/portion) of B*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- A and B are substance denoting nouns

"""
relations.mero_portion.com.en = """
usually portions (as concepts) do not receive a separate lexical item but are realized by sense
extension (for instance, there is no lexical item equivalent to “portion of cake”);
"""


### Relation: holo_portion EDP27

relations.holo_portion.name.en = "Portion Holonym"
relations.holo_portion.df.en = "Concept B is the whole amount/piece of A"
relations.holo_portion.dfn.en = """
A relation between two concepts where concept B is an
amount/piece/portion of concept A
"""
relations.holo_portion.ex.en = "liquid  has holo-portion drop"
relations.holo_portion.exe.en = """
 * `Africa <ILIURL/84937>`_ has part-holonym `Eastern Hemisphere <ILIURL/81982>`_

"""
relations.holo_portion.test.en = """
Portion holonymy -relation between nouns (EWN test 26)

===     =   ======================================================
yes     a   *(a/an) B is the whole amount/piece of A*

no      b   the converse of (a).
===     =   ======================================================

Conditions:

- B and A are substance denoting nouns

"""
relations.holo_portion.com.en = """
The whole always pre-exist the portion.Sometimes portions are sufficiently 
common in a particular language to become lexicalized.
These lexical items will be linked to their wholes by means of a has_holo_portion
"""


### Relation: eq_synonym

relations.eq_synonym.name.en = "Equal Synonym"
relations.eq_synonym.df.en = """
two words that can be interchanged in a context are said to be
synonymous relative to that context
"""
relations.eq_synonym.dfn.en = """
A relation between two concepts where A and B are equivalent concepts
but their nature requires that they remain separate.

Equality is a self-reciprocal link (the two directions of this
relation share the same meaning) — Concept-A is equal to Concept-B,
and Concept-B is equal to Concept-A.

It denotes a special kind full synonimity that allows separation of
synonym lemmas in two different synsets. It can occur with any type of
part-of-speech.

At the moment, we're currently making use of this in order to isolate
chengyu (成语), a traditional four-character Chinese idiom.
"""
relations.eq_synonym.ex.en = "people has equal synonyms folks"
relations.eq_synonym.exe.en = """
* 一模一样 (70100056-a) EQUALS identical (02068946-a)  identical
* (02068946-a) EQUALS  一模一样 (70100056-a)
* `people <ILIURL/79059>`_ has equal-synonym `folks <ILIURL/79084>`_
* `cop <ILIURL/88724>`_ has equal-synonym `policeman <ILIURL/92109>`_
* `fiddle <ILIURL/30406>`_ has equal-synonym `violin <ILIURL/60869>`_
* `begin <ILIURL/23466>`_ has equal-synonym `start <ILIURL/23481>`_

"""
relations.eq_synonym.test.en = """
Equal Synonym-relation between nouns (EWN 1)

===     =   ======================================================
yes     a   *if it is (a/an) A then it is also (a/an) B*
.       b   *if it is (a/an) B then it is also (a/an) A*

===     =   ======================================================

Conditions:
 - A and B are singular or plural nouns
 
Equal Synonym-relation between verbs (EWN 2)

===     =   ======================================================
yes     a   *If something/someone/it As then something/someone/it Bs*
.       b   *If something/someone/it Bs then something/someone/it As*

===     =   ======================================================

Conditions:
 - A is a verb in the third person singular form
 - B is a verb in the third person singular form
 - there are no specifying PPs that apply to the A-phrase or the B-phrase

"""
relations.eq_synonym.com.en = """
In principle all semantically equivalent words should belong to the same synsets 
(where they can be differentiated by labels on the appropriate usage). 
"""


### Relation: instance_hypernym

relations.instance_hypernym.name.en = "Instance Hypernym"
relations.instance_hypernym.df.en = "the type of an instance"
relations.instance_hypernym.dfn.en = """
A relation between two concepts where concept A (``instance_hyponym``)
is a type of concept B (``instance_hypernym``), and where A is an
individual entity.  A will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hypernym`` can also be referred to as a ``type``
"""
relations.instance_hypernym.ex.en = "*manchester belongs_to_class city*"
relations.instance_hypernym.exe.en = """
 * `manchester <ILIURL/83395>`_ has instance_hypernym `city <ILIURL/81847>`_
"""
relations.instance_hypernym.test.en = """
=== ==================
Yes A is one of the Bs
No  B is one of the As
=== ==================

Condition: A is a proper noun (or named entity), B is a common noun.
"""
relations.instance_hypernym.com.en = """
Sometimes modelled as hyponomy/hypernymy relations.
"""


### Relation: instance_hyponym

relations.instance_hyponym.name.en = "Instance Hyponym"
relations.instance_hyponym.df.en = "an occurrence of something"
relations.instance_hyponym.dfn.en = """
A relation between two concepts where concept A (``instance_hyponym``)
is a type of concept B (``instance_hypernym``), and where A is an
individual entity.  A will be a terminal node in the hierarchy.
Instances are expressed by proper nouns.

An ``instance hyponym`` can also be referred to as a ``type``
"""
relations.instance_hyponym.ex.en = "city HAS_INSTANCE Manchester"
relations.instance_hyponym.exe.en = """
 * `city <ILIURL/81847>`_ has instance_hyponym `manchester <ILIURL/83395>`_
"""
relations.instance_hyponym.test.en = """
=== ==================
Yes A is one of the Bs
No  B is one of the As
=== ==================

Condition: A is a proper noun (or named entity), B is a common noun.
"""
relations.instance_hyponym.com.en = """
Hyponymy is a relation between classes of entities. Individual entities can also be said to belong to some class. 
Although we do not find many instances in a lexical database, the relation is useful for users 
that want to add particular instances and do not want to consult a separate database. 
To distinguish it from class hyponymy the relation is dubbed has_instance.
"""


### Relation: exemplifies

relations.exemplifies.name.en = "Exemplifies"
relations.exemplifies.df.en = "A concept which is the example of a given concept."
relations.exemplifies.dfn.en = """
Exemplifies is a relation between two concepts where Concept A is the example of Concept B.
"""
relations.exemplifies.ex.en = "`Band Aid <ILIURL/50429>`_ exemplifies `trademark <ILIURL/72497>`_ "
relations.exemplifies.exe.en = """
* `wings <ILIURL/36358>`_ exemplifies `plural form <ILIURL/69585>`_ 
* `Band Aid <ILIURL/50429>`_ exemplifies `trademark <ILIURL/72497>`_ 
"""
relations.exemplifies.com.en = """
The name was changed from "Member of this domain - USAGE" as we found it
too different from the standard meaning of domain.
"""


### Relation: is_exemplified_by

relations.is_exemplified_by.name.en = "Is Exemplified By"
relations.is_exemplified_by.df.en = "A concept which is the type of a given concept."
relations.is_exemplified_by.dfn.en = """
Is Exemplified By is a relation between two concepts where Concept B is a type of 
Concept A, such as idiom, honorific or classifier.
"""
relations.is_exemplified_by.ex.en = "`trademark <ILIURL/72497>`_ is exemplified by `Band Aid <ILIURL/50429>`_ "
relations.is_exemplified_by.exe.en = """
* `trademark <ILIURL/72497>`_ is exemplified by `Band Aid <ILIURL/50429>`_ 
* `plural form <ILIURL/69585>`_ is exemplified by `wings <ILIURL/36358>`_ 
"""
relations.is_exemplified_by.com.en = """
We agreed to change the name for these with Christiane! We
propose 'Exemplified_By'.
"""


### Relation: domain_topic

relations.domain_topic.name.en = "Domain Topic"
relations.domain_topic.df.en = "A concept which is the scientific category pointer of a given concept."
relations.domain_topic.dfn.en = """
Domain Topic is a relation between two concepts where Concept B is a scientific
category (e.g. computing, sport, biology, etc.) of concept A.
"""
relations.domain_topic.ex.en = "`computer science <ILIURL/68812>`_ is a domain topic of `CPU <ILIURL/51710>`_ "
relations.domain_topic.exe.en = """
* `football <ILIURL/37873>`_ is a domain topic of `place-kick <ILIURL/27159>`_ 
* `plant <ILIURL/35564>`_ is a domain topic of `evergreen <ILIURL/5001>`_ 
* `ocean <ILIURL/85897>`_ is a domain topic of `water <ILIURL/85104>`_ 
"""
relations.domain_topic.com.en = """
"""


### Relation: has_domain_topic

relations.has_domain_topic.name.en = "Has Domain Topic"
relations.has_domain_topic.df.en = "A concept which is a term in the scientific category of a given concept."
relations.has_domain_topic.dfn.en = """
Has Domain Topic is a relation between two concepts where Concept A is a scientific
category (e.g. computing, sport, biology, etc.) of concept B.
"""
relations.has_domain_topic.ex.en = "`CPU <ILIURL/51710>`_ has domain topic of `computer science <ILIURL/68812>`_ "
relations.has_domain_topic.exe.en = """
* `place-kick <ILIURL/27159>`_ has domain topic of `football <ILIURL/37873>`_ 
* `evergreen <ILIURL/5001>`_ has domain topic of `plant <ILIURL/35564>`_ 
* `water <ILIURL/85104>`_ has domain topic of `ocean <ILIURL/85897>`_ 
"""
relations.has_domain_topic.com.en = """
"""


### Relation: domain_region

relations.domain_region.name.en = "Domain Region"
relations.domain_region.df.en = "A concept which is a geographical / cultural domain pointer of a given concept."
relations.domain_region.dfn.en = """
Domain Region is a relation between two concepts where Concept B is a geographical / 
cultural domain of concept A. 
"""
relations.domain_region.ex.en = "`United States <ILIURL/84182>`_ is a domain region of `billion <ILIURL/12132>`_ "
relations.domain_region.exe.en = """
* `Japan <ILIURL/83607>`_ is a domain region of `sushi <ILIURL/78639>`_ 
* `England <ILIURL/83374>`_ is a domain region of `War of the Roses <ILIURL/42242>`_ 
* `Pacific <ILIURL/85934>`_ is a domain region of `Philippine Sea <ILIURL/42156>`_ 
"""
relations.domain_region.com.en = """
We also agreed to change the name for these (to include both
geographical and cultural regions)! But I'm not sure to
what...
"""


### Relation: has_domain_region

relations.has_domain_region.name.en = "Has Domain Region"
relations.has_domain_region.df.en = "A concept which is the term in the geographical / cultural domain of a given concept."
relations.has_domain_region.dfn.en = """
Has Domain Region is a relation between two concepts where Concept A is a term of the geographical /
cultural domain of concept B.
"""
relations.has_domain_region.ex.en = "`billion <ILIURL/12132>`_ has domain region of `United States <ILIURL/84182>`_ "
relations.has_domain_region.exe.en = """
* `sushi <ILIURL/78639>`_ has domain region of `Japan <ILIURL/83607>`_ 
* `War of the Roses <ILIURL/42242>`_ has domain region of `England <ILIURL/83374>`_ 
* `Philippine Sea <ILIURL/42156>`_ has domain region of `Pacific <ILIURL/85934>`_ 
"""
relations.has_domain_region.com.en = """
We have discussed changing the name for these (as they include both
geographical and cultural regions). But we have not yet come up with
a good name.
"""


### Relation: attribute

relations.attribute.name.en = "Attribute"
relations.attribute.df.en = """
an abstraction belonging to or characteristic of an entity
"""
relations.attribute.dfn.en = """
A relation between nominal and adjectival concepts where the concept A
is an attribute of concept B. ‘Attributes’ is a self-reciprocal link
(the two directions of this relation share the same meaning) —
Concept-A attributes to Concept-B, and Concept-B attributes to
Concept-A.

It denotes a relation between a noun and its adjectival attributes,
and vice-versa — for this reason it should only link adjectives to
nouns and vice-versa.
"""
relations.attribute.ex.en = "fertile attribute fecundity"
relations.attribute.exe.en = """
* `fertile <ILIURL/5483>`_ has attributes `fecundity <ILIURL/110773>`_ 
* `fecundity <ILIURL/110773>`_ has attributes `fertile <ILIURL/5483>`_ 
"""
relations.attribute.test.en = """
Attribute-relation between nouns and adjectives (EWN 14)

===     =   ======================================================
yes     a   *A is an attribute of B*
.       .   *B is an attribute of A*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================

Conditions:
- A is a noun in the singular
- B is an adjective
- there is at least one specifying adverb, NP or PP that applies to the A- phrase or the B-phrase
- preferably there is a no morphological link between the noun and the adjective

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
A relation between a classifier concept A and concept B. A relation
between a classifier A and B
"""
relations.classifies.ex.en = "hammer classifies broom"
relations.classifies.exe.en = """
 * `hammer <ILIURL/54582>`_ classifies `teapot <ILIURL/60046>`_
 * `knife <ILIURL/55422>`_ classifies `sword <ILIURL/59896>`_
 * `thread <ILIURL/60206>`_ classifies `rope <ILIURL/58271>`_

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
A relation between concept B and a classifier concept A. A relation
between B and a classifier A.
"""
relations.classified_by.ex.en = ""
relations.classified_by.exe.en = """
 * `broom <ILIURL/51182>`_ classified by `tool with a handle <ILIURL/54612>`_
 * `dagger <ILIURL/52683>`_ classified by `weapon with a blade <ILIURL/50826>`_
 * `wire <ILIURL/61210>`_ classified by `filiform <ILIURL/13360>`_

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
relations.also.ex.en = "time see also moment"
relations.also.exe.en = """
 * `farmer <ILIURL/89889>`_ see also `farmland <ILIURL/82016>`_
 * `learn <ILIURL/24750>`_ see also `school <ILIURL/58518>`_
 * `picture <ILIURL/56911>`_ see also `sculpture <ILIURL/40330>`_
 * `plant <ILIURL/35564>`_ see also `flower <ILIURL/98673>`_
 * `walk <ILIURL/36884>`_ see also `park <ILIURL/82259>`_
 
"""

relations.also.test.en = """
===     =   ======================================================
yes     a   *A has some strong relation to B*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================

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
relations.antonym.ex.en = "Smart has antonym Stupid"
relations.antonym.exe.en = """
 * `man <ILIURL/48657>`_ has antonym `woman <ILIURL/94168>`_
 * `superior <ILIURL/93443>`_ has antonym `inferior <ILIURL/90690>`_
 * `buy <ILIURL/32788>`_ has antonym `sell <ILIURL/41243>`_
 * `northen <ILIURL/8760>`_ has antonym `southern <ILIURL/8772>`_
 * `homosexual <ILIURL/90552>`_ has antonym `heterosexual <ILIURL/6566>`_
 * `sister <ILIURL/93015>`_ has antonym `brother <ILIURL/88710>`_

"""

relations.antonym.test.en = """
Antonym-relation between nouns (EWN 16)

===     =   ======================================================
yes     a   *A and B are both a kind of C but A is the opposite of B*
.       b   *the converse of (a)*

===     =   ======================================================

Conditions:
 - A and B are singular or plural nouns
 - C is a hyperonym of both A and C and within a reasonable, competitive denotational range.
 
 Antonym-relation between verb (EWN 17)

===     =   ======================================================
yes     a   *If something/someone/it As then something/someone/it does not B*
.       b   *If something/someone/it Bs then something/someone/it does not A)*

===     =   ======================================================

Conditions:
 - A is a synset variant in the third person singular form
 - B is a synset variant in the third person singular form
 - A and B are members of co-hyponym synsets
 - there is a hyperonym of A which is opposite to a hyperonym of B
 - the situation referred to by A has an addressee and the addressee is the
   protagonist of the situation referred to by B
   
 Antonym-relation between verbs and adjectives (or adverbs) EWN 20

===     =   ======================================================
yes     a   *If something/someone/it As then something/someone/it is not B*
.       b   *If something/someone/it is B then something/someone/it does not A*

===     =   ======================================================

Conditions:
 - A is a verb in the third person singular form
 - B is an adjective
 - A and Y are (XPOS) co-hyponyms
 
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
unilateral — Verb-A entails Verb-B, without a reciprocal or tracing
link.  This relation presupposes/requires a semantic restriction in
which Verb-B has to take place before or during Verb-A.
"""
relations.entails.ex.en = "snore entails sleep"
relations.entails.exe.en = """
 * `snore <ILIURL/21852>`_ entails `sleep <ILIURL/21840>`_
 
"""

relations.entails.test.en = """
===     =   ======================================================
yes     a   *A cannot be done unless B is or has been done*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================

"""
relations.entails.com.en = """
A verb A entails B if A cannot be done unless B is, or has been, done.
"""


### Relation: is_entailed_by

relations.is_entailed_by.name.en = "Is Entailed By"
relations.is_entailed_by.df.en = "Concept B is dome/happens because of concept A"
relations.is_entailed_by.dfn.en = """
"""
relations.is_entailed_by.ex.en = "sleep is entailed by snore"
relations.is_entailed_by.exe.en = """
 * `sleep <ILIURL/21840>`_ entails `snore <ILIURL/21852>`_

"""

relations.is_entailed_by.test.en = """
===     =   ======================================================
yes     a   *B is the result/happens because of the occurrence of A*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================

"""
relations.is_entailed_by.com.en = """
"""


### Relation: other

relations.other.name.en = "Other"
relations.other.df.en = "not the same one or ones already mentioned or implied"
relations.other.dfn.en = """
This is used for semantic relation types not currently supported by
the OMW DTD.  The exact relation type can be given with ``dc:type``:

.. code:: xml

    <SynsetRelation relType="other" dc:type="emotion" target="example-en-1234-n"/>

"""
relations.other.ex.en = "Physician other Hospital"
relations.other.exe.en = """
 * `curator <ILIURL/89345>`_ other `museum <ILIURL/56456>`_
 * `priest <ILIURL/92229>`_ other `church <ILIURL/40809>`_
 * `mailman <ILIURL/91159>`_ other `post office <ILIURL/79962>`_
 * `mayor <ILIURL/91277>`_ other `town hall <ILIURL/60420>`_
 * `judge <ILIURL/90808>`_ other `court <ILIURL/52438>`_
 * `ambassador <ILIURL/88178>`_ other `embassy <ILIURL/53393>`_
 * `gardener <ILIURL/90153>`_ other `garden <ILIURL/54178>`_
 
"""
relations.other.test.en = """
===     =   ======================================================
yes     a   *A has some strong relation to B*

no      b   the converse of any of the (a) sentences.
===     =   ======================================================

"""
relations.other.com.en = """
A FUZZYNYM relation holds between words with the same part-of-speech, XPOS_FUZZYNYM holds across part-of-speech.
"""

### Relation: participle

relations.participle.name.en = "Participle"
relations.participle.df.en = "A concept which is a participial adjective derived from a verb expressed by a given concept."
relations.participle.dfn.en = """
Participle is a relation between two concepts where Concept A is a participial adjective 
which is drived from Concept B in the form of verb.
"""
relations.participle.ex.en = "`interesting <ILIURL/7324>`_ is the participial of `interest <ILIURL/30833>`_"
relations.participle.exe.en = """
* `interesting <ILIURL/7324>`_ is the participial of `interest <ILIURL/30833>`_
* `amazing <ILIURL/6996>`_ is the participial of `amaze <ILIURL/25324>`_
"""
relations.participle.test.en = """
"""
relations.participle.com.en = """
These are not linked in the NLTK interface so are not shown in OMW 1.0 (or as far as I can 
see, anywhere FCB)
"""

### Relation: pertainym

relations.pertainym.name.en = "Pertainym"
relations.pertainym.df.en = "A concept which is of or pertaining to a given concept."
relations.pertainym.dfn.en = """
Pertainym is a relation between two concepts where Concept A is the adjective to the noun 
expressed by Concept B it is about, or Concept A is the adverb to the adjective expressed 
by Concept B it is about.
"""
relations.pertainym.ex.en = "`slowly <ILIURL/19235>`_ is the pertainym of `slow <ILIURL/5362>`_"
relations.pertainym.exe.en = """
* `lunar <ILIURL/15548>`_ is the pertainym of `moon <ILIURL/85806>`_
* `naval <ILIURL/15629>`_ is the pertainym of `navy <ILIURL/80195>`_
* `slowly <ILIURL/19235>`_ is the pertainym of `slow <ILIURL/5362>`_
* `English <ILIURL/17163>`_ is the pertainym of `England <ILIURL/83374>`_
* `subclinical <ILIURL/16413>`_ is the pertainym of `clinical <ILIURL/16412>`_
* `clinical <ILIURL/16412>`_ is the pertainym of `clinic <ILIURL/79534>`_
"""
relations.pertainym.test.en = """
"""
relations.pertainym.com.en = """
"""


### Relation: derivation

relations.derivation.name.en = "Derivation"
relations.derivation.df.en = "A concept which is a derivationally related form of a given concept."
relations.derivation.dfn.en = """
Derivation is a relation between two concept where Concept A is the derivationally related 
form of Concept B. 
 """
relations.derivation.ex.en = "`yearly <ILIURL/10786>`_ is the derivation of `year <ILIURL/117116>`_"
relations.derivation.exe.en = """
* `yearly <ILIURL/10786>`_ is the derivation of `year <ILIURL/117116>`_
* `want(n) <ILIURL/113167>`_ is the derivation of `want(v) <ILIURL/30852>`_
* `provision <ILIURL/40949>`_ is the derivation of `provide <ILIURL/33372>`_
"""
relations.pertainym.test.en = """
"""
relations.pertainym.com.en = """
This may be specialized further. It includes zero derivations. Gnerally 
it is used for different syntactic categories that have the same root form and are 
semantically related. Wordnet does not say which is the baseform, the relationship 
is fully reversible. 
"""


### New short definitions based on http://globalwordnet.github.io/schemas/

#relations.agent.df.en = "X is typically the agent of the action expressed by Y"
relations.antonym.df.en = "An opposite and inherently incompatible word"
relations.be_in_state.df.en = "X is qualified by Y"
relations.classified_by.df.en = "A relation between Y and a classifier X"
relations.classifies.df.en = "A relation between a classifier X and Y"
#relations.co_agent_instrument.df.en = "Y is the instrument used by X in a certain action"
#relations.co_agent_patient.df.en = "Y is the patient undergoing an action carried out by X"
#relations.co_agent_result.df.en = "Y is the result of an action carried out by X"
#relations.co_instrument_agent.df.en = "X is the instrument used by Y for a certain action"
#relations.co_instrument_patient.df.en = "Y undergoes an action for which the instrument expressed by X is used"
#relations.co_instrument_result.df.en = "Y is the result of an action carried out by the instrument expressed by X"
#relations.co_patient_agent.df.en = "Y undergoes an action carried out by X"
#relations.co_patient_instrument.df.en = "X undergoes an action for which the instrument expressed by X is used"
#relations.co_result_agent.df.en = "X is the result of an action carried out by Y"
#relations.co_result_instrument.df.en = "X is the result of an action for which the instrument expressed by Y is used"
#relations.co_role.df.en = "One concept undergoes an action in which the other concept is involved (bidirectional)"
#relations.direction.df.en = "X is typically the direction or location of the action or event expressed by Y"
relations.eq_synonym.df.en = "X and Y are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)"
relations.holo_location.df.en = "Y is a place located in X"
relations.holo_portion.df.en = "Y is an amount/piece/portion of X"
relations.holonym.df.en = "X makes up a part of Y"
relations.in_manner.df.en = "Y qualifies the manner in which an action or event expressed by X takes place"
#relations.instrument.df.en = "X is the instrument necessary for the action or event expressed by Y"
#relations.involved_agent.df.en = "Y is typically the agent of the action expressed by X"
#relations.involved_direction.df.en = "Y is typically the direction or location of the action or event expressed by X"
#relations.involved_instrument.df.en = "Y is typically the instrument necessary for the action or event expressed by X"
#relations.involved_location.df.en = "Y is typically the location where the action or event expressed by X takes place"
#relations.involved_patient.df.en = "Y is typically the patient un-dergoing an action or event expressed by X"
#relations.involved_result.df.en = "Y comes into existence as a result of X"
#relations.involved_source_direction.df.en = "Y is the place from where the action or event expressed by X begins/starts/happens"
#relations.involved_target_direction.df.en = "Y is the place where the action or event expressed by X leads to"
#relations.involved.df.en = "Y is typically involved in the action or event expressed by X"
relations.is_caused_by.df.en = "X comes about because of Y"
relations.is_entailed_by.df.en = "Opposite of entails"
relations.is_subevent_of.df.en = "X takes place during or as part of Y, and whenever X takes place, Y takes place"
#relations.location.df.en = "X is the location where the action or event expressed by Y takes place"
relations.manner_of.df.en = "X qualifies the manner in which an action or event expressed by Y takes place"
relations.mero_location.df.en = "X is a place located in Y"
relations.mero_portion.df.en = "X is an amount/piece/portion of Y"
relations.meronym.df.en = "Y makes up a part of X"
relations.other.df.en = "Any relation not otherwise specified"
#relations.patient.df.en = "X is the patient undergoing an action or event expressed by Y"
#rels.pertainym.df.en =  "X is of or pertaining to Y"
relations.restricted_by.df.en = "A relation between nominal (pronominal) Y and an adjectival X (quantifier/determiner)"
relations.restricts.df.en = "A relation between an adjectival X (quantifier/determiner) and a nominal (pronominal) Y"
#relations.result.df.en = "X comes into existence as a result of Y"
#relations.role.df.en = "X is typically involved in the action or event expressed by Y"
#relations.source_direction.df.en = "X is the place from where the event expressed by Y begins"
relations.state_of.df.en = "Y is qualified by X"
relations.subevent.df.en = "Y takes place during or as part of X, and whenever Y takes place, X takes place"
#relations.target_direction.df.en = "X is the place to which the action or event expressed by Y leads"

### Relation Simple Aspect

relations.simple_aspect.name.en = "Simple Aspect"
relations.simple_aspect.df.en = "A concept which is linked to another through a change from perfective to imperfective aspect"
relations.simple_aspect.ex.en = ""


### Relation Secondary Aspect

relations.secondary_aspect.name.en = "Secondary Aspect"
relations.secondary_aspect.df.en = "A concept which is linked to another through a change in aspect"
relations.secondary_aspect.ex.en = ""


### Relation: Feminine form

relations.feminine_form_of.name.en = "Feminine form"
relations.feminine_form_of.df.en= "A concept used to refer to female members of a class"
relations.feminine_form_of.ex.en= "*sow* is a female *pig*"


### Relation: Masculine Form

relations.masculine_form_of.name.en = "Masculine Form"
relations.masculine_form_of.df.en= "A concept used to refer to male members of a class"
relations.masculine_form_of.ex.en= "*boar* is a male *pig*"


### Relation: Young Form

relations.young_form_of.name.en = "Young Form"
relations.young_form_of.df.en = "A concept used to refer to young members of a class"
relations.young_form_of.ex.en = "*piglet* is a young *pig*"


### Relation: Diminuative

relations.diminutive_of.name.en = "Diminutive Form"
relations.diminutive_of.df.en = "A concept used to refer to generally smaller members of a class"
relations.diminutive_of.ex.en = "*piggy* is a diminutive *pig*"


### Relation: Augmentative

relations.augmentative_of.name.en = "Augmentative Form"
relations.augmentative_of.df.en = "A concept used to refer to generally larger members of a class"
relations.augmentative_of.ex.en = "*great house* is a larger *house*"


### Relation: Gradable Antonym

relations.anto_gradable.name.en = "Gradable Antonym"
relations.anto_gradable.df.en = "word pairs whose meanings are opposite and which lie on a continuous spectrum"
relations.anto_gradable.ex.en = "*hot* is a gradable antonym of *cold*"
relations.anto_gradable.com.en = "Also known as *polar antonyms*."

### Relation: Simple Antonym

relations.anto_simple.name.en = "Simple Antonym"
relations.anto_simple.df.en = "word pairs whose meanings are opposite but whose meanings do not lie on a continuous spectrum"
relations.anto_simple.ex.en = "*alive* is a simple antonym of *dead*"
relations.anto_gradable.com.en = "Also known as *complementary antonyms*."

### Relation: Converse Antonym

relations.anto_converse.name.en = "Converse Antonym"
relations.anto_converse.df.en = "word pairs that name or describe a single relationship from opposite perspectives"
relations.anto_converse.ex.en = "*parent* is a converse antonym of *child*"
relations.anto_gradable.com.en = "Also known as just *converse* or *relational antonym*."

### Relation: Inter-register Synonym

relations.ir_synonym.name.en = "Inter-register Synonym"
relations.ir_synonym.df.en= "A concept that means the same except for the style or connotation"
relations.ir_synonym.ex.en= "*loot* is an inter-register synonym of *money*"






