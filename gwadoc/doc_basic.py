# -*- coding: utf-8 -*-

from gwadoc import relations


###############################################################################
### Relations Definitions


### Relation: domain

relations.domain.fa.parent = None
relations.domain.fa.synset_synset = True
relations.domain.fa.sense_synset = False
relations.domain.fa.sense_sense = False
relations.domain.fa.reverse = 'has_domain'

relations.domain.proj.ili = ""
relations.domain.proj.pwn = "domain"
relations.domain.proj.querywn = "domn"
relations.domain.proj.eurown = ""
relations.domain.proj.plwordnet = ""
relations.domain.proj.pointer = ""


### Relation: has_domain

relations.has_domain.fa.parent = None
relations.has_domain.fa.synset_synset = True
relations.has_domain.fa.sense_synset = False
relations.has_domain.fa.sense_sense = False
relations.has_domain.fa.reverse = 'domain'

relations.has_domain.proj.ili = ""
relations.has_domain.proj.pwn = "domain term"
relations.has_domain.proj.querywn = "domt"
relations.has_domain.proj.eurown = ""
relations.has_domain.proj.plwordnet = ""
relations.has_domain.proj.pointer = ""


### Relation: constitutive

relations.constitutive.fa.parent = None
relations.constitutive.fa.synset_synset = False
relations.constitutive.fa.sense_synset = False
relations.constitutive.fa.sense_sense = False


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

relations.hypernym.name.symbol = "⊃"

relations.hypernym.fa.parent = 'constitutive'
relations.hypernym.fa.synset_synset = True
relations.hypernym.fa.sense_synset = False
relations.hypernym.fa.sense_sense = False
relations.hypernym.fa.inOMW = True
relations.hypernym.fa.reverse = "hyponym"

relations.hypernym.proj.ili = """i69569"""
relations.hypernym.proj.querywn = "hype"
relations.hypernym.proj.eurown = "has_hyperonym"
relations.hypernym.proj.plwordnet = "hyperonymy"
relations.hypernym.proj.pointer = "@"


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

relations.hyponym.name.symbol = "⊂"

relations.hyponym.fa.parent = 'constitutive'
relations.hyponym.fa.synset_synset = True
relations.hyponym.fa.sense_synset = False
relations.hyponym.fa.sense_sense = False
relations.hyponym.fa.inOMW = True
relations.hyponym.fa.reverse = "hypernym"

relations.hyponym.proj.ili = "i69570"
relations.hyponym.proj.pwn = "hyponym"
relations.hyponym.proj.querywn = "hypo"
relations.hyponym.proj.eurown = "has_hyponym"
relations.hyponym.proj.plwordnet = "hyponymy"
relations.hyponym.proj.pointer = "~"


### Relation: similar

relations.similar.fa.parent = 'constitutive'
relations.similar.fa.synset_synset = True
relations.similar.fa.sense_synset = False
relations.similar.fa.sense_sense = True
relations.similar.fa.inOMW = True
relations.similar.fa.reverse = "similar"

relations.similar.proj.ili = "i13187"
relations.similar.proj.pwn = "Similar to and Verb Group"
relations.similar.proj.querywn = "sim"
relations.similar.proj.eurown = "near_synonym"
relations.similar.proj.plwordnet = "podobny"
relations.similar.proj.pointer = "&"


### Relation: role

relations.role.fa.parent = None
relations.role.fa.synset_synset = True
relations.role.fa.sense_synset = False
relations.role.fa.sense_sense = False
relations.role.fa.inOMW = True
relations.role.fa.reverse = "involved"

relations.role.proj.ili = "i64041"
relations.role.proj.pwn = ""
relations.role.proj.querywn = ""
relations.role.proj.eurown = "role"
relations.role.proj.plwordnet = "rola"
relations.role.proj.pointer = ""


### Relation: agent

relations.agent.fa.parent = 'role'
relations.agent.fa.synset_synset = True
relations.agent.fa.sense_synset = False
relations.agent.fa.sense_sense = False
relations.agent.fa.inOMW = True
relations.agent.fa.reverse = "involved_agent"

relations.agent.proj.ili = "i69754"
relations.agent.proj.pwn = ""
relations.agent.proj.querywn = ""
relations.agent.proj.eurown = "role_agent"
relations.agent.proj.plwordnet = ""
relations.agent.proj.pointer = ""


### Relation: patient

relations.patient.fa.parent = 'role'
relations.patient.fa.synset_synset = True
relations.patient.fa.sense_synset = False
relations.patient.fa.sense_sense = False
relations.patient.fa.inOMW = True
relations.patient.fa.reverse = "involved_patient"

relations.patient.proj.ili = "i69753"
relations.patient.proj.pwn = ""
relations.patient.proj.querywn = ""
relations.patient.proj.eurown = "role_patient"
relations.patient.proj.plwordnet = ""
relations.patient.proj.pointer = ""


### Relation: result

relations.result.fa.parent = 'role'
relations.result.fa.synset_synset = True
relations.result.fa.sense_synset = False
relations.result.fa.sense_sense = False
relations.result.fa.inOMW = True
relations.result.fa.reverse = "involved_result"

relations.result.proj.ili = "i69759"
relations.result.proj.pwn = ""
relations.result.proj.querywn = ""
relations.result.proj.eurown = "role_result"
relations.result.proj.plwordnet = ""
relations.result.proj.pointer = ""


### Relation: instrument

