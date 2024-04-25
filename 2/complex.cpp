#include <iostream>
#include <complex>
#include <limits>

using namespace std;

complex<double> func(complex<double> z) {
    return pow(z, 3.0) - 1.0;
}

complex<double> der(complex<double> z) {
    return 3.0 * pow(z, 2.0);
}

complex<double> newton(complex<double> init, double eps, int iters) {
    complex<double> z = init;
    int curr_iters = 0;

    while (abs(func(z)) > eps && curr_iters < iters) {
        z = z - func(z) / der(z);
        curr_iters++;
    }

    return z;
}

int determineRoot(const complex<double>& z, double eps, int iters) {
    complex<double> root1 = 1.0;
    complex<double> root2 = -0.5 + 0.5i * sqrt(3);
    complex<double> root3 = -0.5 - 0.5i * sqrt(3);

    complex<double> newton_result = newton(z, eps, iters);

    if (abs(newton_result - root1) < eps)
        return 1;
    else if (abs(newton_result - root2) < eps)
        return 2;
    else if (abs(newton_result - root3) < eps)
        return 3;
    else
        return 0; 
}

int main() {
    double eps = 1e-6;
    int iters = 1000;

    double x_min = -2.0;
    double x_max = 2.0;
    double y_min = -2.0;
    double y_max = 2.0;
    double step = 0.1;

    double root1_min_x = numeric_limits<double>::max();
    double root1_max_x = numeric_limits<double>::lowest();
    double root1_min_y = numeric_limits<double>::max();
    double root1_max_y = numeric_limits<double>::lowest();

    double root2_min_x = numeric_limits<double>::max();
    double root2_max_x = numeric_limits<double>::lowest();
    double root2_min_y = numeric_limits<double>::max();
    double root2_max_y = numeric_limits<double>::lowest();

    double root3_min_x = numeric_limits<double>::max();
    double root3_max_x = numeric_limits<double>::lowest();
    double root3_min_y = numeric_limits<double>::max();
    double root3_max_y = numeric_limits<double>::lowest();

    for (double x = x_min; x <= x_max; x += step) {
        for (double y = y_min; y <= y_max; y += step) {
            complex<double> init_point(x, y);
            int root = determineRoot(init_point, eps, iters);

            if (root == 1) {
                if (x < root1_min_x) root1_min_x = x;
                if (x > root1_max_x) root1_max_x = x;
                if (y < root1_min_y) root1_min_y = y;
                if (y > root1_max_y) root1_max_y = y;
            }
            else if (root == 2) {
                if (x < root2_min_x) root2_min_x = x;
                if (x > root2_max_x) root2_max_x = x;
                if (y < root2_min_y) root2_min_y = y;
                if (y > root2_max_y) root2_max_y = y;
            }
            else if (root == 3) {
                if (x < root3_min_x) root3_min_x = x;
                if (x > root3_max_x) root3_max_x = x;
                if (y < root3_min_y) root3_min_y = y;
                if (y > root3_max_y) root3_max_y = y;
            }
        }
    }


    cout << "Approximate boundaries of attraction regions for roots of z^3 - 1:\n";

    cout << "Root 1: x = [" << root1_min_x << ", " << root1_max_x << "], y = [" 
        << root1_min_y << ", " << root1_max_y << "]\n";

    cout << "Root 2: x = [" << root2_min_x << ", " << root2_max_x << "], y = [" 
        << root2_min_y << ", " << root2_max_y << "]\n";

    cout << "Root 3: x = [" << root3_min_x << ", " << root3_max_x << "], y = [" 
        << root3_min_y << ", " << root3_max_y << "]\n";

    return 0;
}
