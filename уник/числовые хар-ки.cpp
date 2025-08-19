
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <map>
#include <iomanip>
#include <limits> // numeric_limits

using namespace std;

// Структура для хранения ряда распределения
struct Distribution {
    vector<double> values;
    vector<double> probabilities;
};

// Структура для хранения статистических характеристик
struct Statistics {
    double mean;
    double variance;
    double standard_deviation;
    vector<double> central_moments;
    vector<double> initial_moments;
    double excess_kurtosis;
    double skewness;
};

// Функция для вычисления математического ожидания
double calculate_mean(const Distribution& dist) {
    double mean = 0.0;
    for (size_t i = 0; i < dist.values.size(); ++i) {
        mean += dist.values[i] * dist.probabilities[i];
    }
    return mean;
}

// Функция для вычисления дисперсии
double calculate_variance(const Distribution& dist) {
    double mean = calculate_mean(dist);
    double variance = 0.0;
    for (size_t i = 0; i < dist.values.size(); ++i) {
        variance += dist.probabilities[i] * pow(dist.values[i] - mean, 2);
    }
    return variance;
}

// Функция для вычисления среднеквадратичного отклонения
double calculate_standard_deviation(const Distribution& dist) {
    return sqrt(calculate_variance(dist));
}

// Функция для вычисления центрального момента заданного порядка
double calculate_central_moment(const Distribution& dist, int order) {
    double mean = calculate_mean(dist);
    double moment = 0.0;
    for (size_t i = 0; i < dist.values.size(); ++i) {
        moment += dist.probabilities[i] * pow(dist.values[i] - mean, order);
    }
    return moment;
}

// Функция для вычисления начального момента заданного порядка
double calculate_initial_moment(const Distribution& dist, int order) {
    double moment = 0.0;
    for (size_t i = 0; i < dist.values.size(); ++i) {
        moment += dist.probabilities[i] * pow(dist.values[i], order);
    }
    return moment;
}

// Функция для вычисления коэффициента эксцесса
double calculate_excess_kurtosis(const Distribution& dist) {
    double central_4 = calculate_central_moment(dist, 4);
    double variance = calculate_variance(dist);
    return central_4 / pow(variance, 2) - 3;
}

// Функция для вычисления коэффициента асимметрии
double calculate_skewness(const Distribution& dist) {
    double central_3 = calculate_central_moment(dist, 3);
    double standard_deviation = calculate_standard_deviation(dist);
    return central_3 / pow(standard_deviation, 3);
}

// Функция для вычисления статистических характеристик ряда
Statistics calculate_statistics(const Distribution& dist) {
    Statistics stats;

    stats.mean = calculate_mean(dist);
    stats.variance = calculate_variance(dist);
    stats.standard_deviation = calculate_standard_deviation(dist);

    // Вычисляем центральные моменты до 5-го порядка
    stats.central_moments.resize(5);
    for (int i = 0; i < 5; ++i) {
        stats.central_moments[i] = calculate_central_moment(dist, i + 1);
    }

    // Вычисляем начальные моменты до 2-го порядка
    stats.initial_moments.resize(2);
    for (int i = 0; i < 2; ++i) {
        stats.initial_moments[i] = calculate_initial_moment(dist, i + 1);
    }

    stats.excess_kurtosis = calculate_excess_kurtosis(dist);
    stats.skewness = calculate_skewness(dist);

    return stats;
}

// Функция для создания ряда распределения
Distribution create_distribution(const vector<double>& values, const vector<double>& probabilities) {
    Distribution dist;
    dist.values = values;
    dist.probabilities = probabilities;
    return dist;
}