relations.instrument.fa.parent = 'role'
relations.instrument.fa.synset_synset = True
relations.instrument.fa.sense_synset = False
relations.instrument.fa.sense_sense = False
relations.instrument.fa.inOMW = True
relations.instrument.fa.reverse = "involved_instrument"

relations.instrument.proj.ili = "i69756"
relations.instrument.proj.pwn = ""
relations.instrument.proj.querywn = ""
relations.instrument.proj.eurown = "role_instrument"
relations.instrument.proj.plwordnet = ""
relations.instrument.proj.pointer = ""


### Relation: location

relations.location.fa.parent = 'role'
relations.location.fa.synset_synset = True
relations.location.fa.sense_synset = False
relations.location.fa.sense_sense = False
relations.location.fa.inOMW = True
relations.location.fa.reverse = "involved_location"

relations.location.proj.ili = "i35580"
relations.location.proj.pwn = ""
relations.location.proj.querywn = ""
relations.location.proj.eurown = "role_location"
relations.location.proj.plwordnet = ""
relations.location.proj.pointer = ""


### Relation: direction

relations.direction.fa.parent = 'role'
relations.direction.fa.synset_synset = True
relations.direction.fa.sense_synset = False
relations.direction.fa.sense_sense = False
relations.direction.fa.inOMW = True
relations.direction.fa.reverse = "involved_direction"

relations.direction.proj.ili = "i82556"
relations.direction.proj.pwn = ""
relations.direction.proj.querywn = ""
relations.direction.proj.eurown = "role_direction"
relations.direction.proj.plwordnet = ""
relations.direction.proj.pointer = ""


### Relation: target_direction

relations.target_direction.fa.parent = 'role'
relations.target_direction.fa.synset_synset = True
relations.target_direction.fa.sense_synset = False
relations.target_direction.fa.sense_sense = False
relations.target_direction.fa.inOMW = True
relations.target_direction.fa.reverse = "involved_target_direction"

relations.target_direction.proj.ili = "i82007" ###(ili doesn't have target in it)
relations.target_direction.proj.pwn = ""
relations.target_direction.proj.querywn = ""
relations.target_direction.proj.eurown = "role_target_direction"
relations.target_direction.proj.plwordnet = ""
relations.target_direction.proj.pointer = ""


### Relation: source_direction

relations.source_direction.fa.parent = 'role'
relations.source_direction.fa.synset_synset = True
relations.source_direction.fa.sense_synset = False
relations.source_direction.fa.sense_sense = False
relations.source_direction.fa.inOMW = True
relations.source_direction.fa.reverse = "involved_source_direction"

relations.source_direction.proj.ili = "i81759"
relations.source_direction.proj.pwn = ""
relations.source_direction.proj.querywn = ""
relations.source_direction.proj.eurown = "role_source_direction"
relations.source_direction.proj.plwordnet = ""
relations.source_direction.proj.pointer = ""


### Relation: involved

relations.involved.fa.parent = None
relations.involved.fa.synset_synset = True
relations.involved.fa.sense_synset = False
relations.involved.fa.sense_sense = False
relations.involved.fa.inOMW = True
relations.involved.fa.reverse = "role"

relations.involved.proj.ili = "i8315"
relations.involved.proj.pwn = ""
relations.involved.proj.querywn = ""
relations.involved.proj.eurown = "involved"
relations.involved.proj.plwordnet = "unspecified subtype, time and causation inclusion"
relations.involved.proj.pointer = ""


### Relation: involved_agent (EuroWordNet - page 29/30)

relations.involved_agent.fa.parent = 'involved'
relations.involved_agent.fa.synset_synset = True
relations.involved_agent.fa.sense_synset = False
relations.involved_agent.fa.sense_sense = False
relations.involved_agent.fa.inOMW = True
relations.involved_agent.fa.reverse = "agent"

relations.involved_agent.proj.ili = ""
relations.involved_agent.proj.pwn = ""
relations.involved_agent.proj.querywn = ""
relations.involved_agent.proj.eurown = "involved_agent"
relations.involved_agent.proj.plwordnet = "agent inclusion"
relations.involved_agent.proj.pointer = ""


### Relation: involved_patient

relations.involved_patient.fa.parent = 'involved'
relations.involved_patient.fa.synset_synset = True
relations.involved_patient.fa.sense_synset = False
relations.involved_patient.fa.sense_sense = False
relations.involved_patient.fa.inOMW = True
relations.involved_patient.fa.reverse = "patient"

relations.involved_patient.proj.ili = ""
relations.involved_patient.proj.pwn = ""
relations.involved_patient.proj.querywn = ""
relations.involved_patient.proj.eurown = "involved_patient"
relations.involved_patient.proj.plwordnet = "patient inclusion"
relations.involved_patient.proj.pointer = ""


### Relation: involved_result

relations.involved_result.fa.parent = 'involved'
relations.involved_result.fa.synset_synset = True
relations.involved_result.fa.sense_synset = False
relations.involved_result.fa.sense_sense = False
relations.involved_result.fa.inOMW = True
relations.involved_result.fa.reverse = "result"

relations.involved_result.proj.ili = ""
relations.involved_result.proj.pwn = ""
relations.involved_result.proj.querywn = ""
relations.involved_result.proj.eurown = "involved_result"
relations.involved_result.proj.plwordnet = "result inclusion"
relations.involved_result.proj.pointer = ""


### Relation: involved_instrument

