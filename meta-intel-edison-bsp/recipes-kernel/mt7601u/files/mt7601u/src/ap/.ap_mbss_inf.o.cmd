cmd_/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o := gcc -Wp,-MD,/home/qqq/mt7601u/src/os/linux/../../ap/.ap_mbss_inf.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/4.6/include -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include -Iarch/x86/include/generated  -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include -Iinclude -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi -Iarch/x86/include/generated/uapi -I/media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi -Iinclude/generated/uapi -include /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kconfig.h   -I/home/qqq/mt7601u/src/os/linux -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m32 -msoft-float -mregparm=3 -freg-struct-return -fno-pic -mpreferred-stack-boundary=2 -march=core2 -mtune=generic -mtune=generic -maccumulate-outgoing-args -Wa,-mtune=generic32 -ffreestanding -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -DCONFIG_AS_AVX=1 -DCONFIG_AS_AVX2=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -Wframe-larger-than=2048 -fno-stack-protector -Wno-unused-but-set-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -g -pg -fno-inline-functions-called-once -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO -DAGGREGATION_SUPPORT -DPIGGYBACK_SUPPORT -DWMM_SUPPORT -DLINUX -Wall -Wstrict-prototypes -Wno-trigraphs -DSYSTEM_LOG_SUPPORT -DRT28xx_MODE=AP -DCHIPSET=7601U -DRESOURCE_PRE_ALLOC   -I/home/qqq/mt7601u/src/include -DCONFIG_AP_SUPPORT -DUAPSD_SUPPORT -DMBSS_SUPPORT -DIAPP_SUPPORT -DDBG -DDOT1X_SUPPORT -DAP_SCAN_SUPPORT -DSCAN_SUPPORT -DHOSTAPD_SUPPORT -DRALINK_ATE -DCONFIG_RT2880_ATE_CMD_NEW   -I/home/qqq/mt7601u/src/ate/include -DRALINK_QA -DWSC_AP_SUPPORT -DWSC_V2_SUPPORT -DDOT11_N_SUPPORT -DDOT11N_DRAFT3 -DSTATS_COUNT_SUPPORT -DOS_ABL_SUPPORT -DOS_ABL_FUNC_SUPPORT -DOS_ABL_OS_PCI_SUPPORT -DOS_ABL_OS_USB_SUPPORT -DOS_ABL_OS_AP_SUPPORT -DOS_ABL_OS_STA_SUPPORT -DEXPORT_SYMTAB -DMT7601U -DMT7601 -DRLT_MAC -DRLT_RF -DRTMP_MAC_USB -DRTMP_USB_SUPPORT -DRTMP_TIMER_TASK_SUPPORT -DRX_DMA_SCATTER -DVCORECAL_SUPPORT -DRTMP_EFUSE_SUPPORT -DNEW_MBSSID_MODE -DRTMP_INTERNAL_TX_ALC -DCONFIG_ANDES_SUPPORT -DDPD_CALIBRATION_SUPPORT -DCONFIG_RX_CSO_SUPPORT  -DMODULE  -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(ap_mbss_inf)"  -D"KBUILD_MODNAME=KBUILD_STR(rtnet7601Uap)" -c -o /home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o /home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.c

source_/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o := /home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.c

