#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - prints the list of info
 *
 * @p: pyObject
 *
 * Return: no return
 */
void print_python_list_info(pyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_getItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
