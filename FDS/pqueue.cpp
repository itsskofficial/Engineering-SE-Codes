#include<iostream>
using namespace std;

class node{
    public:
        int data;
        node *next;
};
class Queue{
    public:
        node *top=NULL;
        node *rear=NULL;
        void enqueue();
};

void Queue::enqueue(){
    node *temp;
    temp=new node;

}

