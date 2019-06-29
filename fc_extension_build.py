from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("""double * fc(double zr, double zi, double cr, double ci);
                int bailout(double zr, double zi, double radius);""")

ffibuilder.set_source("_fc",
    """ 
        #include "fc.h"',
    """,
    sources=["fc.c"])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)