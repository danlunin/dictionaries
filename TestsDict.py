#!/usr/bin/env python3
import unittest
import Dict_list
import Dictionary2
import BinaryTreeDict


class MyTestCase(unittest.TestCase):

    def test_check_set1(self):
        dic1 = Dict_list.Dictionary()
        dic1[0] = 1
        self.assertEqual(dic1[0], 1)

    def test_check_set2(self):
        dic2 = [(1, 'Ok'), (2, 'q'), (3, 0)]
        dic1 = Dict_list.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[3] = 0
        self.assertEqual(str(dic1), str(dic2))

    def test_check_set3(self):
        dic2 = [(2, 'q'), (1, 0)]
        dic1 = Dict_list.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        self.assertEqual(str(dic1), str(dic2))

    def test_size1(self):
        dic1 = Dict_list.Dictionary()
        dic1[1] = 'Ok'
        self.assertEqual(dic1.size(), 1)

    def test_size2(self):
        dic1 = Dict_list.Dictionary()
        self.assertEqual(dic1.size(), 0)

    def test_get1(self):
        dic1 = Dict_list.Dictionary()
        dic1[0] = 0
        right = False
        try:
            dic1[1]
        except KeyError:
            right = True
        self.assertTrue(right)

    def test_del(self):
        dic2 = [(2, 'q'), (1, 0)]
        dic1 = Dict_list.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        dic1[3] = 2
        dic1.__delitem__(3)
        self.assertEqual(str(dic1), str(dic2))

    def test_del22(self):
        dic2 = [(2, 'q'), (1, 0)]
        dic1 = Dict_list.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        dic1[3] = 2
        right = False
        try:
            dic1.__delitem__(4)
        except KeyError:
            right = True
        self.assertTrue(right)

    def test_check_set12(self):
        dic1 = Dictionary2.Dictionary()
        dic1[0] = 1
        self.assertEqual(dic1[0], 1)

    def test_check_set22(self):
        dic2 = [(1, 'Ok'), (2, 'q'), (3, 0)]
        dic1 = Dictionary2.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[3] = 0
        self.assertEqual(str(dic1), str(dic2))

    def test_check_set32(self):
        dic2 = [(1, 0), (2, 'q')]
        dic1 = Dictionary2.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        self.assertEqual(str(dic1), str(dic2))

    def test_size12(self):
        dic1 = Dictionary2.Dictionary()
        dic1[1] = 'Ok'
        self.assertEqual(dic1.size(), 1)

    def test_size22(self):
        dic1 = Dictionary2.Dictionary()
        self.assertEqual(dic1.size(), 0)

    def test_del2(self):
        dic2 = [(1, 0), (2, 'q')]
        dic1 = Dictionary2.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        dic1[3] = 2
        dic1.__delitem__(3)
        self.assertEqual(str(dic1), str(dic2))

    def test_get12(self):
        dic1 = Dictionary2.Dictionary()
        dic1[0] = 0
        right = False
        try:
            dic1[1]
        except KeyError:
            right = True
        self.assertTrue(right)

    def test_del23(self):
        dic2 = [(2, 'q'), (1, 0)]
        dic1 = BinaryTreeDict.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        dic1[3] = 2
        right = False
        try:
            dic1.__delitem__(4)
        except KeyError:
            right = True
        self.assertTrue(right)

    def test_check_set13(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[0] = 1
        self.assertEqual(dic1[0], 1)

    def test_check_set23(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[3] = 0
        self.assertEqual(dic1[2], 'q')

    def test_check_set33(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        self.assertEqual(dic1[1], 0)

    def test_get13(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[0] = 0
        right = False
        try:
            dic1[1]
        except KeyError:
            right = True
        self.assertTrue(right)

    def test_size13(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[1] = 'Ok'
        self.assertEqual(dic1.size, 1)

    def test_size23(self):
        dic1 = BinaryTreeDict.Dictionary()
        self.assertEqual(dic1.size, 0)

    def test_del3(self):
        dic1 = BinaryTreeDict.Dictionary()
        dic1[1] = 'Ok'
        dic1[2] = 'q'
        dic1[1] = 0
        dic1[3] = 2
        dic1.__delitem__(3)
        right = False
        try:
            dic1[3]
        except KeyError:
            right = True
        self.assertTrue(right)

if __name__ == '__main__':
    unittest.main()
