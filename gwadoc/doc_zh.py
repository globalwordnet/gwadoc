# -*- coding: utf-8 -*-

from gwadoc import relations


###############################################################################
### Relations Definitions


### Relation: domain

relations.domain.name.zh = "域关系"
relations.domain.df.zh = "一个概念是给定概念的主题，地区或示例指针。"
relations.domain.dfn.zh = "域关系是一个总括关系，其中概念B是概念A的主题（科学类别）、地区或示例指针。"

relations.domain.ex.zh = ""
relations.domain.exe.zh = ""
relations.domain.test.zh = ""
relations.domain.com.zh = """
该关系是一个总括关系，包含主题域、地区域、和示例域。因此，\
它不是词网中直接使用的一种关系，但词网把它当作一个总括的关系，将相应的子关系归在该关系下。
"""



### Relation: has_domain

relations.has_domain.name.zh = "在域关系"
relations.has_domain.df.zh = "给定主题，地区或示例域概念中的一个专有概念。"
relations.has_domain.dfn.zh = "在域关系是一个总括关系，其中概念A是概念B主题（科学类别）、地区或示例域中的一个专有概念。"

relations.has_domain.ex.zh = ""
relations.has_domain.exe.zh = ""
relations.has_domain.test.zh = ""
relations.has_domain.com.zh = """
该关系是一个总括关系，包含在主题域、在地区域、和在示例域。因此，\
它不是词网中直接使用的一种关系，但词网把它当作一个总括的关系，将相应的子关系归在该关系下。
"""



### Relation: constitutive

relations.constitutive.name.zh = "基本关系"
relations.constitutive.df.zh = "能够用来定义同义词集的核心语义概念关系。"
relations.constitutive.dfn.zh = ""



### Relation: Hypernym
### X ⊃ Y,  X is a hypernym of Y

relations.hypernym.name.zh = "上位关系"
relations.hypernym.df.zh = "比给定概念更具概括性、更笼统的一个概念。"
relations.hypernym.dfn.zh = "上位关系指两个概念之间，概念A是一个更笼统的概念，它能涵盖概念B。"

relations.hypernym.ex.zh = "动物 (cmnwn-00015388-n) 是狗 (cmnwn-02084071-n) 的上位关系概念"
relations.hypernym.exe.zh = """
* 动物 (cmnwn-00015388-n) 是狗 (cmnwn-02084071-n) 的上位关系概念
* 肉 (cmnwn-07649854-n) 是牛肉 (cmnwn-07663592-n) 的上位关系概念
* 水果 (cmnwn-13134947-n) 是浆果 (cmnwn-13137409-n) 的上位关系概念
"""
relations.hypernym.test.zh = ""
relations.hypernym.com.zh = ""



### Relation: hyponym
### X ⊂ Y,  X is a hyponym of Y

relations.hyponym.name.zh = "下位关系"
relations.hyponym.df.zh = "比给定概念更具体的一个概念。"
relations.hyponym.dfn.zh = "下位关系指两个概念之间，概念B是比概念A更具体的一个概念。"

relations.hyponym.ex.zh = "狗 (cmnwn-02084071-n) 是 动物 (cmnwn-00015388-n) 的下位关系概念"
relations.hyponym.exe.zh = """
* 狗 (cmnwn-02084071-n) 是动物 (cmnwn-00015388-n) 的下位关系概念
* 牛肉 (cmnwn-07663592-n) 是肉 (cmnwn-07649854-n) 的下位关系概念
* 浆果 (cmnwn-13137409-n) 是水果 (cmnwn-13134947-n) 的下位关系概念
"""
relations.hyponym.test.zh = ""
relations.hyponym.com.zh = ""



### Relation: similar

relations.similar.name.zh = "近义关系"
relations.similar.df.zh = "与给定概念意义相近的一个概念。"
relations.similar.dfn.zh = """
近义关系指含义相近，但不在同一同义词集中的两个概念。\
该关系具有双向性，如果概念A与概念B是近义词，那同样的，概念B与概念A也是近义词。\
起初该关系仅用于连接形容词，但之后不再局限于此，而是可以用来连接各类词类。\
近义关系可被看作弱同义，与所有词元都必须有相同意义的真正同义关系不同。\
由于形容词不像动词或名词那样是按层次结构来组织的（上位关系/下位关系），\
因此近义关系有助于显示形容词之间的关系。
"""

relations.similar.ex.zh = ""
relations.similar.exe.zh = ""
relations.similar.test.zh = ""
relations.similar.com.zh = ""



### Relation: role

relations.role.name.zh = "角色关系"
relations.role.df.zh = "给定概念表示的动作或事件中所涉及的一个概念。"
relations.role.dfn.zh = "角色关系是一个总括型关系，指两个概念之间，概念A通常涉及概念B所表示的动作或事件。"

relations.role.ex.zh = ""
relations.role.exe.zh = ""
relations.role.test.zh = ""
relations.role.com.zh = """
该关系为总括型关系，包括施事、受事、结果，工具、地点、方向、目标方向和源方向关系。\
因此，该关系并不是词网中直接使用的关系，只是把它作为涵盖所有子类型的总括关系。
"""



### Relation: agent

relations.agent.name.zh = "施事关系"
relations.agent.df.zh = "通常是执行给定概念所表示动作的一个施事者概念。"
relations.agent.dfn.zh = "施事关系指两个概念之间，概念A是有生命个体的语义角色，通常有意识地促使或引起概念B动作的发生。"

relations.agent.ex.zh = "教师 (cmnwn-10694258-n) 是教 (cmnwn-00829107-v) 的施事关系概念"
relations.agent.exe.zh = """
* 教师 (cmnwn-10694258-n) 是教 (cmnwn-00829107-v) 的施事关系概念
"""
relations.agent.test.zh = ""
relations.agent.com.zh = ""



### Relation: patient

relations.patient.name.zh = "受事关系"
relations.patient.df.zh = "经历给定概念所指事件的那一个概念。"
relations.patient.dfn.zh = "受事关系指两个概念之间，概念A是非施事的语义角色，但直接涉及或者受概念B所表示事件的影响。"

relations.patient.ex.zh = "学习者 (cmnwn-10251779-n) 是学 (cmnwn-00604576-v) 的受事关系概念"
relations.patient.exe.zh = """
* 学习者 (cmnwn-10251779-n) 是学 (cmnwn-00604576-v) 的受事关系概念
"""
relations.patient.test.zh = ""
relations.patient.com.zh = ""



### Relation: result

relations.result.name.zh = "结果关系"
relations.result.df.zh = "作为给定概念的结果而产生的一个概念。"
relations.result.dfn.zh = "结果关系指两个概念之间，概念A是仅由于概念B表示的活动而存在的结果。"

relations.result.ex.zh = "冰 (cmnwn-14915184-n) 是冻结 (cmnwn-00374135-v) 的结果关系概念"
relations.result.exe.zh = """
* 冰 (cmnwn-14915184-n) 是冻结 (cmnwn-00374135-v) 的结果关系概念
"""
relations.result.test.zh = ""
relations.result.com.zh = ""



### Relation: instrument

relations.instrument.name.zh = "工具关系"
relations.instrument.df.zh = "一个概念是给定概念表达的动作或事件所必需的工具。"
relations.instrument.dfn.zh = "工具关系指两个概念之间，概念A是施事用来实施概念B所表达的动作或者步骤的语义角色实体（通常是无生命的）。"

