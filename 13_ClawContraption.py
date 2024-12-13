# https://adventofcode.com/2024/day/13
# Day 13: Claw Contraption

from re import *

def claw_contraption(data):
    for offset in 0, 10000000000000:
        res = 0
        for eqs in data.split('\n\n'):
            (a, b, c, d, e, f) = map(int, findall('\d+', eqs))
            e += offset
            f += offset
            D = a * d - c * b
            x, r = divmod(e * d - c * f, D)
            y, s = divmod(a * f - e * b, D)
            res += 0 if r + s else 3 * x + y
        yield int(res)


def inputs():

    yield """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
    
    yield """
Button A: X+46, Y+89
Button B: X+99, Y+32
Prize: X=5826, Y=7443

Button A: X+66, Y+31
Button B: X+23, Y+70
Prize: X=7780, Y=8390

Button A: X+40, Y+81
Button B: X+51, Y+15
Prize: X=12271, Y=14153

Button A: X+81, Y+83
Button B: X+74, Y+15
Prize: X=9473, Y=5449

Button A: X+13, Y+43
Button B: X+56, Y+32
Prize: X=6619, Y=373

Button A: X+40, Y+13
Button B: X+71, Y+95
Prize: X=8622, Y=8700

Button A: X+43, Y+94
Button B: X+73, Y+37
Prize: X=4797, Y=3009

Button A: X+87, Y+33
Button B: X+28, Y+70
Prize: X=7697, Y=3929

Button A: X+59, Y+38
Button B: X+16, Y+40
Prize: X=7920, Y=6864

Button A: X+74, Y+12
Button B: X+22, Y+81
Prize: X=2452, Y=18596

Button A: X+17, Y+68
Button B: X+78, Y+29
Prize: X=5557, Y=18778

Button A: X+61, Y+73
Button B: X+49, Y+12
Prize: X=6583, Y=6199

Button A: X+15, Y+81
Button B: X+50, Y+15
Prize: X=1940, Y=3336

Button A: X+51, Y+77
Button B: X+33, Y+14
Prize: X=5336, Y=19205

Button A: X+18, Y+33
Button B: X+60, Y+16
Prize: X=7338, Y=4241

Button A: X+99, Y+58
Button B: X+30, Y+53
Prize: X=8391, Y=5589

Button A: X+13, Y+56
Button B: X+71, Y+63
Prize: X=2373, Y=4151

Button A: X+52, Y+19
Button B: X+39, Y+68
Prize: X=18476, Y=3897

Button A: X+18, Y+65
Button B: X+66, Y+11
Prize: X=11612, Y=1592

Button A: X+53, Y+19
Button B: X+16, Y+45
Prize: X=17227, Y=5955

Button A: X+17, Y+52
Button B: X+42, Y+22
Prize: X=4984, Y=5024

Button A: X+50, Y+13
Button B: X+23, Y+43
Prize: X=3321, Y=16777

Button A: X+99, Y+11
Button B: X+78, Y+77
Prize: X=4128, Y=2167

Button A: X+62, Y+32
Button B: X+38, Y+89
Prize: X=5712, Y=7944

Button A: X+49, Y+26
Button B: X+19, Y+44
Prize: X=2700, Y=3366

Button A: X+45, Y+68
Button B: X+93, Y+15
Prize: X=3756, Y=1031

Button A: X+48, Y+22
Button B: X+29, Y+45
Prize: X=14156, Y=18998

Button A: X+65, Y+39
Button B: X+13, Y+31
Prize: X=13497, Y=6951

Button A: X+12, Y+35
Button B: X+59, Y+19
Prize: X=1564, Y=17449

Button A: X+86, Y+12
Button B: X+22, Y+54
Prize: X=3524, Y=2478

Button A: X+12, Y+31
Button B: X+92, Y+28
Prize: X=4348, Y=3894

Button A: X+15, Y+45
Button B: X+35, Y+13
Prize: X=5300, Y=16160

Button A: X+20, Y+62
Button B: X+78, Y+33
Prize: X=8480, Y=6176

Button A: X+12, Y+37
Button B: X+30, Y+17
Prize: X=8636, Y=1522

Button A: X+35, Y+91
Button B: X+97, Y+40
Prize: X=5566, Y=4286

