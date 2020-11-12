import sys
import random
from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(*word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = str(*word)[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        for var in self.domains:
            wordSet = set()
            for word in self.domains[var]:
                if len(word) == var.length:
                    wordSet.add(word)
            self.domains[var] = wordSet

        print("The domain after the unary check")
        for var in self.domains.items():
            print(var)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # print("Revise")
        # print(x)
        # print(y)

        # print("Neighbors for {}: {}".format(x,self.crossword.neighbors(x)))
        # print("Overlaps for {}: {}".format(x,self.crossword.overlaps[x,y]))

        revised = False
        wordSetX = set()
        # wordSetY = set()

        if(self.crossword.overlaps[x,y] == None):
            return revised

        for wordX in self.domains[x]: 
            for wordY in (self.domains[y] - set(wordX)):
                if wordX[self.crossword.overlaps[x,y][0]] == wordY[self.crossword.overlaps[x,y][1]]:
                    wordSetX.add(wordX)
                    # wordSetY.add(wordY)
                    revised = True
        self.domains[x] = wordSetX
        # self.domains[y] = wordSetY
        return revised


    def  ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        
        isConsistent = True

        # create the arcs list:
        if(arcs==None):
            arcs = list()

            for node in self.domains:
                for n in self.crossword.neighbors(node):
                    arcs.append((node,n))
        else:
            node = arcs
            arcs = list()
            for n in self.crossword.neighbors(node):
                    arcs.append((node,n))
                    
        while (len(arcs) > 0):
            x,y = arcs.pop(-1)
            if(self.revise(x,y) == True):
                if (len(self.domains[x]) == 0):
                    isConsistent = False
                    break
                for z in (self.crossword.neighbors(x)):
                    if(z==y):
                        continue
                    arcs.append((z,x))               

        print("result after ac3 function")
        for var in self.domains.items():
            print(var)

        return isConsistent

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        isCopleted = True
    
        for node in assignment:
            if len(assignment[node]) != 1:
                isCopleted = False

        if(len(self.domains) != len(assignment)):
            isCopleted = False

        return isCopleted

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        isConsistent = True

        checkDistint = set()
        for node in assignment:
            checkDistint.add(list(assignment[node])[0])

        # checking if all words are different in the crosswords
        if(len(checkDistint) != len(assignment)):
            isConsistent = False
            # print("Same words in the assignment check: FAIL")
            return isConsistent

        for node in assignment:
            # checking if the element of crosswords has only one correct solution
            # print("Check the size of the {}, length {} ".format(assignment[node],len(assignment[node])))
            if(len(assignment[node]) != 1):
                isConsistent = False
                # print("Correct size of element {},{}: FAIL".format(node,assignment[node]))
                return isConsistent

            neighbors = self.crossword.neighbors(node)
            for n in neighbors:
                if(n not in assignment):
                    # print("No neighbours")
                    continue
                pair = self.crossword.overlaps[node, n]
                # print("conflict pairs: {}".format(pair))
                # print("Compare to keywords: {}, {}".format(assignment[node], assignment[n]))
                # print("Compare chars: {}, {}".format(str(*assignment[node])[pair[0]],str(*assignment[node])[pair[1]]))
                if str(*assignment[node])[pair[0]] != str(*assignment[n])[pair[1]]:
                    isConsistent = False
                    # print("Neighbour check: FAIL".format(node,assignment[node]))
                    return isConsistent

        return isConsistent

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        # neigbours = self.crossword.neighbors(*var)
        # not_assigned_neighbourd = neigbours - set(*assignment.keys())
        # k = str(*var.keys())
        # values_for_var = self.domains[k]

        # cout_constraints = dict()
        # for word1 in values_for_var:
        #     counter = 0
        #     for variable in not_assigned_neighbourd:
        #         values_for_variable = self.domains[variable]
        #         overlaps = self.crossword.overlaps[var, variable]
        #         letter1 = word1[overlaps[0]]
        #         for word2 in values_for_variable:   
        #             letter2 = word2[overlaps[1]]
        #             if letter1 != letter2:
        #                 counter += 1
        #     cout_constraints.update({word1: counter})
        # output = sorted(cout_constraints, key=cout_constraints.get)
        # return output
        return list(*var.values())

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        
        smallestDomain = 999999
        var = None

        for node in self.domains:
            if node not in assignment:
                if(len(self.domains[node]) < smallestDomain):
                    smallestDomain = len(self.domains[node])
                    var = {node: self.domains[node]}
                elif(len(self.domains[node]) == smallestDomain):
                    if(len(self.crossword.neighbors(node)) < len(self.crossword.neighbors(*var.keys()))):
                        smallestDomain = len(self.domains[node])
                        var = {node: self.domains[node]}
                    
        return var

    def interfaces(self, assignment):
        pass

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # print("\nNew backtrack")
        result = assignment
        
        if (self.assignment_complete(assignment) == True): 
            # print("assignment completed")
            return assignment

        var = self.select_unassigned_variable(assignment)
        
        # print("randomised node {}".format(var))
        
        for value in self.order_domain_values(var,assignment):
            # print("randomised word {}".format(value))
            node = {list(var.keys())[0]: {value}}
            assignment.update(node)
            # print(node, value,  list(*var.values()))
            if(self.consistent(assignment) == True):
                # interfaces = self.interfaces(assignment)

                result = self.backtrack(assignment)
                # print(node, value,  list(*var.values()))
                if result != None:
                    # print("ok")
                    return result
            
            # print("Not correct result need to backtrack")
            assignment.pop(list(node.keys())[0])
        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    print("Print result nodes")
    for node in assignment:
        print(node, assignment[node])

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
