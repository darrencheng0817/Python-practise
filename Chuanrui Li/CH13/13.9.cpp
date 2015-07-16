Write an aligned malloc and free function that supports allocating memory such that the memory address returned is divisible by a specific power of two

Memory allocation:
required_bytes --> (actual size of memory needed) + offset --> (for the alignment issue)

void* aligned_malloc(size_t required_bytes, size_t alignment) 
{ 	
	int offset = alignment - 1;
	void* p = (void*) malloc(required_bytes + offset);
	# mask the value in order to divisible by alignment
	void* q = (void*) (((size_t)(p) + offset) & -(alignment - 1)); 
	return q;
}



Free Memory:

	step 1 -> storing the starting address of the memory block
	p2->[p1]
	p1->[required_bytes ]

	step 2
	p2->[p1]
	[]

void* aligned_malloc(size_t required_bytes size_t alignment){
	void* p1; // original block
	void** p2; // aligned block
	int offset = alignment - 1 + sizeof(void*);
	if ((p1 = (void*)malloc(required_bytes + offset)) == NULL) {
		return NULL;
	}

	p2 = (void**)malloc(((size_t)(p1) + offset) & -(alignment - 1)); 
	P2[-1] = p1;
	return p2;
}



void aligned_free(void *p2) {
	/* for consistency., we use the same names as aligned_malloc*/.
	void* p1 = ((void**)p2)[-1];
	free(p1);
}






