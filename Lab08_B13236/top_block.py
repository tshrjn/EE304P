#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Nov 20 12:08:55 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 88200
        self.noiseAmp = noiseAmp = 0
        self.consMultiply = consMultiply = 1.333

        ##################################################
        # Blocks
        ##################################################
        _noiseAmp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noiseAmp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noiseAmp_sizer,
        	value=self.noiseAmp,
        	callback=self.set_noiseAmp,
        	label='noiseAmp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noiseAmp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noiseAmp_sizer,
        	value=self.noiseAmp,
        	callback=self.set_noiseAmp,
        	minimum=0,
        	maximum=2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noiseAmp_sizer)
        self.n = self.n = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.n.AddPage(grc_wxgui.Panel(self.n), "tab1")
        self.n.AddPage(grc_wxgui.Panel(self.n), "tab2")
        self.n.AddPage(grc_wxgui.Panel(self.n), "tab3")
        self.n.AddPage(grc_wxgui.Panel(self.n), "tab4")
        self.Add(self.n)
        _consMultiply_sizer = wx.BoxSizer(wx.VERTICAL)
        self._consMultiply_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_consMultiply_sizer,
        	value=self.consMultiply,
        	callback=self.set_consMultiply,
        	label='consMultiply',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._consMultiply_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_consMultiply_sizer,
        	value=self.consMultiply,
        	callback=self.set_consMultiply,
        	minimum=0,
        	maximum=3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_consMultiply_sizer)
        self.wxgui_fftsink2_0_2 = fftsink2.fft_sink_c(
        	self.n.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT After AWGN Addition",
        	peak_hold=False,
        )
        self.n.GetPage(2).Add(self.wxgui_fftsink2_0_2.win)
        self.wxgui_fftsink2_0_1 = fftsink2.fft_sink_c(
        	self.n.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT AFter WSBM Transmit",
        	peak_hold=False,
        )
        self.n.GetPage(1).Add(self.wxgui_fftsink2_0_1.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.n.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT of File Source",
        	peak_hold=False,
        )
        self.n.GetPage(0).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.n.GetPage(3).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT After WSBM Receive (We listen to this)",
        	peak_hold=False,
        )
        self.n.GetPage(3).Add(self.wxgui_fftsink2_0.win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/students/btech/b13236/EE304P/Lab_8/zeno_lp.wav", True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((consMultiply, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(44100, "", True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=44100,
        	quad_rate=88200,
        	tau=75e-6,
        	max_dev=75e3,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=88200,
        	audio_decimation=2,
        )
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noiseAmp, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.analog_wfm_tx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_wfm_tx_0, 0), (self.wxgui_fftsink2_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.wxgui_fftsink2_0_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_2.set_sample_rate(self.samp_rate)

    def get_noiseAmp(self):
        return self.noiseAmp

    def set_noiseAmp(self, noiseAmp):
        self.noiseAmp = noiseAmp
        self._noiseAmp_slider.set_value(self.noiseAmp)
        self._noiseAmp_text_box.set_value(self.noiseAmp)
        self.analog_noise_source_x_0.set_amplitude(self.noiseAmp)

    def get_consMultiply(self):
        return self.consMultiply

    def set_consMultiply(self, consMultiply):
        self.consMultiply = consMultiply
        self._consMultiply_slider.set_value(self.consMultiply)
        self._consMultiply_text_box.set_value(self.consMultiply)
        self.blocks_multiply_const_vxx_0.set_k((self.consMultiply, ))

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

