from .context import ds18b20
import time

def script():
    print('ds18b20.all_probes:', ds18b20.all_probes())
    p = ds18b20.all_probes()[0]

    print('ds18b20.probe_by_id:', ds18b20.probe_by_id(p.probe_id))

    temp = p.read_temperature()
    print('Probe.read_temperature:', temp)

    print('Wating for change...')
    while not p.changed():
        time.sleep(1)
    print('Changed!', p.read_temperature() - temp)

if __name__ == '__main__':
    script()