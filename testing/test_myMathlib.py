import myMathlib
import pytest
import sys


# you can run (pytest -v) to run the test in terminal

# you can skip methods as like this
@pytest.mark.skip(reason='not usable')
def test_cal_add2():
    result = myMathlib.cal_add(4, 5)
    assert result == 9


@pytest.mark.skipif(sys.version_info > (3,5), reason='not version')
def test_cal_add():
    result = myMathlib.cal_add(4, 5)
    assert result == 9


def test_cal_deduct():
    result = myMathlib.cal_deduct(4, 5)
    assert result == -1


# if we want to run deduct1, deduct2 methods only
# pytest -k deduct -v (this run all the test cases wich has deduct in their name)

# in here we mark the test by mac
# in order to run test which marks as mac pytest -m mac -v
# if we ant to run all others not mac pytest -m "not mac" -v
@pytest.mark.mac
def test_cal_add():
    result = myMathlib.cal_add(4, 5)
    assert result == 9


# when we have repeating line as db connections we can add those into def setup_module(module)
# for eg db connections for query testing
# we have def teardown_module(module) method to close what ever the thing we need to close after test cases as db connections


