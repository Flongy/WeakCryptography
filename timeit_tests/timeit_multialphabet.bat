@echo off
SETLOCAL EnableDelayedExpansion
set TEST_STR1=Hello, world!
set "TEST_STR2="
for /f "delims=" %%x in (timeit_tests\lorem.txt) do set "TEST_STR2=!TEST_STR2!%%x"


ECHO MULTIALPHABET CIPHER SPEED TESTS
ECHO Encryption with default alphabet_num
python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto()" "crypto.encrypt('''%TEST_STR1%''')"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy()" "crypto.encrypt('''%TEST_STR1%''')"

python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto()" "crypto.encrypt('''%TEST_STR2%''')"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy()" "crypto.encrypt('''%TEST_STR2%''')"
ECHO ==============================

ECHO Encryption with alphabet_num = 64
python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto(alphabet_num=64)" "crypto.encrypt('''%TEST_STR1%''')"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy(alphabet_num=64)" "crypto.encrypt('''%TEST_STR1%''')"

python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto(alphabet_num=64)" "crypto.encrypt('''%TEST_STR2%''')"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy(alphabet_num=64)" "crypto.encrypt('''%TEST_STR2%''')"
ECHO ==============================

ECHO Decryption with default alphabet_num
python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto();ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy();ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"

python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto();ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy();ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
ECHO ==============================

ECHO Decryption with alphabet_num = 64
python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto(alphabet_num=64);ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy(alphabet_num=64);ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"

python -m timeit -s "from weakcrypto import MultiAlphabetCrypto;crypto = MultiAlphabetCrypto(alphabet_num=64);ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import MultiAlphabetCryptoNumPy;crypto = MultiAlphabetCryptoNumPy(alphabet_num=64);ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
ECHO ==============================