relations.involved_instrument.fa.parent = 'involved'
relations.involved_instrument.fa.synset_synset = True
relations.involved_instrument.fa.sense_synset = False
relations.involved_instrument.fa.sense_sense = False
relations.involved_instrument.fa.inOMW = True
relations.involved_instrument.fa.reverse = "instrument"

relations.involved_instrument.proj.ili = ""
relations.involved_instrument.proj.pwn = ""
relations.involved_instrument.proj.querywn = ""
relations.involved_instrument.proj.eurown = "involved_instrument"
relations.involved_instrument.proj.plwordnet = "instrument inclusion"
relations.involved_instrument.proj.pointer = ""


### Relation: involved_location

relations.involved_location.fa.parent = 'involved'
relations.involved_location.fa.synset_synset = True
relations.involved_location.fa.sense_synset = False
relations.involved_location.fa.sense_sense = False
relations.involved_location.fa.inOMW = True
relations.involved_location.fa.reverse = "location"

relations.involved_location.proj.ili = ""
relations.involved_location.proj.pwn = ""
relations.involved_location.proj.querywn = ""
relations.involved_location.proj.eurown = "involved_location"
relations.involved_location.proj.plwordnet = "location inclusion"
relations.involved_location.proj.pointer = ""


### Relation: involved_direction

relations.involved_direction.fa.parent = 'involved'
relations.involved_direction.fa.synset_synset = True
relations.involved_direction.fa.sense_synset = False
relations.involved_direction.fa.sense_sense = False
relations.involved_direction.fa.inOMW = True
relations.involved_direction.fa.reverse = "direction"

relations.involved_direction.proj.ili = ""
relations.involved_direction.proj.pwn = ""
relations.involved_direction.proj.querywn = ""
relations.involved_direction.proj.eurown = "involved_direction"
relations.involved_direction.proj.plwordnet = ""
relations.involved_direction.proj.pointer = ""


### Relation: involved_target_direction

relations.involved_target_direction.fa.parent = 'involved'
relations.involved_target_direction.fa.synset_synset = True
relations.involved_target_direction.fa.sense_synset = False
relations.involved_target_direction.fa.sense_sense = False
relations.involved_target_direction.fa.inOMW = True
relations.involved_target_direction.fa.reverse = "target_direction"

relations.involved_target_direction.proj.ili = ""
relations.involved_target_direction.proj.pwn = ""
relations.involved_target_direction.proj.querywn = ""
relations.involved_target_direction.proj.eurown = "involved_target_direction"
relations.involved_target_direction.proj.plwordnet = ""
relations.involved_target_direction.proj.pointer = ""


### Relation: involved_source_direction

relations.involved_source_direction.fa.parent = 'involved'
relations.involved_source_direction.fa.synset_synset = True
relations.involved_source_direction.fa.sense_synset = False
relations.involved_source_direction.fa.sense_sense = False
relations.involved_source_direction.fa.inOMW = True
relations.involved_source_direction.fa.reverse = "source_direction"

relations.involved_source_direction.proj.ili = ""
relations.involved_source_direction.proj.pwn = ""
relations.involved_source_direction.proj.querywn = ""
relations.involved_source_direction.proj.eurown = "involved_source_direction"
relations.involved_source_direction.proj.plwordnet = ""
relations.involved_source_direction.proj.pointer = ""


### Relation: co_role EDP31

relations.co_role.fa.parent = 'role'
relations.co_role.fa.synset_synset = True
relations.co_role.fa.sense_synset = False
relations.co_role.fa.sense_sense = False
relations.co_role.fa.inOMW = True
relations.co_role.fa.reverse = "co_role"

relations.co_role.proj.eurown = "co_role"
relations.co_role.proj.plwordnet = ""


### Relation: co_agent_patient EDP32

relations.co_agent_patient.fa.parent = 'co_role'
relations.co_agent_patient.fa.synset_synset = True
relations.co_agent_patient.fa.sense_synset = False
relations.co_agent_patient.fa.sense_sense = False
relations.co_agent_patient.fa.inOMW = True
relations.co_agent_patient.fa.reverse = "co_patient_agent"

relations.co_agent_patient.proj.eurown = "co_agent_patient"
relations.co_agent_patient.proj.plwordnet = ""


### Relation: co_agent_instrument EDP32

relations.co_agent_instrument.fa.parent = 'co_role'
relations.co_agent_instrument.fa.synset_synset = True
relations.co_agent_instrument.fa.sense_synset = False
relations.co_agent_instrument.fa.sense_sense = False
relations.co_agent_instrument.fa.inOMW = True
relations.co_agent_instrument.fa.reverse = "co_instrument_agent"

relations.co_agent_instrument.proj.eurown = "co_agent_instrument"
relations.co_agent_instrument.proj.plwordnet = ""


### Relation: co_agent_result EDP32

relations.co_agent_result.fa.parent = 'co_role'
relations.co_agent_result.fa.synset_synset = True
relations.co_agent_result.fa.sense_synset = False
relations.co_agent_result.fa.sense_sense = False
relations.co_agent_result.fa.inOMW = True
relations.co_agent_result.fa.reverse = "co_result_agent"

relations.co_agent_result.proj.eurown = "co_agent_result"
relations.co_agent_result.proj.plwordnet = ""


### Relation: co_patient_agent EDP32

relations.co_patient_agent.fa.parent = 'co_role'
relations.co_patient_agent.fa.synset_synset = True
relations.co_patient_agent.fa.sense_synset = False
relations.co_patient_agent.fa.sense_sense = False
relations.co_patient_agent.fa.inOMW = True
relations.co_patient_agent.fa.reverse = "co_agent_patient"

