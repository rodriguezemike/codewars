#https://www.codewars.com/kata/585894545a8a07255e0002f1/python

from itertools import permutations

def count_patterns_from(firstPoint, length):
    if length > 9 or length < 1:
        return 0
    elif length == 1:
        return 1
    else:
        second_degree = {
            "AC" : "B",
            "AI" : "E",
            "AG" : "D",
            "BH" : "E",
            "CG" : "E",
            "CI" : "F",
            "DF" : "E",
            "GI" : "H",
        }
        first_degree = {
                "A" : "BDEFH",
                "B" : "ACDEFGI",
                "C" : "BDEFH",
                "D" : "ABCEGHI",
                "E" : "ABCDFGHI",
                "F" : "ABCEFGHI",
                "G" : "BDEFH",
                "H" : "ACDEFGI",
                "I" : "BDEFHI"
        }
        all_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        all_patterns = [list(p) for p in permutations(all_letters, length) if p[0] == firstPoint]
        valid_patterns = 0
        for pattern in all_patterns:
            path = [pattern[0]]
            for i in range(1,len(pattern)):
                if not pattern[i] in first_degree[path[-1]] and not (second_degree.get(pattern[i]+path[-1],"") in path or second_degree.get(path[-1]+pattern[i]) in path):
                    break
                path.append(pattern[i])
            else:
                valid_patterns += 1
        return valid_patterns
