import random


ORD_A = ord('a')
ORD_Z = ord('z')


class BaseCrypto:
    """ Base class. All algorithms have to implement encrypt and decrypt methods """
    @staticmethod
    def _encode_text(text: str):
        """ Convert string var into a list of characters as ints """
        return list(text.lower().encode("ascii"))

    @staticmethod
    def _decode_text(lst):
        """ Convert list of ints (characters) to string """
        return bytes(lst).decode('ascii')

    def encrypt(self, text: str):
        pass

    def decrypt(self, ciphertext: str):
        pass


class ShiftCrypto(BaseCrypto):
    """ Shift cipher (Ceasar cipher) """
    def __init__(self, shift_value=9):
        self.shift = shift_value

    def __rshift_character(self, character: int):
        """ Shift character RIGHT (overflowing characters cycle over starting with an 'a') """
        if ORD_A <= character <= ORD_Z:      # is alpha - between symbols 'a' (= 97) and 'z' (= 122)
            character += self.shift
            if character > ORD_Z:         # overflow (more than 'z')
                character -= 25
        return character

    def __lshift_character(self, character: int):
        """ Shift character LEFT (overflowing characters cycle over starting with a 'z') """
        if ORD_A <= character <= ORD_Z:      # is alpha - between symbols 'a' (= 97) and 'z' (= 122)
            character -= self.shift
            if character < ORD_A:          # overflow (less than 'a')
                character += 25
        return character

    def encrypt(self, text: str):
        """ Encrypt text into ciphertext """
        char_as_int_list = self._encode_text(text)
        shifted_char_list = map(self.__rshift_character, char_as_int_list)
        ciphertext = self._decode_text(shifted_char_list)
        return ciphertext

    def decrypt(self, ciphertext):
        """ Decrypt ciphertext into plain text """
        char_as_int_list = self._encode_text(ciphertext)
        shifted_char_list = map(self.__lshift_character, char_as_int_list)
        text = self._decode_text(shifted_char_list)
        return text


class MultiAlphabetCrypto(BaseCrypto):
    """ MultiAlphabet Cipher
    Using table with 32 randomly picked shift combinations """
    def __init__(self, seed: int = 42, alphabet_num: int = 32):
        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)

        self.alphabet_num = alphabet_num

        table = []
        for i in range(self.alphabet_num):
            table.append(list(range(26)))
            random.shuffle(table[i])
        self.table = table
        self._dtable = None

    @classmethod
    def from_table(cls, table: list):
        """ Construct a Crypto Object with the table of shifts """
        crypto = cls()
        crypto.table = table
        return crypto

    def _get_dtable(self):
        """ Calculate table for decryption """
        if self._dtable is None:
            dtable = []
            for row in self.table:
                dtable.append([])
                for i in range(26):
                    dtable[-1].append(row.index(i))
            self._dtable = dtable
        return self._dtable

    def _process_text(self, text: str, table: list):
        """ Use table to shift characters (encryption and decryption use same algorithm, just different tables) """
        char_list = self._encode_text(text)

        i = 0
        l = len(text)
        while True:
            for line in table:
                while not ORD_A <= char_list[i] <= ORD_Z:
                    i += 1
                    if i >= l:
                        return self._decode_text(char_list)
                char_list[i] = ORD_A + line[char_list[i] - ORD_A]

                i += 1
                if i >= l:
                    return self._decode_text(char_list)

    def encrypt(self, text: str):
        """ Encrypt text into ciphertext """
        return self._process_text(text, self.table)

    def decrypt(self, ciphertext: str):
        """ Decrypt ciphertext into plain text """
        return self._process_text(ciphertext, self._get_dtable())


if __name__ == "__main__":
    """ Testing the module """
    test_string = "Hello GitHub! Testing your code is always important.".lower()    # No upper letters yet
    big_test_string = open("timeit_tests/lorem.txt").read().lower()

    # Testing Shift Cipher
    crypto = ShiftCrypto()  # Default shift - 9
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "Shift cipher"

    crypto = ShiftCrypto(3)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "Shift cipher"
    print("[SUCCESS] Shift Cipher")

    # Testing Multi Alphabet Cipher
    crypto = MultiAlphabetCrypto()      # Default seed - 42
    table = crypto.table
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet cipher"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet cipher"

    crypto = MultiAlphabetCrypto(1337)  # Different seed
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet cipher"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet cipher"

    crypto = MultiAlphabetCrypto.from_table(table)  # Constructed from table
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet cipher"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet cipher"

    crypto = MultiAlphabetCrypto(1)
    encrypted = crypto.encrypt(test_string)
    crypto = MultiAlphabetCrypto(1)
    decrypted = crypto.decrypt(encrypted)
    assert test_string == decrypted, "MultiAlphabet cipher"     # Testing recreated Crypto object
    print("[SUCCESS] MultiAlphabet Cipher")
