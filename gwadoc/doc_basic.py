# -*- coding: utf-8 -*-

from gwadoc import sense_rels, synset_rels


###############################################################################
### Relations Definitions


### Relation: domain

synset_rels.domain.fa.parent = None
synset_rels.domain.fa.reverse = 'has_domain'


### Relation: has_domain

synset_rels.has_domain.fa.parent = None
synset_rels.has_domain.fa.reverse = 'domain'


### Relation: constitutive

synset_rels.constitutive.fa.parent = None


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

synset_rels.hypernym.name.symbol = "⊃"

synset_rels.hypernym.fa.parent = 'constitutive'
synset_rels.hypernym.fa.inOMW = True
synset_rels.hypernym.fa.reverse = "hyponym"

synset_rels.hypernym.proj.ili = """i69569"""
synset_rels.hypernym.proj.querywn = "hype"
synset_rels.hypernym.proj.eurown = """HAS_HYPONYM"""
synset_rels.hypernym.proj.plwordnet = "hyperonymy"
synset_rels.hypernym.proj.pointer = "@"


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

synset_rels.hyponym.name.symbol = "⊂"

synset_rels.hyponym.fa.parent = 'constitutive'
synset_rels.hyponym.fa.inOMW = True
synset_rels.hyponym.fa.reverse = "hypernym"

synset_rels.hyponym.proj.ili = "i69570"
synset_rels.hyponym.proj.pwn = "hyponym"
synset_rels.hyponym.proj.querywn = "hypo"
synset_rels.hyponym.proj.eurown = "HAS_HYPERONYM"
synset_rels.hyponym.proj.plwordnet = "hyponymy"
synset_rels.hyponym.proj.pointer = "~"


### Relation: similar

synset_rels.similar.fa.parent = 'constitutive'
synset_rels.similar.fa.inOMW = True
synset_rels.similar.fa.reverse = "similar"

synset_rels.similar.proj.ili = "i13187"
synset_rels.similar.proj.pwn = "Similar to and Verb Group"
synset_rels.similar.proj.querywn = "sim"
synset_rels.similar.proj.eurown = "near_synonym"
synset_rels.similar.proj.plwordnet = "near_synonymy"
synset_rels.similar.proj.pointer = "&"


### Relation: role

synset_rels.role.fa.parent = None
synset_rels.role.fa.inOMW = True
synset_rels.role.fa.reverse = "involved"

synset_rels.role.proj.ili = "i64041"
synset_rels.role.proj.eurown = "role"
synset_rels.role.proj.plwordnet = "role_unspecified subtype and role_time"
synset_rels.role.proj.pointer = ""


### Relation: agent

synset_rels.agent.fa.parent = 'role'
synset_rels.agent.fa.inOMW = True
synset_rels.agent.fa.reverse = "involved_agent"

synset_rels.agent.proj.ili = "i69754"
synset_rels.agent.proj.eurown = "role_agent"
synset_rels.agent.proj.plwordnet = "role_agent"
synset_rels.agent.proj.pointer = ""


### Relation: patient

synset_rels.patient.fa.parent = 'role'
synset_rels.patient.fa.inOMW = True
synset_rels.patient.fa.reverse = "involved_patient"

synset_rels.patient.proj.ili = "i69753"
synset_rels.patient.proj.eurown = "role_patient"
synset_rels.patient.proj.plwordnet = "role_patient"
synset_rels.patient.proj.pointer = ""


### Relation: result

synset_rels.result.fa.parent = 'role'
synset_rels.result.fa.inOMW = True
synset_rels.result.fa.reverse = "involved_result"

synset_rels.result.proj.ili = "i69759"
synset_rels.result.proj.eurown = "role_result"
synset_rels.result.proj.plwordnet = "role_result"
synset_rels.result.proj.pointer = ""


### Relation: instrument

synset_rels.instrument.fa.parent = 'role'
synset_rels.instrument.fa.inOMW = True
synset_rels.instrument.fa.reverse = "involved_instrument"

