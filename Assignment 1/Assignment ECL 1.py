import RPi.GPIO as GPIO
import time
# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable warnings

# Define the LED pin (BCM numbering)
LED_PIN = 18  

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    print("Controlling LED (Press CTRL+C to exit)")
    while True:
        # Turn LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  
        
        # Turn LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  

except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    GPIO.cleanup()