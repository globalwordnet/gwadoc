# -*- coding: utf-8 -*-

from gwadoc.base import rels


###############################################################################
### Relations Definitions


### Relation: domain

rels.domain.form.parent = None
rels.domain.form.reverse = 'has_domain'


### Relation: has_domain

rels.has_domain.form.parent = None
rels.has_domain.form.reverse = 'domain'


### Relation: constitutive

rels.constitutive.form.parent = None


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

rels.hypernym.name.symbol = "⊃"

rels.hypernym.form.parent = 'constitutive'
rels.hypernym.form.inOMW = True
rels.hypernym.form.reverse = "hyponym"

rels.hypernym.proj.ili = """i69569"""
rels.hypernym.proj.querywn = "hype"
rels.hypernym.proj.eurown = """HAS_HYPONYM"""
rels.hypernym.proj.plwordnet = "hyperonymy"
rels.hypernym.proj.pointer = "@"


### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

rels.hyponym.name.symbol = "⊂"

rels.hyponym.form.parent = 'constitutive'
rels.hyponym.form.inOMW = True
rels.hyponym.form.reverse = "hypernym"

rels.hyponym.proj.ili = "i69570"
rels.hyponym.proj.pwn = "hyponym"
rels.hyponym.proj.querywn = "hypo"
rels.hyponym.proj.eurown = "HAS_HYPERONYM"
rels.hyponym.proj.plwordnet = "hyponymy"
rels.hyponym.proj.pointer = "~"


### Relation: similar

rels.similar.form.parent = 'constitutive'
rels.similar.form.inOMW = True
rels.similar.form.reverse = "similar"

rels.similar.proj.ili = "i13187"
rels.similar.proj.pwn = "Similar to and Verb Group"
rels.similar.proj.querywn = "sim"
rels.similar.proj.eurown = "near_synonym"
rels.similar.proj.plwordnet = "near_synonymy"
rels.similar.proj.pointer = "&"


### Relation: role

rels.role.form.parent = None
rels.role.form.inOMW = True
rels.role.form.reverse = "involved"

rels.role.proj.ili = "i64041"
rels.role.proj.eurown = "role"
rels.role.proj.plwordnet = "role_unspecified subtype and role_time"
rels.role.proj.pointer = ""


### Relation: agent

rels.agent.form.parent = 'role'
rels.agent.form.inOMW = True
rels.agent.form.reverse = "involved_agent"

rels.agent.proj.ili = "i69754"
rels.agent.proj.eurown = "role_agent"
rels.agent.proj.plwordnet = "role_agent"
rels.agent.proj.pointer = ""


### Relation: patient

rels.patient.form.parent = 'role'
rels.patient.form.inOMW = True
rels.patient.form.reverse = "involved_patient"

rels.patient.proj.ili = "i69753"
rels.patient.proj.eurown = "role_patient"
rels.patient.proj.plwordnet = "role_patient"
rels.patient.proj.pointer = ""


### Relation: result

rels.result.form.parent = 'role'
rels.result.form.inOMW = True
rels.result.form.reverse = "involved_result"

rels.result.proj.ili = "i69759"
rels.result.proj.eurown = "role_result"
rels.result.proj.plwordnet = "role_result"
rels.result.proj.pointer = ""


### Relation: instrument

rels.instrument.form.parent = 'role'
rels.instrument.form.inOMW = True
rels.instrument.form.reverse = "involved_instrument"

rels.instrument.proj.ili = "i69756"
rels.instrument.proj.eurown = "role_instrument"
rels.instrument.proj.plwordnet = "role_instrument"
rels.instrument.proj.pointer = ""


### Relation: location

rels.location.form.parent = 'role'
rels.location.form.inOMW = True
rels.location.form.reverse = "involved_location"

rels.location.proj.ili = "i35580"
rels.location.proj.eurown = "role_location"
rels.location.proj.plwordnet = "role_location"
rels.location.proj.pointer = ""


### Relation: direction

rels.direction.form.parent = 'role'
rels.direction.form.inOMW = True
rels.direction.form.reverse = "involved_direction"

