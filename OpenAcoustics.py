""" OPEN ACOUSTICS """

'''Imports'''

#import math
from math import sqrt #for speed of sound
from math import pi #for angular wavenumber and angular frequency
from math import log10 #for decibel sound intensity, Leq, and SEL
from numpy import asarray #for Leq/SEL
from numpy import array #for a weighting

'''Global Variables'''

''''Units'''

def period(frequency):
    return float(1/frequency)
    #unit is seconds

def frequency1(period):
    return float(1/period)
    #unit is hertz

def frequency2(wavelength, degreesCelsius = 15):
    return speed_of_sound(degreesCelsius)/wavelength
    #unit is hertz

def speed_of_sound(degreesCelsius):
    return 20.05 * sqrt(273.75 + degreesCelsius)
    #unit is m/s, and medium is air (do one for gas)

def wavelength(frequency, degreesCelsius = 15):
    return speed_of_sound(degreesCelsius)/frequency
    #unit is meters

def wavenumber(wavelength):
    return 1/wavelength
    #unit is cycles per meter

def angular_wavenumber(wavelength):
    return (2*pi)/wavelength
    #unit is radians per meter

def angular_frequency1(period):
    return (2*pi)/period

def angular_frequency2(frequency):
    return (2*pi)*frequency





'''Transverse & Longitudnal Waves'''


'''Physical Acoustic Quantities'''


'''Inverse Square & Distance Laws'''


'''Decibel'''

def sound_intensity_level(intensity, I0 = 10**(-12), r = True):
    if r == True: return round(10*log10(intensity/I0), 1)
    else: return 10*log10(intensity/I0)
    #unit is dB intensity (SIL)

def sound_pressure_level(pressure, P0 = 2*(10**(-5)), r = True):
    if r == True: return round(20*log10(pressure/P0), 1)
    else: return 20*log10(pressure/P0)
    #unit is dB pressure (SPL)

def sound_power_level(watts, W0 = 10**(-12), r = True):
    if r == True: return round(10*log10(watts/W0), 1)
    else: return 10*log10(watts/W0)
    #unit is dB power (SWL)

def db_add(levels):
    total = 0
    for i in levels: total += 10**(i/10)
    return round(10*log10(total), 1)

'''Decibel Weightings'''

def a_weighting(spectrum):
    spectrum_array = asarray(spectrum)
    single_corrections = array([-39.4, -26.2, -16.1, -8.6,
                                -3.2, 0, 1.2, 1, -1.1, -6.6])
    third_corrections = array([-56.7, -50.5, -44.7, -39.4,
                               -34.6, -30.2, -26.2, -22.5,
                               -19.1, -16.1, -13.4, -10.9,
                               -8.6, -6.6, -4.8, -3.2, -1.9,
                               -0.8, 0, 0.6, 1.0, 1.2, 1.3,
                               1.2, 1.0, 0.5, -0.1, -1.1,
                               -2.5, -4.3, -6.6])
    if len(spectrum) > 10:
        #1/3 octave band
        return (spectrum_array + third_corrections)
    else:
        #1/1 octave band
        return (spectrum_array + single_corrections)


'''Spectrum'''

#returns a list of the center frequencies in the range of human hearing (20hz - 20kHz)
def octave_band_centers(low_fc = 31.250):
    centers, center = [low_fc], low_fc
    while centers[-1] < 10000:
        center *= 2
        centers.append(round(center))
    return centers

def third_octave_band_centers(low_fc = 15.625):
    centers, center = [low_fc], low_fc
    while centers[-1] < 16000:
        center *= 2**(1/3)
        centers.append(round(center, 2))
    return centers
    



'''Descriptors'''

#takes two regular python lists as arguments, time (seconds) and level (dB)
def Leq(time, level):
    T, L = asarray(time), asarray(level)
    return 10*log10(sum(T*10**(L/10))/sum(T))

def SEL(time, level):
    T, L = asarray(time), asarray(level)
    return 10*log10(sum(T*10**(L/10)))

def testsel(time, level):
    T, L = asarray(time), asarray(level)
    return Leq(T, L) + (10 * log10(sum(T)))

def Ldn(daylevel, daytime, nightlevel, nighttime):
    day, night = Leq(daylevel, daytime), Leq(nightlevel, nighttime)
    return 10*log10((15*(10**(day/10))+9*(10**((night+10)/10)))/24)
    

