#include<iostream>
using namespace std;

class node{
    public:
        int data;
        node *next;
};
class Queue{
    public:
        node *front=NULL;
        node *rear=NULL;
        void enqueue();
};

void Queue::enqueue(){
    node *temp;
    temp=new node;
    cout << "Enter no to insert in Queue: ";
    cin>>temp->data;
    if (rear==NULL){
        front=temp;
        rear = temp;
        return;
    }

    e
}

