import hashlib
import datetime


class Block:
    key = ''

    def __init__(self, index, time, data, previous_hash):
        self.previous_hash = previous_hash
        self.index = index
        self.time = time
        self.data = data
        self.hash = hashlib.sha256((str(self.index) + str(self.time) \
                                    + str(self.data) + str(self.previous_hash)).encode("utf-8")).hexdigest()

    # def mine(self):
    #     nonce = 0
    #     while not self.valid_nonce(nonce):
    #         nonce += 1
    #     print("새 블록 생성 됨: {}".format(self.hash))
    #
    # def valid_nonce(self, nonce):
    #     self.nonce = nonce
    #     self.hash = self.get_block_hash()
    #     i = 1
    #     for c in self.hash:
    #         if (c != "0"):
    #             return False
    #
    #         if (i is self.bits):
    #             return True
    #         i += 1
def create_genesis_block():
    return Block(0, 0, 0, 0)


def next_block(prev_block, data):
    index = prev_block.index + 1
    time = datetime.datetime.now()
    previous_hash = prev_block.hash
    block = Block(index, time, data, previous_hash)
    return block
