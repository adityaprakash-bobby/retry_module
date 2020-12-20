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

        @retry(Exception, max_retries=5)
        def f():
            retries[0] += 1
            raise Exception("Faulty function")

        with self.assertRaises(Exception):
            f()

        self.assertEqual(max_tries, retries[0])

    def test_fn_is_executed_once_for_0_max_retries(self):
        fn_calls = [0]

        @retry(Exception, max_retries=0)
        def f():
            fn_calls[0] += 1
            raise Exception("Fauty function")

        with self.assertRaises(Exception):
            f()

        self.assertEqual(1, fn_calls[0])

    def test_retry_raises_error_on_negative_retries(self):
        """Test retry for negative max_retries"""

        @retry(Exception, max_retries=-1)
        def f():
            raise Exception("Faulty function")

        self.assertRaises(ValueError, f)
