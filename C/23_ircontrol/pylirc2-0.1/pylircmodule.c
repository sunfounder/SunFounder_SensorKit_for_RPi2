
 /**************************************************************************\
 ** pylircmoduke.c                                                         **
 ****************************************************************************
 **                                                                        **
 ** pyLirc, lirc (remote control) module for python                        **
 ** Copyright (C) 2002 Linus McCabe <pylirc.linus@mccabe.nu>               **
 **                                                                        **
 ** This library is free software; you can redistribute it and/or          **
 ** modify it under the terms of the GNU Lesser General Public             **
 ** License as published by the Free Software Foundation; either           **
 ** version 2.1 of the License, or (at your option) any later version.     **
 **                                                                        **
 ** This library is distributed in the hope that it will be useful,        **
 ** but WITHOUT ANY WARRANTY; without even the implied warranty of         **
 ** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU      **
 ** Lesser General Public License for more details.                        **
 **                                                                        **
 ** You should have received a copy of the GNU Lesser General Public       **
 ** License along with this library; if not, write to the Free Software    **
 ** Foundation, Inc., 59 Temple Place, Suite 330, Boston MA 02111-1307 USA **
 **                                                                        **
 \**************************************************************************/

// $Id: pylircmodule.c,v 1.8 2005/01/07 16:50:37 mccabe Exp $

#ifdef HAVE_CONFIG_H
# include <config.h>
#endif

#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lirc/lirc_client.h"
#include <Python.h>

// Lirc programname
char *progname;

// boolean telling if we're initialized or not
int intInitialized = 0;
int intSocket = 0;

// Pointer to lirc's config
struct lirc_config *config;

// Prototypes - Python functions
static PyObject * pylirc_init(PyObject *, PyObject *);
static PyObject * pylirc_exit(PyObject *, PyObject *);
static PyObject * pylirc_nextcode(PyObject *, PyObject *);
static PyObject * pylirc_blocking(PyObject *, PyObject *);

// Prototypes - internal functions
int SetMode(int);

// pylirc_init
// Function:   Initialize the lirc communication
// Arguments:  lircname (string), name of program as used in lirc fonig
//             configname (string), optional filename of lirc configuration
//             blocking (int), optional flag wether or not we want blocking mode
// Returns:    lirc socket
//
static PyObject * pylirc_init(self, args)
   PyObject *self;
   PyObject *args; {

   char *lircname;
   char *configname = NULL;
   int intBlocking = 0;

   // Just return if already initialized...
   if(intInitialized)
      return NULL;

   // Check if we got the right arguments..
   if (!PyArg_ParseTuple(args, "s|si", &lircname, &configname, &intBlocking)) {
      PyErr_SetString(PyExc_ValueError, "Wrong number of arguments!");
      return NULL;
   }

   // initialize lirc
   intSocket = lirc_init(lircname, 1);
   if(intSocket == -1) {
      PyErr_SetString(PyExc_RuntimeError, "Unable to initialize lirc!");
      return NULL;
   }

   // Set nonblocking mode (now optional)
   SetMode(intBlocking);


   // Read configuration
   if(!lirc_readconfig(configname, &config, NULL) == 0) {
      lirc_deinit();
      PyErr_SetString(PyExc_IOError, "Unable to read configuration!");
      return NULL;
   }

   // set flag and return
   intInitialized = 1;
   return Py_BuildValue("i", intSocket);
}


// pylirc_exit
// Function:   Shut down the lirc communication
// Arguments:  none
// Returns:    true on success
//
static PyObject * pylirc_exit(self, args)
   PyObject *self;
   PyObject *args; {

   // Only do this if we're really initialized...
   if(intInitialized) {
      intInitialized = 0;

      // Free the lirc config
      lirc_freeconfig(config);

      // lirc DeInit()
      if(lirc_deinit() == -1) {
         PyErr_SetString(PyExc_RuntimeError, "Unable to deinit!");
         return NULL;
      }
   }

   // Return
   return Py_BuildValue("i", 1);
}


