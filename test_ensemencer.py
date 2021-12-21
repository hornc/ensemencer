from ensemencer import seed, read, read32


def test_0seed_32bit():
    seed(0)
    assert read32() == 2357136044
    assert read32() == 2546248239
    assert read32() == 3071714933


def test_1seed_32bit():
    seed(1)
    assert read32() == 1791095845 
    assert read32() == 4282876139
    assert read32() == 3093770124


def test_highseed_32bit():
    seed(2**32 + 1)
    assert read32() == 953453411 
    assert read32() == 236996814
    assert read32() == 3739766767


def test_seed_8bit():
    # read() returns the MSB
    seed(0)
    r = read()
    assert r == 140


def test_test_command():
    # Test returns the LS-bit
    seed(0)
    assert not read32() & 1
    assert read32() & 1
    assert read32() & 1