Button A: X+70, Y+19
Button B: X+40, Y+72
Prize: X=7010, Y=2881

Button A: X+79, Y+14
Button B: X+45, Y+46
Prize: X=2915, Y=2646

Button A: X+20, Y+17
Button B: X+20, Y+89
Prize: X=2580, Y=7089

Button A: X+20, Y+62
Button B: X+98, Y+74
Prize: X=4852, Y=4930

Button A: X+41, Y+65
Button B: X+35, Y+18
Prize: X=10821, Y=16101

Button A: X+59, Y+96
Button B: X+25, Y+12
Prize: X=3286, Y=3540

Button A: X+60, Y+16
Button B: X+44, Y+96
Prize: X=2908, Y=2208

Button A: X+67, Y+34
Button B: X+11, Y+28
Prize: X=1190, Y=11006

Button A: X+52, Y+25
Button B: X+24, Y+53
Prize: X=18020, Y=5753

Button A: X+18, Y+62
Button B: X+77, Y+22
Prize: X=4881, Y=8984

Button A: X+13, Y+52
Button B: X+68, Y+27
Prize: X=10422, Y=10288

Button A: X+82, Y+83
Button B: X+12, Y+74
Prize: X=4762, Y=6119

Button A: X+65, Y+25
Button B: X+31, Y+70
Prize: X=19366, Y=12695

Button A: X+26, Y+65
Button B: X+47, Y+11
Prize: X=15571, Y=10762

Button A: X+11, Y+41
Button B: X+63, Y+38
Prize: X=19330, Y=11675

Button A: X+49, Y+17
Button B: X+13, Y+61
Prize: X=8694, Y=18710

Button A: X+58, Y+11
Button B: X+12, Y+43
Prize: X=6232, Y=14986

Button A: X+49, Y+22
Button B: X+22, Y+67
Prize: X=6238, Y=8056

Button A: X+24, Y+48
Button B: X+64, Y+35
Prize: X=9856, Y=11940

Button A: X+86, Y+97
Button B: X+98, Y+24
Prize: X=13426, Y=10730

Button A: X+13, Y+37
Button B: X+60, Y+38
Prize: X=1385, Y=9879

Button A: X+24, Y+49
Button B: X+58, Y+31
Prize: X=7232, Y=13984

Button A: X+73, Y+91
Button B: X+65, Y+15
Prize: X=7926, Y=9022

Button A: X+17, Y+86
Button B: X+90, Y+49
Prize: X=6199, Y=6982

Button A: X+14, Y+59
Button B: X+60, Y+39
Prize: X=4992, Y=5640

Button A: X+35, Y+78
Button B: X+55, Y+28
Prize: X=3430, Y=3010

Button A: X+93, Y+23
Button B: X+30, Y+39
Prize: X=10557, Y=5011

Button A: X+25, Y+84
Button B: X+80, Y+33
Prize: X=6480, Y=5031

Button A: X+25, Y+11
Button B: X+41, Y+60
Prize: X=9940, Y=8659

Button A: X+85, Y+17
Button B: X+82, Y+80
Prize: X=6742, Y=6182

Button A: X+13, Y+37
Button B: X+69, Y+48
Prize: X=4366, Y=13687

Button A: X+12, Y+20
Button B: X+55, Y+24
Prize: X=3481, Y=2080

Button A: X+14, Y+52
Button B: X+50, Y+20
Prize: X=14422, Y=17156

Button A: X+17, Y+26
Button B: X+85, Y+19
Prize: X=6086, Y=2315

Button A: X+14, Y+39
Button B: X+52, Y+12
Prize: X=5474, Y=4089

Button A: X+78, Y+45
Button B: X+12, Y+35
Prize: X=884, Y=12475

Button A: X+51, Y+23
Button B: X+21, Y+45
Prize: X=9608, Y=15828

Button A: X+80, Y+29
Button B: X+19, Y+87
Prize: X=3256, Y=3103

Button A: X+20, Y+58
Button B: X+58, Y+16
Prize: X=18674, Y=10192

Button A: X+41, Y+25
Button B: X+23, Y+78
Prize: X=2203, Y=2111

Button A: X+66, Y+93
Button B: X+82, Y+27
Prize: X=9672, Y=5394

