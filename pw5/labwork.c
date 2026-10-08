#include <stdio.h>
#define MAX 100

typedef struct {
    int data[MAX];
    int size;
} List;

int sumDigits(List *list);

void addDigit(List *list, int digit, int position) {
    int i;

    if (position < 1 || position > list->size || list->size >= MAX) {
        return;
    }

    for (i = list->size; i > position; i--) {
        list->data[i] = list->data[i - 1];
    }

    list->data[position] = digit;
    list->size++;
}

void removeDigit(List *list, int position) {
    int i;

    if (position < 1 || position >= list->size) {
        return;
    }

    for (i = position; i < list->size - 1; i++) {
        list->data[i] = list->data[i + 1];
    }

    list->size--;
}

int sumDigits(List *list) {
    int i;
    int sum = 0;

    for (i = 1; i < list->size; i++) {
        sum += list->data[i];
    }

    return sum;
}

void display(List *list) {
    int i;

    if (list->data[0] == -1) {
        printf("-");
    }

    for (i = 1; i < list->size; i++) {
        printf("%d", list->data[i]);
    }

    printf("\n");
}

int main(void) {
    List list;
    int n;
    int i;
    int digit;
    int position;

    list.size = 1;

    printf("Enter sign (1 or -1): ");
    scanf("%d", &list.data[0]);

    printf("Enter number of digits: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        printf("Enter digit %d: ", i);
        scanf("%d", &list.data[i]);
    }

    list.size = n + 1;

    printf("\nNumber: ");
    display(&list);

    printf("\nEnter digit to add: ");
    scanf("%d", &digit);

    printf("Enter position: ");
    scanf("%d", &position);

    addDigit(&list, digit, position);

    printf("After adding: ");
    display(&list);

    printf("\nEnter position to remove: ");
    scanf("%d", &position);

    removeDigit(&list, position);

    printf("After removing: ");
    display(&list);

    printf("\nSum of digits: %d\n", sumDigits(&list));

    return 0;
}
