class Dictionary:
    def __init__(self):
        self.dict_list = []

    def __str__(self):
        return str(self.dict_list)

    def __repr__(self):
        return str(self.dict_list)

    def __getitem__(self, item):
        index = self.BinSearch(item)
        try:
            if self.dict_list[index][0] == item:
                return self.dict_list[index][1]
        except IndexError:
            raise KeyError
        raise KeyError

    def __setitem__(self, key, value):
        if self.size() != 0:
            index = self.BinSearch(key)
            if index < len(self.dict_list) and self.dict_list[index][0] == key:
                self.dict_list[index] = key, value
            else:
                self.dict_list.insert(index, (key, value))
        else:
            self.dict_list.append((key, value))

    def __delitem__(self, key):
        index = self.BinSearch(key)
        if len(self.dict_list) == 0 or self.dict_list[index][0] != key:
            raise KeyError
            return
        else:
            self.dict_list.remove(self.dict_list[index])

    def size(self):
        return len(self.dict_list)

    def BinSearch(self, x):
        i = 0
        j = len(self.dict_list)-1
        while i < j:
            m = int((i+j)/2)
            if x > self.dict_list[m][0]:
                i = m+1
            else:
                j = m
        if i == j and x > self.dict_list[i][0]:
            i += 1
        return i
