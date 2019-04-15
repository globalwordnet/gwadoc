# gwadoc

This package has two main uses:

1. To provide user-facing
   [documentation](https://globalwordnet.github.io/gwadoc) of things
   like relations and parts of speech used by wordnets.
2. To provide a Python API for querying this documentation, such as
   for retrieving the localized name or definition for specific
   relations.

# Installation

You can use `pip` to install gwadoc (use of a virtual environment is
strongly recommended; see [here][virtualenv]). The minimum Python
version is 3.5. As gwadoc is not on [PyPI](https://pypi.org/), you can
give the GitHub URL to `pip`:

``` bash
~$ pip install git+git://github.com/globalwordnet/gwadoc.git
```

... or clone the repository and install from your local copy:

``` bash
~$ git clone https://github.com/globalwordnet/gwadoc.git
~$ cd gwadoc/
~/gwadoc$ pip install .
```

To mark gwadoc as a dependency for your project, just put the
`git+git://github.com/globalwordnet/gwadoc.git` URL in your
`requirements.txt` file or the appropriate place in your `setup.py`
file.

To install the requirements for building the documentation, use the
`[build]` extra. For example, when installing from a local copy:

``` bash
~/gwadoc$ pip install .[build]
```

[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

# Usage

To use gwadoc in your Python code
Then you can use it like this:

``` python
>>> import gwadoc
>>> for relname in gwadoc.RELATIONS[:5]:
...     print(relname, '\n   ', gwadoc.relations[relname].df.en)
... 
constitutive
    Core semantic relations that define synsets
hyponym
    a word that is more specific than a given word
hypernym
    a word that is more general than a given word
instance_hyponym
    an occurrence of something
instance_hypernym
    the type of an instance
```

Where `gwadoc.RELATIONS` is the inventory of relation names, and
`gwadoc.relations` is the data structure containing documentation
about each relation. For each relation, there are several fields:

| Field  | Description            |
| ------ | ---------------------- |
| `df`   | short definition       |
| `dfn`  | long definition        |
| `ex`   | short example          |
| `exe`  | more examples          |
| `fa`   | formal attributes      |
| `name` | relation name          |
| `proj` | project-specific names |
| `test` | linguistic tests       |

For the formal attributes and project names that are available, see
[`gwadoc.inventories`](gwadoc/inventories.py). The data structure
may be accessed (and defined) using dot-notation or index-notation:

``` python
>>> print(gwadoc.relations.hypernym.name)
Hypernym
>>> print(gwadoc.relations['hypernym']['name'])
Hypernym
```

String fields, such as `df`, `ex`, `name`, `test`, etc. use the
`gwadoc.base.MultiString` class (see [`gwadoc.base`](gwadoc/base.py))
so that projects may provide these fields in their own language. The
language may be requested directly, or the default language may be
specified by calling the `gwadoc.set_preferred_language()` function:

``` python
>>> gwadoc.relations.hypernym.name
<MultiString (Hypernym)>
>>> gwadoc.relations.hypernym.name.ja
'上位語'
>>> gwadoc.set_preferred_language('ja')
>>> gwadoc.relations.hypernym.name
<MultiString (上位語)>
```

# Building the Documentation

After installing the requirements, you can build the HTML documentation:

``` bash
~/gwadoc$ python docs/build.py html > docs/index.html
```

Note: if you installed the requirements in a virtual environment make
sure you activate it before building the documentation.

# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Global Wordnet Association Documentation</span>
by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">GWA Documentation Working Group</span>
is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
