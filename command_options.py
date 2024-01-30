from enum import Enum
from build import Build

class Options():

    def __init__(self):
        # Commands
        self.commands = {self.Commands.HELP : self.help, self.Commands.BUILD : self.build}
        # Builds
        self.url = 'https://lost-ark.maxroll.gg/build-guides/'
        self.build = Build()
        #

    class Commands(Enum, str):
        HELP = 'help'
        BUILD = 'build'

    def build(self, advanced_class, type_build):
        result = self.url + '-' + self.build.advanced_classes.get(advanced_class, '') + '-' + self.build.types.get(type_build, '') + 'guide' 
        return result

    def help():
        return ''

    def error():
        return ''

    def process_command(self, command):
        try:
            if command in self.commands:
                self.commands[command](command)
            else:
                raise Exception()
        except:
            self.error(command)
