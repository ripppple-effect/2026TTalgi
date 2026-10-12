import RPi.GPIO as GPIO
from time import sleep

pin = 16
MIN_DUTY = 2.0
MAX_DUTY = 12.0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50) # pin을 PWM 모드 50Hz로 사용
servo.start(0)

#서보모터는 펄스 폭(듀티비)에 따라 각도가 정해지기 때문에
#사용자 편의를 위해 각도(angle)를 듀티사이클(duty)로 변환해 사용한다.
def setAngle(angle):
    angle = max(0, min(180, angle))
    duty = MIN_DUTY + (MAX_DUTY - MIN_DUTY) * angle / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)
    # Give the servo enough time to complete a full-range movement.
    sleep(2.0)
    servo.ChangeDutyCycle(0)

if __name__ == "__main__":
    try:
        setAngle(0)
        sleep(1)
        setAngle(90)
        sleep(1)
        setAngle(50)
        sleep(1)
        setAngle(120)
        sleep(1)
        setAngle(180)
        sleep(1)
    finally:
        servo.stop()
        GPIO.cleanup()
