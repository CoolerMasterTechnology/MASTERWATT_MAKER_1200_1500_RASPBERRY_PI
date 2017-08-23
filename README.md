# MASTERWATT_MAKER_1200_1500_RASPBERRY_PI

## Installation

```
wget https://github.com/CoolerMasterTechnology/MASTERWATT_MAKER_1200_1500_RASPBERRY_PI/archive/master.zip
unzip master.zip
sudo apt-get install python-serial
```
## Requirement
* pyserial (for Python)
* python-shell (for Node.JS)
  * ```npm install python-shell```

* #Enable Serial (on Raspberry Pi)

## Monitoring for Python
### Blocking Mode
```python BlockingModeDemo.py```  

### Non-Blocking Mode
##### Require set timeout. (Default: 10 seconds)  
```python NonBlockingModeDemo.py```

## Monitoring for Node.js
```node NodeApp.js```

## PSU_API Reference
* MasterWatt1200W()  <-- Constructor. Defalut: **MasterWatt1200W(serialPort = "/dev/ttyAMA0")**
* currentVersion()   <-- Get Current Version by String.
* getData()          <-- Get Current Power Supply Monitor Data by Dictionary.

## Wire Connection
![Wire Connection](https://raw.githubusercontent.com/CoolerMasterTechnology/MASTERWATT_MAKER_1200_1500_RASPBERRY_PI/master/Image/wire_connection.png)

## Raspberry Pi GPIO pins
![Raspberry Pi GPIO pins](https://cdn-images-1.medium.com/max/1000/1*QlSyHfcfNu4ePpNoNtKcZQ.jpeg)
