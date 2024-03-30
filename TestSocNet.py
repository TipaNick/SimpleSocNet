import pytest
from SocNet import SocNet

def test_class_socnet_create():
	socnet = SocNet()
	assert socnet is not None