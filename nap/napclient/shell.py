#coding:utf-8
"""
Command-line interface to the Nap API.
"""

import sys

from nap.lib import argparse


import nap.napclient
from nap.napclient import logger
from nap.napclient.v1 import shell as shell_v1
from nap.napclient import utils
from nap.napclient import client



class NapShell(object):
    """ NapShell  """
    def get_base_parser(self):
        parser = NapClientArgumentParser(
            prog='nap',
            description=__doc__.strip(),
            epilog='See "nap help COMMAND" '
                   'for help on a specific command.',
            add_help=False,
            formatter_class=NapHelpFormatter,
        )
        
        # Global arguments
        parser.add_argument('-h', '--help',
            action='store_true',
            help=argparse.SUPPRESS,
        )
        
        parser.add_argument('-v','--version',
                            action='version',
                            version="0.0.1")
        
        parser.add_argument('-d','--debug',
            default=False,
            action='store_true',
            help="Print debugging output")
        
        return parser
    
    def get_subcommand_parser(self,version):
        parser = self.get_base_parser()
        self.subcommands = {}
        subparsers = parser.add_subparsers(metavar='<subcommand>')
        
        actions_module = shell_v1
        self._find_actions(subparsers, actions_module,startswith="sub",has_subcommand=True)
        self._find_actions(subparsers, actions_module)
        self._find_actions(subparsers, self)
        
  
        return parser
    
    def _find_actions(self, subparsers, actions_module,startswith="do",has_subcommand=False):
        startlen = len(startswith) + 1
        for attr in (a for a in dir(actions_module) if a.startswith(startswith)):
            # I prefer to be hyphen-separated instead of underscores.
            command = attr[startlen:].replace('_', '-')
            callback = getattr(actions_module, attr)
            desc = callback.__doc__ or ''
            action_help = desc.strip()
            arguments = getattr(callback, 'arguments', [])
            
            subparser = subparsers.add_parser(command,
                help=action_help,
                description=desc,
                add_help=False,
                formatter_class=NapHelpFormatter
            )
            subparser.add_argument('-h', '--help',
                action='help',
                help=argparse.SUPPRESS,
            )
            if startswith != "do" and startswith != "sub":
                self.subcommands[attr[:].replace('_', '-')] = subparser
            else:
                self.subcommands[command] = subparser
            
            if has_subcommand:
                sub = self.subcommands[command].add_subparsers(metavar='<subcommand>')
                self._find_actions(sub, actions_module,startswith=attr[startlen:])
            else:
                for (args, kwargs) in arguments:
                    subparser.add_argument(*args, **kwargs)
                subparser.set_defaults(func=callback)
        
        
    
    def setup_debugging(self, debug):
        if not debug:
            return
        nap.napclient.start_debugging()
        
    
    def main(self, argv):
        
        parser = self.get_base_parser()
        (options, args) = parser.parse_known_args(argv)
        
        self.setup_debugging(options.debug)

        subcommand_parser = self.get_subcommand_parser("v1")
        self.parser = subcommand_parser
        
        if options.help or not argv:
            subcommand_parser.print_help()
            return 0
        
        args = subcommand_parser.parse_args(argv)

        if args.func == self.do_help:
            self.do_help(args)
            return 0
        
        cs = client.Client("1")
        args.func(cs,args)
        
    
    @utils.arg('command', metavar='<subcommand>', nargs='*',
                    help='Display help for <subcommand>')
    def do_help(self, args):
        """
        Display help about this program or one of its subcommands.
        """  
        if args.command:
            if len(args.command) > 1:
                command = args.command[0] +"-" + args.command[1]
            else:
                command = args.command[0]
            if command in self.subcommands:
                self.subcommands[command].print_help()
            else:
                print(("'%s' is not a valid subcommand") %
                                       args.command)
        else:
            self.parser.print_help()

class NapClientArgumentParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(NapClientArgumentParser, self).__init__(*args, **kwargs)

    def error(self, message):
        """error(message: string)

        Prints a usage message incorporating the message to stderr and
        exits.
        """
        self.print_usage(sys.stderr)
        choose_from = ' (choose from'
        progparts = self.prog.partition(' ')
        self.exit(2, "error: %(errmsg)s\nTry '%(mainp)s help %(subp)s'"
                     " for more information.\n" %
                     {'errmsg': message.split(choose_from)[0],
                      'mainp': progparts[0],
                      'subp': progparts[2]})


class NapHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=52,
                 width=None):
        super(NapHelpFormatter, self).__init__(prog, indent_increment,
              max_help_position, width)

    def start_section(self, heading):
        # Title-case the headings
        heading = '%s%s' % (heading[0].upper(), heading[1:])
        super(NapHelpFormatter, self).start_section(heading)




def main():
    NapShell().main(sys.argv[1:])
#    while True:
#        args = raw_input().split()
#        NapShell().main(args[1:])


if __name__ == "__main__":
    main()