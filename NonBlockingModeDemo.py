#===============================================
# Cooler Master Technology Power Supply
# For Master Watt Maker
# Non-Blocking Mode Demo
# Version: Release v1.00
# Aug, 23 2017
#===============================================

import time,sys
from PSU_API import MasterWatt1200W

if __name__ == '__main__':

    # initial
    PSU = MasterWatt1200W()

    while (True):
        # Non Blocking Mode, with 10 secs timeout
        data = PSU.getData(timeout=10)

        if(data != None):
            sys.stdout.write("[%s] " % data["TimeStamp"])
            sys.stdout.write("Input AC:[%.1fV] [%.1fA] " % (data["input_AC_Voltage"], data["input_AC_Current"]))
            sys.stdout.write("FanSpeed:[%.0frpm] " % data["fan_rpm"])
            sys.stdout.write("Temperature:[%.1fC] " % data["temperature"])
            sys.stdout.write("PFC:[%s%%] " % data["pfc"])
            sys.stdout.write("Output DC 12V1:[%.1fV] [%.1fA] " % (data["output_DC_12V1_Voltage"], data["output_DC_12V1_Current"]))
            sys.stdout.write("12V2:[%.1fV] [%.1fA] " % (data["output_DC_12V2_Voltage"], data["output_DC_12V2_Current"]))
            sys.stdout.write("5V:[%.1fV] [%.1fA] " % (data["output_DC_5V_Voltage"], data["output_DC_5V_Current"]))
            sys.stdout.write("5Vsb:[%.1fV] [%.1fA] " % (data["output_DC_5Vsb_Voltage"], data["output_DC_5Vsb_Current"]))
            sys.stdout.write("3.3V:[%.1fV] [%.1fA]\n" % (data["output_DC_3d3V_Voltage"], data["output_DC_3d3V_Current"]))