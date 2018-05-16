class Stack {
    constructor() {
        this.items = [];
    }

    push(element) {
        this.items.push(element);
    }

    pop() {
        if (this.items.length == 0) {
            return "Underflow";
        }
        return this.items.pop();
    }

    peek() {
        return this.items[this.items.length - 1];
    }

    printStack() {
        var str = "";
        for (var i = 0; i < this.items.length; i++)
            str += this.items[i] + " ";
        return str;
    }
}

// creating object for stack class
var stack = new Stack();
stack.push(10);
stack.push(20);
stack.push(30);
console.log(stack.printStack());

console.log("Peek", stack.peek());

console.log("Pop", stack.pop());

console.log(stack.printStack());