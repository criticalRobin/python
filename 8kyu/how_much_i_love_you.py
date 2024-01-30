def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    
    if nb_petals >= len(phrases):
        petal = (nb_petals - 1) % len(phrases)
    else:
        petal = nb_petals - 1
    
    return phrases[petal]
    
    

how_much_i_love_you(458)