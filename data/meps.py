import numpy as np
import sys

sys.path.append("../")


"""
 feature_names = ['REGION' 'AGE' 'SEX' 'RACE' 'MARRY' 'FTSTU' 'ACTDTY' 'HONRDC' 'RTHLTH'
 'MNHLTH' 'CHDDX' 'ANGIDX' 'MIDX' 'OHRTDX' 'STRKDX' 'EMPHDX' 'CHBRON'
 'CHOLDX' 'CANCERDX' 'DIABDX' 'JTPAIN' 'ARTHDX' 'ARTHTYPE' 'ASTHDX'
 'ADHDADDX' 'PREGNT' 'WLKLIM' 'ACTLIM' 'SOCLIM' 'COGLIM' 'DFHEAR42'
 'DFSEE42' 'ADSMOK42' 'PCS42' 'MCS42' 'K6SUM42' 'PHQ242' 'EMPST' 'POVCAT'
 'INSCOV']
"""
### REGION,AGE,SEX,RACE,MARRY,FTSTU,ACTDTY,HONRDC,RTHLTH,MNHLTH,CHDDX,ANGIDX,MIDX,OHRTDX,STRKDX,EMPHDX,CHBRON,CHOLDX,CANCERDX,DIABDX,JTPAIN,ARTHDX,ARTHTYPE,ASTHDX,ADHDADDX,PREGNT,WLKLIM,ACTLIM,SOCLIM,COGLIM,DFHEAR42,DFSEE42,ADSMOK42,PCS42,MCS42,K6SUM42,PHQ242,EMPST,POVCAT,INSCOV


def meps_data(path="datasets/meps"):
    """
    Prepare the data of dataset Census Income
    :return: X, Y, input shape and number of classes
    """
    X = []
    Y = []
    i = 0

    with open(path, "r") as ins:
        for line in ins:
            line = line.strip()
            line1 = line.split(",")
            if i == 0:
                i += 1
                continue
            # L = map(int, line1[:-1])
            L = [int(i) for i in line1[:-1]]
            X.append(L)
            if int(line1[-1]) == 0:
                Y.append([1, 0])
            else:
                Y.append([0, 1])
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    input_shape = (None, 40)
    nb_classes = 2

    return X, Y, input_shape, nb_classes

