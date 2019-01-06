# measure version 1.8.3
from measure import npfarray,np,exp,sqrt,ln,mv,dsto_mv,dsys_mv,dtot,val,tbl,T0,p0,plt,pltext,linreg,sig,curve_fit

# Messwerte
wl_sa = npfarray([-36,0,200,404,706])*1e-6
wl_sa_dsys = npfarray([10,10,10,10,10])*1e-6
wl_se = npfarray([2930,2951,3155,3370,3677])*1e-6
wl_se_dsys = npfarray([10,10,10,10,10])*1e-6
wl_m = npfarray([11165,11136,11134,11163,11170])
wl_m_dsys = npfarray([1,1,1,1,1])
wl_lit = 532e-9
wl_lit_dsys = 1e-9

bi_T = mv([23.3,23.4]) + T0
bi_T_dtot = sqrt(2) * 0.1
bi_a = 50e-3
bi_a_dsys = 0.05e-3
bi_m1 = npfarray([0,5,10,15,20,25,30,35])
bi_m2 = npfarray([0,5,10,15,20,25,30,35])
bi_m3 = npfarray([0,5,10,15,20,25,30,35])
bi_p1 = npfarray([540,470,395,320,245,175,100,25])*101325/760
bi_p1_dsys = npfarray([5,5,5,5,5,5,5,5])*101325/760
bi_p2 = npfarray([700,625,555,480,410,340,265,190])*101325/760
bi_p2_dsys = npfarray([5,5,5,5,5,5,5,5])*101325/760
bi_p3 = npfarray([630,550,485,410,335,265,190,115])*101325/760
bi_p3_dsys = npfarray([5,5,5,5,5,5,5,5])*101325/760
bi_n0_lit = 1.00028

