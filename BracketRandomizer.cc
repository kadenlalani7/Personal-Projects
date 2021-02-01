#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include<cmath>

using namespace std;

//Program Description:
//Give N number of totalTeams and a decision between tournamnet or league play,
//creates a list of names put them into a vector list. Then the list is randomized
//given a safe quanitity check and produces the brakcet or league match ups in a
//simple neat print format

void printList();
void shuffleTeams();
bool is2n(int);
void printBracket();
void leaguePlay();
void tournamentPlay();

struct team
{
  string name;
  int teamNum;
  team* next;

};

vector <team*> teamList;

int main()
{
  int mode = 0;
  cout << "Make a League or Tournament? (Press 1 for League 2 for Tournament)" << endl;
  cin >> mode; //Mode 1 is for League mode 2 is for Tournament
  if(mode == 1)
  {
      leaguePlay();
  }
  else if(mode == 2)
  {
      tournamentPlay();
  }
  else
  {
      cout << "Invalid Game Mode." << endl; //Error Invalid mode warning
      return 0;
  }
}

void tournamentPlay()
{
  int totalTeams;
  cout << "How many teams? " << endl;
  cin >> totalTeams;
  for (int i = 0; i < totalTeams; i++) //add the teams to a vector list
  {
    team* tempAdd = new team();
    cout << "Team " << i+1 << " name: ";
    cin >> tempAdd->name;
    tempAdd->teamNum = i+1;

    teamList.push_back(tempAdd);
  }
  random_shuffle(teamList.begin(), teamList.end()); //shuffle the teams

  bool flag1 = is2n(totalTeams);
  if (flag1) //checks the quanitity of teams is elligible for a torunament
  {
    printBracket();
  }

  return;
}

void leaguePlay()
{
    int totalTeams;
    int weeks;
    cout << "How many teams? " << endl;
    cin >> totalTeams;
    cout << "How long is the season? (In weeks)" << endl;
    cin >> weeks;
    for (int i = 0; i < totalTeams; i++) //add the teams to a vector list
    {
      team* tempAdd = new team();
      cout << "Team " << i+1 << " name: ";
      cin >> tempAdd->name;
      tempAdd->teamNum = i+1;

      teamList.push_back(tempAdd);
    }

    random_shuffle(teamList.begin(), teamList.end()); //shuffle the teams

    for(int i = 0; i < weeks; i++)
    {
     cout << endl << "-----WEEK " << i+1 << "-----" << endl;
     printBracket(); //print the weekly match ups
     random_shuffle(teamList.begin(), teamList.end()); //reshuffle teams
    }

    return;
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
      cout << "Match " << matchCount << ": " << endl;
      matchCount++;
    }
    cout << "Team " << teamList.at(i)->teamNum << " name: "
    << teamList.at(i)->name << endl;
  }

}
