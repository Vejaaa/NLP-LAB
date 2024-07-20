import nltk
from nltk import CFG, ChartParser, RecursiveDescentParser,tree

# Define grammar
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "Rahil" | "Bob" | Det N | Det N PP | N
    Det -> "a" | "an" | "the" | "my" | "his"
    N -> "dog" | "cat" | "telescope" | "park" | "Moon" | "terrace"
    P -> "in" | "on" | "by" | "with" | "from"
""")

# Get user input for the sentence
sentence = input("Enter a sentence: ").split()

# Function to parse and display trees
def parse_and_display(parser, sentence, parse_type):
    print(f"{parse_type} Parsing:")
    trees = list(parser.parse(sentence))
    if not trees:
        print("No parse trees found.")
    else:
        for tree in trees:
            tree.pretty_print()
            tree.draw()

# Bottom-Up Parsing
parse_and_display(ChartParser(grammar), sentence, "Bottom-Up")

# Top-Down Parsing
parse_and_display(RecursiveDescentParser(grammar), sentence, "Top-Down")
