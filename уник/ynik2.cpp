// динамические двумерные массивы (проверено)
// задание а

/*
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    srand(time(0));
    int size1, size2;

    cout << "Введите размер первого массива: ";
    cin >> size1;
    cout << "Введите размер второго массива: ";
    cin >> size2;

    // Создание и заполнение массивов случайными числами
    int* arr1 = new int[size1];
    int* arr2 = new int[size2];

    cout << "Первый массив: ";
    for (int i = 0; i < size1; i++) {
        arr1[i] = rand() % 100;
        cout << arr1[i] << " ";
    }
    cout << endl;

    cout << "Второй массив: ";
    for (int i = 0; i < size2; i++) {
        arr2[i] = rand() % 100;
        cout << arr2[i] << " ";
    }
    cout << endl;

    // Создание третьего массива
    int* arr3 = new int[size1 + size2];

    // Заполнение третьего массива
    for (int i = 0; i < size1; i++) {
        arr3[i] = arr1[i];
    }
    for (int i = 0; i < size2; i++) {
        arr3[size1 + i] = arr2[i];
    }

    cout << "Третий массив: ";
    for (int i = 0; i < size1 + size2; i++) {
        cout << arr3[i] << " ";
    }

    // Освобождение памяти
    delete[] arr1;
    delete[] arr2;
    delete[] arr3;

    return 0;
}
*/

// задание 2

/*
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите количество строк (n): ";
    cin >> n;
    cout << "Введите количество столбцов (m): ";
    cin >> m;

    // Создание и заполнение матрицы
    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cout << "a[" << i << "][" << j << "]: ";
            cin >> a[i][j];
        }
    }

    // Вычисление произведения положительных элементов по столбцам
    double* result = new double[m];
    for (int j = 0; j < m; j++) {
        result[j] = 1;
        for (int i = 0; i < n; i++) {
            if (a[i][j] > 0) {
                result[j] *= a[i][j];
            }
        }
    }

    // Вывод результата
    cout << "Произведение положительных элементов по столбцам:\n";
    for (int j = 0; j < m; j++) {
        cout << result[j] << " ";
    }

    // Освобождение памяти
    for (int i = 0; i < n; i++) delete[] a[i];
    delete[] a;
    delete[] result;

    return 0;
}
*/

// задание 6

/*
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите количество строк (n): ";
    cin >> n;
    cout << "Введите количество столбцов (m): ";
    cin >> m;

    // Создание и заполнение матрицы
    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cout << "a[" << i << "][" << j << "]: ";
            cin >> a[i][j];
        }
    }

    // Вычисление среднего арифметического положительных элементов
    double* result = new double[m];
    for (int j = 0; j < m; j++) {
        double sum = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (a[i][j] > 0) {
                sum += a[i][j];
                count++;
            }
        }
        result[j] = (count > 0) ? sum / count : 0;
    }

    // Вывод результата
    cout << "Среднее арифметическое положительных элементов по столбцам:\n";
    for (int j = 0; j < m; j++) {
        cout << result[j] << " ";
    }

    // Освобождение памяти
    for (int i = 0; i < n; i++) delete[] a[i];
    delete[] a;
    delete[] result;

    return 0;
}
*/

// задание 9

/*
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите количество строк (n): ";
    cin >> n;
    cout << "Введите количество столбцов (m): ";
    cin >> m;

    // Создание и заполнение матрицы
    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cout << "a[" << i << "][" << j << "]: ";
            cin >> a[i][j];
        }
    }

    // Нахождение минимального элемента в каждой строке
    int* minRow = new int[n];
    for (int i = 0; i < n; i++) {
        minRow[i] = a[i][0];
        for (int j = 1; j < m; j++) {
            if (a[i][j] < minRow[i]) {
                minRow[i] = a[i][j];
            }
        }
    }

    // Прибавление минимального элемента к каждому элементу строки
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            a[i][j] += minRow[i];
        }
    }

    // Вывод преобразованной матрицы
    cout << "Матрица после преобразования:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    // Освобождение памяти
    for (int i = 0; i < n; i++) delete[] a[i];
    delete[] a;
    delete[] minRow;

    return 0;
}
*/

// задание 13

/*
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите количество строк (n): ";
    cin >> n;
    cout << "Введите количество столбцов (m): ";
    cin >> m;

    // Создание и заполнение матрицы
    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cout << "a[" << i << "][" << j << "]: ";
            cin >> a[i][j];
        }
    }

    // Вычисление произведения отрицательных элементов по столбцам
    double* result = new double[m];
    for (int j = 0; j < m; j++) {
        result[j] = 1;
        for (int i = 0; i < n; i++) {
            if (a[i][j] < 0) {
                result[j] *= a[i][j];
            }
        }
    }

    // Вывод результата
    cout << "Произведение отрицательных элементов по столбцам:\n";
    for (int j = 0; j < m; j++) {
        cout << result[j] << " ";
    }

    // Освобождение памяти
    for (int i = 0; i < n; i++) delete[] a[i];
    delete[] a;
    delete[] result;

    return 0;
}
*/


