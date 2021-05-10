//Given two Binary Search Trees, find common nodes in them. In other words,
// find the intersection of two BSTs.

const tree1 = {
  value: 5,
  left: { value: 1, left: { value: 0 }, right: { value: 4 } },
  right: { value: 10, left: { value: 7, right: { value: 9 } } },
};
const tree2 = {
  value: 10,
  left: { value: 7, left: { value: 4 }, right: { value: 9 } },
  right: {
    value: 20,
  },
};

// [4, 7, 9 , 10 ]

const findCommonElements = (tree1, tree2) => {
  return tree1Values(tree1, tree2);
};

const tree1Values = (tree1, tree2, arr = []) => {
  if (tree1.left != null) {
    arr = tree1Values(tree1.left, tree2, arr);
  }
  if (tree1.right != null) {
    arr = tree1Values(tree1.right, tree2, arr);
  }
  arr = searchInTree2(tree1.value, tree2, arr);
  return arr;
};

const searchInTree2 = (t1Value, tree2, arr) => {
  if (t1Value === tree2.value) {
    arr.push(t1Value);
  } else if (t1Value > tree2.value && tree2.right != null) {
    searchInTree2(t1Value, tree2.right, arr);
  } else if (t1Value < tree2.value && tree2.left != null) {
    searchInTree2(t1Value, tree2.left, arr);
  }
  return arr;
};

console.log(findCommonElements(tree1, tree2));