relations.co_patient_agent.proj.eurown = "co_patient_agent"
relations.co_patient_agent.proj.plwordnet = ""


### Relation: co_patient_instrument EDP32

relations.co_patient_instrument.fa.parent = 'co_role'
relations.co_patient_instrument.fa.synset_synset = True
relations.co_patient_instrument.fa.sense_synset = False
relations.co_patient_instrument.fa.sense_sense = False
relations.co_patient_instrument.fa.inOMW = True
relations.co_patient_instrument.fa.reverse = "co_instrument_patient"

relations.co_patient_instrument.proj.eurown = "co_patient_instrument"
relations.co_patient_instrument.proj.plwordnet = ""


### Relation: co_result_agent EDP32

relations.co_result_agent.fa.parent = 'co_role'
relations.co_result_agent.fa.synset_synset = True
relations.co_result_agent.fa.sense_synset = False
relations.co_result_agent.fa.sense_sense = False
relations.co_result_agent.fa.inOMW = True
relations.co_result_agent.fa.reverse = "co_agent_result"

relations.co_result_agent.proj.eurown = "co_result_agent"
relations.co_result_agent.proj.plwordnet = ""


### Relation: co_result_instrument EDP32

relations.co_result_instrument.fa.parent = 'co_role'
relations.co_result_instrument.fa.synset_synset = True
relations.co_result_instrument.fa.sense_synset = False
relations.co_result_instrument.fa.sense_sense = False
relations.co_result_instrument.fa.inOMW = True
relations.co_result_instrument.fa.reverse = "co_instrument_result"

relations.co_result_instrument.proj.eurown = "co_result_instrument"
relations.co_result_instrument.proj.plwordnet = ""


### Relation: co_instrument_agent EDP32

relations.co_instrument_agent.fa.parent = 'co_role'
relations.co_instrument_agent.fa.synset_synset = True
relations.co_instrument_agent.fa.sense_synset = False
relations.co_instrument_agent.fa.sense_sense = False
relations.co_instrument_agent.fa.inOMW = True
relations.co_instrument_agent.fa.reverse = "co_agent_instrument"

relations.co_instrument_agent.proj.eurown = "co_instrument_agent"
relations.co_instrument_agent.proj.plwordnet = ""


### Relation: co_instrument_patient EDP32

relations.co_instrument_patient.fa.parent = 'co_role'
relations.co_instrument_patient.fa.synset_synset = True
relations.co_instrument_patient.fa.sense_synset = False
relations.co_instrument_patient.fa.sense_sense = False
relations.co_instrument_patient.fa.inOMW = True
relations.co_instrument_patient.fa.reverse = "co_patient_instrument"

relations.co_instrument_patient.proj.eurown = "co_instrument_patient"
relations.co_instrument_patient.proj.plwordnet = ""


### Relation: co_instrument_result ice saw/ice

relations.co_instrument_result.fa.parent = 'co_role'
relations.co_instrument_result.fa.synset_synset = True
relations.co_instrument_result.fa.sense_synset = False
relations.co_instrument_result.fa.sense_sense = False
relations.co_instrument_result.fa.inOMW = True
relations.co_instrument_result.fa.reverse = "co_result_instrument"

relations.co_instrument_result.proj.eurown = "co_instrument_result"
relations.co_instrument_result.proj.plwordnet = ""


### Relation: state_of EDP37

relations.state_of.fa.parent = 'other'
relations.state_of.fa.synset_synset = True
relations.state_of.fa.sense_synset = False
relations.state_of.fa.sense_sense = False
relations.state_of.fa.inOMW = True
relations.state_of.fa.reverse = "be_in_state"

relations.state_of.proj.ili = "i35578"
relations.state_of.proj.pwn = "attribute"
relations.state_of.proj.eurown = "state_of"
relations.state_of.proj.plwordnet = "stan|cecha"
relations.state_of.proj.pointer = "="


### Relation: be_in_state EDP37

relations.be_in_state.fa.parent = 'other'
relations.be_in_state.fa.synset_synset = True
relations.be_in_state.fa.sense_synset = False
relations.be_in_state.fa.sense_sense = False
relations.be_in_state.fa.inOMW = True
relations.be_in_state.fa.reverse = "state_of"

relations.be_in_state.proj.eurown = "be_in_state"
relations.be_in_state.proj.plwordnet = "nosiciel_stanu|cechy"
relations.be_in_state.proj.pointer = ""


### Relation: causes EDP34

relations.causes.fa.parent = 'other'
relations.causes.fa.synset_synset = True
relations.causes.fa.sense_synset = False
relations.causes.fa.sense_sense = False
relations.causes.fa.inOMW = True
relations.causes.fa.reverse = "is_caused_by"

relations.causes.proj.ili = "i35561"
relations.causes.proj.pwn = "cause"
relations.causes.proj.querywn = "caus"
relations.causes.proj.eurown = "causes"
relations.causes.proj.plwordnet = "cause"
relations.causes.proj.pointer = ">"


### Relation: is_caused_by EDP34

relations.is_caused_by.fa.parent = 'other'
relations.is_caused_by.fa.synset_synset = True
relations.is_caused_by.fa.sense_synset = False
relations.is_caused_by.fa.sense_sense = False
relations.is_caused_by.fa.inOMW = True
relations.is_caused_by.fa.reverse = "causes"

