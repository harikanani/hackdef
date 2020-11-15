import hashlib as hl
import json
from collections import OrderedDict


genesis_block = {'previous_hash': '','index': 0,'transactions': [],'proof': 100}
blockchain =[]
open_transaction = []
wallet = 'abhi'


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block): #creats has using previous block to verify block chian and mine them and add them into blockchain
#    # hashed_block = '-'.join(str(last_block[key]) for key in last_block)
    hashable_block = block.copy()
    hashable_block['transactions'] = [OrderedDict([('sender',tx['sender']),('recipient',tx['recipient'])]) for tx in hashable_block['transactions']]

    return hash_string_256(json.dumps(hashable_block,sort_keys=True).encode())


def proof_of_work():
        last_block = blockchain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not valid_proof(open_transaction,last_hash , proof):
            proof += 1
        return proof


def valid_proof(trasnsaction,last_hash,proof):
        guess = (str([OrderedDict([('sender',tx['sender']),('recipient',tx['recipient'])]) for tx in trasnsaction]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'


def get_last_block_chain_value(self): # get last block value and for empty block chain return none data type
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient,sender): #add new block to the open transaction  
    transaction ={
        'sender' : sender,              
        'recipient' : recipient,        #creates an block of the datas
        'amount' : amount
    }
        # transaction = OrderedDict([
        #     ('sender',sender),
        #     ('recipient',recipient),
        #     ('amount',amount)
        # ]) 
    if  Verification.verify_transaction(transaction,self.get_balance):     #verify transaction iff the semder has enough balance to send
        self.__open_transaction.append(transaction)
        # participants.add(sender)    #add the participents if the are not avalable
            # participants.add(recipient)
        self.save_data()
        return True
    return False
        # blockchain.append([last_transaction,transaction_amount])


while True:
    choice = input('1.vote\n2.block\n3.exit')
    if(choice==1):
        recipient = input('recipent address:')

    elif(choice==3):
        break