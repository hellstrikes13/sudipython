import sys
def absolute_value(n):
 if n < 0:
  return 1
 elif n > 0:
  return n
 else:
  return n

def test(did_pass):
 ln = sys._getframe(1).f_lineno
 if did_pass:
  msg = "TEST at line no %r OK" %ln
 else:
  msg = "TEST at line no %r Failed" %ln
 print msg
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite()