relations.is_caused_by.proj.pwn = ""
relations.is_caused_by.proj.querywn = "caus"
relations.is_caused_by.proj.eurown = "is_caused_by"
relations.is_caused_by.proj.plwordnet = ""
relations.is_caused_by.proj.pointer = ""


### Relation: subevent EDP35

relations.subevent.fa.parent = 'other'
relations.subevent.fa.synset_synset = True
relations.subevent.fa.sense_synset = False
relations.subevent.fa.sense_sense = False
relations.subevent.fa.inOMW = True
relations.subevent.fa.reverse = "is_subevent_of"

relations.subevent.proj.querywn = "enta"
relations.subevent.proj.eurown = "has_subevent"
relations.subevent.proj.plwordnet = "holonimia sytuacji towarzyszącej"
relations.subevent.proj.pointer = "\*"


### Relation: is_subevent_of EDP35

relations.is_subevent_of.fa.parent = 'other'
relations.is_subevent_of.fa.synset_synset = True
relations.is_subevent_of.fa.sense_synset = False
relations.is_subevent_of.fa.sense_sense = False
relations.is_subevent_of.fa.inOMW = True
relations.is_subevent_of.fa.reverse = "subevent"

relations.is_subevent_of.proj.querywn = "enta"
relations.is_subevent_of.proj.eurown = "is_subevent_of"
relations.is_subevent_of.proj.plwordnet = "meronimia sytuacji towarzyszącej"
relations.is_subevent_of.proj.pointer = "*"


### Relation: in_manner EDP36

relations.in_manner.fa.parent = 'other'
relations.in_manner.fa.synset_synset = True
relations.in_manner.fa.sense_synset = False
relations.in_manner.fa.sense_sense = False
relations.in_manner.fa.inOMW = True
relations.in_manner.fa.reverse = "manner_of"

relations.in_manner.proj.querywn = "enta"
relations.in_manner.proj.eurown = "in_manner"
relations.in_manner.proj.plwordnet = ""
relations.in_manner.proj.pointer = ""


### Relation: manner_of EDP36

relations.manner_of.fa.parent = 'other'
relations.manner_of.fa.synset_synset = True
relations.manner_of.fa.sense_synset = False
relations.manner_of.fa.sense_sense = False
relations.manner_of.fa.inOMW = True
relations.manner_of.fa.reverse = "in_manner"

relations.manner_of.proj.ili = "i62791"
relations.manner_of.proj.querywn = "enta"
relations.manner_of.proj.eurown = "manner_of"
relations.manner_of.proj.plwordnet = "sposób"
relations.manner_of.proj.pointer = ""


### Relation: meronym EDP26

relations.meronym.fa.parent = 'constitutive'
relations.meronym.fa.synset_synset = True
relations.meronym.fa.sense_synset = False
relations.meronym.fa.sense_sense = False
relations.meronym.fa.inOMW = True
relations.meronym.fa.reverse = "holonym"

relations.meronym.proj.ili = "i69575"
relations.meronym.proj.pwn = "meronym"
relations.meronym.proj.querywn = "mero"
relations.meronym.proj.eurown = "has_meronym"
relations.meronym.proj.plwordnet = "meronim"
relations.meronym.proj.pointer = "%"


### Relation: holonym EDP26

relations.holonym.fa.parent = 'constitutive'
relations.holonym.fa.synset_synset = True
relations.holonym.fa.sense_synset = False
relations.holonym.fa.sense_sense = False
relations.holonym.fa.inOMW = True
relations.holonym.fa.reverse = "meronym"

relations.holonym.proj.ili = "i69567"
relations.holonym.proj.querywn = "holo"
relations.holonym.proj.eurown = "has_holonym"
relations.holonym.proj.plwordnet = "holonim"
relations.holonym.proj.pointer = "#"


### Relation: mero_part EDP27

relations.mero_part.fa.parent = 'meronym'
relations.mero_part.fa.synset_synset = True
relations.mero_part.fa.sense_synset = False
relations.mero_part.fa.sense_sense = False
relations.mero_part.fa.inOMW = True
relations.mero_part.fa.reverse = "holo_part"

relations.mero_part.proj.pwn = "part meronym"
relations.mero_part.proj.querywn = "mprt"
relations.mero_part.proj.eurown = "has_mero_part"
relations.mero_part.proj.plwordnet = "meronymy_part"
relations.mero_part.proj.pointer = "%p"


### Relation: holo_part EDP27

relations.holo_part.fa.parent = 'holonym'
relations.holo_part.fa.synset_synset = True
relations.holo_part.fa.sense_synset = False
relations.holo_part.fa.sense_sense = False
relations.holo_part.fa.inOMW = True
relations.holo_part.fa.reverse = "mero_part"

relations.holo_part.proj.pwn = "part holonym"
relations.holo_part.proj.querywn = "hprt"
relations.holo_part.proj.eurown = "has_holo_part"
relations.holo_part.proj.plwordnet = "holonymy_part"
relations.holo_part.proj.pointer = "#p"


### Relation: mero_member EPD27

relations.mero_member.fa.parent = 'meronym'
relations.mero_member.fa.synset_synset = True
relations.mero_member.fa.sense_synset = False
relations.mero_member.fa.sense_sense = False
relations.mero_member.fa.inOMW = True
relations.mero_member.fa.reverse = "holo_member"

relations.mero_member.proj.pwn = "member meronym"
relations.mero_member.proj.querywn = "mmem"
relations.mero_member.proj.eurown = "has_mero_member"
relations.mero_member.proj.plwordnet = "meronymy_member"
relations.mero_member.proj.pointer = "%m"