// Функции (проверено)
// задание 6

/*
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Функция для формирования геометрической прогрессии
void createGeometricProgression(double* arr, int size, double firstTerm, double ratio) {
    arr[0] = firstTerm;
    for (int i = 1; i < size; i++) {
        arr[i] = arr[i - 1] * ratio;
    }
}

// Функция для подсчёта отрицательных элементов
int countNegatives(const double* arr, int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] < 0) count++;
    }
    return count;
}

// Функция для вывода массива
void printArray(const double* arr, int size, const char* name) {
    cout << "Массив " << name << ": ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    setlocale(LC_ALL, "RU");
    srand(time(0));
    int size1, size2;
    double firstTerm1, firstTerm2;

    cout << "Введите размер первого массива: ";
    cin >> size1;
    cout << "Введите первый элемент первой прогрессии: ";
    cin >> firstTerm1;

    cout << "Введите размер второго массива: ";
    cin >> size2;
    cout << "Введите первый элемент второй прогрессии: ";
    cin >> firstTerm2;

    double ratio1 = (rand() % 20 - 10) / 10.0; // Случайный знаменатель от -1.0 до 1.0
    double ratio2 = (rand() % 20 - 10) / 10.0;

    double* arr1 = new double[size1];
    double* arr2 = new double[size2];

    createGeometricProgression(arr1, size1, firstTerm1, ratio1);
    createGeometricProgression(arr2, size2, firstTerm2, ratio2);

    printArray(arr1, size1, "A");
    printArray(arr2, size2, "B");

    int negCount1 = countNegatives(arr1, size1);
    int negCount2 = countNegatives(arr2, size2);

    cout << "Количество отрицательных элементов в массиве A: " << negCount1 << endl;
    cout << "Количество отрицательных элементов в массиве B: " << negCount2 << endl;

    delete[] arr1;
    delete[] arr2;

    return 0;
}
*/

// задание 14

/*
#include <iostream>
#include <climits>
using namespace std;

// Функция для поиска индексов минимального и максимального элементов
void findMinMaxIndices(const int* arr, int size, int& minIndex, int& maxIndex) {
    minIndex = maxIndex = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] < arr[minIndex]) minIndex = i;
        if (arr[i] > arr[maxIndex]) maxIndex = i;
    }
}

// Функция для вычисления произведения элементов между min и max
int productBetweenMinMax(const int* arr, int size) {
    int minIndex, maxIndex;
    findMinMaxIndices(arr, size, minIndex, maxIndex);

    if (abs(minIndex - maxIndex) <= 1) return 0; // Нет элементов между ними

    int start = min(minIndex, maxIndex) + 1;
    int end = max(minIndex, maxIndex) - 1;
    int product = 1;

    for (int i = start; i <= end; i++) {
        product *= arr[i];
    }

    return product;
}

int main() {
    setlocale(LC_ALL, "RU");
    const int SIZE = 20;
    int arr[SIZE];

    cout << "Введите " << SIZE << " элементов массива:\n";
    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    int product = productBetweenMinMax(arr, SIZE);
    cout << "Произведение элементов между min и max: " << product << endl;

    return 0;
}
*/

// задание 22

/*
#include <iostream>
#include <climits>
using namespace std;

// Функция для поиска минимального элемента
int findMin(const int* arr, int size) {
    int minVal = INT_MAX;
    for (int i = 0; i < size; i++) {
        if (arr[i] < minVal) minVal = arr[i];
    }
    return minVal;
}

// Функция для поиска максимального элемента
int findMax(const int* arr, int size) {
    int maxVal = INT_MIN;
    for (int i = 0; i < size; i++) {
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    return maxVal;
}

// Функция для вычисления суммы положительных элементов
int sumPositives(const int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > 0) sum += arr[i];
    }
    return sum;
}

int main() {
    setlocale(LC_ALL, "RU");
    const int SIZE = 20;
    int arr[SIZE];

    cout << "Введите " << SIZE << " элементов массива:\n";
    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    int minVal = findMin(arr, SIZE);
    int maxVal = findMax(arr, SIZE);
    int sumPos = sumPositives(arr, SIZE);

    if (sumPos == 0) {
        cout << "Ошибка: сумма положительных элементов равна нулю.\n";
    }
    else {
        double S = (maxVal - minVal) * 1.0 / sumPos;
        cout << "Результат S: " << S << endl;
    }


    return 0;
}
*/

