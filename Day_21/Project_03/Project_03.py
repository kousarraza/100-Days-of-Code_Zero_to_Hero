def count_articles(text):
    articles = ['a', 'an', 'the']
    article_count = {'a': 0, 'an': 0, 'the': 0}
    words = text.lower().split()
    
    for word in words:
        if word in articles:
            article_count[word] += 1
    
    return article_count

def count_words(text):
    return len(text.split())

def count_prepositions(text):
    prepositions = ['of', 'in', 'on', 'at', 'by', 'with', 'from', 'to', 'into', 'during', 'including', 'until', 'against', 'among', 'throughout', 'despite', 'towards', 'upon', 'within', 'without', 'before', 'after', 'above', 'below', 'across', 'along', 'around', 'behind', 'between', 'beyond', 'down', 'from', 'in', 'into', 'near', 'off', 'on', 'onto', 'out', 'over', 'past', 'since', 'through', 'throughout', 'till', 'to', 'toward', 'under', 'underneath', 'until', 'up', 'upon', 'with', 'within', 'without']
    preposition_count = 0
    words = text.lower().split()
    
    for word in words:
        if word in prepositions:
            preposition_count += 1
    
    return preposition_count

def count_vowels_consonants(text):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Get input from the user
user_text = input("Enter some text: ")

# Count the articles
articles = count_articles(user_text)
print("Articles:")
for article, count in articles.items():
    print(f"{article.capitalize()}: {count}")

# Count the words
num_words = count_words(user_text)
print(f"Words: {num_words}")

# Count the prepositions
num_prepositions = count_prepositions(user_text)
print(f"Prepositions: {num_prepositions}")

# Count the vowels and consonants
vowels, consonants = count_vowels_consonants(user_text)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
