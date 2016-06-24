using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using nom.tam.fits;
using nom.tam.util;
using nom.tam.image;

namespace ConsoleApplication2.astro {

    class cubo {

        private String nombre;
        private int num_dimensiones;
        private int eje_x;
        private int eje_y;
        private int eje_z;
        private Fits datos;
       
        public cubo(String nombre_archivo) {

           datos = new Fits(nombre_archivo);

  
        }
    }
}
