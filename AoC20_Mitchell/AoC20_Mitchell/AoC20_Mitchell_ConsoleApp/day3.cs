using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC20_Mitchell_ConsoleApp
{
    public static class Day3
    {
        private static string[] Input = System.IO.File.ReadAllLines(@"../AoC20_Mitchell_ConsoleApp/inputday3.txt");

        public static void Day3a() 
        {
            var position = 3;
            var trees = 0;

            for (int i = 0; i < Input.Length - 1; i++)
            {
                var line = Input[i+1];
                var stop = line[position].ToString();
                var steps = 3;
                var tree = "#";

                if (stop == tree) 
                {
                    trees = trees + 1;
                }

                if (position + steps >= line.Length) 
                {
                    position = steps - (line.Length - position);
                } else {
                    position = position + 3;
                } 
            }

            System.Console.WriteLine(trees);
        } 
    }
}