### Relation: holo_member EDP27

relations.holo_member.fa.parent = 'holonym'
relations.holo_member.fa.synset_synset = True
relations.holo_member.fa.sense_synset = False
relations.holo_member.fa.sense_sense = False
relations.holo_member.fa.inOMW = True
relations.holo_member.fa.reverse = "mero_member"

relations.holo_member.proj.pwn = "member holonym"
relations.holo_member.proj.querywn = "hmem"
relations.holo_member.proj.eurown = "has_holo_member"
relations.holo_member.proj.plwordnet = "holonymy_member"
relations.holo_member.proj.pointer = "#m"


### Relation: mero_substance EDP28

relations.mero_substance.fa.parent = 'meronym'
relations.mero_substance.fa.synset_synset = True
relations.mero_substance.fa.sense_synset = False
relations.mero_substance.fa.sense_sense = False
relations.mero_substance.fa.inOMW = True
relations.mero_substance.fa.reverse = "holo_substance"

relations.mero_substance.proj.pwn = "substance meronym"
relations.mero_substance.proj.querywn = "msub"
relations.mero_substance.proj.eurown = "has_mero_madeof"
relations.mero_substance.proj.plwordnet = "meronymy_substance"
relations.mero_substance.proj.pointer = "%s"


### Relation: holo_substance EDP28

relations.holo_substance.fa.parent = 'holonym'
relations.holo_substance.fa.synset_synset = True
relations.holo_substance.fa.sense_synset = False
relations.holo_substance.fa.sense_sense = False
relations.holo_substance.fa.inOMW = True
relations.holo_substance.fa.reverse = "mero_substance"

relations.holo_substance.proj.pwn = "substance holonym"
relations.holo_substance.proj.querywn = "hsub"
relations.holo_substance.proj.eurown = "has_holo_madeof"
relations.holo_substance.proj.plwordnet = "holonymy_substance"
relations.holo_substance.proj.pointer = "#s"


### Relation: mero_location EDP28

relations.mero_location.fa.parent = 'meronym'
relations.mero_location.fa.synset_synset = True
relations.mero_location.fa.sense_synset = False
relations.mero_location.fa.sense_sense = False
relations.mero_location.fa.inOMW = True
relations.mero_location.fa.reverse = "holo_location"

relations.mero_location.proj.querywn = "hsub"
relations.mero_location.proj.eurown = "has_mero_location"
relations.mero_location.proj.plwordnet = "meronymy_location"


### Relation: holo_location EDP28

relations.holo_location.fa.parent = 'holonym'
relations.holo_location.fa.synset_synset = True
relations.holo_location.fa.sense_synset = False
relations.holo_location.fa.sense_sense = False
relations.holo_location.fa.inOMW = True
relations.holo_location.fa.reverse = "mero_location"

relations.holo_location.proj.querywn = "hsub"
relations.holo_location.proj.eurown = "has_holo_location"
relations.holo_location.proj.plwordnet = "holonymy_location"


### Relation: mero_portion EDP27

relations.mero_portion.fa.parent = 'meronym'
relations.mero_portion.fa.synset_synset = True
relations.mero_portion.fa.sense_synset = False
relations.mero_portion.fa.sense_sense = False
relations.mero_portion.fa.inOMW = True
relations.mero_portion.fa.reverse = "holo_portion"

relations.mero_portion.proj.pwn = "portion meronym"
relations.mero_portion.proj.querywn = "hsub"
relations.mero_portion.proj.eurown = "has_mero_portion"
relations.mero_portion.proj.plwordnet = "meronymy_portion"
relations.mero_portion.proj.pointer = ""


### Relation: holo_portion EDP27

relations.holo_portion.fa.parent = 'holonym'
relations.holo_portion.fa.synset_synset = True
relations.holo_portion.fa.sense_synset = False
relations.holo_portion.fa.sense_sense = False
relations.holo_portion.fa.inOMW = True
relations.holo_portion.fa.reverse = "mero_portion"

relations.holo_portion.proj.querywn = "hsub"
relations.holo_portion.proj.eurown = "has_holo_portion"
relations.holo_portion.proj.plwordnet = "holonymy_portion"
relations.holo_portion.proj.pointer = ""


### Relation: eq_synonym

relations.eq_synonym.fa.parent = 'constitutive'
relations.eq_synonym.fa.synset_synset = True
relations.eq_synonym.fa.sense_synset = False
relations.eq_synonym.fa.sense_sense = False
relations.eq_synonym.fa.inOMW = True
relations.eq_synonym.fa.reverse = "eq_synonym"

relations.eq_synonym.proj.ili = "i69607"
relations.eq_synonym.proj.eurown = "eq_synonym"
relations.eq_synonym.proj.plwordnet = "synonim"


### Relation: instance_hypernym

relations.instance_hypernym.fa.parent = 'constitutive'
relations.instance_hypernym.fa.synset_synset = True
relations.instance_hypernym.fa.sense_synset = False
relations.instance_hypernym.fa.sense_sense = False
relations.instance_hypernym.fa.inOMW = True
relations.instance_hypernym.fa.reverse = "instance_hyponym"

relations.instance_hypernym.proj.pwn = "Instance Hypernym"
relations.instance_hypernym.proj.querywn = "hypes"
relations.instance_hypernym.proj.eurown = "has_instance"
relations.instance_hypernym.proj.plwordnet = "type"
relations.instance_hypernym.proj.pointer = "@i"


### Relation: instance_hyponym

