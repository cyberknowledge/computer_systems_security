def xor_bytes(key_stream, message):
    length = len(key_stream)
    return bytes([key_stream[i] ^ message[i] for i in range(length)])