// задание 30

/*
#include <iostream>
using namespace std;

// Функция для формирования массива из отрицательных элементов
void filterNegatives(const int* src, int size, int*& dest, int& destSize) {
    destSize = 0;
    for (int i = 0; i < size; i++) {
        if (src[i] < 0) destSize++;
    }
    dest = new int[destSize];
    int index = 0;
    for (int i = 0; i < size; i++) {
        if (src[i] < 0) {
            dest[index] = src[i];
            index++;
        }
    }
}

// Функция для формирования массива из положительных элементов
void filterPositives(const int* src, int size, int*& dest, int& destSize) {
    destSize = 0;
    for (int i = 0; i < size; i++) {
        if (src[i] > 0) destSize++;
    }
    dest = new int[destSize];
    int index = 0;
    for (int i = 0; i < size; i++) {
        if (src[i] > 0) {
            dest[index] = src[i];
            index++;
        }
    }
}

// Функция для поиска минимального элемента
int findMin(const int* arr, int size) {
    if (size == 0) return 0;
    int minVal = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < minVal) minVal = arr[i];
    }
    return minVal;
}

// Функция для поиска максимального элемента
int findMax(const int* arr, int size) {
    if (size == 0) return 0;
    int maxVal = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    return maxVal;
}

int main() {
    setlocale(LC_ALL, "RU");
    const int SIZE = 20;
    int A[SIZE];

    cout << "Введите " << SIZE << " элементов массива:\n";
    for (int i = 0; i < SIZE; i++) {
        cin >> A[i];
    }

    int* P = NULL;
    int* N = NULL;
    int P_size = 0, N_size = 0;

    filterNegatives(A, SIZE, P, P_size);
    filterPositives(A, SIZE, N, N_size);

    cout << "Массив отрицательных элементов (P):\n";
    for (int i = 0; i < P_size; i++) cout << P[i] << " ";
    cout << "\nMin: " << findMin(P, P_size) << ", Max: " << findMax(P, P_size) << endl;

    cout << "Массив положительных элементов (N):\n";
    for (int i = 0; i < N_size; i++) cout << N[i] << " ";
    cout << "\nMin: " << findMin(N, N_size) << ", Max: " << findMax(N, N_size) << endl;

    if (P != NULL) delete[] P;
    if (N != NULL) delete[] N;

    return 0;
}
*/

// задание 38

/*
#include <iostream>
#include <cmath>
using namespace std;

// Функция для вычисления ln(y^2)
double computeLnSquare(double y) {
    if (y == 0) {
        cout << "Ошибка: логарифм нуля не определён.\n";
        return 0;
    }
    return log(y * y);
}

int main() {
    setlocale(LC_ALL, "RU");
    double a, b, c;
    cout << "Введите три числа (a, b, c): ";
    cin >> a >> b >> c;

    double x = computeLnSquare(a) + computeLnSquare(b) + computeLnSquare(c);
    cout << "Результат x: " << x << endl;

    return 0;
}
*/


// Производные типы данных
// задание 1

/*
#include <iostream>
#include <cstring>
using namespace std;

// Объявляем новый тип данных TEXT как массив символов длиной 100
typedef char TEXT[100];

// Функция для подсчёта количества слов в строке
int countWords(const TEXT str) {
    int count = 0;
    bool inWord = false;
    // Проходим по всей строке посимвольно
    for (int i = 0; str[i] != '\0'; ++i) {
        // Если встретили не пробел и не находимся внутри слова — это начало нового слова
        if (str[i] != ' ' && !inWord) {
            inWord = true;
            count++;
        }
        else if (str[i] == ' ') {
            // Если встретили пробел — выходим из слова
            inWord = false;
        }
    }
    return count;
}

int main() {
    setlocale(LC_ALL, "RU");
    TEXT line;
    cout << "Введите строку: ";
    cin.getline(line, 100); // Вводим строку с пробелами
    cout << "Количество слов: " << countWords(line) << endl;
    return 0;
}
*/

// задание 3

/*
#include <iostream>
#include <cstring>
using namespace std;

// Описание структуры для хранения адреса
struct adress {
    char street[50];
    int house;
    int flat;
};

int main() {
    setlocale(LC_ALL, "RU");
    adress* pa = new adress; // Выделяем память под структуру адреса динамически
    cout << "Введите улицу: ";
    cin.getline(pa->street, 50); // Вводим название улицы
    cout << "Введите номер дома: ";
    cin >> pa->house; // Вводим номер дома
    cout << "Введите номер квартиры: ";
    cin >> pa->flat; // Вводим номер квартиры

    // Выводим введённую информацию
    cout << "Адрес: " << pa->street << ", дом " << pa->house << ", кв. " << pa->flat << endl;
    delete pa; // Освобождаем выделенную память
    return 0;
}
*/

