#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	
	//first part is about the pointer
	int * p = new int;
	*p = 7;
	int *q = p;
	*p = 8;
	cout << *q; //prints 8 
		
	//comments
	//q and p point to the same object, so they both change the value of the same data blocks
	
	//second part is about the reference
	int a = 5;
	int & b = a;
	b = 7;
	cout << a; //prints 7
	
	//comments
	//A reference is the alias for a pre-exsiting object and it does not have memory of its own
	
	//so in this case, a is the temporary variable and memory is on the stack, B is alias of the same object.
	//This is similar to the pointers
	 
	//Detailed explainations
	//A reference is an entity that is an alias for another object.

	//A reference is not a variable as a variable is only introduced by the declaration of an object. An object is a region of storage and, in C++, references do not (necessarily) take up any storage.
	//As objects and references are distinct groups of entities in C++ so the term "reference variable" isn't meaningful.
	
	
	//third part is about pointer arithmetic
	int * p = new int[2];
	p[0] = 0;
	p[0] = 1;
	p++; //p is increment by size of int byte, rather than just 1 byte
	cout << *p //output is 1
	
	
	
	//Template are a way of reusing code to apply the same class to different data types. We might have a list-like data structure.
	SAME CLASS -> DIFFERENT DATA TYPE
	
	template <class T>
	class Shiftedlist{
		//this public elements in the class
		//data type is not defined at this stage
		T* array;
		int offset, size;
		
		public: ShiftedList(int sz): offset(0), size(sz){
			array = new T[size]
		}
	}
	
	
	int main(){
		//In the main, we define the integer type
		int size = 4
		Shiftedlist<int> * list = new shiftedList<int>(size)
		//this will call the template
	}
	
	
	
	
	
	
}