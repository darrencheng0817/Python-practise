Write a smart pointer class. A smart pointer is a data type, usually implemented with templates, that simulates a pointer while also providing automatic garbage collec- tion. 
It automatically counts the number of references to a SmartPointer<T*> object and frees the object of type T when the reference count hits zero.

In short, the smart pointer is the reference counter for the object, when constructor being called: pointer ++
when equal operater being called: pointer++

Then, if remove called, pointer++
	- if *ref_count ==0:
		delete object


SmartPointer(SmartPointer<T> & sptr) 
{ 
	ref = sptr.ref;
	ref_count = sptr.ref_count; 
	++(*ref_count);
}

void remove()
{
	--(*ref_count); 
	if(*ref_count ==0){
		delete ref; 
		free(ref_count);
		ref = NULL;
		ref_count = NULL; 
	}
}

