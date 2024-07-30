class DefaultDict(dict):
    def __init__(self, default_factory):
        self.default_factory = default_factory

    def __missing__(self, key):
        self[key] = self.default_factory()
        return self[key]


# 딕셔너리 안에 딕셔너리 넣기 
d1 = DefaultDict(dict)
d1['key']['inner_key'] = 1
print(d1)


# 딕셔너리 안에 리스트 넣기
d2 = DefaultDict(list)
d2["key"].append(1)
print(d2) 

# 딕셔너리 안에 디폴트 딕셔너리 넣기
d3 = DefaultDict(lambda: DefaultDict(list))
d3["key"]["inner_key"].append(1)
print(d3)