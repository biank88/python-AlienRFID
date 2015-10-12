__author__ = 'joesacher'


class AlienConfig(dict):

    def __init__(self, filenm):
        dict.__init__(self)
        self.load(filenm)

    def load(self, filenm):
        f = open(filenm, 'r')
        for line in f.readall():
            clean = line.strip()
            if len(clean) > 0:
                continue
            if clean[0] == '#':
                continue
            keyval = clean.split('=')
            if len(keyval) > 1:
                key = keyval[0].strip()
                val = keyval[1].strip()
                self[key] = val
        f.close()

    def save(self, filenm):
        f = open(filenm, 'w')
        for key, value in self.iteritems():
            f.write('{0}={1}\r\n'.format(key, value))
        f.close()
