C Start of script
C Reasonable overflow temperature Fortran 2018 library
C This library handles overflows for temperature counters, so that they don't become completely unreasonable

C This script is highly incomplete
C integer absoluteHotInt :: ! Not yet calculated
integer absoluteColdInt_Cel :: -3000
integer absoluteColdInt_Fah :: -5368

C Current issues:
C I am really bad at Fortran, and I wasn't able to convert most Python data here. The parts that are commented out need to be rewritten for Fortran
C I don't know how the program will link to this library and detect an overflow
C Temperatures in Fahrenheit, Celsius, Kelvin, and Rankine need to be accounted for
C An exact value for absolute hot and absolute cold has not been defined. It is still a question in science. Estimates are sorted by year
C My research on this is a bit shotty, and needs correction. I feel like I made several errors here
C Absolute hot is not fully documented, and needs calculations and assignments

C Some notes:
C Absolute hot is a theoretical max temperature
C Absolute cold is not completely exact yet, as new discoveries are being made, finding colder and colder temperatures, and pushing the science further

integer overflowCounter1Int :: 0
C overflowCounter1Float = float(0) # Capture here upon detection of overflow
C testInt_x16 = int(65536) # 16 bit integer for testing
C testInt_x32 = int(42949672964294967296) # 32 bit integer for testing, calculation error?
C testInt_x64 = int(18446744073709551615) # 64 bit integer for testing, calculation error?
C absoluteHotFloat = float(2.55*10^32) # Needs to be calculated
C integer absoluteHotInt :: int(2.55*10^32) ! Needs to be calculated
C As of 1740 CE
C absoluteZero1740Float_Fah = float(-400.00) # As of 1740 CE
C absoluteZero1740Float_Cel = float(-240.00) # As of 1740 CE
C absoluteZero1740Int_Fah = int(-400) # As of 1740 CE
C absoluteZero1740Int_Cel = int(-240) # As of 1740 CE
C Rankine
C Kelvin
C As of 1779 CE
C absoluteZero1779Float_Fah = float(-454.00) # As of 1779 CE
C absoluteZero1779Float_Cel = float(-270.00) # As of 1779 CE
C absoluteZero1779Int_Fah = int(-454) # As of 1779 CE
C absoluteZero1779Int_Cel = int(-270) # As of 1779 CE
C Rankine
C Kelvin
C I divided 1780 into 2 quarters, as the source I am using (John Dalton >-> Wikipedia) defines the first calc as 1500 and the final as 3000, both in 1780.
C As of 1780 CE Q1
C absoluteZero1780Q1Float_Fah = float(-2668.00) # As of 1780 CE Quarter 1
C absoluteZero1780Q1Float_Cel = float(-1500.00) # As of 1780 CE Quarter 1
C absoluteZero1780Q1Int_Fah = int(-2668) # As of 1780 CE Quarter 1
C absoluteZero1780Q1Int_Cel = int(-1500) # As of 1780 CE Quarter 1
C As of 1780 CE Q2
C absoluteZero1780Q2Float_Fah = float(-5368.00) # As of 1780 CE Quarter 2
C absoluteZero1780Q2Float_Cel = float(-3000.00) # As of 1780 CE Quarter 2
C absoluteZero1780Q2Int_Fah = int(-5368) # As of 1780 CE Quarter 2
C absoluteZero1780Q2Int_Cel = int(-3000) # As of 1780 CE Quarter 2
C Rankine
C Kelvin
C End of script

C File info
C File type: Fortan 2018 source file (*.for)
C File version: 1 (Wednesday, January 20th 2021 at 2:09 pm)
C Line count (including blank lines and compiler line): 64

STOP
