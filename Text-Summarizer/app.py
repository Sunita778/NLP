import streamlit as st
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Function for text summarization
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

# Streamlit app
def main():
    st.title("Text Summarization App")
    text_input = st.text_area("Enter text to summarize:")
    num_sentences = st.slider("Select number of sentences for summary:", min_value=1, max_value=10, value=3)

    if st.button("Summarize"):
        if text_input:
            summary = text_summarization(text_input, num_sentences)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
