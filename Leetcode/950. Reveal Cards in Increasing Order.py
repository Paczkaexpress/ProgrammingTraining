class Solution(object):
    def deckRevealedIncreasing(self, deck):
        index = collections.deque(range(len(deck)))
        ans = [0] * len(deck)
        
        deck.sort()
        
        for card in deck:
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
                
        return ans