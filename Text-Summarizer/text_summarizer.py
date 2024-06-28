import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def text_summarization(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stop words
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    words = [word.lower() for word in words if word.isalnum()]
    filtered_words = [word for word in words if word not in stop_words]

    # Calculate word frequency distribution
    freq_dist = FreqDist(filtered_words)

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word]
                else:
                    sentence_scores[sentence] += freq_dist[word]

    # Get the top 'num_sentences' sentences based on scores
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Join selected sentences to form the summary
    summary = ' '.join(summarized_sentences)
    return summary

# Example text for testing
text = '''
Your text goes here. This could be a larger piece of content that you'd like to summarize. 
It could be an article, a story, or any textual content. The function `text_summarization` 
will extract the most relevant sentences and generate a summary.
'''

# Call the function with the example text and print the summary
summary = text_summarization(text)
print("Summary:")
print(summary)
