#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <string>

using namespace std;

// Структура для хранения значения и его вероятности
struct ValueWithProbability {
    double value;            // значение случайной величины
    double probability;      // вероятность этого значения
};

// Функция для ввода ряда с вероятностями
vector<ValueWithProbability> input_series_with_probabilities(const string& name) {
    vector<ValueWithProbability> series;         // создаём пустой ряд
    int n;
    cout << "Введите количество элементов в ряду " << name << ": ";
    cin >> n;

    cout << "Введите " << n << " пар (значение вероятность) для ряда " << name << ":\n";
    double total_prob = 0.0;

    for (int i = 0; i < n; i++) {
        double value, prob;
        cin >> value >> prob;         // вводим значение и вероятность
        series.push_back({ value, prob });     // добавляем в ряд
        total_prob += prob;            // считаем сумму вероятностей
    }

    // Проверка суммы вероятностей
    if (abs(total_prob - 1.0) > 1e-6) {
        cout << "Ошибка: сумма вероятностей должна быть равна 1.0!\n";
        exit(1);          // аварийный выход из программы
    }

    return series;         // возвращаем заполненный ряд
}

// Математическое ожидание (с учетом вероятностей)
long double calculate_mean(const vector<ValueWithProbability>& series) {
    long double mean = 0.0;
    for (const auto& item : series) {
        mean += static_cast<long double>(item.value) * static_cast<long double>(item.probability);
    }
    return mean;
}

// Дисперсия (с учетом вероятностей)
double calculate_variance(const vector<ValueWithProbability>& series) {
    double mean = calculate_mean(series);
    double variance = 0.0;
    for (const auto& item : series) {
        variance += pow(item.value - mean, 2) * item.probability;
    }
    return variance;
}

// Среднеквадратичное отклонение
double calculate_stddev(const vector<ValueWithProbability>& series) {
    return sqrt(calculate_variance(series));
}

// Центральные моменты (α^1 - α^5)
vector<double> calculate_central_moments(const vector<ValueWithProbability>& series) {
    vector<double> moments(5, 0.0);
    long double mean = calculate_mean(series);

    //cout << "Вычисление центральных моментов (mean = " << mean << "):\n"; // Вывод для отладки

    for (int k = 1; k <= 5; k++) {
        long double moment_sum = 0.0;
        //cout << "Момент порядка " << k << ":\n"; // Вывод для отладки

        for (const auto& item : series) {
            long double diff = static_cast<long double>(item.value) - mean;
            long double term = pow(diff, k) * static_cast<long double>(item.probability);

            // Проверка на переполнение
            if (abs(term) > numeric_limits<double>::max()) {
                cerr << "Ошибка: переполнение при вычислении момента порядка " << k << endl;
                exit(1); // Завершаем программу при переполнении
            }

            moment_sum += term;
            //cout << (item.value) << "  (x - mean)^" << k << " * p = (" << diff << ")^" << k << " * " << item.probability << " = " << term << endl; // Вывод для отладки
        }

        moments[k - 1] = static_cast<double>(moment_sum); // Преобразуем обратно в double
        //cout << "  Сумма: " << moment_sum << endl; // Вывод для отладки
    }

    // Корректировка первого момента (он должен быть 0)
    if (std::abs(moments[0]) < 1e-12) moments[0] = 0.0;

    return moments;
}

// Начальные моменты (μ^1 - μ^5)
vector<double> calculate_raw_moments(const vector<ValueWithProbability>& series) {
    vector<double> moments(5, 0.0);
    for (int k = 1; k <= 5; k++) {
        for (const auto& item : series) {
            moments[k - 1] += pow(item.value, k) * item.probability;
        }
    }
    return moments;
}

// Коэффициент асимметрии
double calculate_skewness(const vector<ValueWithProbability>& series) {
    double stddev = calculate_stddev(series);
    if (stddev == 0) return 0;
    vector<double> cm = calculate_central_moments(series);
    return cm[2] / pow(stddev, 3);
}

// Коэффициент эксцесса
double calculate_kurtosis(const vector<ValueWithProbability>& series) {
    double stddev = calculate_stddev(series);
    if (stddev == 0) return 0;
    vector<double> cm = calculate_central_moments(series);
    return cm[3] / pow(stddev, 4) - 3;
}

