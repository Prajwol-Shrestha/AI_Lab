#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 1000 // maximum size of the queue

int visited[MAX_QUEUE_SIZE]; // array to keep track of visited nodes

typedef struct {
    int data[MAX_QUEUE_SIZE];
    int rear;
    int front;
} Queue;

void enqueue(Queue *q, int value) {
    if (q->rear == MAX_QUEUE_SIZE-1) {
        printf("Queue overflow\n");
        exit(1);
    }
    q->rear++;
    q->data[q->rear] = value;
}

int dequeue(Queue *q) {
    if (q->front > q->rear) {
        printf("Queue underflow\n");
        exit(1);
    }
    int value = q->data[q->front];
    q->front++;
    return value;
}

void bfs(int adjacency_matrix[][MAX_QUEUE_SIZE], int source_node, int num_nodes) {
    Queue q;
    q.front = 0;
    q.rear = -1;
    int i, j;
    for (i = 0; i < num_nodes; i++) {
        visited[i] = 0;
    }
    visited[source_node] = 1;
    enqueue(&q, source_node);
    while (q.front <= q.rear) {
        int current_node = dequeue(&q);
        printf("%d ", current_node);
        for (j = 0; j < num_nodes; j++) {
            if (adjacency_matrix[current_node][j] == 1 && !visited[j]) {
                visited[j] = 1;
                enqueue(&q, j);
            }
        }
    }
}

int main() {
    int adjacency_matrix[MAX_QUEUE_SIZE][MAX_QUEUE_SIZE], num_nodes, source_node, i, j;
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
    printf("BFS Traversal: ");
    bfs(adjacency_matrix, source_node, num_nodes);
    printf("\n");
    return 0;
}
