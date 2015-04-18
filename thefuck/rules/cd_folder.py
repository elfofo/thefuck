# Adds the missing space between the cd command and the target directory
#
# Does not really save chars, but is fun :D
#
# Example:
# > cd..
# cd..: command not found
import re
from thefuck.utils import which, wrap_settings

local_settings = {'command_not_found': '/usr/lib/command-not-found'}

@wrap_settings(local_settings)
def match(command, settings):
    return 'cd' in  command.stderr and settings.command_not_found in command.stderr


@wrap_settings(local_settings)
def get_new_command(command, settings):
    return command.script[:2] + ' ' + command.script[2:]
