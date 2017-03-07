from collections import *

def ransom_note(magazine, ransom):
    '''

    :param magazine: a list of words in the magzine
    :param ransom: a list of words in the ransom
    :return: 1 or 0
    '''
    # m, the num_words in magazine
    # n, the num of words in random note
    mag_dic=Counter(magazine)
    random_dic=Counter(ransom)
    for word in random_dic:
        try:
            count_mag=mag_dic[word]
        except:
            return 0
        if count_mag < random_dic[word]:
            return 0
    return 1



m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"