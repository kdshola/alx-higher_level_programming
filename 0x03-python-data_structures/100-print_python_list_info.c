#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints python list information
 * @p: Python object
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *list;
	PyObject *item;

	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (; i < list->ob_base.ob_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