rels.direction.proj.ili = "i82556"
rels.direction.proj.eurown = "role_direction"
rels.direction.proj.plwordnet = ""
rels.direction.proj.pointer = ""


### Relation: target_direction

rels.target_direction.form.parent = 'role'
rels.target_direction.form.inOMW = True
rels.target_direction.form.reverse = "involved_target_direction"

rels.target_direction.proj.ili = "i82007" ###(ili doesn't have target in it)
rels.target_direction.proj.eurown = "role_target_direction"
rels.target_direction.proj.plwordnet = ""
rels.target_direction.proj.pointer = ""


### Relation: source_direction

rels.source_direction.form.parent = 'role'
rels.source_direction.form.inOMW = True
rels.source_direction.form.reverse = "involved_source_direction"

rels.source_direction.proj.ili = "i81759"
rels.source_direction.proj.eurown = "role_source_direction"
rels.source_direction.proj.plwordnet = ""
rels.source_direction.proj.pointer = ""


### Relation: involved

rels.involved.form.parent = None
rels.involved.form.inOMW = True
rels.involved.form.reverse = "role"

rels.involved.proj.ili = "i8315"
rels.involved.proj.eurown = "involved"
rels.involved.proj.plwordnet = "unspecified subtype, time and causation inclusion"
rels.involved.proj.pointer = ""


### Relation: involved_agent (EuroWordNet - page 29/30)

rels.involved_agent.form.parent = 'involved'
rels.involved_agent.form.inOMW = True
rels.involved_agent.form.reverse = "agent"

rels.involved_agent.proj.eurown = "involved_agent"
rels.involved_agent.proj.plwordnet = "agent inclusion"
rels.involved_agent.proj.pointer = ""


### Relation: involved_patient

rels.involved_patient.form.parent = 'involved'
rels.involved_patient.form.inOMW = True
rels.involved_patient.form.reverse = "patient"

rels.involved_patient.proj.eurown = "involved_patient"
rels.involved_patient.proj.plwordnet = "patient inclusion"
rels.involved_patient.proj.pointer = ""


### Relation: involved_result

rels.involved_result.form.parent = 'involved'
rels.involved_result.form.inOMW = True
rels.involved_result.form.reverse = "result"

rels.involved_result.proj.eurown = "involved_result"
rels.involved_result.proj.plwordnet = "result inclusion"
rels.involved_result.proj.pointer = ""


### Relation: involved_instrument

rels.involved_instrument.form.parent = 'involved'
rels.involved_instrument.form.inOMW = True
rels.involved_instrument.form.reverse = "instrument"

rels.involved_instrument.proj.eurown = "involved_instrument"
rels.involved_instrument.proj.plwordnet = "instrument inclusion"
rels.involved_instrument.proj.pointer = ""


### Relation: involved_location

rels.involved_location.form.parent = 'involved'
rels.involved_location.form.inOMW = True
rels.involved_location.form.reverse = "location"

rels.involved_location.proj.eurown = "involved_location"
rels.involved_location.proj.plwordnet = "location inclusion"
rels.involved_location.proj.pointer = ""


### Relation: involved_direction

rels.involved_direction.form.parent = 'involved'
rels.involved_direction.form.inOMW = True
rels.involved_direction.form.reverse = "direction"

rels.involved_direction.proj.eurown = "involved_direction"
rels.involved_direction.proj.plwordnet = ""
rels.involved_direction.proj.pointer = ""


### Relation: involved_target_direction

rels.involved_target_direction.form.parent = 'involved'
rels.involved_target_direction.form.inOMW = True
rels.involved_target_direction.form.reverse = "target_direction"

rels.involved_target_direction.proj.eurown = "involved_target_direction"
rels.involved_target_direction.proj.plwordnet = ""
rels.involved_target_direction.proj.pointer = ""


### Relation: involved_source_direction

rels.involved_source_direction.form.parent = 'involved'
rels.involved_source_direction.form.inOMW = True
rels.involved_source_direction.form.reverse = "source_direction"

