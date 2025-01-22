import numpy as np

def f0(x: np.ndarray) -> np.ndarray:
    return np.maximum((26.2 ** 0.5) * (26.2 - (x[0] - (x[1] / -5.6))), -0.7) / (5.2 ** -8.8) * -9.778889672523474e-08 + 26.216037651353062

def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(np.minimum(x[0], np.sign(x[0]) * x[0]))

def f2(x: np.ndarray) -> np.ndarray: 
    return 3784321.3480451438 * np.sign(x[0] - ((np.tan(38.2) - (np.sin(-224.64) ** np.cos(x[2]))) * x[1])) + 91280.86296010547

def f3(x: np.ndarray) -> np.ndarray: 
    return (-1.0040478983216745 * (x[1] ** 2) * x[1]) + 20.40988711941733

def f4(x: np.ndarray) -> np.ndarray: 
    return -0.16470866767462639 *( -42.5*np.cos(x[1]) + np.sign(x[0])) + 3.280924838467743

def f5(x: np.ndarray) -> np.ndarray: 
    return (-5.4509089425111764e-14 * (x[1] * (((x[0] * x[0]) * (np.exp(x[1]) * x[0])) * x[0]))) + 2.3930585966024667e-10

def f6(x: np.ndarray) -> np.ndarray: 
    return (-0.051935559371433154) * ((-11.856588799999997 / ((x[1] + x[1]) - (-26646.855588281243 + x[0])) -
                                       ((x[1] + x[1]) - (-12251.427856681032 + x[0])) / (x[0] - 75363.71813926)) *
                                      (-1224071.64071506 - (((x[1] + x[1]) - (-1317.3578340517238 + x[0])) / (x[0] - 474791.42427736)))) - 10306.35779974637

def f7(x: np.ndarray) -> np.ndarray: 
    return (-13.30888021787793 * np.log(np.abs(x[1] - x[0])) * ((np.maximum(x[1], x[1])) * (x[1] / (x[1] / x[0])))) + (-2.532233896849151)

def f8(x: np.ndarray) -> np.ndarray: 
    return (5.00273373222205 *x[5]*np.square(np.abs(x[5])) * (x[5] ** 2)) + (x[4] + x[3])+ (-520.3818751347435)


