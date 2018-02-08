//Print Linked List in reserve order.

using System;

namespace ConsoleApplication1
{
    class Nodes
    {
        public int data;
        public Nodes nextnode;
        public Nodes(int _data, Nodes _nextnode)
        {
            this.data = _data;
            this.nextnode = _nextnode;
        }
    }
    class LinkedList
    {
        Nodes currnode;

        public LinkedList()
        {
            this.currnode = null;
        }

        void Add(int data)
        {
            Nodes _nodes = new Nodes(data, this.currnode);
            this.currnode = _nodes;
        }        

        void PrintReverse(Nodes head)
        {
            if(head!=null)
            {
                PrintReverse(head.nextnode);
                Console.WriteLine(head.data);
            }
        }
    }
}
