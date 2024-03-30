import pytest
from SocNet import SocNet

def test_class_socnet_create():
	socnet = SocNet()
	assert socnet is not None

def test_login1():
	# todo: finish method
	socnet = SocNet()
	assert socnet.login("admin", "password") == 1