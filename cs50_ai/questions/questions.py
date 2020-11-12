import nltk
import sys
import os
import math
import string
# nltk.download('stopwords')

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    
    files = dict()

    for file in os.listdir(directory):
        files[file] = open(os.path.join(directory, file),encoding="utf8").read()

    return files

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """    
    tokens = [word.lower() for word in nltk.word_tokenize(document)]
    filteredWords = list()
    stopwords = nltk.corpus.stopwords.words("english")
    charSet = set(list(string.punctuation + '–—'))
    
    # filteredWords = removePunctuationChars(tokens, charSet, stopwords)
    filteredWords = removePunctuationWords(tokens, charSet, stopwords)

    return sorted(filteredWords)

def removePunctuationWords(words, charSet, stopwords):
    filteredWords = []
    for word in words:
        if word in stopwords:
            pass
        elif word in charSet:
            pass
        else:
            filteredWords.append(word)
    return filteredWords

def removePunctuationChars(words, charSet, stopwords):
    filteredWords = []
    for word in words:
        newWord = ''
        for char in word:
            if char not in charSet:
                newWord += char
        if newWord not in stopwords and len(newWord) > 0:
            filteredWords.append(newWord)
    return filteredWords

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    numberOfFiles = len(documents)

    idfs = dict()
    wordInFiles = 0

    for words in documents.values():
        for word in words:
            if word not in idfs:
                wordInFiles = sum([documents[testFile].count(word) for testFile in documents])
               
                # wiki td-idf schema 2
                idfs[word] = math.log(1 + (numberOfFiles / wordInFiles))
 
    return idfs

def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    topFilesDir = dict()

    for fileName, fileWords in files.items():
        topFilesDir[fileName] = sum([idfs[x] * fileWords.count(x) for x in query])

    return sorted(topFilesDir, key = topFilesDir.get, reverse = True)[:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    topSentencesDir = dict()

    for keyStentence, sentence in sentences.items():
        topSentencesDir[keyStentence] = {}
        topSentencesDir[keyStentence]["idf"] = sum([idfs.get(x, 0) for x in query if (x in sentence)])
        topSentencesDir[keyStentence]["wordRatio"] = len(query) / len(sentence)
      
    return sorted(topSentencesDir, key = lambda keyStentence: (topSentencesDir[keyStentence]['idf'], topSentencesDir[keyStentence]['wordRatio']), reverse = True)[:n]

if __name__ == "__main__":
    main()
