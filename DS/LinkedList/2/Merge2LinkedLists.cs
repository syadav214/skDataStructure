//Merge 2 Linked List

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

        Nodes MergeList(Nodes headA, Nodes headB)
        {
            if (headA == null && headB == null)
                return null;
            else if (headA == null)
                return headB;
            else if (headB == null)
                return headA;

            if(headA.data> headB.data)
            {
                headB.nextnode = MergeList(headA, headB.nextnode);
                return headB;
            }
            else
            {
                headA.nextnode = MergeList(headA.nextnode, headB);
                return headA;
            }
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


        void PrintReverse(Nodes head)
        {
            if (head != null)
            {
                PrintReverse(head.nextnode);
                Console.WriteLine(head.data);
            }
        }

        Nodes InsertNodeAtPos(int data, Nodes head, int Pos)
        {
            if (head == null || Pos == 0)
            {
                return new Nodes(data, head);
            }
            else
            {
                int currPos = 1;
                var newNode = head;
                while (newNode.nextnode != null && currPos < Pos)
                {
                    newNode = newNode.nextnode;
                    currPos++;
                }

                currnode.nextnode = new Nodes(data, currnode.nextnode);

                return head;
            }
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
            Nodes headA= li.Add(10);

            LinkedList li2 = new LinkedList();
            li2.Add(4);
            Nodes headB = li2.Add(20);

            li2.currnode = li2.MergeList(headA, headB);
            li2.Print();
        }
    }
}
