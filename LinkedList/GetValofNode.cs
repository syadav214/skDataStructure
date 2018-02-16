// Find the node at the given position counting backwards from the tail
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

        Nodes Add(int data)
        {
            Nodes _nodes = new Nodes(data, this.currnode);
            this.currnode = _nodes;
            return this.currnode;
        }

        void GetVal(Nodes head,int pos)
        {
            int currpos = 0;
            Nodes temphead = head;
            while(temphead!=null)
            {
                if(currpos > pos)
                {
                    temphead = temphead.nextnode;
                }
                currpos++;
                head = head.nextnode;
            }
            Console.Write(temphead.data);
        }
    }
}
