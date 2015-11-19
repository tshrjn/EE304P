#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep 11 14:50:34 2015
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
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
		self.samp_rate = samp_rate = 320000

		##################################################
		# Blocks
		##################################################
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
		self.hilbert_fc_0 = filter.hilbert_fc(64)
		self.high_pass_filter_0 = gr.interp_fir_filter_fff(1, firdes.high_pass(
			1, samp_rate, 15000, 10, firdes.WIN_HAMMING, 6.76))
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
		self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
		self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
		self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
		self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
		self.blocks_add_xx_0 = blocks.add_vff(1)
		self.analog_sig_source_x_0_0_2 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 20000, 1, 0)
		self.analog_sig_source_x_0_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 20000, 1, 0)
		self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 20000, 1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.high_pass_filter_0, 0))
		self.connect((self.high_pass_filter_0, 0), (self.hilbert_fc_0, 0))
		self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_1, 0))
		self.connect((self.analog_sig_source_x_0_0_2, 0), (self.blocks_multiply_xx_1, 1))
		self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_xx_1_0, 1))
		self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_1_0, 0))
		self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_real_0, 0))
		self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate)
		self.analog_sig_source_x_0_0_2.set_sampling_freq(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 15000, 10, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

