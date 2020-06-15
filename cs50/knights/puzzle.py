from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(Not(AKnight),And(AKnight,AKnave)),
    Or(Not(AKnave),Or(Not(AKnight),Not(AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight)),
    Or(Not(AKnight),And(BKnave,AKnave)),
    Or(Not(AKnave),Or(Not(BKnave),Not(AKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight)),
    Or(Not(AKnight),And(AKnight,BKnight)),
    Or(Not(AKnave),Or(Not(BKnave),Not(AKnave))),
    Or(Not(BKnight),And(BKnight,AKnave)),
    Or(Not(BKnave),Or(Not(BKnight),Not(AKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # world definitions
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight)),
    Or(And(Not(CKnight),CKnave),And(Not(CKnave),CKnight)),

    # B says "A said 'I am a knave'."
    Or(Not(BKnight),Not(AKnight),AKnave),
    Or(Not(BKnave),AKnight,Not(AKnave)),
    Or(Not(BKnight),Not(AKnave),AKnave),
    Or(Not(BKnave),AKnave),

    # B says "C is a knave."
    Or(Not(BKnight),CKnave),
    Or(Not(BKnave),Not(CKnave)),

    # C says "A is a knight."
    Or(Not(CKnight),AKnight),
    Or(Not(CKnave),Not(AKnight)), 
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
