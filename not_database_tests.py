from not_database import *
from nose.tools import *
from travel_plans.csv import *


def test_check_login():
    assert check_login('prae6', 'jingjing') == True
    assert check_login('j.faulkner', 'montfort') == False
    assert check_login('nadiamounzih', 'Krabi') == False
    