synset_rels.instrument.proj.ili = "i69756"
synset_rels.instrument.proj.eurown = "role_instrument"
synset_rels.instrument.proj.plwordnet = "role_instrument"
synset_rels.instrument.proj.pointer = ""


### Relation: location

synset_rels.location.fa.parent = 'role'
synset_rels.location.fa.inOMW = True
synset_rels.location.fa.reverse = "involved_location"

synset_rels.location.proj.ili = "i35580"
synset_rels.location.proj.eurown = "role_location"
synset_rels.location.proj.plwordnet = "role_location"
synset_rels.location.proj.pointer = ""


### Relation: direction

synset_rels.direction.fa.parent = 'role'
synset_rels.direction.fa.inOMW = True
synset_rels.direction.fa.reverse = "involved_direction"

synset_rels.direction.proj.ili = "i82556"
synset_rels.direction.proj.eurown = "role_direction"
synset_rels.direction.proj.plwordnet = ""
synset_rels.direction.proj.pointer = ""


### Relation: target_direction

synset_rels.target_direction.fa.parent = 'role'
synset_rels.target_direction.fa.inOMW = True
synset_rels.target_direction.fa.reverse = "involved_target_direction"

synset_rels.target_direction.proj.ili = "i82007" ###(ili doesn't have target in it)
synset_rels.target_direction.proj.eurown = "role_target_direction"
synset_rels.target_direction.proj.plwordnet = ""
synset_rels.target_direction.proj.pointer = ""


### Relation: source_direction

synset_rels.source_direction.fa.parent = 'role'
synset_rels.source_direction.fa.inOMW = True
synset_rels.source_direction.fa.reverse = "involved_source_direction"

synset_rels.source_direction.proj.ili = "i81759"
synset_rels.source_direction.proj.eurown = "role_source_direction"
synset_rels.source_direction.proj.plwordnet = ""
synset_rels.source_direction.proj.pointer = ""


### Relation: involved

synset_rels.involved.fa.parent = None
synset_rels.involved.fa.inOMW = True
synset_rels.involved.fa.reverse = "role"

synset_rels.involved.proj.ili = "i8315"
synset_rels.involved.proj.eurown = "involved"
synset_rels.involved.proj.plwordnet = "unspecified subtype, time and causation inclusion"
synset_rels.involved.proj.pointer = ""


### Relation: involved_agent (EuroWordNet - page 29/30)

synset_rels.involved_agent.fa.parent = 'involved'
synset_rels.involved_agent.fa.inOMW = True
synset_rels.involved_agent.fa.reverse = "agent"

synset_rels.involved_agent.proj.eurown = "involved_agent"
synset_rels.involved_agent.proj.plwordnet = "agent inclusion"
synset_rels.involved_agent.proj.pointer = ""


### Relation: involved_patient

synset_rels.involved_patient.fa.parent = 'involved'
synset_rels.involved_patient.fa.inOMW = True
synset_rels.involved_patient.fa.reverse = "patient"

synset_rels.involved_patient.proj.eurown = "involved_patient"
synset_rels.involved_patient.proj.plwordnet = "patient inclusion"
synset_rels.involved_patient.proj.pointer = ""


### Relation: involved_result

synset_rels.involved_result.fa.parent = 'involved'
synset_rels.involved_result.fa.inOMW = True
synset_rels.involved_result.fa.reverse = "result"

synset_rels.involved_result.proj.eurown = "involved_result"
synset_rels.involved_result.proj.plwordnet = "result inclusion"
synset_rels.involved_result.proj.pointer = ""


### Relation: involved_instrument

synset_rels.involved_instrument.fa.parent = 'involved'
synset_rels.involved_instrument.fa.inOMW = True
synset_rels.involved_instrument.fa.reverse = "instrument"

synset_rels.involved_instrument.proj.eurown = "involved_instrument"
synset_rels.involved_instrument.proj.plwordnet = "instrument inclusion"
synset_rels.involved_instrument.proj.pointer = ""


### Relation: involved_location

synset_rels.involved_location.fa.parent = 'involved'
synset_rels.involved_location.fa.inOMW = True
synset_rels.involved_location.fa.reverse = "location"

