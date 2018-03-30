
import pickle
import codecs
import sys
from jsonparse import jsonparse
from network import network

class blockprocess:

    def __init__(self, contractkey, param):
        self.contractkey = contractkey
        self.param = param

    def loadContractByte(self):
        # print("contractkey : " + self.contractkey)
        self.version, self.path, self.blockname, self.dbfolder, self.filename = jsonparse().getWebConfigure()
        fullpath = self.path + self.blockname +'/'+ self.dbfolder + '/'+ self.filename
        # print('fullpath : ' + fullpath)
        dbfile = open(fullpath, "r")
        lines = dbfile.readlines()
        
        timestamp = ""
        contractdata = ""
        pretimestamp = ""
        
        for line in lines:
            arrayvalue = line.split(',')
            timestamp = arrayvalue[0].replace('{', '').replace('}', '').split(':')
            
            # print("timestamp : " + str(timestamp[0]))
            contentdata = arrayvalue[11].split(':')
            
            if contentdata[0].replace('{', '') == self.contractkey:
                if pretimestamp == "" or pretimestamp < timestamp[0]:
                    pretimestamp = timestamp[0]

                contractdata = contentdata[2]
                self.sourceHex = contentdata[3].replace('}', '')
                # print("bingo!!!! " + pretimestamp + " -- " + contractdata)

        dbfile.close()
        return contractdata

    def appendContractByte(self, hashcode):
        # with open(filename, "a") as contractfile:
        #     contractfile.write(str(contractkey)+":"+str(hashcode)[2:-1]+"\n")
        # contractfile.close()
        net = network()
        _, _, _, taxi = net.getinfo()
        # print(hashcode)
        # print(self.contractkey)
        contractBlock = self.contractkey + ":" + taxi + ":" + hashcode + ":" + self.sourceHex
        # print("contractBlock : " + contractBlock)
        net.connect()
        net.mksend(("registercontract " + contractBlock).encode('utf-8'))


    def getJsonTotalCadidate(self, condiList, voteCount):
            jsonstring = "{ \n"
            for i in range(len(condiList)):
                jsonstring += "\t \"" + condiList[i] + "\":" + " \"" + voteCount[i] + "\""
                if i != len(condiList)-1: jsonstring += ",\n"
            jsonstring += "\n}"
            return jsonstring

    def makeContractHash(self, candidateName):
        hexcode = self.loadContractByte()
        # print("hexcode : " + hexcode)
        decodemodule = codecs.decode(hexcode, 'hex_codec')
        module = pickle.loads(decodemodule)
        module.votingName(candidateName)
        dumpmodule = pickle.dumps(module, protocol=pickle.HIGHEST_PROTOCOL)
        encodemodule = codecs.encode(dumpmodule, 'hex_codec')
        self.appendContractByte(str(encodemodule).replace('b\'', '').replace('\'',''))

    def loadData(self):
        hexcode = self.loadContractByte()
        #print(hexcode)
        decodemodule = codecs.decode(hexcode, 'hex_codec')
        module = pickle.loads(decodemodule)
        condidateList, votingCount = module.getTotalCadidate()
        jsonstring = self.getJsonTotalCadidate(condidateList, votingCount)
        print(jsonstring)
