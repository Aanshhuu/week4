#include <pybind11/pybind11.h>

class Rectangle {
private:
    double width;
    double height;

public:
    // Constructor
    Rectangle(double w, double h) : width(w), height(h) {}

    // To calculate the area
    double area() const {
        return width * height;
    }

    // To calculate the perimeter
    double perimeter() const {
        return 2 * (width + height);
    }

    // Setters
    void setWidth(double w) {
        width = w;
    }

    void setHeight(double h) {
        height = h;
    }

    // Getters
    double getWidth() const {
        return width;
    }

    double getHeight() const {
        return height;
    }
};

namespace py = pybind11;

PYBIND11_MODULE(rectangle, m) {
    py::class_<Rectangle>(m, "Rectangle")
        .def(py::init<double, double>())  
        .def("area", &Rectangle::area)    
        .def("perimeter", &Rectangle::perimeter)  
        .def("setWidth", &Rectangle::setWidth)  
        .def("setHeight", &Rectangle::setHeight)
        .def("getWidth", &Rectangle::getWidth)  
        .def("getHeight", &Rectangle::getHeight);
}
