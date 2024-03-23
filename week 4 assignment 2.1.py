def get_length(dna):
    return len(dna)
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """



def is_longer(dna1, dna2):
    return len(dna1) > len(dna2) and len(dna1) != len(dna2)
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """


def count_nucleotides(dna, nucleotide):
    return dna.count(nucleotide)
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

                      

def contains_sequence(dna1, dna2):
    if dna2 in dna1:
        return True
    else:
        return False
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    '''


def is_valid_sequence(dna):
    nucleotides='AGTC'
    for char in dna:
        if char in nucleotides and dna == nucleotides:
            return True
        else:
            return False

    
    '''(str)-> bool
    Returns true if and only if DNA sequence is valid
    >>>is_valid_sequence('AGCTC')
    True
    >>>is_valid_sequence('ABTGCT')
    False
    '''



def insert_sequence(dna1,dna2,index):
    return dna1[:index] + dna2 + dna1[index:]
    '''(str, str, int) -> str
    Return the DNA sequence obtained by inserting dna2 into dna1 at the specified index
    >>>insert_sequence(AGTC,ATCG,2)
    AGATCGTC
    >>>insert_sequence(ATGC,CCTA,3)
    ATGCCCTATC
    '''


def get_complement(nucleotides):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[nucleotide] for nucleotide  in nucleotides])
    '''(str) -> str
    Return the complement of the DNA sequence
    >>>get_complement('A')
    'T'
    >>>get_complement('G')
    'C'
    '''

def get_complementary_sequence(dna):
    return get_complement(dna) 
    '''(str) -> str
    Return the complement of the DNA sequence
    >>>get_complementary_sequence('AGT')
    'TCA'
    >>>get_complementary_sequence('ATA')
    'TAT'
    '''