relations.instrument.ex.zh = "船 (cmnwn-02858304-n) 是航行 (cmnwn-01945516-v) 的工具关系概念"
relations.instrument.exe.zh = """
* 船 (cmnwn-02858304-n) 是航行 (cmnwn-01945516-v) 的工具关系概念
* 钢笔 (cmnwn-03906997-n) 是写 (cmnwn-00993014-v) 的工具关系概念
* 纸 (cmnwn-14974264-n) 是写 (cmnwn-00993014-v) 的工具关系概念
"""
relations.instrument.test.zh = ""
relations.instrument.com.zh = ""



### Relation: location

relations.location.name.zh = "地点关系"
relations.location.df.zh = "一个概念是给定概念所表达事件发生的地点。"
relations.location.dfn.zh = "地点关系指两个概念之间，概念A是概念B所表示的动作或事件发生的地点。"

relations.location.ex.zh = "学校 (cmnwn-04146050-n) 是教 (cmnwn-00829107-v) 的地点关系概念"
relations.location.exe.zh = """
* 学校 (cmnwn-04146050-n) 是教 (cmnwn-00829107-v) 的地点关系概念
* 河 (cmnwn-09411430-n) 是游泳 (cmnwn-01960911-v) 的地点关系概念
"""
relations.location.test.zh = ""
relations.location.com.zh = ""



### Relation: direction

relations.direction.name.zh = "方向关系"
relations.direction.df.zh = "一个概念是给定概念所表示的动作或事件的方向。"
relations.direction.dfn.zh = "方向关系指两个概念之间，概念A通常是概念B所表示的动作或事件的方向。"

relations.direction.ex.zh = "前 (cmnwn-01728476-a) 是冲 (cmnwn-02713852-v) 的方向关系概念"
relations.direction.exe.zh = """
* 前 (cmnwn-01728476-a) 是冲 (cmnwn-02713852-v) 的方向关系概念
"""
relations.direction.test.zh = ""
relations.direction.com.zh = ""



### Relation: target_direction

relations.target_direction.name.zh = "目标方向关系"
relations.target_direction.df.zh = "一个概念是给定概念所表达动作或事件导向的方向。"
relations.target_direction.dfn.zh = "目标方向关系指两个概念之间，概念A是概念B所表示的动作或事件指向的终点（无论是比赛还是旅行）。"

relations.target_direction.ex.zh = "地面 (cmnwn-09334396-n) 是掉 (cmnwn-01976841-v) 的目标方向关系概念"
relations.target_direction.exe.zh = """
* 地面 (cmnwn-09334396-n) 是掉 (cmnwn-01976841-v) 的目标方向关系概念
* 家 (cmnwn-03544360-n) 是回 (cmnwn-02004874-v) 的目标方向关系概念
"""
relations.target_direction.test.zh = ""
relations.target_direction.com.zh = ""



### Relation: source_direction

relations.source_direction.name.zh = "源方向关系"
relations.source_direction.df.zh = "一个概念是给定概念所表示的事件开始的地方。"
relations.source_direction.dfn.zh = "源方向关系指两个概念之间，概念A是概念B所表示的动作或事件开始/发生的地方。"

relations.source_direction.ex.zh = "起点 (cmnwn-15266164-n) 是跑步 (cmnwn-01926311-v) 的源方向关系概念"
relations.source_direction.exe.zh = """
* 起点 (cmnwn-15266164-n) 是跑步 (cmnwn-01926311-v) 的源方向关系概念
"""
relations.source_direction.test.zh = ""
relations.source_direction.com.zh = ""



### Relation: involved

relations.involved.name.zh = "涉及关系"
relations.involved.df.zh = "一个概念通常是给定概念所涉及的动作或事件。"
relations.involved.dfn.zh = "涉及关系是一个总括型关系，指两个概念之间，概念A通常是概念B所涉及的动作或事件。"

relations.involved.ex.zh = ""
relations.involved.exe.zh = ""
relations.involved.test.zh = ""
relations.involved.com.zh = """
该关系为总括型关系，包括施事涉及、受事涉及、结果涉及，工具涉及、地点涉及、方向涉及、目标方向涉及和源方向涉及关系。\
因此，该关系并不是词网中直接使用的关系，但是把它作为涵盖所有子类型的总括关系。
"""



### Relation: involved_agent (EuroWordNet - page 29/30)

relations.involved_agent.name.zh = "施事涉及关系"
relations.involved_agent.df.zh = "一个概念是给定概念所表示的施事做出的动作。"
relations.involved_agent.dfn.zh = "施事涉及关系指两个概念之间，概念B通常是概念A所表示施事做出的动作。"

relations.involved_agent.ex.zh = "教 (cmnwn-00829107-v) 是教师 (cmnwn-10694258-n) 的施事涉及关系概念"
relations.involved_agent.exe.zh = """
* 教 (cmnwn-00829107-v) 是教师 (cmnwn-10694258-n) 的施事涉及关系概念
"""
relations.involved_agent.test.zh = ""
relations.involved_agent.com.zh = ""



### Relation: involved_patient

relations.involved_patient.name.zh = "受事涉及关系"
relations.involved_patient.df.zh = "一个概念是给定概念所表示的受事经受的动作。"
relations.involved_patient.dfn.zh = "受事涉及关系指两个概念之间，概念B通常是概念A所表示的受事经受的动作或事件。"

relations.involved_patient.ex.zh = "学 (cmnwn-00604576-v) 是学习者 (cmnwn-10251779-n) 的受事涉及关系概念"
relations.involved_patient.exe.zh = """
* 学 (cmnwn-00604576-v) 是学习者 (cmnwn-10251779-n) 的受事涉及关系概念
"""
relations.involved_patient.test.zh = ""
relations.involved_patient.com.zh = ""


### Relation: involved_result

relations.involved_result.name.zh = "结果涉及关系"
relations.involved_result.df.zh = "一个动作或事件概念形成了给定概念所表示的结果。"
relations.involved_result.dfn.zh = "结果涉及关系指两个概念之间，概念B表示的动作或事件形成了概念A所表示的结果。"

relations.involved_result.ex.zh = "冻结 (cmnwn-00374135-v) 是冰 (cmnwn-14915184-n) 的结果涉及关系概念"
relations.involved_result.exe.zh = """
* 冻结 (cmnwn-00374135-v) 是冰 (cmnwn-14915184-n) 的结果涉及关系概念
"""
relations.involved_result.test.zh = ""
relations.involved_result.com.zh = ""



### Relation: involved_instrument

relations.involved_instrument.name.zh = "工具涉及关系"
relations.involved_instrument.df.zh = "一个动作概念是通过使用给定概念表示的工具发生的。"
relations.involved_instrument.dfn.zh = "工具涉及关系指两个概念之间，概念B表示的动作或者事件通过使用概念A 所表示的工具而发生。"

relations.involved_instrument.ex.zh = "航行 (cmnwn-01945516-v) 是船 (cmnwn-02858304-n) 的工具涉及关系概念"
relations.involved_instrument.exe.zh = """
* 航行 (cmnwn-01945516-v) 是船 (cmnwn-02858304-n) 的工具涉及关系概念
* 写 (cmnwn-00993014-v) 是钢笔 (cmnwn-03906997-n) 的工具涉及关系概念
* 写 (cmnwn-00993014-v) 是纸 (cmnwn-14974264-n) 的工具涉及关系概念
"""
relations.involved_instrument.test.zh = ""
relations.involved_instrument.com.zh = ""



### Relation: involved_location

relations.involved_location.name.zh = "地点涉及关系"
relations.involved_location.df.zh = "一个事件概念发生在给定概念所表示的地点。"
relations.involved_location.dfn.zh = "地点涉及关系指两个概念之间，通常概念B表示的动作或事件发生在概念A所表示的地点上。"

