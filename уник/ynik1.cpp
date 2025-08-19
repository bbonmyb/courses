#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <windows.h>
#include <math.h>
#include <iostream>
using namespace std;


// Программирование разветвленных алгоритмов       задание 5 (1) - сдано

/*
int main()
{
	SetConsoleOutputCP(1251);
	double a, b, c;
	printf("Введите a - ");
	scanf("%lf", &a);
	printf("Введите b - ");
	scanf("%lf", &b);
	printf("Введите c - ");
	scanf("%lf", &c);

	if (a + b > c & b + c > a & a + c > b)
		if ((a == b) & (b == c))
			printf("Треугольник с данными сторонами является равносторонним");
		else if ((a == b & a != c) || (b == c & b != a) || (a == c & a != b))
			printf("Треугольник с данными сторонами является равнобедренным");
		else printf("Треугольник с данными сторонами является разносторонним");

	else printf("Треугольника с данными сторонами не существует");
}
*/



// 20.09.24       Программирование циклических алгоритмов             задания номер 6, 10, 15, 24, 30, 35   - сдано

//задание 6 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, kol, nenul = 0, sum2 = 0;
	cout << "Введите кол-во элементов - ";
	cin >> N;

	for (kol = 1; kol <= N; kol++)
	{
		int x;
		cout << "Введите переменную - ";
		cin >> x;

		if (x != 0)
			nenul++;

		if (x < 2)
			sum2 = sum2 + x;
	}
	cout << "Кол-во ненулевых элементов - " << nenul << endl;
	cout << "Сумма элементов, которые меньше двойки - " << sum2;
}
*/

//задание 10 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, k, x, flag = 0;
	cout << "Введите кол-во элементов - ";
	cin >> N;

	for (k = 1; k <= N; k++)
	{
		cout << "Введите переменную - ";
		cin >> x;

		if (x == 0)
		{
			cout << "Первый ноль в последовательности имеет номер - " << k;
			break;
		}
			flag = 1;

	}
	if (flag == 0)
		cout << "Нули отсутствуют";

}
*/

//задание 15 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, k, posl = 1, umn = 1;
	cout << "Введите кол-во членов последовательности - ";
	cin >> N;

	for (k = 2; k <= N + 1; k++)
	{
		umn = umn * posl;
		posl = posl + k;
	}
	cout << "Произведение членов последовательности данного вида = " << umn;
}
*/

//задание 24 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	srand(time(0));

	int N, i, a, proizv5 = 1;
	cout << "Введите кол-во членов арифметической прогресии - ";
	cin >> N;

	int smin = 1, smax = 10;
	int a1 = rand() % (smax - smin + 1) + smin;               // задает рандомную переменную из диапазона
	int d = rand() % (smax - smin + 1) + smin;

	a = a1;
	if (a > 5)
		proizv5 *= a;

	cout << a1 << endl;
	for (i = 0; i < N-1; i++)                      // for (начальная переменная = 0 ; условие ; изменение переменной)
	{
		a += d;
		cout << a << endl;
		if (a > 5)
			proizv5 *= a;
	}

	cout << "Произведение всех элементов, больших 5 = " << proizv5;
}

*/

//задание 30 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	int i, x, k=0,sum=0;
	for (i = 0; i < 15; i++)
	{
		cout << "Введите число от 0 до 10  - ";
		cin >> x;
		if (x == 4)
		{
		k++;
		sum += x;
		}
	}

	cout << "Кол-во чисел, меньших 5, но больших 3  = " << k << endl;
	cout << "Сумма чисел, меньших 5, но больших 3  = " << sum << endl;

}
*/

//задание 35 - проверенно

/*
int main()
{
	SetConsoleOutputCP(1251);
	int x, y, z;
	bool find = false;
	for (x = 1; x <= 9; x++)
		for (y = 0; y <= 9; y++)
			for (z = 0; z <= 9; z++)
				if ((x * x * x) + (y * y * y) + (z * z * z) == 730 && !find)
				{
					cout << x << " " << y << " " << z << endl;
					find = true;
					break;
				}

}
*/



//25.10.24 Память, адреса, указатели - сдано

/*
#define _CRT_SECURE_NO_WARNINGS
#define PI 3.14159
#include <stdio.h>
#include <windows.h>
#define N 11
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
#if N==1
	SetConsoleOutputCP(1251);

	int* ptrInt;
	double* ptrDouble;
	char* ptrChar;

	cout << "Размер указателя на int: " << sizeof(ptrInt) << " байт" << endl;
	cout << "Размер указателя на double: " << sizeof(ptrDouble) << " байт" << endl;
	cout << "Размер указателя на char: " << sizeof(ptrChar) << " байт" << endl;

	return 0;

#elif N==3
	SetConsoleOutputCP(1251);

	double* num1 = new double;
	double* num2 = new double;

	cout << "Введите первое число: ";
	cin >> *num1;

	cout << "Введите второе число: ";
	cin >> *num2;

	double sum = *num1 + *num2;
	double difference = *num1 - *num2;

	cout << "Сумма: " << sum << endl;
	cout << "Разность: " << difference << endl;

	delete num1;
	delete num2;

	return 0;

#elif N==5
	SetConsoleOutputCP(1251);

	int number = 10;
	int& refNumber = number;

	cout << "Исходное значение number: " << number << endl;

	refNumber = 20;

	cout << "Новое значение number (через ссылку): " << refNumber << endl;

	return 0;

#elif N==7
	SetConsoleOutputCP(1251);

	double number = 5.0;
	double* ptrNumber = &number;

	cout << "Исходное значение number: " << number << endl;

	*ptrNumber *= 2;

	cout << "Новое значение number: " << number << endl;

	return 0;

#elif N==9
	SetConsoleOutputCP(1251);

	int num1, num2, num3;
	int& refNum1 = num1;
	int& refNum2 = num2;
	int& refNum3 = num3;

	cout << "Введите первое число: ";
	cin >> refNum1;

	cout << "Введите второе число: ";
	cin >> refNum2;

	refNum3 = 2 * (refNum1 * refNum1 - refNum2 * refNum2);

	cout << "Число №3 = " << num3 << endl;

	return 0;

#elif N==11
	SetConsoleOutputCP(1251);

	const double value = 3.14;

	const double* const ptrValue = &value;
	const double* const* ptrPtrValue = &ptrValue;

	cout << "Значение вещественной константы: " << **ptrPtrValue << endl;

	return 0;
#endif

} */



//01.11.24 Препроцессорные средства
