from builtins import tuple

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
# from pyramid.arima import auto_arima
import pmdarima as pm

data = [1133 ,1339 ,1462 ,1702 ,1656 ,1439 ,1208 ,1613 ,1935 ,1964 ,2003 ,2023 ,1559 ,1274 ,1805 ,2051 ,2024 ,2049 ,1998 ,1441 ,1257 ,1559 ,1643 ,1464 ,1521 ,1576 ,1381 ,1372 ,1610 ,1926 ,2018 ,1930 ,1868 ,1551 ,1471 ,1954 ,2079 ,2061 ,2001 ,2031 ,1574 ,1165 ,1366 ,1384 ,1342 ,1543 ,1509 ,1598 ,1349 ,1625 ,1932 ,2079 ,1857 ,1443 ,1332 ,1149 ,1471 ,1595 ,1498 ,1433 ,1401 ,1178 ,972 ,1283 ,1468 ,1456 ,1466 ,1378 ,1208 ,1038 ,1344 ,1379 ,1418 ,1466 ,1414 ,1129 ,948 ,1285 ,1373 ,1379 ,599 ,614 ,850 ,672 ,747 ,732 ,834 ,996 ,900 ,792 ,688 ,781 ,696 ,834 ,1026 ,974 ,1001 ,997 ,1110 ,1212 ,1301 ,1322 ,1253 ,935 ,857 ,1082 ,1112 ,1291 ,1391 ,1384 ,1089 ,963 ,1174 ,1420 ,1349 ,1338 ,1335 ,1075 ,952 ,1376 ,1586 ,1571 ,1543 ,1525 ,1223 ,1066 ,1555 ,1704 ,1745 ,1749 ,1687 ,1288 ,1152 ,1492 ,1728 ,1742 ,1732 ,1510 ,1288 ,1280 ,1659 ,1852 ,1823 ,1723 ,1416 ,1187 ,1014 ,1324 ,1618 ,1736 ,1552 ,1598 ,1158 ,1083 ,1383 ,1595 ,1540 ,1551 ,1447 ,1128 ,1057 ,1371 ,1746 ,1653 ,1726 ,1759 ,1297 ,1165 ,1480 ,1693 ,1744 ,1661 ,1575 ,1199 ,1062 ,1395 ,1555 ,1441 ,1399 ,1381 ,1287 ,1151 ,1394 ,1660 ,1761 ,1874 ,1863 ,1544 ,1340 ,1707 ,1983 ,1785 ,1725 ,1765 ,1520 ,1274 ,1763 ,1793 ,1853 ,1861 ,1733 ,1575 ,1304 ,1793 ,1886 ,1832 ,1993 ,1805 ,1521 ,1332 ,1813 ,1833 ,1633 ,1682 ,1699 ,1392 ,1249 ,1601 ,1827 ,1755 ,1560 ,1181 ,1039 ,920 ,1106 ,1269 ,1159 ,1192 ,1203 ,1876 ,1065 ,1294 ,1249 ,1145 ,1098 ,1171 ,996 ,807 ,1081 ,1258 ,1201 ,1273 ,1165 ,944 ,797 ,948 ,1160 ,1387 ,1364 ,1061 ,916 ,901 ,1047 ,1107 ,1234 ,1290 ,1027 ,877 ,629 ,789 ,977 ,953 ,983 ,927 ,870 ,724 ,824 ,1015 ,1062 ,962 ,1046 ,766 ,764 ,876 ,975 ,917 ,914 ,1239 ,1000 ,753 ,892 ,1000 ,1509 ,1183 ,955 ,862 ,659 ,780 ,916 ,1010 ,988 ,1032 ,856 ,729 ,917 ,1038 ,1146 ,1228 ,1210 ,939 ,913 ,1045 ,1131 ,1076 ,1068 ,1073 ,919 ,809 ,963 ,1095 ,1150 ,950 ,909 ,889 ,840 ,1156 ,1221 ,1247 ,1146 ,1142 ,969 ,912 ,1103 ,1146 ,1118 ,1193 ,1200 ,1065 ,908 ,1491 ,1968 ,2100 ,2402 ,2489 ,2110 ,2046 ,2288 ,2835 ,2620 ,2467 ,2262 ,2046 ,1711 ,1960 ,2241 ,2383 ,2463 ,2289 ,1847 ,1654 ,2040 ,2473 ,2492 ,2501 ,2566 ,2284 ,2063 ,2655 ,2878 ,2957 ,2710 ,2526 ,2105 ,1782 ,2242 ,2520 ,2246 ,2378 ,2545 ,2154 ,2022 ,2711 ,3142 ,2952 ,2882 ,2766 ,2104 ,1745 ,2043 ,2495 ,2555 ,2572 ,2723 ,2276 ,1936 ,2472 ,2800 ,2843 ,2670 ,2769 ,2267 ,2213 ,2695 ,2801 ,2608 ,2418 ,1940 ,1610 ,1459 ,1972 ,2292 ,2573 ,2630 ,2448 ,2022 ,1869 ,2313 ,2551 ,2653 ,2595 ,2373 ,2088 ,1954 ,2374 ,2780 ,2674 ,2675 ,2445 ,2095 ,1806 ,2279 ,2639 ,2616 ,2152 ,2055 ,1775 ,1682 ,2151 ,2386 ,2519 ,2381 ,2394 ,1832 ,1729 ,1953 ,2224 ,2164 ,2121 ,2103 ,1693 ,1557 ,1859 ,1884 ,1949 ,1861 ,1727 ,1489 ,1197 ,1385 ,1412 ,1165 ,957 ,475 ,1301 ,1148 ,1272 ,1333 ,983 ,1263 ,1513 ,1510 ,1371 ,1567 ,1814 ,1870 ,2014 ,1923 ,1506 ,1262 ,1342 ,1531 ,1360 ,1526 ,1542 ,1269 ,1175 ,1377 ,1615 ,1578 ,1564 ,1514 ,1261 ,1087 ,1389 ,1736 ,1819 ,1890 ,1652 ,1521 ,1274 ,1592 ,1694 ,1705 ,1869 ,1910 ,1544 ,1341 ,1679 ,1823 ,1845 ,1921 ,1808 ,1454 ,1393 ,1733 ,1944 ,1911 ,1804 ,1525 ,573 ,576 ,740 ,760 ,784 ,746 ,713 ,598 ,619 ,711 ,766 ,716 ,803 ,718 ,562 ,499 ,573 ,746 ,679 ,658 ,694 ,545 ,557 ,607 ,672 ,776 ,728 ,804 ,578 ,621 ,689 ,745 ,801 ,1362 ,2025 ,1716 ,1447 ,1585 ,2054 ,2103 ,2059 ,2093 ,1593 ,1519 ,1615 ,1969 ,1982 ,1979 ,1893 ,1677 ,1338 ,1541 ,1784 ,1932 ,1777 ,1609 ,1359 ,1228 ,1499 ,1734 ,1763 ,1775 ,1611 ,1434 ,1315 ,1541 ,1823 ,1725 ,1483 ,1525 ,1444 ,1235 ,1525 ,1836 ,1811 ,1702 ,1764 ,1546 ,1344 ,1619 ,1846 ,1791 ,1772 ,1620 ,1392 ,3327 ,2829 ,3787 ,5798 ,7024 ,4586 ,3328 ,2607 ,3005 ,4014 ,4296 ,5691 ,4643 ,3246 ,2573 ,2745 ,3520 ,2502 ,11 ,2316 ,2543 ,2341 ,2420 ,2847 ,2874 ,2678 ,2647 ,2245 ,1966 ,2329 ,2642 ,2695 ,2663 ,2586 ,2383 ,2131 ,2264 ,2704 ,2670 ,2621 ,2522 ,2237 ,1849 ,1932 ,2551 ,2494 ,2630 ,2471 ,2039 ,1850 ,2166 ,2618 ,2622 ,2693 ,2878 ,2174 ,1869 ,2045 ,2482 ,2464 ,2397 ,2460 ,2058 ,1829 ,2153 ,2536 ,2567 ,2487 ,2456 ,2018 ,1831 ,2027 ,2145 ,2343 ,2358 ,2599 ,2223 ,1989 ,2389 ,2843 ,3200 ,3009 ,2999 ,2524 ,2160 ,2617 ,3180 ,3279 ,3232 ,2413 ,2415 ,2348 ,2901 ,3478 ,3602 ,3536 ,3652 ,3211 ,2948 ,3448 ,4088 ,4042 ,3915 ,3274 ,2849 ,2761 ,3575 ,4101 ,4080 ,4015 ,3760 ,3083 ,2905 ,3655 ,4362 ,4570 ,4536 ,4169 ,3577 ,3257 ,4031 ,4681 ,4578 ,4146 ,4172 ,3351 ,3131 ,3676 ,4351 ,4297 ,4236 ,3693 ,3291 ,2902 ,3476 ,3887 ,3574 ,2797 ,2692 ,2557 ,2539 ,2820 ,3551 ,3674 ,3849 ,3896 ,3389 ,2968 ,3698 ,4376 ,4351 ,4193 ,4053 ,3191 ,2924 ,3178 ,3424 ,2990 ,2812 ,2552 ,2475 ,2416 ,2939 ,3803 ,3940 ,3803 ,3570 ,2977 ,2707 ,3526 ,3416 ,3821 ,3634 ,3679 ,3095 ,2928 ,3368 ,3764 ,3815 ,3682 ,3399 ,3010 ,2712 ,3191 ,3542 ,3565 ,3779 ,3371 ,2907 ,2813 ,3342 ,3656 ,3499 ,3470 ,3123 ,2865 ,2619 ,3118 ,3486 ,3323 ,3312 ,3263 ,2829 ,2404 ,2769 ,3251 ,3206 ,3452 ,3248 ,2791 ,2518 ,2838 ,2958 ,3162 ,3030 ,2957 ,2402 ,2163 ,2452 ,2657 ,2460 ,2037 ,2115 ,2266 ,2057 ,2207 ,2439 ,2341 ,1780 ,2048 ,2586 ,2362 ,2547 ,3000 ,3118 ,3145 ,3080 ,2721 ,2401 ,2801 ,3301 ,2913 ,2866 ,2963 ,2742 ,2510 ,2981 ,3625 ,3626 ,3453 ,3214 ,2572 ,2194 ,2301 ,3044 ,3579 ,3441 ,3505 ,3001 ,2679 ,3157 ,3874 ,3884 ,3875 ,3649 ,3001 ,2547 ,3155 ,3812 ,3728 ,4009 ,3713 ,3117 ,2412 ,3146 ,3538 ,3620 ,3762 ,3799 ,3222 ,2862 ,3609 ,4130 ,4074 ,4242 ,4214 ,3123 ,2691 ,3470 ,4043 ,3701 ,3578 ,2909 ,2699 ,2697 ,3244 ,3880 ,4281 ,4078 ,4185 ,3525 ,3142 ,3853 ,4269 ,4288 ,4029 ,3678 ,3048 ,2849 ,3421 ,4102 ,3950 ,3624 ,3555 ,3375 ,2823 ,3331 ,4228 ,3928 ,3683 ,3205 ,2899 ,2757 ,3315 ,3923 ,3758 ,3831 ,3695 ,3074 ,2664 ,3149 ,3469 ,3583 ,3731 ,3703 ,3128 ,2775 ,3264 ,3679 ,3534 ,3535 ,3556 ,2943 ,2471 ,2837 ,3666 ,3458 ,3198 ,2755 ,2499 ,2344 ,2861 ,3255 ,3254 ,3101 ,3046 ,2570 ,2250 ,2883 ,3094 ,3036 ,2822 ,2925 ,2491 ,2383 ,3641 ,6153 ,4075 ,3891 ,3845 ,2748 ,2362 ,3358 ,11743 ,6975 ,6806 ,10251 ,5817 ,3813 ,3611 ,3964 ,3748 ,4419 ,5033 ,3704 ,2846 ,2863 ,3223 ,3277 ,3028 ,2818 ,2374 ,2167 ,2391 ,3045 ,2891 ,2919 ,2903 ,2594 ,2322 ,2355 ,2831 ,2836 ,2941 ,2751 ,2545 ,2153 ,2266 ,2730 ,2619 ,2696 ,2496 ,2338 ,2156 ,2264 ,2605 ,2608 ,2526 ,2417 ,2256 ,1938 ,2053 ,2492 ,2467 ,2381 ,2185 ,1910 ,1793 ,2119 ,2420 ,2689 ,2557 ,2430 ,2097 ,1929 ,2226 ,2653 ,2537 ,2501 ,2378 ,2145 ,1974 ,2347 ,2748 ,2800 ,2734 ,2866 ,2618 ,2282 ,2625 ,2946 ,2953 ,2997 ,2879 ,2092 ,2158 ,2652 ,3127 ,3277 ,3271 ,3172 ,2822 ,2566 ,2820 ,3347 ,3211 ,2977 ,2918 ,2288 ,2120 ,2632 ,3233 ,3379 ,3385 ,3282 ,2587 ,2485 ,2884 ,3317 ,3370 ,3465 ,3435 ,2974 ,2678 ,3068 ,3561 ,3621 ,2954 ,2881 ,2869 ,2558 ,3166 ,3480 ,3418 ,3122 ,2937 ,2705 ,2594 ,2781 ,3517 ,3750 ,3618 ,3077 ,3017 ,2805 ,3299 ,3841 ,3834 ,3924 ,3562 ,3046 ,2691 ,3174 ,3717 ,3680 ,3504 ,3251 ,2793 ,2437 ,2812 ,3141 ,2915 ,2474 ,2425 ,2601 ,2402 ,2802 ,3256 ,3510 ,3542 ,3483 ,3091 ,2969 ,3777 ,4030 ,3829 ,3697 ,3480 ,3014 ,2671]
df = pd.DataFrame(data,columns =['val'])
df.index = pd.DatetimeIndex(freq="w",start = 0, periods=len(data))
df.head()

# autocorrelation_plot(df)
# pyplot.show()

history = data.copy()
prediction = []
predRange = 30
# for i in range(predRange):
#     model = ARIMA(prediction, order=(2,1,2))
#     model_fit = model.fit(disp=0)
#     output = model_fit.forecast()
#     yhat = output[0]
#     prediction.append((yhat))


model = ARIMA(data, order=(2,0,1))
modelSeasonal = pm.auto_arima(data, start_p=1, start_q=1,
                         test='adf',
                         max_p=3, max_q=3, m=12,
                         start_P=0, seasonal=True,
                         d=None, D=1, trace=True,
                         error_action='ignore',
                         suppress_warnings=True,
                         stepwise=True)
model_fit = model.fit(disp=0)

prediction = model_fit.predict()
fc, confint = modelSeasonal.predict(n_periods=30, return_conf_int=True)
# print(len(prediction))
res = history.copy()
for val in prediction:
    res.append((val))

plt.plot(history[1100:],'r.')
plt.plot(res[1100:],'b')
plt.plot(fc,'g')
# print(prediction[1133:])
# results.plot_predict(1000,1163)
plt.show()
for i in range(30):
    print(int(res[1134+i]))

print(fc)