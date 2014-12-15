from .utils import assert_condition

KEY = "eggs"


class Eggs(object):

    def _initialize(self):
        self[KEY] = self.get(KEY, {})

    def _validate(self, errors):
        assert_condition(
            errors, isinstance(self[KEY], dict),
            "eggs must be a dict! found {0} instead.".format(type(self[KEY]))
        )

    @property
    def eggs(self):
        return self[KEY]
