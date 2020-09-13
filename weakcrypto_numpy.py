import numpy as np
from weakcrypto import BaseCrypto, ORD_A, ORD_Z


class BaseCryptoNumPy(BaseCrypto):
    @staticmethod
    def _encode_text(text: str):
        """ Convert string text to int numpy array.
        Also prepare a mask of characters that are used in shifting (can't shift non-alpha symbols yet)
        """
        ns = np.copy(np.frombuffer(text.lower().encode('ascii'), dtype=np.uint8))
        char_mask = np.logical_and(ns >= ORD_A, ns <= ORD_Z)
        return ns, char_mask

    @staticmethod
    def _decode_text(arr: np.ndarray):
        """ Convert numpy array to string """
        return arr.tobytes().decode('ascii')


class ShiftCryptoNumPy(BaseCryptoNumPy):
    """ Shift cipher (Ceasar cipher) using numpy """
    def __init__(self, shift_value=9):
        self.shift = shift_value

    def encrypt(self, text: str):
        """ Encrypt text into ciphertext """
        ns, char_mask = self._encode_text(text)

        ns[char_mask] += self.shift                         # shift right
        ns[np.logical_and(ns > ORD_Z, char_mask)] -= 25  # overflow correction
        return self._decode_text(ns)

    def decrypt(self, ciphertext: str):
        """ Decrypt ciphertext into plain text """
        ns, char_mask = self._encode_text(ciphertext)

        ns[char_mask] -= self.shift                         # shift left
        ns[np.logical_and(ns < ORD_A, char_mask)] += 25  # overflow correction
        return self._decode_text(ns)


class MultiAlphabetCryptoNumPy(BaseCryptoNumPy):
    """ MultiAlphabet Cipher NumPy
    Using table with 32 randomly picked shift combinations """
    def __init__(self, seed: int = 42, alphabet_num: int = 32):
        self.seed = seed
        if self.seed is not None:
            np.random.seed(self.seed)

        self.alphabet_num = alphabet_num

        table = np.empty([self.alphabet_num, 26], dtype=np.uint8)
        for i in range(self.alphabet_num):
            table[i] = np.random.permutation(26)
        self.table = table
        self._dtable = None

    @classmethod
    def from_table(cls, table: np.ndarray):
        """ Construct a Crypto Object with the table of shifts """
        crypto = cls()
        crypto.table = table
        return crypto

    def _get_dtable(self):
        """ Calculate table for decryption """
        if self._dtable is None:
            self._dtable = np.argsort(self.table)
        return self._dtable

    def _process_text(self, text: str, table: np.ndarray):
        """ Use table to shift characters (encryption and decryption use same algorithm, just different tables) """
        ns, char_mask = self._encode_text(text)
        char_idx = np.where(char_mask)[0]
        ns[char_mask] -= ORD_A

        arange = np.arange(self.alphabet_num)

        idx_slices = []

        for i in range(0, char_idx.size, self.alphabet_num):
            idx_slices.append(char_idx[i:i + self.alphabet_num])

        for idx in idx_slices[:-1]:
            ns[idx] = table[arange, ns[idx]]
        else:
            idx = idx_slices[-1]
            ns[idx] = table[np.arange(idx.size), ns[idx]]

        # # More straightforward method:
        # for i in range(0, char_idx.size, self.alphabet_num):
        #     idx_slice = char_idx[i:i+self.alphabet_num]
        #     temp_slice = ns[idx_slice]
        #     ns[idx_slice] = table[arange[:temp_slice.size], temp_slice]
        #     # ns[idx_slice] = table[np.arange(temp_slice.size), temp_slice]

        ns[char_mask] += ORD_A
        return self._decode_text(ns)

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

    # Testing Shift Cipher NumPy
    crypto = ShiftCryptoNumPy()  # Default shift - 9
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift Cipher NumPy"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "Shift Cipher NumPy. Big String"

    crypto = ShiftCryptoNumPy(3)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift Cipher NumPy: shift - 3"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "Shift Cipher NumPy. Big String: shift - 3"
    print("[SUCCESS] Shift Cipher NumPy")

    # Testing MultiAlphabet Cipher NumPy
    crypto = MultiAlphabetCryptoNumPy()
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet Cipher NumPy"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet Cipher NumPy. Big String"

    crypto = MultiAlphabetCryptoNumPy(alphabet_num=64)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet Cipher NumPy: alphabet_num - 64"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet Cipher NumPy. Big String: alphabet_num - 64"

    crypto = MultiAlphabetCryptoNumPy.from_table(crypto.table)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "MultiAlphabet Cipher NumPy: from table"
    assert big_test_string == crypto.decrypt(crypto.encrypt(big_test_string)), "MultiAlphabet Cipher NumPy. Big String: from table"

    crypto = MultiAlphabetCryptoNumPy(1)
    encrypted = crypto.encrypt(test_string)
    crypto = MultiAlphabetCryptoNumPy(1)
    decrypted = crypto.decrypt(encrypted)
    assert test_string == decrypted, "MultiAlphabet Cipher NumPy: encryption and decryption with different objects"
    print("[SUCCESS] MultiAlphabet Cipher NumPy")
