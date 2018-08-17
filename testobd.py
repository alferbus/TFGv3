import obd

ports = obd.scan_serial()

print(ports)
obd.logger.setLevel(obd.logging.DEBUG)
#connection = obd.OBD(portstr=ports[0], baudrate=10400, fast=False)
connection = obd.OBD('/dev/rfcomm0',baudrate=10400, fast=False)
