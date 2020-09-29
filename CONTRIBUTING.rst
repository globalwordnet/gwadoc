**How to Contribute to Gwadoc**

I'm really glad you're reading this, because we need volunteer technical writers to help this project come to fruition. Thank you for taking the time to contribute!


The following are  guidelines for contributing to `Gwadoc <https://globalwordnet.github.io/gwadoc/>`_ which is hosted in the gwadoc on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.


If you need to reach us, Our major communication channel is Github. Join our mailing list(Link to be provided)

The documentation primarily uses reStructuredText (RST). This means to get started contributing to the documentation a fair knowledge of Python, RST and some knowledge of linguistics will be required. Here is a quick guide to help you get started with `RST <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_


**Creating Issues**

If you want to request for a new feature to be added to the documentation or modification to existing features use the feature request issue template.
Possible improvements that are independent, rather than complex feature requests — are also labeled:

- **Enhancement**- user-facing improvements that address some usability or functionality need

- ** `Newcomer Friendly issues <https://github.com/globalwordnet/gwadoc/issues>`_ ** - If you're a new developer and you're looking for an easy way to get involved, try one of the issues tagged as newcomer friendly:

These range from very simple to moderately complex, but won't require you to understand the entire documentation or make extensive changes. We try to keep a few of these open for "micro contributions" for GSOD applicants and others looking for an easy-to-intermediate task. If you can't find one you like, ask `fcbond! <https://github.com/fcbond>`_

**Submitting Pull Request (PR)**

Google Season of Doc (GSOD) should submit their contributions to the `GSOD branch <https://github.com/globalwordnet/gwadoc/tree/gsod>`_ other contributors can submit to the `master branch <https://github.com/globalwordnet/gwadoc/pulls>`_

Please submit a Pull Request (PR) with a clear list of what you have done. Also reference the issue number for which the PR fixes. Please follow the documentation style guide, PR template and make sure you write a commit message for each feature.

Small pull requests are fine, but it's best if they can be "complete" in some sense. This means that if the pull request is for adding information about 1 or 2 relations, all the relevant information is included. Furthermore, the pull request should not bundle unrelated changes (e.g., a UI or settings change).

The purpose of these guidelines is to make reviewing the pull request easier . It's easiest when we can clearly see all the relevant changes without other noise and to keep the Git history clean so later we can point to where something changed.

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:
> git commit -m “A paragraph describing what changed and its impact”

**Before opening a PR**

Create a git branch for the issue you are working on, rather than working directly on master.
Rebase your work onto the latest version from master and fix any merge conflicts. (See `README <https://github.com/globalwordnet/gwadoc/blob/master/README.md>`_ for common Git procedures.)

Check that only the relevant files are being changed.
If you have a messy git history, squash your commits to clean it up.

**PR format**

Title your pull request to indicate its purpose. (This will likely be similar to the title of the issue it addresses.)
Include a reference to the issue(s).

If it is a work-in-progress, include [WIP] in the title. Remove this once the PR is complete and ready for review.
Include before-and-after screenshots (or animations) for user interface changes.

**Documentation Convention**

Our documentation project setup can be found in the `README <https://github.com/globalwordnet/gwadoc/blob/master/README.md>`_

Start reading our documentation and you’ll get the hang of it. We optimize for readability
We indent using two spaces
Most of our contributions happen in the doc_en.py file and we generate the html file
When writing consider your readers, as this is an open source software. The goal is to make the documentation readers friendly.

**Relation Style Guide**

===================        ====================================================

Name                       Description
===================        ====================================================
-------------------        ----------------------------------------------------

Relation name              Name of the relation
Short Definition.          The short definition only shows up when the user’mouse
                           hover over the relation name, it is a brief
                           introduction of the relation.
                           1. Use concept A / concept B (A / B) for reference, DO
                           NOT use concept X / concept Y (X / y).
                           2. Use “A is … of B” as the sentence pattern if
                           possible.

Short Example              The short example only shows up when the user’s mouse
                           hover over the relation name, it just shows the
                           examples without links to lexicon.
                           At least 2 examples. If there is no example in the
                           docs, go to related resources or wiki to find more.

Apply to                   Apply to describes the type this relation links to, it
                           has 3 values:
                           synset_synset
                           sense_synset
                           sense_sense
Symbol                     It describes what symbol the user can use to represent
                           this relation.

Reverse relation           Some relations have one counterpart as a mutually
                           reversed relation, if this relation do not have one,
                           this field will be “no reverse relation defined”.
Definition                 Definition describe the full introduction of the
                           relation.
                           1. Use concept A / concept B (A / B) for reference, DO
                           NOT use concept X / concept Y (X / y).
                           2. Use “A relation between two concepts where...” as
                           the sentence pattern if possible.

Example                    Example shows how words are linked in this relation,
                           and each word will also be linked to the lexicon so the
                           user can check the details of that word directly.
                           1. At least 2 examples. If there is no example in the
                           docs, go to related resources or wiki to find more.
                           2. Link the examples to entries in the OMW. Go to below
                           two websites to search for the right sense of an
                           example word:
                           - `<http://compling.hss.ntu.edu.sg/omw/cgi-bin/wn-
                           gridx.cgi>`_
                           - `<https://lr.soh.ntu.edu.sg/omw/omw>`_

                           relations.hypernym.exe.en = """

                           * * <sense: pwn-3.0:07649854-n:meat> * ``hypernym``
                             * <sense: pwn-3.0:07663592-n:beef> *
                           * *edible fruit* ``hypernym`` *pear*
                           * *wordbook* ``hypernym`` *dictionary*

                           """

                           - `Meat
                             <https://lr.soh.ntu.edu.sg/omw/ili/concepts/77100>`_

                           - `Beef:
                             <https://lr.soh.ntu.edu.sg/omw/ili/concepts/77197>`_

Test                       The Test provide a method to justify whether the
                           linguistic data concords with this relation type or
                           not.
                           If there is no test in the docs, go to EuroWordnet
                           general document to see whether there are any EWN tests
                           there.
XML Sample                 XML sample provides the sample code of relations.

Comment                    Note provides some additional info the user may need to
                           know when using Wordnet.

===================        ====================================================


**Other name in specific Project**

The relations may have different names in different projects, and this is a summary of the names referring to the particular relation, we need to review all the names in different projects to ensure the current name is documented.

==============================     ==============================================

Project Specific Names              Description
==============================     ==============================================
------------------------------     ----------------------------------------------

Name in Princeton WordNet.         Go to `Princeton Wordnet Website
                                   <https://wordnet.princeton.edu/>`_ and the
                                   Princeton Wordnet in OMW to check whether the
                                   relation name is correct.
Princeton WordNet Pointer.         Go to `Princeton Wordnet Website
                                   <https://wordnet.princeton.edu/>`_ and the
                                   Princeton Wordnet in OMW to check whether the
                                   relation name is correct.

Name in Euro WordNet               Go to EuroWordnet general document and the
                                   EuroWordnet in OMW to check whether the
                                   relation name is correct.

Name in PlWordNet.                 Go to PlWordNet Relation type mapping to check
                                   whether the name is correct.

PERL WordNet-QueryData             Go to
Module                             https://metacpan.org/pod/WordNet::QueryData


Interlingual Index Node            Go to https://lr.soh.ntu.edu.sg/omw/ili to check
                                   whether the node number is correct.


==============================     ==============================================



**Technical Writer Resources**

`Gwadoc <https://globalwordnet.github.io/gwadoc/>`_

`Princeton Wordnet <https://wordnet.princeton.edu/>`_

`reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_












