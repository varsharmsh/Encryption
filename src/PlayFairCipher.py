class PlayFairCipher:
    def __init__(self, key, plaintext=None):
        self._key = key.lower()
        self._ciphertext = ""
        self._plaintext = plaintext if plaintext else ""
        self._generatematrix()

    def __del__(self):
        pass

    def _generatematrix(self):
        self._key = self._key.replace(" ", "")
        self._keymatrix = [[None for i in range(5)] for j in range(5)]
        self._keydict = dict()
        language = list(map(lambda x: chr(x), range(97, 123)))
        language.remove('z')
        count = 0
        for letter in list(self._key):
            letter_index = ord(letter) - 97
            if letter_index == 25:
                letter_index, letter = 24, 'y'
            if language[letter_index]:
                self._keymatrix[int(count / 5)][count % 5] = letter
                self._keydict[letter] = (int(count / 5), count % 5)
                language[letter_index] = None
                count += 1
        for l in language:
            if l:
                self._keymatrix[int(count / 5)][count % 5] = l
                self._keydict[l] = (int(count / 5), count % 5)
                count += 1

    def _digrams(self):
        self._text_digrams = list()
        if len(self._plaintext) % 2 != 0:
            self._plaintext += 'x'
        for i in range(0, len(self._plaintext), 2):
            if self._plaintext[i + 1] == self._plaintext[i]:
                self._text_digrams.append((self._plaintext[i], 'x'))
            else:
                self._text_digrams.append(
                    (self._plaintext[i], self._plaintext[i + 1]))

    def encrypt(self, plaintext=None):
        if plaintext:
            self._plaintext = plaintext
        assert self._plaintext, "No plain text is provided"
        self._plaintext = self._plaintext.lower()
        self._plaintext = self._plaintext.replace(" ", "")
        self._digrams()
        for letter1, letter2 in self._text_digrams:
            row1, column1 = self._keydict[letter1]
            row2, column2 = self._keydict[letter2]
            if row1 == row2:
                self._ciphertext += self._keymatrix[row1][(
                    column1 + 1) % 5] + self._keymatrix[row2][(column2 + 1) % 5]
            elif column1 == column2:
                self._ciphertext += self._keymatrix[(row1 + 1) %
                                                    5][column1] + self._keymatrix[(row2 + 1) %
                                                                                  5][column2]
            else:
                self._ciphertext += self._keymatrix[row1][column2] + self._keymatrix[row2][column1]
        return self._ciphertext

if __name__ == "__main__":
    x = PlayFairCipher("playfair example", "Hide the gold in the tree stump")
    print(x.encrypt())
