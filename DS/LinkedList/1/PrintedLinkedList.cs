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

        void Print()
        {
            Nodes printednode =  this.currnode;
            while(printednode !=null)
            {
                Console.WriteLine(printednode.data);
                printednode = printednode.nextnode;
            }
        }

        public void Main()
        {
            LinkedList li = new LinkedList();
            li.Add(23);
            li.Add(12);
            li.Print();
        }
    }
}
