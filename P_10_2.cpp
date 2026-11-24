#include<iostream>
using namespace std;

    struct displaySize
    {
        int age;
        float ht;
        char m;
        char wt;
    };
    struct sizeDisplay//making two struct of same dataypes to show the difference of size in both due to order difference
    {
        char m;
        int age;
        char wt;
        float ht;

    };

    union typeUnion
    {
        int age;
        float ht;
        char m;
    };

    void displayUnion(const typeUnion &u)//will be used repeatedly after assigning value to one variable
    {
        cout<<"age : "<<u.age<<endl;
        cout<<"ht : "<<u.ht<<endl;
        cout<<"m : "<<u.m<<endl;
    }

    int main()
    {
        displaySize s;

        cout<<"*************************************************"<<endl;
        cout<<"COMPOSITE DATA REPRESENTATION ANALYZER"<<endl;
        cout<<"*************************************************"<<endl;

        cout<<"Part A – Composite Data Representation (Structure)"<<endl;
        cout<<"Size of 'int' : "<<sizeof(s.age)<<endl;
        cout<<"Size of 'float' "<<sizeof(s.ht)<<endl;
        cout<<"Size of 'char' : "<<sizeof(s.m)<<endl;
        cout<<"Size of structure 1 : "<<sizeof(s)<<endl<<endl;

        cout<<"-----------------------------------------------"<<endl;

        cout<<"Part B – Padding and Alignment (Structure)"<<endl;
        sizeDisplay d;
        cout<<"Size of structure 1: "<<sizeof(s)<<"bytes"<<endl;//12
        cout<<"Size of structure 2: "<<sizeof(d)<<"bytes"<<endl<<endl;//16

        cout<<"-----------------------------------------------"<<endl;
        cout<<"Padding and Alignment Observed "<<endl;//both sizes are different due to diff order of dataypes
        cout<<"-----------------------------------------------"<<endl;

        cout<<"Part C – Shared Memory Composite Data Representation (Union)"<<endl;
        typeUnion u;

        cout<<"Size of Union : "<<sizeof(u)<<"bytes"<<endl;//size of the union

        u.age = 17;//assigning value to one variable of union
        cout<<"After storing age= 17 : "<<endl;
        displayUnion(u);//calling the function and printing value of every variable of union

        cout<<"-----------------------------------------------"<<endl;

        u.ht = 15.6;//assigning another value to another variable
        cout<<"After storing ht = 15.6 : "<<endl;
        displayUnion(u);//will display ht value correctly but now age value will be wrong as ht overwritten it

        cout<<"-----------------------------------------------"<<endl;

        u.m = 'A';
        cout<<"After storing m = A : "<<endl;
        displayUnion(u);//will display m value correctly but now ht value will be wrong as m again overwritten it

        cout<<"-----------------------------------------------"<<endl;

        cout<<"Part D – Trade-off Analysis (Structure vs Union)"<<endl;
        cout<<"Structure : Separate Memory for Every Member"<<endl<<"\t Suitable for Storing Complete Records"<<endl<<endl;
        cout<<"Union : Shared Memory for All Members."<<endl<<"\t Suitable for Memory-efficient Applications"<<endl<<endl;

        cout<<"-----------------------------------------------"<<endl;
        cout<<"Program Executed Successfully";



    }
