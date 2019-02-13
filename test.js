class Node {
  constructor(data, nextnode) {
    this.data = data;
    this.nextnode = nextnode;
  }
}

class LinkedList {
  constructor() {
    this.currnode = null;
    this.oddNode = null;
    this.evenNode = null;
  }

  add(data) {
    const newNode = new Node(data, this.currnode);
    this.currnode = newNode;
  }

  separateNode() {
    while (this.currnode) {
      if (this.currnode.data % 2 == 0) {
        const newNode = new Node(this.currnode.data , this.evenNode);
        this.evenNode = newNode;
      } else {
        const newNode = new Node(this.currnode.data , this.oddNode);
        this.oddNode = newNode;
      }
      this.currnode = this.currnode.nextnode;
    }
  }

  print(printNode) {
    while (printNode) {
      console.log(printNode.data);
      printNode = printNode.nextnode;
    }
  }
}

const li = new LinkedList();
li.add(1);
li.add(2);
li.add(3);
li.add(4);
li.add(5);
li.add(6);
li.add(7);
li.separateNode();
li.print(li.oddNode);
li.print(li.evenNode);
