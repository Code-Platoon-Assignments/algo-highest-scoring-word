from main import high

def test_high1():
  assert high('man i need a taxi up to ubud') == 'taxi'

def test_high2():
  assert high('what time are we climbing up the volcano') == 'volcano'

def test_high3():
  assert high('take me to semynak') == 'semynak'

def test_high4():
  assert high('aa b') == 'aa'

def test_high5():
  assert high('b aa') == 'b'

def test_high6():
  assert high('bb d') == 'bb'

def test_high7():
  assert high('d bb') == 'd'

def test_high8():
  assert high("aaa b") == "aaa"