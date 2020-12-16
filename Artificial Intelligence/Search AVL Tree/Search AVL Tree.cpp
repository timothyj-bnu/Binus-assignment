#include<stdio.h>
#include<stdlib.h>

//The search algorithm is at the bottom part (at the top of main function)
struct data{
	int value;
	int height;
	struct data *left;
	struct data *right;
}*root = NULL;

bool isInserted = false;

struct data *createNewNode(int val){
	isInserted = true;
	struct data *newNode = (struct data *) malloc (sizeof(struct data));
	newNode->height = 1;
	newNode->value = val;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

int getMax(int a, int b){
	if(a > b) return a;
	else return b;
}

int getHeight(struct data *node){
	if(node == NULL) return 0;
	return node->height;
}

int getBF(struct data *node){
	if(node == NULL) return 0;
	int left = getHeight(node->left);
	int right = getHeight(node->right);
	return left - right;
}

struct data *LL(struct data *A){
	struct data *B = A->left;
	struct data *f = B->right;
	
	B->right = A;
	A->left = f;
	
	A->height = getMax(getHeight(A->left), getHeight(A->right))+1;
	B->height = getMax(getHeight(B->left), getHeight(B->right))+1;
	
	return B;
}

struct data *RR(struct data *A){
	struct data *B = A->right;
	struct data *e = B->left;
	
	B->left = A;
	A->right = e;
	
	A->height = getMax(getHeight(A->left), getHeight(A->right))+1;
	B->height = getMax(getHeight(B->left), getHeight(B->right))+1;
	
	return B;
}

struct data *insertNode(struct data *node, int val){
	if(node == NULL) return createNewNode(val);
	else if(val < node->value) node->left = insertNode(node->left, val);
	else if(val > node->value) node->right = insertNode(node->right, val);
	else printf("\n\tCannot enter the same value!\n\n");

	node->height = 1 + getMax(getHeight(node->left), getHeight(node->right));
	int BF = getBF(node);
	
	//kalo string : strcmp(nama, node->left->nama) < 0

	if(BF > 1 && val < node->left->value) return LL(node);
	if(BF < -1 && val > node->right->value)	return RR(node);
	if(BF > 1 && val > node->left->value){
		node->left = RR(node->left);
		return LL(node);
	}

	if(BF < -1 && val < node->right->value){
		node->right = LL(node->right);
		return RR(node);
	}
	return node;
}

void infix(struct data *node){
	if(node){
		infix(node->left);
		printf("%d->", node->value);
		infix(node->right);
	}
}

struct data *searchNode(struct data *node, int num){
	if(node == NULL) {
		printf("NOT FOUND\n\n");
		return NULL;
	}
	
	if(num < node->value) node->left = searchNode(node->left, num);
	else if(num > node->value) node->right = searchNode(node->right, num);
	else if(num == node->value) printf("%d is found!\n\n", node->value);
	else printf("NOT FOUND!\n\n");
	return node;
}

int main()
{
	printf("Search in AVL Tree\n===========================\n");
	printf("Input number of nodes : ");
	int node;
	scanf("%d", &node);
	int i = 1;
	while(node--){
		isInserted = false;
		int num;
		while(!isInserted){
			printf("%d. Insert number : ", i);
			scanf("%d", &num);
			root = insertNode(root, num);
		}
		i++;
	}
	
	printf("\nTree representation (inorder) : \n");
	infix(root);
	printf("\n\n");
	
	
	printf("Search function\n===========================\n");
	while(true){
		int n;
		printf("Search number : ");
		scanf("%d", &n);
		root = searchNode(root, n);
	}

	return 0;
}
