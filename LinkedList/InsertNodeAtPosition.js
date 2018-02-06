//Insert Node At a specific Position

function Node(data, next) {
    this.data = data;
    this.next = next;
}

function LinkedList(currNode) {
    this.currNode = null;
}

LinkedList.prototype = {
    addNode: function(data) {
        var newNode = new Node(data, this.currNode);
        this.currNode = newNode;
    },
    addNodeAtPos: function(data, head, pos) {
        if (head == null || pos == 0) {
            return new Node(data, head);
        } else {
            var currPos = 1
            var newNode = head
            while (currPos < pos && newNode.next != null) {
                newNode = newNode.next
                currPos++;
            }
            newNode.next = new Node(data, newNode.next)
            return head

        }
    }
}