// Вывод характеристик ряда
void print_series_stats(const vector<ValueWithProbability>& series, const string& name) {
    cout << "\n─────────────────────────────────────\n";
    cout << "Характеристики ряда " << name << ":\n";
    cout << "1. Математическое ожидание: " << calculate_mean(series) << endl;
    cout << "2. Дисперсия: " << calculate_variance(series) << endl;
    cout << "3. Среднеквадратичное отклонение: " << calculate_stddev(series) << endl;

    vector<double> cm = calculate_central_moments(series);
    cout << "4. Центральные моменты:\n";
    for (int i = 0; i < 5; i++) {
        cout << "   α^" << i + 1 << ": " << cm[i] << endl;
    }

    vector<double> rm = calculate_raw_moments(series);
    cout << "5. Начальные моменты:\n";
    for (int i = 0; i < 5; i++) {
        cout << "   μ^" << i + 1 << ": " << rm[i] << endl;
    }

    cout << "6. Коэффициент асимметрии (A): " << calculate_skewness(series) << endl;
    cout << "7. Коэффициент эксцесса (E): " << calculate_kurtosis(series) << endl;
    cout << "─────────────────────────────────────\n";
}

// Операции с рядами (создание новых распределений)
vector<ValueWithProbability> add_constant(const vector<ValueWithProbability>& series, double constant) {
    vector<ValueWithProbability> result;
    for (const auto& item : series) {
        result.push_back({ item.value + constant, item.probability });
    }
    return result;
}

vector<ValueWithProbability> multiply_constant(const vector<ValueWithProbability>& series, double constant) {
    vector<ValueWithProbability> result;
    for (const auto& item : series) {
        result.push_back({ item.value * constant, item.probability });
    }
    return result;
}

vector<ValueWithProbability> power_series(const vector<ValueWithProbability>& series, int power) {
    vector<ValueWithProbability> result;
    for (const auto& item : series) {
        result.push_back({ pow(item.value, power), item.probability });
    }
    return result;
}

// Комбинирование двух рядов (для суммы, разности, произведения)
vector<ValueWithProbability> combine_series(
    const vector<ValueWithProbability>& s1,
    const vector<ValueWithProbability>& s2,
    double (*op)(double, double)
) {
    vector<ValueWithProbability> result;
    for (const auto& item1 : s1) {
        for (const auto& item2 : s2) {
            double new_value = op(item1.value, item2.value);
            double new_prob = item1.probability * item2.probability;
            result.push_back({ new_value, new_prob });
        }
    }
    return result;
}

// Операции для combine_series
double add_op(double a, double b) { return a + b; }
double sub_op(double a, double b) { return a - b; }
double mul_op(double a, double b) { return a * b; }

int main() {
    setlocale(LC_ALL, "RU");
    cout << "=== Ввод рядов распределений ===\n";
    vector<ValueWithProbability> X = input_series_with_probabilities("X");
    vector<ValueWithProbability> Y = input_series_with_probabilities("Y");

    // Ввод констант
    double a, b;
    cout << "\nВведите константу a для ряда X: ";
    cin >> a;
    cout << "Введите константу b для ряда Y: ";
    cin >> b;

    // Ввод степени для степенного ряда
    int power;
    cout << "Введите степень для степенного ряда: ";
    cin >> power;

    // Вычисление преобразованных рядов
    vector<ValueWithProbability> X_plus_a = add_constant(X, a);
    vector<ValueWithProbability> Y_plus_b = add_constant(Y, b);
    vector<ValueWithProbability> X_times_a = multiply_constant(X, a);

    vector<ValueWithProbability> X_plus_Y = combine_series(X, Y, add_op);
    vector<ValueWithProbability> X_minus_Y = combine_series(X, Y, sub_op);
    vector<ValueWithProbability> X_times_Y = combine_series(X, Y, mul_op);

    vector<ValueWithProbability> X_pow = power_series(X, power);

    // Вывод характеристик
    cout << "\n=== Результаты расчетов ===\n";
    print_series_stats(X, "X (исходный)");
    print_series_stats(Y, "Y (исходный)");

    print_series_stats(X_plus_a, "X + a");
    print_series_stats(Y_plus_b, "Y + b");
    print_series_stats(X_times_a, "X * a");

    print_series_stats(X_plus_Y, "X + Y");
    print_series_stats(X_minus_Y, "X - Y");
    print_series_stats(X_times_Y, "X * Y");

    print_series_stats(X_pow, "X^" + to_string(power));

    return 0;
}