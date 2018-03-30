#pragma python 3.6.4
import json
import numpy as np

class contract:

    def __init__(self):
        self.candidateList = []
        self.votingCount = []

    def appendCandidateNames(self, names):
        self.candidateList = names
        for i in range(len(names)):
            self.votingCount.append("0")

    def appendCandidateName(self, name):
        self.candidateList.append(name)
        self.votingCount.append("0")

    def votingName(self, name):
        # print(self.candidateList)
        idx = self.candidateList.index(name)
        # print("--> " + str(idx))
        self.votingCount[idx] = str(int(self.votingCount[idx]) + 1)

    def getTotalCadidate(self):
        return self.candidateList, self.votingCount

    def vaildCandidateName(self, name):
        for candiName in self.candidateList:
            if candiName == name:
                # print("found!!!!")
                return True

        return False

