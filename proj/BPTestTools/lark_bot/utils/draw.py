import csv

import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np
from fps_avg_datas import *

res_t = [{'date': '2022-02-19', 'total_time': 21.006191498749402, 'android_enter': 22.419060800806648,
  'ios_success': 8.24016025709106},
 {'date': '2022-02-20', 'total_time': 19.331317030260525, 'android_enter': 20.901845818135804,
  'ios_success': 7.226433995166532},
 {'date': '2022-02-21', 'total_time': 18.722859914215178, 'android_enter': 20.535326979474643,
  'ios_success': 7.027378724526917},
 {'date': '2022-02-22', 'total_time': 20.23846735055918, 'android_enter': 22.120076323482877,
  'ios_success': 7.394506249919022},
 {'date': '2022-02-23', 'total_time': 19.078287648084675, 'android_enter': 20.492817605313114,
  'ios_success': 7.236230465459668},
 {'date': '2022-02-24', 'total_time': 17.654103061384074, 'android_enter': 18.95821281153904,
  'ios_success': 7.796914951386913},
 {'date': '2022-02-25', 'total_time': 17.953697726899794, 'android_enter': 19.20727316333374,
  'ios_success': 7.6357182699051025},
 {'date': '2022-02-26', 'total_time': 17.320205750289713, 'android_enter': 18.334942949963903,
  'ios_success': 7.364968388127858},
 {'date': '2022-02-27', 'total_time': 17.72577858878794, 'android_enter': 18.886420122438942,
  'ios_success': 6.967630716423029},
 {'date': '2022-02-28', 'total_time': 18.607593401701525, 'android_enter': 19.85310437797424,
  'ios_success': 7.115986735423149},
 {'date': '2022-03-01', 'total_time': 18.141913900162436, 'android_enter': 19.090979614167487,
  'ios_success': 7.229889876089699},
 {'date': '2022-03-02', 'total_time': 18.232135534728673, 'android_enter': 18.991712449971253,
  'ios_success': 7.743150518692705},
 {'date': '2022-03-03', 'total_time': 18.068178076511707, 'android_enter': 18.7431952484814,
  'ios_success': 7.839710067811963},
 {'date': '2022-03-04', 'total_time': 18.777845233736866, 'android_enter': 19.55698429622424,
  'ios_success': 7.9683382038751525},
 {'date': '2022-03-05', 'total_time': 17.555674927339442, 'android_enter': 18.292088167986932,
  'ios_success': 7.363438304125011},
 {'date': '2022-03-06', 'total_time': 17.90828569335172, 'android_enter': 18.810489154658857,
  'ios_success': 6.9599316233679165},
 {'date': '2022-03-07', 'total_time': 18.119097674139052, 'android_enter': 19.1337959265843,
  'ios_success': 6.907591515282135},
 {'date': '2022-03-08', 'total_time': 18.184975634105204, 'android_enter': 18.925837316872848,
  'ios_success': 7.382907858780247},
 {'date': '2022-03-09', 'total_time': 17.44479033886276, 'android_enter': 18.120401258090236,
  'ios_success': 7.202526195928347},
 {'date': '2022-03-10', 'total_time': 17.10020457898468, 'android_enter': 18.268009174241314,
  'ios_success': 7.254249535055062},
 {'date': '2022-03-11', 'total_time': 15.627310225066363, 'android_enter': 16.690581629533153,
  'ios_success': 7.108844251820842},
 {'date': '2022-03-12', 'total_time': 14.944684526734713, 'android_enter': 15.90485737350879,
  'ios_success': 7.069471306149125},
 {'date': '2022-03-13', 'total_time': 14.494651308559101, 'android_enter': 15.481014262633186,
  'ios_success': 6.7092053953518285},
 {'date': '2022-03-14', 'total_time': 14.81880527438669, 'android_enter': 16.162367037769332,
  'ios_success': 6.837191713318003},
 {'date': '2022-03-15', 'total_time': 15.991814090300897, 'android_enter': 17.688800709317075,
  'ios_success': 7.581636697313819},
 {'date': '2022-03-16', 'total_time': 17.306574408375873, 'android_enter': 18.945728621687575,
  'ios_success': 8.359236612250083},
 {'date': '2022-03-17', 'total_time': 16.641862471050814, 'android_enter': 17.966406963551794,
  'ios_success': 8.16869227624019},
 {'date': '2022-03-18', 'total_time': 17.72944933368051, 'android_enter': 19.185978489338307,
  'ios_success': 8.349174681260553},
 {'date': '2022-03-19', 'total_time': 17.418298108627408, 'android_enter': 18.669030927499307,
  'ios_success': 8.07070579015862},
 {'date': '2022-03-20', 'total_time': 17.239956650078962, 'android_enter': 18.617358047330036,
  'ios_success': 8.163940486913052},
 {'date': '2022-03-21', 'total_time': 17.30012837171102, 'android_enter': 18.704551427952655,
  'ios_success': 8.190696862831919},
 {'date': '2022-03-22', 'total_time': 18.534615421918616, 'android_enter': 19.80058064828368,
  'ios_success': 8.192207374913055},
 {'date': '2022-03-23', 'total_time': 19.29, 'android_enter': 20.92,
  'ios_success': 7.35},
 {'date': '2022-03-24', 'total_time': 19.995079900126942, 'android_enter': 22.179957376419907,
  'ios_success': 9.387357996337384},
 {'date': '2022-03-25', 'total_time': 19.312464772159647, 'android_enter': 20.39881128702241,
  'ios_success': 8.301635973013424},
 {'date': '2022-03-26', 'total_time': 19.851376988308427, 'android_enter': 21.02630443686572,
  'ios_success': 8.383091481136361},
 {'date': '2022-03-27', 'total_time': 19.58422350201919, 'android_enter': 20.889976530972724,
  'ios_success': 8.318085547969416},
 {'date': '2022-03-28', 'total_time': 18.962417195734453, 'android_enter': 20.196134962949127,
  'ios_success': 7.868284056364692},
 {'date': '2022-03-29', 'total_time': 17.739055772534716, 'android_enter': 18.493915454981366,
  'ios_success': 7.7461216081236},
 {'date': '2022-03-30', 'total_time': 16.806111217035383, 'android_enter': 17.496972060862806,
  'ios_success': 7.455039335888978},
 {'date': '2022-03-31', 'total_time': 15.984281560561339, 'android_enter': 16.623502335114154,
  'ios_success': 7.0531081114319045},
 {'date': '2022-04-01', 'total_time': 16.42837808863684, 'android_enter': 17.045366987793752,
  'ios_success': 7.007225192247551},
 {'date': '2022-04-02', 'total_time': 16.216093598102937, 'android_enter': 16.842234966959783,
  'ios_success': 6.879743869490832},
 {'date': '2022-04-03', 'total_time': 16.172510485997822, 'android_enter': 16.894282666566617,
  'ios_success': 6.562026116174872},
 {'date': '2022-04-04', 'total_time': 16.657072362378244, 'android_enter': 17.34719057444695,
  'ios_success': 6.806164654415447},
 {'date': '2022-04-05', 'total_time': 16.071648391404842, 'android_enter': 16.663782037802797,
  'ios_success': 6.703490053225068},
 {'date': '2022-04-06', 'total_time': 16.070058432682217, 'android_enter': 16.611319131037813,
  'ios_success': 6.655062705590129},
 {'date': '2022-04-07', 'total_time': 15.889712671183673, 'android_enter': 16.42519706257236,
  'ios_success': 6.382871678680897},
 {'date': '2022-04-08', 'total_time': 15.251736351812907, 'android_enter': 15.69163712438301,
  'ios_success': 6.4270199366411855},
 {'date': '2022-04-09', 'total_time': 15.78529404872454, 'android_enter': 16.250539894124643,
  'ios_success': 6.551085149258959},
 {'date': '2022-04-10', 'total_time': 16.064547176280005, 'android_enter': 16.540798588227517,
  'ios_success': 6.478061693881641},
 {'date': '2022-04-11', 'total_time': 16.06894721729645, 'android_enter': 16.56002706776878,
  'ios_success': 6.611226753560294},
 {'date': '2022-04-12', 'total_time': 16.348681635243633, 'android_enter': 16.776862185110605,
  'ios_success': 6.759042739496894},
 {'date': '2022-04-13', 'total_time': 16.284538480889996, 'android_enter': 16.772512731466396,
  'ios_success': 6.487032653551792},
 {'date': '2022-04-14', 'total_time': 16.399972617935564, 'android_enter': 16.937097197694573,
  'ios_success': 6.562544195722433},
 {'date': '2022-04-15', 'total_time': 16.388217058967278, 'android_enter': 16.87222020645411,
  'ios_success': 7.396033275353641},
 {'date': '2022-04-16', 'total_time': 16.20544388972451, 'android_enter': 16.754698390216944,
  'ios_success': 7.181500467652207},
 {'date': '2022-04-17', 'total_time': 16.100999055969204, 'android_enter': 16.676209312948245,
  'ios_success': 6.860827724978601}
         # {'date': '2022-04-18', 'total_time': 0, 'android_enter': 0, 'ios_success': 0}
         ]

