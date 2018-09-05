===========================================
  combined coverage for behave and pytest
===========================================

Goal
====

When trying to use behave_ in a new command-line tool project, I
quickly ended up with some code paths that are quite difficult to
test.  I thought I could simply add some unit tests using pytest_ and
combine the coverage, but I hit a snag.

This project merely attemps at reproducing that issue in order to
share the recipe and get some help finding a functional solution.

.. _behave: https://behave.readthedocs.io/
.. _pytest: https://docs.pytest.org/

How to use this project
=======================

Run ``tox``.  If everything passes, you do not experience the issue.

On my machine, the ``coverage report -m --fail-under=100`` command
fails and produces this output::

   py36 runtests: commands[5] | coverage report -m --fail-under=100
   Name                                          Stmts   Miss Branch BrPart  Cover   Missing
   -----------------------------------------------------------------------------------------
   .tox\py36\Lib\site-packages\cli\__init__.py       0      0      0      0   100%
   .tox\py36\Lib\site-packages\cli\__main__.py      16      7      4      2    55%   12, 17-19, 23-24, 28, 11->12, 27->28
   src\cli\__init__.py                               0      0      0      0   100%
   src\cli\__main__.py                              16      5      4      1    60%   11-13, 24, 28, 27->28
   -----------------------------------------------------------------------------------------
   TOTAL                                            32     12      8      3    58%

Somehow, the same files appear as both ``.tox/...`` and ``src/``.
From what I can tell in the coverage output, the ``behave`` run
produces paths like ``.tox/...`` and the ``pytest`` run produces
paths like ``src/``.

Note that this recipe uses the accumulation feature to build the data file.

(See `data file`_.)

According to the ``coverage`` documentation, we should be able to describe path equivalencies like this in our ``.coveragerc``::

   [paths]
   source =
     src/cli
     .tox/*/Lib/site-packages/cli

(See `combining data files`_.)

However, this seems to only apply to ``coverage combine``.

.. _`data file`: https://coverage.readthedocs.io/en/coverage-4.2/cmd.html#data-file
.. _`combining data files`: https://coverage.readthedocs.io/en/coverage-4.2/cmd.html#combining-data-files
