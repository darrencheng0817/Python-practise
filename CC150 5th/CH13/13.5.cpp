Volatile informs the compiler that the value of the variable can change from the outside, without any update done by the code.
This can be done by Operating system, hardware and other threads. So the value can change unexpectedly.
Therefore, compiler will reloaf the value each time.

In short, the volatile value may be change by the low level operations. So compiler do not optimize the 
user level code to prevent some errors happens

Several cases
Declaring a simple volatile variable:
volatile int x; int volatile x;
Declaring a pointer variable for a volatile memory (only the pointer address is volatile):
volatile int * x; int volatile * x;
Declaring a volatile pointer variable for a non-volatile memory (only memory contained is volatile):
int * volatile x;
Declaring a volatile variable pointer for a volatile memory (both pointer address and memo- ry contained are volatile):
volatile int * volatile x; int volatile * volatile x;


Detailed example for the volatile:
Volatile variables are not optimized, but this can actually be useful. Imagine this function:

int opt=1; 
void Fn(void) {
	start:
	if (opt == 1) goto start; 
	else break;
At first glance, our code appears to loop infinitely. The compiler will try to optimize it to:
}

void Fn(void) { 
	start:
	int opt = 1; 
	if (true) goto start;
}
This becomes an infinite loop. However, an external program might write ‘0’ to the location of variable opt. 
Volatile variables are also useful when multi-threaded programs have global variables and any thread can modify these shared variables. 
Of course, we don’t want opti- mization on them.