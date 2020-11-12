import csv
import itertools
import sys
import unittest
import random
import copy

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # print(people)
    # print(one_gene)
    # print(two_genes)
    # print(have_trait)

    jp = dict((k,0) for k in people)
    people_tmp = copy.deepcopy(people)

    while(len(people_tmp.keys()) > 0):
        person = random.choices(tuple(people_tmp.keys()))[0]
        # print(person)
        if people[person]["mother"] == None and people[person]["father"] == None:
            # print(person)
            gene = 0
            if person in one_gene:
                gene = 1
            elif person in two_genes:
                gene = 2

            trait = False
            if person in have_trait:
                trait = True

            # print(PROBS["trait"][gene][people[person]["trait"]])
            # print(PROBS["gene"][gene])
            if(people[person]["trait"] == None):
                jp[person] = PROBS["trait"][gene][trait] * PROBS["gene"][gene]
            else:
                jp[person] = PROBS["trait"][gene][people[person]["trait"]] * PROBS["gene"][gene]
            people_tmp.pop(person,None)

        elif jp[people[person]["mother"]] != 0 and jp[people[person]["father"]] != 0:

            gene = 0
            trait = False

            if person in have_trait:
                trait = True

            if person in one_gene:
                gene = 1
            elif person in two_genes:
                gene = 2

            genProbability = 0
            momGen = 0
            dadGen = 0
            genPool = 0
            if (people[person]["mother"] in two_genes):
                momGen = 3
            elif (people[person]["mother"] in one_gene):
                momGen = 1
            else:
                momGen = 0    

            if (people[person]["father"] in two_genes):
                dadGen = 3
            elif (people[person]["father"] in one_gene):
                dadGen = 1
            else:
                dadGen = 0
            genPool = momGen * 4 + dadGen

            for i in range(4):
                genConfNr = ((genPool>>2)>>(int(i/2)%2) & 1) + (genPool>>(i%2) & 1) 
                # print(genConfNr)

                if (abs(genConfNr-gene) == 0): # require two genes
                    genProbability += 0.25 * 0.99 * 0.99      
                    if(gene == 1):
                        genProbability += 0.25 * 0.01 * 0.01     

                elif(abs(genConfNr-gene) == 1):
                    genProbability += 0.25 * 0.99 * 0.01
                    if(gene == 1):
                        genProbability += 0.25 * 0.99 * 0.01
                else:
                    genProbability += 0.25 * 0.01 * 0.01
            # print("son prob: {}".format(genProbability))

            if(people[person]["trait"] == None):
                # jp[person] = genProbability * PROBS["trait"][gene][trait] * jp[people[person]["mother"]] * jp[people[person]["father"]]   
                jp[person] = genProbability * PROBS["trait"][gene][trait]
            else:
                # jp[person] = genProbability * PROBS["trait"][gene][people[person]["trait"]] * jp[people[person]["mother"]] * jp[people[person]["father"]]   
                jp[person] = genProbability * PROBS["trait"][gene][people[person]["trait"]]
            people_tmp.pop(person,None)

    # print(PROBS["trait"][gene][trait])
    # print(genProbability * PROBS["trait"][gene][trait])
    # print(jp)

    # only for a single output value:
    tempSum = 0
    for item in jp:
        if(tempSum == 0):
            tempSum = jp[item]
        else:
            tempSum *= jp[item]
    # print("{} * {} * {} = {}".format(jp["Lily"],jp["James"],jp["Harry"],tempSum))
    jp = tempSum
    # print(jp)
    return jp


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # print("New update")
    # print(p)

    # #old dictionary approach:
    # for item in probabilities.items():
    #     # print(item, item[0])

    #     if item[0] in two_genes:
    #         item[1]["gene"][2] += p[item[0]]
    #     elif item[0] in one_gene:
    #         item[1]["gene"][1] += p[item[0]]
    #     else:
    #         item[1]["gene"][0] += p[item[0]]
        
    #     if item[0] in have_trait:
    #         item[1]["trait"][True] += p[item[0]]
    #     else:
    #         item[1]["trait"][False] += p[item[0]]

    # new single value approach:
    for item in probabilities.items():
        # print(item)
        if item[0] in two_genes:
            item[1]["gene"][2] += p
        elif item[0] in one_gene:
            item[1]["gene"][1] += p
        else:
            item[1]["gene"][0] += p
        
        if item[0] in have_trait:
            item[1]["trait"][True] += p
        else:
            item[1]["trait"][False] += p

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    try:
        for person in probabilities.values():
            norm = sum(list(x for x in person["gene"].values()))
            person["gene"] = dict((i[0],i[1]/norm) for i in person["gene"].items()) 

        for person in probabilities.values():
            norm = sum(list(x for x in person["trait"].values()))
            person["trait"] = dict((i[0],i[1]/norm) for i in person["trait"].items()) 
    except:
        print("Incorrect probability components")

class MyTest(unittest.TestCase):
    def test_normalise(self):
        people = ["Joe" , "Kimmi"]
        
        probabilities = {
            person: {
                "gene": {
                    2: 0,
                    1: 0,
                    0: 0
                },
                "trait": {
                    True: 0,
                    False: 0
                }
            }
            for person in people
        }

        correct_probabilities =  {
            person: {
                "gene": {
                    2: 0,
                    1: 0,
                    0: 0
                },
                "trait": {
                    True: 0,
                    False: 0
                }
            }
            for person in people
        }

        probabilities["Joe"]["gene"] = {2:0.0, 1: 0.1, 0: 0.1}
        probabilities["Joe"]["trait"] = {True: 0.1, False: 0.1}
        
        probabilities["Kimmi"]["gene"] = {2:0.2, 1: 0.2, 0: 0.1}
        probabilities["Kimmi"]["trait"] = {True: 0.8, False: 0.8}

        correct_probabilities["Joe"]["gene"] = {2:0, 1: 0.5, 0: 0.5}
        correct_probabilities["Joe"]["trait"] = {True: 0.5, False: 0.5}
        
        correct_probabilities["Kimmi"]["gene"] = {2:0.4, 1: 0.4, 0: 0.2}
        correct_probabilities["Kimmi"]["trait"] = {True: 0.5, False: 0.5}

        normalize(probabilities)

        self.assertDictEqual(probabilities, correct_probabilities)

if __name__ == "__main__":
    # unittest.main()
    main()
