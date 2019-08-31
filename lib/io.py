def readAscii(fname='', **kwargs):
        import numpy as np     
        from tools import dtg2epoch, convCoord

        from hursat2 import Storm

        print fname
        tmp = []

        with open(fname, 'r') as f:
            for line in f.readlines():
                print 'TESTING', line
                cols = [n.strip() for n in line.split(',')]
                print "LENGTH", len(cols)

                #_initialize storm
                if len(cols) == 4: 
                    tmp.append(Storm)
                    continue 

                elif len(cols) < 4:
                    print 'EDGECASE:', cols
            
                epoch = dtg2epoch(cols[0] + cols[1])
                lat = convCoord(cols[4])
                lon = convCoord(cols[5])

                data = [epoch, cols[3], lat, lon, cols[6], cols[7]]
                print data
                print 'TYPING', type(tmp[-1]), tmp, tmp[-1].size
                tmp[-1].resize(tmp[-1].size + 1)
                tmp[-1][-1] = data

                if i > 100:
                    print "Exiting for now"
                    break
