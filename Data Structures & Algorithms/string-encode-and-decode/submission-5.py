import string

class Solution:
    def encode(self, strs: List[str]) -> str:
        hashmap = {letter : i + 1 for i, letter in enumerate(string.ascii_letters + string.digits + string.punctuation + ' ')}
        encoded_string = []

        for i in strs:
            for j in i:
                encoded_string.append(str(hashmap[j]))
                encoded_string.append('#')
            encoded_string.append('@')
        print(encoded_string)
        return ''.join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        hashmap = {i + 1 : letter for i, letter in enumerate(string.ascii_letters + string.digits + string.punctuation + ' ')}        # print(hashmap)
        decoded_strs = []

        for j in s.split('@')[:-1]:
            word = []
            
            for i in j.split('#')[:-1]:
                i = int(i)
                letter = hashmap[i]
                word.append(letter)
            decoded_strs.append(''.join(word))
        return decoded_strs