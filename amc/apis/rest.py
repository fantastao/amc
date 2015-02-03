# -*- coding: utf-8 -*-

from cerberus import Validator


class AmcValidator(Validator):

    def _validate_isdigit(self, isdigit, field, value):
        if isdigit and not value.isdigit():
            self._error(field, 'Must be a number')