// pylirc_nextcode
// Function:   Reads queued commands
// Arguments:  none
// Returns:    a list of commands (lirc config-strings)
//             or a 'None' if nothing is queued
//
static PyObject * pylirc_nextcode(self, args)
   PyObject *self;
   PyObject *args; {

   char *code, *c;
   PyObject *poTemp;
   int intExtended = 0;
   unsigned int intRepeatCount;

   // Get arguments
   if (!PyArg_ParseTuple(args, "|i", &intExtended)) {

      // I guess this one cannot fail, but for completeness
      PyErr_SetString(PyExc_ValueError, "Wrong number of arguments!");
      return NULL;
   }

   // Returnvalue = 'None' (will change upon success)
   poTemp =  Py_BuildValue("");

   // Check if there is anything in the queue
   if(lirc_nextcode(&code) != -1) {

      // If code isn't NULL...
      if(code) {

    // Translate the string from configfile
    lirc_code2char(config, code, &c);

    if (c)
      {
        // Returnvalue = empty list
        poTemp = PyList_New(0);

        // If the list-creation was successful
        if(poTemp) {

          // If success...
          while(c) {

        if(intExtended) {
          // Extended api - returns a list
          // Thanks alot to Brian J. Murrell for the contribution!

                  // Extract the repeat value from the code
                  if (sscanf(code, "%*s %x %*s %*s\n", &intRepeatCount) != 1)
                     // some kind of error getting the repeat value, shouldnt happen...
                     intRepeatCount = 0;

                  // Append the read code and repeat tuple to the list
                  PyList_Append(poTemp, Py_BuildValue("{s:s, s:i}", "config", c, "repeat", intRepeatCount));

               } else {
                  // Old api

                  // Appen the read code to the list
                  PyList_Append(poTemp, Py_BuildValue("s", c));
        }

        // Read the next code
        lirc_code2char(config, code, &c);
          }
        }
      }

    // Free the memory
    free(code);
      }


   }
   // Return a list or 'None'
   return poTemp;

}


// pylirc_blocking
// Function:   Set or unset blocking mode
// Arguments:  boolean wether or not to use blocking mode
// Returns:    true on success
//
static PyObject * pylirc_blocking(self, args)
   PyObject *self;
   PyObject *args; {

   int intBlocking = 0;

   // Read arguments
   if (!PyArg_ParseTuple(args, "i", &intBlocking)) {
      PyErr_SetString(PyExc_ValueError, "Wrong arguments!");
      return NULL;
   }

   intBlocking = SetMode(intBlocking);
   // Return
   return Py_BuildValue("i", intBlocking);
}

// SetMode
// Function:   Slavefunction, called in pylirc_init() and pylirc_blocking()
//             to set or unset blocking mode
// Arguments:  none
// Returns:    true on success
//
int SetMode(int intBlocking) {
   int flags;

   fcntl(intSocket, F_SETOWN, getpid());
   flags = fcntl(intSocket, F_GETFL, 0);
   if(flags != -1) {
      fcntl(intSocket, F_SETFL, (flags & ~O_NONBLOCK) | (intBlocking ? 0 : O_NONBLOCK));
      return -1;
   }

   return 0;
}

// Python function table
static PyMethodDef pylircMethods[] = {
    {"init",  pylirc_init, METH_VARARGS, "Register a lirc program."},
    {"exit",  pylirc_exit, METH_VARARGS, "Unregister a lirc program."},
    {"blocking",  pylirc_blocking, METH_VARARGS, "Sets wether or not to use blocking mode."},
    {"nextcode",  pylirc_nextcode, METH_VARARGS, "Poll queued codes (or wait until one arrives if in blocking mode)."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

// Python init function
//void initpylirc(void) {
//    (void) Py_InitModule("pylirc", pylircMethods);
//}

#if PY_MAJOR_VERSION >= 3

struct module_state {
PyObject *error;
};

#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))

static int pylircTraverse(PyObject *m, visitproc visit, void *arg) {
Py_VISIT(GETSTATE(m)->error);
return 0;
}

static int pylircClear(PyObject *m) {
Py_CLEAR(GETSTATE(m)->error);
return 0;
}

static struct PyModuleDef moduledef = {
PyModuleDef_HEAD_INIT,
"pylirc",
NULL,
sizeof(struct module_state),
pylircMethods,
NULL,
pylircTraverse,
pylircClear,
NULL
};

PyObject * PyInit_pylirc(void)
{
PyObject *module = PyModule_Create(&moduledef);
if (module == NULL)
return NULL;
struct module_state *st = GETSTATE(module);

st->error = PyErr_NewException("pylirc.Error", NULL, NULL);
if (st->error == NULL) {
    Py_DECREF(module);
    return NULL;
}

return module;
}
#else
// Python init function
void initpylirc(void) {
(void) Py_InitModule("pylirc", pylircMethods);
}
#endif