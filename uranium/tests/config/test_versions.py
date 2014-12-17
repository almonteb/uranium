from uranium.config import Config
from .utils import get_valid_config
from nose.tools import eq_


class TestVersions(object):

    def setUp(self):
        config = get_valid_config()
        self.config_dict = config
        self.config = Config(config)

    def test_invalid_phase_name(self):
        self.config['versions'] = {
            'sprinter': "@!} whaat"
        }
        warnings, errors = self.config.validate()
        eq_(len(errors), 1)
