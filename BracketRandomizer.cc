#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include<cmath>

using namespace std;

void printList();
void shuffleTeams();
bool is2n(int);
void printBracket();

struct team
{
  string name;
  int teamNum;
  team* next;

};
//Program Description:
//Give N number of totalTeams
//get a list of names
//put them into an array
//randomize the array
//safe quanitity check
//produce brakcet
//pretty print
vector <team*> teamList;

int main()
{
  int totalTeams;
  cout << "How many teams? " << endl;
  cin >> totalTeams;
  for (int i = 0; i < totalTeams; i++)
  {
    team* tempAdd = new team();
    cout << "Team " << i+1 << " name: ";
    cin >> tempAdd->name;
    tempAdd->teamNum = i+1;

    teamList.push_back(tempAdd);
  }
  //printList();
  cout << endl;

  random_shuffle(teamList.begin(), teamList.end());
  //printList();
  cout << endl;

  bool flag1 = is2n(totalTeams);
  if (flag1)
  {
    printBracket();
  }



  return 0;
}

void printList()
{
  for (int i = 0; i < teamList.size(); i++)
  {
    cout << "Team " << teamList.at(i)->teamNum << " name: "
    << teamList.at(i)->name << endl;
  }
}

bool is2n(int n)
{
  for (int i = 0; i < 7; i++)
  {
    if (n == pow(2, i))
    {
      return true;
    }
  }

  return false;
}

void printBracket()
{
  int matchCount = 1;
  for (int i = 0; i < teamList.size(); i++)
  {
    if (0 || i%2 == 0)
    {
      cout << endl << "Match " << matchCount << ": " << endl;
      matchCount++;
    }
    cout << "Team " << teamList.at(i)->teamNum << " name: "
    << teamList.at(i)->name << endl;
  }

}