relations.involved_location.ex.zh = "教 (cmnwn-00829107-v) 是学校 (cmnwn-04146050-n) 的地点涉及关系概念"
relations.involved_location.exe.zh = """
* 教 (cmnwn-00829107-v) 是学校 (cmnwn-04146050-n) 的地点涉及关系概念
* 游泳 (cmnwn-01960911-v) 是河 (cmnwn-09411430-n) 的地点涉及关系概念
"""
relations.involved_location.test.zh = ""
relations.involved_location.com.zh = ""



### Relation: involved_direction

relations.involved_direction.name.zh = "方向涉及关系"
relations.involved_direction.df.zh = "一个动作概念朝着给定概念表示的方向运动。"
relations.involved_direction.dfn.zh = "方向涉及关系指两个概念之间，概念B表示的动作或事件朝着概念A表示的方向运动。"

relations.involved_direction.ex.zh = "冲 (cmnwn-02713852-v) 是前 (cmnwn-01728476-a) 的方向涉及关系概念" 
relations.involved_direction.exe.zh = """
* 冲 (cmnwn-02713852-v) 是前 (cmnwn-01728476-a) 的方向涉及关系概念
"""
relations.involved_direction.test.zh = ""
relations.involved_direction.com.zh = ""



### Relation: involved_target_direction

relations.involved_target_direction.name.zh = "目标方向涉及关系"
relations.involved_target_direction.df.zh = "一个动作或事件概念导向给定概念表示的方位。"
relations.involved_target_direction.dfn.zh = "目标方向涉及关系指两个概念之间，概念B表示的动作或事件朝着概念A 表示的方位运动。"

relations.involved_target_direction.ex.zh = "掉 (cmnwn-01976841-v) 是地面 (cmnwn-09334396-n) 的目标方向涉及关系概念"
relations.involved_target_direction.exe.zh = """
* 掉 (cmnwn-01976841-v) 是地面 (cmnwn-09334396-n) 的目标方向涉及关系概念
* 回 (cmnwn-02004874-v) 是家 (cmnwn-03544360-n) 的目标方向涉及关系概念
"""
relations.involved_target_direction.test.zh = ""
relations.involved_target_direction.com.zh = ""



### Relation: involved_source_direction

relations.involved_source_direction.name.zh = "源方向涉及关系"
relations.involved_source_direction.df.zh = "一个动作概念从给定概念表示的方位开始。"
relations.involved_source_direction.dfn.zh = "源方向涉及关系指两个概念之间，概念B表示的动作或事件从概念A所表示的方位开始。"

relations.involved_source_direction.ex.zh = "跑步 (cmnwn-01926311-v) 是起点 (cmnwn-15266164-n) 的源方向涉及关系概念"
relations.involved_source_direction.exe.zh = """
* 跑步 (cmnwn-01926311-v) 是起点 (cmnwn-15266164-n) 的源方向涉及关系概念
"""
relations.involved_source_direction.test.zh = ""
relations.involved_source_direction.com.zh = ""



### Relation: co_role EDP31

relations.co_role.name.zh = "共同角色关系"
relations.co_role.df.zh = "一个概念经历着给定概念涉及的动作。"
relations.co_role.dfn.zh = "共同角色是一个总括型关系，指两个概念之间，概念A经历着涉及概念B的动作（双向的）。"

relations.co_role.ex.zh = ""
relations.co_role.exe.zh = ""
relations.co_role.test.zh = ""
relations.co_role.com.zh = """
该关系为总括型关系，包括共同施事受事、共同受事施事、共同施事工具，共同工具施事、共同施事结果、共同结果施事、共同受事工具、共同工具受事、\
共同结果工具和共同工具结果关系。因此，该关系并不是词网中直接使用的关系，但是把它作为涵盖所有子类型的总括关系。
"""



### Relation: co_agent_patient EDP32

relations.co_agent_patient.name.zh = "共同施事受事关系"
relations.co_agent_patient.df.zh = "一个受事概念正在经受由给定概念执行的动作。"
relations.co_agent_patient.dfn.zh = "共同施事受事关系指两个概念之间，概念B是受事，经历着由概念A执行的动作。"

relations.co_agent_patient.ex.zh = "受害者 (cmnwn-10752093-n) 是罪犯 (cmnwn-09977660-n) 的共同施事受事关系概念"
relations.co_agent_patient.exe.zh = """
* 受害者 (cmnwn-10752093-n) 是罪犯 (cmnwn-09977660-n) 的共同施事受事关系概念
"""
relations.co_agent_patient.com.zh = ""



### Relation: co_patient_agent EDP32

relations.co_patient_agent.name.zh = "共同受事施事关系"
relations.co_patient_agent.df.zh = "一个概念执行的动作是给定概念正在经历的。"
relations.co_patient_agent.dfn.zh = "共同受事施事关系指两个概念之间，概念A执行的动作，是概念B正在经历的。"

relations.co_patient_agent.ex.zh = "罪犯 (cmnwn-09977660-n) 是受害者 (cmnwn-10752093-n) 的共同受事施事关系概念"
relations.co_patient_agent.exe.zh = """
* 罪犯 (cmnwn-09977660-n) 是受害者 (cmnwn-10752093-n) 的共同受事施事关系概念
"""
relations.co_patient_agent.test.zh = ""
relations.co_patient_agent.com.zh = ""



### Relation: co_agent_instrument EDP32

relations.co_agent_instrument.name.zh = "共同施事工具关系"
relations.co_agent_instrument.df.zh = "给定施事概念在动作中使用的一个工具概念。"
relations.co_agent_instrument.dfn.zh = "共同施事工具关系指两个概念之间，概念B是概念A执行动作时使用的工具。"

relations.co_agent_instrument.ex.zh = "画笔 (cmnwn-03234952-n) 是 画家 (cmnwn-10391653-n) 的共同施事工具关系概念"
relations.co_agent_instrument.exe.zh = """
* 画笔 (cmnwn-03234952-n) 是画家 (cmnwn-10391653-n) 的共同施事工具关系概念
"""
relations.co_agent_instrument.test.zh = ""
relations.co_agent_instrument.com.zh = ""



### Relation: co_instrument_agent EDP32

relations.co_instrument_agent.name.zh = "共同工具施事关系"
relations.co_instrument_agent.df.zh = "一个概念通过使用给定工具概念来执行动作。"
relations.co_instrument_agent.dfn.zh = "共同工具施事关系指两个概念之间，概念A通过使用概念B表示的工具来执行动作。"

relations.co_instrument_agent.ex.zh = "画家 (cmnwn-10391653-n) 是画笔 (cmnwn-03234952-n) 的共同工具施事关系概念"
relations.co_instrument_agent.exe.zh = """
* 画家 (cmnwn-10391653-n) 是画笔 (cmnwn-03234952-n) 的共同工具施事关系概念
"""
relations.co_instrument_agent.test.zh = ""
relations.co_instrument_agent.com.zh = ""



### Relation: co_agent_result EDP32

relations.co_agent_result.name.zh = "共同施事结果关系"
relations.co_agent_result.df.zh = "一个概念是给定施事概念执行动作产生的结果。"
relations.co_agent_result.dfn.zh = "共同施事结果关系指两个概念之间，概念B是概念A执行动作所产生的结果。"

relations.co_agent_result.ex.zh = "曲子 (cmnwn-07028373-n) 是作曲家 (cmnwn-09947232-n) 的共同施事结果关系概念"
relations.co_agent_result.exe.zh = """
* 曲子 (cmnwn-07028373-n) 是作曲家 (cmnwn-09947232-n) 的共同施事结果关系概念
"""
relations.co_agent_result.com.zh = ""



### Relation: co_result_agent EDP32

