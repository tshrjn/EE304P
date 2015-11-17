To : Prof. Renu
From : Tushar Jain, B13236
Subject: Lab-08

##Our task :
1. Explore the NBFM module of gnuradio.
2. Modulate this audio clip using NBFM transmit module.
3. Model an AWGN channel; use a NBFM recevier module and see how the performance is affected by noise.
4. Modulate the same signal using DSB-SC and compare the noise performance of DSB-SC and NBFM.
5. Repeat for WBFM module.
6. Make a note of all your observations in a text file which you have to upload at the end of the lab session along with the grc files. 


##Lab Members
Concepts were discussed with following persons:
1. Shri Kisna Mahajan, B13230
2. Prof. Renu R

##Observations:
1. On modulating with NBFM module, the spectrum becomes symmetric about 0 with peak at 0, and bandwidth of 10 kHz & max amp = -8.4 dB.
2. Same as 1
3. On adding Additive White Gaussian Channel, audio is understandable till 0.650 amplittude of AWGN. Above that, audio is incomprehensible. 
4. Noise performance of NBFM is much better than DSB-SC as a small amount of noise disrupts the signal completely for DSB-SC. In other words, NBFM is much more tolerant to Noise. DSB-SC is comprehensible to 0.250 AWGN-amplitude.
5. For WBFM, bandwidth increases to 30kHz instead of 10Khz as of NBFM. Also, noise performance is better than NBFM. In our case, above the AWGN-amplitude of 1.6, the signal is completely incomprehensible ( as tested by Mr. Paramjeet, TA).

