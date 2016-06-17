using nom.tam.fits;
using nom.tam.util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using nom.tam.image;

namespace ConsoleApplication2 {

    class Program {

        static void Main(string[] args) {

            String salida = "";
            Console.WriteLine("Probando lectura");

            /*Lectura parcial y automatica de parte de cabezera*/

            /*Fits f = new Fits("cubo_ing_comp.fits");

            BasicHDU[] hdus = f.Read();

            Console.WriteLine("Longitud: " + hdus.Length);

            for (int i = 0; i < hdus.Length; i += 1) {
                hdus[i].Info();
            }

           f.Close();*/

            /*Lectura mayor y manual de parte de cabezera*/

            /*BufferedFile bf = new BufferedFile("cubo_ing_comp.fits", FileAccess.Read,FileShare.None);
            Header h = Header.ReadHeader(bf);
            Console.WriteLine(h.GetCard(155)); //Obtener las propiedades des header numericamente
            Console.WriteLine("HEADER SIZE: "+h.DataSize);

            Console.WriteLine("SIMPLE: " + h.GetBooleanValue("SIMPLE"));
            Console.WriteLine("BITPIX: " + h.GetIntValue("BITPIX"));

            int naxes = h.GetIntValue("NAXIS");

            Console.WriteLine("NAXIS: "+naxes);

            for (int i = 1; i <= naxes;i++) {

                salida = "NAXIS" + i;
                Console.WriteLine(salida+" : "+ h.GetIntValue(salida));
            }

            Console.WriteLine("DATAMIN: " + h.GetFloatValue("DATAMIN"));
            Console.WriteLine("DATAMAX: " + h.GetFloatValue("DATAMAX"));
            Console.WriteLine("ORIGIN: " + h.GetStringValue("ORIGIN"));
            Console.WriteLine("DATE: " + h.GetStringValue("DATE"));
            Console.WriteLine("NEXTEND: " + h.GetFloatValue("NEXTEND"));
            Console.WriteLine("FILENAME: " + h.GetStringValue("FILENAME"));
            Console.WriteLine("OBJECT: " + h.GetStringValue("OBJECT"));
            Console.WriteLine("EXPTIME: " + h.GetFloatValue("EXPTIME"));
            Console.WriteLine("DARKTIME: " + h.GetFloatValue("DARKTIME"));
            Console.WriteLine("PREFLASH: " + h.GetStringValue("PREFLASH"));
            Console.WriteLine("RADECSYS: " + h.GetStringValue("RADECSYS"));
            Console.WriteLine("RADECEQ: " + h.GetFloatValue("RADECEQ"));
            Console.WriteLine("RA: " + h.GetStringValue("RA"));
            Console.WriteLine("DEC: " + h.GetStringValue("DEC"));
            Console.WriteLine("TIMESYS: " + h.GetStringValue("TIMESYS"));
            Console.WriteLine("DATE-OBS: " + h.GetStringValue("DATE-OBS"));
            Console.WriteLine("TIME-OBS: " + h.GetStringValue("TIME-OBS"));
            Console.WriteLine("MJD-OBS: " + h.GetFloatValue("MJD-OBS"));
            Console.WriteLine("MJDHDR: " + h.GetFloatValue("MJDHDR"));
            Console.WriteLine("LSTHDR: " + h.GetStringValue("LSTHDR"));
            Console.WriteLine("OBSERVAT: " + h.GetStringValue("OBSERVAT"));
            Console.WriteLine("TELESCOP: " + h.GetStringValue("TELESCOP"));
            Console.WriteLine("INSTRUME: " + h.GetStringValue("INSTRUME"));
            Console.WriteLine("TELRADEC: " + h.GetStringValue("TELRADEC"));
            Console.WriteLine("IMAGENUM: " + h.GetStringValue("IMAGENUM"));
            Console.WriteLine("TELEQUIN: " + h.GetStringValue("TELEQUIN"));
            Console.WriteLine("...");
            Console.WriteLine("FLATFILE: " + h.GetStringValue("FLATFILE"));

            bf.Close();*/

            /*Lectura imagen en matriz*/

            Fits f = new Fits("cubo_ing_comp.fits");

            ImageHDU hdu = (ImageHDU)f.GetHDU(0);


            ImageHDU h = (ImageHDU)f.ReadHDU();

            try {

                Console.WriteLine("Estoy aqui");
                // float[,,] img = (float[,,])h.Kernel;
                //float[,,] img = (float[,,])hdu.Kernel;

                float[] img = (float[])hdu.Kernel;

                Console.WriteLine("valor:"+img[10]);
                
               // Console.WriteLine("datos imagen"+img[15, 20, 10]);
                Console.WriteLine("Estoy aca");
            } catch (NullReferenceException e) {
                e.GetBaseException();
            }

            int[,,] threeDimensional = new int[3, 5, 4];
            threeDimensional[0, 0, 0] = 1;
            threeDimensional[0, 1, 0] = 2;
            threeDimensional[0, 2, 0] = 3;
            threeDimensional[0, 3, 0] = 4;
            threeDimensional[0, 4, 0] = 5;
            threeDimensional[1, 1, 1] = 2;
            threeDimensional[2, 2, 2] = 3;
            threeDimensional[2, 2, 3] = 4;

            // Loop over each dimension's length.
            for (int i = 0; i < threeDimensional.GetLength(2); i++) {
                for (int y = 0; y < threeDimensional.GetLength(1); y++) {
                    for (int x = 0; x < threeDimensional.GetLength(0); x++) {
                        Console.Write(threeDimensional[x, y, i]);
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }

            /*BasicHDU bs = f.GetHDU(0);

            Data datos = bs.Data;

            float[,,] cubo = (Data) datos.DataArray;


            hdu.Data;
           
            ImageTiler tiler = hdu.Tiler;
            float[] tile = new float[50 * 50];

            try {
                tiler.GetTile(tile, new int[] { 200, 200 }, new int[] { 50, 50 });
            } catch (IndexOutOfRangeException e) {
                Console.WriteLine(e.GetBaseException());
                Console.WriteLine("Mensaje de error: "+e.Message);
            }
           */


            //ImageHDU h = (ImageHDU)f.ReadHDU();
            
            ImageData image = new ImageData(f);
            float[][][] foto = (float[][][]) image.DataArray;

            Console.WriteLine("foto = "+foto[0][0][0]);
            // h.Info();
            //f.GetHDU(0);
            //ImageTiler t = h.Tiler;

            /*float[] tile = new float[50 * 50];
            t.GetTile(tile, new int[] { 100, 100 }, new int[] { 40, 40 });*/

            Console.ReadKey();
        }
    }
}
