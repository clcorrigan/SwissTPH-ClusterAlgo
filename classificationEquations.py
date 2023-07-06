import pandas as pd
from Levenshtein import distance as lev
from math import floor, ceil 


global lev_thresh; global jar_thresh; global n_thresh; 
lev_thresh = 0.5
jar_thresh = 0.5
n_thresh = 0.5

jar_distances = []
lev_ratios = []
n_sim_values = [] 


def pass_fail(ratio, threshold):
    if(ratio >= threshold):
        return False 
    else: 
        return True

def compare_with_lev(string1, string2):
    """
    Comparing the two strings with the Lev package/library. 
    Calls the pass/fail function and returns whether the value has passed or failed. 
    """
    string1 = string1.lower() 
    string2 = string2.lower()
    dist = lev(string1, string2)
    max_len = max(len(string1),len(string2))
    ratio = dist/max_len
    lev_ratios.append(ratio)
    passing = pass_fail(ratio, lev_thresh)

def compare_with_jar(string1, string2):
    """
    
    """
    s1 = string1.lower()
    s2 = string2.lower() 

    max_dist = floor(max(len(s1), len(s2))/2)-1
    match = 0

    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)

    for i in range(len(s1)):
        for j in range (max(0, i - max_dist), min(len(s2), i+max_dist + 1)):
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1 
                match += 1 
                break 
    if (match == 0):
        return 0.0
    
    t = 0 
    point = 0 

    for i in range(len(s1)):
        if (hash_s1[i]):
            while(hash_s2[point] == 0):
                point += 1 
            if (s1[i] == s2[point]):
                t+=1
            point +=1
    t = t//2

    # getting the Jaro Similarity
    similarity = (match/len(s1) + match/len(s2) + (match-t)/match)/3.0

    # getting the Jaro Distance
    dist = 1 - similarity 
    return pass_fail(dist, jar_thresh)


print(compare_with_jar("Allergic Rash", "Allargic Rash"))

    