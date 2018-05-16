//Insert Node At a specific Position

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

        Nodes InsertNodeAtPos(int data,Nodes head,int Pos)
        {
            if(head == null || Pos == 0)
            {
                return new Nodes(data, head);
            }
            else
            {
                int currPos = 1;
                var newNode = head;
                while(newNode.nextnode !=null && currPos  < Pos)
                {
                    newNode = newNode.nextnode;
                    currPos++;
                }

                currnode.nextnode = new Nodes(data, currnode.nextnode);

                return head;
            }
        }
    }
}