relations.co_result_agent.name.zh = "共同结果施事关系"
relations.co_result_agent.df.zh = "一个概念发起的动作产生了给定概念表示的结果。"
relations.co_result_agent.dfn.zh = "共同结果施事关系指两个概念之间，概念A发起的动作产生了概念B表示的结果。"

relations.co_result_agent.ex.zh = "作曲家 (cmnwn-09947232-n) 是曲子 (cmnwn-07028373-n) 的共同结果施事关系概念"
relations.co_result_agent.exe.zh = """
* 作曲家 (cmnwn-09947232-n) 是曲子 (cmnwn-07028373-n) 的共同结果施事关系概念
"""
relations.co_result_agent.test.zh = ""
relations.co_result_agent.com.zh = ""



### Relation: co_patient_instrument EDP32

relations.co_patient_instrument.name.zh = "共同受事工具关系"
relations.co_patient_instrument.df.zh = "一个概念是给定概念在经历某个动作时使用的工具。"
relations.co_patient_instrument.dfn.zh = "共同受事工具关系指两个概念之间，概念B是概念A经受某个动作时使用的工具。"

relations.co_patient_instrument.ex.zh = "菜刀 (cmnwn-03041632-n) 是菜 (cmnwn-07557434-n) 的共同受事工具关系概念"
relations.co_patient_instrument.exe.zh = """
* 菜刀 (cmnwn-03041632-n) 是菜 (cmnwn-07557434-n) 的共同受事工具关系概念
"""
relations.co_patient_instrument.test.zh = ""
relations.co_patient_instrument.com.zh = ""



### Relation: co_instrument_patient EDP32

relations.co_instrument_patient.name.zh = "共同工具受事关系"
relations.co_instrument_patient.df.zh = "通过使用给定工具概念，一个概念经受着某个动作。"
relations.co_instrument_patient.dfn.zh = "共同工具受事关系指两个概念之间，概念A通过使用概念B表示的工具来经受某个动作。"

relations.co_instrument_patient.ex.zh = "菜 (cmnwn-07557434-n) 是菜刀 (cmnwn-03041632-n) 的共同工具受事关系概念"
relations.co_instrument_patient.exe.zh = """
* 菜 (cmnwn-07557434-n) 是菜刀 (cmnwn-03041632-n) 的共同工具受事关系概念
"""
relations.co_instrument_patient.test.zh = ""
relations.co_instrument_patient.com.zh = ""



### Relation: co_result_instrument EDP32

relations.co_result_instrument.name.zh = "共同结果工具关系"
relations.co_result_instrument.df.zh = "在某个动作中使用一个工具概念，以产生给定结果概念。"
relations.co_result_instrument.dfn.zh = "共同结果工具关系指两个概念之间，概念B是某个动作中使用的工具，以产生概念A 表示的结果。"

relations.co_result_instrument.ex.zh = "照相机 (cmnwn-02942699-n) 是照片 (cmnwn-03925226-n) 的共同结果工具关系概念"
relations.co_result_instrument.exe.zh = """
* 照相机 (cmnwn-02942699-n) 是照片 (cmnwn-03925226-n) 的共同结果工具关系概念
"""
relations.co_result_instrument.test.zh = ""
relations.co_result_instrument.com.zh = ""


### Relation: co_instrument_result ice saw/ice

relations.co_instrument_result.name.zh = "共同工具结果关系"
relations.co_instrument_result.df.zh = "一个概念是某个动作通过使用给定工具概念所产生的结果。"
relations.co_instrument_result.dfn.zh = "共同工具结果关系指两个概念之间，概念A是通过使用概念B表示的工具产生的动作的结果，"

relations.co_instrument_result.ex.zh = "照片 (cmnwn-03925226-n) 是照相机 (cmnwn-02942699-n) 的共同工具结果关系概念"
relations.co_instrument_result.exe.zh = """
* 照片 (cmnwn-03925226-n) 是照相机 (cmnwn-02942699-n) 的共同工具结果关系概念
"""
relations.co_instrument_result.test.zh = ""
relations.co_instrument_result.com.zh = ""



### Relation: state_of EDP37

relations.state_of.name.zh = "状态关系"
relations.state_of.df.zh = "一个概念是适用于给定概念的一种状态。"
relations.state_of.dfn.zh = "状态关系指两个概念之间，概念A是适用于概念B的一种状态。"

relations.state_of.ex.zh = "富 (cmnwn-02021905-a) 是富人 (cmnwn-09776642-n) 的状态关系概念"
relations.state_of.exe.zh = """
* 富 (cmnwn-02021905-a) 是富人 (cmnwn-09776642-n) 的状态关系概念
"""
relations.state_of.test.zh = ""
relations.state_of.com.zh = ""



### Relation: be_in_state EDP37

relations.be_in_state.name.zh = "具有状态关系"
relations.be_in_state.df.zh = "一个概念具有给定概念表示的状态。"
relations.be_in_state.dfn.zh = "具有状态关系指两个概念之间，概念B具有概念A表示的某种状态。"

relations.be_in_state.ex.zh = "富人 (cmnwn-09776642-n) 具有状态关系概念富 (cmnwn-02021905-a) "
relations.be_in_state.exe.zh = """
* 富人 (cmnwn-09776642-n) 具有状态关系概念富 (cmnwn-02021905-a) 
"""
relations.be_in_state.test.zh = ""
relations.be_in_state.com.zh = ""



### Relation: causes EDP34

relations.causes.name.zh = "原因关系"
relations.causes.df.zh = "一个概念是使给定概念产生效果，或对给定事件概念结果负责的实体。"
relations.causes.dfn.zh = "原因关系指两个概念之间，概念A是概念B的原因。"

relations.causes.ex.zh = "杀 (cmnwn-01323958-v) 是死亡 (cmnwn-00358431-v) 的原因关系概念"
relations.causes.exe.zh = """
* 杀 (cmnwn-01323958-v) 是死亡 (cmnwn-00358431-v) 的原因关系概念
"""
relations.causes.test.zh = ""
relations.causes.com.zh = """
蕴涵关系是连接两个动词的关系，是单向的，动词A蕴涵动词B，而不是双向的。原因关系预设/要求动词B不可避免地\
会在动词A发生期间或之后发生（例如，如果动词A发生了，那么动词B也会发生）。\
尽管这些动词不具排他性，但许多既具有及物性又具有不及物性的动词都会经常归入这种关系中。
"""



### Relation: is_caused_by EDP34

relations.is_caused_by.name.zh = "为原因关系"
relations.is_caused_by.df.zh = "一个概念的出现是由给定概念造成的。"
relations.is_caused_by.dfn.zh = "为原因关系指两个概念之间，概念A因概念B而存在。"

relations.is_caused_by.ex.zh = "死亡 (cmnwn-00358431-v) 的为原因关系概念是杀 (cmnwn-01323958-v) "
relations.is_caused_by.exe.zh = """
* 死亡 (cmnwn-00358431-v) 的为原因关系概念是杀 (cmnwn-01323958-v) 
"""
relations.is_caused_by.test.zh = ""
relations.is_caused_by.com.zh = ""



### Relation: subevent EDP35

relations.subevent.name.zh = "子事件关系"
relations.subevent.df.zh = "一个概念与给定概念同步，且在给定概念发生期间，作为其一部分而发生。"
relations.subevent.dfn.zh = "子事件关系指两个概念之间，概念B在概念A期间作为概念A的一部分发生，且每当概念B发生时，概念A就会发生。"