kl_t = npfarray([-2.9599994e-02,-2.9399995e-02,-2.9199995e-02,-2.8999995e-02,-2.8799992e-02,-2.8599992e-02,-2.8399993e-02,-2.8199993e-02,-2.7999993e-02,-2.7799994e-02,-2.7599994e-02,-2.7399994e-02,-2.7199995e-02,-2.6999995e-02,-2.6799995e-02,-2.6599992e-02,-2.6399992e-02,-2.6199993e-02,-2.5999993e-02,-2.5799993e-02,-2.5599994e-02,-2.5399994e-02,-2.5199994e-02,-2.4999995e-02,-2.4799995e-02,-2.4599995e-02,-2.4399996e-02,-2.4199992e-02,-2.3999993e-02,-2.3799993e-02,-2.3599993e-02,-2.3399994e-02,-2.3199994e-02,-2.2999994e-02,-2.2799995e-02,-2.2599995e-02,-2.2399995e-02,-2.2199996e-02,-2.1999996e-02,-2.1799993e-02,-2.1599993e-02,-2.1399993e-02,-2.1199994e-02,-2.0999994e-02,-2.0799994e-02,-2.0599995e-02,-2.0399995e-02,-2.0199995e-02,-1.9999996e-02,-1.9799996e-02,-1.9599993e-02,-1.9399993e-02,-1.9199993e-02,-1.8999994e-02,-1.8799994e-02,-1.8599994e-02,-1.8399995e-02,-1.8199995e-02,-1.7999995e-02,-1.7799996e-02,-1.7599996e-02,-1.7399997e-02,-1.7199993e-02,-1.6999993e-02,-1.6799994e-02,-1.6599994e-02,-1.6399994e-02,-1.6199995e-02,-1.5999995e-02,-1.5799996e-02,-1.5599997e-02,-1.5399997e-02,-1.5199997e-02,-1.4999998e-02,-1.4799994e-02,-1.4599995e-02,-1.4399995e-02,-1.4199995e-02,-1.3999996e-02,-1.3799996e-02,-1.3599996e-02,-1.3399997e-02,-1.3199997e-02,-1.2999997e-02,-1.2799998e-02,-1.2599994e-02,-1.2399995e-02,-1.2199995e-02,-1.1999995e-02,-1.1799996e-02,-1.1599996e-02,-1.1399996e-02,-1.1199997e-02,-1.0999997e-02,-1.0799997e-02,-1.0599998e-02,-1.0399998e-02,-1.0199995e-02,-9.9999951e-03,-9.7999955e-03,-9.5999958e-03,-9.3999961e-03,-9.1999965e-03,-8.9999968e-03,-8.7999972e-03,-8.5999975e-03,-8.3999978e-03,-8.1999982e-03,-7.9999985e-03,-7.7999947e-03,-7.5999950e-03,-7.3999953e-03,-7.1999957e-03,-6.9999960e-03,-6.7999964e-03,-6.5999967e-03,-6.3999970e-03,-6.1999974e-03,-5.9999977e-03,-5.7999981e-03,-5.5999947e-03,-5.3999950e-03,-5.1999954e-03,-4.9999957e-03,-4.7999960e-03,-4.5999964e-03,-4.3999967e-03,-4.1999971e-03,-3.9999974e-03,-3.7999977e-03,-3.5999981e-03,-3.3999984e-03,-3.1999950e-03,-2.9999954e-03,-2.7999957e-03,-2.5999960e-03,-2.3999964e-03,-2.1999967e-03,-1.9999971e-03,-1.7999974e-03,-1.5999977e-03,-1.3999981e-03,-1.1999984e-03,-9.9999504e-04,-7.9999730e-04,-5.9999764e-04,-3.9999612e-04,-1.9999644e-04,3.2126903e-09,2.0000288e-04,4.0000252e-04,6.0000218e-04,8.0000371e-04,1.0000034e-03,1.2000031e-03,1.4000027e-03,1.6000024e-03,1.8000021e-03,2.0000036e-03,2.2000032e-03,2.4000029e-03,2.6000026e-03,2.8000022e-03,3.0000019e-03,3.2000034e-03,3.4000031e-03,3.6000027e-03,3.8000024e-03,4.0000021e-03,4.2000017e-03,4.4000032e-03,4.6000029e-03,4.8000026e-03,5.0000022e-03,5.2000019e-03,5.4000034e-03,5.6000031e-03,5.8000027e-03,6.0000024e-03,6.2000020e-03,6.4000017e-03,6.6000032e-03,6.8000029e-03,7.0000025e-03,7.2000022e-03,7.4000019e-03,7.6000015e-03,7.8000030e-03,8.0000022e-03,8.2000019e-03,8.4000016e-03,8.6000012e-03,8.8000009e-03,9.0000024e-03,9.2000021e-03,9.4000017e-03,9.6000014e-03,9.8000010e-03,1.0000001e-02,1.0200002e-02,1.0400002e-02,1.0600002e-02,1.0800001e-02,1.1000001e-02,1.1200001e-02,1.1400002e-02,1.1600002e-02,1.1800001e-02,1.2000001e-02,1.2200001e-02,1.2400002e-02,1.2600002e-02,1.2800002e-02,1.3000001e-02,1.3200001e-02,1.3400001e-02,1.3600002e-02,1.3800002e-02,1.4000001e-02,1.4200001e-02,1.4400001e-02,1.4600000e-02,1.4800001e-02,1.5000002e-02,1.5200001e-02,1.5400001e-02,1.5600001e-02,1.5800001e-02,1.6000001e-02,1.6200002e-02,1.6400002e-02,1.6600002e-02,1.6800001e-02,1.7000001e-02,1.7200001e-02,1.7400002e-02,1.7600002e-02,1.7800001e-02,1.8000001e-02,1.8200001e-02,1.8400000e-02,1.8600002e-02,1.8800002e-02,1.9000001e-02,1.9200001e-02,1.9400001e-02,1.9600000e-02,1.9800002e-02,2.0000001e-02,2.0200001e-02,2.0400001e-02,2.0600000e-02,2.0800000e-02,2.1000002e-02,2.1200001e-02,2.1400001e-02,2.1600001e-02,2.1800000e-02,2.2000002e-02,2.2200001e-02,2.2400001e-02,2.2600001e-02,2.2800000e-02,2.3000000e-02,2.3200000e-02,2.3400001e-02,2.3600001e-02,2.3800001e-02,2.4000000e-02,2.4200000e-02,2.4400000e-02,2.4600001e-02,2.4800001e-02,2.5000000e-02,2.5200000e-02,2.5400000e-02,2.5599999e-02,2.5800001e-02,2.6000001e-02,2.6200000e-02,2.6400000e-02,2.6600000e-02,2.6800001e-02,2.7000001e-02,2.7200000e-02,2.7400000e-02,2.7600000e-02,2.7799999e-02,2.8000001e-02,2.8200001e-02,2.8400000e-02,2.8600000e-02,2.8800000e-02,2.9000001e-02,2.9200001e-02,2.9400000e-02,2.9600000e-02,2.9800000e-02,2.9999999e-02,3.0200001e-02,3.0400001e-02,3.0600000e-02,3.0800000e-02,3.0999999e-02,3.1199999e-02,3.1399999e-02,3.1599998e-02,3.1799998e-02,3.2000002e-02,3.2200001e-02,3.2400001e-02,3.2600001e-02,3.2800000e-02,3.3000000e-02,3.3199999e-02,3.3399999e-02,3.3599999e-02,3.3799998e-02,3.3999998e-02,3.4199998e-02,3.4400001e-02,3.4600001e-02,3.4800000e-02,3.5000000e-02,3.5200000e-02,3.5399999e-02,3.5599999e-02,3.5799999e-02,3.5999998e-02,3.6199998e-02,3.6399998e-02,3.6599997e-02,3.6800001e-02,3.7000000e-02,3.7200000e-02,3.7400000e-02,3.7599999e-02,3.7799999e-02,3.7999999e-02,3.8199998e-02,3.8399998e-02,3.8599998e-02,3.8799997e-02,3.9000001e-02,3.9200000e-02,3.9400000e-02,3.9600000e-02,3.9799999e-02,3.9999999e-02,4.0199999e-02,4.0399998e-02,4.0599998e-02,4.0799998e-02,4.0999997e-02,4.1200001e-02,4.1400000e-02,4.1600000e-02,4.1800000e-02,4.1999999e-02,4.2199999e-02,4.2399999e-02,4.2599998e-02,4.2799998e-02,4.2999998e-02,4.3199997e-02,4.3399997e-02,4.3600000e-02,4.3800000e-02,4.4000000e-02,4.4199999e-02,4.4399999e-02,4.4599999e-02,4.4799998e-02,4.4999998e-02,4.5199998e-02,4.5399997e-02,4.5599997e-02,4.5799997e-02,4.6000000e-02,4.6200000e-02,4.6399999e-02,4.6599999e-02,4.6799999e-02,4.6999998e-02,4.7199998e-02,4.7399998e-02,4.7599997e-02,4.7799997e-02,4.7999997e-02,4.8199996e-02,4.8399996e-02,4.8599999e-02,4.8799999e-02,4.8999999e-02,4.9199998e-02,4.9399998e-02,4.9599998e-02,4.9799997e-02,4.9999997e-02,5.0199997e-02,5.0399996e-02,5.0599996e-02,5.0799999e-02,5.0999999e-02,5.1199999e-02,5.1399998e-02,5.1599998e-02,5.1799998e-02,5.1999997e-02,5.2199997e-02,5.2399997e-02,5.2599996e-02,5.2799996e-02,5.2999996e-02,5.3199999e-02,5.3399999e-02,5.3599998e-02,5.3799998e-02,5.3999998e-02,5.4199997e-02,5.4399997e-02,5.4599997e-02,5.4799996e-02,5.4999996e-02,5.5199996e-02,5.5399995e-02,5.5599999e-02,5.5799998e-02,5.5999998e-02,5.6199998e-02,5.6399997e-02,5.6599997e-02,5.6799997e-02,5.6999996e-02,5.7199996e-02,5.7399996e-02,5.7599995e-02,5.7799999e-02,5.7999998e-02,5.8199998e-02,5.8399998e-02,5.8599997e-02,5.8799997e-02,5.8999997e-02,5.9199996e-02,5.9399996e-02,5.9599996e-02,5.9799995e-02,5.9999995e-02,6.0199998e-02,6.0399998e-02,6.0599998e-02,6.0799997e-02,6.0999997e-02,6.1199997e-02,6.1399996e-02,6.1599996e-02,6.1799996e-02,6.1999999e-02,6.2199999e-02,6.2399998e-02,6.2599994e-02,6.2799998e-02,6.2999994e-02,6.3199997e-02,6.3399993e-02,6.3599996e-02,6.3799992e-02,6.3999996e-02,6.4199999e-02,6.4399995e-02,6.4599998e-02,6.4799994e-02,6.4999998e-02,6.5199994e-02,6.5399997e-02,6.5599993e-02,6.5799996e-02,6.5999992e-02,6.6199996e-02,6.6399992e-02,6.6599995e-02,6.6799998e-02,6.6999994e-02,6.7199998e-02,6.7399994e-02,6.7599997e-02,6.7799993e-02,6.7999996e-02,6.8199992e-02,6.8399996e-02,6.8599992e-02,6.8799995e-02,6.8999998e-02,6.9199994e-02,6.9399998e-02,6.9599994e-02,6.9799997e-02,6.9999993e-02,7.0199996e-02,7.0399992e-02,7.0599996e-02,7.0799991e-02,7.0999995e-02,7.1199998e-02,7.1399994e-02,7.1599998e-02,7.1799994e-02,7.1999997e-02,7.2199993e-02,7.2399996e-02,7.2599992e-02,7.2799996e-02,7.2999991e-02,7.3199995e-02,7.3399991e-02,7.3599994e-02,7.3799998e-02,7.3999994e-02,7.4199997e-02,7.4399993e-02,7.4599996e-02,7.4799992e-02,7.4999996e-02,7.5199991e-02,7.5399995e-02,7.5599991e-02,7.5799994e-02,7.5999998e-02,7.6199993e-02,7.6399997e-02,7.6599993e-02,7.6799996e-02,7.6999992e-02,7.7199996e-02,7.7399991e-02,7.7599995e-02,7.7799991e-02,7.7999994e-02,7.8199998e-02,7.8399993e-02,7.8599997e-02,7.8799993e-02,7.8999996e-02,7.9199992e-02,7.9399996e-02,7.9599991e-02,7.9799995e-02,7.9999991e-02,8.0199994e-02,8.0399990e-02,8.0599993e-02,8.0799997e-02,8.0999993e-02,8.1199996e-02,8.1399992e-02,8.1599995e-02,8.1799991e-02,8.1999995e-02,8.2199991e-02,8.2399994e-02,8.2599990e-02,8.2799993e-02,8.2999997e-02,8.3199993e-02,8.3399996e-02,8.3599992e-02,8.3799995e-02,8.3999991e-02,8.4199995e-02,8.4399991e-02,8.4599994e-02,8.4799990e-02,8.4999993e-02,8.5199997e-02,8.5399993e-02,8.5599996e-02,8.5799992e-02,8.5999995e-02,8.6199991e-02,8.6399995e-02,8.6599991e-02,8.6799994e-02,8.6999990e-02,8.7199993e-02,8.7399989e-02,8.7599993e-02,8.7799996e-02,8.7999992e-02,8.8199995e-02,8.8399991e-02,8.8599995e-02,8.8799991e-02,8.8999994e-02,8.9199990e-02,8.9399993e-02,8.9599989e-02,8.9799993e-02,8.9999996e-02,9.0199992e-02])
kl_U = npfarray([0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,0.03506667,-0.00493333,0.03506667,-0.00493333,0.03506667,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.00493333,-0.00493333,-0.00493333,-0.00493333,0.03506667,0.03506667,-0.00493333,0.03506667,0.03506667,0.03506667,-0.00493333,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.08493333,-0.08493333,-0.00493333,0.03506667,-0.00493333,0.03506667,0.07506667,0.03506667,0.03506667,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.08493333,-0.00493333,0.03506667,-0.00493333,0.03506667,0.03506667,0.07506667,0.03506667,-0.00493333,-0.00493333,-0.08493333,-0.00493333,-0.08493333,-0.00493333,-0.08493333,0.03506667,-0.00493333,0.03506667,0.07506667,0.07506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.08493333,-0.00493333,-0.08493333,0.03506667,0.07506667,0.07506667,0.03506667,0.07506667,-0.00493333,-0.00493333,-0.08493333,-0.08493333,-0.08493333,-0.08493333,0.03506667,0.03506667,0.07506667,0.07506667,0.07506667,0.07506667,-0.00493333,-0.00493333,-0.08493333,-0.08493333,-0.08493333,-0.08493333,-0.00493333,-0.00493333,0.07506667,0.07506667,0.11506667,0.07506667,0.03506667,0.03506667,-0.08493333,-0.08493333,-0.12493333,-0.12493333,-0.08493333,-0.08493333,0.03506667,0.03506667,0.11506667,0.11506667,0.07506667,0.11506667,-0.00493333,-0.00493333,-0.08493333,-0.12493333,-0.00493333,-0.08493333,-0.00493333,-0.08493333,0.03506667,0.03506667,0.11506667,0.11506667,0.15506667,0.11506667,0.03506667,0.03506667,-0.08493333,-0.12493333,-0.16493333,-0.16493333,-0.00493333,-0.08493333,0.03506667,0.07506667,0.15506667,0.15506667,0.11506667,0.11506667,-0.08493333,-0.08493333,-0.16493333,-0.16493333,-0.20493333,-0.12493333,-0.00493333,0.03506667,0.15506667,0.19506667,0.23506667,0.19506667,0.03506667,-0.00493333,-0.20493333,-0.20493333,-0.24493333,-0.24493333,-0.08493333,-0.08493333,0.15506667,0.19506667,0.27506667,0.27506667,0.07506667,0.07506667,-0.16493333,-0.16493333,-0.32493333,-0.32493333,-0.20493333,-0.16493333,0.11506667,0.19506667,0.31506667,0.35506667,0.23506667,0.27506667,-0.08493333,-0.08493333,-0.36493333,-0.36493333,-0.40493333,-0.32493333,-0.08493333,-0.00493333,0.27506667,0.35506667,0.47506667,0.43506667,0.15506667,0.11506667,-0.24493333,-0.36493333,-0.52493333,-0.52493333,-0.32493333,-0.28493333,0.19506667,0.23506667,0.55506667,0.59506667,0.43506667,0.39506667,-0.16493333,-0.24493333,-0.60493333,-0.68493333,-0.56493333,-0.56493333,0.03506667,0.11506667,0.63506667,0.67506667,0.75506667,0.63506667,0.07506667,-0.08493333,-0.68493333,-0.76493333,-0.88493333,-0.80493333,-0.24493333,-0.12493333,0.71506667,0.75506667,0.95506667,0.91506667,0.23506667,0.15506667,-0.72493333,-0.80493333,-1.12493333,-1.04493333,-0.32493333,-0.20493333,0.83506667,0.91506667,1.19506667,1.15506667,0.39506667,0.27506667,-0.88493333,-1.00493333,-1.36493333,-1.24493333,-0.40493333,-0.28493333,0.91506667,0.99506667,1.43506667,1.35506667,0.55506667,0.39506667,-0.84493333,-0.92493333,-1.52493333,-1.52493333,-0.92493333,-0.80493333,0.51506667,0.59506667,1.47506667,1.59506667,1.43506667,1.35506667,0.27506667,0.11506667,-1.20493333,-1.28493333,-1.68493333,-1.64493333,-0.92493333,-0.84493333,0.47506667,0.63506667,1.51506667,1.67506667,1.51506667,1.43506667,0.27506667,0.11506667,-1.08493333,-1.16493333,-1.72493333,-1.72493333,-1.20493333,-1.08493333,0.11506667,0.23506667,1.27506667,1.39506667,1.71506667,1.71506667,1.07506667,0.95506667,-0.44493333,-0.60493333,-1.52493333,-1.60493333,-1.72493333,-1.52493333,-0.60493333,-0.44493333,0.87506667,0.95506667,1.63506667,1.63506667,1.19506667,1.07506667,-0.08493333,-0.20493333,-1.28493333,-1.36493333,-1.56493333,-1.36493333,-0.36493333,-0.20493333,0.95506667,1.03506667,1.47506667,1.43506667,0.63506667,0.51506667,-0.92493333,-1.04493333,-1.36493333,-1.36493333,-0.68493333,-0.56493333,0.63506667,0.75506667,1.31506667,1.27506667,0.51506667,0.39506667,-0.68493333,-0.80493333,-1.20493333,-1.20493333,-0.48493333,-0.36493333,0.75506667,0.83506667,1.11506667,1.03506667,0.43506667,0.35506667,-0.60493333,-0.68493333,-1.00493333,-0.96493333,-0.40493333,-0.32493333,0.43506667,0.51506667,0.91506667,0.91506667,0.59506667,0.51506667,-0.24493333,-0.28493333,-0.76493333,-0.84493333,-0.72493333,-0.72493333,-0.20493333,-0.12493333,0.39506667,0.47506667,0.71506667,0.75506667,0.67506667,0.63506667,0.23506667,0.15506667,-0.32493333,-0.40493333,-0.64493333,-0.68493333,-0.60493333,-0.56493333,-0.28493333,-0.24493333,0.23506667,0.23506667,0.51506667,0.55506667,0.59506667,0.55506667,0.35506667,0.31506667,-0.00493333,-0.08493333,-0.40493333,-0.44493333,-0.52493333,-0.52493333,-0.32493333,-0.32493333,0.03506667,0.07506667,0.35506667,0.39506667,0.47506667,0.43506667,0.23506667,0.23506667,-0.08493333,-0.16493333,-0.36493333,-0.40493333,-0.40493333,-0.36493333,-0.12493333,-0.08493333,0.23506667,0.23506667,0.35506667,0.35506667,0.15506667,0.15506667,-0.16493333,-0.20493333,-0.32493333,-0.32493333,-0.16493333,-0.12493333,0.15506667,0.19506667,0.27506667,0.27506667,0.07506667,0.11506667,-0.16493333,-0.16493333,-0.28493333,-0.24493333,-0.08493333,-0.08493333,0.15506667,0.15506667,0.23506667,0.23506667,0.11506667,0.11506667,-0.12493333,-0.12493333,-0.20493333,-0.20493333,-0.08493333,-0.08493333,0.07506667,0.07506667,0.15506667,0.19506667,0.11506667,0.07506667,-0.08493333,-0.00493333,-0.16493333,-0.16493333,-0.12493333,-0.12493333,0.03506667,0.07506667,0.11506667,0.15506667,0.07506667,0.11506667,0.03506667,-0.00493333,-0.12493333,-0.12493333,-0.08493333,-0.12493333,-0.00493333,-0.00493333,0.11506667,0.11506667,0.07506667,0.11506667,0.03506667,0.03506667,-0.08493333,-0.08493333,-0.12493333,-0.08493333,-0.00493333,-0.00493333,0.07506667,0.07506667,0.11506667,0.11506667,0.03506667,0.03506667,-0.08493333,-0.00493333,-0.12493333,-0.08493333,-0.00493333,-0.00493333,0.07506667,0.07506667,0.07506667,0.11506667,0.03506667,0.03506667,-0.08493333,-0.08493333,-0.08493333,-0.08493333,-0.00493333,-0.00493333,0.07506667,0.11506667,0.03506667,0.07506667,0.03506667,0.03506667,-0.08493333,-0.08493333,-0.00493333,-0.08493333,-0.00493333,-0.00493333,0.07506667,0.03506667,0.07506667,0.03506667,-0.00493333,0.03506667,-0.00493333,-0.00493333,-0.08493333,-0.08493333,-0.00493333,-0.00493333,0.03506667,0.03506667,0.03506667,0.03506667,0.07506667,0.03506667,-0.00493333,0.03506667,-0.08493333,-0.00493333,-0.08493333,0.03506667,-0.00493333,-0.00493333,0.03506667,0.03506667,0.07506667,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,-0.08493333,-0.08493333,0.03506667,-0.00493333,0.03506667,-0.00493333,0.03506667,0.03506667,-0.00493333,0.03506667,-0.00493333,-0.00493333,-0.00493333,-0.00493333,0.03506667,-0.00493333,0.03506667,0.03506667,-0.00493333,0.03506667,-0.00493333,0.03506667,-0.00493333,0.03506667,-0.00493333,-0.00493333,0.03506667,-0.00493333,0.03506667])
kl_v = 0.1e-3

