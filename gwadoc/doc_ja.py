# -*- coding: utf-8 -*-

from gwadoc import relations

###############################################################################
### Relations Definitions


### Relation: domain


### Relation: has_domain


### Relation: constitutive


### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

relations.hypernym.name.ja="上位語"
relations.hypernym.dfn.ja="当該synsetが相手synsetに包含される"
relations.hypernym.ex.ja="動物は犬の上位語"
relations.hypernym.exe.ja=""""canis familiaris"(02084071-n)は"domestic animal"(01317541-n)と"canid"(02083346-n)に包含される"""

### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

relations.hyponym.name.ja="下位語"
relations.hyponym.df.ja="""当該synsetが相手synsetを包含する"""
relations.hyponym.ex.ja=""""canis familiaris"(02084071-n)は"toy canis familiaris"(02085374-n),"mutt"(02084861-n),"pooch"(02084732-n),...を包含する"""

### Relation: similar

relations.similar.name.ja="""近似"""
relations.similar.df.ja="""当該synsetは表す意味が相手synsetと近似している"""	
relations.similar.ex.ja=""""white"(00393105-a)は意味が"albescent"(00393422-a)と近似している"""

### Relation: role


### Relation: agent


### Relation: patient


### Relation: result


### Relation: instrument


### Relation: location


### Relation: direction


### Relation: target_direction


### Relation: source_direction


### Relation: involved


### Relation: involved_agent (EuroWordNet - page 29/30)


### Relation: involved_patient


### Relation: involved_result


### Relation: involved_instrument


### Relation: involved_location


### Relation: involved_direction


### Relation: involved_target_direction


### Relation: involved_source_direction


### Relation: co_role EDP31


### Relation: co_agent_patient EDP32


### Relation: co_agent_instrument EDP32


### Relation: co_agent_result EDP32


### Relation: co_patient_agent EDP32


### Relation: co_patient_instrument EDP32


### Relation: co_result_agent EDP32


### Relation: co_result_instrument EDP32


### Relation: co_instrument_agent EDP32


### Relation: co_instrument_patient EDP32


### Relation: co_instrument_result ice saw/ice


### Relation: state_of EDP37


### Relation: be_in_state EDP37


### Relation: causes EDP34

relations.causes.name.ja="引き起こし"
relations.causes.df.ja="""当該synsetを行うと、相手synsetを引き起こす"""
relations.causes.ex.ja=""""project"(02138075-v)を行うと、"appear"(00422090-v)を引き起こす"""

### Relation: is_caused_by EDP34


### Relation: subevent EDP35


### Relation: is_subevent_of EDP35


### Relation: in_manner EDP36


### Relation: manner_of EDP36


### Relation: meronym EDP26

relations.meronym.name.ja="被構成要素"
relations.meronym.df.ja="""当該synsetが相手synsetによって構成される"""

### Relation: holonym EDP26
relations.holonym.name.ja="構成要素"
relations.holonym.df.ja="""当該synsetがsynsetを構成する"""

### Relation: mero_part EDP27
relations.mero_part.name.ja="被構成要素(部分)"
relations.mero_part.df.ja="""当該synsetが相手synsetという部分によって構成される"""
relations.mero_part.ex.ja=""""canis familiaris"(02084071-n)は"flag"(02158846-n)を一部分として持つ"""

### Relation: holo_part EDP27
relations.holo_part.name.ja="構成要素(部分)"
relations.holo_part.df.ja="""当該synsetが部分として相手synsetを構成する"""
relations.holo_part.ex.ja=""""flag"(02158846-n)は"canis familiaris"(02084071-n)や"cervid"(02430045-n)の一部分である"""

### Relation: mero_member EPD27


relations.mero_member.name.ja="構成要素(構成員)"
relations.mero_member.df.ja="""当該synsetが相手synsetの構成員である"""
relations.mero_member.ex.ja=""""canis familiaris"(02084071-n)は"02083863-n"(canis)や"pack"(07994941-n)の構成員である"""

### Relation: holo_member EDP27

relations.holo_member.name.ja="被構成要素(構成員)"
relations.holo_member.df.ja="""当該synsetが相手synsetという構成員によって構成される"""
relations.holo_member.ex.ja=""""canis"(02083863-n)は"canis familiaris"(02084071-n)や" jackal"(02115096-n)、"wolf"(02114100-n)を構成員として持"""

### Relation: mero_substance EDP28

relations.mero_substance.name.ja="被構成要素(物質・材料)"
relations.mero_substance.df.ja="""当該synsetが相手synsetという物質or材料によって構成される"""
relations.mero_substance.ex.ja=""""ozone"(14972807-n)は"atomic number 8"(14648100-n)という物質を構成要素として持つ"""

### Relation: holo_substance EDP28

