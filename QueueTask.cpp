#include <iostream>
using namespace std;
class queue
{
public:
    int rear = -1, front = -1;
    int size = 10;
    string s[10];

    bool isQueueFull()
    {
        if (rear == size - 1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    bool isQueueEmpty()
    {
        if (front > rear || (front == -1 && rear == -1))
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    void Enqueue(string task)
    {
        if (isQueueFull())
        {
            cout << "Queue is full!" << endl;
        }
        else
        {
            if (isQueueEmpty())
            {
                rear++;
                front++;
                s[rear] = task;
            }
            else
            {
                rear++;
                s[rear] = task;
            }
        }
    }
    void Dequeue()
    {
        if (isQueueEmpty())
        {
            cout<<"Queue Empty!!\nCannot Dequeue";
        }
        else{
            string d;
            d=s[front];
            front++;
        }
    }

    void Traverse()
    {
        int sr=1;
        int t=front;
        while (t<=rear)
        {
            cout<<sr<<"."<<s[t]<<endl;
            t++;
            sr++;
        }
        cout<<"\n\n";
    }
};

int main()
{
    queue q;
    char ch = 'y';
    while (ch != 'n')
    {
        cout << "\n\nEnter your choice:" << endl;
        cout << "1.Add Task" << endl;
        cout << "2.Delete Task" << endl;
        cout << "3.Show list" << endl;
        cout << "4.exit\n" << endl;
        int flag;
        cin >> flag;
        switch (flag)
        {
        case 1:
        {
            cout << "Enter Task:" << endl;
            string task;
            cin >> task;
            q.Enqueue(task);
            break;
        }
        case 2:{
            cout << "Deleting Task.....Done!!\n" << endl;
            q.Dequeue();
            break;
        }
        case 3:{
            cout<<"----------All List----------"<<endl;
            q.Traverse();
            break;
        }
        case 4:
        {
            ch = 'n';
            break;
        }
        }
    }
}
