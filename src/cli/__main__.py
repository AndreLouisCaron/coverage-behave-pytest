# -*- coding: utf-8 -*-


import argparse
import os.path
import sys


def dirpath(path):
    """Custom type for ``argparse``: path to directory."""
    if not os.path.isdir(path):
        raise ValueError  # not exercised by `behave` features.
    return os.path.abspath(path)


def make_parser():
    parser = argparse.ArgumentParser('cli')
    parser.add_argument('--dir', type=dirpath)
    return parser


def main(argv=None):
    args = vars(make_parser().parse_args(argv))
    print('ARGS:', args)


if __name__ == '__main__':  # pragma: no cover
    main(sys.argv[1:])
