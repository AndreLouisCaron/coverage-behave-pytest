# -*- coding: utf-8 -*-


def before_scenario(context, scenario):
    scenario.shell_commands = []


def after_scenario(context, scenario):
    del scenario.shell_commands
