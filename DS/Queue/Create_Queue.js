class Queue {
    // Array is used to implement a Queue
    constructor() {
        this.items = [];
    }

    // enqueue function
    enqueue(element) {
        // adding element to the queue
        this.items.push(element);
    }

    // dequeue function
    dequeue() {
        // removing element from the queue
        // returns underflow when called 
        // on empty queue
        if (this.isEmpty())
            return "Underflow";
        return this.items.shift();
    }

    // isEmpty function
    isEmpty() {
        // return true if the queue is empty.
        return this.items.length == 0;
    }

    getQueue() {
        return this.items;
    }
}

var q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);

console.log(q.getQueue());
q.dequeue();
q.dequeue();

console.log(q.getQueue());