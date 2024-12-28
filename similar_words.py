from difflib import SequenceMatcher

def check_similarity (text1,text2):
        #Compare the word sequences
        similarity = SequenceMatcher(None, text1, text2).ratio()
        return similarity

#Example 
text1= "how are you doing?"
text2= "how are you faring?"

print(check_similarity(text1,text2))