synset_rels.involved_location.proj.eurown = "involved_location"
synset_rels.involved_location.proj.plwordnet = "location inclusion"
synset_rels.involved_location.proj.pointer = ""


### Relation: involved_direction

synset_rels.involved_direction.fa.parent = 'involved'
synset_rels.involved_direction.fa.inOMW = True
synset_rels.involved_direction.fa.reverse = "direction"

synset_rels.involved_direction.proj.eurown = "involved_direction"
synset_rels.involved_direction.proj.plwordnet = ""
synset_rels.involved_direction.proj.pointer = ""


### Relation: involved_target_direction

synset_rels.involved_target_direction.fa.parent = 'involved'
synset_rels.involved_target_direction.fa.inOMW = True
synset_rels.involved_target_direction.fa.reverse = "target_direction"

synset_rels.involved_target_direction.proj.eurown = "involved_target_direction"
synset_rels.involved_target_direction.proj.plwordnet = ""
synset_rels.involved_target_direction.proj.pointer = ""


### Relation: involved_source_direction

synset_rels.involved_source_direction.fa.parent = 'involved'
synset_rels.involved_source_direction.fa.inOMW = True
synset_rels.involved_source_direction.fa.reverse = "source_direction"

synset_rels.involved_source_direction.proj.eurown = "involved_source_direction"
synset_rels.involved_source_direction.proj.plwordnet = ""
synset_rels.involved_source_direction.proj.pointer = ""


### Relation: co_role EDP31

synset_rels.co_role.fa.parent = 'role'
synset_rels.co_role.fa.inOMW = True
synset_rels.co_role.fa.reverse = "co_role"

synset_rels.co_role.proj.eurown = "co_role"
synset_rels.co_role.proj.plwordnet = ""


### Relation: co_agent_patient EDP32

synset_rels.co_agent_patient.fa.parent = 'co_role'
synset_rels.co_agent_patient.fa.inOMW = True
synset_rels.co_agent_patient.fa.reverse = "co_patient_agent"

synset_rels.co_agent_patient.proj.eurown = "co_agent_patient"
synset_rels.co_agent_patient.proj.plwordnet = ""


### Relation: co_agent_instrument EDP32

synset_rels.co_agent_instrument.fa.parent = 'co_role'
synset_rels.co_agent_instrument.fa.inOMW = True
synset_rels.co_agent_instrument.fa.reverse = "co_instrument_agent"

synset_rels.co_agent_instrument.proj.eurown = "co_agent_instrument"
synset_rels.co_agent_instrument.proj.plwordnet = ""


### Relation: co_agent_result EDP32

synset_rels.co_agent_result.fa.parent = 'co_role'
synset_rels.co_agent_result.fa.inOMW = True
synset_rels.co_agent_result.fa.reverse = "co_result_agent"

synset_rels.co_agent_result.proj.eurown = "co_agent_result"
synset_rels.co_agent_result.proj.plwordnet = ""


### Relation: co_patient_agent EDP32

synset_rels.co_patient_agent.fa.parent = 'co_role'
synset_rels.co_patient_agent.fa.inOMW = True
synset_rels.co_patient_agent.fa.reverse = "co_agent_patient"

synset_rels.co_patient_agent.proj.eurown = "co_patient_agent"
synset_rels.co_patient_agent.proj.plwordnet = ""


### Relation: co_patient_instrument EDP32

synset_rels.co_patient_instrument.fa.parent = 'co_role'
synset_rels.co_patient_instrument.fa.inOMW = True
synset_rels.co_patient_instrument.fa.reverse = "co_instrument_patient"

synset_rels.co_patient_instrument.proj.eurown = "co_patient_instrument"
synset_rels.co_patient_instrument.proj.plwordnet = ""


### Relation: co_result_agent EDP32

synset_rels.co_result_agent.fa.parent = 'co_role'
synset_rels.co_result_agent.fa.inOMW = True
synset_rels.co_result_agent.fa.reverse = "co_agent_result"

synset_rels.co_result_agent.proj.eurown = "co_result_agent"
synset_rels.co_result_agent.proj.plwordnet = ""


