import spacy
from textstat import flesch_reading_ease, flesch_kincaid_grade
from textstat.textstat import textstatistics
from deepeval.test_case import LLMTestCase
from deepeval.metrics import BaseMetric


# Splits the text into sentences, using spacy's sentence segmentation
def break_sentences(text):
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(text)
	return list(doc.sents)

# Returns Number of Words in the text
def word_count(text):
	sentences = break_sentences(text)
	words = 0
	for sentence in sentences:
		words += len([token for token in sentence])
	return words

# Using textstat library to calculate syllables in a word
def syllables_count(word):
	return textstatistics().syllable_count(word)

# Returns the average number of syllables per word in the text
def avg_syllables_per_word(text):
	syllable = syllables_count(text)
	words = word_count(text)
	ASPW = float(syllable) / float(words)
	return round(ASPW, 1)

def calculate_readability_scores(text):
    sentences = len(break_sentences(text))
    words = word_count(text)
    syllables = syllables_count(text)

    flesch_ease = flesch_reading_ease(text)
    flesch_kincaid = flesch_kincaid_grade(text)
    
    return {
        "Flesch Reading Ease": flesch_ease,
        "Flesch-Kincaid Grade": flesch_kincaid,
        "Sentence Count": sentences,
        "Word Count": words,
        "Syllable Count": syllables,
        "Average Syllables per Word": avg_syllables_per_word(text)
    }

# DeepEval - define custom readability metric
class ReadabilityMetric(BaseMetric):
    def __init__(self, threshold_high: float = 3.0, threshold_low: float = 2.0):
        self.threshold_high = threshold_high
        self.threshold_low = threshold_low

    def measure(self, test_case: LLMTestCase):
        score = self.score(test_case.actual_output)
		#return score
        return score <= self.threshold_high and score >= self.threshold_low

    def score(self, text: str) -> float:
        # Implement your custom readability logic here
        return calculate_readability_scores(text)["Flesch-Kincaid Grade"]


"""
# Returns the number of sentences in the text
def sentence_count(text):
	sentences = break_sentences(text)
	return len(sentences)

# Returns average sentence length
def avg_sentence_length(text):
	words = word_count(text)
	sentences = sentence_count(text)
	average_sentence_length = float(words / sentences)
	return average_sentence_length


# Return total Difficult Words in a text
def difficult_words(text):
	
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(text)
	# Find all words in the text
	words = []
	sentences = break_sentences(text)
	for sentence in sentences:
		words += [str(token) for token in sentence]

	# difficult words are those with syllables >= 2
	# easy_word_set is provide by Textstat as 
	# a list of common words
	diff_words_set = set()
	
	for word in words:
		syllable_count = syllables_count(word)
		if word not in nlp.Defaults.stop_words and syllable_count >= 2:
			diff_words_set.add(word)

	return len(diff_words_set)

# A word is polysyllablic if it has more than 3 syllables
# Counts the number of polysyllabic words in the text
def poly_syllable_count(text):
	count = 0
	words = []
	sentences = break_sentences(text)
	for sentence in sentences:
		words += [token for token in sentence]

	for word in words:
		
		try: 
			syllable_count = syllables_count(word)
			if syllable_count >= 3:
				count += 1
		except:
			pass
	return count
"""