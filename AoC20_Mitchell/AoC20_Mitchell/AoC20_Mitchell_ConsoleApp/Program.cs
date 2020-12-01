using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC20_Mitchell_ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Fakka World!");
            Day1a();
            Day1b();
        }

        static void Day1a()
        {
            string[] values = System.IO.File.ReadAllLines(@"C:\Users\MIWI\Desktop\REPOS\AdventOfCode-OtisRefsThug\AoC20_Mitchell\AoC20_Mitchell\AoC20_Mitchell_ConsoleApp\inputday1.txt");
            List<int> valuesList = values.ToList().Select(val => Int32.Parse(val)).ToList();

            int sum;
            bool go = true;

            while(go)
            {
                for (int i = 0; i < valuesList.Count; i++)
                {
                    var value = valuesList[i];

                    for (int x = i + 1; x < valuesList.Count; x++)
                    {
                        int summed = value + valuesList[x];

                        if (summed == 2020)
                        {
                            sum = value * valuesList[x];
                            Console.WriteLine("Day 1a solution: " + sum);
                            go = false;
                        }
                    }
                }
            }
        }

        static void Day1b()
        {
            string[] values = System.IO.File.ReadAllLines(@"C:\Users\MIWI\Desktop\REPOS\AdventOfCode-OtisRefsThug\AoC20_Mitchell\AoC20_Mitchell\AoC20_Mitchell_ConsoleApp\inputday1.txt");
            List<int> valuesList = values.ToList().Select(val => Int32.Parse(val)).ToList();

            int sum;
            bool go = true;

            while (go)
            {
                for (int i = 0; i < valuesList.Count; i++)
                {
                    var valueOne = valuesList[i];

                    for (int x = i + 1; x < valuesList.Count; x++)
                    {
                        var valueTwo = valuesList[x];

                        for (int z = x + 1; z < valuesList.Count; z++)
                        {
                            var valueThree = valuesList[z];

                            if (valueOne + valueTwo + valueThree == 2020)
                            {
                                sum = valueOne * valueTwo * valueThree;
                                Console.WriteLine("Day 1b solution: " + sum);
                                go = false;
                            }
                        }
                    }
                }
            }
        }
    }
}
