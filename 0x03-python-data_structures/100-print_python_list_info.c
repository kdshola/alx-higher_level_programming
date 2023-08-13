#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list information
 * @p: Python object
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), i = 0;
	PyListObject *list;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %d\n", list->allocated);
	for (; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