relations.subevent.ex.zh = "睡觉 (cmnwn-00017865-v) 的子事件关系概念是做梦 (cmnwn-02118242-v) "
relations.subevent.exe.zh = """
* 睡觉 (cmnwn-00017865-v) 的子事件关系概念是做梦 (cmnwn-02118242-v) 
"""
relations.subevent.test.zh = ""
relations.subevent.com.zh = "子事件关系对于许多密切相关的动词非常有用，并且更符合人的直觉（与具体实体的整体—部分关系相比）。"



### Relation: is_subevent_of EDP35

relations.is_subevent_of.name.zh = "为子事件关系"
relations.is_subevent_of.df.zh = "一个概念为给定概念的一部分，且同步发生。"
relations.is_subevent_of.dfn.zh = "为子事件关系指两个概念之间，概念A的一部分是概念B，且每当概念B发生时，概念A就会发生。"

relations.is_subevent_of.ex.zh = "做梦 (cmnwn-02118242-v) 的为子事件关系概念是睡觉 (cmnwn-00017865-v) "
relations.is_subevent_of.exe.zh = """
* 做梦 (cmnwn-02118242-v) 的为子事件关系概念是睡觉 (cmnwn-00017865-v) 
"""
relations.is_subevent_of.test.zh = ""
relations.is_subevent_of.com.zh = ""



### Relation: in_manner EDP36

relations.in_manner.name.zh = "方式关系"
relations.in_manner.df.zh = "一个概念是给定概念动作或事件发生的方式。"
relations.in_manner.dfn.zh = "方式关系指两个概念之间，概念B是概念A表示的动作或事件发生的方式。"

relations.in_manner.ex.zh = "吼叫 (cmnwn-00916274-v) 的方式关系概念是大声 (cmnwn-01452593-a) "
relations.in_manner.exe.zh = """
* 吼叫 (cmnwn-00916274-v) 的方式关系概念是大声 (cmnwn-01452593-a) 
"""
relations.in_manner.test.zh = ""
relations.in_manner.com.zh = ""


### Relation: manner_of EDP36

relations.manner_of.name.zh = "为方式关系"
relations.manner_of.df.zh = "一个动作或事件概念通过给定概念表示的方式发生。"
relations.manner_of.dfn.zh = "为方式关系指两个概念之间，概念A表示某一动作或事件，且通过概念B表示的方式发生。"

relations.manner_of.ex.zh = "大声 (cmnwn-01452593-a) 的为方式关系概念是吼叫 (cmnwn-00916274-v) "
relations.manner_of.exe.zh = """
* 大声 (cmnwn-01452593-a) 的为方式关系概念是吼叫 (cmnwn-00916274-v) 
"""
relations.manner_of.test.zh = ""
relations.manner_of.com.zh = ""



### Relation: meronym EDP26

relations.meronym.name.zh = "部分关系"
relations.meronym.df.zh = "一个用来表示整体中某个部分的概念。"
relations.meronym.dfn.zh = "部分关系指两个概念间，概念A是概念B整体中的一部分。"

relations.meronym.ex.zh = ""
relations.meronym.exe.zh = ""
relations.meronym.test.zh = ""
relations.meronym.com.zh = """
这是一个总括型关系，涵盖了位置型部分关系、成员型部分关系、组件型部分关系、份额型部分关系和实质型部分关系。\
且为自动计算，不是一种具体的关系。
"""


### Relation: holonym EDP26

relations.holonym.name.zh = "整体关系"
relations.holonym.df.zh = "一个用来表示整体的概念，给定概念是其部分。"
relations.holonym.dfn.zh = "整体关系指两个概念间，概念B是整体，概念A是其中的一部分。"

relations.holonym.ex.zh = ""
relations.holonym.exe.zh = ""
relations.holonym.test.zh = ""
relations.holonym.com.zh = """
这是一个总括型关系，涵盖了位置型整体关系、成员型整体关系、组件型整体关系、份额型整体关系和实质型整体关系。\
且为自动计算，不是一种具体的关系。
"""



### Relation: mero_part EDP27

relations.mero_part.name.zh = "组件型部分关系"
relations.mero_part.df.zh = "概念A是概念B整体中的一个组件部分。"
relations.mero_part.dfn.zh = """
组件型部分关系指两个概念之间，概念A是概念B整体中的一个组件部分。
部分关系与整体关系（组件型）是一对成对的关系，表示原则上可分离的组件与整体保持的一种归属关系，即使物理上的连接已经断开。概念B中可以拆分出概念A，同时概念A是概念B的一部分。
该关系还经常用于表示地理上的包含性关系。
"""

relations.mero_part.ex.zh = "汽车 (cmnwn-02958343-n) 的组件型部分关系概念是车轮 (cmnwn-02973236-n) "
relations.mero_part.exe.zh = """
* 汽车 (cmnwn-02958343-n) 的组件型部分关系概念是车轮 (cmnwn-02973236-n) 
* 手 (cmnwn-02440250-n) 的组件型部分关系是手指 (cmnwn-05566504-n)
"""
relations.mero_part.test.zh = ""
relations.mero_part.com.zh = ""



### Relation: holo_part EDP27

relations.holo_part.name.zh = "组件型整体关系"
relations.holo_part.df.zh = "概念B是整体，概念A是其中的一部分。"
relations.holo_part.dfn.zh = """
组件型整体关系指两个概念之间，概念B作为整体，概念A是其组成部分。\
部分关系与整体关系（组件型）是一对成对的关系，表示原则上可分离的组件与整体保持的一种归属关系，\
即使物理上的连接已经断开。概念B中可以拆分出概念A，同时概念A是概念B的一部分。\
该关系还经常用于表示地理上的包含性关系。
"""

relations.holo_part.ex.zh = "车轮 (cmnwn-02973236-n) 的组件型整体关系概念是汽车 (cmnwn-02958343-n) "
relations.holo_part.exe.zh = """
* 车轮 (cmnwn-02973236-n) 的组件型整体关系概念是汽车 (cmnwn-02958343-n) 
* 手指 (cmnwn-05566504-n) 的组件型部分关系是手 (cmnwn-02440250-n) 
"""
relations.holo_part.test.zh = ""
relations.holo_part.com.zh = """
该关系通常连接起组件与整体。即：某种事物以拓扑或时间方式，包含于较大实体之中，\
并且还具有某种自治性（非任意边界）和相对于整体的确定功能。
"""



### Relation: mero_member EPD27

relations.mero_member.name.zh = "成员型部分关系"
relations.mero_member.df.zh = "概念A是概念B中的成员。"
relations.mero_member.dfn.zh = """
成员型部分关系指两个概念之间，概念A是概念B中的成员、成分。\
部分关系和整体关系（成员型）是一对成对的关系，表示组织的形成和成员身份。\
与下位关系不同，因为它连接的不是概念的子类型。它连接的是组织与成员。\
—概念A的许多实例组成概念B；概念B由概念A的许多成员组成。
"""

relations.mero_member.ex.zh = "球队 (cmnwn-08208560-n) 的成员型部分关系是运动员 (cmnwn-09820263-n) "
relations.mero_member.exe.zh = """
* 球队 (cmnwn-08208560-n) 的成员型部分关系是运动员 (cmnwn-09820263-n) 
* 舰队 (cmnwn-08293336-n) 的成员型部分关系是船只 (cmnwn-04530566-n) 
"""
relations.mero_member.test.zh = ""
relations.mero_member.com.zh = ""



### Relation: holo_member EDP27

relations.holo_member.name.zh = "成员型整体关系"
relations.holo_member.df.zh = "概念B是由概念A成员组成的整体。"
relations.holo_member.dfn.zh = """
成员型部分关系指两个概念之间，概念A是概念B中的成员、成分。\
部分关系和整体关系（成员型）是一对成对的关系，表示组织的形成和成员身份。\
与下位关系不同，因为它连接的不是概念的子类型。它连接的是组织与成员。\
—概念A的许多实例组成概念B；概念B由概念A的许多成员组成。
"""