rels.involved_source_direction.proj.eurown = "involved_source_direction"
rels.involved_source_direction.proj.plwordnet = ""
rels.involved_source_direction.proj.pointer = ""


### Relation: co_role EDP31

rels.co_role.form.parent = 'role'
rels.co_role.form.inOMW = True
rels.co_role.form.reverse = "co_role"

rels.co_role.proj.eurown = "co_role"
rels.co_role.proj.plwordnet = ""


### Relation: co_agent_patient EDP32

rels.co_agent_patient.form.parent = 'co_role'
rels.co_agent_patient.form.inOMW = True
rels.co_agent_patient.form.reverse = "co_patient_agent"

rels.co_agent_patient.proj.eurown = "co_agent_patient"
rels.co_agent_patient.proj.plwordnet = ""


### Relation: co_agent_instrument EDP32

rels.co_agent_instrument.form.parent = 'co_role'
rels.co_agent_instrument.form.inOMW = True
rels.co_agent_instrument.form.reverse = "co_instrument_agent"

rels.co_agent_instrument.proj.eurown = "co_agent_instrument"
rels.co_agent_instrument.proj.plwordnet = ""


### Relation: co_agent_result EDP32

rels.co_agent_result.form.parent = 'co_role'
rels.co_agent_result.form.inOMW = True
rels.co_agent_result.form.reverse = "co_result_agent"

rels.co_agent_result.proj.eurown = "co_agent_result"
rels.co_agent_result.proj.plwordnet = ""


### Relation: co_patient_agent EDP32

rels.co_patient_agent.form.parent = 'co_role'
rels.co_patient_agent.form.inOMW = True
rels.co_patient_agent.form.reverse = "co_agent_patient"

rels.co_patient_agent.proj.eurown = "co_patient_agent"
rels.co_patient_agent.proj.plwordnet = ""


### Relation: co_patient_instrument EDP32

rels.co_patient_instrument.form.parent = 'co_role'
rels.co_patient_instrument.form.inOMW = True
rels.co_patient_instrument.form.reverse = "co_instrument_patient"

rels.co_patient_instrument.proj.eurown = "co_patient_instrument"
rels.co_patient_instrument.proj.plwordnet = ""


### Relation: co_result_agent EDP32

rels.co_result_agent.form.parent = 'co_role'
rels.co_result_agent.form.inOMW = True
rels.co_result_agent.form.reverse = "co_agent_result"

rels.co_result_agent.proj.eurown = "co_result_agent"
rels.co_result_agent.proj.plwordnet = ""


### Relation: co_result_instrument EDP32

rels.co_result_instrument.form.parent = 'co_role'
rels.co_result_instrument.form.inOMW = True
rels.co_result_instrument.form.reverse = "co_instrument_result"

rels.co_result_instrument.proj.eurown = "co_result_instrument"
rels.co_result_instrument.proj.plwordnet = ""


### Relation: co_instrument_agent EDP32

rels.co_instrument_agent.form.parent = 'co_role'
rels.co_instrument_agent.form.inOMW = True
rels.co_instrument_agent.form.reverse = "co_agent_instrument"

rels.co_instrument_agent.proj.eurown = "co_instrument_agent"
rels.co_instrument_agent.proj.plwordnet = ""


### Relation: co_instrument_patient EDP32

rels.co_instrument_patient.form.parent = 'co_role'
rels.co_instrument_patient.form.inOMW = True
rels.co_instrument_patient.form.reverse = "co_patient_instrument"

rels.co_instrument_patient.proj.eurown = "co_instrument_patient"
rels.co_instrument_patient.proj.plwordnet = ""


### Relation: co_instrument_result ice saw/ice

rels.co_instrument_result.form.parent = 'co_role'
rels.co_instrument_result.form.inOMW = True
rels.co_instrument_result.form.reverse = "co_result_instrument"

rels.co_instrument_result.proj.eurown = "co_instrument_result"
rels.co_instrument_result.proj.plwordnet = ""


### Relation: state_of EDP37

