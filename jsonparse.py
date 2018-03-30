import json

class jsonparse:

    def __init__(self):
        filename = 'webconf.json'
        json_data=open(filename).read()
        self.data = json.loads(json_data)

    def getWebConfigure(self):
        return self.data['version'], self.data['dbinfo']['path'], self.data['dbinfo']['blockname'], self.data['dbinfo']['folder'], self.data['dbinfo']['file']

    def getSocketConfigure(self):
        return self.data['version'], self.data['network']['ip'], self.data['network']['port'], self.data['network']['taxi']