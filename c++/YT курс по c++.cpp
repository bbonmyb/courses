// Тут дан кусок базовой теории для C++, взятый из бесплатного курса на ютубе.




#include <iostream>  // включаем библиотеку Input Output Stream

#include <cstdlib>   // включаем библиотеку C Standard Library (стандартная библиотека C)
#include <ctime>     // включаем библиотеку C Time Library (библиотека времени из C)

#include <string>    // включаем библиотеку string для работы с строками


using namespace std;  // говорим, что будем использовать именно пространство имён std Стандарт






// || базовая теория || типы данных || условные конструкции IF и SWITCH || 
// || простой калькулятор || сокращения || случайные числа ||

/*
int main() {                 // 
	setlocale(LC_ALL, "RU");  // чтобы понимал русский язык

	cout << "Program start..." << endl;  // 'endl' - end line, перенос на след.строку
	cout << "Program start... \n";       //  \n - тоже перенос на след.строку



	// Использование переменных
	int a, b;
	cout << "Введите значение переменной a - ";    // вывод на экран
	cin >> a;                                      // ввод в консоли

	cout << "Введите значение переменной b - ";
	cin >> b;




	// Типы данных (целые числа)
	short num1 = 1;            // 2 byte | диапазон значений от -32к до 32к
	int num2 = 1;              // 4 byte | диапазон значений от -2В до 2В
	long num3 = 1;             // 8 byte | диапазон значений очень большой

	unsigned short num11 = 1;  // 2 byte | диапазон значений от 0 до 65к
	unsigned int num22 = 1;    // 4 byte | диапазон значений от 0 до 4В
	unsigned long num33 = 1;   // 8 byte | диапазон значений от 0 до очень большой


	// Вещественные числа
	float num4 = 5.13463561345f;    // приписка f в конце числа необязательна, но так грамотно
	double num5 = 454.13665432f;

	// Хранение одного символа
	char symbol = '&';

	// Логический тип данных - true|false
	bool isHappy = true;
	



	cout << "\n\n\n\n Условная конструкция if \n\n";

	if (a > b) {                                    // Оператор if (если) - условная конструкция, которая выполняет кусок кода, если условие верно.
		cout << "Число a больше числа b \n";        // Если код больше чем в 1 строку, нужно ставить фигурные скобки, чтобы обозначить начало и конец кода.
		if (a / b >= 2)                             // После if у нас прописывается основное условие.
			cout << "Больше чем в 2 раза";
	}
	else if (a == b)                                // Код else if выполнится, если прошлые условия == false и это условие == true
		cout << "Числа одинаковые";
	else if (isHappy)
		cout << "пример с булевой функцией - True";
	else if (!isHappy)
		cout << "пример с булевой функцией - False";
	else                                            // Если все условия false, выполняется блок else (если он есть)
		cout << "Число b больше числа a";           // Он необязательный и используется только при наличии if




	cout << "\n\n\n\n Условная конструкция switch case \n\n";

	switch (a) {                                    // switch case - тоже условная конструкция, но только для сравнения с конкретными значениями.
	case 5:
		cout << "a == 5";
		break;                                      // break — выход из цикла (без него выполнение проваливается в следующий case!)
	case 6:
		cout << "a == 6";
		break;
	case 7: cout << "a == 6"; break;
	default:
		cout << "default";
		break;
	}




	cout << "\n\n\n\n (практика) Калькулятор на if \n\n";

	float number1, number2, res;
	cout << "Введите первое число - ";
	cin >> number1;

	cout << "Введите второе число - ";
	cin >> number2;

	//    +, -, *, /
	char math;
	cout << "Введите математический символ (+, -, *, /)  -  ";
	cin >> math;

	if (math == '+')
		res = number1 + number2;
	else if (math == '-')
		res = number1 - number2;
	else if (math == '*')
		res = number1 * number2;
	else if (math == '/')
		res = number1 / number2;

	cout << "Result = " << res;




	cout << "\n\n\n\n (практика) Калькулятор на switch \n\n";

	switch (math) {
	case '+': res = number1 + number2; break;
	case '-': res = number1 - number2; break;
	case '*': res = number1 * number2; break;
	case '/': res = number1 / number2; break;
	default:
		res = 0;
		cout << "Error";
		break;
	}

	cout << "Result = " << res;




	cout << "\n\n\n\n Сокращения математических операций \n\n";

	int A = 10;

	A += 5;         // тоже самое что   A = A + 5     || точно также работает со всеми математическими операциями
	A++;            // тоже самое что   A = A + 1     || точно также работает с вычитанием




	cout << "\n\n\n\n Случайные числа \n\n";

	// rand() генерирует псевдослучайное число в диапазоне от 0 до RAND_MAX (обычно 32767).

	srand(time(0));   // Устанавливает начальное значение (seed) для генератора. А мы сейчас привязываем к времени, чтобы были рандомные числа.

	int result1 = 1 + rand() % 20;    // Рандомное число в диапазоне от 1 до 20

	cout << "Рандомное число - " << result1;


	return 0;
}
*/


