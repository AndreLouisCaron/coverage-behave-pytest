# -*- coding: utf-8 -*-

import shlex
import subprocess
import testfixtures

from behave import (
    then,
    when,
)
from cli.__main__ import main


@when('I run "{command}"')
def run(context, command):
    """Run a shell command (in-process if it's our own tool)."""
    command = shlex.split(command, posix=True)
    if command[0] == 'cli':
        status = 0
        with testfixtures.OutputCapture() as output:
            try:
                main(command[1:])
            except SystemExit as error:
                status = error.args[0]
        output = output.captured
    else:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output, _ = process.communicate()
        output = output.decode('utf-8')
        status = process.returncode
    context.scenario.shell_commands.append({
        'command': command,
        'output': output,
        'status': status,
    })


@then('I see "{text}"')
def see(context, text):
    """Search output of the last command for a given substring."""
    execution = context.scenario.shell_commands[-1]
    output = execution['output']
    if text not in output:
        raise Exception('"%s" not found in """%s"""!' % (
            text,
            output,
        ))
