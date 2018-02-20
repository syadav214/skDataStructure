//To check if a node is visited

using System;
using System.Collections.Generic;

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

        bool hasCycle(Nodes head)
        {
            if (head == null)
                return false;

            bool ret = false;
            Nodes node = head;
            var flag = 0;
            List<Nodes> visitedNode= new List<Nodes>();

            while (head !=null)
            {
                if(visitedNode.Contains(node))
                {
                    flag = 1;
                    ret = true;
                    break;
                } 
                else
                {
                    visitedNode.Add(head);
                }
                head = head.nextnode;
            }

            if(flag==0)
            {
                ret = false;
            }
            return ret;
        }
 
        
        public void Main()
        {
            LinkedList li = new LinkedList();
            li.Add(2);
            li.Add(3);
            Nodes headA = li.Add(3);
            li.Print(headA);
            Console.Write(li.hasCycle(headA));
        }
    }
}