res_rate = [
    {'date': '2022-02-18', 'total_rate': 82.98, 'total_enter': 453001, 'total_success': 375921, 'android_rate': 82.4,
     'android_enter': 414621, 'android_success': 341631, 'ios_rate': 89.34, 'ios_enter': 38380, 'ios_success': 34290},
    {'date': '2022-02-19', 'total_rate': 81.81, 'total_enter': 609520, 'total_success': 498662, 'android_rate': 81.08,
     'android_enter': 554056, 'android_success': 449248, 'ios_rate': 89.09, 'ios_enter': 55464, 'ios_success': 49414},
    {'date': '2022-02-20', 'total_rate': 85.7, 'total_enter': 653941, 'total_success': 560420, 'android_rate': 84.95,
     'android_enter': 584463, 'android_success': 496477, 'ios_rate': 92.03, 'ios_enter': 69478, 'ios_success': 63943},
    {'date': '2022-02-21', 'total_rate': 86.08, 'total_enter': 495273, 'total_success': 426344, 'android_rate': 85.17,
     'android_enter': 433837, 'android_success': 369488, 'ios_rate': 92.55, 'ios_enter': 61436, 'ios_success': 56856},
    {'date': '2022-02-22', 'total_rate': 84.61, 'total_enter': 428655, 'total_success': 362678, 'android_rate': 83.64,
     'android_enter': 378528, 'android_success': 316594, 'ios_rate': 91.93, 'ios_enter': 50127, 'ios_success': 46084},
    {'date': '2022-02-23', 'total_rate': 84.73, 'total_enter': 424216, 'total_success': 359422, 'android_rate': 84.09,
     'android_enter': 382057, 'android_success': 321276, 'ios_rate': 90.48, 'ios_enter': 42159, 'ios_success': 38146},
    {'date': '2022-02-24', 'total_rate': 83.9, 'total_enter': 465302, 'total_success': 390382, 'android_rate': 83.3,
     'android_enter': 414139, 'android_success': 344990, 'ios_rate': 88.72, 'ios_enter': 51163, 'ios_success': 45392},
    {'date': '2022-02-25', 'total_rate': 82.04, 'total_enter': 498565, 'total_success': 409035, 'android_rate': 81.59,
     'android_enter': 447316, 'android_success': 364966, 'ios_rate': 85.99, 'ios_enter': 51249, 'ios_success': 44069},
    {'date': '2022-02-26', 'total_rate': 87.76, 'total_enter': 642363, 'total_success': 563747, 'android_rate': 87.49,
     'android_enter': 585099, 'android_success': 511903, 'ios_rate': 90.54, 'ios_enter': 57264, 'ios_success': 51844},
    {'date': '2022-02-27', 'total_rate': 84.74, 'total_enter': 671894, 'total_success': 569332, 'android_rate': 84.34,
     'android_enter': 609685, 'android_success': 514204, 'ios_rate': 88.62, 'ios_enter': 62209, 'ios_success': 55128},
    {'date': '2022-02-28', 'total_rate': 75.25, 'total_enter': 533234, 'total_success': 401245, 'android_rate': 74.97,
     'android_enter': 483146, 'android_success': 362227, 'ios_rate': 77.9, 'ios_enter': 50088, 'ios_success': 39018},
    {'date': '2022-03-01', 'total_rate': 89.49, 'total_enter': 487700, 'total_success': 436455, 'android_rate': 89.32,
     'android_enter': 449690, 'android_success': 401678, 'ios_rate': 91.49, 'ios_enter': 38010, 'ios_success': 34777},
    {'date': '2022-03-02', 'total_rate': 89.0, 'total_enter': 488825, 'total_success': 435042, 'android_rate': 88.92,
     'android_enter': 456361, 'android_success': 405802, 'ios_rate': 90.07, 'ios_enter': 32464, 'ios_success': 29240},
    {'date': '2022-03-03', 'total_rate': 87.66, 'total_enter': 570203, 'total_success': 499828, 'android_rate': 87.6,
     'android_enter': 535419, 'android_success': 469038, 'ios_rate': 88.52, 'ios_enter': 34784, 'ios_success': 30790},
    {'date': '2022-03-04', 'total_rate': 89.4, 'total_enter': 600962, 'total_success': 537273, 'android_rate': 89.29,
     'android_enter': 561508, 'android_success': 501347, 'ios_rate': 91.06, 'ios_enter': 39454, 'ios_success': 35926},
    {'date': '2022-03-05', 'total_rate': 91.24, 'total_enter': 645121, 'total_success': 588577, 'android_rate': 91.19,
     'android_enter': 602181, 'android_success': 549103, 'ios_rate': 91.93, 'ios_enter': 42940, 'ios_success': 39474},
    {'date': '2022-03-06', 'total_rate': 90.69, 'total_enter': 670937, 'total_success': 608490, 'android_rate': 90.51,
     'android_enter': 621307, 'android_success': 562373, 'ios_rate': 92.92, 'ios_enter': 49630, 'ios_success': 46117},
    {'date': '2022-03-07', 'total_rate': 90.11, 'total_enter': 546840, 'total_success': 492773, 'android_rate': 89.95,
     'android_enter': 502599, 'android_success': 452084, 'ios_rate': 91.97, 'ios_enter': 44241, 'ios_success': 40689},
    {'date': '2022-03-08', 'total_rate': 89.19, 'total_enter': 537241, 'total_success': 479171, 'android_rate': 89.14,
     'android_enter': 503204, 'android_success': 448571, 'ios_rate': 89.9, 'ios_enter': 34037, 'ios_success': 30600},
    {'date': '2022-03-09', 'total_rate': 92.41, 'total_enter': 544498, 'total_success': 503160, 'android_rate': 92.4,
     'android_enter': 511013, 'android_success': 472174, 'ios_rate': 92.54, 'ios_enter': 33485, 'ios_success': 30986},
    {'date': '2022-03-10', 'total_rate': 92.71, 'total_enter': 522396, 'total_success': 484315, 'android_rate': 92.65,
     'android_enter': 467657, 'android_success': 433285, 'ios_rate': 93.22, 'ios_enter': 54739, 'ios_success': 51030},
    {'date': '2022-03-11', 'total_rate': 93.34, 'total_enter': 620792, 'total_success': 579472, 'android_rate': 93.33,
     'android_enter': 552321, 'android_success': 515488, 'ios_rate': 93.45, 'ios_enter': 68471, 'ios_success': 63984},
    {'date': '2022-03-12', 'total_rate': 93.6, 'total_enter': 775381, 'total_success': 725720, 'android_rate': 93.62,
     'android_enter': 691492, 'android_success': 647343, 'ios_rate': 93.43, 'ios_enter': 83889, 'ios_success': 78377},
    {'date': '2022-03-13', 'total_rate': 93.58, 'total_enter': 740418, 'total_success': 692872, 'android_rate': 93.59,
     'android_enter': 657440, 'android_success': 615302, 'ios_rate': 93.48, 'ios_enter': 82978, 'ios_success': 77570},
    {'date': '2022-03-14', 'total_rate': 93.55, 'total_enter': 597440, 'total_success': 558921, 'android_rate': 93.48,
     'android_enter': 512186, 'android_success': 478785, 'ios_rate': 94.0, 'ios_enter': 85254, 'ios_success': 80136},
    {'date': '2022-03-15', 'total_rate': 91.99, 'total_enter': 580860, 'total_success': 534353, 'android_rate': 91.7,
     'android_enter': 485268, 'android_success': 444969, 'ios_rate': 93.51, 'ios_enter': 95592, 'ios_success': 89384},
    {'date': '2022-03-16', 'total_rate': 91.47, 'total_enter': 528566, 'total_success': 483455, 'android_rate': 91.17,
     'android_enter': 448527, 'android_success': 408923, 'ios_rate': 93.12, 'ios_enter': 80039, 'ios_success': 74532},
    {'date': '2022-03-17', 'total_rate': 92.6, 'total_enter': 562099, 'total_success': 520503, 'android_rate': 92.41,
     'android_enter': 487353, 'android_success': 450359, 'ios_rate': 93.84, 'ios_enter': 74746, 'ios_success': 70144},
    {'date': '2022-03-18', 'total_rate': 92.0, 'total_enter': 609174, 'total_success': 560460, 'android_rate': 91.8,
     'android_enter': 528818, 'android_success': 485442, 'ios_rate': 93.36, 'ios_enter': 80356, 'ios_success': 75018},
    {'date': '2022-03-19', 'total_rate': 92.61, 'total_enter': 768589, 'total_success': 711821, 'android_rate': 92.49,
     'android_enter': 679222, 'android_success': 628204, 'ios_rate': 93.57, 'ios_enter': 89367, 'ios_success': 83617},
    {'date': '2022-03-20', 'total_rate': 92.52, 'total_enter': 773704, 'total_success': 715830, 'android_rate': 92.3,
     'android_enter': 673812, 'android_success': 621950, 'ios_rate': 93.98, 'ios_enter': 99892, 'ios_success': 93880},
    {'date': '2022-03-21', 'total_rate': 92.19, 'total_enter': 611314, 'total_success': 563556, 'android_rate': 91.96,
     'android_enter': 531297, 'android_success': 488599, 'ios_rate': 93.68, 'ios_enter': 80017, 'ios_success': 74957},
    {'date': '2022-03-22', 'total_rate': 90.2, 'total_enter': 552017, 'total_success': 497902, 'android_rate': 89.92,
     'android_enter': 493469, 'android_success': 443744, 'ios_rate': 92.5, 'ios_enter': 58548, 'ios_success': 54158},
    {'date': '2022-03-23', 'total_rate': 88.79, 'total_enter': 499315, 'total_success': 443365, 'android_rate': 88.79,
     'android_enter': 460666, 'android_success': 409039, 'ios_rate': 88.81, 'ios_enter': 38649, 'ios_success': 34326},
    {'date': '2022-03-24', 'total_rate': 88.74, 'total_enter': 581319, 'total_success': 515843, 'android_rate': 88.72,
     'android_enter': 534860, 'android_success': 474515, 'ios_rate': 88.96, 'ios_enter': 46459, 'ios_success': 41328},
    {'date': '2022-03-25', 'total_rate': 83.97, 'total_enter': 813571, 'total_success': 683160, 'android_rate': 84.37,
     'android_enter': 740917, 'android_success': 625117, 'ios_rate': 79.89, 'ios_enter': 72654, 'ios_success': 58043},
    {'date': '2022-03-26', 'total_rate': 85.53, 'total_enter': 818803, 'total_success': 700356, 'android_rate': 85.95,
     'android_enter': 743765, 'android_success': 639283, 'ios_rate': 81.39, 'ios_enter': 75038, 'ios_success': 61073},
    {'date': '2022-03-27', 'total_rate': 82.16, 'total_enter': 864814, 'total_success': 710515, 'android_rate': 82.93,
     'android_enter': 776133, 'android_success': 643621, 'ios_rate': 75.43, 'ios_enter': 88681, 'ios_success': 66894},
    {'date': '2022-03-28', 'total_rate': 67.67, 'total_enter': 889498, 'total_success': 601929, 'android_rate': 68.51,
     'android_enter': 798934, 'android_success': 547336, 'ios_rate': 60.28, 'ios_enter': 90564, 'ios_success': 54593},
    {'date': '2022-03-29', 'total_rate': 63.02, 'total_enter': 907563, 'total_success': 571981, 'android_rate': 63.07,
     'android_enter': 840158, 'android_success': 529865, 'ios_rate': 62.48, 'ios_enter': 67405, 'ios_success': 42116},
    {'date': '2022-03-30', 'total_rate': 76.31, 'total_enter': 799791, 'total_success': 610285, 'android_rate': 76.42,
     'android_enter': 742742, 'android_success': 567618, 'ios_rate': 74.79, 'ios_enter': 57049, 'ios_success': 42667},
    {'date': '2022-03-31', 'total_rate': 80.11, 'total_enter': 862510, 'total_success': 690950, 'android_rate': 80.0,
     'android_enter': 803627, 'android_success': 642865, 'ios_rate': 81.66, 'ios_enter': 58883, 'ios_success': 48085},
    {'date': '2022-04-01', 'total_rate': 87.42, 'total_enter': 867917, 'total_success': 758755, 'android_rate': 87.55,
     'android_enter': 813166, 'android_success': 711956, 'ios_rate': 85.48, 'ios_enter': 54751, 'ios_success': 46799},
    {'date': '2022-04-02', 'total_rate': 78.05, 'total_enter': 1017489, 'total_success': 794161, 'android_rate': 77.97,
     'android_enter': 951832, 'android_success': 742135, 'ios_rate': 79.24, 'ios_enter': 65657, 'ios_success': 52026},
    {'date': '2022-04-03', 'total_rate': 82.97, 'total_enter': 941444, 'total_success': 781136, 'android_rate': 83.13,
     'android_enter': 874077, 'android_success': 726603, 'ios_rate': 80.95, 'ios_enter': 67367, 'ios_success': 54533},
    {'date': '2022-04-04', 'total_rate': 61.43, 'total_enter': 1013692, 'total_success': 622718, 'android_rate': 61.16,
     'android_enter': 944044, 'android_success': 577424, 'ios_rate': 65.03, 'ios_enter': 69648, 'ios_success': 45294},

    {'date': '2022-04-06', 'total_rate': 77.14, 'total_enter': 751396, 'total_success': 579626, 'android_rate': 77.02,
     'android_enter': 709043, 'android_success': 546115, 'ios_rate': 79.12, 'ios_enter': 42353, 'ios_success': 33511},
    {'date': '2022-04-07', 'total_rate': 84.03, 'total_enter': 744283, 'total_success': 625393, 'android_rate': 83.98,
     'android_enter': 703671, 'android_success': 590911, 'ios_rate': 84.91, 'ios_enter': 40612, 'ios_success': 34482},
    {'date': '2022-04-08', 'total_rate': 81.85, 'total_enter': 946373, 'total_success': 774571, 'android_rate': 81.8,
     'android_enter': 900088, 'android_success': 736234, 'ios_rate': 82.83, 'ios_enter': 46285, 'ios_success': 38337},
    {'date': '2022-04-09', 'total_rate': 86.47, 'total_enter': 1105402, 'total_success': 955811, 'android_rate': 86.67,
     'android_enter': 1050663, 'android_success': 910609, 'ios_rate': 82.58, 'ios_enter': 54739, 'ios_success': 45202},
    {'date': '2022-04-10', 'total_rate': 69.01, 'total_enter': 1513241, 'total_success': 1044216, 'android_rate': 69.01,
     'android_enter': 1437998, 'android_success': 992427, 'ios_rate': 68.83, 'ios_enter': 75243, 'ios_success': 51789},
    {'date': '2022-04-11', 'total_rate': 68.18, 'total_enter': 1290924, 'total_success': 880105, 'android_rate': 68.1,
     'android_enter': 1223818, 'android_success': 833448, 'ios_rate': 69.53, 'ios_enter': 67106, 'ios_success': 46657},
    {'date': '2022-04-12', 'total_rate': 64.58, 'total_enter': 1186227, 'total_success': 766048, 'android_rate': 64.37,
     'android_enter': 1133272, 'android_success': 729484, 'ios_rate': 69.05, 'ios_enter': 52955, 'ios_success': 36564},
    {'date': '2022-04-13', 'total_rate': 92.16, 'total_enter': 838279, 'total_success': 772524, 'android_rate': 92.22,
     'android_enter': 797761, 'android_success': 735730, 'ios_rate': 90.81, 'ios_enter': 40518, 'ios_success': 36794},
    {'date': '2022-04-14', 'total_rate': 91.82, 'total_enter': 808824, 'total_success': 742631, 'android_rate': 91.91,
     'android_enter': 766311, 'android_success': 704290, 'ios_rate': 90.19, 'ios_enter': 42513, 'ios_success': 38341},
    {'date': '2022-04-15', 'total_rate': 80.43, 'total_enter': 1042998, 'total_success': 838860, 'android_rate': 80.36,
     'android_enter': 989230, 'android_success': 794909, 'ios_rate': 81.74, 'ios_enter': 53768, 'ios_success': 43951},
    {'date': '2022-04-16', 'total_rate': 92.28, 'total_enter': 1075549, 'total_success': 992503, 'android_rate': 92.26,
     'android_enter': 1010435, 'android_success': 932271, 'ios_rate': 92.5, 'ios_enter': 65114, 'ios_success': 60232},
    {'date': '2022-04-17', 'total_rate': 89.38, 'total_enter': 1082986, 'total_success': 968003, 'android_rate': 89.31,
     'android_enter': 1019894, 'android_success': 910917, 'ios_rate': 90.48, 'ios_enter': 63092, 'ios_success': 57086}]

