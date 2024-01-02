from DetectEnglish import DetectEnglish 
from CipherMaker import CipherMaker

class CipherBreaker:

    __english_detector : DetectEnglish = None 
    __cipher_maker : CipherMaker = None

    def __init__(self, cipher_maker : CipherMaker):

        self.__english_detector = DetectEnglish()
        self.__cipher_maker = cipher_maker

    def caesar_brute_force(self, text: str):

        for key in range(26):
            
            plaintext = self.__cipher_maker.decrypt(key, text).lower()
            if self.__english_detector.is_english(plaintext):
                return key, plaintext

        return 0, "failed"
    
#cipher_maker = CipherMaker()
#cipher_breaker = CipherBreaker(cipher_maker)
#print(cipher_breaker.caesar_brute_force("MJQQT RD SFRJ NX"))