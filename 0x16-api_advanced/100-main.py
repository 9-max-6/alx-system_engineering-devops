#!/usr/bin/python3
"""
100-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    
    a = 'programming'
    b = ['python', 'java', 'javascript', 'scala', 'no_results_for_this_one', 'is', 'the', 'is']
    result = count_words(a, b)