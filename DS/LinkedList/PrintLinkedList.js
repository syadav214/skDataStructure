class Node {
    constructor(data,next) {
      this.data = data;
      this.next = next;
    }
  }
  
  class LinkedList {
    constructor(currNode) {
      this.currNode = null;
    }
  
    addNode(data) {
      const nd = new Node(data,this.currNode);
      this.currNode = nd;
      return this.currNode;
    }
  
    printNode(nodes) {
      while(nodes) {
        console.log(nodes.data);
        nodes = nodes.next;
      }
    }
  }
  
  const li = new LinkedList();
  li.addNode(11);
  li.addNode(12);
  const pNode = li.addNode(13);
  li.printNode(pNode);
  