relations.holo_substance.name.ja="構成要素(物質・材料)"
relations.holo_substance.df.ja="""当該synsetが相手synsetを構成する物質or材料である"""
relations.holo_substance.ex.ja=""""atomic number 8"(14648100-n)は"ozone"(14972807-n)や"water"(14845743-n)、"air"(14841267-n)を構成する物質である"""

### Relation: mero_location EDP28


### Relation: holo_location EDP28


### Relation: mero_portion EDP27


### Relation: holo_portion EDP27


### Relation: eq_synonym

relations.eq_synonym.name.ja="同義語"

### Relation: instance_hypernym


relations.instance_hypernym.name.ja="事例あり"
relations.instance_hypernym.df.ja="""当該synsetは相手synsetを事例として持つ"""
relations.instance_hypernym.ex.ja=""""director"(09952539-n)は"seiji ozawa"(11219502-n)を事例に持つ"""

### Relation: instance_hyponym

relations.instance_hyponym.name.ja="事例"
relations.instance_hyponym.df.ja="""当該synsetは相手synsetの事例である"""
relations.instance_hyponym.ex.ja=""""seiji ozawa"(11219502-n)は"director"(09952539-n)の事例である"""

### Relation: exemplifies
relations.exemplifies.name.ja="被包含領域(語法)"
relations.exemplifies.df.ja="""当該synsetの用法が相手synsetの領域に限られる"""
relations.exemplifies.ex.ja=""""jean"(03594734-n)の用法は"plural form"(06295235-n)に限定される"""


### Relation: is_exemplified_by

relations.is_exemplified_by.name.ja="包含領域(語法)"
relations.is_exemplified_by.df.ja="""当該synsetの領域が相手synsetの用法を規定する"""
relations.is_exemplified_by.ex.ja=""""plural form"(06295235-n)は"jean"(03594734-n)の用法を規定する"""

### Relation: domain_topic

relations.domain_topic.name.ja="被包含領域(カテゴリ)"
relations.domain_topic.df.ja="""当該synsetが相手synsetのカテゴリに属する"""
relations.domain_topic.ex.ja=""""comet"(09251407-n)は"astronomy"(06095022-n)のカテゴリに属する"""

### Relation: has_domain_topic

relations.has_domain_topic.name.ja="包含領域(カテゴリ)"
relations.has_domain_topic.df.ja="""当該synsetが相手synsetが属するカテゴリである"""
relations.has_domain_topic.ex.ja=""""astronomy"(06095022-n)というカテゴリには"uprise"(01970348-v)や"absolute magnitude"(05090979-n)が属している"""

### Relation: domain_region

relations.domain_region.name.ja="被包含領域(地域)"
relations.domain_region.df.ja="""当該synsetが相手synsetの地域に属するものである"""
relations.domain_region.ex.ja=""""sake"(07891433-n)は"nippon"(08921850-n)という地域に属している"""

### Relation: has_domain_region

relations.has_domain_region.name.ja="包含領域(地域)"
relations.has_domain_region.df.ja="""当該synsetが相手synsetの属する地域である"""
relations.has_domain_region.ex.ja=""""nippon"(08921850-n)は"sake"(07891433-n)の属する地域である"""

### Relation: attribute
relations.attribute.name.ja="属性"
relations.attribute.df.ja="""(a=形容詞のsynsetから見て)当該synsetが相手synsetという属性を表す際に使われる
(n=名詞のsynsetから見て)当該synsetという属性を表す際に相手synsetを使う"""
relations.attribute.ex.ja=""""white"(00393105-a)は"value"(04979425-n)という属性を表す際に使われる"""


### Relation: restricts


### Relation: restricted_by


### Relation: classifies


### Relation: classified_by


### Relation: also (no ili)

relations.also.name.ja="関連"
relations.also.df.ja="""当該synsetと相手synsetとの間に何らかの関連がある"""
relations.also.ex.ja=""""white"(00393105-a)は"light"(00408660-a)との間に何らかの関連がある"""

### Relation: antonym

relations.antonym.name.ja="対義語"
relations.antonym.df.ja="""当該語義やsynsetの意味や程度が反対または対の関係となっている語義やsynset"""
relations.antonym.ex.ja="""「長い」の対義語は「短い」"""
relations.antonym.com.ja="""類語:反意語、反対語、反義語、アントニム、対照語"""

### Relation: entails


relations.entails.name.ja="含意"
relations.entails.df.ja="""当該synsetを行う場合、必ず相手synsetも行っている"""
relations.entails.ex.ja=""" "fleece"(02319050-v)を行う場合、必ず"charge"(02320374-v)も行っている"""

### Relation: is_entailed_by


### Relation: other
relations.other.name.ja="その他"

### Relation: derivation
relations.derivation.name.ja="派生語"
relations.derivation.ex.ja="「楽しみ」は「楽しい」の派生語"
