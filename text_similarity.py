def simple_similarity(text1,text2):
    # Convert the texts to sets of words
    set1= set(text1.lower().split())
    set2= set(text2.lower().split())


    # Find common words in the pieces of texts
    common_words= set1.intersection(set2)

    #Calculate the similarity ratio

    similarity=len(common_words)/max(len(set1), len(set2))
    return similarity

#Example
text1= "The maize is sweet"
text2="The bean is sweet"

print(simple_similarity(text1,text2))


