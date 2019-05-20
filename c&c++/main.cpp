#include <iostream>
#include <vector>
using namespace std;

//外联
class Mytest{
public:
    Mytest(){
    }
    Mytest(int a);

    void output();

    static int add(int a,int b);

    ~Mytest(){
        cout<<"aaa"<<endl;
    }

};
void Mytest::output() {
    cout<<"bbb"<<endl;
}

int Mytest::add(int a, int b) {
    return  a+b;
}
Mytest::Mytest(int a){

}




class LoadClass{
public:
    void loadClass(){

    }

protected:
    void findClass();
    void define(){
        cout<<"底层调用"<<endl;
    }
};
class MyLoadClass:public LoadClass{
public:
   void loadClass(){
       cout<<"装载"<<endl;
        findClass();
    }

private:
    void findClass(){
        define();
    }
};



class Y{
public:
    ~Y(){
        cout<<"shanchu"<<endl;
    }

};

//智能指针
class Z{
private:
    Y *y;
public:
    Z(Y *y){
        this->y=y;
    }
    ~Z(){
        delete(y);
    }
};

void cereaPoint(){
    Z z=new Y;
}



//继承
class A{
public:
    int a1;
     A(){
      cout<<"creat A"<<endl;
    }

      void xxx(){
        cout<<"AAA"<<endl;
    }
    void aa1(){
        cout<<"a1"<<endl;
    }

    virtual ~A(){
        cout<<"A is die"<<endl;
    }

protected:
    int a2;
    void aa2(){
        cout<<"a2"<<endl;
    }

private:
    int a3;
    void aa3(){
        cout<<"a3"<<endl;
    }
};


class B: public A{
public:

    B():A(){
        cout<<"creat B"<<endl;
    }
      void xxx(){
        cout<<"AAAAAAA"<<endl;
    }
    void *b1;
   void bb1(){
   }
    ~B(){
        cout<<"B is die"<<endl;
    }

protected:
    int b2;
    void bb2(){}

private:
    int b3;
    void bb3(){}

};
class C:public B{
    void test(){

    }
};


int main() {
    Mytest *m1=new Mytest();
    m1->output();
    cout<<m1->add(1,2)<<endl;
    delete(m1);
    std::cout << "Hello, World!" << std::endl;


//    MyLoadClass myLoadClass;
//    myLoadClass.loadClass();

    int arry[4]={1,2,3,4};

    vector<int> v1(arry,arry+4);
//    vector::iterator iterator1;
//    for(iterator1=v1.begin();)

    cereaPoint();

    B *a=new B;
    a->xxx();
    delete(a);

    const char b='a';
//    char * c=const_cast<char *> (b);
//    char * c=(char *)b;
//    char *bbb=const_cast<char *> (b);
//    bbb="aaa";
    const char *ccc= &b;
   char *ddd=(char *)ccc;
    *ddd='b';
   cout << b << "\t" <<*ddd<< endl;





    return 0;
}