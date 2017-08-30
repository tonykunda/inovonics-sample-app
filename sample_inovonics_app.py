import ino_com
import logging

log = logging
logFormat = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
log.basicConfig(format=logFormat, level="DEBUG")

inovonics = ino_com.InovonicsCommunication('/dev/ttyUSB0', log)
inovonics.start_processing()

while True:
    # Get the next inovoincs event in the queue
    event = inovonics.event_queue.get()
    # Do something with the event
    log.debug(event)
    if "Alarm 1" in event['status']:
        log.info("******Alarm Detected on Serial Number %s********" % event['uid'])
