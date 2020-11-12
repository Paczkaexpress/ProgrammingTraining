import nltk
import sys
# nltk.download('punkt')
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# NONTERMINALS = """
# S -> NP VP | NP VP Conj NP VP  
# NP -> N | Det N | NP PP | Det NP PP | AP NP | N NP
# VP -> V | VP NP | VP PP | VP NP PP
# AP -> Adj Adj | Adj | Det Adj | Adj Conj Adj | Det Adj Conj Adj  
# PP -> P NP
# """

NONTERMINALS = """
S -> SS | SS Conj SS
SS -> NP VP  
NP -> N | Det N | NP PP | Det NP PP | AP NP | N NP | NP Adv | AP N
VP -> V | VP NP | VP PP | VP NP PP | VP Adv | VP Conj VP
AP -> Adj Adj | Adj | Det Adj | Adj Conj Adj | Det Adj Conj Adj  
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = sentence.lower()
    alphabet = list("qwertyuioplkjhgfdsazxcvbnm")

    words = nltk.word_tokenize(sentence)
    finalWords = list()

    for word in words:
        # print(word)
        # print(set(word))
        if set(word).issubset(alphabet):
            finalWords.append(word)

    print(finalWords)
    return finalWords

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    subTreeList = list()
    onlyND = True

    for node in tree.subtrees():
        # print(node)
        # print(node.label())

        if(node.label() == 'NP'):
            onlyND = True
            for subNodes in node:
                if(subNodes.label() == 'NP'):
                    onlyND = False
                    break
            if(onlyND == True):
                subTreeList.append(node)

    return subTreeList

if __name__ == "__main__":
    main()