Button A: X+77, Y+20
Button B: X+15, Y+68
Prize: X=14735, Y=1124

Button A: X+11, Y+50
Button B: X+61, Y+14
Prize: X=17846, Y=17220

Button A: X+59, Y+72
Button B: X+85, Y+27
Prize: X=5363, Y=4473

Button A: X+60, Y+31
Button B: X+53, Y+95
Prize: X=5536, Y=9081

Button A: X+72, Y+63
Button B: X+24, Y+85
Prize: X=4128, Y=4444

Button A: X+91, Y+24
Button B: X+22, Y+34
Prize: X=4938, Y=2966

Button A: X+34, Y+71
Button B: X+87, Y+33
Prize: X=7889, Y=5026

Button A: X+58, Y+63
Button B: X+14, Y+94
Prize: X=4538, Y=9578

Button A: X+28, Y+67
Button B: X+73, Y+55
Prize: X=6993, Y=7518

Button A: X+18, Y+91
Button B: X+50, Y+38
Prize: X=4006, Y=6292

Button A: X+86, Y+47
Button B: X+31, Y+87
Prize: X=5085, Y=3970

Button A: X+11, Y+46
Button B: X+42, Y+19
Prize: X=19769, Y=14095

Button A: X+74, Y+19
Button B: X+21, Y+67
Prize: X=13880, Y=8750

Button A: X+22, Y+70
Button B: X+99, Y+33
Prize: X=8206, Y=6934

Button A: X+54, Y+23
Button B: X+21, Y+61
Prize: X=5918, Y=16251

Button A: X+24, Y+39
Button B: X+30, Y+11
Prize: X=14630, Y=19481

Button A: X+54, Y+83
Button B: X+62, Y+26
Prize: X=4420, Y=3121

Button A: X+41, Y+15
Button B: X+20, Y+56
Prize: X=8464, Y=15604

Button A: X+52, Y+87
Button B: X+66, Y+20
Prize: X=2868, Y=1724

Button A: X+23, Y+73
Button B: X+50, Y+15
Prize: X=14055, Y=10765

Button A: X+57, Y+25
Button B: X+13, Y+40
Prize: X=6852, Y=6195

Button A: X+64, Y+22
Button B: X+21, Y+63
Prize: X=17980, Y=10000

Button A: X+71, Y+48
Button B: X+28, Y+68
Prize: X=4517, Y=4624

Button A: X+16, Y+92
Button B: X+50, Y+11
Prize: X=1628, Y=7702

Button A: X+46, Y+99
Button B: X+76, Y+33
Prize: X=12078, Y=13068

Button A: X+73, Y+26
Button B: X+61, Y+75
Prize: X=5049, Y=5634

Button A: X+23, Y+39
Button B: X+43, Y+13
Prize: X=4148, Y=3978

Button A: X+57, Y+21
Button B: X+30, Y+73
Prize: X=6029, Y=10726

Button A: X+19, Y+42
Button B: X+34, Y+14
Prize: X=752, Y=1782

Button A: X+75, Y+41
Button B: X+49, Y+91
Prize: X=5033, Y=8659

Button A: X+51, Y+29
Button B: X+28, Y+53
Prize: X=2672, Y=6081

Button A: X+22, Y+95
Button B: X+78, Y+77
Prize: X=1748, Y=4950

Button A: X+19, Y+70
Button B: X+83, Y+79
Prize: X=6107, Y=6851

Button A: X+74, Y+19
Button B: X+61, Y+62
Prize: X=6078, Y=6009

Button A: X+43, Y+61
Button B: X+76, Y+14
Prize: X=3754, Y=1010

Button A: X+56, Y+65
Button B: X+45, Y+13
Prize: X=2651, Y=1547

Button A: X+63, Y+45
Button B: X+28, Y+82
Prize: X=6818, Y=7412

Button A: X+40, Y+25
Button B: X+11, Y+33
Prize: X=11944, Y=16022

Button A: X+47, Y+19
Button B: X+33, Y+75
Prize: X=5736, Y=6450

Button A: X+38, Y+89
Button B: X+89, Y+50
Prize: X=8505, Y=11205