relations.holo_member.ex.zh = "运动员 (cmnwn-09820263-n) 的成员型整体关系是球队 (cmnwn-08208560-n) "
relations.holo_member.exe.zh = """
* 运动员 (cmnwn-09820263-n) 的成员型整体关系是球队 (cmnwn-08208560-n) 
* 船只 (cmnwn-04530566-n) 的成员型整体关系是舰队 (cmnwn-08293336-n) 
"""
relations.holo_member.test.zh = ""
relations.holo_member.com.zh = ""



### Relation: mero_substance EDP28

relations.mero_substance.name.zh = "实质型部分关系"
relations.mero_substance.df.zh = "概念A是生成概念B的物质。"
relations.mero_substance.dfn.zh = """
实质型部分关系指概念B是基于概念A物质生成的。\
部分关系与整体关系（实质型）是成对的，用来表示部分和整体之间结合程度较高的一种关系类型，\
分离/删除实质部分将会改变整体—概念B由概念A制成，而概念A是概念B的实质。
"""

relations.mero_substance.ex.zh = "桌子 (cmnwn-03179701-n) 的实质型部分关系概念是木头 (cmnwn-15098161-n) "
relations.mero_substance.exe.zh = """
* 桌子 (cmnwn-03179701-n) 的实质型部分关系概念是木头 (cmnwn-15098161-n) 
* 纸张 (cmnwn-06255777-n) 的实质型部分关系概念是纤维素 (cmnwn-14793921-n) 
"""
relations.mero_substance.test.zh = ""
relations.mero_substance.com.zh = """
有两种看待世界中实体的基本方法，即当作个体事物，还是看其由何构成。例如：可以看待一本书为“一本书”或“纸”。
"""


### Relation: holo_substance EDP28

relations.holo_substance.name.zh = "实质型整体关系"
relations.holo_substance.df.zh = "概念B是基于概念A物质生成的整体。"
relations.holo_substance.dfn.zh = """
实质型整体关系指概念B是基于概念A物质生成的整体。\
部分关系与整体关系（实质型）是成对的，用来表示部分和整体之间结合程度较高的一种关系类型。\
分离/删除实质部分将会改变整体—概念B由概念A制成，而概念A是概念B的实质。
"""

relations.holo_substance.ex.zh = "木头 (cmnwn-15098161-n) 的实质型整体关系概念是桌子 (cmnwn-03179701-n) "
relations.holo_substance.exe.zh = """
* 木头 (cmnwn-15098161-n) 的实质型整体关系概念是桌子 (cmnwn-03179701-n) 
* 纤维素 (cmnwn-14793921-n) 的实质型整体关系概念是纸张 (cmnwn-06255777-n) 
"""
relations.holo_substance.test.zh = ""
relations.holo_substance.com.zh = """
复杂的整体关系也包括实质，但这种情况应属于构成关系。
"""



### Relation: mero_location EDP28

relations.mero_location.name.zh = "位置型部分关系"
relations.mero_location.df.zh = "概念A处于概念B中的一处位置。"
relations.mero_location.dfn.zh = "位置型部分关系指两个概念之间，概念A是处于概念B中的一处位置。"

relations.mero_location.ex.zh = "城市 (cmnwn-08524735-n) 的位置型部分关系概念是商业中心 (cmnwn-03722288-n) "
relations.mero_location.exe.zh = """
* 城市 (cmnwn-08524735-n) 的位置型部分关系概念是商业中心 (cmnwn-03722288-n) 
"""
relations.mero_location.test.zh = ""
relations.mero_location.com.zh = ""



### Relation: holo_location EDP28

relations.holo_location.name.zh = "位置型整体关系"
relations.holo_location.df.zh = "概念B是概念A所处位置的整体。"
relations.holo_location.dfn.zh = "位置型整体关系指两个概念之间，概念B是概念A所处位置的整体。"

relations.holo_location.ex.zh = "商业中心 (cmnwn-03722288-n) 的位置型整体关系概念是城市 (cmnwn-08524735-n) "
relations.holo_location.exe.zh = """
* 商业中心 (cmnwn-03722288-n) 的位置型整体关系概念是城市 (cmnwn-08524735-n) 
"""
relations.holo_location.test.zh = ""
relations.holo_location.com.zh = ""



### Relation: mero_portion EDP27

relations.mero_portion.name.zh = "份额型部分关系"
relations.mero_portion.df.zh = "概念A在数量上占据概念B的一部分份额。"
relations.mero_portion.dfn.zh = "份额型部分关系指两个概念之间，概念A在数量上占据概念B的一部分份额。"

relations.mero_portion.ex.zh = "海洋 (cmnwn-09376198-n) 的份额型部分关系概念是浪花 (cmnwn-15056827-n) "
relations.mero_portion.exe.zh = """
* 海洋 (cmnwn-09376198-n) 的份额型部分关系概念是浪花 (cmnwn-15056827-n) 
"""
relations.mero_portion.test.zh = ""
relations.mero_portion.com.zh = ""



### Relation: holo_portion EDP27

relations.holo_portion.name.zh = "份额型整体关系"
relations.holo_portion.df.zh = "概念B是概念A占据份额的全部整体。"
relations.holo_portion.dfn.zh = "份额型整体关系指两个概念之间，概念B是概念A所占份额的全部整体。"

relations.holo_portion.ex.zh = "浪花 (cmnwn-15056827-n) 的份额型整体关系概念是海洋 (cmnwn-09376198-n) "
relations.holo_portion.exe.zh = """
* 浪花 (cmnwn-15056827-n) 的份额型整体关系概念是海洋 (cmnwn-09376198-n) 
"""
relations.holo_portion.test.zh = ""
relations.holo_portion.com.zh = ""



### Relation: eq_synonym

relations.eq_synonym.name.zh = "等义关系"
relations.eq_synonym.df.zh = "两个概念意义相同，在同一语境中可以互相替换。"
relations.eq_synonym.dfn.zh = """
等义关系指两个概念意义是等同的，但是在语言中形式不同。\
等义关系是双向的，概念A等同于概念B，则概念B也等同于概念A。\
它表示一种特殊的同义关系，允许同义的词元分别分布在不同的同义词集中。该关系适用于任何词类。\
当前，我们利用此关系来分离汉语中的成语等俗语。
"""

relations.eq_synonym.ex.zh = "欢天喜地 (cmnwn-13986372-n) 的等义关系概念是高兴 (cmnwn-07527352-n) "
relations.eq_synonym.exe.zh = """
* 欢天喜地 (cmnwn-13986372-n) 的等义关系概念是高兴 (cmnwn-07527352-n) 
"""
relations.eq_synonym.test.zh = ""
relations.eq_synonym.com.zh = "原则上，所有语义上等同的词都应属于同一个同义词集（可以通过适当的用法标签来进行区分）。"



### Relation: instance_hypernym

relations.instance_hypernym.name.zh = "实例型上位关系"
relations.instance_hypernym.df.zh = "一个概念是给定的某个实例概念的类。"
relations.instance_hypernym.dfn.zh = """
实例型上位关系指两个概念之间，概念A是概念B实例的类，B是实例。是层级结构中的终端节点。\
实例用专有名词表示。实例型上位关系也可以称为“类“。
"""

relations.instance_hypernym.ex.zh = "北京的实例型上位关系概念是城市 (cmnwn-08665504-n) "
relations.instance_hypernym.exe.zh = """
* 北京的实例型上位关系概念是城市 (cmnwn-08665504-n) 
"""
relations.instance_hypernym.com.zh = "该关系有时会被归入上位/下位关系中。"