# Wellenlänge Laser
wl = 2. * (wl_se - wl_sa) / wl_m
wl_dsys = 2. / wl_m * sqrt(wl_se_dsys**2 + wl_sa_dsys**2 + (wl_m_dsys/wl_m)**2)
wl_mv = mv(wl)
wl_mv_dsto = dsto_mv(wl)
wl_mv_dsys = dsys_mv(wl_dsys)
wl_mv_dtot = dtot(wl_mv_dsys, wl_mv_dsto)

print()
print('Wellenlänge Laser')
print(val('wl',wl_mv,wl_mv_dtot))

# Brechungsindex Luft
pltext.initplot(num=1, title='Brechungsindex Luft', xlabel='Intensitätsringe', ylabel='Druck in Pa')
[sl1, dsl1, tmp, tmp] = linreg(bi_m1,bi_p1,bi_p1_dsys, plot=True, graphname='1. Durchgang')
[sl2, dsl2, tmp, tmp] = linreg(bi_m2,bi_p2,bi_p2_dsys, plot=True, graphname='2. Durchgang')
[sl3, dsl3, tmp, tmp] = linreg(bi_m3,bi_p3,bi_p3_dsys, plot=True, graphname='3. Durchgang')
slope = mv([sl1, sl2, sl3])
slope_dtot = dtot(dsys_mv(npfarray([dsl1, dsl2, dsl3])),dsto_mv(npfarray([sl1, sl2, sl3])))

