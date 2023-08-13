#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list information
 * @p: Python object
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), itr = 0;
	PyListObject *list;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %d\n", list->allocated);
	for (; itr < size; itr++)
	{
		item = PyList_GetItem(p, itr);
		printf("Element %d: %s\n", itr, Py_TYPE(item)->tp_name);
	}
}
