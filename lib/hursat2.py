class Hursat(object):
    

    def __readNcdf__(self, fname, **kwargs):
        pass

    def _convCoords(latStr, lonStr):
        return int(latStr[:-1]), int(lonStr[:-1])

    def __init__(self, dtype='txt', **kwargs):
        from io import readAscii
        if dtype == 'txt':
            self = readAscii(**kwargs)


from numpy import recarray
class Storm(object):
    
    def __init__(self, name, **kwargs):
       # self.name = name
        dtype = [('epoch', 'f8'),
                ('category', 'a2'),
                ('lat', 'f4'),
                ('lon', 'f4'),
                ('U_max', 'i4'),
                ('p', 'f4')]
        self = recarray((0,), dtype=dtype)
        #_ignoring other twelve vars for now (extend in quadrants?)
