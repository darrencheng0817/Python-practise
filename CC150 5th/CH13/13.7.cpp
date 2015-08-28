Why does a destructor in the base class need to declared virtual.


----> destructor  need to be virtual

Why?
We want to ensure that the destructor for the most derived class is called



Detailed example;

class Base { public:
Base() { cout << “Base Constructor “ << endl; }
~Base() { cout << “Base Destructor “ << endl; } /* see below */ };

class Derived: public Base { public:
Derived() { cout << ”Derived Constructor “ << endl; }
~Derived() { cout << ”Derived Destructor “ << endl; } };

void main() {
	Base *p = new Derived(); 
	delete p;
}

Output
Base Constructor 
Derived Constructor 
Base Destructor

-----> the derived object does not clear completely

class Base { public:
Base() { cout << “Base Constructor “ << endl; }
virtual ~Base() { cout << “Base Destructor “ << endl; } /* see below */ };

class Derived: public Base { public:
Derived() { cout << ”Derived Constructor “ << endl; }
~Derived() { cout << ”Derived Destructor “ << endl; } };


Output
Base Constructor 
Derived Constructor
Derived Destructor  
Base Destructor




