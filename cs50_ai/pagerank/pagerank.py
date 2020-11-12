import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    N = len(corpus[page])
    # print(page)
    pr = dict()
    s = (1-damping_factor)/len(corpus)
    if (N > 0):
        for key in corpus:
            if key in corpus[page]:
                pr[key] = s + damping_factor * (1/N)
            else:
                pr[key] = s
    else:
        for key in corpus:
            pr[key] = 1 / len(corpus)
            # print("rec")
            # print(page)
    # print(pr)
    return pr


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dic = dict()
    temp = dict()
    n = 10000
    page = random.choices(tuple(corpus.keys()))[0]
    for i in range(n): 

        temp = transition_model(corpus, page, damping_factor)
        # select new page based on the transition_model result.  
        page = random.choices(tuple(corpus.keys()),temp.values())[0]

        for k in temp:
            if k not in dic:
                dic[k] = temp[k]
            else:
                dic[k] = ((dic[k]*(i-1)) + temp[k])/i
    return dic

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pr = dict()
    prev_pr = dict()
    tmp = dict()
    treshold = 0.0001

    tmp = dict((k,1/len(corpus)) for k in corpus)
    pr = dict((k,1/len(corpus)) for k in corpus)
    prev_pr = dict((k,0) for k in corpus)

    # find pages without outgoing connections
    for page in corpus:
        # print("{} {}".format(page,corpus[page]))
        if(len(corpus[page]) == 0):
            corpus[page] = corpus.keys()
        
    finished = False
    while finished == False:
        # copy data to prev pr

        prev_pr = dict((k,pr[k]) for k in pr)

        for k in pr:

            s = 0
            for p in corpus:
                if k in corpus[p]: 
                    s += damping_factor * tmp[p] / len(corpus[p])

            pr[k] = (1-damping_factor)/len(corpus) + s

        tmp = dict((k,pr[k]) for k in pr)
        counterList = list(((abs(pr[k] - prev_pr[k]) < treshold) for k in pr)) 
        if False not in counterList:
            finished = True      
        # print(pr)
    
    norm = sum(list(pr[k] for k in pr))
    pr = dict((k,pr[k]/norm) for k in pr)
    return pr

if __name__ == "__main__":
    main()
