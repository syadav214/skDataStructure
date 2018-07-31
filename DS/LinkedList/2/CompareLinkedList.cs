//Compare Linked List
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

        int Compare(Nodes headA,Nodes headB)
        {
            if(headA == null || headB==null)
            {
                return 0;
            }
            else
            {
                var unmatched = 0;
                while(headA !=null &&  headB != null)
                {
                    if(headA.data != headB.data)
                    {
                        unmatched = 1;
                    }
                    headA = headA.nextnode;
                    headB = headB.nextnode;
                }

                if(unmatched==1)
                {
                    return 0;
                }
                else
                {
                    if(headA == null && headB !=null)
                    {
                        return 0;
                    }
                    else if(headB == null && headA !=null)
                    {
                        return 0;
                    }
                    else
                    {
                        return 1;
                    }
                }
            }
        }

    }
}