// задание 4

/*
#include <iostream>
#include <cstring>
using namespace std;

// Структура для хранения анкеты студента
struct anketa {
    char fio[50];
    char adress[50];
    int year;
    char group[20];
};

int main() {
    setlocale(LC_ALL, "RU");
    anketa students[5]; // Массив из 5 студентов
    for (int i = 0; i < 5; ++i) {
        cout << "Студент #" << i + 1 << endl;
        cout << "ФИО: ";
        cin.ignore(i == 0 ? 0 : 1000, '\n'); // Очищаем буфер ввода для корректной работы getline
        cin.getline(students[i].fio, 50); // Вводим ФИО
        cout << "Адрес: ";
        cin.getline(students[i].adress, 50); // Вводим адрес
        cout << "Год рождения: ";
        cin >> students[i].year; // Вводим год рождения
        cout << "Группа: ";
        cin.ignore(1000, '\n'); // Очищаем буфер перед вводом строки
        cin.getline(students[i].group, 20); // Вводим группу
    }

    // Выводим студентов, у которых фамилия начинается на 'С'
    cout << "\nСтуденты, у которых фамилия начинается на 'С':\n";
    for (int i = 0; i < 5; ++i) {
        // Проверяем первый символ ФИО
        if (students[i].fio[0] == 'С' || students[i].fio[0] == 'C') {
            cout << students[i].fio << ", " << students[i].adress << ", " << students[i].year << ", " << students[i].group << endl;
        }
    }
    return 0;
}
*/

// задание 5

/*
#include <iostream>
#include <cstring>
using namespace std;

// Структура для хранения информации о клиенте
struct client {
    char surname[50];
    int year;
    int num_purchases;
    double total;
};

// Функция для ввода информации о клиенте
void generateClient(client& c) {
    cout << "Фамилия: ";
    cin.getline(c.surname, 50); // Вводим фамилию
    cout << "Год рождения: ";
    cin >> c.year; // Вводим год рождения
    cout << "Количество покупок: ";
    cin >> c.num_purchases; // Вводим количество покупок
    cout << "Стоимость покупок: ";
    cin >> c.total; // Вводим общую стоимость
    cin.ignore(1000, '\n'); // Очищаем буфер после ввода чисел
}

// Функция для вывода информации о клиенте
void printClient(const client& c) {
    cout << "Фамилия: " << c.surname << endl;
    cout << "Год рождения: " << c.year << endl;
    cout << "Количество покупок: " << c.num_purchases << endl;
    cout << "Стоимость покупок: " << c.total << endl;
}

int main() {
    setlocale(LC_ALL, "RU");
    client c;
    generateClient(c); // Вводим данные
    cout << "\nИнформация о клиенте:\n";
    printClient(c); // Выводим данные
    return 0;
}
*/

// задание 6

/*
#include <iostream>
#include <cstring>
#include <cstdlib> // для rand() и srand()
#include <ctime>   // для time()
using namespace std;

// Вложенная структура для хранения ФИО
struct FIO {
    char surname[30];
    char name[30];
    char patronymic[30];
};

// Основная структура для хранения информации о студенте
struct student {
    FIO fio;           // ФИО (структура)
    char adress[50];   // Адрес
    int year;          // Год рождения
    char group[20];    // Группа
    int marks[10];     // 10 оценок
};

int main() {
    setlocale(LC_ALL, "RU");
    student s; // Объявляем переменную типа student

    // Вводим ФИО
    cout << "Введите фамилию: ";
    cin.getline(s.fio.surname, 30);
    cout << "Введите имя: ";
    cin.getline(s.fio.name, 30);
    cout << "Введите отчество: ";
    cin.getline(s.fio.patronymic, 30);

    // Вводим адрес
    cout << "Введите адрес: ";
    cin.getline(s.adress, 50);

    // Вводим год рождения
    cout << "Введите год рождения: ";
    cin >> s.year;
    cin.ignore(1000, '\n'); // Очищаем буфер после ввода числа

    // Вводим группу
    cout << "Введите группу: ";
    cin.getline(s.group, 20);

    // Генерируем случайные оценки от 3 до 5
    srand(time(0)); // Инициализируем генератор случайных чисел
    for (int i = 0; i < 10; ++i) {
        s.marks[i] = 3 + rand() % 3; // 3, 4 или 5
    }

    // Выводим всю информацию о студенте
    cout << "\nИнформация о студенте:\n";
    cout << "ФИО: " << s.fio.surname << " " << s.fio.name << " " << s.fio.patronymic << endl;
    cout << "Адрес: " << s.adress << endl;
    cout << "Год рождения: " << s.year << endl;
    cout << "Группа: " << s.group << endl;
    cout << "Оценки: ";
    for (int i = 0; i < 10; ++i) {
        cout << s.marks[i] << " ";
    }
    cout << endl;

    return 0;
}
*/


