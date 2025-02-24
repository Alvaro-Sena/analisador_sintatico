import nltk
import sys
import re

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

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> Det N | Det AdjP N | N | NP PP
AdjP -> Adj | Adj AdjP
VP -> V | V NP | V Adv | V NP PP | VP Conj VP
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # Se um nome de arquivo for especificado, leia a frase do arquivo
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Caso contrário, obtenha a frase como entrada
    else:
        s = input("Sentence: ")

    # Converta a entrada em uma lista de palavras
    s = preprocess(s)

    # Tente analisar a frase
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Imprima cada árvore com os segmentos de frase nominal
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Converte `sentence` em uma lista de suas palavras.
    Pré-processa a frase convertendo todos os caracteres para minúsculas
    e removendo qualquer palavra que não contenha pelo menos um caractere alfabético.
    """
    sentence = sentence.lower()
    words = nltk.word_tokenize(sentence)
    return [word for word in words if re.match('[a-z]', word)]


def np_chunk(tree):
    """
    Retorna uma lista de todos os segmentos de frases nominais na árvore da frase.
    Um segmento de frase nominal é definido como uma subárvore da frase
    cuja etiqueta é NP e que não contém outras frases nominais como subárvores.
    """
    np_chunks = []
    for subtree in tree.subtrees(lambda t: t.label() == 'NP'):
        # Verifica se não há outra subárvore NP dentro desta subárvore
        if not any(child.label() == 'NP' for child in subtree.subtrees(lambda t: t != subtree)):
            np_chunks.append(subtree)
    return np_chunks


if __name__ == "__main__":
    main()
