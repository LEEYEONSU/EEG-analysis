#include <stdio.h>
#include <iostream>

using namespace std;

int arr[26][2];

//root-left-right
void preorder(int node){

        if (node == -1) return;

        else {
                cout << char(node + 'A');
                preorder(arr[node][0]);
                preorder(arr[node][1]);

        }

}

//left-root-right
void inorder(int node){

        if (node == -1) return;

        else {
                inorder(arr[node][0]);
                cout << char(node + 'A');
                inorder(arr[node][1]);

        }
}

//left-right-root
void postorder(int node){

        if (node == -1) return;

        else {
                postorder(arr[node][0]);
                postorder(arr[node][1]);
                cout << char(node + 'A');

        }
}

int main(void){

        int N;

        scanf("%d", &N);

        for( int i = 0 ; i < N ; i++ ){
                char root, L, R ; 

                cin >> root >> L >> R;
                
                if (L != '.') arr[root-'A'][0] = L-'A';
                else arr[root-'A'][0] = -1;

                if (R != '.') arr[root-'A'][1] = R-'A';
                else arr[root-'A'][1] = -1;


        }
        preorder(0);
        printf("\n");
        inorder(0);
        printf("\n");
        postorder(0);
        printf("\n");

        return 0;
}