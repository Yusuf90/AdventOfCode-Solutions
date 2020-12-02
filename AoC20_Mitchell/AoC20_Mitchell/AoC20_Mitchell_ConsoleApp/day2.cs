using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC20_Mitchell_ConsoleApp
{
    public static class Day2
    {
        private static string[] Input = System.IO.File.ReadAllLines(@"../AoC20_Mitchell_ConsoleApp/inputday2.txt");

        public static void Day2b()
        {
            var passwordGroups = MapInputToModel(Input);

            foreach (var item in passwordGroups)
            {
                if (item.Password.Length > item.Max - 1)
                {
                    var firstValue = item.Password[item.Min - 1].ToString();
                    var secondValue = item.Password[item.Max - 1].ToString();

                    if ((firstValue == item.Character && secondValue != item.Character) || (firstValue != item.Character && secondValue == item.Character))
                    {
                        item.correct = true;
                    }
                    else
                    {
                        item.correct = false;
                    }
                }
            }

            var answer = passwordGroups.Where(pg => pg.correct == true).ToList().Count();

            System.Console.WriteLine("Day 2b: " + answer);
        }

        public static void Day2a()
        {
            var passwordGroups = MapInputToModel(Input);

            foreach (var item in passwordGroups)
            {
                int amount = 0;

                for (int i = 0; i < item.Password.Length; i++)
                {
                    if (item.Password[i].ToString() == item.Character)
                    {
                        amount = amount + 1;
                    }
                }

                if (amount >= item.Min && amount <= item.Max)
                {
                    item.correct = true;
                }
                else
                {
                    item.correct = false;
                }
            }

            var answer = passwordGroups.Where(pg => pg.correct == true).ToList().Count();

            System.Console.WriteLine("Day 2a: " + answer);
        }

        private static List<PasswordGroup> MapInputToModel(string[] input)
        {
            var passwordGroups = new List<PasswordGroup>();

            foreach (var item in input)
            {
                var min = Int32.Parse(item.Substring(0, item.IndexOf("-")));
                var max = Int32.Parse(item.Substring(item.IndexOf("-") + 1, item.IndexOf(" ") - item.IndexOf("-")));
                var character = item.Substring(item.IndexOf(":") - 1, 1);
                var password = item.Substring(item.IndexOf(":") + 2, item.Length - (item.IndexOf(":") + 2));
                var passwordGroup = new PasswordGroup(min, max, character, password);
                passwordGroups.Add(passwordGroup);
            }

            return passwordGroups;
        }
    }

    public class PasswordGroup
    {
        public int Min { get; set; }
        public int Max { get; set; }
        public string Character { get; set; }
        public string Password { get; set; }
        public bool? correct = null;

        public PasswordGroup(int min, int max, string character, string password)
        {
            Min = min;
            Max = max;
            Character = character;
            Password = password;
        }
    }
}

