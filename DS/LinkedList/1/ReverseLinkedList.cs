//Reverse the LinkedList
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

        void ReverseList()
        {
            Nodes prev_node = null;
            var currentHead = this.currnode;
            while(currentHead!=null)
            {
                var curr_prev_node = prev_node;
                var curr_currHead_next = currentHead.nextnode;

                prev_node = currentHead;
                currentHead.nextnode = curr_prev_node;
                currentHead = curr_currHead_next;
            }
            this.currnode = prev_node;
        }

        void Print()
        {
            Nodes printednode = this.currnode;
            while (printednode != null)
            {
                Console.WriteLine(printednode.data);
                printednode = printednode.nextnode;
            }
        }   
        
        public void Main()
        {
            LinkedList li = new LinkedList();
            li.Add(2);
            li.Add(12);
            li.Add(21);
            li.ReverseList();
            li.Print();
        }
    }
}
