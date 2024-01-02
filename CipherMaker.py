class CipherMaker:

    __ALPHA = "abcdefghijklmnopqrstuvwxyz"
    __ALPHA_LIST = None

    def __init__(self):
        self.__ALPHA_LIST = list(self.__ALPHA)

    def decrypt(self, key, text):
        return self.__key_operations(key, text, True)

    def encrypt(self, key, text):
        return self.__key_operations(key, text, False)

    def __key_operations(self, key, text, decrypt):

        if decrypt:
            key = 26 - key

        text = text.lower()
        new = [None] * len(text)

        for idx, char in enumerate(text):

            if char not in self.__ALPHA_LIST:
                new[idx] = char
                continue

            new_idx = self.__ALPHA_LIST.index(char)
            new[idx] = self.__ALPHA_LIST[(new_idx + key) % 26]

        return ''.join(new).upper()       