res = [{'date': '2022-02-12', 'total_avg': 31.60099192870549, 'android_avg': 28.570188373452364,
        'ios_avg': 51.311295896328275},
       {'date': '2022-02-13', 'total_avg': 30.47224597509415, 'android_avg': 27.16963721940402,
        'ios_avg': 51.196776539948715},
       {'date': '2022-02-14', 'total_avg': 29.56354507472425, 'android_avg': 26.097415117326133,
        'ios_avg': 50.08445183140994},
       {'date': '2022-02-15', 'total_avg': 28.65160941166949, 'android_avg': 26.35048685823232,
        'ios_avg': 47.53109869646182},
       {'date': '2022-02-16', 'total_avg': 28.872224075776955, 'android_avg': 26.9135400256171,
        'ios_avg': 49.09246717346234},
       {'date': '2022-02-17', 'total_avg': 29.313780323040014, 'android_avg': 27.302325117850494,
        'ios_avg': 51.24280178189852},
       {'date': '2022-02-18', 'total_avg': 28.719574942693043, 'android_avg': 26.489919989174016,
        'ios_avg': 51.45885519097403},
       {'date': '2022-02-19', 'total_avg': 30.054412610692477, 'android_avg': 27.628287589358333,
        'ios_avg': 52.223427902196505},
       {'date': '2022-02-20', 'total_avg': 31.032764247005176, 'android_avg': 28.249905632779388,
        'ios_avg': 52.563574635855865},
       {'date': '2022-02-21', 'total_avg': 31.88666400239225, 'android_avg': 28.599283360444456,
        'ios_avg': 52.80286008230451},
       {'date': '2022-02-22', 'total_avg': 30.83067991340757, 'android_avg': 27.533828363511432,
        'ios_avg': 52.7264312383323},
       {'date': '2022-02-23', 'total_avg': 30.57418788706066, 'android_avg': 27.949507816150863,
        'ios_avg': 52.28002867294147},
       {'date': '2022-02-24', 'total_avg': 31.625394429011102, 'android_avg': 28.944411083199444,
        'ios_avg': 51.80172250615181},
       {'date': '2022-02-25', 'total_avg': 30.651665115169514, 'android_avg': 28.154302412551555,
        'ios_avg': 51.81608235265212},
       {'date': '2022-02-26', 'total_avg': 30.65712857142858, 'android_avg': 28.49860894500052,
        'ios_avg': 51.99517927755809},
       {'date': '2022-02-27', 'total_avg': 30.367432622480283, 'android_avg': 28.041055979006156,
        'ios_avg': 51.92272784836843},
       {'date': '2022-02-28', 'total_avg': 30.20540560587237, 'android_avg': 27.879703037014906,
        'ios_avg': 52.149108500345534},
       {'date': '2022-03-01', 'total_avg': 34.405176556497295, 'android_avg': 32.921549590210546,
        'ios_avg': 51.65102013149868},
       {'date': '2022-03-02', 'total_avg': 36.35905356346727, 'android_avg': 35.28690278918662,
        'ios_avg': 51.44674213031479},
       {'date': '2022-03-03', 'total_avg': 36.310600759753804, 'android_avg': 35.36873748479746,
        'ios_avg': 51.03757203227046},
       {'date': '2022-03-04', 'total_avg': 36.895211590336814, 'android_avg': 35.905016499084134,
        'ios_avg': 51.07318031498643},
       {'date': '2022-03-05', 'total_avg': 37.39937585688594, 'android_avg': 36.42417041429953,
        'ios_avg': 51.40070382630998},
       {'date': '2022-03-06', 'total_avg': 37.40516772710745, 'android_avg': 36.22620879877521,
        'ios_avg': 52.095180418874605},
       {'date': '2022-03-07', 'total_avg': 37.408303842828225, 'android_avg': 36.11741097843694,
        'ios_avg': 52.0487898789879},
       {'date': '2022-03-08', 'total_avg': 36.88022883711139, 'android_avg': 35.92111438223076,
        'ios_avg': 51.07049223678744},
       {'date': '2022-03-09', 'total_avg': 35.834168493933305, 'android_avg': 34.92371120649278,
        'ios_avg': 50.143676859192134},
       {'date': '2022-03-10', 'total_avg': 35.094023063806006, 'android_avg': 33.509390125847055,
        'ios_avg': 48.69854095484347},
       {'date': '2022-03-11', 'total_avg': 36.04082340020354, 'android_avg': 34.41664613123838,
        'ios_avg': 49.36700055648303},
       {'date': '2022-03-12', 'total_avg': 36.616042314733384, 'android_avg': 35.09210002552585,
        'ios_avg': 49.4878931339143},
       {'date': '2022-03-13', 'total_avg': 36.885162999963164, 'android_avg': 35.230362429657326,
        'ios_avg': 50.19364757202144},
       {'date': '2022-03-14', 'total_avg': 37.544104407659574, 'android_avg': 35.41315924563061,
        'ios_avg': 50.50752258233983},
       {'date': '2022-03-15', 'total_avg': 37.58194918750932, 'android_avg': 35.118876892799825,
        'ios_avg': 50.072632546736145},
       {'date': '2022-03-16', 'total_avg': 36.5606912944439, 'android_avg': 34.265863362443646,
        'ios_avg': 49.448432329718585},
       {'date': '2022-03-17', 'total_avg': 36.89356698953025, 'android_avg': 34.93881687036148,
        'ios_avg': 49.936407842059154},
       {'date': '2022-03-18', 'total_avg': 36.423750790902126, 'android_avg': 34.41507797510819,
        'ios_avg': 49.99796554340983},
       {'date': '2022-03-19', 'total_avg': 36.40013090000366, 'android_avg': 34.58045757135205,
        'ios_avg': 50.487567364512444},
       {'date': '2022-03-20', 'total_avg': 36.61801811446109, 'android_avg': 34.60074548518784,
        'ios_avg': 50.47414838355605},
       {'date': '2022-03-21', 'total_avg': 36.384069101883654, 'android_avg': 34.329856278546984,
        'ios_avg': 50.17678227360307},
       {'date': '2022-03-22', 'total_avg': 36.535680178519115, 'android_avg': 34.915840604527126,
        'ios_avg': 50.479456721706164},
       {'date': '2022-03-23', 'total_avg': 35.95, 'android_avg': 34.74,
        'ios_avg': 50.62},
       {'date': '2022-03-24', 'total_avg': 34.182499108310566, 'android_avg': 31.51812456263127,
        'ios_avg': 49.21958925750401},
       {'date': '2022-03-25', 'total_avg': 36.17859309696949, 'android_avg': 34.82087959009396,
        'ios_avg': 51.125248381514034},
       {'date': '2022-03-26', 'total_avg': 35.66150850963639, 'android_avg': 34.208839231106104,
        'ios_avg': 51.102912223133714},
       {'date': '2022-03-27', 'total_avg': 35.843997859644105, 'android_avg': 34.2744604088157,
        'ios_avg': 51.109430055577754},
       {'date': '2022-03-28', 'total_avg': 35.79735231333991, 'android_avg': 34.26964980804249,
        'ios_avg': 51.11759591591057},
       {'date': '2022-03-29', 'total_avg': 35.176487977507556, 'android_avg': 34.01035345092133,
        'ios_avg': 50.360508110687014},
       {'date': '2022-03-30', 'total_avg': 35.32994007912274, 'android_avg': 34.2851017143444,
        'ios_avg': 49.95279856330438},
       {'date': '2022-03-31', 'total_avg': 35.56804146257644, 'android_avg': 34.512100890020136,
        'ios_avg': 50.40414304746479},
       {'date': '2022-04-01', 'total_avg': 34.3731099043895, 'android_avg': 33.37968444594016,
        'ios_avg': 50.20641547323364},
       # {'date': '2022-04-02', 'total_avg': 34.399075925593735, 'android_avg': 33.339607778624895,
       #  'ios_avg': 50.18594291371059},
       {'date': '2022-04-03', 'total_avg': 34.95287941252258, 'android_avg': 33.76867266508402,
        'ios_avg': 51.24478848373739},
       # {'date': '2022-04-04', 'total_avg': 34.59996433909721, 'android_avg': 33.3707206050752,
       #  'ios_avg': 51.171153106630776},
       {'date': '2022-04-05', 'total_avg': 34.29574998246694, 'android_avg': 33.25017934199591,
        'ios_avg': 50.750284826514765},
       {'date': '2022-04-06', 'total_avg': 34.13865155267281, 'android_avg': 33.17185278163016,
        'ios_avg': 50.54675803508252},
       {'date': '2022-04-07', 'total_avg': 33.61837840063491, 'android_avg': 32.64645413296985,
        'ios_avg': 50.58527064838164},
       {'date': '2022-04-08', 'total_avg': 33.633952242675484, 'android_avg': 32.743609848634605,
        'ios_avg': 51.01048994199681},
       {'date': '2022-04-09', 'total_avg': 33.02665155250331, 'android_avg': 32.19487921181564,
        'ios_avg': 50.16258551919062},
       {'date': '2022-04-10', 'total_avg': 33.24952983893487, 'android_avg': 32.36603411715136,
        'ios_avg': 50.561390449121376},
       {'date': '2022-04-11', 'total_avg': 33.08923046280281, 'android_avg': 32.13927798311978,
        'ios_avg': 50.3505596819751}]


