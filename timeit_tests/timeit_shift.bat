@echo off
SETLOCAL EnableDelayedExpansion
set TEST_STR1=Hello, world!
set "TEST_STR2="
for /f "delims=" %%x in (timeit_tests\lorem.txt) do set "TEST_STR2=!TEST_STR2!%%x"

ECHO CAESAR CIPHER SPEED TESTS
ECHO Encryption with default shift
python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto()" "crypto.encrypt('''%TEST_STR1%''')"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy()" "crypto.encrypt('''%TEST_STR1%''')"

python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto()" "crypto.encrypt('''%TEST_STR2%''')"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy()" "crypto.encrypt('''%TEST_STR2%''')"
ECHO ==============================

ECHO Encryption with shift = 3
python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto(3)" "crypto.encrypt('''%TEST_STR1%''')"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy(3)" "crypto.encrypt('''%TEST_STR1%''')"

python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto(3)" "crypto.encrypt('''%TEST_STR2%''')"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy(3)" "crypto.encrypt('''%TEST_STR2%''')"
ECHO ==============================


ECHO Decryption with default shift
python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto();ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy();ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"

python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto();ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy();ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
ECHO ==============================

ECHO Decryption with shift = 3
python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto(3);ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy(3);ciphertext = crypto.encrypt('''%TEST_STR1%''')" "crypto.decrypt(ciphertext)"

python -m timeit -s "from weakcrypto import ShiftCrypto;crypto = ShiftCrypto(3);ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
python -m timeit -s "from weakcrypto_numpy import ShiftCryptoNumPy;crypto = ShiftCryptoNumPy(3);ciphertext = crypto.encrypt('''%TEST_STR2%''')" "crypto.decrypt(ciphertext)"
ECHO ==============================