### Relation: instance_hyponym

relations.instance_hyponym.name.zh = "实例型下位关系"
relations.instance_hyponym.df.zh = "一个概念是给定的某个类概念的一个实例。"
relations.instance_hyponym.dfn.zh = """
实例型下位关系指两个概念之间，概念B是概念A类中的一个实例，B是实例。是层级结构中的终端节点。\ 
实例用专有名词表示。实例型上位关系'也可以称为“类“。
"""

relations.instance_hyponym.ex.zh = "城市 (cmnwn-08665504-n) 的实例型下位关系概念是北京"
relations.instance_hyponym.exe.zh = """
* 城市 (cmnwn-08665504-n) 的实例型下位关系概念是北京
"""
relations.instance_hyponym.com.zh = """
下位关系是实体与类之间的关系。个体实体也可以说属于某个类。\
尽管我们在词库中找不到很多实例，但是该关系对于想要添加特定实例并且不想查询单独数据库的用户很有用。\
为了区别于类下位关系，该关系称为has_instance。
"""



### Relation: exemplifies

relations.exemplifies.name.zh = "在示例域关系"
relations.exemplifies.df.zh = "一个概念是给定概念的示例。"
relations.exemplifies.dfn.zh = "在示例域关系指两个概念之间，概念A是概念B的示例。"

relations.exemplifies.ex.zh = "邦迪 (cmnwn-02786058-n) 的在示例域关系概念是商标 (cmnwn-05845140-n) "
relations.exemplifies.exe.zh = """
* 邦迪 (cmnwn-02786058-n) 的在示例域关系概念是商标 (cmnwn-05845140-n) 
"""
relations.exemplifies.com.zh = """
该关系的名称由“用途域中的成员”改动而来，因为我们发现它与标准域的意义差距太大。
"""



### Relation: is_exemplified_by

relations.is_exemplified_by.name.zh = "示例域关系"
relations.is_exemplified_by.df.zh = "一个概念是给定概念的类。"
relations.is_exemplified_by.dfn.zh = "示例域关系指两个概念之间，概念B是概念A的类。例如成语，敬语和量词。"

relations.is_exemplified_by.ex.zh = "商标 (cmnwn-05845140-n) 的示例域关系概念是邦迪 (cmnwn-02786058-n) "
relations.is_exemplified_by.exe.zh = """
* 商标 (cmnwn-05845140-n) 的示例域关系概念是邦迪 (cmnwn-02786058-n) 
"""
relations.is_exemplified_by.com.zh = ""



### Relation: domain_topic

relations.domain_topic.name.zh = "主题域关系"
relations.domain_topic.df.zh = "一个概念是给定概念的科学范畴指针。"
relations.domain_topic.dfn.zh = "主题域关系指两个概念之间，概念B是概念A的科学范畴（例如计算机科学、体育、生物等）指针。"

relations.domain_topic.ex.zh = "计算机科学 (cmnwn-06128570-n) 的主题域关系概念是中央处理器 (cmnwn-02995345-n) "
relations.domain_topic.exe.zh = """
* 计算机科学 (cmnwn-06128570-n) 的主题域关系概念是中央处理器 (cmnwn-02995345-n) 
"""
relations.domain_topic.com.zh = ""



### Relation: has_domain_topic

relations.has_domain_topic.name.zh = "在主题域关系"
relations.has_domain_topic.df.zh = "给定科学范畴领域概念中的一个专有概念。"
relations.has_domain_topic.dfn.zh = "在主题域关系指两个概念之间，概念A是概念B科学范畴（例如：计算机科学、体育、生物）领域中的一个专有概念。"

relations.has_domain_topic.ex.zh = "中央处理器 (cmnwn-02995345-n) 的在主题域关系概念是计算机科学 (cmnwn-06128570-n) "
relations.has_domain_topic.exe.zh = """
* 中央处理器 (cmnwn-02995345-n) 的在主题域关系概念是计算机科学 (cmnwn-06128570-n) 
"""
relations.has_domain_topic.com.zh = ""



### Relation: domain_region

relations.domain_region.name.zh = "地区域关系"
relations.domain_region.df.zh = "一个概念是给定概念的地理、文化领域指针。"
relations.domain_region.dfn.zh = "地区域关系指两个概念之间，概念B是概念A的地理、文化领域指针。"

relations.domain_region.ex.zh = "日本的地区域关系概念是寿司"
relations.domain_region.exe.zh = """
* 日本的地区域关系概念是寿司
"""
relations.domain_region.com.zh = ""


### Relation: has_domain_region

relations.has_domain_region.name.zh = "在地区域关系"
relations.has_domain_region.df.zh = "给定概念地理、文化领域中的一个专有概念。"
relations.has_domain_region.dfn.zh = "在地区域关系指两个概念之间，概念A是概念B地理、文化领域中的一个专有概念。"

relations.has_domain_region.ex.zh = "寿司的在地区域关系概念是日本"
relations.has_domain_region.exe.zh = """
* 寿司的在地区域关系概念是日本
"""
relations.has_domain_region.com.zh = ""



### Relation: attribute

relations.attribute.name.zh = "属性关系"
relations.attribute.df.zh = "一个概念是给定概念所具有的特征或属性。"
relations.attribute.dfn.zh = "属性关系指名词概念和形容词概念之间，概念A是概念B的属性。"

relations.attribute.ex.zh = ""
relations.attribute.exe.zh = ""
relations.attribute.test.zh = ""
relations.attribute.com.zh = ""



### Relation: restricts

relations.restricts.name.zh = "限制关系"
relations.restricts.df.zh = "一个概念是给定概念程度、数量或其他方面的限制。"
relations.restricts.dfn.zh = "限制关系指两个概念之间，形容词概念A（数量词/限定词）对名词概念B（指代词）进行限制的关系。"

relations.restricts.ex.zh = ""
relations.restricts.exe.zh = ""
relations.restricts.com.zh = ""



### Relation: restricted_by

relations.restricted_by.name.zh = "受限关系"
relations.restricted_by.df.zh = "一个概念受到给定概念在程度、数量或其他方面的限制。"
relations.restricted_by.dfn.zh = "受限关系指两个概念之间，名词概念B（指代词）受到形容词概念A（数量词/限定词）限制的关系。"

relations.restricted_by.ex.zh = ""
relations.restricted_by.exe.zh = ""
relations.restricted_by.com.zh = ""



### Relation: classifies

relations.classifies.name.zh = "分类关系"
relations.classifies.df.zh = "一个概念是给定概念的量词。"
relations.classifies.dfn.zh = "分类概念指两个概念之间，概念A是概念B的量词，对概念B进行分类。"

relations.classifies.ex.zh = "一匹 (cmnwn-02866286-n) 的分类关系概念是马 (cmnwn-02374451-n) "
relations.classifies.exe.zh = """
* 一匹 (cmnwn-02866286-n) 的分类关系概念是马 (cmnwn-02374451-n) 
* 一把 (cmnwn-13767350-n) 的分类关系概念是枪 (cmnwn-03467984-n) 
"""
relations.classifies.com.zh = "目前该关系仅有名词的连接，不过今后会包含其他词类（如动词）。"



### Relation: classified_by

relations.classified_by.name.zh = "被分类关系"
relations.classified_by.df.zh = "一个概念被给定概念进行了分类，被给定概念划入某个范畴。"
relations.classified_by.dfn.zh = "被分类关系指两个概念之间，概念A被量词概念B进行分类。"

