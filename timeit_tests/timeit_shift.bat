@echo off
set TEST_STR1=Hello, world!
set TEST_STR2=Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut quis risus pharetra, faucibus tortor at, ullamcorper massa. Fusce neque ante, faucibus sed tristique vel, cursus sed arcu. Aliquam massa velit, imperdiet et lectus ullamcorper, pulvinar scelerisque felis. Sed maximus metus sapien, eu egestas sapien mattis nec. Nulla finibus magna in fringilla commodo. Phasellus ut rutrum tortor, vel egestas ex. Quisque rhoncus venenatis augue in consectetur. Morbi consequat fermentum velit eget iaculis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris a consequat mi. Sed quis ex tristique, tincidunt libero sit amet, porttitor risus. Suspendisse sed faucibus felis, sit amet mattis nulla. Mauris ac orci facilisis, pellentesque erat ut, dignissim tellus. Integer ac molestie eros, non sodales nulla. Etiam ut tristique risus, a consequat purus. Sed sit amet facilisis odio. Suspendisse lacinia, dui quis tincidunt hendrerit, urna dolor lobortis sem, et viverra lectus erat et nisl. In auctor tortor sed auctor euismod. Nulla facilisi. Nulla facilisi. Vestibulum tincidunt egestas purus at faucibus. Donec hendrerit urna eu luctus euismod. Sed accumsan interdum odio in pharetra. Pellentesque hendrerit est est. Nam iaculis risus mi, a luctus neque vulputate ac. Nunc lorem odio, placerat sed leo eu, porta suscipit nunc. Donec sapien dolor, imperdiet et imperdiet eu, accumsan nec augue. In dapibus blandit luctus. Integer ultricies rhoncus dolor, sit amet rutrum felis. Etiam at sapien arcu. In finibus, magna sed laoreet bibendum, ligula dui gravida nisi, at malesuada orci urna eget elit. Fusce magna arcu, scelerisque at velit eu, suscipit cursus massa. Nullam lacinia vehicula neque, et mollis diam luctus a. Pellentesque ligula nisi, semper sit amet convallis quis, viverra nec lorem. Vivamus blandit scelerisque efficitur. Nulla sit amet tellus in erat maximus tincidunt. Nam tristique a lectus sed iaculis. Vivamus eget justo eget ex vehicula aliquam ultrices non massa. Vivamus accumsan semper magna, a finibus dolor tristique sit amet. Sed lacinia urna in nisl finibus luctus. Nam est justo, volutpat vestibulum iaculis id, cursus quis urna. Cras vestibulum vel dolor ut fringilla. Sed aliquet semper ultrices. Aenean dolor velit, vestibulum eget libero a, vestibulum condimentum arcu. Morbi quis lacus arcu. Vivamus scelerisque purus velit, ut dignissim nibh condimentum nec. Fusce lobortis magna a mauris tristique lacinia. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In nisi elit, ultrices in placerat quis, iaculis eu magna. In quis placerat lorem. Fusce ac mi ligula. Etiam commodo imperdiet enim at tincidunt. Etiam efficitur lacus nec erat vehicula fermentum. Fusce iaculis lectus at sodales interdum. Suspendisse vel velit nisi.


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
