#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Oct  9 00:26:20 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
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
		self.volume = volume = 0.05
		self.samp_rate = samp_rate = 256000
		self.resamp_factor = resamp_factor = 4

		##################################################
		# Blocks
		##################################################
		_volume_sizer = wx.BoxSizer(wx.VERTICAL)
		self._volume_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			label='volume',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._volume_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_volume_sizer)
		self.wxgui_scopesink2_1_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_1_0.win)
		self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=True,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_1.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
			self.GetWin(),
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
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.low_pass_filter_0 = gr.fir_filter_ccf(resamp_factor, firdes.low_pass(
			1, samp_rate/resamp_factor, 5000, 100, firdes.WIN_HAMMING, 6.76))
		self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
		self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/Jack_Sparrow/EE304P/Lab04/am_usrp710.dat", True)
		self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=3,
			decimation=4,
			taps=None,
			fractional_bw=None,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -80000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))
		self.connect((self.blocks_file_source_0, 0), (self.wxgui_scopesink2_1, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.wxgui_scopesink2_1_0, 0))


	def get_volume(self):
		return self.volume

	def set_volume(self, volume):
		self.volume = volume
		self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
		self._volume_slider.set_value(self.volume)
		self._volume_text_box.set_value(self.volume)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.resamp_factor, 5000, 100, firdes.WIN_HAMMING, 6.76))
		self.wxgui_scopesink2_1_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

	def get_resamp_factor(self):
		return self.resamp_factor

	def set_resamp_factor(self, resamp_factor):
		self.resamp_factor = resamp_factor
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.resamp_factor, 5000, 100, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