// Функция для сложения двух рядов распределения
Distribution sum_distributions(const Distribution& dist1, const Distribution& dist2) {
    map<double, double> sum_probabilities;
    for (size_t i = 0; i < dist1.values.size(); ++i) {
        for (size_t j = 0; j < dist2.values.size(); ++j) {
            double sum = dist1.values[i] + dist2.values[j];
            double probability = dist1.probabilities[i] * dist2.probabilities[j];

            if (sum_probabilities.find(sum) == sum_probabilities.end()) {
                sum_probabilities[sum] = probability;
            }
            else {
                sum_probabilities[sum] += probability;
            }
        }
    }

    Distribution result;
    for (const auto& pair : sum_probabilities) {
        result.values.push_back(pair.first);
        result.probabilities.push_back(pair.second);
    }

    return result;
}

// Функция для вычитания двух рядов распределения
Distribution subtract_distributions(const Distribution& dist1, const Distribution& dist2) {
    map<double, double> diff_probabilities;
    for (size_t i = 0; i < dist1.values.size(); ++i) {
        for (size_t j = 0; j < dist2.values.size(); ++j) {
            double diff = dist1.values[i] - dist2.values[j];
            double probability = dist1.probabilities[i] * dist2.probabilities[j];

            if (diff_probabilities.find(diff) == diff_probabilities.end()) {
                diff_probabilities[diff] = probability;
            }
            else {
                diff_probabilities[diff] += probability;
            }
        }
    }

    Distribution result;
    for (const auto& pair : diff_probabilities) {
        result.values.push_back(pair.first);
        result.probabilities.push_back(pair.second);
    }

    return result;
}

// Функция для умножения двух рядов распределения
Distribution multiply_distributions(const Distribution& dist1, const Distribution& dist2) {
    map<double, double> product_probabilities;
    for (size_t i = 0; i < dist1.values.size(); ++i) {
        for (size_t j = 0; j < dist2.values.size(); ++j) {
            double product = dist1.values[i] * dist2.values[j];
            double probability = dist1.probabilities[i] * dist2.probabilities[j];

            if (product_probabilities.find(product) == product_probabilities.end()) {
                product_probabilities[product] = probability;
            }
            else {
                product_probabilities[product] += probability;
            }
        }
    }

    Distribution result;
    for (const auto& pair : product_probabilities) {
        result.values.push_back(pair.first);
        result.probabilities.push_back(pair.second);
    }

    return result;
}

// Функция для умножения ряда распределения на константу
Distribution constant_multiply(const Distribution& dist, double constant) {
    Distribution result = dist;
    for (size_t i = 0; i < result.values.size(); ++i) {
        result.values[i] *= constant;
    }
    return result;
}

// Функция для добавления константы к ряду распределения
Distribution constant_add(const Distribution& dist, double constant) {
    Distribution result = dist;
    for (size_t i = 0; i < result.values.size(); ++i) {
        result.values[i] += constant;
    }
    return result;
}

// Функция для возведения ряда распределения в степень
Distribution power_distribution(const Distribution& dist, int power) {
    Distribution result = dist;
    for (size_t i = 0; i < result.values.size(); ++i) {
        result.values[i] = pow(result.values[i], power);
    }
    return result;
}

// Функция для вывода ряда распределения
void print_distribution(const Distribution& dist) {
    cout << "Значения: ";
    for (double val : dist.values) {
        cout << val << " ";
    }
    cout << endl;

    cout << "Вероятности: ";
    for (double prob : dist.probabilities) {
        cout << prob << " ";
    }
    cout << endl;
}

// Функция для вывода статистических характеристик
void print_statistics(const Statistics& stats) {
    cout << "Математическое ожидание: " << stats.mean << endl;
    cout << "Дисперсия: " << stats.variance << endl;
    cout << "Среднеквадратичное отклонение: " << stats.standard_deviation << endl;

    cout << "Центральные моменты: ";
    for (double moment : stats.central_moments) {
        cout << moment << " ";
    }
    cout << endl;

    cout << "Начальные моменты: ";
    for (double moment : stats.initial_moments) {
        cout << moment << " ";
    }
    cout << endl;

    cout << "Коэффициент эксцесса: " << stats.excess_kurtosis << endl;
    cout << "Коэффициент асимметрии: " << stats.skewness << endl;
}