Button A: X+17, Y+85
Button B: X+28, Y+28
Prize: X=1581, Y=4097

Button A: X+41, Y+16
Button B: X+15, Y+57
Prize: X=4388, Y=10370

Button A: X+95, Y+39
Button B: X+36, Y+83
Prize: X=2773, Y=4413

Button A: X+80, Y+31
Button B: X+31, Y+83
Prize: X=9819, Y=8703

Button A: X+13, Y+31
Button B: X+96, Y+33
Prize: X=4634, Y=4193

Button A: X+12, Y+55
Button B: X+80, Y+17
Prize: X=12104, Y=1262

Button A: X+45, Y+79
Button B: X+40, Y+22
Prize: X=5030, Y=5262

Button A: X+72, Y+40
Button B: X+13, Y+49
Prize: X=1294, Y=4838

Button A: X+58, Y+20
Button B: X+17, Y+43
Prize: X=11537, Y=18431

Button A: X+23, Y+59
Button B: X+61, Y+34
Prize: X=7642, Y=7723

Button A: X+55, Y+34
Button B: X+18, Y+34
Prize: X=5365, Y=10410

Button A: X+16, Y+88
Button B: X+36, Y+40
Prize: X=4020, Y=11208

Button A: X+17, Y+54
Button B: X+80, Y+63
Prize: X=4426, Y=5841

Button A: X+21, Y+51
Button B: X+50, Y+26
Prize: X=9075, Y=2037

Button A: X+25, Y+60
Button B: X+63, Y+17
Prize: X=19354, Y=1841

Button A: X+15, Y+36
Button B: X+69, Y+50
Prize: X=18074, Y=12164

Button A: X+65, Y+37
Button B: X+20, Y+54
Prize: X=15420, Y=10398

Button A: X+91, Y+37
Button B: X+45, Y+70
Prize: X=7547, Y=3689

Button A: X+11, Y+17
Button B: X+50, Y+24
Prize: X=4565, Y=891

Button A: X+38, Y+32
Button B: X+97, Y+13
Prize: X=6420, Y=1560

Button A: X+48, Y+19
Button B: X+32, Y+51
Prize: X=2064, Y=8477

Button A: X+33, Y+71
Button B: X+79, Y+18
Prize: X=5538, Y=2341

Button A: X+47, Y+19
Button B: X+21, Y+56
Prize: X=1466, Y=4784

Button A: X+16, Y+57
Button B: X+47, Y+14
Prize: X=10890, Y=12655

Button A: X+19, Y+65
Button B: X+77, Y+34
Prize: X=4981, Y=3275

Button A: X+52, Y+75
Button B: X+37, Y+12
Prize: X=4862, Y=16721

Button A: X+54, Y+80
Button B: X+34, Y+13
Prize: X=4332, Y=13007

Button A: X+47, Y+66
Button B: X+57, Y+18
Prize: X=5906, Y=3144

Button A: X+50, Y+12
Button B: X+45, Y+83
Prize: X=5275, Y=9227

Button A: X+64, Y+33
Button B: X+33, Y+84
Prize: X=3282, Y=7185

Button A: X+91, Y+28
Button B: X+11, Y+77
Prize: X=8105, Y=8015

Button A: X+64, Y+14
Button B: X+16, Y+53
Prize: X=2288, Y=19247

Button A: X+28, Y+72
Button B: X+66, Y+13
Prize: X=5164, Y=12100

Button A: X+44, Y+78
Button B: X+81, Y+42
Prize: X=4694, Y=3648

Button A: X+98, Y+50
Button B: X+50, Y+96
Prize: X=9028, Y=5452

Button A: X+13, Y+58
Button B: X+76, Y+71
Prize: X=5600, Y=5415

Button A: X+36, Y+12
Button B: X+24, Y+69
Prize: X=7136, Y=9800

Button A: X+11, Y+48
Button B: X+52, Y+24
Prize: X=1837, Y=17552

Button A: X+12, Y+51
Button B: X+21, Y+11
Prize: X=4538, Y=10584

Button A: X+67, Y+76
Button B: X+95, Y+17
Prize: X=8134, Y=4144

Button A: X+27, Y+83
Button B: X+94, Y+35
Prize: X=11320, Y=10926

