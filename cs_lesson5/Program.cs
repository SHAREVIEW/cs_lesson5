using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cs_lesson5  //溢出检查
{
    class Program
    {
        static void Main(string[] args)
        {
            byte destinationVar;
            short sourceVar = 281;
            destinationVar = checked((byte)sourceVar);            //checked,unchecked 表达式的溢出检查上下文
            Console.WriteLine("sourceVar val:{0}",sourceVar);
            Console.WriteLine("destinationVar val:{0}",destinationVar);
            Console.ReadKey();

            /*
              281 = 100011001
              25  = 000011001
              255 = 011111111 
           */
            

        }
    }
}