def line_base() -> Line:
    date_list = [d['date'] for d in res]
    total_list = [round(d['total_avg'], 2) for d in res]
    android_list = [round(d['android_avg'], 2) for d in res]
    ios_list = [round(d['ios_avg'], 2) for d in res]
    c = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis(series_name="总平均FPS", y_axis=total_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="Android平均FPS", y_axis=android_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="iOS平均FPS", y_axis=ios_list, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="BP FPS趋势图"),
                             yaxis_opts=opts.AxisOpts(name='FPS值'),
                             xaxis_opts=opts.AxisOpts(name='日期')

                             )
    )
    return c


def draw_engine_rate(res):
    date_list = [d['date'] for d in res]
    total_list = [round(d['total_rate'], 2) for d in res]
    android_list = [round(d['android_rate'], 2) for d in res]
    ios_list = [round(d['ios_rate'], 2) for d in res]

    c = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis(series_name="总success_rate", y_axis=total_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="Android success_rate", y_axis=android_list,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="iOS success_rate", y_axis=ios_list, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="BP 进房成功率趋势图"),
                             yaxis_opts=opts.AxisOpts(name='成功率'),
                             xaxis_opts=opts.AxisOpts(name='日期')

                             )
    )
    return c


def draw_engine_enter_success(res):
    date_list = [d['date'] for d in res]
    total_list = [d['total_enter'] for d in res]
    android_list = [d['android_enter'] for d in res]
    ios_list = [d['ios_enter'] for d in res]

    total_succ_list = [d['total_success'] for d in res]
    android_succ_list = [d['android_success'] for d in res]
    ios_succ_list = [d['ios_success'] for d in res]

    c = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis(series_name="总进房量", y_axis=total_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="Android进房量", y_axis=android_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="iOS进房量", y_axis=ios_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="总成功进房", y_axis=total_succ_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="Android成功进房量", y_axis=android_succ_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="iOS成功进房量", y_axis=ios_succ_list, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="进房量趋势图"),
                             yaxis_opts=opts.AxisOpts(name='进房量'),
                             xaxis_opts=opts.AxisOpts(name='日期')

                             )
    )
    return c


def draw_enter_time(res):
    date_list = [d['date'] for d in res]
    total_list = [d['total_time'] for d in res]
    android_list = [d['android_enter'] for d in res]
    ios_list = [d['ios_success'] for d in res]

    c = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis(series_name="总平均时长", y_axis=total_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="Android 平均时长", y_axis=android_list, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name="iOS 平均时长", y_axis=ios_list, label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="平均进房时长趋势图"),
                             yaxis_opts=opts.AxisOpts(name='时长（秒）'),
                             xaxis_opts=opts.AxisOpts(name='日期')

                             )
    )
    return c


if __name__ == '__main__':
    # line_base().render('line1.html')
    # # tmp = [[d['date'], round(d['total_avg'], 2), round(d['android_avg'], 2), round(d['ios_avg'], 2)] for d in res]
    # with open('avg_fps.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["date", "total_avg_fps", "android_avg_fps", "ios_avg_fps"])
    #     writer.writerows(tmp)
    res = get_res_data()
    draw_engine_rate(res_rate).render("rate.html")
    draw_engine_enter_success(res_rate).render("enter.html")
    # res_t = get_enter_time()
    # draw_enter_time(res_t).render("avg-time.html")
