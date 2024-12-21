#https://www.codewars.com/kata/5739174624fc28e188000465/train/python

class PokerHand:

    def __init__(self, hand):
        self.hand = hand
        self.value = [card[0] if not card[0] == 'T' else "10" for card in hand.split()]
        self.suit = [card[1] for card in hand.split()]
        self._rank = None
        self._score = None
        self.card_scores = {
            "A" : 1000000000000,
            "K" : 100000000000,
            "Q" : 10000000000,
            "J" : 1000000000,
            "10": 100000000,
            "9" : 10000000,
            "8" : 1000000,
            "7" : 100000,
            "6" : 10000,
            "5" : 1000,
            "4" : 100,
            "3" : 10,
            "2" : 1,
        }
        self.straights = [\
            ['A', '2', '3', '4', '5'],
            ['2', '3', '4', '5', '6'],
            ['3', '4', '5', '6', '7'],
            ['4', '5', '6', '7', '8'],
            ['5', '6', '7', '8', '9'],
            ['6', '7', '8', '9', '10'],
            ['7', '8', '9', '10', 'J'],
            ['8', '9', '10', 'J', 'Q'],
            ['9', '10', 'J', 'Q', 'K'],
            ['10', 'J', 'Q', 'K', 'A']\
         ]
        
    def compare_with(self, other):
        if self.rank < other.rank:
            return "Win"
        elif self.rank > other.rank:
            return "Loss"
        else:
            if self.score["hand"] > other.score["hand"]:
                return "Win"
            elif self.score["hand"] < other.score["hand"]:
                return "Loss"
            else:
                if self.score["kicker"] > other.score["kicker"]:
                    return "Win"
                elif self.score["kicker"] < other.score["kicker"]:
                    return "Loss"
                else:
                    return "Tie"
        
    def get_rank(self):
        if self._rank is None:
            if set(self.value) == set(["10", "J", "Q", "K", "A"]) and len(set(self.suit)) == 1:
                self._rank = 0
            elif len(set(self.suit)) == 1 and any([set(self.value) == set(straight) for straight in self.straights]):
                self._rank =  1
            elif len(set(self.value)) == 2 and any([self.value.count(v) > 3 for v in list(set(self.value))]):
                self._rank =  2
            elif len(set(self.value)) == 2 and not any([self.value.count(v) > 3 for v in list(set(self.value))]):
                self._rank = 3
            elif len(set(self.suit)) == 1:
                self._rank =  4
            elif any([set(self.value) == set(straight) for straight in self.straights]):
                self._rank = 5
            elif len(set(self.value)) == 3 and any([self.value.count(v) == 3 for v in list(set(self.value))]):
                self._rank =  6
            elif len(set(self.value)) == 3 and any([self.value.count(v) == 2 for v in list(set(self.value))]):
                self._rank = 7
            elif len(set(self.value)) == 4:
                self._rank = 8
            else:
                self._rank =  9
        return self._rank
    
    def get_score(self):
        if self._score is None:
            self._score = {}
            values = list(set(self.value))
            if self.rank == 8:
                self._score["hand"] = sum([self.card_scores[v] for v in values if self.value.count(v) == 2 ])
                self._score["kicker"] = sum([self.card_scores[v] for v in values if self.value.count(v) == 1])
            elif self.rank == 7:
                self._score["hand"] = sum([self.card_scores[v] for v in values if self.value.count(v) == 2])
                self._score["kicker"] = sum([self.card_scores[v] for v in values if self.value.count(v) == 1])
            elif self.rank == 6:
                self._score["hand"] = sum([self.card_scores[v] for v in values if self.value.count(v) == 3])
                self._score["kicker"] = sum([self.card_scores[v] for v in values if self.value.count(v) != 3])
            else:
                self._score["hand"] = sum([self.card_scores[v] for v in values])
                self._score["kicker"] = sum([self.card_scores[v]for v in values])
        return self._score
    
    rank = property(get_rank)
    score = property(get_score)

