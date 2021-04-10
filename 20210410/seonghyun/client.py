from block import *
from socket import *
import pickle
from ende import *

port = 4444
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

block_chain = [create_genesis_block()]
cnt = 0

while True:
    input_data = str(input('데이터 입력 : '))
    new_block = next_block(block_chain[len(block_chain) - 1],
                           encrypt(input_data, block_chain[-1].hash))
    block_chain.append(new_block)
    sendData = pickle.dumps(new_block)
    clientSock.send(sendData)
    print('현재 체인 상태 : ' + str(block_chain) + '\n')
    for bn in range(len(block_chain)):
        if bn == 0:
            continue
        block = block_chain[bn]
        print("블록넘: {}\n블록해시: {}\n시간: {}\n암호화된 데이터: {}\n복호화된 데이터: {}\n" \
              .format(block.index, block.hash, block.time,
                      block.data, decrypt(block.data, block_chain[bn-1].hash)))

    recvData = pickle.loads(clientSock.recv(1024))
    block_chain.append(recvData)
    print('서버 블록 생성 :', recvData)
    print('현재 체인 상태 : ' + str(block_chain) + '\n')
    for bn in range(len(block_chain)):
        if bn == 0:
            continue
        block = block_chain[bn]
        print("블록넘: {}\n블록해시: {}\n시간: {}\n암호화된 데이터: {}\n복호화된 데이터: {}\n" \
              .format(block.index, block.hash, block.time,
                      block.data, decrypt(block.data, block_chain[bn-1].hash)))

    pre_data = decrypt(block_chain[-2].data, block_chain[-3].hash).decode('utf-8')
    now_data = decrypt(block_chain[-1].data, block_chain[-2].hash).decode('utf-8')

    cnt += 1
    if pre_data == now_data:
        print('******************* ', str(cnt), '번째 cycle *******************')
        print('이전 데이터 : ', pre_data, '\n다음 데이터 : ', now_data)
        print('True')
        print('****************************************************\n')
    else:
        print('******************* ', str(cnt), '번째 cycle *******************')
        print('False')
        print('****************************************************\n')

