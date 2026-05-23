#!/usr/bin/env python3
"""
Author : blagebo
Date   : 30-04-2026
Purpose: solution to crowsnest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crowsnest - choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    parser.add_argument('-s',
                        '--side',
                        help='A side string argument',
                        metavar='str',
                        type=str,
                        default='larboard')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    valid_side = ['larboard', 'starboard']
    #article = ''
    #if word[0].lower() in 'aeiou':
    #    article = 'an'
    #else:
    #    article = 'a' 
    article = 'An' if word[0] in 'AEIOU' else 'an' if word[0] in 'aeiou' else 'a' if word[0]!=word[0].upper() else 'A'
    
    #print('Ahoy, Captain, ' + article + ' ' + word + ' off the larboard bow!')
    #print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))
    
    if side in valid_side:
        if word.isalpha():
            print(f'Ahoy, Captain, {article} {word} off the {side} bow!')
        else:
            print('invalid word')
    else:
        print('invalid side')
# --------------------------------------------------
if __name__ == '__main__':
    main()

