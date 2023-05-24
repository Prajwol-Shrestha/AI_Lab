#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 1000 // maximum size of the stack

int visited[MAX_STACK_SIZE]; // array to keep track of visited nodes

typedef struct {
    int data[MAX_STACK_SIZE];
    int top;
} Stack;

void push(Stack *s, int value) {
    if (s->top == MAX_STACK_SIZE-1) {
        printf("Stack overflow\n");
        exit(1);
    }
    s->top++;
    s->data[s->top] = value;
}

int pop(Stack *s) {
    if (s->top == -1) {
        printf("Stack underflow\n");
        exit(1);
    }
    int value = s->data[s->top];
    s->top--;
    return value;
}

void dfs(int adjacency_matrix[][MAX_STACK_SIZE], int source_node, int num_nodes) {
    Stack s;
    s.top = -1;
    int i, j;
    for (i = 0; i < num_nodes; i++) {
        visited[i] = 0;
    }
    visited[source_node] = 1;
    push(&s, source_node);
    while (s.top != -1) {
        int current_node = pop(&s);
        printf("%d ", current_node);
        for (j = num_nodes-1; j >= 0; j--) {
            if (adjacency_matrix[current_node][j] == 1 && !visited[j]) {
                visited[j] = 1;
                push(&s, j);
            }
        }
    }
}

int main() {
    int adjacency_matrix[MAX_STACK_SIZE][MAX_STACK_SIZE], num_nodes, source_node, i, j;
    printf("Enter the number of nodes: ");
    scanf("%d", &num_nodes);
    printf("Enter the adjacency matrix:\n");
    for (i = 0; i < num_nodes; i++) {
        for (j = 0; j < num_nodes; j++) {
            scanf("%d", &adjacency_matrix[i][j]);
        }
    }
    printf("Enter the source node: ");
    scanf("%d", &source_node);
    printf("DFS Traversal: ");
    dfs(adjacency_matrix, source_node, num_nodes);
    printf("\n");
    return 0;
}
