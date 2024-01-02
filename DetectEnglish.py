import string

class DetectEnglish:

    __word_set = None

    def __init__(self):

        self.__word_set = set(line.lower()[:-1] for line in open('/usr/share/dict/words', 'r'))
        #app.logger.info(self.__word_set)

    def remove_symbols(self, text: str):

        return text.translate({sym : '' for sym in string.punctuation})


    def count_english(self, text: list):
        count = 0
        for word in text:
            if word in self.__word_set:
                count += 1

        return count

    def is_english(self, text: str):

        text_list = self.remove_symbols(text).split()
        num_words = len(text_list)
        eng_count = self.count_english(text_list)

        percent = eng_count / num_words

        return percent >= 0.8
    

#detect_english = DetectEnglish()
#print(detect_english.is_english("yes"))