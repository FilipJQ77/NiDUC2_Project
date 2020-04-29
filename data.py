import random
import crc
import hamming
import repetition


# generates given amount of random data
def generate_random_data(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        bits.append(random.randint(0, 1))
    return bits


# prints data generated with generate_random_data
def print_data(bits: list):
    print(f"Data of a list with id: {id(bits)}: [", end='')
    for bit in bits:
        print(bit, end='')
    print("]")


# separates data into blocks of size n, returns a list of lists, where each inside list is a block of data
def separate_data(bits: list, n: int) -> list:
    i = 0
    complete_data = []
    block_of_data = []
    for bit in bits:
        i += 1
        block_of_data.append(bit)
        if i == n:
            i = 0
            complete_data.append(block_of_data)
            block_of_data = []

    # if we still have some data which wasn't added, we fill it with 0s until it has a size of n
    if block_of_data:
        length = len(block_of_data)
        for i in range(length, n):
            block_of_data.append(0)
        complete_data.append(block_of_data)
    return complete_data


# basic distortion of a single bit, probability is in range [0,100]
def distort_bit(bit: int, probability: int) -> int:
    rand = random.randint(0, 100)
    if rand >= probability:
        if bit == 0:
            bit = 1
        else:
            bit = 0
    return bit


# basic distortion of data, probability is in range [0,100] todo pomyśleć nad innymi implementacjami
def distort_bits(bits: list, probability: int) -> list:
    size = len(bits)
    for i in range(0, size):
        bits[i] = distort_bit(bits[i], probability)
    return bits


# encodes a block of data with a given type of code
def encode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "R":
        block_of_data = repetition.encode_repetition(block_of_data)
    elif code_type == "C":
        block_of_data = crc.encode_crc(block_of_data)
    elif code_type == "H":
        block_of_data = hamming.encode_hamming(block_of_data)
    return block_of_data


def decode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "R":
        block_of_data = repetition.decode_repetition(block_of_data)
        pass
    elif code_type == "C":
        block_of_data = crc.decode_crc(block_of_data)
        pass
    elif code_type == "H":
        block_of_data = hamming.decode_hamming(block_of_data)
        pass
    return block_of_data


# todo zwraca co się stało tzn. czy wiadomość odebrana była poprawna, czy wykryto błąd, naprawiono błąd itp.
def sending_data(bits: list, block_size: int, code_type: str, probability: int) -> str:
    separated_data = separate_data(bits, block_size)
    data_size = len(separated_data)
    sent_data = []
    for block in separated_data:
        sent_data.append(encode_data(block, code_type))
    for i in range(data_size):
        sent_data[i] = distort_bits(sent_data[i], probability)
    decoded_data = []
    # block_results = ["" for x in range(data_size)]
    for i in range(data_size):
        while True:
            decoded_data.append(decode_data(sent_data[i], code_type))
            if (decoded_data[-1])[-1] == "F":
                # block_results[i] += "F"
                decoded_data[-1].pop()
                break
            elif (decoded_data[-1])[-1] == "R":
                # block_results[i] += "R"
                decoded_data[-1].pop()
            else:
                # block_results[i] += "C"  # correct
                break
    # len(block_results)
    data_results = {"Correct": 0, "Fixed correctly": 0, "Fixed wrongly": 0, "Didn't detect error": 0}
    for i in range(data_size):
        if separated_data[i] == decoded_data[i]:
            data_results["Correct"] += 1
            # todo wtedy jest correct itd dla każdego przypadku
            pass

    return data_results
