#!/usr/bin/env python

"""Tests for `retry_module` package."""

import unittest

from retry_module.decorators import retry


class TestRetry_module(unittest.TestCase):
    """Tests for `retry_module` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_retry(self):
        """Test max retiries on exception."""
        retries = [0]
        max_tries = 5

        @retry(Exception, max_retires=5)
        def f():
            retries[0] += 1
            raise Exception("Faulty function")

        with self.assertRaises(Exception):
            f()

        self.assertEqual(max_tries, retries[0])
