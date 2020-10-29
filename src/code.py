def anagrams(word, words):
    #word contains the string
    #words contains the possible strings
    #character_word = [[char,word.count(char)] for char in word]
    #and we have to return the correct possibilities
    character_word = [char for char in word]
    count_characters = {x: character_word.count(x) for x in character_word}
    answer = []
    for sample_word in words:
        character_sample_word = [char for char in sample_word ]
        count_sample_characters = {x: character_sample_word.count(x) for x in character_sample_word}
        if count_sample_characters == count_characters:
            answer.append(sample_word)
        else:
            continue
    return answer
            