relations.classified_by.ex.zh = "马 (cmnwn-02374451-n) 的被分类关系概念是一匹 (cmnwn-02866286-n) "
relations.classified_by.exe.zh = """
* 马 (cmnwn-02374451-n) 的被分类关系概念是一匹 (cmnwn-02866286-n) 
* 枪 (cmnwn-03467984-n) 的被分类关系概念是一把 (cmnwn-13767350-n) 
"""
relations.classified_by.com.zh = ""



### Relation: also (no ili)

relations.also.name.zh = "另见关系"
relations.also.df.zh = "一个概念与给定概念有松散或模糊的语义关系。"
relations.also.dfn.zh = """
另见关系具有双向性（此关系的两个方向具有相同的含义）—概念A与概念B有关，概念B也与概念A有关。\
它表示一个概念与另一个概念相关联（超越同义和相似性）。\
该关系最初用于关联形容词，但我们对此没有限制，并且我们正在使用该关系来关联所有词类。
"""

relations.also.ex.zh = "农民 (cmnwn-10410996-n) 的另见关系概念是田地 (cmnwn-14514039-n) "
relations.also.exe.zh = """
* 农民 (cmnwn-10410996-n) 的另见关系概念是田地 (cmnwn-14514039-n) 
* 散步 (cmnwn-01959776-v) 的另见关系概念是公园 (cmnwn-08439808-n)
"""
relations.also.test.zh = ""
relations.also.com.zh = "又被成为模糊关系。"


### Relation: antonym

relations.antonym.name.zh = "反义关系"
relations.antonym.df.zh = "一个概念所表达的意义与另一个概念是相反的，这样两个概念互为反义关系。"
relations.antonym.dfn.zh = """
反义关系是双向的，概念A与概念B是反义关系，那么概念B与概念A也为反义关系。\
它表示两个概念之间的任何适当的反义关系。囊括了大多数类型的反义词，包括可分级的反义词（例如：热与冷），\
互补的反义词（例如：优与劣）以及逆向或关系反义词（例如：买与卖）。反义关系可以连接任何词类中的两个词\
-动词（例如，穿与脱）、副词（例如，自然与不自然）、形容词（例如，高级与低级）和名词（例如，催化剂与反催化剂）），\
并且只能将相同词类的概念连接在一起。是意义相反且互不相容的词。
"""

relations.antonym.ex.zh = "南 (cmnwn-13833375-n) 的反义关系概念是北 (cmnwn-13831176-n) "
relations.antonym.exe.zh = """
* 南 (cmnwn-13833375-n) 的反义关系概念是北 (cmnwn-13831176-n) 
* 黑 (cmnwn-00392812-a) 的反义关系概念是白 (cmnwn-00393105-a)
"""
relations.antonym.test.zh = ""
relations.antonym.com.zh = """
反义关系主要是义项之间的关系，但是义项层面的反义关系意味着一种更加松散的同义词集关系，
我们自动添加这种同义词集关系，以供那些还没有义项层面关系的词网使用。
"""



### Relation: entails

relations.entails.name.zh = "蕴涵关系"
relations.entails.df.zh = "如果概念B的动作不能实现，概念A的动作也无法实现；那么概念A蕴涵概念B。"
relations.entails.dfn.zh = "蕴涵关系指两个动作概念之间，（理论上是单向的）如果概念B的动作不能实现，概念A的动作也无法实现；那么概念A蕴涵概念B。此关系在语义上预设/要求，动作概念B必须在动作概念A发生之前或期间发生。"

relations.entails.ex.zh = "做梦 (cmnwn-02118242-v) 的蕴涵关系概念是睡觉 (cmnwn-00017865-v) "
relations.entails.exe.zh = """
* 做梦 (cmnwn-02118242-v) 的蕴涵关系概念是睡觉 (cmnwn-00017865-v) 
"""
relations.entails.test.zh = ""
relations.entails.com.zh = ""



### Relation: is_entailed_by

relations.is_entailed_by.name.zh = "被蕴涵关系"
relations.is_entailed_by.df.zh = "如果概念B的动作不能实现，概念A的动作也无法实现；那么概念B被概念A蕴涵。"
relations.is_entailed_by.dfn.zh = "这是一个用来追踪的关系，使我们能找到什么概念‘可以’蕴涵什么。如果概念A可以被概念B雨涵，那么概念A就使概念B的发生成为可能。"

relations.is_entailed_by.ex.zh = "睡觉 (cmnwn-00017865-v) 的被蕴涵关系概念是做梦 (cmnwn-02118242-v) "
relations.is_entailed_by.exe.zh = """
* 睡觉 (cmnwn-00017865-v) 的被蕴涵关系概念是做梦 (cmnwn-02118242-v) 
"""
relations.is_entailed_by.test.zh = ""
relations.is_entailed_by.com.zh = "普林斯顿词网没有该关系。"


### Relation: other

relations.other.name.zh = "其他关系"
relations.other.df.zh = "用于当前OMW DTD不支持的语义关系类型。"
relations.other.dfn.zh = """
其他关系用于当前OMW DTD不支持的语义关系类型。具体的关系类型可以使用``dc:type``给出：

.. code:: xml

    <SynsetRelation relType="other" dc:type="emotion" target="example-en-1234-n"/>

"""

relations.other.ex.zh = "牧师 (cmnwn-09983572-n) 的其他关系概念是教堂 (cmnwn-03028079-n) "
relations.other.exe.zh = """
* 牧师 (cmnwn-09983572-n) 的其他关系概念是教堂 (cmnwn-03028079-n) 
* 法官 (cmnwn-10225219-n) 的其他关系概念是法庭 (cmnwn-03649459-n) 
"""
relations.other.test.zh = ""
relations.other.com.zh = ""

### Relation: participle

relations.participle.name.zh = "分词关系"
relations.participle.df.zh = "一个概念是从给定概念表示的动词派生出来的形容词。"
relations.participle.dfn.zh = "分词关系指两个概念之间，概念A是一个从概念B动词形式派生而来的形容词。"

relations.participle.ex.zh = ""
relations.participle.exe.zh = ""
relations.participle.test.zh = ""
relations.participle.com.zh = """
该关系未接入NLTK，因此未在OMW 1.0（或据我所知，在任何地方的FCB）中显示。
"""


### Relation: pertainym

relations.pertainym.name.zh = "属于关系"
relations.pertainym.df.zh = "一个概念是属于给定概念的。"
relations.pertainym.dfn.zh = "属于关系指两个概念之间，其中概念A是概念B表示的名词的形容词，或者概念A是概念B所表示的形容词的副词。"

relations.pertainym.ex.zh = ""
relations.pertainym.exe.zh = ""
relations.pertainym.test.zh = ""
relations.pertainym.com.zh = """
该关系是由普林斯顿词网项目创建的。它是为没有反义词的形容词而制定的。\
一个属于关系的同义词集通常仅包含一个词或搭配词，并指向形容词所从属的名词。\
以及副词所从属的形容词。\
`wngloss(7WN) <https://wordnet.princeton.edu/documentation/wngloss7wn>`_.
"""



### Relation: derivation

relations.derivation.name.zh = "派生关系"
relations.derivation.df.zh = "一个概念是给定概念的派生相关形式。"
relations.derivation.dfn.zh = "派生关系指两个概念之间，概念A是概念B的派生相关形式。"

relations.derivation.ex.zh = ""
relations.derivation.exe.zh = ""
relations.derivation.test.zh = ""
relations.derivation.com.zh = """
该关系可能会进一步细化。它包括零形派生。\
通常，它用于具有相同词根形式并在语义上相关的不同词类。\
词网没有规定哪个是基本形式，这种关系是完全可逆的。
"""









