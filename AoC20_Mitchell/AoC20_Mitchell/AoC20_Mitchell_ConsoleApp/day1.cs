using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC20_Mitchell_ConsoleApp
{
    public static class day1
    {
        public static void Day1sexy()
        {
            string[] values = System.IO.File.ReadAllLines(@"../AoC20_Mitchell_ConsoleApp/inputday1.txt");
            List<int> valueList = values.ToList().Select(val => Int32.Parse(val)).ToList();

            int solution1a = checkValuesDay1a(valueList, new List<int>(valueList), 0);
            System.Console.WriteLine("Day 1a sexy solution: " + solution1a);
        }

        private static int checkValuesDay1a(List<int> valueList, List<int> comparedList, int index)
        {
            var value = valueList[index] + comparedList[comparedList.Count - 1];

            if (value != 2020 && comparedList.Count > 1)
            {
                comparedList.RemoveAt(comparedList.Count - 1);
                return checkValuesDay1a(valueList, comparedList, index);
            }
            else if (comparedList.Count == 1)
            {
                return checkValuesDay1a(valueList, new List<int>(valueList), index + 1);
            }
            else if (value == 2020)
            {
                return valueList[index] * comparedList[comparedList.Count - 1];
            }
            else
            {
                return 0;
            }
        }

        public static void Day1a()
        {
            string[] values = System.IO.File.ReadAllLines(@"../AoC20_Mitchell_ConsoleApp/inputday1.txt");
            List<int> valuesList = values.ToList().Select(val => Int32.Parse(val)).ToList();

            int sum;
            bool go = true;

            while (go)
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

        public static void Day1b()
        {
            string[] values = System.IO.File.ReadAllLines(@"../AoC20_Mitchell_ConsoleApp/inputday1.txt");
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
