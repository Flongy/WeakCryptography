import numpy as np
from weakcrypto import BaseCrypto


class ShiftCryptoNumPy(BaseCrypto):
    """ Shift cipher (Ceasar cipher) using numpy """
    def __init__(self, shift_value=9):
        self.shift = shift_value

    @staticmethod
    def __encode_text(text: str):
        """ Convert string text to int numpy array.
        Also prepare a mask of characters that are used in shifting (can't shift non-alpha symbols yet)
        """
        ns = np.copy(np.frombuffer(text.lower().encode('ascii'), dtype=np.uint8))
        char_mask = np.logical_and(ns >= ord('a'), ns <= ord('z'))
        return ns, char_mask

    @staticmethod
    def __decode_text(arr: np.ndarray):
        """ Convert numpy array to string """
        return arr.tobytes().decode('ascii')

    def encrypt(self, text: str):
        """ Encrypt text into ciphertext """
        ns, char_mask = self.__encode_text(text)

        ns[char_mask] += self.shift                         # shift right
        ns[np.logical_and(ns > ord('z'), char_mask)] -= 25  # overflow correction
        return self.__decode_text(ns)

    def decrypt(self, ciphertext: str):
        """ Decrypt ciphertext into plain text """
        ns, char_mask = self.__encode_text(ciphertext)

        ns[char_mask] -= self.shift                         # shift left
        ns[np.logical_and(ns < ord('a'), char_mask)] += 25  # overflow correction
        return self.__decode_text(ns)


if __name__ == "__main__":
    """ Testing the module """
    test_string = "Hello GitHub! Testing your code is always important.".lower()    # No upper letters yet

    # Testing Shift Cipher NumPy
    crypto = ShiftCryptoNumPy()  # Default shift - 9
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"

    crypto = ShiftCryptoNumPy(3)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"
    print("[SUCCESS] Shift Cipher NumPy")
