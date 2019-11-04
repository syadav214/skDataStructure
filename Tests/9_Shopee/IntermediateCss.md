1. How react compare difference
Ans: Filename=> reactExplained.md


2. Diff display none, visibility hidden, and opacity 0
opacity: 0              No     Yes     Yes
visibility: hidden      No     No      No
visibility: collapse    *      No      No
display: none          Yes     No      No

* Yes inside a table element, otherwise No.

3. <style>
    #a {
        background: green;
    }

    .c {
        background: yellow;
    }

    .b {
        background: blue;
    }

    div {
        background: red;
    }
</style>

<div id="a"  class="b c" style="background:black;">
    Hello
</div>

What is the color? : black
Ans: hierachy=> inline, id, class, tag


4. div {
    padding: 10px;
    margin: 20px;
    border: 5px solid black;
    width: 100px;
}

Ans: padding is inside the element. margin is outside the element.
     if border is of 5px, then padding will start from 5px to inwards and margin will start from 0px to outwards.


