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

            long n = h.DataSize;

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
            ImageHDU h = (ImageHDU)f.ReadHDU();

            ImageTiler t = h.Tiler;

            float[] tile = new float[50 * 50];
            t.GetTile(tile, new int[] { 100, 100 }, new int[] { 40, 40 });

            Console.ReadKey();

        }
    }
}