// Списки

// задание 2

/*
#include <iostream>
using namespace std;

struct Spisok {
    int Elem;
    Spisok* Next;
};

// Функция удаления первого элемента списка
void delete_first(Spisok*& head) {
    if (head == nullptr) return; // Если список пуст, ничего не делаем
    Spisok* temp = head;         // Сохраняем указатель на первый элемент
    head = head->Next;           // Сдвигаем голову на следующий элемент
    delete temp;                 // Освобождаем память старого первого элемента
}

// Функция вывода списка
void print_list(Spisok* head) {
    while (head != nullptr) {
        cout << head->Elem << " ";
        head = head->Next;
    }
    cout << endl;
}

// Функция добавления элемента в начало списка (для создания списка)
void push_front(Spisok*& head, int value) {
    Spisok* new_node = new Spisok;
    new_node->Elem = value;
    new_node->Next = head;
    head = new_node;
}

int main() {
    setlocale(LC_ALL, "RU");
    Spisok* list = nullptr;

    // Создаем список: 3 -> 2 -> 1
    push_front(list, 1);
    push_front(list, 2);
    push_front(list, 3);

    cout << "Исходный список: ";
    print_list(list);

    delete_first(list);

    cout << "После удаления первого элемента: ";
    print_list(list);

    // Освобождение памяти
    while (list != nullptr) {
        delete_first(list);
    }

    return 0;
}
*/

//задание 6

/*
#include <iostream>
using namespace std;

struct Spisok {
    int Elem;
    Spisok* Next;
};

// Функция подсчета суммы элементов списка
int sum_list(Spisok* head) {
    int sum = 0;
    while (head != nullptr) {
        sum += head->Elem;  // Добавляем значение текущего элемента к сумме
        head = head->Next;  // Переходим к следующему элементу
    }
    return sum;
}

// Функция вывода списка
void print_list(Spisok* head) {
    while (head != nullptr) {
        cout << head->Elem << " ";
        head = head->Next;
    }
    cout << endl;
}

// Функция добавления элемента в начало списка
void push_front(Spisok*& head, int value) {
    Spisok* new_node = new Spisok;
    new_node->Elem = value;
    new_node->Next = head;
    head = new_node;
}

int main() {
    setlocale(LC_ALL, "RU");
    Spisok* list = nullptr;

    // Создаем список: 4 -> 3 -> 2 -> 1
    push_front(list, 1);
    push_front(list, 2);
    push_front(list, 3);
    push_front(list, 4);

    cout << "Список: ";
    print_list(list);

    cout << "Сумма элементов: " << sum_list(list) << endl;

    // Освобождение памяти
    while (list != nullptr) {
        Spisok* temp = list;
        list = list->Next;
        delete temp;
    }

    return 0;
}
*/

// задание 10

/*
#include <iostream>
using namespace std;

struct Spisok {
    int Elem;
    Spisok* Next;
};

// Вставка нового элемента со значением value после последнего вхождения target
void insert_after_last(Spisok* head, int target, int value) {
    Spisok* last_match = nullptr;
    Spisok* current = head;

    // Ищем последний элемент со значением target
    while (current != nullptr) {
        if (current->Elem == target) {
            last_match = current;
        }
        current = current->Next;
    }

    if (last_match != nullptr) {
        // Создаем новый элемент
        Spisok* new_node = new Spisok;
        new_node->Elem = value;
        new_node->Next = last_match->Next;
        last_match->Next = new_node;
    }
    else {
        cout << "Значение " << target << " не найдено в списке." << endl;
    }
}

// Функция вывода списка
void print_list(Spisok* head) {
    while (head != nullptr) {
        cout << head->Elem << " ";
        head = head->Next;
    }
    cout << endl;
}

// Функция добавления элемента в начало списка
void push_front(Spisok*& head, int value) {
    Spisok* new_node = new Spisok;
    new_node->Elem = value;
    new_node->Next = head;
    head = new_node;
}

int main() {
    setlocale(LC_ALL, "RU");
    Spisok* list = nullptr;

    // Создаем список: 1 -> 2 -> 3 -> 2 -> 4
    push_front(list, 4);
    push_front(list, 2);
    push_front(list, 3);
    push_front(list, 2);
    push_front(list, 1);

    cout << "Исходный список: ";
    print_list(list);

    insert_after_last(list, 2, 99);

    cout << "После вставки 99 после последнего 2: ";
    print_list(list);

    // Освобождение памяти
    while (list != nullptr) {
        Spisok* temp = list;
        list = list->Next;
        delete temp;
    }

    return 0;
}
*/