rels.state_of.form.parent = 'other'
rels.state_of.form.inOMW = True
rels.state_of.form.reverse = "be_in_state"

rels.state_of.proj.ili = "i35578"
rels.state_of.proj.pwn = "attribute"
rels.state_of.proj.eurown = "state_of"
rels.state_of.proj.plwordnet = "state"
rels.state_of.proj.pointer = ""


### Relation: be_in_state EDP37

rels.be_in_state.form.parent = 'other'
rels.be_in_state.form.inOMW = True
rels.be_in_state.form.reverse = "state_of"

rels.be_in_state.proj.eurown = "be_in_state"
rels.be_in_state.proj.plwordnet = "bearer of state"
rels.be_in_state.proj.pointer = ""


### Relation: causes EDP34

rels.causes.form.parent = 'other'
rels.causes.form.inOMW = True
rels.causes.form.reverse = "is_caused_by"

rels.causes.proj.ili = "i35561"
rels.causes.proj.pwn = "cause"
rels.causes.proj.querywn = "caus"
rels.causes.proj.eurown = "causes"
rels.causes.proj.plwordnet = "causation"
rels.causes.proj.pointer = ">"


### Relation: is_caused_by EDP34

rels.is_caused_by.form.parent = 'other'
rels.is_caused_by.form.inOMW = True
rels.is_caused_by.form.reverse = "causes"

rels.is_caused_by.proj.pwn = ""
rels.is_caused_by.proj.querywn = "caus"
rels.is_caused_by.proj.eurown = "is_caused_by"
rels.is_caused_by.proj.plwordnet = ""
rels.is_caused_by.proj.pointer = ""


### Relation: subevent EDP35

rels.subevent.form.parent = 'other'
rels.subevent.form.inOMW = True
rels.subevent.form.reverse = "is_subevent_of"

rels.subevent.proj.querywn = "enta"
rels.subevent.proj.eurown = "has_subevent"
rels.subevent.proj.plwordnet = "verbal_holonymy"
rels.subevent.proj.pointer = "\*"


### Relation: is_subevent_of EDP35

rels.is_subevent_of.form.parent = 'other'
rels.is_subevent_of.form.inOMW = True
rels.is_subevent_of.form.reverse = "subevent"

rels.is_subevent_of.proj.querywn = "enta"
rels.is_subevent_of.proj.eurown = "is_subevent_of"
rels.is_subevent_of.proj.plwordnet = "verbal_meronymy"
rels.is_subevent_of.proj.pointer = ""


### Relation: in_manner EDP36

rels.in_manner.form.parent = 'other'
rels.in_manner.form.inOMW = True
rels.in_manner.form.reverse = "manner_of"

rels.in_manner.proj.querywn = "enta"
rels.in_manner.proj.eurown = "in_manner"
rels.in_manner.proj.plwordnet = ""
rels.in_manner.proj.pointer = ""


### Relation: manner_of EDP36

rels.manner_of.form.parent = 'other'
rels.manner_of.form.inOMW = True
rels.manner_of.form.reverse = "in_manner"

rels.manner_of.proj.ili = "i62791"
rels.manner_of.proj.querywn = "enta"
rels.manner_of.proj.eurown = "manner_of"
rels.manner_of.proj.plwordnet = ""
rels.manner_of.proj.pointer = ""


### Relation: meronym EDP26

rels.meronym.form.parent = 'constitutive'
rels.meronym.form.inOMW = True
rels.meronym.form.reverse = "holonym"

rels.meronym.proj.ili = "i69575"
rels.meronym.proj.pwn = "meronym"
rels.meronym.proj.querywn = "enta"
rels.meronym.proj.eurown = "has_meronym"
rels.meronym.proj.plwordnet = "meronym"
rels.meronym.proj.pointer = "%"


### Relation: holonym EDP26

rels.holonym.form.parent = 'constitutive'
rels.holonym.form.inOMW = True
rels.holonym.form.reverse = "meronym"

rels.holonym.proj.ili = "i69567"
rels.holonym.proj.querywn = "enta"
rels.holonym.proj.eurown = "has_holonym"
rels.holonym.proj.plwordnet = "holonym"
rels.holonym.proj.pointer = "#"


