def match(command, settings):
    return ('rm:' in command.stderr
	and 'is a directory' in command.stderr.lower())


def get_new_command(command, settings):
    return 'rm -rf' + command.script[2:]