// || Циклы For, While, Do While || игра угадай число ||

/*
int main() {
	setlocale(LC_ALL, "RU");

	
	// Цикл for                                                  (начало цикла ; условие работы цикла, то есть конец ; шаг цикла)
	for (int i = 1; i <= 10; i++)          
		cout << "for. Number i: " << i << endl;
	
	// Цикл while                                                прописывается только условие для цикла
	int j = 1;
	while (j <= 10) {                                   
		cout << "while. Number j: " << j << endl;
		j++;
	}

	// Цикл do while                                             тоже самое что while, но цикл 1 раз точно выполняется, а потом уже проверяет условие
	int l = 100;
	do {
		cout << "do while. Number l: " << l << endl;
		l -= 10;
	} while (l < 10);




	cout << "\n\n\n\n Операторы в циклах (на примере цикла for) \n\n";

	for (int k = 1; k < 15; k++) {
		if (k == 10) break;                                             // break - выход из цикла
		
		if (k % 2 == 0) continue;                                       // continue - пропускает текущую итерацию цикла и сразу переходит к следующему кругу

		cout << "Number k : " << k << endl;
	}




	cout << "\n\n\n\n Практический пример - игра угадай число! \n\n";

	srand(time(0));
	int rand_num = 1 + rand() % 15;
	bool stop = false;
	int user_input;

	do {
		cout << "Введите число: ";
		cin >> user_input;
		if (user_input != rand_num)
			cout << "Вы не угадали \n";
		else stop = true;
	} while (!stop);
	cout << "Вы угадали!";

	return 0;

}
*/


// || Массивы  одномерные и многомерные, базовые понятия ||

/*
int main() {
	setlocale(LC_ALL, "RU");

	int nums[3];                              // при создании массива указываем сколько у него будет элементов в квадратных скобках
	nums[0] = 56;                             // индексы массивов начинаются с нуля!
	nums[1] = 563;                            // заполняем элементы массивы по отдельности
	nums[2] = 2;

	nums[1] = 0;
	nums[1]++;

	cout << nums[1] << endl;                  // выводим элемент массива


	float nums2[5] = { 4,6,7 };               // заполняем элементы массивы все вместе или можно не все, а первые несколько


	for (int i = 0; i < 3; i++)                                                    // выводим все элементы массива
		cout << "Элемент под индексом " << i << " - " << nums[i] << endl;



	cout << "\n\n\n\n Практика. Заполнение массива \n\n";

	float mas[5];
	for (int i = 0; i < 5; i++) {
		cout << "Введите число для элемента массива под индексом " << i << " - ";
		cin >> mas[i];
	}
	cout << "Получился такой массив - ";
	for (int i = 0; i < 5; i++)
		cout << mas[i] << " ";

	cout << endl << endl << "Многомерные массивы" << endl;

	// Многомерные массивы

	int matrix[3][2] = { {3,5},{5,8},{-2,0} };              // при создании также указываем в первых скобках размерность массива
	cout << matrix[1][1] << endl;	                        // и также указываем во вторых скобках размерность каждого вложенного массива

	for (int j = 0; j < 3; j++) {
		for (int l = 0; l < 2;l++)
			cout << matrix[j][l] << " ";
	}

	return 0;
}
*/


// || Динамическая память || динамические массивы ||

/*
int main() {
	setlocale(LC_ALL, "RU");

	int* nums = new int[3];            // занимаем память для массива
	nums[0] = 45;
	cout << nums[0] << endl;
	delete[] nums;                     // очищаем память

	return 0;
}
*/


// || Строки ||


int main() {
	setlocale(LC_ALL, "RU");
	
	char word[] = "Hi !";        // { 'H', 'I', ' ', '!'};               // метод старого языка "С",  тогда не было другого способа
	for (int i = 0; i < 4;i++) cout << word[i];


	string words = "Hello World!";                                      // актуальный метод 
	words[0] = 'W';
	cout << endl << words << endl;


	cout << "Введите строчку - ";
	cin >> words;
	cout << "new string - " << words;
	

	return 0;
}