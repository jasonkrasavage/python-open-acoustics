""" OPEN ACOUSTICS """


'''Imports'''

#import math
from numpy import sqrt #for speed of sound
from numpy import pi #for angular wavenumber and angular frequency
from numpy import log10 #for decibel sound intensity, Leq, and SEL
from numpy import asarray #for Leq/SEL
from numpy import array #for a weighting


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


'''Inverse Square & Distance Laws'''

#returns the dB SPL value at the new distance for the given sound source, distance is in meters
def inverse_distance_law(dBSPL,oldDistance, newDistance):
    return dBSPL+20*log10(oldDistance/newDistance)
    

'''Decibel'''

def sound_intensity_level(intensity, I0 = 10**(-12)):
    return 10*log10(intensity/I0)
    #unit is dB intensity (SIL)

def sound_pressure_level(pressure, P0 = 2*(10**(-5))):
    return 20*log10(pressure/P0)
    #unit is dB pressure (SPL)

def sound_power_level(watts, W0 = 10**(-12)):
    return 10*log10(watts/W0)
    #unit is dB power (SWL)

def db_add(levels):
    L = asarray(levels)
    return (10*log10(sum(10**(L/10))))


'''Decibel Weightings'''
#convert between dbA and db


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

def c_weighting(spectrum):
    spectrum_array = asarray(spectrum)
    single_corrections = array([-3.0, -0.8, -0.2, 0.0, 0.0,
                                0.0, -0.2, -0.8, -3.0, -8.5])
    third_corrections = array([-8.5, -6.2, -4.4, -3.0, -2.0
                               -1.3, -0.8, -0.5, -0.3, -0.2
                               -0.1, 0.0, 0.0, 0.0, 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, -0.1, -0.2,
                               -0.3, -0.5, -0.8, -1.3, -2.0,
                               -3.0, -4.4, -6.2, -8.5])
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

def recExposureTime(level): #returns the recommended exposure times for an array of dBA values (minutes)
    return 480/(2**((level-85)/3))

def dose(exposureTimes, levels): #returns the daily noise dose for arrays of both actual exposure times and their corresponding dBA levels)
    C, L = asarray(exposureTimes), asarray(levels)
    return 100*sum(C/recExposureTime(L))

def TWA(exposureTimes, levels): #returns the time weighted average for two corresponding lists of exposure times and levels
    C, L = asarray(exposureTimes), asarray(levels)
    return 10*log10((dose(C,L))/100)+85

def Leq(times, levels):
    T, L = asarray(times), asarray(levels)
    return 10*log10(sum(T*10**(L/10))/sum(T))

def SEL(times, levels):
    T, L = asarray(times), asarray(levels)
    return 10*log10(sum(T*10**(L/10)))

def testsel(times, levels):
    T, L = asarray(times), asarray(levels)
    return Leq(T, L) + (10 * log10(sum(T)))

def Ldn(daylevels, daytimes, nightlevels, nighttimes):
    day, night = Leq(daylevels, daytimes), Leq(nightlevels, nighttimes)
    return 10*log10((16*(10**(day/10))+8*(10**((night+10)/10)))/24)

def Lden(daylevels, daytimes, eveninglevels, eveningtimes, nightlevels, nighttimes):
    day, evening, night = Leq(daylevels, daytimes), Leq(eveninglevels, eveningtimes), Leq(nightlevels, nighttimes)
    return 10*log10((12*(10**(day/10))+4*(10**((evening+5)/10))+8*(10**((night+10)/10)))/24)
    