deps_/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o := \
  /home/qqq/mt7601u/src/include/rtmp_comm.h \
    $(wildcard include/config/sta/support.h) \
    $(wildcard include/config/ap/support.h) \
    $(wildcard include/config/opmode/on/ap.h) \
    $(wildcard include/config/opmode/on/sta.h) \
    $(wildcard include/config/if/opmode/on/ap.h) \
    $(wildcard include/config/if/opmode/on/sta.h) \
  /home/qqq/mt7601u/src/include/rtmp_type.h \
  /home/qqq/mt7601u/src/include/rtmp_os.h \
  /home/qqq/mt7601u/src/include/os/rt_linux.h \
    $(wildcard include/config/apsta/mixed/support.h) \
    $(wildcard include/config/multi/channel.h) \
    $(wildcard include/config/5vt/enhance.h) \
    $(wildcard include/config/cso/support.h) \
    $(wildcard include/config/rx/cso/support.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/module.h \
    $(wildcard include/config/sysfs.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/unused/symbols.h) \
    $(wildcard include/config/module/sig.h) \
    $(wildcard include/config/generic/bug.h) \
    $(wildcard include/config/kallsyms.h) \
    $(wildcard include/config/smp.h) \
    $(wildcard include/config/tracepoints.h) \
    $(wildcard include/config/tracing.h) \
    $(wildcard include/config/event/tracing.h) \
    $(wildcard include/config/ftrace/mcount/record.h) \
    $(wildcard include/config/module/unload.h) \
    $(wildcard include/config/constructors.h) \
    $(wildcard include/config/debug/set/module/ronx.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/list.h \
    $(wildcard include/config/debug/list.h) \
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
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/x86/32.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/posix_types_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/posix_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/poison.h \
    $(wildcard include/config/illegal/pointer/value.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/const.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/stat.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/stat.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/stat.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/time.h \
    $(wildcard include/config/arch/uses/gettimeoffset.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/cache.h \
    $(wildcard include/config/arch/has/cache/line/size.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kernel.h \
    $(wildcard include/config/preempt/voluntary.h) \
    $(wildcard include/config/debug/atomic/sleep.h) \
    $(wildcard include/config/prove/locking.h) \
    $(wildcard include/config/ring/buffer.h) \
  /usr/lib/gcc/x86_64-linux-gnu/4.6/include/stdarg.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/linkage.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/stringify.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/export.h \
    $(wildcard include/config/have/underscore/symbol/prefix.h) \
    $(wildcard include/config/modversions.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/linkage.h \
    $(wildcard include/config/x86/64.h) \
    $(wildcard include/config/x86/alignment/16.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/bitops.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/bitops.h \
    $(wildcard include/config/x86/cmov.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/alternative.h \
    $(wildcard include/config/paravirt.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/asm.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cpufeature.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/required-features.h \
    $(wildcard include/config/x86/minimum/cpu/family.h) \
    $(wildcard include/config/math/emulation.h) \
    $(wildcard include/config/x86/pae.h) \
    $(wildcard include/config/x86/cmpxchg64.h) \
    $(wildcard include/config/x86/use/3dnow.h) \
    $(wildcard include/config/x86/p6/nop.h) \
    $(wildcard include/config/matom.h) \
    $(wildcard include/config/mslm.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/fls64.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/find.h \
    $(wildcard include/config/generic/find/first/bit.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/sched.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/arch_hweight.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/const_hweight.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/le.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/byteorder.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/byteorder/little_endian.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/byteorder/little_endian.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/swab.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/swab.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/swab.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/byteorder/generic.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bitops/ext2-atomic-setbit.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/log2.h \
    $(wildcard include/config/arch/has/ilog2/u32.h) \
    $(wildcard include/config/arch/has/ilog2/u64.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/typecheck.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/printk.h \
    $(wildcard include/config/early/printk.h) \
    $(wildcard include/config/printk.h) \
    $(wildcard include/config/dynamic/debug.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/init.h \
    $(wildcard include/config/broken/rodata.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kern_levels.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dynamic_debug.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/kernel.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/sysinfo.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/div64.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cache.h \
    $(wildcard include/config/x86/l1/cache/shift.h) \
    $(wildcard include/config/x86/internode/cache/shift.h) \
    $(wildcard include/config/x86/vsmp.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/seqlock.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/spinlock.h \
    $(wildcard include/config/debug/spinlock.h) \
    $(wildcard include/config/generic/lockbreak.h) \
    $(wildcard include/config/preempt.h) \
    $(wildcard include/config/debug/lock/alloc.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/preempt.h \
    $(wildcard include/config/debug/preempt.h) \
    $(wildcard include/config/preempt/tracer.h) \
    $(wildcard include/config/context/tracking.h) \
    $(wildcard include/config/preempt/count.h) \
    $(wildcard include/config/preempt/notifiers.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/thread_info.h \
    $(wildcard include/config/compat.h) \
    $(wildcard include/config/debug/stack/usage.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/bug.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/bug.h \
    $(wildcard include/config/bug.h) \
    $(wildcard include/config/debug/bugverbose.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/bug.h \
    $(wildcard include/config/generic/bug/relative/pointers.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/thread_info.h \
    $(wildcard include/config/ia32/emulation.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/page.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/page_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/page_32_types.h \
    $(wildcard include/config/highmem4g.h) \
    $(wildcard include/config/highmem64g.h) \
    $(wildcard include/config/page/offset.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/page_32.h \
    $(wildcard include/config/hugetlb/page.h) \
    $(wildcard include/config/debug/virtual.h) \
    $(wildcard include/config/flatmem.h) \
    $(wildcard include/config/x86/3dnow.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/string.h \
    $(wildcard include/config/binary/printf.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/string.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/string.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/string_32.h \
    $(wildcard include/config/kmemcheck.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/range.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/memory_model.h \
    $(wildcard include/config/discontigmem.h) \
    $(wildcard include/config/sparsemem/vmemmap.h) \
    $(wildcard include/config/sparsemem.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/getorder.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/processor.h \
    $(wildcard include/config/cc/stackprotector.h) \
    $(wildcard include/config/m486.h) \
    $(wildcard include/config/x86/debugctlmsr.h) \
    $(wildcard include/config/xen.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/processor-flags.h \
    $(wildcard include/config/vm86.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/processor-flags.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/vm86.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/ptrace.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/segment.h \
    $(wildcard include/config/x86/32/lazy/gs.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ptrace.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ptrace-abi.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/ptrace.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/vm86.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/math_emu.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/sigcontext.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/sigcontext.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/current.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/percpu.h \
    $(wildcard include/config/x86/64/smp.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/percpu.h \
    $(wildcard include/config/have/setup/per/cpu/area.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/threads.h \
    $(wildcard include/config/nr/cpus.h) \
    $(wildcard include/config/base/small.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/percpu-defs.h \
    $(wildcard include/config/debug/force/weak/per/cpu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable_types.h \
    $(wildcard include/config/compat/vdso.h) \
    $(wildcard include/config/proc/fs.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable_32_types.h \
    $(wildcard include/config/highmem.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable-3level_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/pgtable-nopud.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/msr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/msr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/msr-index.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/ioctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ioctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/ioctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/ioctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/errno.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/errno.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/errno-base.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cpumask.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/cpumask.h \
    $(wildcard include/config/cpumask/offstack.h) \
    $(wildcard include/config/hotplug/cpu.h) \
    $(wildcard include/config/debug/per/cpu/maps.h) \
    $(wildcard include/config/disable/obsolete/cpumask/functions.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/bitmap.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/errno.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/errno.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/desc_defs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/nops.h \
    $(wildcard include/config/mk7.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/special_insns.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/personality.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/personality.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/math64.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/err.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/irqflags.h \
    $(wildcard include/config/trace/irqflags.h) \
    $(wildcard include/config/irqsoff/tracer.h) \
    $(wildcard include/config/trace/irqflags/support.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/irqflags.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/atomic.h \
    $(wildcard include/config/arch/has/atomic/or.h) \
    $(wildcard include/config/generic/atomic64.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/atomic.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cmpxchg.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cmpxchg_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/atomic64_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/atomic-long.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/bottom_half.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/barrier.h \
    $(wildcard include/config/x86/ppro/fence.h) \
    $(wildcard include/config/x86/oostore.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/spinlock_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/spinlock_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/rwlock.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/lockdep.h \
    $(wildcard include/config/lockdep.h) \
    $(wildcard include/config/lock/stat.h) \
    $(wildcard include/config/prove/rcu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rwlock_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/spinlock.h \
    $(wildcard include/config/paravirt/spinlocks.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/paravirt.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rwlock.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/spinlock_api_smp.h \
    $(wildcard include/config/inline/spin/lock.h) \
    $(wildcard include/config/inline/spin/lock/bh.h) \
    $(wildcard include/config/inline/spin/lock/irq.h) \
    $(wildcard include/config/inline/spin/lock/irqsave.h) \
    $(wildcard include/config/inline/spin/trylock.h) \
    $(wildcard include/config/inline/spin/trylock/bh.h) \
    $(wildcard include/config/uninline/spin/unlock.h) \
    $(wildcard include/config/inline/spin/unlock/bh.h) \
    $(wildcard include/config/inline/spin/unlock/irq.h) \
    $(wildcard include/config/inline/spin/unlock/irqrestore.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rwlock_api_smp.h \
    $(wildcard include/config/inline/read/lock.h) \
    $(wildcard include/config/inline/write/lock.h) \
    $(wildcard include/config/inline/read/lock/bh.h) \
    $(wildcard include/config/inline/write/lock/bh.h) \
    $(wildcard include/config/inline/read/lock/irq.h) \
    $(wildcard include/config/inline/write/lock/irq.h) \
    $(wildcard include/config/inline/read/lock/irqsave.h) \
    $(wildcard include/config/inline/write/lock/irqsave.h) \
    $(wildcard include/config/inline/read/trylock.h) \
    $(wildcard include/config/inline/write/trylock.h) \
    $(wildcard include/config/inline/read/unlock.h) \
    $(wildcard include/config/inline/write/unlock.h) \
    $(wildcard include/config/inline/read/unlock/bh.h) \
    $(wildcard include/config/inline/write/unlock/bh.h) \
    $(wildcard include/config/inline/read/unlock/irq.h) \
    $(wildcard include/config/inline/write/unlock/irq.h) \
    $(wildcard include/config/inline/read/unlock/irqrestore.h) \
    $(wildcard include/config/inline/write/unlock/irqrestore.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/time.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/uidgid.h \
    $(wildcard include/config/uidgid/strict/type/checks.h) \
    $(wildcard include/config/user/ns.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/highuid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kmod.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/gfp.h \
    $(wildcard include/config/numa.h) \
    $(wildcard include/config/zone/dma.h) \
    $(wildcard include/config/zone/dma32.h) \
    $(wildcard include/config/pm/sleep.h) \
    $(wildcard include/config/cma.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mmzone.h \
    $(wildcard include/config/force/max/zoneorder.h) \
    $(wildcard include/config/memory/isolation.h) \
    $(wildcard include/config/memcg.h) \
    $(wildcard include/config/compaction.h) \
    $(wildcard include/config/memory/hotplug.h) \
    $(wildcard include/config/have/memblock/node/map.h) \
    $(wildcard include/config/flat/node/mem/map.h) \
    $(wildcard include/config/no/bootmem.h) \
    $(wildcard include/config/numa/balancing.h) \
    $(wildcard include/config/have/memory/present.h) \
    $(wildcard include/config/have/memoryless/nodes.h) \
    $(wildcard include/config/need/node/memmap/size.h) \
    $(wildcard include/config/need/multiple/nodes.h) \
    $(wildcard include/config/have/arch/early/pfn/to/nid.h) \
    $(wildcard include/config/sparsemem/extreme.h) \
    $(wildcard include/config/have/arch/pfn/valid.h) \
    $(wildcard include/config/nodes/span/other/nodes.h) \
    $(wildcard include/config/holes/in/zone.h) \
    $(wildcard include/config/arch/has/holes/memorymodel.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/wait.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/wait.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/numa.h \
    $(wildcard include/config/nodes/shift.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/nodemask.h \
    $(wildcard include/config/movable/node.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pageblock-flags.h \
    $(wildcard include/config/hugetlb/page/size/variable.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/page-flags-layout.h \
  include/generated/bounds.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/memory_hotplug.h \
    $(wildcard include/config/memory/hotremove.h) \
    $(wildcard include/config/have/arch/nodedata/extension.h) \
    $(wildcard include/config/have/bootmem/info/node.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/notifier.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mutex.h \
    $(wildcard include/config/debug/mutexes.h) \
    $(wildcard include/config/mutex/spin/on/owner.h) \
    $(wildcard include/config/have/arch/mutex/cpu/relax.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mutex-debug.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rwsem.h \
    $(wildcard include/config/rwsem/generic/spinlock.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/rwsem.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/srcu.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rcupdate.h \
    $(wildcard include/config/rcu/torture/test.h) \
    $(wildcard include/config/tree/rcu.h) \
    $(wildcard include/config/tree/preempt/rcu.h) \
    $(wildcard include/config/rcu/trace.h) \
    $(wildcard include/config/preempt/rcu.h) \
    $(wildcard include/config/rcu/user/qs.h) \
    $(wildcard include/config/tiny/rcu.h) \
    $(wildcard include/config/tiny/preempt/rcu.h) \
    $(wildcard include/config/debug/objects/rcu/head.h) \
    $(wildcard include/config/rcu/nocb/cpu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/completion.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/debugobjects.h \
    $(wildcard include/config/debug/objects.h) \
    $(wildcard include/config/debug/objects/free.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rcutree.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/workqueue.h \
    $(wildcard include/config/debug/objects/work.h) \
    $(wildcard include/config/freezer.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/timer.h \
    $(wildcard include/config/timer/stats.h) \
    $(wildcard include/config/debug/objects/timers.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ktime.h \
    $(wildcard include/config/ktime/scalar.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/jiffies.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/timex.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/timex.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/param.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/param.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/param.h \
    $(wildcard include/config/hz.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/param.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/timex.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/tsc.h \
    $(wildcard include/config/x86/tsc.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/topology.h \
    $(wildcard include/config/sched/smt.h) \
    $(wildcard include/config/sched/mc.h) \
    $(wildcard include/config/sched/book.h) \
    $(wildcard include/config/use/percpu/numa/node/id.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/smp.h \
    $(wildcard include/config/use/generic/smp/helpers.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/smp.h \
    $(wildcard include/config/x86/local/apic.h) \
    $(wildcard include/config/x86/io/apic.h) \
    $(wildcard include/config/x86/32/smp.h) \
    $(wildcard include/config/debug/nmi/selftest.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/mpspec.h \
    $(wildcard include/config/x86/numaq.h) \
    $(wildcard include/config/eisa.h) \
    $(wildcard include/config/x86/mpparse.h) \
    $(wildcard include/config/acpi.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/mpspec_def.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/x86_init.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/bootparam.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/screen_info.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/screen_info.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/apm_bios.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/apm_bios.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/edd.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/edd.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/e820.h \
    $(wildcard include/config/efi.h) \
    $(wildcard include/config/hibernation.h) \
    $(wildcard include/config/memtest.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/e820.h \
    $(wildcard include/config/intel/txt.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ioport.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/ist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/video/edid.h \
    $(wildcard include/config/x86.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/video/edid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/apicdef.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/apic.h \
    $(wildcard include/config/x86/x2apic.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pm.h \
    $(wildcard include/config/vt/console/sleep.h) \
    $(wildcard include/config/pm.h) \
    $(wildcard include/config/pm/runtime.h) \
    $(wildcard include/config/pm/clk.h) \
    $(wildcard include/config/pm/generic/domains.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/fixmap.h \
    $(wildcard include/config/paravirt/clock.h) \
    $(wildcard include/config/provide/ohci1394/dma/init.h) \
    $(wildcard include/config/x86/visws/apic.h) \
    $(wildcard include/config/pci/mmconfig.h) \
    $(wildcard include/config/x86/intel/mid.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/acpi.h \
    $(wildcard include/config/acpi/numa.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/acpi/pdc_intel.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/numa.h \
    $(wildcard include/config/numa/emu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/topology.h \
    $(wildcard include/config/x86/ht.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/topology.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/numa_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/mmu.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/realmode.h \
    $(wildcard include/config/acpi/sleep.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/io.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/iomap.h \
    $(wildcard include/config/has/ioport.h) \
    $(wildcard include/config/pci.h) \
    $(wildcard include/config/generic/iomap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/pci_iomap.h \
    $(wildcard include/config/no/generic/pci/ioport/map.h) \
    $(wildcard include/config/generic/pci/iomap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/vmalloc.h \
    $(wildcard include/config/mmu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rbtree.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pvclock.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/clocksource.h \
    $(wildcard include/config/arch/clocksource/data.h) \
    $(wildcard include/config/clocksource/watchdog.h) \
    $(wildcard include/config/clksrc/of.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pvclock-abi.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/kmap_types.h \
    $(wildcard include/config/debug/highmem.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/kmap_types.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/io_apic.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/irq_vectors.h \
    $(wildcard include/config/have/kvm.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/percpu.h \
    $(wildcard include/config/need/per/cpu/embed/first/chunk.h) \
    $(wildcard include/config/need/per/cpu/page/first/chunk.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pfn.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mmdebug.h \
    $(wildcard include/config/debug/vm.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/sysctl.h \
    $(wildcard include/config/sysctl.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/sysctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/elf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/elf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/user.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/user_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/auxvec.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/vdso.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/desc.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ldt.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/elf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/elf-em.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kobject.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/sysfs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kobject_ns.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kref.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/moduleparam.h \
    $(wildcard include/config/alpha.h) \
    $(wildcard include/config/ia64.h) \
    $(wildcard include/config/ppc64.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/tracepoint.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/static_key.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/jump_label.h \
    $(wildcard include/config/jump/label.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/module.h \
    $(wildcard include/config/m586.h) \
    $(wildcard include/config/m586tsc.h) \
    $(wildcard include/config/m586mmx.h) \
    $(wildcard include/config/mcore2.h) \
    $(wildcard include/config/m686.h) \
    $(wildcard include/config/mpentiumii.h) \
    $(wildcard include/config/mpentiumiii.h) \
    $(wildcard include/config/mpentiumm.h) \
    $(wildcard include/config/mpentium4.h) \
    $(wildcard include/config/mk6.h) \
    $(wildcard include/config/mk8.h) \
    $(wildcard include/config/melan.h) \
    $(wildcard include/config/mcrusoe.h) \
    $(wildcard include/config/mefficeon.h) \
    $(wildcard include/config/mwinchipc6.h) \
    $(wildcard include/config/mwinchip3d.h) \
    $(wildcard include/config/mcyrixiii.h) \
    $(wildcard include/config/mviac3/2.h) \
    $(wildcard include/config/mviac7.h) \
    $(wildcard include/config/mgeodegx1.h) \
    $(wildcard include/config/mgeode/lx.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/module.h \
    $(wildcard include/config/have/mod/arch/specific.h) \
    $(wildcard include/config/modules/use/elf/rel.h) \
    $(wildcard include/config/modules/use/elf/rela.h) \
  include/generated/uapi/linux/version.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/slab.h \
    $(wildcard include/config/slab/debug.h) \
    $(wildcard include/config/failslab.h) \
    $(wildcard include/config/slob.h) \
    $(wildcard include/config/slab.h) \
    $(wildcard include/config/slub.h) \
    $(wildcard include/config/debug/slab.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/slub_def.h \
    $(wildcard include/config/slub/stats.h) \
    $(wildcard include/config/memcg/kmem.h) \
    $(wildcard include/config/slub/debug.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kmemleak.h \
    $(wildcard include/config/debug/kmemleak.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/interrupt.h \
    $(wildcard include/config/generic/hardirqs.h) \
    $(wildcard include/config/irq/forced/threading.h) \
    $(wildcard include/config/generic/irq/probe.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/irqreturn.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/irqnr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/irqnr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/hardirq.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ftrace_irq.h \
    $(wildcard include/config/ftrace/nmi/enter.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/vtime.h \
    $(wildcard include/config/virt/cpu/accounting.h) \
    $(wildcard include/config/virt/cpu/accounting/native.h) \
    $(wildcard include/config/virt/cpu/accounting/gen.h) \
    $(wildcard include/config/irq/time/accounting.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/hardirq.h \
    $(wildcard include/config/x86/thermal/vector.h) \
    $(wildcard include/config/x86/mce/threshold.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/irq.h \
    $(wildcard include/config/generic/pending/irq.h) \
    $(wildcard include/config/hardirqs/sw/resend.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/irq.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/irq_regs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/irqdesc.h \
    $(wildcard include/config/irq/preflow/fasteoi.h) \
    $(wildcard include/config/sparse/irq.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/hw_irq.h \
    $(wildcard include/config/irq/remap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/profile.h \
    $(wildcard include/config/profiling.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/sections.h \
    $(wildcard include/config/debug/rodata.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/sections.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/uaccess.h \
    $(wildcard include/config/x86/intel/usercopy.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/smap.h \
    $(wildcard include/config/x86/smap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/uaccess_32.h \
    $(wildcard include/config/debug/strict/user/copy/checks.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/hrtimer.h \
    $(wildcard include/config/high/res/timers.h) \
    $(wildcard include/config/timerfd.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/timerqueue.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pci.h \
    $(wildcard include/config/pci/iov.h) \
    $(wildcard include/config/pcieaspm.h) \
    $(wildcard include/config/pci/msi.h) \
    $(wildcard include/config/pci/ats.h) \
    $(wildcard include/config/pcieportbus.h) \
    $(wildcard include/config/pcieaer.h) \
    $(wildcard include/config/pcie/ecrc.h) \
    $(wildcard include/config/ht/irq.h) \
    $(wildcard include/config/pci/domains.h) \
    $(wildcard include/config/pci/quirks.h) \
    $(wildcard include/config/hotplug/pci.h) \
    $(wildcard include/config/of.h) \
    $(wildcard include/config/eeh.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mod_devicetable.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/uuid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/uuid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/device.h \
    $(wildcard include/config/debug/devres.h) \
    $(wildcard include/config/pinctrl.h) \
    $(wildcard include/config/devtmpfs.h) \
    $(wildcard include/config/sysfs/deprecated.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/klist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pinctrl/devinfo.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ratelimit.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/device.h \
    $(wildcard include/config/x86/dev/dma/ops.h) \
    $(wildcard include/config/intel/iommu.h) \
    $(wildcard include/config/amd/iommu.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pm_wakeup.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/io.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/pci.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/pci_regs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pci_ids.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pci-dma.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dmapool.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/scatterlist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/scatterlist.h \
    $(wildcard include/config/debug/sg.h) \
    $(wildcard include/config/need/sg/dma/length.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pci.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mm.h \
    $(wildcard include/config/ppc.h) \
    $(wildcard include/config/parisc.h) \
    $(wildcard include/config/metag.h) \
    $(wildcard include/config/stack/growsup.h) \
    $(wildcard include/config/transparent/hugepage.h) \
    $(wildcard include/config/ksm.h) \
    $(wildcard include/config/debug/vm/rb.h) \
    $(wildcard include/config/arch/uses/numa/prot/none.h) \
    $(wildcard include/config/debug/pagealloc.h) \
    $(wildcard include/config/hugetlbfs.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/debug_locks.h \
    $(wildcard include/config/debug/locking/api/selftests.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/mm_types.h \
    $(wildcard include/config/split/ptlock/cpus.h) \
    $(wildcard include/config/have/cmpxchg/double.h) \
    $(wildcard include/config/have/aligned/struct/page.h) \
    $(wildcard include/config/want/page/debug/flags.h) \
    $(wildcard include/config/aio.h) \
    $(wildcard include/config/mm/owner.h) \
    $(wildcard include/config/mmu/notifier.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/auxvec.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/auxvec.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/page-debug-flags.h \
    $(wildcard include/config/page/poisoning.h) \
    $(wildcard include/config/page/guard.h) \
    $(wildcard include/config/page/debug/something/else.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/uprobes.h \
    $(wildcard include/config/arch/supports/uprobes.h) \
    $(wildcard include/config/uprobes.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/uprobes.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/bit_spinlock.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/shrinker.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable_32.h \
    $(wildcard include/config/highpte.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/pgtable-3level.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/pgtable.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/page-flags.h \
    $(wildcard include/config/pageflags/extended.h) \
    $(wildcard include/config/arch/uses/pg/uncached.h) \
    $(wildcard include/config/memory/failure.h) \
    $(wildcard include/config/swap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/huge_mm.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/vmstat.h \
    $(wildcard include/config/vm/event/counters.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/vm_event_item.h \
    $(wildcard include/config/migration.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/pci-dma-compat.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dma-mapping.h \
    $(wildcard include/config/has/dma.h) \
    $(wildcard include/config/arch/has/dma/set/coherent/mask.h) \
    $(wildcard include/config/have/dma/attrs.h) \
    $(wildcard include/config/need/dma/map/state.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dma-attrs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dma-direction.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/scatterlist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/dma-mapping.h \
    $(wildcard include/config/isa.h) \
    $(wildcard include/config/x86/dma/remap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kmemcheck.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dma-debug.h \
    $(wildcard include/config/dma/api/debug.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/swiotlb.h \
    $(wildcard include/config/swiotlb.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/swiotlb.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/dma-coherent.h \
    $(wildcard include/config/have/generic/dma/coherent.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dma-contiguous.h \
    $(wildcard include/config/cma/areas.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/dma-mapping-common.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/pci.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/netdevice.h \
    $(wildcard include/config/dcb.h) \
    $(wildcard include/config/wlan.h) \
    $(wildcard include/config/ax25.h) \
    $(wildcard include/config/mac80211/mesh.h) \
    $(wildcard include/config/net/ipip.h) \
    $(wildcard include/config/net/ipgre.h) \
    $(wildcard include/config/ipv6/sit.h) \
    $(wildcard include/config/ipv6/tunnel.h) \
    $(wildcard include/config/rps.h) \
    $(wildcard include/config/netpoll.h) \
    $(wildcard include/config/xps.h) \
    $(wildcard include/config/bql.h) \
    $(wildcard include/config/rfs/accel.h) \
    $(wildcard include/config/fcoe.h) \
    $(wildcard include/config/net/poll/controller.h) \
    $(wildcard include/config/libfcoe.h) \
    $(wildcard include/config/wireless/ext.h) \
    $(wildcard include/config/vlan/8021q.h) \
    $(wildcard include/config/net/dsa.h) \
    $(wildcard include/config/net/ns.h) \
    $(wildcard include/config/netprio/cgroup.h) \
    $(wildcard include/config/net/dsa/tag/dsa.h) \
    $(wildcard include/config/net/dsa/tag/trailer.h) \
    $(wildcard include/config/netpoll/trap.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pm_qos.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/plist.h \
    $(wildcard include/config/debug/pi/list.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/miscdevice.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/major.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/delay.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/delay.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/delay.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rculist.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dmaengine.h \
    $(wildcard include/config/async/tx/enable/channel/switch.h) \
    $(wildcard include/config/rapidio/dma/engine.h) \
    $(wildcard include/config/dma/engine.h) \
    $(wildcard include/config/net/dma.h) \
    $(wildcard include/config/async/tx/dma.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/uio.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/uio.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dynamic_queue_limits.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ethtool.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/compat.h \
    $(wildcard include/config/compat/old/sigaction.h) \
    $(wildcard include/config/odd/rt/sigaction.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/ethtool.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/if_ether.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/skbuff.h \
    $(wildcard include/config/nf/conntrack.h) \
    $(wildcard include/config/bridge/netfilter.h) \
    $(wildcard include/config/nf/defrag/ipv4.h) \
    $(wildcard include/config/nf/defrag/ipv6.h) \
    $(wildcard include/config/xfrm.h) \
    $(wildcard include/config/net/sched.h) \
    $(wildcard include/config/net/cls/act.h) \
    $(wildcard include/config/ipv6/ndisc/nodetype.h) \
    $(wildcard include/config/network/secmark.h) \
    $(wildcard include/config/network/phy/timestamping.h) \
    $(wildcard include/config/netfilter/xt/target/trace.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/net.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/random.h \
    $(wildcard include/config/arch/random.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/random.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/fcntl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/fcntl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/fcntl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/fcntl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/net.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/socket.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/socket.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/socket.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/sockios.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/sockios.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/sockios.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/socket.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/textsearch.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/checksum.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/checksum.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/checksum_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/in6.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/in6.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/netdev_features.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/flow_keys.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/if_ether.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/net_namespace.h \
    $(wildcard include/config/ipv6.h) \
    $(wildcard include/config/ip/sctp.h) \
    $(wildcard include/config/ip/dccp.h) \
    $(wildcard include/config/netfilter.h) \
    $(wildcard include/config/wext/core.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/core.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/mib.h \
    $(wildcard include/config/xfrm/statistics.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/snmp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/snmp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/u64_stats_sync.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/unix.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/packet.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/ipv4.h \
    $(wildcard include/config/ip/multiple/tables.h) \
    $(wildcard include/config/ip/route/classid.h) \
    $(wildcard include/config/security.h) \
    $(wildcard include/config/ip/mroute.h) \
    $(wildcard include/config/ip/mroute/multiple/tables.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/inet_frag.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/percpu_counter.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/ipv6.h \
    $(wildcard include/config/ipv6/multiple/tables.h) \
    $(wildcard include/config/ipv6/mroute.h) \
    $(wildcard include/config/ipv6/mroute/multiple/tables.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/dst_ops.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/sctp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/dccp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/netfilter.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/proc_fs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/fs.h \
    $(wildcard include/config/fs/posix/acl.h) \
    $(wildcard include/config/quota.h) \
    $(wildcard include/config/fsnotify.h) \
    $(wildcard include/config/ima.h) \
    $(wildcard include/config/epoll.h) \
    $(wildcard include/config/debug/writecount.h) \
    $(wildcard include/config/file/locking.h) \
    $(wildcard include/config/auditsyscall.h) \
    $(wildcard include/config/block.h) \
    $(wildcard include/config/fs/xip.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kdev_t.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/kdev_t.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dcache.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rculist_bl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/list_bl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/path.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/radix-tree.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/capability.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/capability.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/semaphore.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/fiemap.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/migrate_mode.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/percpu-rwsem.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/blk_types.h \
    $(wildcard include/config/blk/cgroup.h) \
    $(wildcard include/config/blk/dev/integrity.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/fs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/limits.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/quota.h \
    $(wildcard include/config/quota/netlink/interface.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/dqblk_xfs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dqblk_v1.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dqblk_v2.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/dqblk_qtree.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/projid.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/quota.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/nfs_fs_i.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/netfilter.h \
    $(wildcard include/config/nf/nat/needed.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/if.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/hdlc/ioctl.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/in.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/in.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/netfilter.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/flow.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/x_tables.h \
    $(wildcard include/config/bridge/nf/ebtables.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/conntrack.h \
    $(wildcard include/config/nf/conntrack/proc/compat.h) \
    $(wildcard include/config/nf/conntrack/labels.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/list_nulls.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/netfilter/nf_conntrack_tcp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/netfilter/nf_conntrack_tcp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netns/xfrm.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/xfrm.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/seq_file_net.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/seq_file.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/dsa.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/netprio_cgroup.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/cgroup.h \
    $(wildcard include/config/cgroups.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/sched.h \
    $(wildcard include/config/sched/debug.h) \
    $(wildcard include/config/no/hz/common.h) \
    $(wildcard include/config/lockup/detector.h) \
    $(wildcard include/config/core/dump/default/elf/headers.h) \
    $(wildcard include/config/sched/autogroup.h) \
    $(wildcard include/config/bsd/process/acct.h) \
    $(wildcard include/config/taskstats.h) \
    $(wildcard include/config/audit.h) \
    $(wildcard include/config/inotify/user.h) \
    $(wildcard include/config/fanotify.h) \
    $(wildcard include/config/posix/mqueue.h) \
    $(wildcard include/config/keys.h) \
    $(wildcard include/config/perf/events.h) \
    $(wildcard include/config/schedstats.h) \
    $(wildcard include/config/task/delay/acct.h) \
    $(wildcard include/config/fair/group/sched.h) \
    $(wildcard include/config/rt/group/sched.h) \
    $(wildcard include/config/cgroup/sched.h) \
    $(wildcard include/config/blk/dev/io/trace.h) \
    $(wildcard include/config/rcu/boost.h) \
    $(wildcard include/config/compat/brk.h) \
    $(wildcard include/config/sysvipc.h) \
    $(wildcard include/config/detect/hung/task.h) \
    $(wildcard include/config/rt/mutexes.h) \
    $(wildcard include/config/task/xacct.h) \
    $(wildcard include/config/cpusets.h) \
    $(wildcard include/config/futex.h) \
    $(wildcard include/config/fault/injection.h) \
    $(wildcard include/config/latencytop.h) \
    $(wildcard include/config/function/graph/tracer.h) \
    $(wildcard include/config/have/hw/breakpoint.h) \
    $(wildcard include/config/bcache.h) \
    $(wildcard include/config/have/unstable/sched/clock.h) \
    $(wildcard include/config/no/hz/full.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/sched.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/cputime.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/cputime.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/cputime_jiffies.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/sem.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/sem.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ipc.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/ipc.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/ipcbuf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/ipcbuf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/sembuf.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/signal.h \
    $(wildcard include/config/old/sigaction.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/signal.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/signal.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/signal.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/signal-defs.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/siginfo.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/siginfo.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/siginfo.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/proportions.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/seccomp.h \
    $(wildcard include/config/seccomp.h) \
    $(wildcard include/config/seccomp/filter.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/seccomp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/rtmutex.h \
    $(wildcard include/config/debug/rt/mutexes.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/resource.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/resource.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/resource.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/asm-generic/resource.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/asm-generic/resource.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/task_io_accounting.h \
    $(wildcard include/config/task/io/accounting.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/latencytop.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/cred.h \
    $(wildcard include/config/debug/credentials.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/key.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/selinux.h \
    $(wildcard include/config/security/selinux.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/llist.h \
    $(wildcard include/config/arch/have/nmi/safe/cmpxchg.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/cgroupstats.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/taskstats.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/prio_heap.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/idr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/xattr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/xattr.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/cgroup_subsys.h \
    $(wildcard include/config/cgroup/debug.h) \
    $(wildcard include/config/cgroup/cpuacct.h) \
    $(wildcard include/config/cgroup/device.h) \
    $(wildcard include/config/cgroup/freezer.h) \
    $(wildcard include/config/net/cls/cgroup.h) \
    $(wildcard include/config/cgroup/perf.h) \
    $(wildcard include/config/cgroup/hugetlb.h) \
    $(wildcard include/config/cgroup/bcache.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/neighbour.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/netlink.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/scm.h \
    $(wildcard include/config/security/network.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/security.h \
    $(wildcard include/config/security/path.h) \
    $(wildcard include/config/security/network/xfrm.h) \
    $(wildcard include/config/securityfs.h) \
    $(wildcard include/config/security/yama.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/nsproxy.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/netlink.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/netdevice.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/if_packet.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/if_link.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/if_link.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/etherdevice.h \
    $(wildcard include/config/have/efficient/unaligned/access.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/unaligned.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/unaligned/access_ok.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/unaligned/generic.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/wireless.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/wireless.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/if_arp.h \
    $(wildcard include/config/firewire/net.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/if_arp.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/ctype.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/usb.h \
    $(wildcard include/config/usb/mon.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/usb/ch9.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/usb/ch9.h \
    $(wildcard include/config/size.h) \
    $(wildcard include/config/att/one.h) \
    $(wildcard include/config/att/selfpower.h) \
    $(wildcard include/config/att/wakeup.h) \
    $(wildcard include/config/att/battery.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/pm_runtime.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/net/iw_handler.h \
    $(wildcard include/config/wext/priv.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/uapi/linux/unistd.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/asm/unistd.h \
    $(wildcard include/config/x86/x32/abi.h) \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/arch/x86/include/uapi/asm/unistd.h \
  arch/x86/include/generated/uapi/asm/unistd_32.h \
  /media/7ac7050f-caf1-4213-98be-fa898f57e4f0/edison-src/out/linux64/build/tmp/work/edison-poky-linux/linux-yocto/3.10.17-r0/linux/include/linux/kthread.h \
  /home/qqq/mt7601u/src/include/os/rt_linux_cmm.h \
  /home/qqq/mt7601u/src/include/os/rt_os.h \
  /home/qqq/mt7601u/src/include/link_list.h \
  /home/qqq/mt7601u/src/include/rtmp_cmd.h \
    $(wildcard include/config/value.h) \
    $(wildcard include/config/init.h) \
  /home/qqq/mt7601u/src/include/iface/iface_util.h \
  /home/qqq/mt7601u/src/include/rt_os_util.h \
  /home/qqq/mt7601u/src/include/rt_os_net.h \
  /home/qqq/mt7601u/src/include/chip/chip_id.h \

/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o: $(deps_/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o)

$(deps_/home/qqq/mt7601u/src/os/linux/../../ap/ap_mbss_inf.o):
