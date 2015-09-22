
#include <linux/module.h>//与module相关的信息
 
#include <linux/kernel.h>
#include <linux/init.h>      //与init相关的函数
 
static int __init hellokernel_init(void)
{
        printk(KERN_INFO "Hello kernel!\n");
        return 0;
}
 
static void __exit hellokernel_exit(void)
{
        printk(KERN_INFO "Exit kernel!\n");
}

module_init(hellokernel_init);
module_exit(hellokernel_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("xxxx");