### Relation: co_result_instrument EDP32

synset_rels.co_result_instrument.fa.parent = 'co_role'
synset_rels.co_result_instrument.fa.inOMW = True
synset_rels.co_result_instrument.fa.reverse = "co_instrument_result"

synset_rels.co_result_instrument.proj.eurown = "co_result_instrument"
synset_rels.co_result_instrument.proj.plwordnet = ""


### Relation: co_instrument_agent EDP32

synset_rels.co_instrument_agent.fa.parent = 'co_role'
synset_rels.co_instrument_agent.fa.inOMW = True
synset_rels.co_instrument_agent.fa.reverse = "co_agent_instrument"

synset_rels.co_instrument_agent.proj.eurown = "co_instrument_agent"
synset_rels.co_instrument_agent.proj.plwordnet = ""


### Relation: co_instrument_patient EDP32

synset_rels.co_instrument_patient.fa.parent = 'co_role'
synset_rels.co_instrument_patient.fa.inOMW = True
synset_rels.co_instrument_patient.fa.reverse = "co_patient_instrument"

synset_rels.co_instrument_patient.proj.eurown = "co_instrument_patient"
synset_rels.co_instrument_patient.proj.plwordnet = ""


### Relation: co_instrument_result ice saw/ice

synset_rels.co_instrument_result.fa.parent = 'co_role'
synset_rels.co_instrument_result.fa.inOMW = True
synset_rels.co_instrument_result.fa.reverse = "co_result_instrument"

synset_rels.co_instrument_result.proj.eurown = "co_instrument_result"
synset_rels.co_instrument_result.proj.plwordnet = ""


### Relation: state_of EDP37

synset_rels.state_of.fa.parent = 'other'
synset_rels.state_of.fa.inOMW = True
synset_rels.state_of.fa.reverse = "be_in_state"

synset_rels.state_of.proj.ili = "i35578"
synset_rels.state_of.proj.pwn = "attribute"
synset_rels.state_of.proj.eurown = "state_of"
synset_rels.state_of.proj.plwordnet = "state"
synset_rels.state_of.proj.pointer = ""


### Relation: be_in_state EDP37

synset_rels.be_in_state.fa.parent = 'other'
synset_rels.be_in_state.fa.inOMW = True
synset_rels.be_in_state.fa.reverse = "state_of"

synset_rels.be_in_state.proj.eurown = "be_in_state"
synset_rels.be_in_state.proj.plwordnet = "bearer of state"
synset_rels.be_in_state.proj.pointer = ""


### Relation: causes EDP34

synset_rels.causes.fa.parent = 'other'
synset_rels.causes.fa.inOMW = True
synset_rels.causes.fa.reverse = "is_caused_by"

synset_rels.causes.proj.ili = "i35561"
synset_rels.causes.proj.pwn = "cause"
synset_rels.causes.proj.querywn = "caus"
synset_rels.causes.proj.eurown = "causes"
synset_rels.causes.proj.plwordnet = "causation"
synset_rels.causes.proj.pointer = ">"


### Relation: is_caused_by EDP34

synset_rels.is_caused_by.fa.parent = 'other'
synset_rels.is_caused_by.fa.inOMW = True
synset_rels.is_caused_by.fa.reverse = "causes"

synset_rels.is_caused_by.proj.pwn = ""
synset_rels.is_caused_by.proj.querywn = "caus"
synset_rels.is_caused_by.proj.eurown = "is_caused_by"
synset_rels.is_caused_by.proj.plwordnet = ""
synset_rels.is_caused_by.proj.pointer = ""


### Relation: subevent EDP35

synset_rels.subevent.fa.parent = 'other'
synset_rels.subevent.fa.inOMW = True
synset_rels.subevent.fa.reverse = "is_subevent_of"

synset_rels.subevent.proj.querywn = "enta"
synset_rels.subevent.proj.eurown = "has_subevent"
synset_rels.subevent.proj.plwordnet = "verbal_holonymy"
synset_rels.subevent.proj.pointer = "\*"


### Relation: is_subevent_of EDP35