n0 = (wl_mv * p0 * bi_T) / (2. * slope * bi_a * T0) + 1.
n0_dtot = p0 / (2. * abs(slope) * bi_a * T0) * sqrt((wl_mv_dtot * bi_T)**2 + (wl_mv * bi_T_dtot)**2 + (bi_a_dsys/bi_a)**2 + (slope_dtot/slope)**2)

print()
print('Brechungsindex Luft')
print(val('m/p',slope,slope_dtot))
print(val('n0',n0,n0_dtot))

# Kohärenzlänge
kl_U = kl_U - mv(kl_U)
U_top = []
t_top = []
lastmax = np.min(abs(kl_U))
for n in range(len(kl_U)):
  if (abs(kl_U[n]) > lastmax):
    U_top.append(abs(kl_U[n]))
    lastmax = abs(kl_U[n])
    t_top.append(kl_t[n])
    lastn = n + 1

for n in range(lastn, len(kl_U)):
  if abs(kl_U[n]) >= np.max([abs(kl_U[j]) for j in range(n,len(kl_U))]):
    U_top.append(abs(kl_U[n]))
    t_top.append(kl_t[n])

def gauss(x, A, mu, sigma):
  return A * exp(-(x - mu)**2 / (2. * sigma**2))
popt, pcov = curve_fit(gauss, t_top, U_top)

t_int = npfarray([0.1e-2 * n for n in range(-30,91)])
pltext.initplot(num=2, title='Signalverlauf LED', xlabel='Zeit in s', ylabel='Spannung in V')
plt.plot(kl_t, kl_U, label='Messwerte')
plt.plot(t_int, gauss(t_int, popt[0], popt[1], popt[2]), label='Gaußfit')

fwhm = 2.*kl_v * popt[2] * 2.*sqrt(2. * ln(2.))
L = wl_mv**2 / fwhm

print()
print('Kohärenzlänge LED')
print(val('L',L))

# Vergleich
print()
print(sig('Wellenlänge',wl_mv,wl_mv_dtot,wl_lit,wl_lit))
print(sig('Brechungsindex',n0,n0_dtot,bi_n0_lit))

plt.show()
