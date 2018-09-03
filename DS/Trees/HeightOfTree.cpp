// Get height of a tree
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Node
{
  public:
    int data;
    Node *left;
    Node *right;
    Node(int d)
    {
        data = d;
        left = NULL;
        right = NULL;
    }
};

class Solution
{
  public:
    Node *insert(Node *root, int data)
    {
        if (root == NULL)
        {
            return new Node(data);
        }
        else
        {
            Node *cur;
            if (data <= root->data)
            {
                cur = insert(root->left, data);
                root->left = cur;
            }
            else
            {
                cur = insert(root->right, data);
                root->right = cur;
            }

            return root;
        }
    }

    int height(Node *root)
    {
        if (root == NULL)
            return -1;

        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        if (leftHeight > rightHeight)
            return leftHeight + 1;

        else
            return rightHeight + 1;
    }
};

int main()
{
    Solution myTree;
    Node *root = NULL;

    int t;
    int data;

    cin >> t;

    while (t-- > 0)
    {
        cin >> data;
        root = myTree.insert(root, data);
    }

    int height = myTree.height(root);

    cout << "Height: " << height << endl;
    return 0;
}
