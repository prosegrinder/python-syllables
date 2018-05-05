# -*- coding: utf-8 -*-

import pkg_resources

__version__ = pkg_resources.resource_string(
    'syllables', 'VERSION').decode('utf-8').strip()

