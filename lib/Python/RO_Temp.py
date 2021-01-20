# Start of script
# Reasonable overflow temperature Python library
# This library handles overflows for temperature counters, so that they don't become completely unreasonable
'''
Current issues:
I don't know how the program will link to this library and detect an overflow
Temperatures in Fahrenheit, Celsius, Kelvin, and Rankine need to be accounted for
An exact value for absolute hot and absolute cold has not been defined. It is still a question in science. Estimates are sorted by year
My research on this is a bit shotty, and needs correction. I feel like I made several errors here
Absolute hot is not fully documented, and needs calculations and assignments
'''
"""
Some notes:
Absolute hot is a theoretical max temperature
Absolute cold is not completely exact yet, as new discoveries are being made, finding colder and colder temperatures, and pushing the science further
"""
overflowCounter1Int = int(0) # Capture here upon detection of overflow
overflowCounter1Float = float(0) # Capture here upon detection of overflow
testInt_x16 = int(65536) # 16 bit integer for testing
# testInt_x32 = int(42949672964294967296) # 32 bit integer for testing, calculation error?
# testInt_x64 = int(18446744073709551615) # 64 bit integer for testing, calculation error?
# absoluteHotFloat = float(2.55*10^32) # Needs to be calculated
# absoluteHotInt = int(2.55*10^32) # Needs to be calculated
# As of 1740 CE
absoluteZero1740Float_Fah = float(-400.00) # As of 1740 CE
absoluteZero1740Float_Cel = float(-240.00) # As of 1740 CE
absoluteZero1740Int_Fah = int(-400) # As of 1740 CE
absoluteZero1740Int_Cel = int(-240) # As of 1740 CE
# Rankine
# Kelvin
# As of 1779 CE
absoluteZero1779Float_Fah = float(-454.00) # As of 1779 CE
absoluteZero1779Float_Cel = float(-270.00) # As of 1779 CE
absoluteZero1779Int_Fah = int(-454) # As of 1779 CE
absoluteZero1779Int_Cel = int(-270) # As of 1779 CE
# Rankine
# Kelvin
''' I divided 1780 into 2 quarters, as the source I am using (John Dalton >-> Wikipedia) defines the first calc as 1500 and the final as 3000, both in 1780. '''
# As of 1780 CE Q1
absoluteZero1780Q1Float_Fah = float(-2668.00) # As of 1780 CE Quarter 1
absoluteZero1780Q1Float_Cel = float(-1500.00) # As of 1780 CE Quarter 1
absoluteZero1780Q1Int_Fah = int(-2668) # As of 1780 CE Quarter 1
absoluteZero1780Q1Int_Cel = int(-1500) # As of 1780 CE Quarter 1
# As of 1780 CE Q2
absoluteZero1780Q2Float_Fah = float(-5368.00) # As of 1780 CE Quarter 2
absoluteZero1780Q2Float_Cel = float(-3000.00) # As of 1780 CE Quarter 2
absoluteZero1780Q2Int_Fah = int(-5368) # As of 1780 CE Quarter 2
absoluteZero1780Q2Int_Cel = int(-3000) # As of 1780 CE Quarter 2
# Rankine
# Kelvin
''' Divider '''
def overflowDetection():
  # Need a way to link to the program
def absoluteHot():
  if (overflowCounter1Int > absoluteHotInt):
    overflowCounter1Int == 0 # For now, it will just revert to zero
  if (overflowCounter1Float > absoluteHotFloat):
    overflowCounter1Float == 0.0 # For now, it will just revert to zero
def absoluteCold():
  if (overflowCounter1Int > absoluteColdInt):
    overflowCounter1Int == 0 # For now, it will just revert to zero
  if (overflowCounter1Float > absoluteColdFloat):
    overflowCounter1Float == 0.0 # For now, it will just revert to zero
# End of script
'''
File info
File type: Python source file (*.py)
File version: 1 (Wednesday, January 20th 2021 at 2:09 pm)
Line count (including blank lines and compiler line): 71
'''
