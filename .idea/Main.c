#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 10
#define COLS 20

void recursiveBacktracking(char array[ROWS][COLS], int row, int col) {
    array[row][col] = 0;  // Пустая клетка

    // Случайно перемешиваем направления: вверх, вниз, влево, вправо
    int directions[] = {1, 2, 3, 4};
    for (int i = 0; i < 4; i++) {
        int j = rand() % 4;
        int temp = directions[i];
        directions[i] = directions[j];
        directions[j] = temp;
    }

    // Проходим через соседние клетки
    for (int i = 0; i < 4; i++) {
        int nextRow = row;
        int nextCol = col;

        if (directions[i] == 1) {  // Вверх
            nextRow -= 2;
        } else if (directions[i] == 2) {  // Вниз
            nextRow += 2;
        } else if (directions[i] == 3) {  // Влево
            nextCol -= 2;
        } else if (directions[i] == 4) {  // Вправо
            nextCol += 2;
        }

        if (nextRow > 0 && nextRow < ROWS - 1 && nextCol > 0 && nextCol < COLS - 1 && array[nextRow][nextCol] == 1) {
            array[nextRow][nextCol] = 0;  // Проходим через клетку
            array[row + (nextRow - row) / 2][col + (nextCol - col) / 2] = 0;  // Удаляем стену между текущей и следующей клеткой
            recursiveBacktracking(array, nextRow, nextCol);  // Рекурсивно продолжаем генерацию лабиринта
        }
    }
}

void generateArray(char array[ROWS][COLS]) {
    srand(time(NULL));

    // Заполняем лабиринт преградами (1) и пустыми клетками (0)
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            array[i][j] = 1;  // Преграда
        }
    }

    // Рекурсивно генерируем лабиринт
    recursiveBacktracking(array, 1, 1);

    // Размещаем вход и выход в лабиринте
    array[1][0] = 0;  // Вход
    array[ROWS - 2][COLS - 1] = 0;  // Выход
    array[ROWS - 2][COLS - 2] = 0;  // Выход
    array[ROWS - 2][COLS - 3] = 0;  // Выход
}

void printArray(char array[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (array[i][j] == 1) {
                printf("#");  // Преграда
            } else if (i == 1 && j == 0) {
                printf("S");  // Вход
            } else if (i == ROWS - 2 && j == COLS - 1) {
                printf("E");  // Выход
            } else {
                printf(" ");  // Пустая клетка
            }
        }
        printf("\n");
    }
}

int main() {
    char array[ROWS][COLS];

    generateArray(array);
    printArray(array);

    return 0;
}
