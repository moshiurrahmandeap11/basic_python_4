# Text Analyzer - total characters, words, and sentences in dictionary format

def text_analyzer(text):
    num_characters = len(text)
    num_words = len(text.split())
    num_sentences = text.count('.') + text.count('!') + text.count('?')

    return {
        'characters': num_characters,
        'words': num_words,
        'sentences': num_sentences
    }


# Example usage
sample_text = "Hello world! This is a sample text. It has multiple sentences?"
result = text_analyzer(sample_text)
print(result)  # Should return {'characters': 64, 'words': 12, 'sentences': 3}