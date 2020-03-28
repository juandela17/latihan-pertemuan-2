import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

GPIO.output(3, GPIO.HIGH)
print("Led 1 Must Be On")
time.sleep(1)
print("Led 1 Must Be Off")
GPIO.output(3, GPIO.LOW)

GPIO.output(5, GPIO.HIGH)
print("Led 2 Must Be On")
time.sleep(1)
print("Led 2 Must Be Off")
GPIO.output(5, GPIO.LOW)

GPIO.output(7, GPIO.HIGH)
print("Led 3 Must Be On")
time.sleep(1)
print("Led 3 Must Be Off")
GPIO.output(7, GPIO.LOW)

GPIO.cleanup()