int main() {
    setlocale(LC_ALL, "RU");
    int n, m;

    // Ввод данных для X
    cout << "Введите количество значений для X: ";
    cin >> n;

    if (cin.fail() || n <= 0) {
        cout << "Ошибка: Введено некорректное количество значений." << endl;
        return 1;
    }

    vector<double> x_values(n);
    vector<double> x_probabilities(n);

    cout << "Введите значения для X:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "Значение " << i + 1 << ": ";
        cin >> x_values[i];
        if (cin.fail()) {
            cout << "Ошибка: Введено некорректное значение." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return 1;
        }
    }

    cout << "Введите вероятности для X:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "Вероятность " << i + 1 << ": ";
        cin >> x_probabilities[i];
        if (cin.fail()) {
            cout << "Ошибка: Введена некорректная вероятность." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return 1;
        }
    }

    // Ввод данных для Y
    cout << "Введите количество значений для Y: ";
    cin >> m;
    if (cin.fail() || m <= 0) {
        cout << "Ошибка: Введено некорректное количество значений." << endl;
        return 1;
    }

    vector<double> y_values(m);
    vector<double> y_probabilities(m);

    cout << "Введите значения для Y:" << endl;
    for (int i = 0; i < m; ++i) {
        cout << "Значение " << i + 1 << ": ";
        cin >> y_values[i];
        if (cin.fail()) {
            cout << "Ошибка: Введено некорректное значение." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return 1;
        }
    }

    cout << "Введите вероятности для Y:" << endl;
    for (int i = 0; i < m; ++i) {
        cout << "Вероятность " << i + 1 << ": ";
        cin >> y_probabilities[i];
        if (cin.fail()) {
            cout << "Ошибка: Введена некорректная вероятность." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return 1;
        }
    }

    // Создаем ряды распределения
    Distribution dist_x = create_distribution(x_values, x_probabilities);
    Distribution dist_y = create_distribution(y_values, y_probabilities);

    //Проверка, что сумма вероятностей = 1
    double sum_x = accumulate(x_probabilities.begin(), x_probabilities.end(), 0.0);
    double sum_y = accumulate(y_probabilities.begin(), y_probabilities.end(), 0.0);

    if (abs(sum_x - 1.0) > 1e-6 || abs(sum_y - 1.0) > 1e-6) {
        cout << "Ошибка: Сумма вероятностей должна быть равна 1." << endl;
        return 1;
    }

    //Пример: 2X + 3Y
    Distribution dist_2x = constant_multiply(dist_x, 2);
    Distribution dist_3y = constant_multiply(dist_y, 3);
    Distribution dist_2x_plus_3y = sum_distributions(dist_2x, dist_3y);

    cout << "Распределение 2X + 3Y:" << endl;
    print_distribution(dist_2x_plus_3y);

    Statistics stats_2x_plus_3y = calculate_statistics(dist_2x_plus_3y);
    cout << "\nСтатистика для 2X + 3Y:" << endl;
    print_statistics(stats_2x_plus_3y);

    // Пример: Вычисление статистики для X
    Statistics stats_x = calculate_statistics(dist_x);

    cout << "\nСтатистика для X:" << endl;
    print_statistics(stats_x);

    // Пример: Вычисление статистики для Y
    Statistics stats_y = calculate_statistics(dist_y);

    cout << "\nСтатистика для Y:" << endl;
    print_statistics(stats_y);

    //Пример: x^2
    Distribution dist_x_squared = power_distribution(dist_x, 2);
    cout << "\nРаспределение x^2:" << endl;
    print_distribution(dist_x_squared);

    Statistics stats_x_squared = calculate_statistics(dist_x_squared);
    cout << "\nСтатистика для x^2:" << endl;
    print_statistics(stats_x_squared);

    return 0;
}