// задание 12

/*
#include <iostream>
using namespace std;

struct Spisok {
    int Elem;
    Spisok* Next;
};

// Удаление всех элементов со значением value
void delete_all(Spisok*& head, int value) {
    Spisok* current = head;
    Spisok* prev = nullptr;

    while (current != nullptr) {
        if (current->Elem == value) {
            // Если удаляемый элемент - голова списка
            if (prev == nullptr) {
                head = current->Next;
                delete current;
                current = head;
            }
            else {
                prev->Next = current->Next;
                delete current;
                current = prev->Next;
            }
        }
        else {
            prev = current;
            current = current->Next;
        }
    }
}

// Функция вывода списка
void print_list(Spisok* head) {
    while (head != nullptr) {
        cout << head->Elem << " ";
        head = head->Next;
    }
    cout << endl;
}

// Функция добавления элемента в начало списка
void push_front(Spisok*& head, int value) {
    Spisok* new_node = new Spisok;
    new_node->Elem = value;
    new_node->Next = head;
    head = new_node;
}

int main() {
    setlocale(LC_ALL, "RU");
    Spisok* list = nullptr;

    // Создаем список: 5 -> 2 -> 5 -> 3 -> 5 -> 1
    push_front(list, 1);
    push_front(list, 5);
    push_front(list, 3);
    push_front(list, 5);
    push_front(list, 2);
    push_front(list, 5);

    cout << "Исходный список: ";
    print_list(list);

    delete_all(list, 5);

    cout << "После удаления всех 5: ";
    print_list(list);

    // Освобождение памяти
    while (list != nullptr) {
        Spisok* temp = list;
        list = list->Next;
        delete temp;
    }

    return 0;
}
*/


// Работа со структурами данных

// задание 1

/*
#include <iostream>
#include <string>
using namespace std;

struct Worker {
    string surname;
    int days[6]; // Понедельник - Суббота
};

const char* day_names[6] = { "Пн", "Вт", "Ср", "Чт", "Пт", "Сб" };

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество сборщиков: ";
    cin >> n;
    Worker* arr = new Worker[n];

    // Ввод данных
    for (int i = 0; i < n; ++i) {
        cout << "Фамилия сборщика #" << i + 1 << ": ";
        cin >> arr[i].surname;
        for (int j = 0; j < 6; ++j) {
            cout << "  Кол-во изделий за " << day_names[j] << ": ";
            cin >> arr[i].days[j];
        }
    }

    // 1. Фамилия и общее количество деталей
    cout << "\nОбщее количество изделий по каждому сборщику:\n";
    for (int i = 0; i < n; ++i) {
        int sum = 0;
        for (int j = 0; j < 6; ++j)
            sum += arr[i].days[j];
        cout << arr[i].surname << ": " << sum << endl;
    }

    // 2. Сборщик с наибольшим количеством и день максимума
    int max_total = 0, max_idx = 0, max_day = 0, max_day_val = 0;
    for (int i = 0; i < n; ++i) {
        int sum = 0, local_max = 0, local_day = 0;
        for (int j = 0; j < 6; ++j) {
            sum += arr[i].days[j];
            if (arr[i].days[j] > local_max) {
                local_max = arr[i].days[j];
                local_day = j;
            }
        }
        if (sum > max_total) {
            max_total = sum;
            max_idx = i;
            max_day = local_day;
            max_day_val = local_max;
        }
    }
    cout << "\nЛучший сборщик: " << arr[max_idx].surname
        << ", максимум (" << max_day_val << ") в " << day_names[max_day] << endl;

    delete[] arr;
    return 0;
}
*/

// задание 3

/*
#include <iostream>
#include <string>
using namespace std;

struct Phone {
    string surname;
    string street;
    int house;
    int year;
    string number;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество абонентов: ";
    cin >> n;
    Phone* arr = new Phone[n];

    // Ввод данных
    for (int i = 0; i < n; ++i) {
        cout << "Абонент #" << i + 1 << endl;
        cout << "  Фамилия: "; cin >> arr[i].surname;
        cout << "  Улица: "; cin >> arr[i].street;
        cout << "  Дом: "; cin >> arr[i].house;
        cout << "  Год установки: "; cin >> arr[i].year;
        cout << "  Номер телефона: "; cin >> arr[i].number;
    }

    // 1. Поиск по фамилии
    string search_surname;
    cout << "\nВведите фамилию для поиска номера: ";
    cin >> search_surname;
    bool found = false;
    for (int i = 0; i < n; ++i)
        if (arr[i].surname == search_surname) {
            cout << "Номер: " << arr[i].number << endl;
            found = true;
        }
    if (!found)
        cout << "Абонент не найден.\n";

    // 2. Количество телефонов с года X
    int year_x, count = 0;
    cout << "\nВведите год для подсчета телефонов: ";
    cin >> year_x;
    for (int i = 0; i < n; ++i)
        if (arr[i].year >= year_x) ++count;
    cout << "Телефонов установлено с " << year_x << " года: " << count << endl;

    // 3. Телефоны по улице и дому
    string search_street;
    int search_house;
    cout << "\nВведите улицу и дом для поиска: ";
    cin >> search_street >> search_house;
    cout << "Телефоны жильцов: ";
    for (int i = 0; i < n; ++i)
        if (arr[i].street == search_street && arr[i].house == search_house)
            cout << arr[i].number << " ";
    cout << endl;

    delete[] arr;
    return 0;
}
*/

