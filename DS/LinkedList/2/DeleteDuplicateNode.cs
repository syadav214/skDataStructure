//Delete duplicate-value nodes from a sorted linked list

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

        Nodes DeleteDuplicate(Nodes head)
        {
            Nodes node=null;
            if (head != null)
            {
                node = head;
                while (head.nextnode != null)
                {
                    if (head.data == head.nextnode.data)
                    {
                        head.nextnode = head.nextnode.nextnode;
                    }
                    else
                    {
                        head = head.nextnode;
                    }
                }
            }
            return node;
        }
        
        public void Main()
        {
            LinkedList li = new LinkedList();
            li.Add(2);
            li.Add(3);
            Nodes headA = li.Add(3);
            li.Print(headA);
            Nodes headB = li.DeleteDuplicate(headA);
            li.Print(headB);

        }
    }
}
