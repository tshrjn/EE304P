#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Oct  9 00:29:14 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
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
		self.vol = vol =  .05
		self.samp_rate = samp_rate = 256000

		##################################################
		# Blocks
		##################################################
		_vol_sizer = wx.BoxSizer(wx.VERTICAL)
		self._vol_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_vol_sizer,
			value=self.vol,
			callback=self.set_vol,
			label='vol',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._vol_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_vol_sizer,
			value=self.vol,
			callback=self.set_vol,
			minimum=0,
			maximum= .1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_vol_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
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
		self.Add(self.wxgui_scopesink2_0.win)
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate/8,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0_0.win)
		self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(8, (firdes.low_pass(1,samp_rate,2000,100)), -51500, samp_rate)
		self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/8)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/8)
		self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
		self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((vol, ))
		self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/Jack_Sparrow/EE304P/Lab05/ssb_lsb_256k_complex2.dat", True)
		self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
		self.blocks_add_xx_0 = blocks.add_vff(1)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=3,
			decimation=2,
			taps=None,
			fractional_bw=None,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)
		self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate/8, analog.GR_COS_WAVE, 1500, 1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate/8, analog.GR_SIN_WAVE, 1500, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_file_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_float_1, 0))
		self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_throttle_0_0, 0))
		self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_0_0, 0))
		self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_rational_resampler_xxx_0, 0))


	def get_vol(self):
		return self.vol

	def set_vol(self, vol):
		self.vol = vol
		self.blocks_multiply_const_vxx_0.set_k((self.vol, ))
		self._vol_slider.set_value(self.vol)
		self._vol_text_box.set_value(self.vol)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.blocks_throttle_0_0.set_sample_rate(self.samp_rate/8)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate/8)
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,2000,100)))
		self.blocks_throttle_0.set_sample_rate(self.samp_rate/8)
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/8)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/8)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

