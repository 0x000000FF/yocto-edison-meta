cmd_/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o := gcc -Wp,-MD,/home/qqq/mt7601u/src/os/linux/../../os/linux/.rt_profile.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/4.6/include -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include -Iarch/x86/include/generated  -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include -Iinclude -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi -Iarch/x86/include/generated/uapi -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi -Iinclude/generated/uapi -include /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kconfig.h   -I/home/qqq/mt7601u/src/os/linux -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m32 -msoft-float -mregparm=3 -freg-struct-return -fno-pic -mpreferred-stack-boundary=2 -march=core2 -mtune=generic -mtune=generic -maccumulate-outgoing-args -Wa,-mtune=generic32 -ffreestanding -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -DCONFIG_AS_AVX=1 -DCONFIG_AS_AVX2=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -Wframe-larger-than=2048 -fno-stack-protector -Wno-unused-but-set-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -g -pg -fno-inline-functions-called-once -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO -DAGGREGATION_SUPPORT -DPIGGYBACK_SUPPORT -DWMM_SUPPORT -DLINUX -Wall -Wstrict-prototypes -Wno-trigraphs -DSYSTEM_LOG_SUPPORT -DRT28xx_MODE=AP -DCHIPSET=7601U -DRESOURCE_PRE_ALLOC   -I/home/qqq/mt7601u/src/include -DCONFIG_AP_SUPPORT -DUAPSD_SUPPORT -DMBSS_SUPPORT -DIAPP_SUPPORT -DDBG -DDOT1X_SUPPORT -DAP_SCAN_SUPPORT -DSCAN_SUPPORT -DHOSTAPD_SUPPORT -DRALINK_ATE -DCONFIG_RT2880_ATE_CMD_NEW   -I/home/qqq/mt7601u/src/ate/include -DRALINK_QA -DWSC_AP_SUPPORT -DWSC_V2_SUPPORT -DDOT11_N_SUPPORT -DDOT11N_DRAFT3 -DSTATS_COUNT_SUPPORT -DOS_ABL_SUPPORT -DOS_ABL_FUNC_SUPPORT -DOS_ABL_OS_PCI_SUPPORT -DOS_ABL_OS_USB_SUPPORT -DOS_ABL_OS_AP_SUPPORT -DOS_ABL_OS_STA_SUPPORT -DEXPORT_SYMTAB -DMT7601U -DMT7601 -DRLT_MAC -DRLT_RF -DRTMP_MAC_USB -DRTMP_USB_SUPPORT -DRTMP_TIMER_TASK_SUPPORT -DRX_DMA_SCATTER -DVCORECAL_SUPPORT -DRTMP_EFUSE_SUPPORT -DNEW_MBSSID_MODE -DRTMP_INTERNAL_TX_ALC -DCONFIG_ANDES_SUPPORT -DDPD_CALIBRATION_SUPPORT -DCONFIG_RX_CSO_SUPPORT  -DMODULE  -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(rt_profile)"  -D"KBUILD_MODNAME=KBUILD_STR(mt7601Uap)" -c -o /home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o /home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.c

source_/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o := /home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.c

