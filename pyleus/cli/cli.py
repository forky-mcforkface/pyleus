"""Command-line interface to Pyleus. Routes to differents sub-commands modules
based on arguments provided.
"""
from __future__ import absolute_import

import argparse

from pyleus import __version__
from pyleus.cli.commands.build_subcommand import BuildSubCommand
from pyleus.cli.commands.list_subcommand import ListSubCommand
from pyleus.cli.commands.local_subcommand import LocalSubCommand
from pyleus.cli.commands.submit_subcommand import SubmitSubCommand
from pyleus.cli.commands.kill_subcommand import KillSubCommand


def main():
    parser = argparse.ArgumentParser(
        description="Python layer on top of Storm",
        add_help=False)
    parser.add_argument(
        "-h", "--help", action="help",
        help="Show this message and exit")
    parser.add_argument(
        "-c", "--config", dest="config_file",
        default=None,
        help="Pyleus configuration file")
    parser.add_argument(
        "-v", "--verbose", dest="verbose",
        default=False, action="store_true",
        help="Verbose")
    parser.add_argument(
        "-V", "--version", action="version",
        version="%(prog)s {0}".format(__version__),
        help="Show version number and exit")

    subparsers = parser.add_subparsers(
        title="Commands",
        metavar="COMMAND")
    BuildSubCommand().add_parser(subparsers)
    ListSubCommand().add_parser(subparsers)
    LocalSubCommand().add_parser(subparsers)
    SubmitSubCommand().add_parser(subparsers)
    KillSubCommand().add_parser(subparsers)

    args = parser.parse_args()

    args.func(args)