relations.instance_hyponym.fa.parent = 'constitutive'
relations.instance_hyponym.fa.synset_synset = True
relations.instance_hyponym.fa.sense_synset = False
relations.instance_hyponym.fa.sense_sense = False
relations.instance_hyponym.fa.inOMW = True
relations.instance_hyponym.fa.reverse = "instance_hypernym"

relations.instance_hyponym.proj.ili = "i75102"
relations.instance_hyponym.proj.pwn = "Instance Hyponym"
relations.instance_hyponym.proj.querywn = "hasi"
relations.instance_hyponym.proj.eurown = "instance_hyponym"
relations.instance_hyponym.proj.plwordnet = "typ"
relations.instance_hyponym.proj.pointer = "~i"


### Relation: exemplifies

relations.exemplifies.fa.parent = 'domain'
relations.exemplifies.fa.synset_synset = True
relations.exemplifies.fa.sense_synset = True
relations.exemplifies.fa.sense_sense = True
relations.exemplifies.fa.inOMW = True
relations.exemplifies.fa.reverse = "is_exemplified_by"

relations.exemplifies.proj.ili = "i108797"
relations.exemplifies.proj.pwn = "Member of this domain - USAGE"
relations.exemplifies.proj.querywn = "dmtu"
relations.exemplifies.proj.eurown = ""
relations.exemplifies.proj.plwordnet = ""
relations.exemplifies.proj.pointer = "-u"


### Relation: is_exemplified_by

relations.is_exemplified_by.fa.parent = 'has_domain'
relations.is_exemplified_by.fa.synset_synset = True
relations.is_exemplified_by.fa.sense_synset = False
relations.is_exemplified_by.fa.sense_sense = True
relations.is_exemplified_by.fa.inOMW = True
relations.is_exemplified_by.fa.reverse = "exemplifies"

relations.is_exemplified_by.proj.ili = ""
relations.is_exemplified_by.proj.pwn = "Domain of synset - USAGE"
relations.is_exemplified_by.proj.querywn = "dmnu"
relations.is_exemplified_by.proj.eurown = ""
relations.is_exemplified_by.proj.plwordnet = ""
relations.is_exemplified_by.proj.pointer = ";u"


### Relation: domain_topic

relations.domain_topic.fa.parent = 'domain'
relations.domain_topic.fa.synset_synset = True
relations.domain_topic.fa.sense_synset = True
relations.domain_topic.fa.sense_sense = True
relations.domain_topic.fa.inOMW = True
relations.domain_topic.fa.reverse = "has_domain_topic"

relations.domain_topic.proj.ili = ""
relations.domain_topic.proj.pwn = "Domain of synset - TOPIC"
relations.domain_topic.proj.querywn = "dmnc"
relations.domain_topic.proj.eurown = ""
relations.domain_topic.proj.plwordnet = ""
relations.domain_topic.proj.pointer = ";c"


### Relation: has_domain_topic

relations.has_domain_topic.fa.parent = 'has_domain'
relations.has_domain_topic.fa.synset_synset = True
relations.has_domain_topic.fa.sense_synset = False
relations.has_domain_topic.fa.sense_sense = True
relations.has_domain_topic.fa.inOMW = True
relations.has_domain_topic.fa.reverse = "domain_topic"

relations.has_domain_topic.proj.ili = ""
relations.has_domain_topic.proj.pwn = "Member of this domain - TOPIC"
relations.has_domain_topic.proj.querywn = "dmtc"
relations.has_domain_topic.proj.eurown = ""
relations.has_domain_topic.proj.plwordnet = ""
relations.has_domain_topic.proj.pointer = "-c"


### Relation: domain_region

relations.domain_region.fa.parent = 'domain'
relations.domain_region.fa.synset_synset = True
relations.domain_region.fa.sense_synset = True
relations.domain_region.fa.sense_sense = True
relations.domain_region.fa.inOMW = True
relations.domain_region.fa.reverse = "has_domain_region"

relations.domain_region.proj.ili = ""
relations.domain_region.proj.pwn = "Domain of synset - REGION"
relations.domain_region.proj.querywn = "dmnr"
relations.domain_region.proj.eurown = ""
relations.domain_region.proj.plwordnet = ""
relations.domain_region.proj.pointer = ";r"


### Relation: has_domain_region

relations.has_domain_region.fa.parent = 'has_domain'
relations.has_domain_region.fa.synset_synset = True
relations.has_domain_region.fa.sense_synset = False
relations.has_domain_region.fa.sense_sense = True
relations.has_domain_region.fa.inOMW = True
relations.has_domain_region.fa.reverse = "domain_region"

relations.has_domain_region.proj.ili = ""
relations.has_domain_region.proj.pwn = "Member of this domain - REGION"
relations.has_domain_region.proj.querywn = "dmtr"
relations.has_domain_region.proj.eurown = ""
relations.has_domain_region.proj.plwordnet = ""
relations.has_domain_region.proj.pointer = "-r"


### Relation: attribute

relations.attribute.fa.parent = 'other'
relations.attribute.fa.synset_synset = True
relations.attribute.fa.sense_synset = False
relations.attribute.fa.sense_sense = False
relations.attribute.fa.inOMW = True
relations.attribute.fa.reverse = "attribute"

relations.attribute.proj.ili = "i35577"
relations.attribute.proj.pwn = "attribute"
relations.attribute.proj.querywn = "attr"
relations.attribute.proj.plwordnet = "Attribute"
relations.attribute.proj.pointer = "="


