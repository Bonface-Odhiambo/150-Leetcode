from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import dot
from numpy.linalg import norm
import numpy as np

class CosineSimilarity:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def calculate_similarity(self, text1, text2):
        """Calculate cosine similarity between two texts using TF-IDF."""
        # Fit and transform the texts
        tfidf_matrix = self.vectorizer.fit_transform([text1, text2])
        
        # Convert to dense arrays
        vector1 = tfidf_matrix[0].toarray().flatten()
        vector2 = tfidf_matrix[1].toarray().flatten()
        
        # Calculate cosine similarity
        similarity = dot(vector1, vector2) / (norm(vector1) * norm(vector2))
        return float(similarity)

class LevenshteinSimilarity:
    def calculate_similarity(self, text1, text2):
        """Calculate normalized Levenshtein distance between two texts."""
        # Create matrix of size (len(text1) + 1) x (len(text2) + 1)
        matrix = np.zeros((len(text1) + 1, len(text2) + 1))
        
        # Initialize first row and column
        for i in range(len(text1) + 1):
            matrix[i][0] = i
        for j in range(len(text2) + 1):
            matrix[0][j] = j
            
        # Fill in the rest of the matrix
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(
                        matrix[i-1][j] + 1,    # deletion
                        matrix[i][j-1] + 1,    # insertion
                        matrix[i-1][j-1] + 1   # substitution
                    )
        
        # Get the Levenshtein distance
        distance = matrix[len(text1)][len(text2)]
        
        # Normalize the distance to get similarity
        max_length = max(len(text1), len(text2))
        similarity = 1 - (distance / max_length)
        return float(similarity)

# Example usage
def compare_texts(text1, text2):
    # Initialize both similarity calculators
    cosine_calc = CosineSimilarity()
    levenshtein_calc = LevenshteinSimilarity()
    
    # Calculate similarities
    cosine_sim = cosine_calc.calculate_similarity(text1, text2)
    levenshtein_sim = levenshtein_calc.calculate_similarity(text1, text2)
    
    return {
        'cosine_similarity': cosine_sim,
        'levenshtein_similarity': levenshtein_sim
    }

# Test the implementations
if __name__ == "__main__":
    text1 = "The quick brown fox jumps over the lazy dog"
    text2 = "The fast brown fox jumped over a lazy dog"
    
    results = compare_texts(text1, text2)
    print(f"Cosine Similarity: {results['cosine_similarity']:.4f}")
    print(f"Levenshtein Similarity: {results['levenshtein_similarity']:.4f}")