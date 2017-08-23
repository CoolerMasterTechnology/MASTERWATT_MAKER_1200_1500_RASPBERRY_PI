import sys,json
from PSU_API import MasterWatt1200W

if __name__ == '__main__':

    if len(sys.argv) < 2:
        try:
            PSU = MasterWatt1200W()
            print json.dumps(PSU.getData())
        except:
            print json.dumps({"Status":"Serial port Unavailable"})

    else:
        try:
            PSU = MasterWatt1200W(sys.argv[1])
            print json.dumps(PSU.getData())
        except:
            print json.dumps({"Status": "Serial port Unavailable"})