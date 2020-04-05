#include <iostream>
using namespace std;


#define DLLEXPORT extern "C" __declspec(dllexport)


void fname(string n) {
    cout << n << endl;
}

DLLEXPORT int sum(int a, int b) {
    return a + b;
}

DLLEXPORT void show(char* s) {
    fname("~~show~~");
    cout << s << endl;
}

DLLEXPORT void see(char* s, wchar_t *wt) {
    fname("~~see~~");
    cout << s << endl;
    wcout << wt << endl;
}


DLLEXPORT void view(char* s) {
    cout << "~~ view ~~" << endl;
    cout << s << endl;
}


DLLEXPORT void combine(char* name, float price) {
    cout << "~~ combine ~~" << endl;
    cout << name << " - $" << price << endl;
}

DLLEXPORT char* append(char* s) {
    cout << "~~ append ~~" << endl;
    return s;
}


DLLEXPORT void ref(int& i) {
    cout << "~~ ref ~~" << endl;
    i = 99;
}


struct Person
{
    char* name;
    int age;
    void show() {
        cout << "~~ show ~~" << endl;
        cout << age << endl;
        cout << name << endl;
    }
};

DLLEXPORT void stru(Person person) {
    cout << "~~ stru ~~" << endl;
    cout << person.age << endl;
    cout << person.name << endl;
    person.show();
}

DLLEXPORT void strus(Person person[]) {
    cout << "~~ strus ~~" << endl;

    for (int i = 0; i < 2; i++)
    {
        cout << person[i].age << endl;
        cout << person[i].name << endl;
    }
    
}

DLLEXPORT void poi(int* p) {
    cout << "~~ poi ~~" << endl;
    cout << *p << endl;
    *p = 82;
    cout << *p << endl;
}



DLLEXPORT void marr(int* p) {
    cout << "~~ marr ~~" << endl;
    cout << p[1] << endl;
    p[1] = 89;
    cout << p[1] << endl;
}

DLLEXPORT void ints(int arr[]) {
    cout << "~~ arr ~~" << endl;
    cout << arr[1] << endl;
    arr[1] = 89;
    cout << arr[1] << endl;
}


DLLEXPORT int num =10;
DLLEXPORT const char*  s = "xxxxxxxxx";

DLLEXPORT void vari(char* si, int ii) {
    cout << "~~ vari ~~" << endl;
    cout << num << endl;
    cout << s << endl;
    cout << ii << endl;
    cout << si << endl;
}

typedef int (*PF)(int);

DLLEXPORT void funp(PF pf) {
    cout << "~~ funp ~~" << endl;

    int n = pf(24);
    cout << n << endl;
}

typedef void (*PFO)(int);

DLLEXPORT void funpo(PFO pf) {
    cout << "~~ funpo ~~" << endl;

    pf(24);
}



class Car {
public:
    float price;
    char* name;

    Car() {
        cout << "++ Car ++" << endl;
        this->name = "NNNN";
        this->price = 0.00;
    }

    Car(float price, char* name) {
        cout << "++ Car1 ++" << endl;
        this->name = name;
        this->price = price;
    }

    ~Car() {
        cout << "-- Car --" << endl;
    }

    void show() {
        cout << "~~ show ~~" << endl;
        cout << this->name << endl;
        cout << this->price << endl;
    }
};


DLLEXPORT void clas(Car c) {
    cout << "~~ clas ~~" << endl;
    c.show();
}