synset_rels.is_subevent_of.fa.parent = 'other'
synset_rels.is_subevent_of.fa.inOMW = True
synset_rels.is_subevent_of.fa.reverse = "subevent"

synset_rels.is_subevent_of.proj.querywn = "enta"
synset_rels.is_subevent_of.proj.eurown = "is_subevent_of"
synset_rels.is_subevent_of.proj.plwordnet = "verbal_meronymy"
synset_rels.is_subevent_of.proj.pointer = ""


### Relation: in_manner EDP36

synset_rels.in_manner.fa.parent = 'other'
synset_rels.in_manner.fa.inOMW = True
synset_rels.in_manner.fa.reverse = "manner_of"

synset_rels.in_manner.proj.querywn = "enta"
synset_rels.in_manner.proj.eurown = "in_manner"
synset_rels.in_manner.proj.plwordnet = ""
synset_rels.in_manner.proj.pointer = ""


### Relation: manner_of EDP36

synset_rels.manner_of.fa.parent = 'other'
synset_rels.manner_of.fa.inOMW = True
synset_rels.manner_of.fa.reverse = "in_manner"

synset_rels.manner_of.proj.ili = "i62791"
synset_rels.manner_of.proj.querywn = "enta"
synset_rels.manner_of.proj.eurown = "manner_of"
synset_rels.manner_of.proj.plwordnet = ""
synset_rels.manner_of.proj.pointer = ""


### Relation: meronym EDP26

synset_rels.meronym.fa.parent = 'constitutive'
synset_rels.meronym.fa.inOMW = True
synset_rels.meronym.fa.reverse = "holonym"

synset_rels.meronym.proj.ili = "i69575"
synset_rels.meronym.proj.pwn = "meronym"
synset_rels.meronym.proj.querywn = "enta"
synset_rels.meronym.proj.eurown = "has_meronym"
synset_rels.meronym.proj.plwordnet = "meronym"
synset_rels.meronym.proj.pointer = "%"


### Relation: holonym EDP26

synset_rels.holonym.fa.parent = 'constitutive'
synset_rels.holonym.fa.inOMW = True
synset_rels.holonym.fa.reverse = "meronym"

synset_rels.holonym.proj.ili = "i69567"
synset_rels.holonym.proj.querywn = "enta"
synset_rels.holonym.proj.eurown = "has_holonym"
synset_rels.holonym.proj.plwordnet = "holonym"
synset_rels.holonym.proj.pointer = "#"


### Relation: mero_part EDP27

synset_rels.mero_part.fa.parent = 'meronym'
synset_rels.mero_part.fa.inOMW = True
synset_rels.mero_part.fa.reverse = "holo_part"

synset_rels.mero_part.proj.pwn = "part meronym"
synset_rels.mero_part.proj.querywn = "mprt"
synset_rels.mero_part.proj.eurown = "has_mero_part"
synset_rels.mero_part.proj.plwordnet = "meronymy_part"
synset_rels.mero_part.proj.pointer = "%p"


### Relation: holo_part EDP27

synset_rels.holo_part.fa.parent = 'holonym'
synset_rels.holo_part.fa.inOMW = True
synset_rels.holo_part.fa.reverse = "mero_part"

synset_rels.holo_part.proj.pwn = "part holonym"
synset_rels.holo_part.proj.querywn = "hprt"
synset_rels.holo_part.proj.eurown = "has_holo_part"
synset_rels.holo_part.proj.plwordnet = "holonymy_part"
synset_rels.holo_part.proj.pointer = "#p"


### Relation: mero_member EPD27

synset_rels.mero_member.fa.parent = 'meronym'
synset_rels.mero_member.fa.inOMW = True
synset_rels.mero_member.fa.reverse = "holo_member"

synset_rels.mero_member.proj.pwn = "member meronym"
synset_rels.mero_member.proj.querywn = "mmem"
synset_rels.mero_member.proj.eurown = "has_mero_member"
synset_rels.mero_member.proj.plwordnet = "meronymy_member"
synset_rels.mero_member.proj.pointer = "%m"


