#!/usr/bin/python3

def validUTF8(data):
    for i in range(len(data)):
        if data[i] >= 256:
            return False
    return True