deps_/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o := \
    $(wildcard include/config/sta/support.h) \
    $(wildcard include/config/ap/support.h) \
    $(wildcard include/config/opmode/on/ap.h) \
    $(wildcard include/config/opmode/on/sta.h) \
    $(wildcard include/config/5vt/enhance.h) \
    $(wildcard include/config/apsta/mixed/support.h) \
  /home/qqq/mt7601u/src/include/rt_config.h \
    $(wildcard include/config/h//.h) \
  /home/qqq/mt7601u/src/include/rtmp_comm.h \
    $(wildcard include/config/if/opmode/on/ap.h) \
    $(wildcard include/config/if/opmode/on/sta.h) \
  /home/qqq/mt7601u/src/include/rtmp_type.h \
  /home/qqq/mt7601u/src/include/rtmp_os.h \
  /home/qqq/mt7601u/src/include/os/rt_drv.h \
    $(wildcard include/config/multi/channel.h) \
    $(wildcard include/config/cso/support.h) \
    $(wildcard include/config/rx/cso/support.h) \
  /home/qqq/mt7601u/src/include/os/rt_linux_cmm.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/string.h \
    $(wildcard include/config/binary/printf.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/compiler.h \
    $(wildcard include/config/sparse/rcu/pointer.h) \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
    $(wildcard include/config/kprobes.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/compiler-gcc.h \
    $(wildcard include/config/arch/supports/optimized/inlining.h) \
    $(wildcard include/config/optimize/inlining.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/compiler-gcc4.h \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/types.h \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/lbdaf.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/int-ll64.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/int-ll64.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/bitsperlong.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitsperlong.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/bitsperlong.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/posix_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/stddef.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/stddef.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/x86/32.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/posix_types_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/posix_types.h \
  /usr/lib/gcc/x86_64-linux-gnu/4.6/include/stdarg.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/string.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/string.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/string_32.h \
    $(wildcard include/config/x86/use/3dnow.h) \
    $(wildcard include/config/kmemcheck.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ctype.h \
  /home/qqq/mt7601u/src/include/link_list.h \
  /home/qqq/mt7601u/src/include/rtmp_cmd.h \
    $(wildcard include/config/pm.h) \
    $(wildcard include/config/value.h) \
    $(wildcard include/config/init.h) \
  /home/qqq/mt7601u/src/include/iface/iface_util.h \
  /home/qqq/mt7601u/src/include/rtmp_def.h \
    $(wildcard include/config/desp/entry/size.h) \
  /home/qqq/mt7601u/src/include/oid.h \
    $(wildcard include/config/status.h) \
  /home/qqq/mt7601u/src/include/rtmp_chip.h \
    $(wildcard include/config/andes/support.h) \
  /home/qqq/mt7601u/src/include/mac_ral/pbf.h \
  /home/qqq/mt7601u/src/include/mac_ral/nmac/ral_nmac_pbf.h \
  /home/qqq/mt7601u/src/include/eeprom.h \
  /home/qqq/mt7601u/src/include/mac_ral/rtmp_mac.h \
  /home/qqq/mt7601u/src/include/mac_ral/nmac/ral_nmac.h \
  /home/qqq/mt7601u/src/include/rtmp_type.h \
  /home/qqq/mt7601u/src/include/mac_ral/omac/ral_omac_rxwi.h \
  /home/qqq/mt7601u/src/include/mac_ral/nmac/ral_nmac_txwi.h \
  /home/qqq/mt7601u/src/include/mac_ral/mac_usb.h \
  /home/qqq/mt7601u/src/include/mac_ral/nmac/ral_nmac_usb.h \
  /home/qqq/mt7601u/src/include/mac_ral/rtmp_mac.h \
  /home/qqq/mt7601u/src/include/chip/rtmp_phy.h \
  /home/qqq/mt7601u/src/include/mac_ral/rf_ctrl.h \
  /home/qqq/mt7601u/src/include/phy/rlt_phy.h \
  /home/qqq/mt7601u/src/include/rtmp_iface.h \
    $(wildcard include/config/.h) \
  /home/qqq/mt7601u/src/include/iface/rtmp_usb.h \
  /home/qqq/mt7601u/src/include/rtusb_io.h \
  /home/qqq/mt7601u/src/include/wpa_cmm.h \
  /home/qqq/mt7601u/src/include/dot11i_wpa.h \
  /home/qqq/mt7601u/src/include/rtmp_dot11.h \
  /home/qqq/mt7601u/src/include/rtmp_mcu.h \
  /home/qqq/mt7601u/src/include/chip/mt7601.h \
  /home/qqq/mt7601u/src/include/rtmp_timer.h \
  /home/qqq/mt7601u/src/include/mlme.h \
  /home/qqq/mt7601u/src/include/rtmp_dot11.h \
  /home/qqq/mt7601u/src/include/crypt_md5.h \
  /home/qqq/mt7601u/src/include/crypt_sha2.h \
  /home/qqq/mt7601u/src/include/crypt_hmac.h \
  /home/qqq/mt7601u/src/include/rt_config.h \
  /home/qqq/mt7601u/src/include/crypt_aes.h \
  /home/qqq/mt7601u/src/include/crypt_arc4.h \
  /home/qqq/mt7601u/src/include/rtmp.h \
    $(wildcard include/config/t.h) \
  /home/qqq/mt7601u/src/include/spectrum_def.h \
  /home/qqq/mt7601u/src/include/ap_autoChSel_cmm.h \
  /home/qqq/mt7601u/src/include/wsc.h \
    $(wildcard include/config/req.h) \
    $(wildcard include/config/methods.h) \
    $(wildcard include/config/methods/usba.h) \
    $(wildcard include/config/methods/ethernet.h) \
    $(wildcard include/config/methods/label.h) \
    $(wildcard include/config/methods/display.h) \
    $(wildcard include/config/methods/ent.h) \
    $(wildcard include/config/methods/int.h) \
    $(wildcard include/config/methods/nfci.h) \
    $(wildcard include/config/methods/pbc.h) \
    $(wildcard include/config/methods/keypad.h) \
  /home/qqq/mt7601u/src/include/drs_extr.h \
  /home/qqq/mt7601u/src/include/rtmp_M51.h \
  /home/qqq/mt7601u/src/include/rtmp_and.h \
  /home/qqq/mt7601u/src/include/radar.h \
  /home/qqq/mt7601u/src/ate/include/rt_ate.h \
  /home/qqq/mt7601u/src/include/ap.h \
  /home/qqq/mt7601u/src/include/wpa.h \
  /home/qqq/mt7601u/src/include/chlist.h \
  /home/qqq/mt7601u/src/include/spectrum.h \
  /home/qqq/mt7601u/src/include/ap_autoChSel.h \
  /home/qqq/mt7601u/src/include/rt_os_util.h \
  /home/qqq/mt7601u/src/include/rt_os_net.h \
  /home/qqq/mt7601u/src/include/chip/chip_id.h \
  /home/qqq/mt7601u/src/include/uapsd.h \
  /home/qqq/mt7601u/src/include/ap_mbss.h \
  /home/qqq/mt7601u/src/include/ap_ids.h \
  /home/qqq/mt7601u/src/include/ap_cfg.h \
  /home/qqq/mt7601u/src/ate/include/rt_qa.h \
  /home/qqq/mt7601u/src/ate/include/rt_ate.h \
  /home/qqq/mt7601u/src/include/crypt_biginteger.h \
  /home/qqq/mt7601u/src/include/crypt_dh.h \
  /home/qqq/mt7601u/src/include/wsc_tlv.h \
    $(wildcard include/config/error.h) \
    $(wildcard include/config/fail.h) \
  /home/qqq/mt7601u/src/include/mac_ral/fce.h \

/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o: $(deps_/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o)

$(deps_/home/qqq/mt7601u/src/os/linux/../../os/linux/rt_profile.o):
