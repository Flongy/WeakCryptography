class BaseCrypto:
    """ Base class. All algorithms have to implement encrypt and decrypt methods """
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
        if ord('a') <= character <= ord('z'):
            character += self.shift
            if character > ord('z'):
                character -= 25
        return character

    def __lshift_character(self, character: int):
        """ Shift character LEFT (overflowing characters cycle over starting with a 'z') """
        if ord('a') <= character <= ord('z'):
            character -= self.shift
            if character < ord('a'):
                character += 25
        return character

    @staticmethod
    def encode_text(text: str):
        """ Convert string var into a list of characters as ints """
        return list(text.lower().encode("ascii"))

    @staticmethod
    def decode_text(lst):
        """ Convert list of ints (characters) to string """
        return bytes.decode(bytes(lst))

    def encrypt(self, text: str):
        """ Encrypt text into ciphertext """
        char_as_int_list = self.encode_text(text)
        shifted_char_list = map(self.__rshift_character, char_as_int_list)
        ciphertext = self.decode_text(shifted_char_list)
        return ciphertext

    def decrypt(self, ciphertext):
        """ Decrypt ciphertext into plain text """
        char_as_int_list = self.encode_text(ciphertext)
        shifted_char_list = map(self.__lshift_character, char_as_int_list)
        text = self.decode_text(shifted_char_list)
        return text


if __name__ == "__main__":
    """ Testing the module """
    test_string = "Hello GitHub! Testing your code is always important.".lower()    # No upper letters yet

    # Testing Shift Cipher
    crypto = ShiftCrypto()  # Default shift - 9
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"

    crypto = ShiftCrypto(3)
    assert test_string == crypto.decrypt(crypto.encrypt(test_string)), "Shift cipher"
    print("[Shift cipher] success")
