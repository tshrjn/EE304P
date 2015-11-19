#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct  8 22:59:17 2015
##################################################

from gnuradio import analog
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
		self.sliderFc = sliderFc = 20000
		self.sliderBeta = sliderBeta = 1
		self.samp_rate = samp_rate = 200000

		##################################################
		# Blocks
		##################################################
		_sliderFc_sizer = wx.BoxSizer(wx.VERTICAL)
		self._sliderFc_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_sliderFc_sizer,
			value=self.sliderFc,
			callback=self.set_sliderFc,
			label='sliderFc',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._sliderFc_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_sliderFc_sizer,
			value=self.sliderFc,
			callback=self.set_sliderFc,
			minimum=0,
			maximum=100000,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_sliderFc_sizer)
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
		_sliderBeta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._sliderBeta_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_sliderBeta_sizer,
			value=self.sliderBeta,
			callback=self.set_sliderBeta,
			label='sliderBeta',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._sliderBeta_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_sliderBeta_sizer,
			value=self.sliderBeta,
			callback=self.set_sliderBeta,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_sliderBeta_sizer)
		self.blocks_transcendental_0_0 = blocks.transcendental("sin", "float")
		self.blocks_transcendental_0 = blocks.transcendental("cos", "float")
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
		self.blocks_sub_xx_0 = blocks.sub_ff(1)
		self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
		self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
		self.blocks_integrate_xx_0 = blocks.integrate_ff(1)
		self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sliderFc, 1, 0)
		self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, sliderFc, 1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)
		self.Beta = blocks.multiply_const_vff((sliderBeta, ))

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.blocks_integrate_xx_0, 0))
		self.connect((self.blocks_integrate_xx_0, 0), (self.Beta, 0))
		self.connect((self.Beta, 0), (self.blocks_transcendental_0, 0))
		self.connect((self.Beta, 0), (self.blocks_transcendental_0_0, 0))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.blocks_transcendental_0_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
		self.connect((self.blocks_transcendental_0, 0), (self.blocks_multiply_xx_0_0, 1))
		self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_sub_xx_0, 0))
		self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_sub_xx_0, 1))
		self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_fftsink2_0, 0))


	def get_sliderFc(self):
		return self.sliderFc

	def set_sliderFc(self, sliderFc):
		self.sliderFc = sliderFc
		self._sliderFc_slider.set_value(self.sliderFc)
		self._sliderFc_text_box.set_value(self.sliderFc)
		self.analog_sig_source_x_0_0_0.set_frequency(self.sliderFc)
		self.analog_sig_source_x_0_0.set_frequency(self.sliderFc)

	def get_sliderBeta(self):
		return self.sliderBeta

	def set_sliderBeta(self, sliderBeta):
		self.sliderBeta = sliderBeta
		self._sliderBeta_slider.set_value(self.sliderBeta)
		self._sliderBeta_text_box.set_value(self.sliderBeta)
		self.Beta.set_k((self.sliderBeta, ))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

