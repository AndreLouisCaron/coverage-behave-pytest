# -*- coding: utf-8 -*-

Feature: run as a command-line too

  Scenario: run standalone
    When I run "cli --help"
    Then I see "usage: cli"

  Scenario: run as Python module
    When I run "python -m cli --help"
    Then I see "usage: cli"
