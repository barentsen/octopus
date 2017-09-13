from .. import core
from .. import models


def test_whether_octopus_is_generic():
    assert("Prior" not in dir(core))
    assert("Likelihood" not in dir(core))
