""" OPEN ACOUSTICS """

'''Imports'''

#import math
from math import sqrt #for speed of sound
from math import pi #for angular wavenumber and angular frequency
from math import log10 #for decibel sound intensity, Leq, and SEL
from sympy import integrate #for Leq
from sympy import Symbol #for Leq
import numpy #for SEL
from scipy.integrate import quad

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


'''Spectrum'''


'''Descriptors'''
#is the time in this formula seconds or hours?
#is the sound pressure in this formula one measurement at one time?
#If so, which measurement at which time do you use?
def Leq(time, sound_pressure, reference_pressure = 2*(10**(-5))):
    t = Symbol('t')
    integrand = (sound_pressure**2)/(reference_pressure**2)
    integration = integrate(integrand,(t, 0, time))
    return 10*log10((1/time)*integration)

#can't get the integration with infinite limits to return positive
"""
def SEL(sound_pressure, reference_pressure = 2*(10**(-5))):
    t = Symbol('t')
    integrand = lambda x: ((sound_pressure**2)/(reference_pressure**2))
    integration = quad(integrand,-numpy.inf, numpy.inf)
    print(integration)
    return 10*log10(integration[0])
    
"""
def SEL(time, sound_pressure):
    return Leq(time, sound_pressure) + (10*log10(time))

