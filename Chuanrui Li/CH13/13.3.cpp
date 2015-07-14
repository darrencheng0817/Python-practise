
#parent class
class Shape 
{ 
	public:
		int edge_length;

		virtual int circumference () {
			cout << “Circumference of Base Class\n”; 
			return 0;
		}
};

#derived class
class Triangle: public Shape {
	public:
	int circumference () {
		cout<< “Circumference of Triangle Class\n”;
		return 3 * edge_length; 
	}
};


void main() {
	Shape * x = new Shape();
	x->circumference(); // prints “Circumference of Base Class” Shape *y = new Triangle();
	y->circumference(); // prints “Circumference of Triangle Class”
}


#In the above example, circumference is a virtual function in shape class, so it becomes vir- tual in each of the derived classes (triangle, rectangle). 
#C++ non-virtual function calls are resolved at compile time with static binding, while virtual function calls are resolved at run time with dynamic binding.