### Relation: holo_member EDP27

synset_rels.holo_member.fa.parent = 'holonym'
synset_rels.holo_member.fa.inOMW = True
synset_rels.holo_member.fa.reverse = "mero_member"

synset_rels.holo_member.proj.pwn = "member holonym"
synset_rels.holo_member.proj.querywn = "hmem"
synset_rels.holo_member.proj.eurown = "has_holo_member"
synset_rels.holo_member.proj.plwordnet = "holonymy_member"
synset_rels.holo_member.proj.pointer = "#m"


### Relation: mero_substance EDP28

synset_rels.mero_substance.fa.parent = 'meronym'
synset_rels.mero_substance.fa.inOMW = True
synset_rels.mero_substance.fa.reverse = "holo_substance"

synset_rels.mero_substance.proj.pwn = "substance meronym"
synset_rels.mero_substance.proj.querywn = "msub"
synset_rels.mero_substance.proj.eurown = "has_mero_madeof"
synset_rels.mero_substance.proj.plwordnet = "meronymy_substance"
synset_rels.mero_substance.proj.pointer = "%s"


### Relation: holo_substance EDP28

synset_rels.holo_substance.fa.parent = 'holonym'
synset_rels.holo_substance.fa.inOMW = True
synset_rels.holo_substance.fa.reverse = "mero_substance"

synset_rels.holo_substance.proj.pwn = "substance holonym"
synset_rels.holo_substance.proj.querywn = "hsub"
synset_rels.holo_substance.proj.eurown = "has_holo_madeof"
synset_rels.holo_substance.proj.plwordnet = "holonymy_substance"
synset_rels.holo_substance.proj.pointer = "#s"


### Relation: mero_location EDP28

synset_rels.mero_location.fa.parent = 'meronym'
synset_rels.mero_location.fa.inOMW = True
synset_rels.mero_location.fa.reverse = "holo_location"

synset_rels.mero_location.proj.querywn = "hsub"
synset_rels.mero_location.proj.eurown = "has_mero_location"
synset_rels.mero_location.proj.plwordnet = "meronymy_location"


### Relation: holo_location EDP28

synset_rels.holo_location.fa.parent = 'holonym'
synset_rels.holo_location.fa.inOMW = True
synset_rels.holo_location.fa.reverse = "mero_location"

synset_rels.holo_location.proj.querywn = "hsub"
synset_rels.holo_location.proj.eurown = "has_holo_location"
synset_rels.holo_location.proj.plwordnet = "holonymy_location"


### Relation: mero_portion EDP27

synset_rels.mero_portion.fa.parent = 'meronym'
synset_rels.mero_portion.fa.inOMW = True
synset_rels.mero_portion.fa.reverse = "holo_portion"

synset_rels.mero_portion.proj.pwn = "portion meronym"
synset_rels.mero_portion.proj.querywn = "hsub"
synset_rels.mero_portion.proj.eurown = "has_mero_portion"
synset_rels.mero_portion.proj.plwordnet = "meronymy_portion"
synset_rels.mero_portion.proj.pointer = ""


### Relation: holo_portion EDP27

synset_rels.holo_portion.fa.parent = 'holonym'
synset_rels.holo_portion.fa.inOMW = True
synset_rels.holo_portion.fa.reverse = "mero_portion"

synset_rels.holo_portion.proj.querywn = "hsub"
synset_rels.holo_portion.proj.eurown = "has_holo_portion"
synset_rels.holo_portion.proj.plwordnet = "holonymy_portion"
synset_rels.holo_portion.proj.pointer = ""


### Relation: eq_synonym

synset_rels.eq_synonym.fa.parent = 'constitutive'
synset_rels.eq_synonym.fa.inOMW = True
synset_rels.eq_synonym.fa.reverse = "eq_synonym"

synset_rels.eq_synonym.proj.ili = "i69607"
synset_rels.eq_synonym.proj.eurown = "eq_synonym"
synset_rels.eq_synonym.proj.plwordnet = ""


### Relation: instance_hypernym

