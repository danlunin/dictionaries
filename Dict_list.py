#!/usr/bin/env python3
class Dictionary:
    def __init__(self, dict_list=None):
        if dict_list:
            self.dict_list = dict_list
        else:
            self.dict_list = []

    def __str__(self):
        return str(self.dict_list)

    def __repr__(self):
        return str(self.dict_list)

    def __getitem__(self, item):
        for e in self.dict_list:
            if e[0] == item:
                return e[1]
        raise KeyError

    def __setitem__(self, key, value):
        for e in self.dict_list:
            if e[0] == key:
                self.dict_list.remove(e)
                self.dict_list.append((key, value))
                return
        self.dict_list.append((key, value))

    def __delitem__(self, key):
        for e in self.dict_list:
            if e[0] == key:
                self.dict_list.remove(e)
                return
        raise KeyError

    def size(self):
        return len(self.dict_list)


def main():
    a = Dictionary()
    a[1] = 'Ok'
    a[2] = 'q'
    a[1] = 0
    a[7] = 'p'
    a[10] = 1
    a[0] = 5
    a[3] = 2
    print(a.size())
    print(a)
    print(a[7])
    b = Dictionary()
    print(b)

if __name__ == '__main__':
    main()
