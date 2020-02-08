import sys
from PIL import Image
import glob
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np
import random

def prepareRawImgs():
    for i in range(25):
        fName = str(i)
        f = open("raw/" + fName + ".txt", "r+")

        rawTxt = f.read().split("\n")

        rawTxt = rawTxt[1:]

        colMap = []

        for line in rawTxt:
            line = line.split(" ")
            # print(line)
            # colMap.append(list())
            for v in line:
                colMap.append(tuple(map(int, v.split(','))))

        letter = [[] * x for x in range(5)]

        for j in range(5):
            for i in range(len(colMap)):
                if i % 60 < j * 9 + 13 and i % 60 > j * 9 + 4:
                    letter[j].append(colMap[i])

        for i in range(5):
            im = Image.new('RGB', (8, 30))
            im.putdata(letter[i])
            im = im.convert('LA')
            im.save('img/' + fName + str(i) + '.png')
            # f = open('img/' + fName + str(i) + '.txt', "w+")
            # f.write(letter[i])

def getLettersFromFile(fName):
    f = open("raw/" + fName + ".txt", "r+")

    rawTxt = f.read().split("\n")

    rawTxt = rawTxt[1:]

    colMap = []

    for line in rawTxt:
        line = line.split(" ")
        # print(line)
        # colMap.append(list())
        for v in line:
            colMap.append(tuple(map(int, v.split(','))))

    letter = [[] * x for x in range(5)]

    for j in range(5):
        for i in range(len(colMap)):
            if i % 60 < j * 9 + 13 and i % 60 > j * 9 + 4:
                letter[j].append(colMap[i])

    return letter

def prepareTestImg(sliceNr):
    f = open('raw/1.txt','r+')

    rawTxt = f.read().split("\n")

    rawTxt = rawTxt[1:]

    colMap = []

    for line in rawTxt:
        line = line.split(" ")
        for v in line:
            colMap.append(tuple(map(int, v.split(','))))

    letter = [[] * x for x in range(1)]

    for i in range(len(colMap)):
        if i % 60 < sliceNr * 9 + 13 and i % 60 > sliceNr * 9 + 4:
            letter[0].append(colMap[i])

    img = Image.new('RGB', (8, 30))
    img.putdata(letter[0])
    img = img.convert('LA')
    # f = open('img/test' + str(i) + '.txt', "w+")
    # f.write(letter[i])
    return img

def imgTreshold(x):
    if x > 100:
        return 255
    else:
        return 0

def assignTrainedValues(neurons):
    # neurons['0'].synaptic_weight =

    pass


class Neuron():
    def __init__(self, nr_of_inputs):
        # self.synaptic_weight = np.random.random((nr_of_inputs,1))
        self.synaptic_weight = [0]*nr_of_inputs
        # print("initial value of synaptic weight {}".format(self.synaptic_weight.T))

    def train(self, type, input_items, training_output, number_of_iterations):
        # print(input_items)
        input_items = np.array(input_items)[np.newaxis]
        for _ in range(number_of_iterations):
            output = self.think(input_items)
            if type == training_output:
                t = 1
            else:
                t = 0

            error = t - output
            # print("error {}, prediction output {}, type of neuron {}, letter {}".format(error, output, type, training_output))
            # print("sigmoidDot(output) {}, error * sigmoidDot(output) {}".format(self.sigmoidDot(output), error * self.sigmoidDot(output)))
            adjustment = np.dot(input_items.T, error * self.sigmoidDot(output))
            # print("neruon adjustment {}".format(adjustment))
            self.synaptic_weight += adjustment
            # print("Synaptic weight after adjustment {}".format(self.synaptic_weight.T))
        # function which is guessing the answer
        # input_items = map(lambda x: float(x), pixelVal)
        output = self.sigmoid(np.dot(input_items, self.synaptic_weight))
        return output

    def think(self, input_items):
        # inputs = input_items.astype(float)
        # print("dot product {}".format(np.dot(input_items, self.synaptic_weight)))
        output = self.sigmoid(np.dot(input_items, self.synaptic_weight))
        return output

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidDot(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

if __name__ == "__main__":
    IMAGE_SIZE = 8 * 30
    letterSet = "0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
    # prepareRawImgs() # it is done for training set

    # check number of letters
    print(glob.glob("tagged/*.png"))
    taggedLetters = glob.glob("tagged/*.png")
    # create new neuron for every new letter
    dicNeuron = {}

    for l in taggedLetters:
        if l[7] not in dicNeuron: # trying to get only a tag from name
            dicNeuron[l[7]] = Neuron(IMAGE_SIZE)


    assignTrainedValues(dicNeuron)

    for l in taggedLetters:
        # print("Neuron to be trained {}".format(l[7]))
        img = Image.open(l)
        img = img.convert('L')
        # img = img.filter()
        pixelVal = np.array(img)
        pixelVal = [y for x in pixelVal for y in x]  # join arrays to one big one
        pixelVal = [(255 - imgTreshold(x)) for x in pixelVal]
        # train every neuron
        # for d in dicNeuron.items():
        #     d[1].train(d[0], pixelVal, l[7], 20)
        # train only neuron equivalent to given letter
        dicNeuron[l[7]].train(l[7], pixelVal, l[7], 5)

    s = ""
    for l in letterSet:
        s +="neurons['{}'].synaptic_weight = {}".format(l,list(dicNeuron[l].synaptic_weight))
        s += '\n'

    f = open("synapsis.txt", "w+")
    f.write(s)

    rawTxt = f.read().split("\n")

    predictionVal = None
    predictionKey = None

    ans = ""
    fileToOpen = "2"
    letters = getLettersFromFile(fileToOpen)
    for let in letters:
        im = Image.new('RGB', (8, 30))
        im.putdata(let)
        im = im.convert('L')
        pixelVal = np.array(im)
        pixelVal = [y for x in pixelVal for y in x]  # join arrays to one big one
        pixelVal = [(255 - imgTreshold(x)) for x in pixelVal]
        for d in dicNeuron.items():
            # pred = d[1].think(pixelVal)
            pred = np.dot(pixelVal, d[1].synaptic_weight)
            print("Neuron {}, pred {}, dot prod {}".format(d[0], pred, np.dot(pixelVal, d[1].synaptic_weight)))
            if predictionVal == None:
                predictionVal = pred
                predictionKey = d[0]
            else:
                # print("biggest val {} current val {}".format(predictionVal, pred))
                if predictionVal < pred:
                    predictionVal = pred
                    predictionKey = d[0]

        # print("Guessed key:{}, correct  key {}, surity:{}".format(predictionKey, let, predictionVal))
        ans += predictionKey
        predictionKey = None
        predictionVal = 0
    print(ans)


