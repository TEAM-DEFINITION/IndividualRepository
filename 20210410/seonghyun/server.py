from block import *
from socket import *
import pickle
from ende import *

port = 4444
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...' % port)
connectionSock, addr = serverSock.accept()
# print(str(addr), '에서 접속되었습니다.')

block_chain = [create_genesis_block()]

while True:
    recvData = pickle.loads(connectionSock.recv(1024))
    block_chain.append(recvData)
    print('클라이언트 블록 생성 :', recvData)
    print('현재 체인 상태 : ' + str(block_chain) + '\n')
    for bn in range(len(block_chain)):
        if bn == 0:
            continue
        block = block_chain[bn]
        print("블록넘: {}\n블록해시: {}\n시간: {}\n암호화된 데이터: {}\n복호화된 데이터: {}\n" \
              .format(block.index, block.hash, block.time,
                      block.data, decrypt(block.data, block_chain[bn - 1].hash)))
    input()
  # input_data = str(input('데이터 입력 : '))
    new_block = next_block(block_chain[len(block_chain) - 1],
                           encrypt(decrypt(block_chain[-1].data, block_chain[-2].hash).decode('utf-8'), block_chain[-1].hash))
    block_chain.append(new_block)
    sendData = pickle.dumps(new_block)
    connectionSock.send(sendData)
    print('현재 체인 상태 : ' + str(block_chain) + '\n')
    for bn in range(len(block_chain)):
        if bn == 0:
            continue
        block = block_chain[bn]
        print("블록넘: {}\n블록해시: {}\n시간: {}\n암호화된 데이터: {}\n복호화된 데이터: {}\n" \
              .format(block.index, block.hash, block.time,
                      block.data, decrypt(block.data, block_chain[bn - 1].hash)))
