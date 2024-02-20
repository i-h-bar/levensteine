#include<pybind11/pybind11.h>
#include<vector>
#include<string>
#include<algorithm>


int cppdist(const std::string &string1, const std::string &string2) {
    const int size1 = string1.size() + 1;
    const int size2 = string2.size() + 1;
    std::vector<std::vector<int>> matrix(size1, std::vector<int>(size2));

    for (int i = 0; i < size1; i++) {
        matrix[i][0] = i;
    }

    for (int i = 1; i < size2; i++) {
        matrix[0][i] = i;
    }

    for (int i = 1; i < size1; i++) {
        for (int j = 1; j < size2; j++) {
            if (string1[i-1] == string2[j-1]) {
                matrix[i][j] = matrix[i-1][j-1];
            }
            else {
                matrix[i][j] = (std::min(std::min(matrix[i-1][j], matrix[i][j-1]), matrix[i-1][ j-1])) + 1;
            }
        }
    }

    return matrix[size1 - 1][size2 - 1];
}


PYBIND11_MODULE(cpplev, handle) {
    handle.doc() = "Lev Dist";
    handle.def("cppdist", &cppdist);
}