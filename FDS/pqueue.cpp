#include<iostream>
using namespace std;

class node{
    int data;
    node *next;
};
class Queue{
    public:
        node *head;
        node **top;
        node **rear;
        void create();
};

void Queue::create()

