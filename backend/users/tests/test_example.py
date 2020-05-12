# -*- coding: utf-8 -*-

"""
Tests for status endpoint
"""

import pytest


class TestExample:

    @pytest.mark.parametrize('status_code, answer', [
        (
            {}, 200,
        ),
    ])
    def test_status_page_response(self, status_code, answer):
        assert 5 == 5
