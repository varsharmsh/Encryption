class CeasarCipher:
    def __init__(self, plaintext, shift):
        self.name = "Ceasar Cipher"
        self.description = "Shift wise encryption"
        self.plaintext = plaintext
        self.shift = shift
        self.ciphertext = ""
        assert isinstance(plaintext, str), "Plain text has to be a string"
        assert isinstance(shift, int), "Shift has to be an integer"

    def __del__(self):
        pass

    def encrypt(self, shift=None, lowercase=False, uppercase=False):
        shift = shift if shift else self.shift
        for c in self.plaintext:
            if lowercase:
                self.ciphertext += chr(ord(c.lower()) + shift)
            elif uppercase:
                self.ciphertext += chr(ord(c.upper()) + shift)
            else:
                self.ciphertext += chr(ord(c) + shift)
        return self.ciphertext


if __name__ == '__main__':
    x = CeasarCipher("something", 2)
    print(x.encrypt(uppercase=True))
