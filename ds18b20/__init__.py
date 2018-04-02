import os
import fnmatch
import time

def all_probes():
    """return list of probes"""
    return [Probe(probe_id) for probe_id in os.listdir("/sys/bus/w1/devices") if fnmatch.fnmatch(probe_id, '28-*')]    

def probe_by_id(probe_id):
    if os.path.exists('/sys/bus/w1/devices/{}/w1_slave'.format(probe_id)):
        return Probe(probe_id)

class Probe:
    def __init__(self, probe_id):
        self.probe_id = probe_id
        self._probe_addr = '/sys/bus/w1/devices/{}/w1_slave'.format(self.probe_id)
        self.temperature = None

    def __repr__(self):
        return 'Probe({})'.format(self.probe_id)

    def read_temperature(self):
        self.temperature = self._get_temp()
        return self.temperature

    def mean_temperature(self, n):
        temps = []
        for _ in range(n):
            temp = self._get_temp()
            if temp == None:
                return
            temps.append(temp)
        return sum(temps)/n
    
    def _get_temp(self):  # TODO: async?
        for _ in range(3):
            with open(self._probe_addr, 'r') as f_obj:
                lines = f_obj.readlines()
                if lines[0].find("YES") is -1:
                    time.sleep(0.2)
                    continue
                pok = lines[1].find('=')
                if lines[1].find('=') is -1:
                    time.sleep(0.2)
                    continue
                temperature = float(lines[1][pok+1:pok+6])/1000
                return temperature