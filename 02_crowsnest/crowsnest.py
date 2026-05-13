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

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    
    #article = ''
    #if word[0].lower() in 'aeiou':
    #    article = 'an'
    #else:
    #    article = 'a' 
    article = 'An' if word[0] in 'AEIOU' else 'an' if word[0] in 'aeiou' else 'a' if word[0]!=word[0].upper() else 'A'
    
    #print('Ahoy, Captain, ' + article + ' ' + word + ' off the larboard bow!')
    #print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()