### Relation: mero_part EDP27

rels.mero_part.form.parent = 'meronym'
rels.mero_part.form.inOMW = True
rels.mero_part.form.reverse = "holo_part"

rels.mero_part.proj.pwn = "part meronym"
rels.mero_part.proj.querywn = "mprt"
rels.mero_part.proj.eurown = "has_mero_part"
rels.mero_part.proj.plwordnet = "meronymy_part"
rels.mero_part.proj.pointer = "%p"


### Relation: holo_part EDP27

rels.holo_part.form.parent = 'holonym'
rels.holo_part.form.inOMW = True
rels.holo_part.form.reverse = "mero_part"

rels.holo_part.proj.pwn = "part holonym"
rels.holo_part.proj.querywn = "hprt"
rels.holo_part.proj.eurown = "has_holo_part"
rels.holo_part.proj.plwordnet = "holonymy_part"
rels.holo_part.proj.pointer = "#p"


### Relation: mero_member EPD27

rels.mero_member.form.parent = 'meronym'
rels.mero_member.form.inOMW = True
rels.mero_member.form.reverse = "holo_member"

rels.mero_member.proj.pwn = "member meronym"
rels.mero_member.proj.querywn = "mmem"
rels.mero_member.proj.eurown = "has_mero_member"
rels.mero_member.proj.plwordnet = "meronymy_member"
rels.mero_member.proj.pointer = "%m"


### Relation: holo_member EDP27

rels.holo_member.form.parent = 'holonym'
rels.holo_member.form.inOMW = True
rels.holo_member.form.reverse = "mero_member"

rels.holo_member.proj.pwn = "member holonym"
rels.holo_member.proj.querywn = "hmem"
rels.holo_member.proj.eurown = "has_holo_member"
rels.holo_member.proj.plwordnet = "holonymy_member"
rels.holo_member.proj.pointer = "#m"


### Relation: mero_substance EDP28

rels.mero_substance.form.parent = 'meronym'
rels.mero_substance.form.inOMW = True
rels.mero_substance.form.reverse = "holo_substance"

rels.mero_substance.proj.pwn = "substance meronym"
rels.mero_substance.proj.querywn = "msub"
rels.mero_substance.proj.eurown = "has_mero_madeof"
rels.mero_substance.proj.plwordnet = "meronymy_substance"
rels.mero_substance.proj.pointer = "%s"


### Relation: holo_substance EDP28

rels.holo_substance.form.parent = 'holonym'
rels.holo_substance.form.inOMW = True
rels.holo_substance.form.reverse = "mero_substance"

rels.holo_substance.proj.pwn = "substance holonym"
rels.holo_substance.proj.querywn = "hsub"
rels.holo_substance.proj.eurown = "has_holo_madeof"
rels.holo_substance.proj.plwordnet = "holonymy_substance"
rels.holo_substance.proj.pointer = "#s"


### Relation: mero_location EDP28

rels.mero_location.form.parent = 'meronym'
rels.mero_location.form.inOMW = True
rels.mero_location.form.reverse = "holo_location"

rels.mero_location.proj.querywn = "hsub"
rels.mero_location.proj.eurown = "has_mero_location"
rels.mero_location.proj.plwordnet = "meronymy_location"


### Relation: holo_location EDP28

rels.holo_location.form.parent = 'holonym'
rels.holo_location.form.inOMW = True
rels.holo_location.form.reverse = "mero_location"

rels.holo_location.proj.querywn = "hsub"
rels.holo_location.proj.eurown = "has_holo_location"
rels.holo_location.proj.plwordnet = "holonymy_location"


### Relation: mero_portion EDP27

rels.mero_portion.form.parent = 'meronym'
rels.mero_portion.form.inOMW = True
rels.mero_portion.form.reverse = "holo_portion"

rels.mero_portion.proj.pwn = "portion meronym"
rels.mero_portion.proj.querywn = "hsub"
rels.mero_portion.proj.eurown = "has_mero_portion"
rels.mero_portion.proj.plwordnet = "meronymy_portion"
rels.mero_portion.proj.pointer = ""