Button A: X+51, Y+28
Button B: X+16, Y+37
Prize: X=18394, Y=7724

Button A: X+16, Y+87
Button B: X+42, Y+17
Prize: X=5370, Y=8696

Button A: X+28, Y+83
Button B: X+93, Y+27
Prize: X=10339, Y=8018

Button A: X+54, Y+21
Button B: X+13, Y+38
Prize: X=6183, Y=19732

Button A: X+24, Y+97
Button B: X+92, Y+74
Prize: X=2652, Y=8038

Button A: X+17, Y+92
Button B: X+89, Y+22
Prize: X=8227, Y=3614

Button A: X+63, Y+19
Button B: X+14, Y+67
Prize: X=3493, Y=4004

Button A: X+11, Y+19
Button B: X+45, Y+17
Prize: X=1190, Y=10370

Button A: X+51, Y+12
Button B: X+24, Y+59
Prize: X=6530, Y=13600

Button A: X+67, Y+31
Button B: X+11, Y+41
Prize: X=6841, Y=289

Button A: X+31, Y+59
Button B: X+66, Y+36
Prize: X=14590, Y=15318

Button A: X+72, Y+25
Button B: X+18, Y+53
Prize: X=2762, Y=15786

Button A: X+15, Y+41
Button B: X+66, Y+45
Prize: X=16427, Y=8793

Button A: X+54, Y+21
Button B: X+20, Y+52
Prize: X=11110, Y=3663

Button A: X+89, Y+16
Button B: X+12, Y+46
Prize: X=8925, Y=3972

Button A: X+29, Y+20
Button B: X+20, Y+94
Prize: X=1887, Y=1542

Button A: X+91, Y+21
Button B: X+37, Y+60
Prize: X=5132, Y=4272

Button A: X+52, Y+91
Button B: X+91, Y+20
Prize: X=8398, Y=7734

Button A: X+97, Y+15
Button B: X+64, Y+98
Prize: X=15103, Y=10441

Button A: X+85, Y+14
Button B: X+61, Y+79
Prize: X=11721, Y=8550

Button A: X+80, Y+36
Button B: X+31, Y+46
Prize: X=4383, Y=3030

Button A: X+62, Y+56
Button B: X+19, Y+61
Prize: X=4693, Y=6913

Button A: X+88, Y+63
Button B: X+17, Y+65
Prize: X=8500, Y=9255

Button A: X+83, Y+30
Button B: X+31, Y+91
Prize: X=11224, Y=11797

Button A: X+65, Y+27
Button B: X+50, Y+71
Prize: X=4605, Y=6082

Button A: X+69, Y+38
Button B: X+19, Y+43
Prize: X=459, Y=16498

Button A: X+22, Y+30
Button B: X+97, Y+41
Prize: X=2530, Y=1442

Button A: X+74, Y+41
Button B: X+13, Y+78
Prize: X=4527, Y=7818

Button A: X+41, Y+17
Button B: X+16, Y+30
Prize: X=2485, Y=3903

Button A: X+38, Y+66
Button B: X+40, Y+13
Prize: X=14936, Y=4261

Button A: X+13, Y+42
Button B: X+63, Y+24
Prize: X=5494, Y=4464

Button A: X+15, Y+96
Button B: X+85, Y+78
Prize: X=7925, Y=7848

Button A: X+30, Y+76
Button B: X+51, Y+14
Prize: X=6578, Y=980

Button A: X+24, Y+93
Button B: X+88, Y+27
Prize: X=3112, Y=1383

Button A: X+30, Y+42
Button B: X+34, Y+13
Prize: X=3144, Y=3156

Button A: X+14, Y+92
Button B: X+97, Y+37
Prize: X=6405, Y=4263

Button A: X+27, Y+48
Button B: X+66, Y+32
Prize: X=3954, Y=4640

Button A: X+57, Y+19
Button B: X+15, Y+65
Prize: X=585, Y=1395

Button A: X+75, Y+43
Button B: X+12, Y+44
Prize: X=10319, Y=5967

Button A: X+24, Y+61
Button B: X+39, Y+14
Prize: X=4484, Y=15526

Button A: X+35, Y+36
Button B: X+93, Y+12
Prize: X=8976, Y=1536

