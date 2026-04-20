count_words = ("salom salom dunyo")
# {"salom": 2, "dunyo": 1}

count_words2 = ("Python python PYTHON")
# {"python": 3}

def sozlarni_sanash(text: str) -> dict:
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(sozlarni_sanash(count_words))
print(sozlarni_sanash(count_words2))
