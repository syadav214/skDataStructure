//Traverse binary Tree

class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class Tree {
    constructor() {
        this.currTree = null;
    }

    addNode(data) {
        if (this.currTree == null) {
            this.currTree = new Node(data);
        } else {
            this._addNode(data, this.currTree);
        }
        return this.currTree;
    }

    _addNode(data, node) {
        if (data < node.data) {
            if (node.left != null) {
                this._addNode(data, node.left);
            } else {
                node.left = new Node(data);
            }

        } else {
            if (node.right != null) {
                this._addNode(data, node.right);
            } else {
                node.right = new Node(data);
            }
        }
    }

    printInOrder(node) {
        if (node != null) {
            this.printInOrder(node.left);
            console.log(node.data);
            this.printInOrder(node.right);
        }
    }

    printPreOrder(node) {
        if (node != null) {
            console.log(node.data);
            this.printPreOrder(node.left);
            this.printPreOrder(node.right);
        }
    }

    printPostOrder(node) {
        if (node != null) {
            this.printPostOrder(node.left);
            this.printPostOrder(node.right);
            console.log(node.data);
        }
    }
}


var tr = new Tree();
tr.addNode(20);
tr.addNode(3);
var node = tr.addNode(1);
tr.printInOrder(node);