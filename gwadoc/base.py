# -*- coding: utf-8 -*-

from gwadoc.inventories import (
    PROJECTS,
    LANGUAGES,
    RELATIONS,
    PARTS,
    FORMS
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
        return any(self.get(key) is not None for key in self._inventory)


class MultiString(AttrBase):

    _inventory = LANGUAGES

    def __repr__(self):
        return '<MultiString ({!s})>'.format(self)

    def __str__(self):
        return self.get(preferred_language, self.get('en', '---'))

    def __len__(self):
        return len(str(self))


class Forms(AttrBase):

    _inventory = FORMS

    def __init__(self):
        for form in self._inventory:
            setattr(self, form, None)


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
        self.form = Forms()
        self.name = MultiString()
        self.proj = Projects()
        self.test = MultiString()


class Relations(AttrBase):

    _inventory = set(RELATIONS)

    def __init__(self):
        for rel in self._inventory:
            setattr(self, rel, Parts())


rels = Relations()
