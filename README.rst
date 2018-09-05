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


