#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        int sum_C = 0;
        double sum_total = 0.0;

        for (int j = 0; j < N; j++) {
            int C;
            double G;
            cin >> C >> G;

            sum_C += C;
            sum_total += C * G;
        }

        double avg = sum_total / sum_C;

        cout << sum_C << " " << fixed << setprecision(1) << avg << "\n";
    }

    return 0;
}