// задание 4

/*
#include <iostream>
#include <string>
using namespace std;

struct Toy {
    string name;
    double price;
    int amount;
    int age_from, age_to;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество игрушек: ";
    cin >> n;
    Toy* arr = new Toy[n];

    // Ввод данных
    for (int i = 0; i < n; ++i) {
        cout << "Игрушка #" << i + 1 << endl;
        cout << "  Название: "; cin >> arr[i].name;
        cout << "  Цена: "; cin >> arr[i].price;
        cout << "  Количество: "; cin >> arr[i].amount;
        cout << "  Возраст от: "; cin >> arr[i].age_from;
        cout << "  Возраст до: "; cin >> arr[i].age_to;
    }

    // 1. Игрушки для детей от 1 до 3 лет
    cout << "\nИгрушки для детей от 1 до 3 лет:\n";
    for (int i = 0; i < n; ++i)
        if (arr[i].age_from <= 3 && arr[i].age_to >= 1)
            cout << arr[i].name << endl;

    // 2. Самая дорогая игрушка
    double max_price = 0;
    int max_idx = 0;
    for (int i = 0; i < n; ++i)
        if (arr[i].price > max_price) {
            max_price = arr[i].price;
            max_idx = i;
        }
    cout << "\nСамая дорогая игрушка: " << arr[max_idx].name
        << " (Цена: " << arr[max_idx].price << ")\n";

    // 3. Игрушки по цене и возрасту
    int A, B;
    double X;
    cout << "\nВведите возрастной диапазон (A B) и максимальную цену X: ";
    cin >> A >> B >> X;
    cout << "Игрушки, подходящие по цене и возрасту:\n";
    for (int i = 0; i < n; ++i)
        if (arr[i].price <= X && arr[i].age_from <= B && arr[i].age_to >= A)
            cout << arr[i].name << endl;

    delete[] arr;
    return 0;
}
*/

// задание 6

/*
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string surname;
    int group;
    char disc[5]; // '1' - выбрал, ' ' - не выбрал
    double avg;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество студентов: ";
    cin >> n;
    Student* arr = new Student[n];

    // Ввод данных
    for (int i = 0; i < n; ++i) {
        cout << "Студент #" << i + 1 << endl;
        cout << "  Фамилия: "; cin >> arr[i].surname;
        cout << "  Группа: "; cin >> arr[i].group;
        cout << "  Дисциплины (5 символов, 1 - выбрал, ' ' - нет): ";
        for (int j = 0; j < 5; ++j)
            cin >> arr[i].disc[j];
        cout << "  Средний балл: "; cin >> arr[i].avg;
    }

    int x;
    cout << "\nВведите номер дисциплины (1-5) для поиска: ";
    cin >> x;
    x = x - 1; // индексация с 0

    // Формируем список желающих
    int count = 0;
    for (int i = 0; i < n; ++i)
        if (arr[i].disc[x] == '1')
            ++count;

    cout << "Желающие студенты:\n";
    if (count <= 4) {
        for (int i = 0; i < n; ++i)
            if (arr[i].disc[x] == '1')
                cout << arr[i].surname << " (группа " << arr[i].group << ")\n";
    }
    else {
        // Если больше 4, отбираем по среднему баллу > 4.0
        for (int i = 0; i < n; ++i)
            if (arr[i].disc[x] == '1' && arr[i].avg > 4.0)
                cout << arr[i].surname << " (группа " << arr[i].group << ", ср. балл " << arr[i].avg << ")\n";
    }

    delete[] arr;
    return 0;
}
*/



// Работа со структурами данных

// задание 1 

