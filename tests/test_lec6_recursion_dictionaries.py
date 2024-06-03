import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89

# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
def test_18_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89

def test_18_is_palindrome():
    assert lec6.is_palidrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

def test_most_common_words():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
    'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
        
    'you', 'think', "you've", 'lost', 'your', 'love',
    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
    "it's", 'you', "she's", 'thinking', 'of',
    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
    
    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'she', 'said', 'you', 'hurt', 'her', 'so',
    'she', 'almost', 'lost', 'her', 'mind',
    'and', 'now', 'she', 'says', 'she', 'knows',
    "you're", 'not', 'the', 'hurting', 'kind',
    
    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    
    'you', 'know', "it's", 'up', 'to', 'you',
    'i', 'think', "it's", 'only', 'fair',
    'pride', 'can', 'hurt', 'you', 'too',
    'pologize', 'to', 'her',
    
    'Because', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'Yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'yeah', 'yeah', 'yeah',
    'yeah', 'yeah', 'yeah', 'yeah'
    ]

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(she_loves_you)) == (['you'], 36)
    assert lec6.is_palindrome('cookieliileikooc') == True

import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    
def test_is_palindrome():   
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

def test_1_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89 
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 233
    assert lec6.fib(13) == 377
    


fuchengguo = ['wuo','due','ni','i','i','i','bu','wan']
beatles = lec6.lyrics_to_frequencies(fuchengguo)
def test_lyrics_to_frequencies():
    assert lec6.lyrics_to_frequencies(fuchengguo) == {'wuo': 1, 'due': 1, 'ni': 1, 'i': 3, 'bu': 1, 'wan': 1}
def test_most_common_words():
    assert lec6.most_common_words(beatles) == (['i'], 3)
def test_words_often():
    assert lec6.words_often(beatles, 3) == [(['i'], 3)]
    assert lec6.words_often(beatles, 2) == []
        


def test_most_common_words():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
    'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
        
    'you', 'think', "you've", 'lost', 'your', 'love',
    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
    "it's", 'you', "she's", 'thinking', 'of',
    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
    
    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'she', 'said', 'you', 'hurt', 'her', 'so',
    'she', 'almost', 'lost', 'her', 'mind',
    'and', 'now', 'she', 'says', 'she', 'knows',
    "you're", 'not', 'the', 'hurting', 'kind',
    
    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    
    'you', 'know', "it's", 'up', 'to', 'you',
    'i', 'think', "it's", 'only', 'fair',
    'pride', 'can', 'hurt', 'you', 'too',
    'pologize', 'to', 'her',
    
    'Because', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'Yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'yeah', 'yeah', 'yeah',
    'yeah', 'yeah', 'yeah', 'yeah'
    ]

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(she_loves_you)) == (['you'], 36)
    assert lec6.is_palindrome('cookieliileikooc') == True


# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89


# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

def test_18_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89

def test_18_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

def test_1_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
    assert lec6.is_palindrome('cookieliileikooc') == True
    

def test_1_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 233
    assert lec6.fib(13) == 377
        
    











def test_most_common_words():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
    'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
        
    'you', 'think', "you've", 'lost', 'your', 'love',
    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
    "it's", 'you', "she's", 'thinking', 'of',
    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
    
     'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'she', 'said', 'you', 'hurt', 'her', 'so',
    'she', 'almost', 'lost', 'her', 'mind',
    'and', 'now', 'she', 'says', 'she', 'knows',
    "you're", 'not', 'the', 'hurting', 'kind',
    
    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    
    'you', 'know', "it's", 'up', 'to', 'you',
    'i', 'think', "it's", 'only', 'fair',
    'pride', 'can', 'hurt', 'you', 'too',
    'pologize', 'to', 'her',
    
    'Because', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'Yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
    
    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'yeah', 'yeah', 'yeah',
    'yeah', 'yeah', 'yeah', 'yeah'
    ]

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(she_loves_you)) == (['you'], 36)
    assert lec6.is_palindrome('cookieliileikooc') == True
