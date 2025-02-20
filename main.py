def evaluate_word(word: str) -> int:
    score = 0
    for ltr in word:
        score += ord(ltr) - 96
    return score


def high(words: str) -> str:
    list_of_words = words.split()
    # print(list_of_words)
    highest_score_word = {
        "word": list_of_words[0],
        "score": evaluate_word(list_of_words[0]),
    }
    for word in list_of_words[1:]:
        score = evaluate_word(word)
        if highest_score_word.get("score") < score:
            highest_score_word["word"] = word
            highest_score_word["score"] = score
        # print(highest_score_word)
    return highest_score_word.get("word")