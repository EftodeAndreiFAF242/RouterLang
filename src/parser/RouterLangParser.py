# Generated from src/grammar/RouterLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,70,459,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,0,1,0,3,0,98,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,107,8,
        1,1,1,1,1,1,2,1,2,1,2,4,2,114,8,2,11,2,12,2,115,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,130,8,4,1,5,1,5,1,5,4,5,135,
        8,5,11,5,12,5,136,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,149,
        8,6,1,7,1,7,1,7,4,7,154,8,7,11,7,12,7,155,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,5,9,169,8,9,10,9,12,9,172,9,9,1,9,1,9,1,9,
        3,9,177,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,3,11,186,8,11,1,11,
        1,11,3,11,190,8,11,3,11,192,8,11,1,12,1,12,1,12,1,12,3,12,198,8,
        12,1,12,3,12,201,8,12,1,12,1,12,1,13,1,13,1,13,4,13,208,8,13,11,
        13,12,13,209,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,4,15,224,8,15,11,15,12,15,225,1,15,1,15,3,15,230,8,15,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,4,18,243,8,
        18,11,18,12,18,244,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,5,20,262,8,20,10,20,12,20,265,9,20,
        1,21,1,21,1,21,4,21,270,8,21,11,21,12,21,271,1,21,1,21,1,22,1,22,
        1,22,1,22,4,22,280,8,22,11,22,12,22,281,1,22,1,22,1,23,3,23,287,
        8,23,1,23,1,23,1,23,5,23,292,8,23,10,23,12,23,295,9,23,1,23,5,23,
        298,8,23,10,23,12,23,301,9,23,1,23,3,23,304,8,23,1,23,1,23,1,24,
        1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,333,
        8,27,1,28,1,28,1,28,3,28,338,8,28,1,29,1,29,1,29,1,30,1,30,1,30,
        1,30,1,30,1,30,3,30,349,8,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,3,33,363,8,33,1,34,1,34,1,35,1,35,1,35,
        4,35,370,8,35,11,35,12,35,371,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,391,8,36,
        1,37,1,37,3,37,395,8,37,1,37,3,37,398,8,37,1,37,3,37,401,8,37,1,
        38,1,38,1,38,1,38,1,38,1,38,3,38,409,8,38,1,39,1,39,1,39,4,39,414,
        8,39,11,39,12,39,415,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,5,43,435,8,43,10,43,12,43,
        438,9,43,3,43,440,8,43,1,44,1,44,3,44,444,8,44,1,45,1,45,1,45,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,0,0,46,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,
        2,1,0,26,27,1,0,44,46,457,0,92,1,0,0,0,2,101,1,0,0,0,4,110,1,0,0,
        0,6,119,1,0,0,0,8,126,1,0,0,0,10,131,1,0,0,0,12,140,1,0,0,0,14,150,
        1,0,0,0,16,159,1,0,0,0,18,176,1,0,0,0,20,178,1,0,0,0,22,191,1,0,
        0,0,24,193,1,0,0,0,26,204,1,0,0,0,28,213,1,0,0,0,30,229,1,0,0,0,
        32,231,1,0,0,0,34,235,1,0,0,0,36,239,1,0,0,0,38,248,1,0,0,0,40,258,
        1,0,0,0,42,266,1,0,0,0,44,275,1,0,0,0,46,286,1,0,0,0,48,307,1,0,
        0,0,50,311,1,0,0,0,52,313,1,0,0,0,54,332,1,0,0,0,56,334,1,0,0,0,
        58,339,1,0,0,0,60,348,1,0,0,0,62,350,1,0,0,0,64,353,1,0,0,0,66,362,
        1,0,0,0,68,364,1,0,0,0,70,366,1,0,0,0,72,390,1,0,0,0,74,392,1,0,
        0,0,76,402,1,0,0,0,78,410,1,0,0,0,80,417,1,0,0,0,82,421,1,0,0,0,
        84,425,1,0,0,0,86,439,1,0,0,0,88,441,1,0,0,0,90,445,1,0,0,0,92,93,
        3,2,1,0,93,94,3,20,10,0,94,95,3,42,21,0,95,97,3,70,35,0,96,98,3,
        90,45,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,0,0,1,
        100,1,1,0,0,0,101,102,5,1,0,0,102,103,5,2,0,0,103,104,3,4,2,0,104,
        106,3,10,5,0,105,107,3,14,7,0,106,105,1,0,0,0,106,107,1,0,0,0,107,
        108,1,0,0,0,108,109,5,3,0,0,109,3,1,0,0,0,110,111,5,4,0,0,111,113,
        5,2,0,0,112,114,3,6,3,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,
        1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,3,0,0,118,5,1,
        0,0,0,119,120,5,66,0,0,120,121,5,2,0,0,121,122,5,5,0,0,122,123,5,
        6,0,0,123,124,3,8,4,0,124,125,5,3,0,0,125,7,1,0,0,0,126,129,5,65,
        0,0,127,128,5,7,0,0,128,130,5,65,0,0,129,127,1,0,0,0,129,130,1,0,
        0,0,130,9,1,0,0,0,131,132,5,8,0,0,132,134,5,2,0,0,133,135,3,12,6,
        0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,
        0,137,138,1,0,0,0,138,139,5,3,0,0,139,11,1,0,0,0,140,141,5,66,0,
        0,141,142,5,9,0,0,142,148,5,66,0,0,143,144,5,2,0,0,144,145,5,10,
        0,0,145,146,5,6,0,0,146,147,5,65,0,0,147,149,5,3,0,0,148,143,1,0,
        0,0,148,149,1,0,0,0,149,13,1,0,0,0,150,151,5,11,0,0,151,153,5,2,
        0,0,152,154,3,16,8,0,153,152,1,0,0,0,154,155,1,0,0,0,155,153,1,0,
        0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,3,0,0,158,15,1,0,0,
        0,159,160,5,66,0,0,160,161,5,6,0,0,161,162,5,12,0,0,162,163,3,18,
        9,0,163,164,5,13,0,0,164,17,1,0,0,0,165,170,5,66,0,0,166,167,5,14,
        0,0,167,169,5,66,0,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,
        0,0,170,171,1,0,0,0,171,177,1,0,0,0,172,170,1,0,0,0,173,174,5,66,
        0,0,174,175,5,7,0,0,175,177,5,66,0,0,176,165,1,0,0,0,176,173,1,0,
        0,0,177,19,1,0,0,0,178,179,5,15,0,0,179,180,5,2,0,0,180,181,3,22,
        11,0,181,182,5,3,0,0,182,21,1,0,0,0,183,185,3,24,12,0,184,186,3,
        36,18,0,185,184,1,0,0,0,185,186,1,0,0,0,186,192,1,0,0,0,187,189,
        3,36,18,0,188,190,3,24,12,0,189,188,1,0,0,0,189,190,1,0,0,0,190,
        192,1,0,0,0,191,183,1,0,0,0,191,187,1,0,0,0,192,23,1,0,0,0,193,194,
        5,16,0,0,194,195,5,2,0,0,195,197,3,26,13,0,196,198,3,30,15,0,197,
        196,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,201,3,34,17,0,200,
        199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,5,3,0,0,203,
        25,1,0,0,0,204,205,5,17,0,0,205,207,5,2,0,0,206,208,3,28,14,0,207,
        206,1,0,0,0,208,209,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,
        211,1,0,0,0,211,212,5,3,0,0,212,27,1,0,0,0,213,214,5,66,0,0,214,
        215,5,6,0,0,215,216,5,65,0,0,216,29,1,0,0,0,217,218,5,18,0,0,218,
        219,5,6,0,0,219,230,5,19,0,0,220,221,5,18,0,0,221,223,5,2,0,0,222,
        224,3,32,16,0,223,222,1,0,0,0,224,225,1,0,0,0,225,223,1,0,0,0,225,
        226,1,0,0,0,226,227,1,0,0,0,227,228,5,3,0,0,228,230,1,0,0,0,229,
        217,1,0,0,0,229,220,1,0,0,0,230,31,1,0,0,0,231,232,5,66,0,0,232,
        233,5,6,0,0,233,234,5,63,0,0,234,33,1,0,0,0,235,236,5,20,0,0,236,
        237,5,6,0,0,237,238,5,66,0,0,238,35,1,0,0,0,239,240,5,21,0,0,240,
        242,5,2,0,0,241,243,3,38,19,0,242,241,1,0,0,0,243,244,1,0,0,0,244,
        242,1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,247,5,3,0,0,247,
        37,1,0,0,0,248,249,5,22,0,0,249,250,5,65,0,0,250,251,5,2,0,0,251,
        252,5,4,0,0,252,253,5,6,0,0,253,254,5,12,0,0,254,255,3,40,20,0,255,
        256,5,13,0,0,256,257,5,3,0,0,257,39,1,0,0,0,258,263,5,66,0,0,259,
        260,5,14,0,0,260,262,5,66,0,0,261,259,1,0,0,0,262,265,1,0,0,0,263,
        261,1,0,0,0,263,264,1,0,0,0,264,41,1,0,0,0,265,263,1,0,0,0,266,267,
        5,23,0,0,267,269,5,2,0,0,268,270,3,44,22,0,269,268,1,0,0,0,270,271,
        1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,273,1,0,0,0,273,274,
        5,3,0,0,274,43,1,0,0,0,275,276,5,24,0,0,276,277,5,66,0,0,277,279,
        5,2,0,0,278,280,3,46,23,0,279,278,1,0,0,0,280,281,1,0,0,0,281,279,
        1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,284,5,3,0,0,284,45,1,
        0,0,0,285,287,3,48,24,0,286,285,1,0,0,0,286,287,1,0,0,0,287,288,
        1,0,0,0,288,289,3,50,25,0,289,293,5,2,0,0,290,292,3,52,26,0,291,
        290,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,
        299,1,0,0,0,295,293,1,0,0,0,296,298,3,58,29,0,297,296,1,0,0,0,298,
        301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,303,1,0,0,0,301,
        299,1,0,0,0,302,304,3,62,31,0,303,302,1,0,0,0,303,304,1,0,0,0,304,
        305,1,0,0,0,305,306,5,3,0,0,306,47,1,0,0,0,307,308,5,25,0,0,308,
        309,5,65,0,0,309,310,5,6,0,0,310,49,1,0,0,0,311,312,7,0,0,0,312,
        51,1,0,0,0,313,314,5,28,0,0,314,315,3,54,27,0,315,53,1,0,0,0,316,
        317,5,29,0,0,317,333,3,56,28,0,318,319,5,30,0,0,319,333,5,67,0,0,
        320,321,5,31,0,0,321,333,5,67,0,0,322,323,5,32,0,0,323,324,5,33,
        0,0,324,325,5,66,0,0,325,326,5,34,0,0,326,327,5,35,0,0,327,328,5,
        36,0,0,328,329,5,33,0,0,329,330,5,66,0,0,330,333,5,34,0,0,331,333,
        5,37,0,0,332,316,1,0,0,0,332,318,1,0,0,0,332,320,1,0,0,0,332,322,
        1,0,0,0,332,331,1,0,0,0,333,55,1,0,0,0,334,337,5,64,0,0,335,336,
        5,38,0,0,336,338,5,65,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,57,
        1,0,0,0,339,340,5,39,0,0,340,341,3,60,30,0,341,59,1,0,0,0,342,343,
        5,62,0,0,343,349,5,65,0,0,344,345,5,40,0,0,345,349,5,65,0,0,346,
        347,5,31,0,0,347,349,5,67,0,0,348,342,1,0,0,0,348,344,1,0,0,0,348,
        346,1,0,0,0,349,61,1,0,0,0,350,351,5,41,0,0,351,352,3,64,32,0,352,
        63,1,0,0,0,353,354,5,66,0,0,354,355,5,42,0,0,355,356,5,66,0,0,356,
        357,5,43,0,0,357,358,3,66,33,0,358,65,1,0,0,0,359,363,3,68,34,0,
        360,363,5,65,0,0,361,363,5,67,0,0,362,359,1,0,0,0,362,360,1,0,0,
        0,362,361,1,0,0,0,363,67,1,0,0,0,364,365,7,1,0,0,365,69,1,0,0,0,
        366,367,5,47,0,0,367,369,5,2,0,0,368,370,3,72,36,0,369,368,1,0,0,
        0,370,371,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,373,1,0,0,
        0,373,374,5,3,0,0,374,71,1,0,0,0,375,376,5,66,0,0,376,377,5,6,0,
        0,377,378,5,48,0,0,378,379,5,66,0,0,379,380,5,2,0,0,380,381,3,74,
        37,0,381,382,5,3,0,0,382,391,1,0,0,0,383,384,5,66,0,0,384,385,5,
        6,0,0,385,386,5,49,0,0,386,387,5,2,0,0,387,388,3,88,44,0,388,389,
        5,3,0,0,389,391,1,0,0,0,390,375,1,0,0,0,390,383,1,0,0,0,391,73,1,
        0,0,0,392,394,3,76,38,0,393,395,3,80,40,0,394,393,1,0,0,0,394,395,
        1,0,0,0,395,397,1,0,0,0,396,398,3,82,41,0,397,396,1,0,0,0,397,398,
        1,0,0,0,398,400,1,0,0,0,399,401,3,84,42,0,400,399,1,0,0,0,400,401,
        1,0,0,0,401,75,1,0,0,0,402,403,5,50,0,0,403,404,5,6,0,0,404,408,
        3,78,39,0,405,406,5,51,0,0,406,407,5,6,0,0,407,409,3,78,39,0,408,
        405,1,0,0,0,408,409,1,0,0,0,409,77,1,0,0,0,410,413,5,66,0,0,411,
        412,5,52,0,0,412,414,5,66,0,0,413,411,1,0,0,0,414,415,1,0,0,0,415,
        413,1,0,0,0,415,416,1,0,0,0,416,79,1,0,0,0,417,418,5,53,0,0,418,
        419,5,6,0,0,419,420,5,66,0,0,420,81,1,0,0,0,421,422,5,54,0,0,422,
        423,5,6,0,0,423,424,5,65,0,0,424,83,1,0,0,0,425,426,5,55,0,0,426,
        427,5,6,0,0,427,428,3,86,43,0,428,85,1,0,0,0,429,440,5,60,0,0,430,
        440,5,61,0,0,431,436,5,66,0,0,432,433,5,14,0,0,433,435,5,66,0,0,
        434,432,1,0,0,0,435,438,1,0,0,0,436,434,1,0,0,0,436,437,1,0,0,0,
        437,440,1,0,0,0,438,436,1,0,0,0,439,429,1,0,0,0,439,430,1,0,0,0,
        439,431,1,0,0,0,440,87,1,0,0,0,441,443,3,80,40,0,442,444,3,84,42,
        0,443,442,1,0,0,0,443,444,1,0,0,0,444,89,1,0,0,0,445,446,5,56,0,
        0,446,447,5,2,0,0,447,448,5,57,0,0,448,449,5,6,0,0,449,450,5,66,
        0,0,450,451,5,58,0,0,451,452,5,6,0,0,452,453,5,66,0,0,453,454,5,
        59,0,0,454,455,5,6,0,0,455,456,5,66,0,0,456,457,5,3,0,0,457,91,1,
        0,0,0,39,97,106,115,129,136,148,155,170,176,185,189,191,197,200,
        209,225,229,244,263,271,281,286,293,299,303,332,337,348,362,371,
        390,394,397,400,408,415,436,439,443
    ]

