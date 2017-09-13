from .. import core
from .. import models


def test_whether_octopus_is_generic():
    for bad_word in ["Prior", "Likelihood"]:
        assert(bad_word not in dir(models))
        assert(bad_word not in dir(core))
