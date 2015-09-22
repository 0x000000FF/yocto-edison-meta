obj-m := helloworld.o
PWD:= $(shell pwd)
all:
	$(MAKE) -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
modules_install:
	$(MAKE) -C $(KERNEL_SRC) M=$(SRC) modules_install
clean:
	rm -rf *.o *~ core .*.cmd *.mod.c ./tmp_version