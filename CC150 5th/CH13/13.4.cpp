
struct Test { 
	char * ptr;
};

void shallow_copy(Test & src, Test & dest) {
	dest.ptr = src.ptr;
}
void deep_copy(Test & src, Test & dest){ 
	dest.ptr = malloc(strlen(src.ptr) + 1); memcpy(dest.ptr, src.ptr);
}
#shallow copy, ---> call by reference
#deep copy, ---> call by value

Note that shallow_copy may cause a lot of programming run-time errors, especially with the creation and deletion of objects. 
Shallow copy should be used very carefully and only when a programmer really understands what he wants to do. 
In most cases shallow copy is used when there is a need to pass information about a complex structure without actual duplica- tion of data (e.g., call by reference). 
One must also be careful with destruction of shallow copy.
In real life, shallow copy is rarely used. There is an important programming concept called “smart pointer” that, in some sense, is an enhancement of the shallow copy concept.
Deep copy should be used in most cases, especially when the size of the copied structure is small.
