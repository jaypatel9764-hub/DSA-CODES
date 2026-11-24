#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node* left;
    Node* right;
};
class Binary
{
private:
    Node* root;
public:
    Binary()
    {
        root= NULL;
    }
    Node* create()
    {
        int value;
        cout<<"Enter node value(-1 for no node): ";
        cin>>value;
        if(value==-1)
            return NULL;
        Node* newNode= new Node();
        newNode->data= value;
        cout<<"Enter left child of "<<value<<endl;
        newNode->left= create();    
        cout<<"Enter right child of "<<value<<endl;    
        newNode->right= create();
        return newNode;
    }
void build()
{
    cout<<"\nCreate a binary tree:\n";
    root= create();
}
void inorder(Node* temp)
{
    if(temp==NULL)
        return;
    inorder(temp->left);
    cout<<temp ->data<<" ";
    inorder(temp->right);
}
void preorder(Node* temp)
{
    if(temp==NULL)
        return;
    cout<<temp ->data<<" ";
    preorder(temp->left);
    preorder(temp->right);
}
void postorder(Node* temp)
{
    if(temp==NULL)
        return;
    postorder(temp->left);
    postorder(temp->right);
    cout<<temp ->data<<" ";
}
void displayInorder()
{
    cout<<"\nInorder Traversal of the binary tree:\n";
    inorder(root);
}
void displayPreorder()
{
    cout<<"\nPreorder Traversal of the binary tree:\n";
    preorder(root);
}
void displayPostorder()
{
    cout<<"\nPostorder Traversal of the binary tree:\n";
    postorder(root);
}
};
int main()
{
    Binary b;
    int value;
    int choice;
    do
    {
        cout << "\n===== BINARY TREE MENU =====\n";
        cout << "1. CREATE TREE\n";
        cout << "2. DISPLAY INORDER\n";
        cout << "3. DISPLAY PREORDER\n";
        cout << "4. DISPLAY POSTORDER\n";
        cout << "5. EXIT\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            b.build();
            break;

        case 2:
            b.displayInorder();
            break;

        case 3:
            b.displayPreorder();
            break;

        case 4:
            b.displayPostorder();
            break;

        case 5:
            cout << "Program Closed.\n";
            break;

        default:
            cout << "Invalid Choice!\n";
        }

    } while (choice != 5);
    return 0;   
};