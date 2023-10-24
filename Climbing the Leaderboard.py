def climbingLeaderboard(ranked, player):
    
    ranked = sorted(set(ranked), reverse=True)
    
    ranks = []
    
    for score in player:
         
        while ranked and score >= ranked[-1]:
            ranked.pop()
        
        ranks.append(len(ranked) + 1)
            
    return ranks
    