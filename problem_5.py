import hashlib
import datetime
from datetime import timezone as tz
import uuid


class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        salt = uuid.uuid4().hex
        hash_str = (self.data + salt).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest() + ":" + salt

    def validate_hash(self, hashed_text):
        sha = hashlib.sha256()
        hashd, salt = hashed_text.split(':')
        hash_str = (self.data + salt).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest() == hashd

    def __str__(self):
        return "Block {}:\t created at {}\t has data \"{}\"\t hash value {}\t and previous hash {}\t" \
            .format(self.index, self.timestamp, self.data, self.hash, self.previous_hash)


class Blockchain(object):
    def __init__(self):
        timestamp = datetime.datetime.now(tz.utc)
        genesis_block = Block(0, timestamp, "genesis", "0")
        genesis_block.next = None
        self.genesis = genesis_block
        self.tail = None
        return

    def append(self, data):

        timestamp = datetime.datetime.now(tz.utc)

        # appending when only the genesis block is available
        if self.genesis.next is None:
            new_block = Block(1, timestamp, data, self.genesis.hash)
            self.genesis.next = new_block
            new_block.next = None
            self.tail = new_block

        new_block = Block(self.tail.index + 1, timestamp, data, self.tail.hash)
        new_block.next = None
        self.tail.next = new_block
        self.tail = new_block
        return

    def validate_chain(self):
        if self.tail is None:
            return True

        current_block = self.genesis
        next_block = current_block.next

        while current_block.next is not None:
            current_block_hash = current_block.hash
            next_block_previous_hash = next_block.previous_hash
            if current_block_hash != next_block_previous_hash:
                return False
            current_block = current_block.next
            next_block = current_block.next

        return True

    def to_list(self):
        out = []
        genesis_block = self.genesis

        if self.tail is None:
            out.append(self.genesis)

        tail_block = genesis_block

        while tail_block.next is not None:
            out.append(tail_block)
            tail_block = tail_block.next

        out.append(self.tail)
        return out


def test_validate_hash(test_case):
    blck = test_case[0]
    hash_value = test_case[1]
    expected_answer = test_case[2]
    evaluated_answer = blck.validate_hash(hash_value)

    if expected_answer == evaluated_answer:
        print("PASS")
        return
    else:
        print("FAIL")
        return


block = Block(0, datetime.datetime.now(tz.utc), "hello", "00")
block1 = Block(0, datetime.datetime.now(tz.utc), "hello", "00")
block2 = Block(0, datetime.datetime.now(tz.utc), "hello udacity", "00")
block3 = Block(0, datetime.datetime.now(tz.utc), "", "00")
block4 = Block(0, datetime.datetime.now(tz.utc), "", "00")
test_case0 = [block, block1.calc_hash(), True]
test_case1 = [block, block2.calc_hash(), False]
test_case2 = [block3, block4.calc_hash(), True]
test_validate_hash(test_case0)
test_validate_hash(test_case1)
test_validate_hash(test_case2)


# test_case is an array that contains the blockchain to be tested at index 0
# and the expected answer at index 1
# the method evaluate the blockchain then compares the evaluated answer and
# the expected answer, print PASS if they match or FAIL if they don't
def test_chain_validity(test_case):
    blockchain = test_case[0]
    expected_answer = test_case[1]
    evaluated_answer = blockchain.validate_chain()
    if expected_answer == evaluated_answer:
        print("PASS")
        return
    else:
        print("FAIL")
        return


# test blockchain that has only genesis block
blockchain1 = Blockchain()
test_case0 = [blockchain1, True]
test_chain_validity(test_case0)

# testing a blockchain where every block data is different from the other
blockchain1.append("first_block")
blockchain1.append("second_block")
test_case1 = [blockchain1, True]
test_chain_validity(test_case1)

# testing a blockchain with blocks of the same data
blockchain2 = Blockchain()
blockchain2.append("first_block")
blockchain2.append("first_block")
blockchain2.append("first_block")
blockchain2.append("first_block")
test_case2 = [blockchain2, True]
test_chain_validity(test_case2)

# testing a blockchain with blocks that have null data
blockchain3 = Blockchain()
blockchain3.append("")
blockchain3.append("")
blockchain3.append("")
blockchain3.append("")
test_case3 = [blockchain3, True]
test_chain_validity(test_case3)

# testing a blockchain with blocks that have mix of same,different and null data
blockchain4 = Blockchain()
blockchain4.append("test casing")
blockchain4.append("13141414$$%%%%%**!^!^!^!")
blockchain4.append("aaaaaa")
blockchain4.append("aaaaaa")
blockchain4.append("789652424222")
test_case4 = [blockchain4, True]
test_chain_validity(test_case4)

