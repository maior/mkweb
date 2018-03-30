import sys
from blockprocess import blockprocess

def main():
    param = sys.argv[2]
    
    proc = blockprocess(sys.argv[1], sys.argv[2])
    if param == 'total':
        proc.loadData()
    elif param == 'voting':
        proc.makeContractHash(sys.argv[3])
        proc.loadData()
    elif param == 'add':
        proc.module.appendCandidateName(sys.argv[3])

    sys.stdout.flush()

if __name__ == '__main__':
    main()