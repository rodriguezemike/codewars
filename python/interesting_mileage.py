def is_interesting(number, awesome_phrases):
    if number > 99: 
        if set(str(number)[1:]) == {"0"} or len(set(str(number))) == 1 or str(number) == str(number)[::-1] or str(number) in "1234567890" or str(number) in "9876543210" or number in awesome_phrases:
            return 2
        elif is_interesting(number + 1, awesome_phrases) == 2 or is_interesting(number+2, awesome_phrases) == 2:
            return 1
        else:
            return 0
    else:
        return 0