synset_rels.instance_hypernym.fa.parent = 'constitutive'
synset_rels.instance_hypernym.fa.inOMW = True
synset_rels.instance_hypernym.fa.reverse = "instance_hyponym"

synset_rels.instance_hypernym.proj.pwn = "Instance Hypernym"
synset_rels.instance_hypernym.proj.querywn = "inst"
synset_rels.instance_hypernym.proj.eurown = "HAS_INSTANCE"
synset_rels.instance_hypernym.proj.plwordnet = "type"
synset_rels.instance_hypernym.proj.pointer = "@i"


### Relation: instance_hyponym

synset_rels.instance_hyponym.fa.parent = 'constitutive'
synset_rels.instance_hyponym.fa.inOMW = True
synset_rels.instance_hyponym.fa.reverse = "instance_hypernym"

synset_rels.instance_hyponym.proj.ili = "i75102"
synset_rels.instance_hyponym.proj.pwn = "Instance Hypernym"
synset_rels.instance_hyponym.proj.querywn = "hasi"
synset_rels.instance_hyponym.proj.eurown = "BELONGS_To_CLASS"
synset_rels.instance_hyponym.proj.plwordnet = "instance"
synset_rels.instance_hyponym.proj.pointer = "~i"


### Relation: exemplifies

synset_rels.exemplifies.fa.parent = 'domain'
synset_rels.exemplifies.fa.inOMW = True
synset_rels.exemplifies.fa.reverse = "is_exemplified_by"

synset_rels.exemplifies.proj.ili = "i26682"
synset_rels.exemplifies.proj.pwn = "Domain of synset - USAGE"
synset_rels.exemplifies.proj.querywn = "dmnu"
synset_rels.exemplifies.proj.plwordnet = ""
synset_rels.exemplifies.proj.pointer = ";u"


### Relation: is_exemplified_by

synset_rels.is_exemplified_by.fa.parent = 'has_domain'
synset_rels.is_exemplified_by.fa.inOMW = True
synset_rels.is_exemplified_by.fa.reverse = "exemplifies"

synset_rels.is_exemplified_by.proj.pwn = "domain term usage"
synset_rels.is_exemplified_by.proj.querywn = "dmtu"
synset_rels.is_exemplified_by.proj.plwordnet = ""
synset_rels.is_exemplified_by.proj.pointer = "-u"


### Relation: domain_topic

synset_rels.domain_topic.fa.parent = 'domain'
synset_rels.domain_topic.fa.inOMW = True
synset_rels.domain_topic.fa.reverse = "has_domain_topic"

synset_rels.domain_topic.proj.pwn = "domain category"
synset_rels.domain_topic.proj.querywn = "Domain of synset - TOPIC"
synset_rels.domain_topic.proj.plwordnet = ""
synset_rels.domain_topic.proj.pointer = ";c"


### Relation: has_domain_topic

synset_rels.has_domain_topic.fa.parent = 'has_domain'
synset_rels.has_domain_topic.fa.inOMW = True
synset_rels.has_domain_topic.fa.reverse = "domain_topic"

synset_rels.has_domain_topic.proj.querywn = "dmtc"
synset_rels.has_domain_topic.proj.plwordnet = ""
synset_rels.has_domain_topic.proj.pointer = "-c"


### Relation: domain_region

synset_rels.domain_region.fa.parent = 'domain'
synset_rels.domain_region.fa.inOMW = True
synset_rels.domain_region.fa.reverse = "has_domain_region"

synset_rels.domain_region.proj.pwn = "Domain of synset - REGION"
synset_rels.domain_region.proj.querywn = "dmnr"
synset_rels.domain_region.proj.plwordnet = ""
synset_rels.domain_region.proj.pointer = ";r"


### Relation: has_domain_region

synset_rels.has_domain_region.fa.parent = 'has_domain'
synset_rels.has_domain_region.fa.inOMW = True
synset_rels.has_domain_region.fa.reverse = "domain_region"

synset_rels.has_domain_region.proj.querywn = "dmtr"
synset_rels.has_domain_region.proj.plwordnet = ""
synset_rels.has_domain_region.proj.pointer = "-r"


