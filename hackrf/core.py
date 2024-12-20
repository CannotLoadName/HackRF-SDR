#-*-coding:utf-8;-*-
from ctypes import CDLL,CFUNCTYPE,c_bool,c_char_p,c_double,c_int,c_size_t,c_ubyte,c_uint,c_uint16,c_uint32,c_uint64,c_uint8,c_void_p,POINTER,Structure
from json import load
from os.path import dirname,join
from sys import maxsize
if maxsize>0x100000000:
    LIBRARY=CDLL(load(open(join(dirname(__file__),"config.json"),"r",encoding="utf-8"))["x64"])
else:
    LIBRARY=CDLL(load(open(join(dirname(__file__),"config.json"),"r",encoding="utf-8"))["x86"])
class hackrf_transfer(Structure):
    _fields_=(
        ("device",c_void_p),
        ("buffer",POINTER(c_uint8)),
        ("buffer_length",c_int),
        ("valid_length",c_int),
        ("rx_ctx",c_void_p),
        ("tx_ctx",c_void_p)
    )
class read_partid_serialno_t(Structure):
    _fields_=(
        ("part_id",c_uint32*2),
        ("serial_no",c_uint32*4)
    )
class hackrf_operacake_dwell_time(Structure):
    _fields_=(
        ("dwell",c_uint32),
        ("port",c_uint8)
    )
class hackrf_operacake_freq_range(Structure):
    _fields_=(
        ("freq_min",c_uint16),
        ("freq_max",c_uint16),
        ("port",c_uint8)
    )
class hackrf_bool_user_settting(Structure):
    _fields_=(
        ("do_update",c_bool),
        ("change_on_mode_entry",c_bool),
        ("enabled",c_bool)
    )
class hackrf_bias_t_user_settting_req(Structure):
    _fields_=(
        ("tx",hackrf_bool_user_settting),
        ("rx",hackrf_bool_user_settting),
        ("off",hackrf_bool_user_settting)
    )
class hackrf_m0_state(Structure):
    _fields_=(
        ("requested_mode",c_uint16),
        ("request_flag",c_uint16),
        ("active_mode",c_uint32),
        ("m0_count",c_uint32),
        ("m4_count",c_uint32),
        ("num_shortfalls",c_uint32),
        ("longest_shortfall",c_uint32),
        ("shortfall_limit",c_uint32),
        ("threshold",c_uint32),
        ("next_mode",c_uint32),
        ("error",c_uint32)
    )
class hackrf_device_list_t(Structure):
    _fields_=(
        ("serial_numbers",POINTER(c_char_p)),
        ("usb_board_ids",POINTER(c_int)),
        ("usb_device_index",POINTER(c_int)),
        ("devicecount",c_int),
        ("usb_devices",POINTER(c_void_p)),
        ("usb_devicecount",c_int)
    )
