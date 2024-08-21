from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
        # TODO
)

print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

while True:
    msg = input("YOU: ")
    if msg == 'exit':
        break

    data = {'message': msg, 'time': time.time()}
    # TODO
    producer
