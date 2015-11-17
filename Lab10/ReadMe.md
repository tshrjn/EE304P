To : Prof. Renu
From : Tushar Jain, B13236
Subject: Lab-10
Date: 17 November 2015

###Our tasks :
## QPSK by direct mapping 
1. Observe what happens to the signal constellation as you vary the noise in the channel and the cutoff frequency of the filter.
2. Observe the effects of inter symbol interference (ISI) and why is it caused?
## QPSK modulator
1. Model PSK mod with packet encoder & decoder with an AWGN channel and see how the performance is affected by noise.

###Lab Members:
Concepts were discussed with following persons:
1. Guntuku Vikas, B13212
2. Prof. Renu R

###Observations:
1. Addition nof noise obviously increases the distortion in the signal.
2. Cause of intersymbol interference (ISI) is the transmission of a signal through a bandlimited channel.
3. Due to above stated reason increasing the bandwidth decreases the ISI.
4. Above the half of sampling frequency, ISI cannot be observed. This is because above the half the sample rate sinc function covers the sufficinetly enough of the symbol sequence.
5. Raised cosine filter at the encoders introduces distortion which is removed by the PSK Demod block which has complimentary and it also acts as an LPF and takes care of ISI.
6. QPSK is very noise tolerant to noise  to good extent (e.g. 0.35), as the sin wave is reasonably understandable.
7. Also, Constellation sink is circular and elleptical for complex and float cosine respectively and vanishes after the noise value is greater than the possible signal amplitude.
8. The amplitude of modulated signal is unaffected by the noise as long as noise is less than the signal's amplitude but is shifted in phase and distorted.