hackrf_sample_block_cb_fn=CFUNCTYPE(c_int,POINTER(hackrf_transfer))
hackrf_tx_block_complete_cb_fn=CFUNCTYPE(None,POINTER(hackrf_transfer),c_int)
hackrf_flush_cb_fn=CFUNCTYPE(None,c_void_p,c_int)
LIBRARY.hackrf_init.argtypes=()
LIBRARY.hackrf_init.restype=c_int
LIBRARY.hackrf_exit.argtypes=()
LIBRARY.hackrf_exit.restype=c_int
LIBRARY.hackrf_library_version.argtypes=()
LIBRARY.hackrf_library_version.restype=c_char_p
LIBRARY.hackrf_library_release.argtypes=()
LIBRARY.hackrf_library_release.restype=c_char_p
LIBRARY.hackrf_device_list.argtypes=()
LIBRARY.hackrf_device_list.restype=POINTER(hackrf_device_list_t)
LIBRARY.hackrf_device_list_open.argtypes=(POINTER(hackrf_device_list_t),c_int,POINTER(c_void_p))
LIBRARY.hackrf_device_list_open.restype=c_int
LIBRARY.hackrf_device_list_free.argtypes=(POINTER(hackrf_device_list_t),)
LIBRARY.hackrf_device_list_free.restype=None
LIBRARY.hackrf_open.argtypes=(POINTER(c_void_p),)
LIBRARY.hackrf_open.restype=c_int
LIBRARY.hackrf_open_by_serial.argtypes=(c_char_p,POINTER(c_void_p))
LIBRARY.hackrf_open_by_serial.restype=c_int
LIBRARY.hackrf_close.argtypes=(c_void_p,)
LIBRARY.hackrf_close.restype=c_int
LIBRARY.hackrf_start_rx.argtypes=(c_void_p,hackrf_sample_block_cb_fn,c_void_p)
LIBRARY.hackrf_start_rx.restype=c_int
LIBRARY.hackrf_stop_rx.argtypes=(c_void_p,)
LIBRARY.hackrf_stop_rx.restype=c_int
LIBRARY.hackrf_start_tx.argtypes=(c_void_p,hackrf_sample_block_cb_fn,c_void_p)
LIBRARY.hackrf_start_tx.restype=c_int
LIBRARY.hackrf_set_tx_block_complete_callback.argtypes=(c_void_p,hackrf_tx_block_complete_cb_fn)
LIBRARY.hackrf_set_tx_block_complete_callback.restype=c_int
LIBRARY.hackrf_enable_tx_flush.argtypes=(c_void_p,hackrf_flush_cb_fn,c_void_p)
LIBRARY.hackrf_enable_tx_flush.restype=c_int
LIBRARY.hackrf_stop_tx.argtypes=(c_void_p,)
LIBRARY.hackrf_stop_tx.restype=c_int
LIBRARY.hackrf_get_m0_state.argtypes=(c_void_p,POINTER(hackrf_m0_state))
LIBRARY.hackrf_get_m0_state.restype=c_int
LIBRARY.hackrf_set_tx_underrun_limit.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_tx_underrun_limit.restype=c_int
LIBRARY.hackrf_set_rx_overrun_limit.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_rx_overrun_limit.restype=c_int
LIBRARY.hackrf_is_streaming.argtypes=(c_void_p,)
LIBRARY.hackrf_is_streaming.restype=c_int
LIBRARY.hackrf_max2837_read.argtypes=(c_void_p,c_uint8,POINTER(c_uint16))
LIBRARY.hackrf_max2837_read.restype=c_int
LIBRARY.hackrf_max2837_write.argtypes=(c_void_p,c_uint8,c_uint16)
LIBRARY.hackrf_max2837_write.restype=c_int
LIBRARY.hackrf_si5351c_read.argtypes=(c_void_p,c_uint16,POINTER(c_uint16))
LIBRARY.hackrf_si5351c_read.restype=c_int
LIBRARY.hackrf_si5351c_write.argtypes=(c_void_p,c_uint16,c_uint16)
LIBRARY.hackrf_si5351c_write.restype=c_int
LIBRARY.hackrf_set_baseband_filter_bandwidth.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_baseband_filter_bandwidth.restype=c_int
LIBRARY.hackrf_rffc5071_read.argtypes=(c_void_p,c_uint8,POINTER(c_uint16))
LIBRARY.hackrf_rffc5071_read.restype=c_int
LIBRARY.hackrf_rffc5071_write.argtypes=(c_void_p,c_uint8,c_uint16)
LIBRARY.hackrf_rffc5071_write.restype=c_int
LIBRARY.hackrf_spiflash_erase.argtypes=(c_void_p,)
LIBRARY.hackrf_spiflash_erase.restype=c_int
LIBRARY.hackrf_spiflash_write.argtypes=(c_void_p,c_uint32,c_uint16,POINTER(c_ubyte))
LIBRARY.hackrf_spiflash_write.restype=c_int
LIBRARY.hackrf_spiflash_read.argtypes=(c_void_p,c_uint32,c_uint16,POINTER(c_ubyte))
LIBRARY.hackrf_spiflash_read.restype=c_int
LIBRARY.hackrf_spiflash_status.argtypes=(c_void_p,POINTER(c_uint8))
LIBRARY.hackrf_spiflash_status.restype=c_int
LIBRARY.hackrf_spiflash_clear_status.argtypes=(c_void_p,)
LIBRARY.hackrf_spiflash_clear_status.restype=c_int
LIBRARY.hackrf_cpld_write.argtypes=(c_void_p,POINTER(c_ubyte),c_uint)
LIBRARY.hackrf_cpld_write.restype=c_int
LIBRARY.hackrf_board_id_read.argtypes=(c_void_p,POINTER(c_uint8))
LIBRARY.hackrf_board_id_read.restype=c_int
LIBRARY.hackrf_version_string_read.argtypes=(c_void_p,c_char_p,c_uint8)
LIBRARY.hackrf_version_string_read.restype=c_int
LIBRARY.hackrf_usb_api_version_read.argtypes=(c_void_p,POINTER(c_uint16))
LIBRARY.hackrf_usb_api_version_read.restype=c_int
LIBRARY.hackrf_set_freq.argtypes=(c_void_p,c_uint64)
LIBRARY.hackrf_set_freq.restype=c_int
LIBRARY.hackrf_set_freq_explicit.argtypes=(c_void_p,c_uint64,c_uint64,c_int)
LIBRARY.hackrf_set_freq_explicit.restype=c_int
LIBRARY.hackrf_set_sample_rate_manual.argtypes=(c_void_p,c_uint32,c_uint32)
LIBRARY.hackrf_set_sample_rate_manual.restype=c_int
LIBRARY.hackrf_set_sample_rate.argtypes=(c_void_p,c_double)
LIBRARY.hackrf_set_sample_rate.restype=c_int
LIBRARY.hackrf_set_amp_enable.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_amp_enable.restype=c_int
LIBRARY.hackrf_board_partid_serialno_read.argtypes=(c_void_p,POINTER(read_partid_serialno_t))
LIBRARY.hackrf_board_partid_serialno_read.restype=c_int
LIBRARY.hackrf_set_lna_gain.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_lna_gain.restype=c_int
LIBRARY.hackrf_set_vga_gain.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_vga_gain.restype=c_int
LIBRARY.hackrf_set_txvga_gain.argtypes=(c_void_p,c_uint32)
LIBRARY.hackrf_set_txvga_gain.restype=c_int
LIBRARY.hackrf_set_antenna_enable.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_antenna_enable.restype=c_int
LIBRARY.hackrf_error_name.argtypes=(c_int,)
LIBRARY.hackrf_error_name.restype=c_char_p
LIBRARY.hackrf_board_id_name.argtypes=(c_int,)
LIBRARY.hackrf_board_id_name.restype=c_char_p
LIBRARY.hackrf_board_id_platform.argtypes=(c_int,)
LIBRARY.hackrf_board_id_platform.restype=c_uint32
LIBRARY.hackrf_usb_board_id_name.argtypes=(c_int,)
LIBRARY.hackrf_usb_board_id_name.restype=c_char_p
LIBRARY.hackrf_filter_path_name.argtypes=(c_int,)
LIBRARY.hackrf_filter_path_name.restype=c_char_p
LIBRARY.hackrf_compute_baseband_filter_bw_round_down_lt.argtypes=(c_uint32,)
LIBRARY.hackrf_compute_baseband_filter_bw_round_down_lt.restype=c_uint32
LIBRARY.hackrf_compute_baseband_filter_bw.argtypes=(c_uint32,)
LIBRARY.hackrf_compute_baseband_filter_bw.restype=c_uint32
LIBRARY.hackrf_set_hw_sync_mode.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_hw_sync_mode.restype=c_int
LIBRARY.hackrf_init_sweep.argtypes=(c_void_p,POINTER(c_uint16),c_int,c_uint32,c_uint32,c_uint32,c_int)
LIBRARY.hackrf_init_sweep.restype=c_int
LIBRARY.hackrf_get_operacake_boards.argtypes=(c_void_p,POINTER(c_uint8))
LIBRARY.hackrf_get_operacake_boards.restype=c_int
LIBRARY.hackrf_set_operacake_mode.argtypes=(c_void_p,c_uint8,c_int)
LIBRARY.hackrf_set_operacake_mode.restype=c_int
LIBRARY.hackrf_get_operacake_mode.argtypes=(c_void_p,c_uint8,POINTER(c_int))
LIBRARY.hackrf_get_operacake_mode.restype=c_int
LIBRARY.hackrf_set_operacake_ports.argtypes=(c_void_p,c_uint8,c_uint8,c_uint8)
LIBRARY.hackrf_set_operacake_ports.restype=c_int
LIBRARY.hackrf_set_operacake_dwell_times.argtypes=(c_void_p,POINTER(hackrf_operacake_dwell_time),c_uint8)
LIBRARY.hackrf_set_operacake_dwell_times.restype=c_int
LIBRARY.hackrf_set_operacake_freq_ranges.argtypes=(c_void_p,POINTER(hackrf_operacake_freq_range),c_uint8)
LIBRARY.hackrf_set_operacake_freq_ranges.restype=c_int
LIBRARY.hackrf_reset.argtypes=(c_void_p,)
LIBRARY.hackrf_reset.restype=c_int
LIBRARY.hackrf_set_operacake_ranges.argtypes=(c_void_p,POINTER(c_uint8),c_uint8)
LIBRARY.hackrf_set_operacake_ranges.restype=c_int
LIBRARY.hackrf_set_clkout_enable.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_clkout_enable.restype=c_int
LIBRARY.hackrf_get_clkin_status.argtypes=(c_void_p,POINTER(c_uint8))
LIBRARY.hackrf_get_clkin_status.restype=c_int
LIBRARY.hackrf_operacake_gpio_test.argtypes=(c_void_p,c_uint8,POINTER(c_uint16))
LIBRARY.hackrf_operacake_gpio_test.restype=c_int
LIBRARY.hackrf_set_ui_enable.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_ui_enable.restype=c_int
LIBRARY.hackrf_start_rx_sweep.argtypes=(c_void_p,hackrf_sample_block_cb_fn,c_void_p)
LIBRARY.hackrf_start_rx_sweep.restype=c_int
LIBRARY.hackrf_get_transfer_buffer_size.argtypes=(c_void_p,)
LIBRARY.hackrf_get_transfer_buffer_size.restype=c_size_t
LIBRARY.hackrf_get_transfer_queue_depth.argtypes=(c_void_p,)
LIBRARY.hackrf_get_transfer_queue_depth.restype=c_uint32
LIBRARY.hackrf_board_rev_read.argtypes=(c_void_p,POINTER(c_uint8))
LIBRARY.hackrf_board_rev_read.restype=c_int
LIBRARY.hackrf_board_rev_name.argtypes=(c_int,)
LIBRARY.hackrf_board_rev_name.restype=c_char_p
LIBRARY.hackrf_supported_platform_read.argtypes=(c_void_p,POINTER(c_uint32))
LIBRARY.hackrf_supported_platform_read.restype=c_int
LIBRARY.hackrf_set_leds.argtypes=(c_void_p,c_uint8)
LIBRARY.hackrf_set_leds.restype=c_int
LIBRARY.hackrf_set_user_bias_t_opts.argtypes=(c_void_p,POINTER(hackrf_bias_t_user_settting_req))
LIBRARY.hackrf_set_user_bias_t_opts.restype=c_int