Button A: X+72, Y+15
Button B: X+60, Y+75
Prize: X=7272, Y=2265

Button A: X+70, Y+26
Button B: X+24, Y+97
Prize: X=4156, Y=8062

Button A: X+26, Y+80
Button B: X+79, Y+60
Prize: X=7919, Y=7340

Button A: X+24, Y+12
Button B: X+23, Y+60
Prize: X=3645, Y=11612

Button A: X+14, Y+48
Button B: X+59, Y+21
Prize: X=1906, Y=4722

Button A: X+46, Y+91
Button B: X+80, Y+19
Prize: X=7704, Y=2150

Button A: X+73, Y+18
Button B: X+50, Y+94
Prize: X=9314, Y=9402

Button A: X+31, Y+82
Button B: X+89, Y+14
Prize: X=6548, Y=2264

Button A: X+63, Y+29
Button B: X+45, Y+93
Prize: X=6273, Y=3249

Button A: X+67, Y+74
Button B: X+97, Y+26
Prize: X=10789, Y=5750

Button A: X+17, Y+53
Button B: X+63, Y+35
Prize: X=8488, Y=15320

Button A: X+67, Y+23
Button B: X+21, Y+67
Prize: X=14545, Y=14063

Button A: X+41, Y+11
Button B: X+31, Y+75
Prize: X=3039, Y=3569

Button A: X+18, Y+37
Button B: X+37, Y+16
Prize: X=4860, Y=19639

Button A: X+14, Y+50
Button B: X+74, Y+61
Prize: X=6558, Y=8175

Button A: X+85, Y+51
Button B: X+48, Y+95
Prize: X=9071, Y=8223

Button A: X+14, Y+93
Button B: X+86, Y+99
Prize: X=958, Y=1641

Button A: X+20, Y+12
Button B: X+21, Y+48
Prize: X=2231, Y=2436

Button A: X+30, Y+42
Button B: X+73, Y+11
Prize: X=6954, Y=2622

Button A: X+23, Y+73
Button B: X+88, Y+78
Prize: X=8879, Y=10869

Button A: X+21, Y+66
Button B: X+67, Y+18
Prize: X=4778, Y=5388

Button A: X+11, Y+24
Button B: X+46, Y+28
Prize: X=6340, Y=13440

Button A: X+47, Y+23
Button B: X+26, Y+50
Prize: X=2230, Y=2806

Button A: X+91, Y+18
Button B: X+16, Y+77
Prize: X=8136, Y=8919

Button A: X+78, Y+15
Button B: X+28, Y+51
Prize: X=5746, Y=3477

Button A: X+92, Y+17
Button B: X+65, Y+96
Prize: X=6745, Y=4018

Button A: X+86, Y+45
Button B: X+15, Y+67
Prize: X=7198, Y=9090

Button A: X+65, Y+21
Button B: X+17, Y+62
Prize: X=3532, Y=8152

Button A: X+26, Y+45
Button B: X+54, Y+26
Prize: X=9864, Y=873

Button A: X+33, Y+71
Button B: X+73, Y+40
Prize: X=2949, Y=2833

Button A: X+76, Y+25
Button B: X+23, Y+49
Prize: X=2413, Y=1581

Button A: X+33, Y+42
Button B: X+95, Y+25
Prize: X=11269, Y=5231

Button A: X+97, Y+24
Button B: X+27, Y+90
Prize: X=6964, Y=4056

Button A: X+48, Y+11
Button B: X+21, Y+80
Prize: X=9326, Y=7660

Button A: X+78, Y+34
Button B: X+13, Y+41
Prize: X=6048, Y=2932

Button A: X+46, Y+13
Button B: X+21, Y+75
Prize: X=12934, Y=16405

Button A: X+27, Y+74
Button B: X+60, Y+47
Prize: X=7074, Y=8818

Button A: X+32, Y+44
Button B: X+94, Y+33
Prize: X=9400, Y=6380

Button A: X+38, Y+38
Button B: X+59, Y+15
Prize: X=2554, Y=2378

Button A: X+87, Y+55
Button B: X+13, Y+84
Prize: X=6441, Y=6118

Button A: X+73, Y+11
Button B: X+33, Y+39
Prize: X=3622, Y=3302

