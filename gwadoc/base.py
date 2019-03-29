# -*- coding: utf-8 -*-

from gwadoc.inventories import (
    PROJECTS,
    LANGUAGES,
    SENSE_RELATIONS,
    SYNSET_RELATIONS,
    PARTS,
    FORMAL_ATTRIBUTES
)


preferred_language = 'en'


###############################################################################
### Data Structures

class AttrBase(dict):

    _inventory = set()

    def __getitem__(self, key):
        if key not in self._inventory:
            raise KeyError("'{}' is not defined".format(key))
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        if key not in self._inventory:
            raise KeyError("'{}' is not defined".format(key))
        dict.__setitem__(self, key, value)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'{}' is not defined".format(key))

    def __setattr__(self, key, value):
        try:
            self[key] = value
        except KeyError:
            raise AttributeError("'{}' is not defined".format(key))

    def keys(self):
        return self._inventory

    def __bool__(self):
        return any(self.get(key) for key in self._inventory)


class MultiString(AttrBase):

    _inventory = LANGUAGES

    def __repr__(self):
        return '<MultiString ({!s})>'.format(self)

    def __str__(self):
        return self.get(preferred_language, self.get('en', ''))

    def __len__(self):
        return len(str(self))

    def __bool__(self):
        return bool(str(self))


class FormalAttributes(AttrBase):

    _inventory = FORMAL_ATTRIBUTES

    def __init__(self):
        for fa in self._inventory:
            setattr(self, fa, None)


class Projects(AttrBase):

    _inventory = PROJECTS

    def __init__(self):
        for proj in self._inventory:
            setattr(self, proj, None)


class Parts(AttrBase):

    _inventory = PARTS

    def __init__(self):
        self.com = MultiString()
        self.df = MultiString()
        self.dfn = MultiString()
        self.ex = MultiString()
        self.exe = MultiString()
        self.fa = FormalAttributes()
        self.name = MultiString()
        self.proj = Projects()
        self.test = MultiString()


class Relations(AttrBase):

    def __init__(self, inventory):
        object.__setattr__(self, '_inventory', inventory)
        for rel in self._inventory:
            setattr(self, rel, Parts())

    def hierarchy(self):
        """
        Return the relation hierarchy.

        The hierarchy is built with nodes of the form:

            (relation, [children])
        """
        d = self._build_child_dict()
        def _expand(ids):
            return [(rel_id, _expand(d.get(rel_id, []))) for rel_id in ids]
        return (None, _expand(d[None]))

    def hierarchy_with_reversals(self):
        d = self._build_child_dict()
        seen = set()
        def _expand(ids):
            children = []
            for rel_id in ids:
                if rel_id in seen:
                    continue
                children.append((rel_id,
                                 self[rel_id].fa.reverse,
                                 _expand(d.get(rel_id, []))))
                seen.add(rel_id)
                seen.add(self[rel_id].fa.reverse)
            return children
        h = (None, None, _expand(d[None]))
        if seen.difference([None]) != set(self._inventory):
            raise ValueError('asymmetric hierarchy with reversals')
        return h

    def _build_child_dict(self):
        d = {}
        for rel_id in self._inventory:
            d.setdefault(self[rel_id].fa.parent, []).append(rel_id)
        return d