### Relation: holo_portion EDP27

rels.holo_portion.form.parent = 'holonym'
rels.holo_portion.form.inOMW = True
rels.holo_portion.form.reverse = "mero_portion"

rels.holo_portion.proj.querywn = "hsub"
rels.holo_portion.proj.eurown = "has_holo_portion"
rels.holo_portion.proj.plwordnet = "holonymy_portion"
rels.holo_portion.proj.pointer = ""


### Relation: eq_synonym

rels.eq_synonym.form.parent = 'constitutive'
rels.eq_synonym.form.inOMW = True
rels.eq_synonym.form.reverse = "eq_synonym"

rels.eq_synonym.proj.ili = "i69607"
rels.eq_synonym.proj.eurown = "eq_synonym"
rels.eq_synonym.proj.plwordnet = ""


### Relation: instance_hypernym

rels.instance_hypernym.form.parent = 'constitutive'
rels.instance_hypernym.form.inOMW = True
rels.instance_hypernym.form.reverse = "instance_hyponym"

rels.instance_hypernym.proj.pwn = "Instance Hypernym"
rels.instance_hypernym.proj.querywn = "inst"
rels.instance_hypernym.proj.eurown = "HAS_INSTANCE"
rels.instance_hypernym.proj.plwordnet = "type"
rels.instance_hypernym.proj.pointer = "@i"


### Relation: instance_hyponym

rels.instance_hyponym.form.parent = 'constitutive'
rels.instance_hyponym.form.inOMW = True
rels.instance_hyponym.form.reverse = "instance_hypernym"

rels.instance_hyponym.proj.ili = "i75102"
rels.instance_hyponym.proj.pwn = "Instance Hypernym"
rels.instance_hyponym.proj.querywn = "hasi"
rels.instance_hyponym.proj.eurown = "BELONGS_To_CLASS"
rels.instance_hyponym.proj.plwordnet = "instance"
rels.instance_hyponym.proj.pointer = "~i"


### Relation: exemplifies

rels.exemplifies.form.parent = 'domain'
rels.exemplifies.form.inOMW = True
rels.exemplifies.form.reverse = "is_exemplified_by"

rels.exemplifies.proj.ili = "i26682"
rels.exemplifies.proj.pwn = "Domain of synset - USAGE"
rels.exemplifies.proj.querywn = "dmnu"
rels.exemplifies.proj.plwordnet = ""
rels.exemplifies.proj.pointer = ";u"


### Relation: is_exemplified_by

rels.is_exemplified_by.form.parent = 'has_domain'
rels.is_exemplified_by.form.inOMW = True
rels.is_exemplified_by.form.reverse = "exemplifies"

rels.is_exemplified_by.proj.pwn = "domain term usage"
rels.is_exemplified_by.proj.querywn = "dmtu"
rels.is_exemplified_by.proj.plwordnet = ""
rels.is_exemplified_by.proj.pointer = "-u"


### Relation: domain_topic

rels.domain_topic.form.parent = 'domain'
rels.domain_topic.form.inOMW = True
rels.domain_topic.form.reverse = "has_domain_topic"

rels.domain_topic.proj.pwn = "domain category"
rels.domain_topic.proj.querywn = "Domain of synset - TOPIC"
rels.domain_topic.proj.plwordnet = ""
rels.domain_topic.proj.pointer = ";c"


### Relation: has_domain_topic

rels.has_domain_topic.form.parent = 'has_domain'
rels.has_domain_topic.form.inOMW = True
rels.has_domain_topic.form.reverse = "domain_topic"

rels.has_domain_topic.proj.querywn = "dmtc"
rels.has_domain_topic.proj.plwordnet = ""
rels.has_domain_topic.proj.pointer = "-c"


### Relation: domain_region

rels.domain_region.form.parent = 'domain'
rels.domain_region.form.inOMW = True
rels.domain_region.form.reverse = "has_domain_region"