Button A: X+16, Y+62
Button B: X+61, Y+25
Prize: X=12601, Y=5779

Button A: X+50, Y+42
Button B: X+33, Y+95
Prize: X=3079, Y=6825

Button A: X+21, Y+55
Button B: X+24, Y+12
Prize: X=3950, Y=3942

Button A: X+14, Y+73
Button B: X+45, Y+13
Prize: X=9880, Y=12514

Button A: X+28, Y+72
Button B: X+66, Y+25
Prize: X=4002, Y=507

Button A: X+79, Y+27
Button B: X+22, Y+66
Prize: X=7368, Y=6144

Button A: X+21, Y+51
Button B: X+64, Y+16
Prize: X=8182, Y=15610

Button A: X+61, Y+27
Button B: X+25, Y+54
Prize: X=259, Y=7685

Button A: X+21, Y+31
Button B: X+52, Y+20
Prize: X=4777, Y=2227

Button A: X+41, Y+44
Button B: X+62, Y+17
Prize: X=679, Y=481

Button A: X+24, Y+35
Button B: X+65, Y+31
Prize: X=7674, Y=5450

Button A: X+63, Y+34
Button B: X+28, Y+59
Prize: X=12051, Y=12743

Button A: X+40, Y+72
Button B: X+96, Y+33
Prize: X=8424, Y=8313

Button A: X+74, Y+38
Button B: X+53, Y+92
Prize: X=4761, Y=4194

Button A: X+89, Y+91
Button B: X+90, Y+15
Prize: X=10779, Y=3396

Button A: X+27, Y+81
Button B: X+56, Y+19
Prize: X=5408, Y=3559

Button A: X+78, Y+22
Button B: X+14, Y+21
Prize: X=4354, Y=2541

Button A: X+52, Y+31
Button B: X+13, Y+42
Prize: X=6412, Y=8395

Button A: X+29, Y+90
Button B: X+34, Y+28
Prize: X=3635, Y=6630

Button A: X+95, Y+21
Button B: X+21, Y+62
Prize: X=8441, Y=3644

Button A: X+56, Y+13
Button B: X+11, Y+50
Prize: X=7989, Y=7651

Button A: X+28, Y+75
Button B: X+91, Y+23
Prize: X=6944, Y=7121

Button A: X+29, Y+76
Button B: X+66, Y+20
Prize: X=2690, Y=12896

Button A: X+59, Y+39
Button B: X+31, Y+64
Prize: X=4202, Y=4866

Button A: X+78, Y+15
Button B: X+23, Y+80
Prize: X=8008, Y=3505

Button A: X+50, Y+13
Button B: X+16, Y+82
Prize: X=6326, Y=8339

Button A: X+70, Y+23
Button B: X+20, Y+52
Prize: X=8210, Y=11585

Button A: X+28, Y+69
Button B: X+28, Y+18
Prize: X=3248, Y=6219

Button A: X+97, Y+51
Button B: X+27, Y+53
Prize: X=7688, Y=6448

Button A: X+73, Y+25
Button B: X+35, Y+56
Prize: X=7858, Y=5596

Button A: X+38, Y+18
Button B: X+14, Y+45
Prize: X=17294, Y=14435

Button A: X+62, Y+28
Button B: X+18, Y+38
Prize: X=14660, Y=2052

Button A: X+92, Y+45
Button B: X+22, Y+42
Prize: X=9750, Y=6987

Button A: X+11, Y+83
Button B: X+61, Y+11
Prize: X=5413, Y=5351

Button A: X+20, Y+63
Button B: X+94, Y+78
Prize: X=2868, Y=4236

Button A: X+64, Y+14
Button B: X+19, Y+50
Prize: X=13060, Y=5076

Button A: X+31, Y+77
Button B: X+56, Y+18
Prize: X=19794, Y=4592

Button A: X+13, Y+88
Button B: X+79, Y+70
Prize: X=5342, Y=6416

Button A: X+62, Y+46
Button B: X+31, Y+77
Prize: X=4154, Y=8158

Button A: X+37, Y+11
Button B: X+37, Y+57
Prize: X=1813, Y=1367

Button A: X+40, Y+67
Button B: X+47, Y+24
Prize: X=5233, Y=15974

