How to Contribute to Gwadoc
===========================

Thank you for contributing to the `Global WordNet Association Documentation <https://globalwordnet.github.io/gwadoc>`_!

The documentation primarily uses reStructuredText (ReST). This means to get started contributing to the documentation a fair knowledge of Python, ReST and some knowledge of linguistics will be required. Here is a quick guide to help you get started with `ReST. <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_


Creating Issues
===============
Feel free to raise issues if you want to request for a new feature to be added to the documentation or make modifications to existing features.


Submitting Pull Request (PR)
============================

We're happy to receive pull requests to the  `master branch <https://github.com/globalwordnet/gwadoc/pulls>`_

If you're not sure how to submit pull requests, here are a few resources:

* `How Write Good Commit Messages: A Practical Git Guide <https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/>`_
* `How to Write the Perfect Pull Request <https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/>`_
* `ProGit 6.2: GitHub -- Contributing to a Project <https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project>`_

Please keep pull requests minimal and specific to the issue they are addressing, and give them a clear description. Those containing irrelevant files (such as generated HTML files) or changes may be rejected.

Documentation Convention
=========================

Our documentation project setup can be found in the `README. <https://github.com/globalwordnet/gwadoc/blob/master/README.md>`_

Most of our contributions happen in the ``doc_en.py`` file and we generate the html files from this automatically.

When writing please consider your readers, we would like the documentation reader friendly for beginners as well as useful for experts.

How to add a new relation
=========================

Documentation for a new relation should be done after discussing the relation with the documentation group.

- Add an issue suggesting what should be added
- Add the relations to RELATIONS in ``inventories.py``
- Add basic information about the relations to ``doc_basic.py``
- Add documentation to (at least) ``doc_en.py``

How to add documentation for a new language
============================================

Documentation for a new language can be done by:

 * Add the language to LANGUAGES in ``inventories.py``
 * Create a new language file with ``scripts\addlang.py``
   * Currently you have to add the language and wordnet into the script by hand
 * Add translated information to the file  ``doc_{lang}.py``
   * Start off with relation names, short examples and short
     definitions for the constitutive relations
 * When the core information is added, add the language to the build
   script ``.github/workflows/build.py``


Relation Style Guide
=====================

- **Relation Name** :  The name of the relation

- **Short Definition** : The short definition is a brief introduction of the relation, usually a single sentence.

1. Use concept A / concept B (A / B) for reference, DO NOT use concept X / concept Y (X /y).

2. Use “A is … of B” as the sentence pattern if possible.

- **Short Example** : The short example just shows the examples links to lexicon. At least 2 examples. If there is no example in the docs, go to the `docs/pdf <https://github.com/globalwordnet/gwadoc/tree/master/docs/pdf>`_ folder for related resources or `wiki <https://en.wikipedia.org/wiki/Holonymy>`_ to find more.

- **Apply to** : Apply to describes the type this relation links to, it has 3 values:
    - synset_synset
    - sense_synset
    - sense_sense

- **Symbol** : It describes what symbol the user can use to represent this relation.

- **Reverse Relation** : Some relations have one counterpart as a mutually reversed relation, if this relation do not have one, this field will be “no reverse relation defined”.

- **Definition** : Definition describe the full introduction of the relation.

1. Use concept A / concept B (A / B) for reference, DO NOT use concept X / concept Y (X / y).

2. Use “A relation between two concepts where...” as the sentence pattern if possible.

- **Example** : Example shows how words are linked in this relation, and each word will also be linked to the lexicon so the user can check the details of that word directly.

1. At least 2 examples. If there is no example in the docs, go to related resources or wiki to find more.

2. Link the examples to entries in the OMW. Go to below two websites to search for the right sense of an example word:

- http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-gridx.cgi

- https://lr.soh.ntu.edu.sg/omw/omw

relations.holonym.exe.en = """
 * `eye <ILIURL/64868>`_ has part-holonym `face <ILIURL/87210>`_
 * `planet <ILIURL/85986>`_ has member-holonym `solar system <ILIURL/86215>`_
 * `kibibyte <ILIURL/108305>`_ has part-holonym `mebibyte <ILIURL/108309>`_

"""

Meat: https://lr.soh.ntu.edu.sg/omw/ili/concepts/77100

Beef: https://lr.soh.ntu.edu.sg/omw/ili/concepts/77197

- **Test** : The Test provide a method to justify whether the linguistic data concords with this relation type or not. If there is no test in the docs, go to EuroWordnet general document to see whether there are any EWN tests there.

- **XML Sample** :  XML sample provides the sample code of relations.

- **Comment** : Comment provides some additional info the user may need to know when using Wordnet.


Other name in specific Project
==============================

The relations may have different names in different projects, and this is a summary of the names referring to the particular relation, we need to review all the names in different projects to ensure the current name is documented.

+-------------------------------+-------------------------------------+
| Name                          | Description                         |
+===============================+=====================================+
| Name in Princeton WordNet     | Go to `Princeton Wordnet Website`_  |
|                               | and the Princeton Wordnet in OMW to |
|                               | check whether the relation name is  |
|                               | correct.                            |
+-------------------------------+-------------------------------------+
| Princeton WordNet Pointer     | Go to `Princeton Wordnet Website`_  |
|                               | and the Princeton Wordnet in OMW to |
|                               | check whether the relation name is  |
|                               | correct.                            |
+-------------------------------+-------------------------------------+
| Name in Euro WordNet          | Go to `EuroWordnet general          |
|                               | document`_ and the EuroWordnet in   |
|                               | OMW to check whether the relation   |
|                               | name is correct.                    |
+-------------------------------+-------------------------------------+
| Name in PlWordNet             | Go to `PlWordNet Relation type      |
|                               | mapping`_ to check whether the name |
|                               | is correct.                         |
+-------------------------------+-------------------------------------+
| PERL WordNet-QueryData Module | Go to `PERL WordNet-QueryData       |
|                               | Module`_                            |
+-------------------------------+-------------------------------------+
| Interlingual Index Node       | Go to `Interlingual Index Node`_ to |
|                               | check whether the node number is    |
|                               | correct.                            |
+-------------------------------+-------------------------------------+

.. _Princeton Wordnet Website: https://wordnet.princeton.edu/
.. _EuroWordnet general document: https://pdfs.semanticscholar.org/bc4a/c927ebcc02d778f8c7f9745eea7c81300d89.pdf
.. _PlWordNet Relation type mapping: https://docs.google.com/spreadsheets/d/1CQi97xVICyF0Ek8_RkUkSlD4UgTJUOxYcft_A7DyeMg/edit?ts=5f60b33b#gid=304465341
.. _PERL WordNet-QueryData Module: https://metacpan.org/pod/WordNet::QueryData
.. _Interlingual Index Node: https://lr.soh.ntu.edu.sg/omw/ili


Happy Contributing ! ❤️
