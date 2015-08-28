Write a function in C called my2DAIIoc which allocates a two-dimensional array. 

vertical: array of pointer, horizontal array of data blocks

int** my2DAlloc(int rows, in t cols) {
	int** rowptr;
	int i;
	rowptr = (int**) malloc(rows * sizeof(int*)); 
	for(i=0;i<rows;i++) {
		rowptrf[i] = (int*) malloc(cols * sizeof(int));
	}
	return rowptr;
}


void my2DDealloc(int** rowptr, int rows){ 
	for (i =0;i <rows; i++){
		free(rowptr[i]); 
	}
	free (rowptr);



different apporach

[pt1][pt2][D1][D2][D3][D1][D2][D3]
1	 2	  3	  4	  5   6   7   8
memory is in a contiguous block
[pt1] -> starting position of 4
[pt2] -> starting position of 6

int** my2DAlloc(int rows, int cols){ 
	int i;
	int header = rows * sizeof(int*);
	int data = rows * cols * sizeof(int);
	int** rowptr = (int**)malloc(header + data); 
	if (rowptr ==NULL) {
		return NULL;
		
	#position the array pointers
	int* buf = (int*) (rowptr + rows); 
	for(i=0;i<rows;i++){ 
		rowptrfi] = buf + i * cols;
	}
	return rowptr; 
}