Button A: X+56, Y+14
Button B: X+16, Y+73
Prize: X=16248, Y=12141

Button A: X+18, Y+41
Button B: X+36, Y+25
Prize: X=3960, Y=4004

Button A: X+57, Y+51
Button B: X+22, Y+96
Prize: X=3377, Y=3861

Button A: X+23, Y+64
Button B: X+66, Y+26
Prize: X=6750, Y=5918

Button A: X+73, Y+48
Button B: X+22, Y+48
Prize: X=17229, Y=848

Button A: X+54, Y+17
Button B: X+21, Y+91
Prize: X=4944, Y=7970

Button A: X+57, Y+20
Button B: X+23, Y+65
Prize: X=5736, Y=16035

Button A: X+38, Y+91
Button B: X+27, Y+19
Prize: X=2836, Y=5787

Button A: X+75, Y+29
Button B: X+63, Y+83
Prize: X=9483, Y=6071

Button A: X+46, Y+19
Button B: X+20, Y+55
Prize: X=7470, Y=12955

Button A: X+91, Y+13
Button B: X+21, Y+19
Prize: X=10381, Y=2667

Button A: X+11, Y+27
Button B: X+55, Y+25
Prize: X=5655, Y=2955

Button A: X+64, Y+11
Button B: X+15, Y+75
Prize: X=13004, Y=19196

Button A: X+68, Y+18
Button B: X+25, Y+81
Prize: X=2803, Y=4833

Button A: X+75, Y+15
Button B: X+12, Y+16
Prize: X=3045, Y=745

Button A: X+13, Y+73
Button B: X+40, Y+12
Prize: X=8692, Y=10996

Button A: X+45, Y+21
Button B: X+31, Y+66
Prize: X=3759, Y=2991

Button A: X+17, Y+92
Button B: X+88, Y+80
Prize: X=8733, Y=11996

Button A: X+37, Y+79
Button B: X+59, Y+32
Prize: X=3727, Y=3259

Button A: X+73, Y+42
Button B: X+18, Y+41
Prize: X=11287, Y=14472

Button A: X+13, Y+90
Button B: X+57, Y+62
Prize: X=5281, Y=11282

Button A: X+34, Y+26
Button B: X+20, Y+56
Prize: X=978, Y=870

Button A: X+75, Y+94
Button B: X+92, Y+15
Prize: X=10286, Y=7074

Button A: X+14, Y+63
Button B: X+39, Y+12
Prize: X=10905, Y=752

Button A: X+47, Y+25
Button B: X+17, Y+79
Prize: X=3407, Y=7129

Button A: X+61, Y+11
Button B: X+25, Y+61
Prize: X=9032, Y=17858

Button A: X+94, Y+29
Button B: X+62, Y+88
Prize: X=12466, Y=7565

Button A: X+17, Y+41
Button B: X+41, Y+26
Prize: X=15757, Y=19582

Button A: X+54, Y+22
Button B: X+17, Y+57
Prize: X=12980, Y=6276

Button A: X+28, Y+88
Button B: X+33, Y+24
Prize: X=4151, Y=5792

Button A: X+76, Y+22
Button B: X+16, Y+66
Prize: X=3060, Y=13520

Button A: X+40, Y+75
Button B: X+46, Y+11
Prize: X=12698, Y=19628

Button A: X+20, Y+87
Button B: X+90, Y+49
Prize: X=1810, Y=5476

Button A: X+79, Y+26
Button B: X+58, Y+71
Prize: X=3450, Y=1395

Button A: X+71, Y+22
Button B: X+12, Y+67
Prize: X=15351, Y=14713

Button A: X+67, Y+17
Button B: X+30, Y+81
Prize: X=1621, Y=1284

Button A: X+90, Y+46
Button B: X+17, Y+42
Prize: X=5534, Y=5560

Button A: X+83, Y+34
Button B: X+15, Y+61
Prize: X=11391, Y=6126

Button A: X+99, Y+23
Button B: X+80, Y+87
Prize: X=4029, Y=1757

Button A: X+14, Y+50
Button B: X+70, Y+29
Prize: X=12562, Y=1392
"""

for data in inputs():
    print(*claw_contraption(data.strip()))