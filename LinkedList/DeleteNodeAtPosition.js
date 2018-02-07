//Delete Node At a specific Position

function Node(data, nextNode) {
    this.data = data;
    this.nextNode = nextNode;
}

function LinkedList() {
    this.currNode = null;
}

LinkedList.prototype = {
    addNode: function(data) {
        var newNode = Node(data, this.currNode);
        this.currNode = newNode;
    },
    deleteNode: function(head, pos) {
        if (pos == 0) {
            return head.nextNode;
        }
        head.nextNode = deleteNode(head.nextNode, pos - 1);
        return head;
    }
}