class RouterLangParser ( Parser ):

    grammarFileName = "RouterLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'topology'", "'{'", "'}'", "'roles'", 
                     "'count'", "':'", "'..'", "'links'", "'--'", "'weight'", 
                     "'devices'", "'['", "']'", "','", "'routing'", "'bgp'", 
                     "'asn'", "'neighbors'", "'auto'", "'route-reflector'", 
                     "'ospf'", "'area'", "'policy'", "'define'", "'rank'", 
                     "'permit'", "'deny'", "'match'", "'prefix'", "'aspath'", 
                     "'community'", "'enter'", "'('", "')'", "'and'", "'exit'", 
                     "'any'", "'le'", "'set'", "'metric'", "'if'", "'.'", 
                     "'=='", "'LIVE'", "'DRAINED'", "'WARM'", "'intent'", 
                     "'route'", "'constraint'", "'primary'", "'backup'", 
                     "'>>'", "'apply-policy'", "'fault-tolerance'", "'scope'", 
                     "'transition'", "'from'", "'to'", "'intermediate'", 
                     "'all'", "'border'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "KW_ALL", "KW_BORDER", "KW_LOCAL_PREF", "IPv4_ADDR", 
                      "CIDR", "INT", "IDENT", "STRING", "WS", "LINE_CMT", 
                      "BLOCK_CMT" ]

    RULE_program = 0
    RULE_topoBlock = 1
    RULE_roleSection = 2
    RULE_roleDecl = 3
    RULE_intRange = 4
    RULE_linkSection = 5
    RULE_linkDecl = 6
    RULE_deviceSection = 7
    RULE_deviceBinding = 8
    RULE_deviceList = 9
    RULE_routingBlock = 10
    RULE_routingBody = 11
    RULE_bgpBlock = 12
    RULE_asnDecl = 13
    RULE_roleAsn = 14
    RULE_neighborDecl = 15
    RULE_peerEntry = 16
    RULE_rrDecl = 17
    RULE_ospfBlock = 18
    RULE_areaDecl = 19
    RULE_roleList = 20
    RULE_policyBlock = 21
    RULE_policyDef = 22
    RULE_policyStanza = 23
    RULE_rankClause = 24
    RULE_actionKw = 25
    RULE_matchClause = 26
    RULE_matchExpr = 27
    RULE_prefixExpr = 28
    RULE_setClause = 29
    RULE_setExpr = 30
    RULE_condClause = 31
    RULE_guardExpr = 32
    RULE_condVal = 33
    RULE_stateVal = 34
    RULE_intentBlock = 35
    RULE_intentDecl = 36
    RULE_routeBody = 37
    RULE_pathSpec = 38
    RULE_pathExpr = 39
    RULE_policyRef = 40
    RULE_ftSpec = 41
    RULE_scopeSpec = 42
    RULE_scopeVal = 43
    RULE_constraintBody = 44
    RULE_transitionBlock = 45

    ruleNames =  [ "program", "topoBlock", "roleSection", "roleDecl", "intRange", 
                   "linkSection", "linkDecl", "deviceSection", "deviceBinding", 
                   "deviceList", "routingBlock", "routingBody", "bgpBlock", 
                   "asnDecl", "roleAsn", "neighborDecl", "peerEntry", "rrDecl", 
                   "ospfBlock", "areaDecl", "roleList", "policyBlock", "policyDef", 
                   "policyStanza", "rankClause", "actionKw", "matchClause", 
                   "matchExpr", "prefixExpr", "setClause", "setExpr", "condClause", 
                   "guardExpr", "condVal", "stateVal", "intentBlock", "intentDecl", 
                   "routeBody", "pathSpec", "pathExpr", "policyRef", "ftSpec", 
                   "scopeSpec", "scopeVal", "constraintBody", "transitionBlock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    KW_ALL=60
    KW_BORDER=61
    KW_LOCAL_PREF=62
    IPv4_ADDR=63
    CIDR=64
    INT=65
    IDENT=66
    STRING=67
    WS=68
    LINE_CMT=69
    BLOCK_CMT=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topoBlock(self):
            return self.getTypedRuleContext(RouterLangParser.TopoBlockContext,0)


        def routingBlock(self):
            return self.getTypedRuleContext(RouterLangParser.RoutingBlockContext,0)


        def policyBlock(self):
            return self.getTypedRuleContext(RouterLangParser.PolicyBlockContext,0)


        def intentBlock(self):
            return self.getTypedRuleContext(RouterLangParser.IntentBlockContext,0)


        def EOF(self):
            return self.getToken(RouterLangParser.EOF, 0)

        def transitionBlock(self):
            return self.getTypedRuleContext(RouterLangParser.TransitionBlockContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RouterLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.topoBlock()
            self.state = 93
            self.routingBlock()
            self.state = 94
            self.policyBlock()
            self.state = 95
            self.intentBlock()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 96
                self.transitionBlock()


            self.state = 99
            self.match(RouterLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopoBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roleSection(self):
            return self.getTypedRuleContext(RouterLangParser.RoleSectionContext,0)


        def linkSection(self):
            return self.getTypedRuleContext(RouterLangParser.LinkSectionContext,0)


        def deviceSection(self):
            return self.getTypedRuleContext(RouterLangParser.DeviceSectionContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_topoBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopoBlock" ):
                listener.enterTopoBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopoBlock" ):
                listener.exitTopoBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopoBlock" ):
                return visitor.visitTopoBlock(self)
            else:
                return visitor.visitChildren(self)




    def topoBlock(self):

        localctx = RouterLangParser.TopoBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topoBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(RouterLangParser.T__0)
            self.state = 102
            self.match(RouterLangParser.T__1)
            self.state = 103
            self.roleSection()
            self.state = 104
            self.linkSection()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 105
                self.deviceSection()


            self.state = 108
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roleDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.RoleDeclContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.RoleDeclContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_roleSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleSection" ):
                listener.enterRoleSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleSection" ):
                listener.exitRoleSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoleSection" ):
                return visitor.visitRoleSection(self)
            else:
                return visitor.visitChildren(self)




    def roleSection(self):

        localctx = RouterLangParser.RoleSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_roleSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(RouterLangParser.T__3)
            self.state = 111
            self.match(RouterLangParser.T__1)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.roleDecl()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==66):
                    break

            self.state = 117
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def intRange(self):
            return self.getTypedRuleContext(RouterLangParser.IntRangeContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_roleDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleDecl" ):
                listener.enterRoleDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleDecl" ):
                listener.exitRoleDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoleDecl" ):
                return visitor.visitRoleDecl(self)
            else:
                return visitor.visitChildren(self)




    def roleDecl(self):

        localctx = RouterLangParser.RoleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_roleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(RouterLangParser.IDENT)
            self.state = 120
            self.match(RouterLangParser.T__1)
            self.state = 121
            self.match(RouterLangParser.T__4)
            self.state = 122
            self.match(RouterLangParser.T__5)
            self.state = 123
            self.intRange()
            self.state = 124
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.INT)
            else:
                return self.getToken(RouterLangParser.INT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_intRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntRange" ):
                listener.enterIntRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntRange" ):
                listener.exitIntRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntRange" ):
                return visitor.visitIntRange(self)
            else:
                return visitor.visitChildren(self)




    def intRange(self):

        localctx = RouterLangParser.IntRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_intRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(RouterLangParser.INT)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 127
                self.match(RouterLangParser.T__6)
                self.state = 128
                self.match(RouterLangParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linkDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.LinkDeclContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.LinkDeclContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_linkSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkSection" ):
                listener.enterLinkSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkSection" ):
                listener.exitLinkSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkSection" ):
                return visitor.visitLinkSection(self)
            else:
                return visitor.visitChildren(self)




    def linkSection(self):

        localctx = RouterLangParser.LinkSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_linkSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(RouterLangParser.T__7)
            self.state = 132
            self.match(RouterLangParser.T__1)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.linkDecl()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==66):
                    break

            self.state = 138
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_linkDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkDecl" ):
                listener.enterLinkDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkDecl" ):
                listener.exitLinkDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkDecl" ):
                return visitor.visitLinkDecl(self)
            else:
                return visitor.visitChildren(self)




    def linkDecl(self):

        localctx = RouterLangParser.LinkDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_linkDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(RouterLangParser.IDENT)
            self.state = 141
            self.match(RouterLangParser.T__8)
            self.state = 142
            self.match(RouterLangParser.IDENT)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 143
                self.match(RouterLangParser.T__1)
                self.state = 144
                self.match(RouterLangParser.T__9)
                self.state = 145
                self.match(RouterLangParser.T__5)
                self.state = 146
                self.match(RouterLangParser.INT)
                self.state = 147
                self.match(RouterLangParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deviceBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.DeviceBindingContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.DeviceBindingContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_deviceSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceSection" ):
                listener.enterDeviceSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceSection" ):
                listener.exitDeviceSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeviceSection" ):
                return visitor.visitDeviceSection(self)
            else:
                return visitor.visitChildren(self)




    def deviceSection(self):

        localctx = RouterLangParser.DeviceSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_deviceSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(RouterLangParser.T__10)
            self.state = 151
            self.match(RouterLangParser.T__1)
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.deviceBinding()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==66):
                    break

            self.state = 157
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceBindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def deviceList(self):
            return self.getTypedRuleContext(RouterLangParser.DeviceListContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_deviceBinding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceBinding" ):
                listener.enterDeviceBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceBinding" ):
                listener.exitDeviceBinding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeviceBinding" ):
                return visitor.visitDeviceBinding(self)
            else:
                return visitor.visitChildren(self)




    def deviceBinding(self):

        localctx = RouterLangParser.DeviceBindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_deviceBinding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(RouterLangParser.IDENT)
            self.state = 160
            self.match(RouterLangParser.T__5)
            self.state = 161
            self.match(RouterLangParser.T__11)
            self.state = 162
            self.deviceList()
            self.state = 163
            self.match(RouterLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_deviceList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeviceList" ):
                listener.enterDeviceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeviceList" ):
                listener.exitDeviceList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeviceList" ):
                return visitor.visitDeviceList(self)
            else:
                return visitor.visitChildren(self)




    def deviceList(self):

        localctx = RouterLangParser.DeviceListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_deviceList)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(RouterLangParser.IDENT)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 166
                    self.match(RouterLangParser.T__13)
                    self.state = 167
                    self.match(RouterLangParser.IDENT)
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(RouterLangParser.IDENT)
                self.state = 174
                self.match(RouterLangParser.T__6)
                self.state = 175
                self.match(RouterLangParser.IDENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoutingBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def routingBody(self):
            return self.getTypedRuleContext(RouterLangParser.RoutingBodyContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_routingBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoutingBlock" ):
                listener.enterRoutingBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoutingBlock" ):
                listener.exitRoutingBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoutingBlock" ):
                return visitor.visitRoutingBlock(self)
            else:
                return visitor.visitChildren(self)




    def routingBlock(self):

        localctx = RouterLangParser.RoutingBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_routingBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(RouterLangParser.T__14)
            self.state = 179
            self.match(RouterLangParser.T__1)
            self.state = 180
            self.routingBody()
            self.state = 181
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoutingBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bgpBlock(self):
            return self.getTypedRuleContext(RouterLangParser.BgpBlockContext,0)


        def ospfBlock(self):
            return self.getTypedRuleContext(RouterLangParser.OspfBlockContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_routingBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoutingBody" ):
                listener.enterRoutingBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoutingBody" ):
                listener.exitRoutingBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoutingBody" ):
                return visitor.visitRoutingBody(self)
            else:
                return visitor.visitChildren(self)




    def routingBody(self):

        localctx = RouterLangParser.RoutingBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_routingBody)
        self._la = 0 # Token type
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.bgpBlock()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 184
                    self.ospfBlock()


                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.ospfBlock()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 188
                    self.bgpBlock()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BgpBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asnDecl(self):
            return self.getTypedRuleContext(RouterLangParser.AsnDeclContext,0)


        def neighborDecl(self):
            return self.getTypedRuleContext(RouterLangParser.NeighborDeclContext,0)


        def rrDecl(self):
            return self.getTypedRuleContext(RouterLangParser.RrDeclContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_bgpBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBgpBlock" ):
                listener.enterBgpBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBgpBlock" ):
                listener.exitBgpBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBgpBlock" ):
                return visitor.visitBgpBlock(self)
            else:
                return visitor.visitChildren(self)




    def bgpBlock(self):

        localctx = RouterLangParser.BgpBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bgpBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(RouterLangParser.T__15)
            self.state = 194
            self.match(RouterLangParser.T__1)
            self.state = 195
            self.asnDecl()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 196
                self.neighborDecl()


            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 199
                self.rrDecl()


            self.state = 202
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsnDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roleAsn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.RoleAsnContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.RoleAsnContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_asnDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsnDecl" ):
                listener.enterAsnDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsnDecl" ):
                listener.exitAsnDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsnDecl" ):
                return visitor.visitAsnDecl(self)
            else:
                return visitor.visitChildren(self)




    def asnDecl(self):

        localctx = RouterLangParser.AsnDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_asnDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(RouterLangParser.T__16)
            self.state = 205
            self.match(RouterLangParser.T__1)
            self.state = 207 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.roleAsn()
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==66):
                    break

            self.state = 211
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleAsnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_roleAsn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleAsn" ):
                listener.enterRoleAsn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleAsn" ):
                listener.exitRoleAsn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoleAsn" ):
                return visitor.visitRoleAsn(self)
            else:
                return visitor.visitChildren(self)




    def roleAsn(self):

        localctx = RouterLangParser.RoleAsnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_roleAsn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(RouterLangParser.IDENT)
            self.state = 214
            self.match(RouterLangParser.T__5)
            self.state = 215
            self.match(RouterLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NeighborDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def peerEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.PeerEntryContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.PeerEntryContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_neighborDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeighborDecl" ):
                listener.enterNeighborDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeighborDecl" ):
                listener.exitNeighborDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeighborDecl" ):
                return visitor.visitNeighborDecl(self)
            else:
                return visitor.visitChildren(self)




    def neighborDecl(self):

        localctx = RouterLangParser.NeighborDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_neighborDecl)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(RouterLangParser.T__17)
                self.state = 218
                self.match(RouterLangParser.T__5)
                self.state = 219
                self.match(RouterLangParser.T__18)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(RouterLangParser.T__17)
                self.state = 221
                self.match(RouterLangParser.T__1)
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 222
                    self.peerEntry()
                    self.state = 225 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==66):
                        break

                self.state = 227
                self.match(RouterLangParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeerEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def IPv4_ADDR(self):
            return self.getToken(RouterLangParser.IPv4_ADDR, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_peerEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeerEntry" ):
                listener.enterPeerEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeerEntry" ):
                listener.exitPeerEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeerEntry" ):
                return visitor.visitPeerEntry(self)
            else:
                return visitor.visitChildren(self)




    def peerEntry(self):

        localctx = RouterLangParser.PeerEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_peerEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(RouterLangParser.IDENT)
            self.state = 232
            self.match(RouterLangParser.T__5)
            self.state = 233
            self.match(RouterLangParser.IPv4_ADDR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_rrDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRrDecl" ):
                listener.enterRrDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRrDecl" ):
                listener.exitRrDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRrDecl" ):
                return visitor.visitRrDecl(self)
            else:
                return visitor.visitChildren(self)




    def rrDecl(self):

        localctx = RouterLangParser.RrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_rrDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(RouterLangParser.T__19)
            self.state = 236
            self.match(RouterLangParser.T__5)
            self.state = 237
            self.match(RouterLangParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OspfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def areaDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.AreaDeclContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.AreaDeclContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_ospfBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOspfBlock" ):
                listener.enterOspfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOspfBlock" ):
                listener.exitOspfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOspfBlock" ):
                return visitor.visitOspfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ospfBlock(self):

        localctx = RouterLangParser.OspfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ospfBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RouterLangParser.T__20)
            self.state = 240
            self.match(RouterLangParser.T__1)
            self.state = 242 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 241
                self.areaDecl()
                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 246
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AreaDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def roleList(self):
            return self.getTypedRuleContext(RouterLangParser.RoleListContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_areaDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAreaDecl" ):
                listener.enterAreaDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAreaDecl" ):
                listener.exitAreaDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAreaDecl" ):
                return visitor.visitAreaDecl(self)
            else:
                return visitor.visitChildren(self)




    def areaDecl(self):

        localctx = RouterLangParser.AreaDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_areaDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(RouterLangParser.T__21)
            self.state = 249
            self.match(RouterLangParser.INT)
            self.state = 250
            self.match(RouterLangParser.T__1)
            self.state = 251
            self.match(RouterLangParser.T__3)
            self.state = 252
            self.match(RouterLangParser.T__5)
            self.state = 253
            self.match(RouterLangParser.T__11)
            self.state = 254
            self.roleList()
            self.state = 255
            self.match(RouterLangParser.T__12)
            self.state = 256
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_roleList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleList" ):
                listener.enterRoleList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleList" ):
                listener.exitRoleList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoleList" ):
                return visitor.visitRoleList(self)
            else:
                return visitor.visitChildren(self)




    def roleList(self):

        localctx = RouterLangParser.RoleListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_roleList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(RouterLangParser.IDENT)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 259
                self.match(RouterLangParser.T__13)
                self.state = 260
                self.match(RouterLangParser.IDENT)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def policyDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.PolicyDefContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.PolicyDefContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_policyBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicyBlock" ):
                listener.enterPolicyBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicyBlock" ):
                listener.exitPolicyBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicyBlock" ):
                return visitor.visitPolicyBlock(self)
            else:
                return visitor.visitChildren(self)




    def policyBlock(self):

        localctx = RouterLangParser.PolicyBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_policyBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(RouterLangParser.T__22)
            self.state = 267
            self.match(RouterLangParser.T__1)
            self.state = 269 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 268
                self.policyDef()
                self.state = 271 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 273
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def policyStanza(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.PolicyStanzaContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.PolicyStanzaContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_policyDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicyDef" ):
                listener.enterPolicyDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicyDef" ):
                listener.exitPolicyDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicyDef" ):
                return visitor.visitPolicyDef(self)
            else:
                return visitor.visitChildren(self)




    def policyDef(self):

        localctx = RouterLangParser.PolicyDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_policyDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(RouterLangParser.T__23)
            self.state = 276
            self.match(RouterLangParser.IDENT)
            self.state = 277
            self.match(RouterLangParser.T__1)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.policyStanza()
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    break

            self.state = 283
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyStanzaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionKw(self):
            return self.getTypedRuleContext(RouterLangParser.ActionKwContext,0)


        def rankClause(self):
            return self.getTypedRuleContext(RouterLangParser.RankClauseContext,0)


        def matchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.MatchClauseContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.MatchClauseContext,i)


        def setClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.SetClauseContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.SetClauseContext,i)


        def condClause(self):
            return self.getTypedRuleContext(RouterLangParser.CondClauseContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_policyStanza

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicyStanza" ):
                listener.enterPolicyStanza(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicyStanza" ):
                listener.exitPolicyStanza(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicyStanza" ):
                return visitor.visitPolicyStanza(self)
            else:
                return visitor.visitChildren(self)




    def policyStanza(self):

        localctx = RouterLangParser.PolicyStanzaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_policyStanza)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 285
                self.rankClause()


            self.state = 288
            self.actionKw()
            self.state = 289
            self.match(RouterLangParser.T__1)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 290
                self.matchClause()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 296
                self.setClause()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 302
                self.condClause()


            self.state = 305
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RankClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_rankClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRankClause" ):
                listener.enterRankClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRankClause" ):
                listener.exitRankClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRankClause" ):
                return visitor.visitRankClause(self)
            else:
                return visitor.visitChildren(self)




    def rankClause(self):

        localctx = RouterLangParser.RankClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_rankClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(RouterLangParser.T__24)
            self.state = 308
            self.match(RouterLangParser.INT)
            self.state = 309
            self.match(RouterLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionKwContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RouterLangParser.RULE_actionKw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionKw" ):
                listener.enterActionKw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionKw" ):
                listener.exitActionKw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionKw" ):
                return visitor.visitActionKw(self)
            else:
                return visitor.visitChildren(self)




    def actionKw(self):

        localctx = RouterLangParser.ActionKwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_actionKw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matchExpr(self):
            return self.getTypedRuleContext(RouterLangParser.MatchExprContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_matchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchClause" ):
                listener.enterMatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchClause" ):
                listener.exitMatchClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchClause" ):
                return visitor.visitMatchClause(self)
            else:
                return visitor.visitChildren(self)




    def matchClause(self):

        localctx = RouterLangParser.MatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_matchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(RouterLangParser.T__27)
            self.state = 314
            self.matchExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefixExpr(self):
            return self.getTypedRuleContext(RouterLangParser.PrefixExprContext,0)


        def STRING(self):
            return self.getToken(RouterLangParser.STRING, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_matchExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchExpr" ):
                listener.enterMatchExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchExpr" ):
                listener.exitMatchExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpr" ):
                return visitor.visitMatchExpr(self)
            else:
                return visitor.visitChildren(self)




    def matchExpr(self):

        localctx = RouterLangParser.MatchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_matchExpr)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(RouterLangParser.T__28)
                self.state = 317
                self.prefixExpr()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(RouterLangParser.T__29)
                self.state = 319
                self.match(RouterLangParser.STRING)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(RouterLangParser.T__30)
                self.state = 321
                self.match(RouterLangParser.STRING)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.match(RouterLangParser.T__31)
                self.state = 323
                self.match(RouterLangParser.T__32)
                self.state = 324
                self.match(RouterLangParser.IDENT)
                self.state = 325
                self.match(RouterLangParser.T__33)
                self.state = 326
                self.match(RouterLangParser.T__34)
                self.state = 327
                self.match(RouterLangParser.T__35)
                self.state = 328
                self.match(RouterLangParser.T__32)
                self.state = 329
                self.match(RouterLangParser.IDENT)
                self.state = 330
                self.match(RouterLangParser.T__33)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 331
                self.match(RouterLangParser.T__36)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIDR(self):
            return self.getToken(RouterLangParser.CIDR, 0)

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_prefixExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixExpr" ):
                listener.enterPrefixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixExpr" ):
                listener.exitPrefixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixExpr" ):
                return visitor.visitPrefixExpr(self)
            else:
                return visitor.visitChildren(self)




    def prefixExpr(self):

        localctx = RouterLangParser.PrefixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_prefixExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(RouterLangParser.CIDR)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 335
                self.match(RouterLangParser.T__37)
                self.state = 336
                self.match(RouterLangParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setExpr(self):
            return self.getTypedRuleContext(RouterLangParser.SetExprContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_setClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetClause" ):
                listener.enterSetClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetClause" ):
                listener.exitSetClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetClause" ):
                return visitor.visitSetClause(self)
            else:
                return visitor.visitChildren(self)




    def setClause(self):

        localctx = RouterLangParser.SetClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_setClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(RouterLangParser.T__38)
            self.state = 340
            self.setExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LOCAL_PREF(self):
            return self.getToken(RouterLangParser.KW_LOCAL_PREF, 0)

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def STRING(self):
            return self.getToken(RouterLangParser.STRING, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_setExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetExpr" ):
                listener.enterSetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetExpr" ):
                listener.exitSetExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetExpr" ):
                return visitor.visitSetExpr(self)
            else:
                return visitor.visitChildren(self)




    def setExpr(self):

        localctx = RouterLangParser.SetExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_setExpr)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(RouterLangParser.KW_LOCAL_PREF)
                self.state = 343
                self.match(RouterLangParser.INT)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(RouterLangParser.T__39)
                self.state = 345
                self.match(RouterLangParser.INT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.match(RouterLangParser.T__30)
                self.state = 347
                self.match(RouterLangParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def guardExpr(self):
            return self.getTypedRuleContext(RouterLangParser.GuardExprContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_condClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondClause" ):
                listener.enterCondClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondClause" ):
                listener.exitCondClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondClause" ):
                return visitor.visitCondClause(self)
            else:
                return visitor.visitChildren(self)




    def condClause(self):

        localctx = RouterLangParser.CondClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_condClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(RouterLangParser.T__40)
            self.state = 351
            self.guardExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuardExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def condVal(self):
            return self.getTypedRuleContext(RouterLangParser.CondValContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_guardExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuardExpr" ):
                listener.enterGuardExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuardExpr" ):
                listener.exitGuardExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuardExpr" ):
                return visitor.visitGuardExpr(self)
            else:
                return visitor.visitChildren(self)




    def guardExpr(self):

        localctx = RouterLangParser.GuardExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_guardExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(RouterLangParser.IDENT)
            self.state = 354
            self.match(RouterLangParser.T__41)
            self.state = 355
            self.match(RouterLangParser.IDENT)
            self.state = 356
            self.match(RouterLangParser.T__42)
            self.state = 357
            self.condVal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateVal(self):
            return self.getTypedRuleContext(RouterLangParser.StateValContext,0)


        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def STRING(self):
            return self.getToken(RouterLangParser.STRING, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_condVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondVal" ):
                listener.enterCondVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondVal" ):
                listener.exitCondVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondVal" ):
                return visitor.visitCondVal(self)
            else:
                return visitor.visitChildren(self)




    def condVal(self):

        localctx = RouterLangParser.CondValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_condVal)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.stateVal()
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(RouterLangParser.INT)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(RouterLangParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RouterLangParser.RULE_stateVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateVal" ):
                listener.enterStateVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateVal" ):
                listener.exitStateVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateVal" ):
                return visitor.visitStateVal(self)
            else:
                return visitor.visitChildren(self)




    def stateVal(self):

        localctx = RouterLangParser.StateValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stateVal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntentBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intentDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.IntentDeclContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.IntentDeclContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_intentBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntentBlock" ):
                listener.enterIntentBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntentBlock" ):
                listener.exitIntentBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntentBlock" ):
                return visitor.visitIntentBlock(self)
            else:
                return visitor.visitChildren(self)




    def intentBlock(self):

        localctx = RouterLangParser.IntentBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_intentBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(RouterLangParser.T__46)
            self.state = 367
            self.match(RouterLangParser.T__1)
            self.state = 369 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 368
                self.intentDecl()
                self.state = 371 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==66):
                    break

            self.state = 373
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntentDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def routeBody(self):
            return self.getTypedRuleContext(RouterLangParser.RouteBodyContext,0)


        def constraintBody(self):
            return self.getTypedRuleContext(RouterLangParser.ConstraintBodyContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_intentDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntentDecl" ):
                listener.enterIntentDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntentDecl" ):
                listener.exitIntentDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntentDecl" ):
                return visitor.visitIntentDecl(self)
            else:
                return visitor.visitChildren(self)




    def intentDecl(self):

        localctx = RouterLangParser.IntentDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_intentDecl)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(RouterLangParser.IDENT)
                self.state = 376
                self.match(RouterLangParser.T__5)
                self.state = 377
                self.match(RouterLangParser.T__47)
                self.state = 378
                self.match(RouterLangParser.IDENT)
                self.state = 379
                self.match(RouterLangParser.T__1)
                self.state = 380
                self.routeBody()
                self.state = 381
                self.match(RouterLangParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(RouterLangParser.IDENT)
                self.state = 384
                self.match(RouterLangParser.T__5)
                self.state = 385
                self.match(RouterLangParser.T__48)
                self.state = 386
                self.match(RouterLangParser.T__1)
                self.state = 387
                self.constraintBody()
                self.state = 388
                self.match(RouterLangParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RouteBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathSpec(self):
            return self.getTypedRuleContext(RouterLangParser.PathSpecContext,0)


        def policyRef(self):
            return self.getTypedRuleContext(RouterLangParser.PolicyRefContext,0)


        def ftSpec(self):
            return self.getTypedRuleContext(RouterLangParser.FtSpecContext,0)


        def scopeSpec(self):
            return self.getTypedRuleContext(RouterLangParser.ScopeSpecContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_routeBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRouteBody" ):
                listener.enterRouteBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRouteBody" ):
                listener.exitRouteBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRouteBody" ):
                return visitor.visitRouteBody(self)
            else:
                return visitor.visitChildren(self)




    def routeBody(self):

        localctx = RouterLangParser.RouteBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_routeBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.pathSpec()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 393
                self.policyRef()


            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 396
                self.ftSpec()


            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 399
                self.scopeSpec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RouterLangParser.PathExprContext)
            else:
                return self.getTypedRuleContext(RouterLangParser.PathExprContext,i)


        def getRuleIndex(self):
            return RouterLangParser.RULE_pathSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathSpec" ):
                listener.enterPathSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathSpec" ):
                listener.exitPathSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathSpec" ):
                return visitor.visitPathSpec(self)
            else:
                return visitor.visitChildren(self)




    def pathSpec(self):

        localctx = RouterLangParser.PathSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_pathSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(RouterLangParser.T__49)
            self.state = 403
            self.match(RouterLangParser.T__5)
            self.state = 404
            self.pathExpr()
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 405
                self.match(RouterLangParser.T__50)
                self.state = 406
                self.match(RouterLangParser.T__5)
                self.state = 407
                self.pathExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_pathExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathExpr" ):
                listener.enterPathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathExpr" ):
                listener.exitPathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathExpr" ):
                return visitor.visitPathExpr(self)
            else:
                return visitor.visitChildren(self)




    def pathExpr(self):

        localctx = RouterLangParser.PathExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_pathExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(RouterLangParser.IDENT)
            self.state = 413 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 411
                self.match(RouterLangParser.T__51)
                self.state = 412
                self.match(RouterLangParser.IDENT)
                self.state = 415 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==52):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(RouterLangParser.IDENT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_policyRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicyRef" ):
                listener.enterPolicyRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicyRef" ):
                listener.exitPolicyRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicyRef" ):
                return visitor.visitPolicyRef(self)
            else:
                return visitor.visitChildren(self)




    def policyRef(self):

        localctx = RouterLangParser.PolicyRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_policyRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(RouterLangParser.T__52)
            self.state = 418
            self.match(RouterLangParser.T__5)
            self.state = 419
            self.match(RouterLangParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FtSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RouterLangParser.INT, 0)

        def getRuleIndex(self):
            return RouterLangParser.RULE_ftSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFtSpec" ):
                listener.enterFtSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFtSpec" ):
                listener.exitFtSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFtSpec" ):
                return visitor.visitFtSpec(self)
            else:
                return visitor.visitChildren(self)




    def ftSpec(self):

        localctx = RouterLangParser.FtSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ftSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(RouterLangParser.T__53)
            self.state = 422
            self.match(RouterLangParser.T__5)
            self.state = 423
            self.match(RouterLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scopeVal(self):
            return self.getTypedRuleContext(RouterLangParser.ScopeValContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_scopeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopeSpec" ):
                listener.enterScopeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopeSpec" ):
                listener.exitScopeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScopeSpec" ):
                return visitor.visitScopeSpec(self)
            else:
                return visitor.visitChildren(self)




    def scopeSpec(self):

        localctx = RouterLangParser.ScopeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_scopeSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(RouterLangParser.T__54)
            self.state = 426
            self.match(RouterLangParser.T__5)
            self.state = 427
            self.scopeVal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ALL(self):
            return self.getToken(RouterLangParser.KW_ALL, 0)

        def KW_BORDER(self):
            return self.getToken(RouterLangParser.KW_BORDER, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_scopeVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopeVal" ):
                listener.enterScopeVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopeVal" ):
                listener.exitScopeVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScopeVal" ):
                return visitor.visitScopeVal(self)
            else:
                return visitor.visitChildren(self)




    def scopeVal(self):

        localctx = RouterLangParser.ScopeValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_scopeVal)
        self._la = 0 # Token type
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(RouterLangParser.KW_ALL)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(RouterLangParser.KW_BORDER)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(RouterLangParser.IDENT)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 432
                    self.match(RouterLangParser.T__13)
                    self.state = 433
                    self.match(RouterLangParser.IDENT)
                    self.state = 438
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def policyRef(self):
            return self.getTypedRuleContext(RouterLangParser.PolicyRefContext,0)


        def scopeSpec(self):
            return self.getTypedRuleContext(RouterLangParser.ScopeSpecContext,0)


        def getRuleIndex(self):
            return RouterLangParser.RULE_constraintBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintBody" ):
                listener.enterConstraintBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintBody" ):
                listener.exitConstraintBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintBody" ):
                return visitor.visitConstraintBody(self)
            else:
                return visitor.visitChildren(self)




    def constraintBody(self):

        localctx = RouterLangParser.ConstraintBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_constraintBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.policyRef()
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 442
                self.scopeSpec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RouterLangParser.IDENT)
            else:
                return self.getToken(RouterLangParser.IDENT, i)

        def getRuleIndex(self):
            return RouterLangParser.RULE_transitionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitionBlock" ):
                listener.enterTransitionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitionBlock" ):
                listener.exitTransitionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransitionBlock" ):
                return visitor.visitTransitionBlock(self)
            else:
                return visitor.visitChildren(self)




    def transitionBlock(self):

        localctx = RouterLangParser.TransitionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_transitionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(RouterLangParser.T__55)
            self.state = 446
            self.match(RouterLangParser.T__1)
            self.state = 447
            self.match(RouterLangParser.T__56)
            self.state = 448
            self.match(RouterLangParser.T__5)
            self.state = 449
            self.match(RouterLangParser.IDENT)
            self.state = 450
            self.match(RouterLangParser.T__57)
            self.state = 451
            self.match(RouterLangParser.T__5)
            self.state = 452
            self.match(RouterLangParser.IDENT)
            self.state = 453
            self.match(RouterLangParser.T__58)
            self.state = 454
            self.match(RouterLangParser.T__5)
            self.state = 455
            self.match(RouterLangParser.IDENT)
            self.state = 456
            self.match(RouterLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





