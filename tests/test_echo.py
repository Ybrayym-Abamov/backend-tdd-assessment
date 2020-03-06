#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def setUp(self):
        """ This function is only called only once for all tests """
        self.parser = echo.create_parser()
        self.pystring = 'python2'
        if sys.version_info[0] == 3:
            self.pystring = 'python3'

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            [self.pystring, "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode('utf8')
        with open("./USAGE", "r") as f:
            usage = f.read()
        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        # self.parser = echo.create_parser()
        # parsed = self.parser.parse_args(['-u', '--upper', 'text'])
        # self.assertEqual(parsed.upper, 'text')
        args = ["-u", 'hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--upper", 'hello world']
        actual = echo.main(args)
        expected = "HELLO WORLD"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ["-l", 'hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ["--lower", 'hello world']
        actual = echo.main(args)
        expected = "hello world"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ["-t", 'hello world']
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ["--title", 'hello world']
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_all_args(self):
        args = ["-tul", 'hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)

    def test_no_args(self):
        args = ['hello world']
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.title)
        actual = echo.main(args)
        expected = args[0]
        # assert means: 'Make sure that ...'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
