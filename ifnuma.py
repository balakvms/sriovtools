#! /usr/bin/python

import sys
import os
import commands

def nics():
    global devices
    devices=[]
    status,out=commands.getstatusoutput('lspci -D |grep -i eth')
    if status != 0 :
        print(out)
        sys.exit(0)
    for line in out.splitlines():
        devid,desc=line.split(" ",1)
        numa="cat /sys/bus/pci/devices/%s/numa_node" % devid
        status,res=commands.getstatusoutput(numa)
        dev={'Device : ':devid,'Descrition : ':desc,'NumaNode : ':res}
        devices.append(dev)

    print("Device\t\t\tNumaNode\tDescription")
    for dev in devices:
        print(str(dev.get('Device : '))+"\t\t"+str(dev.get('NumaNode : '))+"\t\t"+str(dev.get('Descrition : ')))

    return

def main():
    nics()

if __name__ == "__main__":
    main()

