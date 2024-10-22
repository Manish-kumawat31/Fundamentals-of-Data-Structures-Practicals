#include<iostream>
using namespace std;

class stack{
	public:
	int top=-1;
	char s1[];
bool isStackFull(int size){
	if(top==size-1){
	return true;
	}
	else {
	return false;
	}
}
bool isStackEmpty(int size){
	if(top==-1){
	return true;
	}
	else {
	return false;
	}
}  

void push(char x){
	if (isStackFull(10))
	{
		cout<<"Stck Full";
	}
	else{
	top++;
	s1[top]=x;

	}
}
void pop(){
	if (isStackEmpty(10))
	{
		cout<<"Stack empty";
	}else{
	char d;
	d=s1[top];
	top--;
	}
}
 
bool check(){
	if (top==-1)
	{
		return true;
	}
	else{
		return false;
	}
	
}

};

int main(){
	stack s1;
	int size=10;
	char s[10];
	
	char ch='y';
	while(ch!='n'){
		cout<<"Enter your choice:"<<endl;
		cout<<"1.check whether given expression is well parenthesized or not."<<endl;
		cout<<"2.exit"<<endl;
		int flag;
		cin>>flag;
		switch(flag){
		case 1:{
			cout<<"Enter Expression:"<<endl;
			cin>>s;
			for (int i = 0; i < size; i++)
			{
				if (s[i]=='(' || s[i]=='{' || s[i]=='[')
				{
					s1.push(s[i]);
				}
				else{
					if (s[i]==')' || s[i]=='}' || s[i]==']')
					{
						s1.pop();
					}
					
				}
				
			}
			if (s1.check())
			{
				cout<<"Given expression is well parenthesized";
			}
			else{
				cout<<"Given expression is not well parenthesized";
			}
			
			
			break;
		}
		case 2:{
			ch='n';
			break;
		}
		}
	}

}