/*
#include <iostream>
#include <string>

using namespace std;

struct Worker {
    string surname;
    int details[7]; // 7 дней недели
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество сборщиков: ";
    cin >> n;

    Worker* workers = new Worker[n]; // Динамический массив

    // Ввод данных
    for (int i = 0; i < n; i++) {
        cout << "Фамилия: ";
        cin >> workers[i].surname;
        cout << "Детали за 7 дней (через пробел): ";
        for (int j = 0; j < 7; j++) {
            cin >> workers[i].details[j];
        }
    }

    // Поиск лучшего
    int max_total = 0, max_day = 0, best_index = 0;
    for (int i = 0; i < n; i++) {
        int total = 0;
        for (int j = 0; j < 7; j++) {
            total += workers[i].details[j];
            if (workers[i].details[j] > max_day) {
                max_day = workers[i].details[j];
            }
        }
        cout << workers[i].surname << ": " << total << endl;

        if (total > max_total) {
            max_total = total;
            best_index = i;
        }
    }

    cout << "Лучший сборщик: " << workers[best_index].surname << endl;
    cout << "Максимум за день: " << max_day << endl;

    delete[] workers; // Освобождение памяти
    return 0;
}
*/

// задание 3

/*
#include <iostream>
#include <string>

using namespace std;

struct Address {
    string street;
    int house;
};

struct Subscriber {
    string surname;
    Address addr;
    int year;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Количество абонентов: ";
    cin >> n;

    Subscriber* subs = new Subscriber[n];

    // Ввод данных
    for (int i = 0; i < n; i++) {
        cout << "Фамилия: ";
        cin >> subs[i].surname;
        cout << "Улица: ";
        cin >> subs[i].addr.street;
        cout << "Дом: ";
        cin >> subs[i].addr.house;
        cout << "Год: ";
        cin >> subs[i].year;
    }

    // Поиск по фамилии
    string target;
    cout << "Введите фамилию для поиска: ";
    cin >> target;
    for (int i = 0; i < n; i++) {
        if (subs[i].surname == target) {
            cout << "Найден: " << subs[i].addr.street
                << " " << subs[i].addr.house << endl;
        }
    }

    // Подсчёт по году
    int year, count = 0;
    cout << "Введите год: ";
    cin >> year;
    for (int i = 0; i < n; i++) {
        if (subs[i].year == year) count++;
    }
    cout << "Телефонов с " << year << " года: " << count << endl;

    delete[] subs;
    return 0;
}
*/

// задание 4

/*
#include <iostream>
#include <string>

using namespace std;

struct Toy {
    string name;
    float price;
    int age_min;
    int age_max;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Количество игрушек: ";
    cin >> n;

    Toy* toys = new Toy[n];

    // Ввод данных
    for (int i = 0; i < n; i++) {
        cout << "Название: ";
        cin >> toys[i].name;
        cout << "Цена: ";
        cin >> toys[i].price;
        cout << "Минимальный возраст: ";
        cin >> toys[i].age_min;
        cout << "Максимальный возраст: ";
        cin >> toys[i].age_max;
    }

    // Игрушки для 1-3 лет
    cout << "\nДля 1-3 лет:\n";
    for (int i = 0; i < n; i++) {
        if (toys[i].age_min <= 1 && toys[i].age_max >= 3) {
            cout << toys[i].name << endl;
        }
    }

    // Самая дорогая
    float max_price = 0;
    int max_index = 0;
    for (int i = 0; i < n; i++) {
        if (toys[i].price > max_price) {
            max_price = toys[i].price;
            max_index = i;
        }
    }
    cout << "\nСамая дорогая: " << toys[max_index].name << endl;

    delete[] toys;
    return 0;
}
*/

// задание 6

/*
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Student {
    string surname;
    string group;
    char subjects[5]; // '1' - выбран
    float avg_score;
};

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Количество студентов: ";
    cin >> n;

    Student* students = new Student[n];

    // Ввод данных
    for (int i = 0; i < n; i++) {
        cout << "Фамилия: ";
        cin >> students[i].surname;
        cout << "Группа: ";
        cin >> students[i].group;
        cout << "Выбранные дисциплины (5 цифр 0/1): ";
        for (int j = 0; j < 5; j++) {
            cin >> students[i].subjects[j];
        }
        cout << "Средний балл: ";
        cin >> students[i].avg_score;
    }

    // Поиск по дисциплине
    int subject;
    cout << "Номер дисциплины (0-4): ";
    cin >> subject;

    vector<Student> selected;
    for (int i = 0; i < n; i++) {
        if (students[i].subjects[subject] == '1') {
            selected.push_back(students[i]);
        }
    }

    // Сортировка если больше 4
    if (selected.size() > 4) {
        sort(selected.begin(), selected.end(),
            [](const Student& a, const Student& b) {
                return a.avg_score > b.avg_score;
            });
    }

    // Вывод результатов
    cout << "\nОтобранные студенты:\n";
    for (const auto& s : selected) {
        cout << s.surname << " (" << s.avg_score << ")" << endl;
    }

    delete[] students;
    return 0;
}
*/