### Relation: attribute

synset_rels.attribute.fa.parent = 'other'
synset_rels.attribute.fa.inOMW = True
synset_rels.attribute.fa.reverse = "attribute"

synset_rels.attribute.proj.ili = "i35577"
synset_rels.attribute.proj.pwn = "attribute"
synset_rels.attribute.proj.querywn = "attr"
synset_rels.attribute.proj.plwordnet = "value_of_the_attribute"
synset_rels.attribute.proj.pointer = "="


### Relation: restricts

synset_rels.restricts.fa.parent = 'other'
synset_rels.restricts.fa.inOMW = True
synset_rels.restricts.fa.reverse = "restricted_by"

synset_rels.restricts.proj.ili = "i22888"
synset_rels.restricts.proj.plwordnet = ""
synset_rels.restricts.proj.pointer = ""


### Relation: restricted_by

synset_rels.restricted_by.fa.parent = 'other'
synset_rels.restricted_by.fa.inOMW = True
synset_rels.restricted_by.fa.reverse = "restricts"

synset_rels.restricted_by.proj.plwordnet = ""
synset_rels.restricted_by.proj.pointer = ""


### Relation: classifies

synset_rels.classifies.fa.parent = 'other'
synset_rels.classifies.fa.inOMW = True
synset_rels.classifies.fa.reverse = "classified_by"

synset_rels.classifies.proj.ili = "i25399"
synset_rels.classifies.proj.plwordnet = ""
synset_rels.classifies.proj.pointer = ""


### Relation: classified_by

synset_rels.classified_by.fa.parent = 'other'
synset_rels.classified_by.fa.inOMW = True
synset_rels.classified_by.fa.reverse = "classifies"

synset_rels.classified_by.proj.ili = "i25002"
synset_rels.classified_by.proj.plwordnet = ""
synset_rels.classified_by.proj.pointer = ""


### Relation: also (no ili)

synset_rels.also.fa.parent = 'other'
synset_rels.also.fa.inOMW = True
synset_rels.also.fa.reverse = 'also'

synset_rels.also.proj.pwn = "also see"
synset_rels.also.proj.querywn = "also"
synset_rels.also.proj.eurown = ""
synset_rels.also.proj.plwordnet = "inchoativity, iterativity, distributivity, anteriority"
synset_rels.also.proj.pointer = "^"


### Relation: antonym

synset_rels.antonym.fa.parent = 'constitutive'
synset_rels.antonym.fa.inOMW = True
synset_rels.antonym.fa.reverse = 'antonym'

synset_rels.antonym.proj.ili = "i69547"
synset_rels.antonym.proj.pwn = ""
synset_rels.antonym.proj.querywn = "antonym"
synset_rels.antonym.proj.eurown = ""
synset_rels.antonym.proj.plwordnet = "complementary, proper and converse antonymy"
synset_rels.antonym.proj.pointer = "!"


### Relation: entails

synset_rels.entails.fa.parent = 'other'
synset_rels.entails.fa.inOMW = True
synset_rels.entails.fa.reverse = 'is_entailed_by'

synset_rels.entails.proj.ili = "i34846"
synset_rels.entails.proj.pwn = "entailment"
synset_rels.entails.proj.querywn = "participle"
synset_rels.entails.proj.eurown = ""
synset_rels.entails.proj.plwordnet = ""
synset_rels.entails.proj.pointer = ""


### Relation: is_entailed_by

synset_rels.is_entailed_by.fa.parent = 'other'
synset_rels.is_entailed_by.fa.inOMW = True
synset_rels.is_entailed_by.fa.reverse = 'entails'

synset_rels.is_entailed_by.proj.pwn = ""
synset_rels.is_entailed_by.proj.querywn = "participle"
synset_rels.is_entailed_by.proj.eurown = ""
synset_rels.is_entailed_by.proj.plwordnet = ""
synset_rels.is_entailed_by.proj.pointer = ""


### Relation: other

synset_rels.other.fa.parent = None
synset_rels.other.fa.inOMW = True

synset_rels.other.proj.ili = "i11342"