rels.domain_region.proj.pwn = "Domain of synset - REGION"
rels.domain_region.proj.querywn = "dmnr"
rels.domain_region.proj.plwordnet = ""
rels.domain_region.proj.pointer = ";r"


### Relation: has_domain_region

rels.has_domain_region.form.parent = 'has_domain'
rels.has_domain_region.form.inOMW = True
rels.has_domain_region.form.reverse = "domain_region"

rels.has_domain_region.proj.querywn = "dmtr"
rels.has_domain_region.proj.plwordnet = ""
rels.has_domain_region.proj.pointer = "-r"


### Relation: attribute

rels.attribute.form.parent = 'other'
rels.attribute.form.inOMW = True
rels.attribute.form.reverse = "attribute"

rels.attribute.proj.ili = "i35577"
rels.attribute.proj.pwn = "attribute"
rels.attribute.proj.querywn = "attr"
rels.attribute.proj.plwordnet = "value_of_the_attribute"
rels.attribute.proj.pointer = "="


### Relation: restricts

rels.restricts.form.parent = 'other'
rels.restricts.form.inOMW = True
rels.restricts.form.reverse = "restricted_by"

rels.restricts.proj.ili = "i22888"
rels.restricts.proj.plwordnet = ""
rels.restricts.proj.pointer = ""


### Relation: restricted_by

rels.restricted_by.form.parent = 'other'
rels.restricted_by.form.inOMW = True
rels.restricted_by.form.reverse = "restricts"

rels.restricted_by.proj.plwordnet = ""
rels.restricted_by.proj.pointer = ""


### Relation: classifies

rels.classifies.form.parent = 'other'
rels.classifies.form.inOMW = True
rels.classifies.form.reverse = "classified_by"

rels.classifies.proj.ili = "i25399"
rels.classifies.proj.plwordnet = ""
rels.classifies.proj.pointer = ""


### Relation: classified_by

rels.classified_by.form.parent = 'other'
rels.classified_by.form.inOMW = True
rels.classified_by.form.reverse = "classifies"

rels.classified_by.proj.ili = "i25002"
rels.classified_by.proj.plwordnet = ""
rels.classified_by.proj.pointer = ""


### Relation: also (no ili)

rels.also.form.parent = 'other'
rels.also.form.inOMW = True
rels.also.form.reverse = 'also'

rels.also.proj.pwn = "also see"
rels.also.proj.querywn = "also"
rels.also.proj.eurown = ""
rels.also.proj.plwordnet = "inchoativity, iterativity, distributivity, anteriority"
rels.also.proj.pointer = "^"


### Relation: antonym

rels.antonym.form.parent = 'constitutive'
rels.antonym.form.inOMW = True
rels.antonym.form.reverse = 'antonym'

rels.antonym.proj.ili = "i69547"
rels.antonym.proj.pwn = ""
rels.antonym.proj.querywn = "antonym"
rels.antonym.proj.eurown = ""
rels.antonym.proj.plwordnet = "complementary, proper and converse antonymy"
rels.antonym.proj.pointer = "!"


### Relation: entails

rels.entails.form.parent = 'other'
rels.entails.form.inOMW = True
rels.entails.form.reverse = 'is_entailed_by'

rels.entails.proj.ili = "i34846"
rels.entails.proj.pwn = "entailment"
rels.entails.proj.querywn = "participle"
rels.entails.proj.eurown = ""
rels.entails.proj.plwordnet = ""
rels.entails.proj.pointer = ""


### Relation: is_entailed_by

rels.is_entailed_by.form.parent = 'other'
rels.is_entailed_by.form.inOMW = True
rels.is_entailed_by.form.reverse = 'entails'

rels.is_entailed_by.proj.pwn = ""
rels.is_entailed_by.proj.querywn = "participle"
rels.is_entailed_by.proj.eurown = ""
rels.is_entailed_by.proj.plwordnet = ""
rels.is_entailed_by.proj.pointer = ""


### Relation: other

rels.other.form.parent = None
rels.other.form.inOMW = True

rels.other.proj.ili = "i11342"
