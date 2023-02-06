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
        void dequeue();
        void display();
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

    rear->next=temp;
    rear = temp;
}

void Queue::dequeue(){
    if (front==NULL){
        return;
    }

    node *temp=front;
    int min = temp->data;
    front=front->next;

    if (front==NULL){
        rear = NULL;
    }

    delete temp;
}

void Queue::display(){
    node *temp=front;
    while(temp!=rear){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<temp->data;
}
