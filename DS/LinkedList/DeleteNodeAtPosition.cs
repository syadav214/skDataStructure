//Delete Node At a specific Position

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

        Nodes DeleteNodeAtPos(Nodes head,int Pos)
        {
            if(Pos == 0)
            {
                return head.nextnode;
            }

            head.nextnode = DeleteNodeAtPos(head.nextnode,Pos-1);
            return head;
        }
    }
}
