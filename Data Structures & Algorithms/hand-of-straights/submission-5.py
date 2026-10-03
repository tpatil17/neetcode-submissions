class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        deck = {}

        for card in hand:
            if card not in deck:
                deck[card] = 1
            else:
                deck[card]+=1
        # store the cards and their count
        hand = sorted(list(set(hand)))[::-1] # get rid of all duplicates and order cards

        while hand:

            num = hand[-1] #smallest card

            if deck[num] == 0:
                hand.pop(-1) # edit hand to reflect true cards state
                # can't open with it as it does not exist
                continue

            # card exists
            deck[num]-=1 # use the card

            if deck[num] == 0:
                hand.pop(-1) # edit hand to reflect true cards state

            ctr = 1
            group = [num]
            trg = num+1 # target card

            while ctr < groupSize: # fill group till size is maxed

                if trg in deck:
                    if deck[trg] > 0:
                        group.append(trg)
                        deck[trg]-=1 # reduce the card count
                        ctr+=1
                        trg+=1
                    else:
                        return False
                else:
                    return False
        return True
            

            
