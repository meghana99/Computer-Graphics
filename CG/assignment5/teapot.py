'''
//  teapot.py
//
//  Routines for tessellating a standard teapot.
//
//  Students should not be modifying this file.
//
//  @author Srini
'''

from simpleShape import simpleShape

class teapot(simpleShape):

    teapotVertices = [
    0.098626,  0.499861, -0.285539,  0.098626,  0.499861, -0.166305,
     0.103349,  0.495678, -0.164634, -0.014442,  0.499861, -0.399697,
    -0.125276,  0.499861, -0.399697, -0.124885,  0.495678, -0.398472,
    -0.233668,  0.495678, -0.283884, -0.233668,  0.495678, -0.167959,
    -0.235994,  0.487311, -0.167137, -0.243066,  0.495678, -0.287210,
    -0.238344,  0.499861, -0.285539, -0.126456,  0.499861, -0.403397,
    -0.014832,  0.495678, -0.053372, -0.014442,  0.499861, -0.052147,
     0.095114,  0.499861, -0.167548, -0.234831,  0.499861, -0.284296,
    -0.234831,  0.499861, -0.167548, -0.014832,  0.495678, -0.398472,
    -0.125666,  0.487311, -0.400922, -0.013262,  0.499861, -0.048447,
    -0.126456,  0.499861, -0.048447, -0.128042,  0.495678, -0.043472,
     0.096277,  0.487311, -0.284707,  0.096277,  0.487311, -0.167137,
     0.093951,  0.495678, -0.167959, -0.011675,  0.495678, -0.043472,
    -0.235994,  0.487311, -0.284707, -0.011675,  0.495678, -0.408372,
    -0.128042,  0.495678, -0.408372,  0.070712,  0.499861, -0.334590,
     0.073705,  0.499861, -0.336903, -0.014051,  0.487311, -0.400922,
    -0.243066,  0.495678, -0.164634,  0.095114,  0.499861, -0.284296,
     0.093951,  0.495678, -0.283884, -0.124885,  0.495678, -0.053372,
    -0.125276,  0.499861, -0.052147, -0.014051,  0.487311, -0.050922,
     0.007794,  0.255758,  0.017578,  0.127115,  0.255758, -0.073652,
     0.009866,  0.288108,  0.024078, -0.238344,  0.499861, -0.166305,
    -0.125666,  0.487311, -0.050922,  0.009866,  0.288108, -0.475922,
    -0.149584,  0.288108, -0.475922, -0.307195,  0.288108, -0.309901,
    -0.268472,  0.440618, -0.244874, -0.268472,  0.440618, -0.206970,
    -0.405045,  0.423728, -0.206970, -0.033205,  0.582610, -0.212917,
    -0.046902,  0.582610, -0.193002, -0.043216,  0.571614, -0.187716,
     0.103349,  0.495678, -0.287210,  0.167477,  0.288108, -0.309901,
    -0.149584,  0.288108,  0.024078, -0.147511,  0.255758,  0.017578,
    -0.129653,  0.188507, -0.038422, -0.069859,  0.188507, -0.028504,
     0.167477,  0.288108, -0.141943,  0.161307,  0.255758, -0.144126,
    -0.318450,  0.283965, -0.206970, -0.379458,  0.331574, -0.206970,
    -0.315351,  0.274084, -0.197494, -0.147511,  0.255758, -0.469422,
    -0.266832,  0.255758, -0.378191,  0.007794,  0.255758, -0.469422,
    -0.077011,  0.541016, -0.203519, -0.087985,  0.541016, -0.211903,
    -0.077831,  0.527152, -0.200922,  0.081815,  0.188507, -0.108671,
     0.161307,  0.255758, -0.307718,  0.074698,  0.255758, -0.433405,
     0.041453,  0.188507, -0.385689,  0.040028,  0.182610, -0.383644,
    -0.069859,  0.188507, -0.423340, -0.258576,  0.464283, -0.244874,
    -0.411516,  0.452046, -0.244874, -0.411516,  0.452046, -0.206970,
    -0.221532,  0.188507, -0.343172, -0.307195,  0.288108, -0.141943,
    -0.301024,  0.255758, -0.144126, -0.424567,  0.431661, -0.197494,
    -0.433466,  0.435277, -0.206970, -0.440796,  0.407630, -0.206970,
    -0.433466,  0.435277, -0.244874, -0.424567,  0.431661, -0.254350,
    -0.420405,  0.407630, -0.254350, -0.431500,  0.407630, -0.254350,
    -0.413945,  0.427344, -0.197494, -0.420405,  0.407630, -0.197494,
     0.290167,  0.447480, -0.244409,  0.295282,  0.446196, -0.225922,
     0.290167,  0.447480, -0.207435, -0.413945,  0.427344, -0.254350,
    -0.405045,  0.423728, -0.244874, -0.265373,  0.448029, -0.197494,
    -0.431500,  0.407630, -0.197494, -0.440796,  0.407630, -0.244874,
    -0.247861,  0.188507, -0.162938, -0.435727,  0.373886, -0.244874,
    -0.435727,  0.373886, -0.206970, -0.308554,  0.252411, -0.206970,
    -0.311653,  0.262291, -0.197494, -0.061886,  0.527152, -0.200922,
    -0.062706,  0.541016, -0.203519, -0.212830,  0.497192, -0.276511,
    -0.212830,  0.497192, -0.175333, -0.093592,  0.527152, -0.234320,
    -0.318450,  0.283965, -0.244874, -0.315351,  0.274084, -0.254350,
    -0.379458,  0.331574, -0.244874, -0.319749,  0.288108, -0.225922,
     0.346618,  0.493377, -0.210785,  0.217033,  0.288937, -0.186921,
     0.142548,  0.259662, -0.184227,  0.142548,  0.248268, -0.225922,
     0.326737,  0.493022, -0.203217,  0.210637,  0.310674, -0.167420,
     0.142548,  0.286833, -0.163380, -0.092815,  0.582610, -0.258842,
    -0.106513,  0.582610, -0.238927, -0.057512,  0.582610, -0.264532,
     0.210637,  0.310674, -0.284423,  0.142549,  0.286833, -0.288464,
     0.142548,  0.319264, -0.288464,  0.196608,  0.358355, -0.264923,
     0.275290,  0.487311, -0.241715,  0.303009,  0.492597, -0.248627,
     0.193926,  0.367471, -0.225922,  0.267494,  0.487311, -0.225922,
     0.142548,  0.357829, -0.225922,  0.142548,  0.346435, -0.184227,
    -0.055530,  0.571614, -0.270733, -0.062706,  0.541016, -0.248324,
    -0.077011,  0.541016, -0.248324,  0.142548,  0.346435, -0.267617,
     0.351059,  0.496732, -0.212352,  0.359204,  0.496993, -0.225922,
     0.348533,  0.497053, -0.214222, -0.308554,  0.252411, -0.244874,
     0.073113,  0.497192, -0.175333, -0.046125,  0.527152, -0.234320,
    -0.046125,  0.527152, -0.217524,  0.142548,  0.259662, -0.267617,
     0.346618,  0.493377, -0.241058,  0.217033,  0.288937, -0.264923,
    -0.112400,  0.571614, -0.241015, -0.106130,  0.571614, -0.197858,
     0.312374,  0.487311, -0.211708,  0.306254,  0.492850, -0.210722,
     0.309708,  0.495492, -0.208372,  0.297581,  0.487311, -0.211708,
     0.331636,  0.496109, -0.205567,  0.303009,  0.492597, -0.203217,
     0.285186,  0.487311, -0.216446,  0.291059,  0.492316, -0.215789,
     0.292009,  0.494781, -0.214222,  0.196608,  0.358355, -0.186921,
     0.275290,  0.487311, -0.210128,  0.279988,  0.487311, -0.225922,
     0.284686,  0.492092, -0.225922,  0.284586,  0.494483, -0.225922,
     0.291059,  0.492316, -0.236055,  0.292009,  0.494781, -0.237622,
     0.306254,  0.492850, -0.241122,  0.285186,  0.487311, -0.235398,
     0.309708,  0.495492, -0.243472,  0.312374,  0.487311, -0.240136,
     0.297581,  0.487311, -0.240136, -0.301024,  0.255758, -0.307718,
     0.331636,  0.496109, -0.246276,  0.326738,  0.493022, -0.248627,
     0.324769,  0.487311, -0.235398,  0.351059,  0.496732, -0.239492,
    -0.061886,  0.527152, -0.250922, -0.077831,  0.527152, -0.250922,
    -0.411109,  0.407630, -0.206970, -0.096501,  0.571614, -0.264128,
    -0.091126,  0.541016, -0.233456, -0.083167,  0.541016, -0.245016,
    -0.056550,  0.541016, -0.206828, -0.093592,  0.527152, -0.217524,
    -0.091126,  0.541016, -0.218388, -0.027318,  0.571614, -0.210829,
    -0.033588,  0.571614, -0.253986, -0.051732,  0.541016, -0.239940,
    -0.048591,  0.541016, -0.233456, -0.048591,  0.541016, -0.218388,
    -0.082205,  0.582610, -0.187312, -0.084187,  0.571614, -0.181111,
    -0.038606,  0.582610, -0.250104, -0.101111,  0.582610, -0.201740,
    -0.021832,  0.497192, -0.376522, -0.018037,  0.487311, -0.388422,
    -0.121680,  0.487311, -0.388422, -0.013262,  0.499861, -0.403397,
     0.073113,  0.497192, -0.276511,  0.084410,  0.487311, -0.171335,
    -0.224127,  0.487311, -0.280508, -0.224127,  0.487311, -0.171335,
    -0.121680,  0.487311, -0.063422, -0.018037,  0.487311, -0.063422,
    -0.021832,  0.497192, -0.075322,  0.084410,  0.487311, -0.280508,
     0.142549,  0.319264, -0.163380, -0.117885,  0.497192, -0.376522,
     0.105865,  0.182610, -0.288100,  0.108143,  0.188507, -0.288906,
     0.117559,  0.188507, -0.225922, -0.117885,  0.497192, -0.075322,
    -0.129653,  0.188507, -0.038422, -0.128887,  0.182610, -0.040822,
    -0.257277,  0.188507, -0.225922, -0.247861,  0.188507, -0.162938,
    -0.010830,  0.182610, -0.040822, -0.245582,  0.182610, -0.163744,
    -0.219591,  0.182610, -0.341672, -0.010065,  0.188507, -0.038422,
    -0.010065,  0.188507, -0.038422,  0.079874,  0.182610, -0.110172,
    -0.129653,  0.188507, -0.413422, -0.128887,  0.182610, -0.411022,
    -0.258576,  0.464283, -0.206970, -0.129653,  0.188507, -0.413422,
    -0.261675,  0.456873, -0.254350,  0.108143,  0.188507, -0.288906,
    -0.265373,  0.448029, -0.254350, -0.311653,  0.262291, -0.254350,
     0.219715,  0.279821, -0.225922, -0.411109,  0.407630, -0.244874,
    -0.261675,  0.456873, -0.197494,  0.330833,  0.496342, -0.208372,
     0.324769,  0.487311, -0.216446]

    #Connectivity data for the teapot
    #Each group of 3 integers specifies a triangle

    teapotFaces = [
     0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,
     12,  13,  14,   5,   4,  15,  15,  16,   7,  17,   5,  18,
     19,  20,  21,  22,  23,  24,   1,  19,  25,  26,  18,   5,
     27,  28,  11,   3,  29,  30,  17,  31,  22,  10,   9,  32,
     33,  34,  24,  12,  35,  36,  23,  37,  12,  38,  39,  40,
     20,  13,  36,  20,  41,  32,  35,  42,   8,  35,   7,  16,
      2,  25,  40,  42,  35,  12,  28,  27,  43,  28,  44,  45,
     46,  47,  48,  49,  50,  51,  52,  53,  43,  34,  33,  29,
     25,  21,  54,  55,  56,  57,  53,  58,  59,  60,  61,  62,
     63,  64,  44,  65,  63,  44,  54,  55,  38,  66,  67,  68,
     69,  39,  38,  70,  71,  53,  72,  73,  74,  65,  71,  72,
     75,  76,  77,  78,  64,  63,  54,  79,  80,  59,  39,  69,
     81,  82,  83,  84,  76,  85,  86,  87,  85,  48,  88,  89,
     90,  91,  92,  86,  93,  94,  47,  95,  88,  89,  81,  96,
     97,  84,  85,  98,  56,  55,  97,  99, 100, 101, 102, 100,
     68, 103, 104, 105, 106, 107,  46,  94,  93, 108, 109, 110,
     61,  60, 111, 112,  92,  91, 113, 114, 115,  92, 112, 116,
    117, 118, 114, 119, 120, 121, 122, 123, 124,  82,  81,  77,
    125, 126, 127, 125, 128, 129, 128, 130, 131, 132, 133, 134,
    135, 130, 128,  76,  84,  82, 136, 137, 138,  99, 139, 101,
    140, 141, 142, 143, 123, 122,  91,  90, 144, 115, 143, 145,
    120, 146, 147, 148, 149, 150, 116, 112, 136, 151, 149, 148,
    152, 153, 116, 154, 155, 149, 155, 156, 150, 157, 158, 129,
    159, 160, 155, 160, 161, 156, 162, 160, 159, 163, 161, 160,
    164, 162, 165, 166, 163, 162,  79,  54,  21, 167, 164, 168,
    111,  45, 169, 170, 171, 127, 164, 167, 172, 173, 144, 171,
    133, 174, 175, 176,  61, 110, 120, 119, 177, 178, 179, 107,
    104, 180,  51, 107, 181, 182,   2,  58,  53,  49, 183, 184,
    185, 186, 141, 184, 185, 133, 186, 187, 142,  72,  71,  70,
    146, 178, 182, 188, 189,  51, 121, 190, 184, 147,  67,  66,
     51, 180, 187, 186, 185, 184, 121, 132, 177, 188, 191, 147,
    187, 180, 142, 177, 179, 178, 192, 193, 194, 195,  30,  27,
    196, 140, 197, 105, 198, 199, 200, 201, 202, 192, 196, 203,
    197, 140, 202, 204, 118, 117, 198, 105, 205,   9,  45, 111,
    206, 207, 208, 209, 106, 199, 158, 157, 153,  94,  48, 176,
    210, 211,  57, 144,  90, 171, 126, 129, 161, 212, 213,  80,
     99,  97,  87, 214, 211, 215,  78, 216, 212,  52,   0,   2,
     17,   3,   5,  26,   6,   8,  28,   9,  11,  24,  12,  14,
      6,   5,  15,   6,  15,   7,  31,  17,  18,  25,  19,  21,
     34,  22,  24,   2,   1,  25,   6,  26,   5, 195,  27,  11,
    195,   3,  30,  34,  17,  22,  41,  10,  32,  14,  33,  24,
     13,  12,  36,  24,  23,  12,  39,  59,  58, 195,  11,   3,
      0,  30,  29,  39,  58,  40,   7,  35,   8,   0,  29,  33,
     15,   4,  11,   1,   0,  33,  15,  11,  10,   1,  33,  14,
     10,  41,  15,  19,   1,  14,  11,   4,   3,  19,  14,  13,
     36,  16,  41,  20,  19,  13,  36,  41,  20,  21,  20,  32,
     41,  16,  15,  36,  35,  16,  58,   2,  40,  37,  42,  12,
     44,  28,  43,   9,  28,  45,  94,  46,  48, 183,  49,  51,
     27,  52,  43,  34,  29,  17,  40,  25,  54,  55,  57,  38,
     29,   3,  17,  70,  53,  59,  61, 176,  89,  57, 217,  38,
     64, 169,  45,  43,  65,  44,  61,  89,  62,  40,  54,  38,
     64,  45,  44,  67, 182, 181, 217, 218, 214,  69, 217, 219,
     67, 181,  68,  71,  65,  43, 220,  74, 221,  69,  38, 217,
    217, 214, 219,  65,  74,  63,  71,  43,  53,  74,  73, 221,
    222,  75,  77, 223, 220, 221,  65,  72,  74,  74, 223,  63,
     78, 223, 216,  55,  54,  80,  59, 208,  70,  78,  63, 223,
    223, 221, 216,  96,  81,  83,  76,  75, 224,  59,  69, 208,
    208, 225,  70, 226,  93, 224, 227,  87, 109,  76, 224,  85,
     92, 113, 228,  93,  85, 224,  93,  86,  85,  87,  86, 109,
    176,  48,  89, 228, 145,  90, 229,  86,  94, 228,  90,  92,
     48,  47,  88,  88,  95, 230,  96, 102,  62,  88, 230,  81,
     96,  62,  89,  89,  88,  81,  87,  97,  85,  80, 213,  98,
    211,  56, 215, 211, 210,  56,  80,  98,  55,  83, 100,  96,
     82,  84,  97,  56,  98, 215,  82,  97,  83,  66,  68, 104,
     97, 100,  83, 100, 102,  96, 175, 174, 192, 105, 107, 205,
    106, 181, 107, 181, 106,  68, 192, 205, 175, 106, 209,  68,
    205, 107, 175, 226,  46,  93, 229, 110,  86,  61, 111, 110,
    110, 109,  86, 113,  92, 117, 137, 112,  91, 111, 108, 110,
    228, 113, 115, 137, 136, 112, 113, 117, 114, 190, 121,  49,
     92, 116, 117, 222,  77, 230, 191, 188, 120,  50,  49, 188,
    127, 171, 122,  49, 121, 188, 120, 188, 121, 122, 124, 127,
    124, 135, 125,  77,  81, 230, 126, 125, 129, 124, 125, 127,
    157, 128, 131, 132, 134, 177, 125, 135, 128,  77,  76,  82,
    134, 179, 177, 138, 231, 152, 100,  99, 101, 152, 136, 138,
    103,  68, 209, 140, 142, 202,  91, 144, 137, 141, 196, 174,
    209, 202, 103, 196, 192, 174, 202, 142, 103, 145, 143, 122,
    141, 140, 196, 228, 115, 145, 191, 120, 147, 144, 173, 137,
    232, 148, 150, 151, 154, 149, 152, 116, 136, 231, 138, 232,
    231, 232, 150, 149, 155, 150, 128, 157, 129, 154, 159, 155,
    155, 160, 156, 165, 162, 159, 162, 163, 160, 168, 164, 165,
    164, 166, 162,  32,  79,  21, 170, 173, 171,  80, 111, 169,
    166, 164, 172,  80,  79, 111, 134, 133, 175, 229, 176, 110,
    146, 120, 177, 179, 134, 175,  66, 104, 189, 178, 107, 182,
    179, 175, 107,  52,   2,  53, 104,  51, 189, 190,  49, 184,
    174, 133, 185, 132, 184, 133, 185, 141, 174, 141, 186, 142,
    225, 207, 206,  72, 225,  73, 146, 182, 147,  50, 188,  51,
     72,  70, 225, 225, 206,  73, 132, 121, 184, 182,  67, 147,
    189, 147,  66, 183,  51, 187, 187, 186, 183, 119, 121, 177,
    189, 188, 147, 186, 184, 183, 180, 104, 103, 146, 177, 178,
    205, 192, 194, 180, 103, 142,   0,  52,  30, 203, 196, 197,
     30,  52,  27, 106, 105, 199, 209, 200, 202, 193, 192, 203,
    201, 197, 202, 204, 117, 153, 194, 198, 205,   9, 111,  32,
    117, 116, 153, 206, 208, 219, 200, 209, 199, 111,  79,  32,
    157, 131, 204, 208,  69, 219, 229,  94, 176, 218,  57, 214,
    157, 204, 153,  90, 145, 122,  57, 211, 214, 172, 232, 138,
    138, 137, 173,  90, 122, 171, 127, 166, 170, 150, 153, 152,
    153, 156, 158, 231, 150, 152, 172, 138, 173, 212, 169,  78,
    173, 170, 172, 153, 150, 156, 170, 166, 172, 158, 156, 161,
    163, 166, 127, 129, 158, 161, 227,  99,  87, 163, 126, 161,
    163, 127, 126, 221,  73, 206, 169,  64,  78, 212,  80, 169,
    215, 216, 221, 227, 139,  99, 206, 219, 214,  98, 212, 215,
    215, 221, 206, 206, 214, 215, 212, 216, 215]

    def __init__(self):
        pass

    def makeTeapot(self):
        '''
        // Approach:  Each group of three values in teapotVertices
        // represents a vertex.  Indices into that array are in
        // teapotFaces.  For vertex N, the relevant entries in
        // teapotVertices are 3N+0, 3N+1, and 3N+2; that is,
        //
        //   vertex   0:  slots 0, 1, 2
        //   vertex   1:  slots 3, 4, 5
        //   ...
        //   vertex 232:  slots 696, 697, 698
        //
        // Iterate through teapotFaces in groups of three entries;
        // for each index, calculate the corresponding entry indices
        // into the teapotVertices array.
        '''

        for incr in range(0, len(self.teapotFaces)-2,3):
            point1 = 3 * self.teapotFaces[incr]
            point2 = 3 * self.teapotFaces[incr+1]
            point3 = 3 * self.teapotFaces[incr+2]

            self.addTriangle(self.teapotVertices[point1+0],
                             self.teapotVertices[point1 + 1] - 0.5,
                             self.teapotVertices[point1 + 2] - 1.0,
                             self.teapotVertices[point2 + 0],
                             self.teapotVertices[point2 + 1] - 0.5,
                             self.teapotVertices[point2 + 2] - 1.0,
                             self.teapotVertices[point3 + 0],
                             self.teapotVertices[point3 + 1] -0.5,
                             self.teapotVertices[point3 + 2] - 1.0)

