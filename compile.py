import pickle
import codecs
from contract import contract


contractkey = '0x6003284f23a3c3ef0234232dfa32'
filename = 'contract.dat'

'''
Candidate Name list 
'''
candidateList = ['Rama', 'Ken', 'Rose']

'''
make Contract
'''
module = contract()

'''
appending candidate names
'''
module.appendCandidateNames(candidateList)

'''
make hex code for block
'''
dumpmodule = pickle.dumps(module, protocol=pickle.HIGHEST_PROTOCOL)
encodemodule = codecs.encode(dumpmodule, 'hex_codec')

'''
# for test
with open(filename, "a") as contractfile:
    contractfile.write(str(contractkey)+":"+str(encodemodule)[2:-1]+"\n")
'''

'''
send hex data to mkc 
'''
print(encodemodule)
