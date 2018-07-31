//  g++ -std=c++11 test.cpp for c++ 11 syntaxes such as

#include <iostream>
using namespace std;

class DoublyLinkedListNode
{
  public:
    int data;
    DoublyLinkedListNode *next;
    DoublyLinkedListNode *prev;

    DoublyLinkedListNode(int node_data)
    {
        this->data = node_data;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

class DoublyLinkedList
{
  public:
    DoublyLinkedListNode *head;
    DoublyLinkedListNode *tail;

    DoublyLinkedList()
    {
        this->head = nullptr;
        this->tail = nullptr;
    }

    void insertNode(int node_data)
    {
        DoublyLinkedListNode *node = new DoublyLinkedListNode(node_data);
        if (!this->head)
        {
            this->head = node;
        }
        else
        {
            this->tail->next = node;
            node->prev = this->tail;
        }

        this->tail = node;
    }

    void print_doubly_linked_list(string sep)
    {
        DoublyLinkedListNode *node = this->head;
        while (node)
        {
            cout << " node=> " << node->data;

            node = node->next;

            if (node)
            {
                cout << " sep=> " << sep;
            }
        }
    }

    DoublyLinkedListNode *SortedInsert(DoublyLinkedListNode *head, int data)
    {
        DoublyLinkedListNode *temp = head;

        //Initializing the new Node
        DoublyLinkedListNode *newNode = new DoublyLinkedListNode(data);

        // If thr List is empty point the head to the new node
        if (temp == NULL)
        {
            temp = newNode;
            head = temp;
            return head;
        }

        //Check if the data in the new node is bigger
        // or smaller than each node in the list. if it's
        // bigger, move to the next node in the list.
        // If it's the last node stop.
        while ((newNode->data > temp->data) && temp->next != NULL)
        {
            temp = temp->next;
        }

        //If it was the last node and the data is still
        //bigger this new node will be added to the tail
        if (temp->next == NULL && newNode->data > temp->data)
        {
            newNode->prev = temp;
            temp->next = newNode;
            return head;
        }

        //If this was smaller than the node pointed by temp
        //we add new node before it
        newNode->prev = temp->prev;
        temp->prev = newNode;
        newNode->next = temp;

        //If there are elements before we need to link its
        //next to our new node
        if (newNode->prev != NULL)
        {
            newNode->prev->next = newNode;
        }

        //If there are no elements before it, our node
        //is the first one so we point the head/temp to it
        if (newNode->prev == NULL)
        {
            temp = newNode;
            return temp;
        }

        return head;
    }
};

int main()
{
    DoublyLinkedList *node = new DoublyLinkedList();
    node->insertNode(5);
    node->insertNode(15);
    node->print_doubly_linked_list("|");
    cout
        << "hello";
    return 0;
}
