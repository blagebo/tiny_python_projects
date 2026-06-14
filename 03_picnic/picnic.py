#!/usr/bin/env python3
"""
Author : blagebo
Date   : 14-06-2026
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        nargs="+",
                        metavar='str',
                        help='Item(s) to bring')
    
    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        metavar='bool',
                        type=bool,
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The mainly main"""

    args = get_args()
    flag_arg = args.sorted
    pos_arg = args.items[0]

    #print(f'str_arg = "{str_arg}"')
    #print(f'int_arg = "{int_arg}"')
    #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    #print(f'flag_arg = "{flag_arg}"')
    print(f'You are bringing {pos_arg}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()