### Relation: restricts

relations.restricts.fa.parent = 'other'
relations.restricts.fa.synset_synset = True
relations.restricts.fa.sense_synset = False
relations.restricts.fa.sense_sense = False
relations.restricts.fa.inOMW = True
relations.restricts.fa.reverse = "restricted_by"

relations.restricts.proj.ili = "i22888"
relations.restricts.proj.plwordnet = ""
relations.restricts.proj.pointer = ""


### Relation: restricted_by

relations.restricted_by.fa.parent = 'other'
relations.restricted_by.fa.synset_synset = True
relations.restricted_by.fa.sense_synset = False
relations.restricted_by.fa.sense_sense = False
relations.restricted_by.fa.inOMW = True
relations.restricted_by.fa.reverse = "restricts"

relations.restricted_by.proj.plwordnet = ""
relations.restricted_by.proj.pointer = ""


### Relation: classifies

relations.classifies.fa.parent = 'other'
relations.classifies.fa.synset_synset = True
relations.classifies.fa.sense_synset = False
relations.classifies.fa.sense_sense = False
relations.classifies.fa.inOMW = True
relations.classifies.fa.reverse = "classified_by"

relations.classifies.proj.ili = "i25399"
relations.classifies.proj.plwordnet = ""
relations.classifies.proj.pointer = ""


### Relation: classified_by

relations.classified_by.fa.parent = 'other'
relations.classified_by.fa.synset_synset = True
relations.classified_by.fa.sense_synset = False
relations.classified_by.fa.sense_sense = False
relations.classified_by.fa.inOMW = True
relations.classified_by.fa.reverse = "classifies"

relations.classified_by.proj.ili = "i25002"
relations.classified_by.proj.plwordnet = ""
relations.classified_by.proj.pointer = ""


### Relation: also (no ili)

relations.also.name.symbol = '☞'

relations.also.fa.parent = 'other'
relations.also.fa.synset_synset = True
relations.also.fa.sense_synset = False
relations.also.fa.sense_sense = True
relations.also.fa.inOMW = True
relations.also.fa.reverse = 'also'

relations.also.proj.ili = "i18418"
relations.also.proj.pwn = "Also see"
relations.also.proj.querywn = "also"
relations.also.proj.eurown = "see also"
relations.also.proj.plwordnet = "dystrybutywność"
relations.also.proj.pointer = "^"



### Relation: antonym

relations.antonym.name.symbol = '⇔'

relations.antonym.fa.parent = 'constitutive'
relations.antonym.fa.synset_synset = True
relations.antonym.fa.sense_synset = False
relations.antonym.fa.sense_sense = True
relations.antonym.fa.inOMW = True
relations.antonym.fa.reverse = 'antonym'

relations.antonym.proj.ili = "i69547"
relations.antonym.proj.pwn = "antonym"
relations.antonym.proj.querywn = "antonym"
relations.antonym.proj.eurown = "antonym"
relations.antonym.proj.plwordnet = "antonim"
relations.antonym.proj.pointer = "!"


### Relation: entails

relations.entails.fa.parent = 'other'
relations.entails.fa.synset_synset = True
relations.entails.fa.sense_synset = False
relations.entails.fa.sense_sense = False
relations.entails.fa.inOMW = True
relations.entails.fa.reverse = 'is_entailed_by'

relations.entails.proj.ili = "i34846"
relations.entails.proj.pwn = "entailment"
relations.entails.proj.querywn = "enta"
relations.entails.proj.eurown = ""
relations.entails.proj.plwordnet = "holonimia podsytuacji"
relations.entails.proj.pointer = ""


### Relation: is_entailed_by

relations.is_entailed_by.fa.parent = 'other'
relations.is_entailed_by.fa.synset_synset = True
relations.is_entailed_by.fa.sense_synset = False
relations.is_entailed_by.fa.sense_sense = False
relations.is_entailed_by.fa.inOMW = True
relations.is_entailed_by.fa.reverse = 'entails'

relations.is_entailed_by.proj.pwn = ""
relations.is_entailed_by.proj.querywn = "enta"
relations.is_entailed_by.proj.eurown = ""
relations.is_entailed_by.proj.plwordnet = "meronimia podsytuacji"
relations.is_entailed_by.proj.pointer = ""


### Relation: other

relations.other.fa.parent = None
relations.other.fa.synset_synset = True
relations.other.fa.sense_synset = False
relations.other.fa.sense_sense = True
relations.other.fa.inOMW = True
relations.is_entailed_by.fa.reverse = 'also'


relations.other.proj.ili = "i11342"
relations.other.proj.pwn = "fuzzynym"
relations.other.proj.eurown = "fuzzynym"
relations.other.proj.plwordnet = "fuzzynimia"


### Relation: participle

relations.participle.fa.parent = None
relations.participle.fa.synset_synset = False
relations.participle.fa.sense_synset = False
relations.participle.fa.sense_sense = True


### Relation: pertainym

relations.pertainym.name.symbol = '⊞'

relations.pertainym.fa.parent = None
relations.pertainym.fa.synset_synset = False
relations.pertainym.fa.sense_synset = False
relations.pertainym.fa.sense_sense = True


### Relation: derivation

relations.derivation.name.symbol = '⊳'

relations.derivation.fa.parent = None
relations.derivation.fa.synset_synset = False
relations.derivation.fa.sense_synset = False
relations.derivation.fa.sense_sense = True
relations.derivation.fa.reverse = 'derivation'
